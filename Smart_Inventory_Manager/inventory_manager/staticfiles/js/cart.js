var updateBtns = document.getElementsByClassName('update-cart');

for(var i=0; i<updateBtns.length; i++){
updateBtns[i].addEventListener('click', function(){
var productId = this.dataset.product;
var actionId = this.dataset.action;
if(user == 'AnonymousUser'){
    console.log('Not logged in')
}else{
        updateUserOrder(productId, actionId)
}
})
}

function updateUserOrder(productId, actionId){
console.log('User is logged in, sending data')
var url = '/cart/update-item/'
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken' : csrftoken,
    },
    body: JSON.stringify({'productId': productId, 'action': actionId}),
})
.then((response) => {
return response.json()
})
.then((data) => {
console.log('data:', data)
location.reload()
})
}