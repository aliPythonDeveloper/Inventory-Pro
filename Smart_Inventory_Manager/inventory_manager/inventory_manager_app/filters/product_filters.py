import django_filters
from ..models import *


class ProductFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(field_name="product_name", lookup_expr="exact")
    category = django_filters.CharFilter(method='filter_category_hierarchy', label="Category/Subcategory")
    description = django_filters.CharFilter(field_name="description", lookup_expr="exact")
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price_max", lookup_expr="lte")
    suppliers = django_filters.CharFilter(field_name="suppliers", lookup_expr="exact")
    sort_by = django_filters.OrderingFilter(
        fields=(
            ('price', 'price'),  # Sort by price ascending
            ('-price', 'price_desc'),  # Sort by price descending
            ('product_name', 'name_asc'),  # Sort by product name A to Z
            ('-product_name', 'name_desc')  # Sort by product name Z to A
        ),
        label='Sort by'
    )

    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price_min', 'price_max', 'suppliers', "sort_by"]

    def filter_category_hierarchy(self, queryset, name, value):
        category_value = value
        parent_category_value = self.request.GET.get('subcategory', None)
        grandparent_category_value = self.request.GET.get('subsubcategory', None)

        filters = []

        # Add filter for direct category
        if category_value:
            filters.append(queryset.filter(category__category_name__iexact=category_value))

        # Add filter for subcategory
        if parent_category_value:
            filters.append(queryset.filter(category__parent__category_name__iexact=category_value, category__category_name__iexact=parent_category_value))

        # Add filter for subsubcategory
        if grandparent_category_value:
            filters.append(queryset.filter(category__parent__category_name__iexact=parent_category_value, category__category_name__iexact=grandparent_category_value))

        # Combine the filters and return the queryset
        if filters:
            print("filters", filters)
            return filters[0] if len(filters) == 1 else filters[0].union(*filters[1:])
        return queryset


