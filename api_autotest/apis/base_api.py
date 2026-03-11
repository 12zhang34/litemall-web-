import json

import requests

from api_autotest.utils.log_util import logger


class BaseApi:
    def __init__(self, base_url, role):
        self.base_url = base_url
        if role:
            self.role = role

    def __set_token(self, request_infos):
        #除登录外每一个接口都需要设置token
        # 1. 管理端登录接口
        admin_url = "admin/auth/login"
        admin_data = {"username": "hogwarts", "password": "test12345", "code": ""}
        r = requests.request("post", self.base_url+admin_url, json=admin_data)
        self.admin_token = {"x-litemall-admin-token": r.json()["data"]["token"]}
        # 2. 用户端登录接口
        client_url = "wx/auth/login"
        client_data = {"username": "user123", "password": "user123"}
        r = requests.request("post", self.base_url+client_url, json=client_data)
        self.client_token = {"x-litemall-token": r.json()["data"]["token"]}
        if self.role == "admin":
            self.final_token = self.admin_token
        else:
            self.final_token = self.client_token

        # 获取headers,如果有有头信息，就更新
        if request_infos.get("headers"):
            request_infos["headers"].update(self.final_token)
        else:
            request_infos["headers"] = self.final_token
        return request_infos

    def send(self, method, url, **kwargs):
        kwargs = self.__set_token(kwargs)
        r = requests.request(method, self.base_url + url, **kwargs)
        logger.debug(f"{url}接口的响应值为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        return r.json()