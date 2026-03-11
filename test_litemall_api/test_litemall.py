import json

import pytest
import requests

from api_autotest.utils.log_util import logger


class TestLiteMall:
    def setup_class(self):
        #1. 管理端登录接口
        url = "https://litemall.hogwarts.ceshiren.com/admin/auth/login"
        user_data = {"username":"hogwarts","password":"test12345","code":""}
        r = requests.post(url, json=user_data)
        self.token = r.json()["data"]["token"]
        #2. 用户端登录接口
        url = "https://litemall.hogwarts.ceshiren.com/wx/auth/login"
        client_data = {"username":"user123","password":"user123"}
        r = requests.post(url, json=client_data)
        self.client_token = r.json()["data"]["token"]

    def teardown(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
        r = requests.post(url, json={"id": self.goods_id}, headers={"x-litemall-admin-token": self.token})
        logger.debug(f"删除商品的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

    @pytest.mark.parametrize("goods_name", ["AD741", "AD852", "AD963"])
    def test_add_goods(self, goods_name):
        #3. 上架商品接口
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/create"
        good_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "123456",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "99", "number": "666", "url": ""}],
            "attributes": []}
        r = requests.post(url, json=good_data, headers={"x-litemall-admin-token": self.token})
        print(r.json())
        logger.debug(f"上架商品接口的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        #4. 获取商品列表
        goods_list_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        goods_data = {
            "name": goods_name,
            "order": "desc",
            "sort": "add_time"
        }
        r = requests.get(goods_list_url, params=goods_data, headers={"x-litemall-admin-token": self.token})
        self.goods_id = r.json()["data"]["list"][0]["id"]
        logger.debug(f"获取商品列表的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        #5. 获取商品详情接口
        goods_detail_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        r = requests.get(goods_detail_url, params={"id": self.goods_id}, headers={"x-litemall-admin-token": self.token})
        product_id = r.json()["data"]["products"][0]["id"]
        logger.debug(f"获取商品详情接口的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        #6. 添加购物车接口
        url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
        cart_data = {"goodsId":self.goods_id,"number":1,"productId":product_id}
        r = requests.post(url, json=cart_data, headers={"x-litemall-token": self.client_token})
        res = r.json()
        logger.info(f"添加购物车接口的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        assert res["errmsg"] == "成功"