import requests

from api_autotest.apis.base_api import BaseApi


class Goods(BaseApi):

    def create(self, goods_data):
        # 3. 上架商品接口
        url = "admin/goods/create"
        r = self.send("post", url, json=goods_data)
        return r

    def list(self, goods_name, order="desc", sort="add_time"):
        goods_list_url = "admin/goods/list"
        goods_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        r = self.send("get", goods_list_url, params=goods_data)
        return r



    def detail(self, goods_id):
        # 5. 获取商品详情接口
        goods_detail_url = "admin/goods/detail"
        r = self.send("get", goods_detail_url, params={"id": goods_id})
        return r

    def delete(self, goods_id):
        url = "/admin/goods/delete"
        r = self.send("post", url, json={"id": goods_id})
        return r
