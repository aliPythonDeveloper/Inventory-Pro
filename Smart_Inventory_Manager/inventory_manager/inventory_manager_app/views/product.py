from django.contrib.admindocs.views import BookmarkletsView
from django.views.generic import ListView, DetailView, UpdateView, CreateView, RedirectView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from ..serializer.product_serializer import *
from ..filters.product_filters import *
from django.utils.translation import gettext_lazy as _
from django.utils.decorators import method_decorator
import json

from ..forms import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from ..decorator.decorator import *


class ProductDRSListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter



class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = context['product']
        related_products = Product.objects.filter(category=product.category).exclude(product_id=product.product_id)[:4]
        context['related_products'] = related_products
        return context


class ProductModelListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/product_list1.html'
    context_object_name = 'products'
    PAGE_TITLE = _('Home Page')
    extra_context = {
        'header_title': PAGE_TITLE,
        'page_title': PAGE_TITLE
    }



    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')
        subsubcategory = self.request.GET.get('subsubcategory')

        if category:
            queryset = Product.objects.filter(category__parent__isnull=True,
                                       category__category_name=category)  # Top-level category
            print('Category: ',len(queryset))
        if subcategory:
            queryset = Product.objects.filter(category__parent__category_name=category,
                                       category__category_name=subcategory)  # Subcategory under the root
        if subsubcategory:
            queryset = Product.objects.filter(category__parent__category_name=subcategory,
                                       category__category_name=subsubcategory)  # Subsubcategory under subcategory

        return queryset



@method_decorator(superuser_required, name='dispatch')
class ProductModelCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductModelCreateForm
    PAGE_TITLE = _('Create Product')
    extra_context = {
        'header_title': PAGE_TITLE,
        'page_title': PAGE_TITLE
    }

    def get_success_url(self):
        return reverse('inventory_manager_app:list')

    def form_valid(self, form):
        # Save the product first
        response = super().form_valid(form)
        product = form.instance  # Get the newly created product

        # Handle the image file (without using form.save())
        if self.request.FILES.get('category_image'):
            category_image = self.request.FILES['category_image']

            # Directly create and save the ProductImage instance
            product_image = ProductImage(product=product, category_image=category_image)
            product_image.save()  # Save the image record

        messages.success(self.request, 'Product and image created successfully!')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        response = super().form_invalid(form)

        # Handle the image form errors as well
        image_form = ProductImageForm(self.request.POST, self.request.FILES)
        if not image_form.is_valid():
            messages.error(self.request, 'There was an error uploading the image.')

        messages.error(self.request, 'There was an error creating the product. Please check the form.')
        return self.render_to_response(self.get_context_data(form=form, image_form=image_form))

    def get_context_data(self, **kwargs):
        # Ensure both product and image forms are available in the context
        context = super().get_context_data(**kwargs)
        if 'image_form' not in context:
            context['image_form'] = ProductImageForm()  # Ensure image form is added to context
        return context

@method_decorator(superuser_required, name='dispatch')
class ProductModelUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product_update.html'
    form_class = ProductModelUpdateForm
    slug_url_kwarg = 'product_slug'

    def get_success_url(self):
        return reverse('inventory_manager_app:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the current product instance
        product = self.get_object()

        # Check if the product has an associated product image
        product_image = ProductImage.objects.filter(product=product).first()

        # Pass the current product image to the context
        if product_image:
            context['image_form'] = ProductImageForm(instance=product_image)
            context['current_image'] = product_image.category_image.url  # Pass current image URL
        else:
            context['image_form'] = ProductImageForm()

        return context

    def form_valid(self, form):
        # Save the product form first
        response = super().form_valid(form)
        product = form.instance  # The updated product instance

        # Fetch the existing product image or create a new one
        product_image = ProductImage.objects.filter(product=product).first()

        if 'delete_image' in self.request.POST and product_image:
            # Delete the current image if the checkbox is checked
            product_image.delete()
            product_image = None  # Set it to None since the image is deleted

        # Handle the image form (if a new image is uploaded)
        if self.request.FILES.get('category_image'):
            print("Category_Image: AM", self.request.FILES.get('category_image'))
            if product_image:
                # Update the existing product image
                product_image.category_image = self.request.FILES['category_image']
            else:
                # Create a new product image if none exists
                product_image = ProductImage(
                    product=product,
                    category_image=self.request.FILES['category_image']
                )
            product_image.save()

        return response

    def form_invalid(self, form):
        # Handle form errors (for both product and image)
        response = super().form_invalid(form)

        image_form = ProductImageForm(self.request.POST, self.request.FILES)

        if not image_form.is_valid():
            messages.error(self.request, 'There was an error uploading the image.')

        return response

@method_decorator(superuser_required, name='dispatch')
class ProductModelDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product_confirm_delete.html'
    slug_url_kwarg = 'product_slug'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def get_success_url(self):
        return reverse('inventory_manager_app:list')


def UpdateProduct(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']


    product = Product.objects.get(product_id=productId)


    if action == 'add':
        product.stock_quantity = (product.stock_quantity + 1)
    if action == "remove":
        product.stock_quantity = (product.stock_quantity - 1)

    product.save()
    print('PRODUCT UPDATE: ',product.stock_quantity)
    if product.stock_quantity <= 0:
        product.delete()

    return JsonResponse('Product Quantity updated', safe=False)


