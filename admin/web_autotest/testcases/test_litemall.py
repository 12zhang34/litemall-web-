import pytest

from admin.web_autotest.page_object.login_page import LoginPage


class TestLiteMall:
     def setup_class(self):
         self.home = LoginPage().login()

     def teardown_class(self):
          self.home.do_quit()

     @pytest.mark.parametrize("category_id, category_name", [("1499288", "行李箱"), ("1499286", "书包"), ("1499299", "课本")])
     def test_add_type(self, category_id, category_name):
         list_page = self.home\
             .go_to_category()\
             .click_add()\
             .create_category(category_id, category_name)
         res = list_page.get_operate_result()
         assert "成功" in res
         list_page.delete_category(category_name)

     @pytest.mark.parametrize("category_id, category_name", [("1499288", "行李箱"), ("1499286", "书包"), ("1499299", "课本")])
     def test_delete_type(self, category_id, category_name):
         res = self.home\
             .go_to_category()\
             .click_add()\
             .create_category(category_id, category_name)\
             .delete_category(category_name)\
             .get_delete_result()
         assert "成功" in res
