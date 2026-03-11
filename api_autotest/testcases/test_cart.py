import pytest

from api_autotest.apis.admin.goods import Goods
from api_autotest.apis.wx.cart import Cart


class TestCart():
    def setup_class(self):
        self.goods = Goods("https://litemall.hogwarts.ceshiren.com/", "admin")
        self.cart = Cart("https://litemall.hogwarts.ceshiren.com/", "client")

    # def teardown(self):
        # self.goods.delete(self.goods_id)

    @pytest.mark.parametrize("goods_name", ["AD741", "AD852", "AD963"])
    def test_add_cart(self, goods_name):
        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "123456",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "99", "number": "666", "url": ""}],
            "attributes": []}
        self.goods.create(goods_data)
        goods_list_r = self.goods.list(goods_name)
        self.goods_id = goods_list_r["data"]["list"][0]["id"]
        goods_detail_r = self.goods.detail(self.goods_id)
        product_id = goods_detail_r["data"]["products"][0]["id"]
        res = self.cart.add(self.goods_id, product_id)
        assert res["errmsg"] == "成功"
        self.goods.delete(self.goods_id)
