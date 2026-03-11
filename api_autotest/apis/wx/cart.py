from api_autotest.apis.base_api import BaseApi


class Cart(BaseApi):
    def add(self, goods_id, product_id):
        url = "wx/cart/add"
        cart_data = {"goodsId": goods_id, "number": 1, "productId": product_id}
        r = self.send("post", url, json=cart_data)
        return r