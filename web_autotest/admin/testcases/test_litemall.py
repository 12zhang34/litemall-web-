import pytest

from web_autotest.admin.page_object.login_page import LoginPage

@pytest.fixture(scope='class')
def home():
    home_page = LoginPage().login()
    yield  home_page
    home_page.do_quit()

class TestLiteMall:

     @pytest.mark.parametrize("category_id, category_name", [("1499288", "行李箱"), ("1499286", "书包"), ("1499299", "课本")])
     def test_add_type(self, home, category_id, category_name):
         list_page = home\
             .go_to_category()\
             .click_add()\
             .create_category(category_id, category_name)
         res = list_page.get_operate_result()
         assert "成功" in res
         list_page.delete_category(category_name)

     @pytest.mark.parametrize("category_id, category_name", [("1499288", "行李箱"), ("1499286", "书包"), ("1499299", "课本")])
     def test_delete_type(self, home, category_id, category_name):
         res = home\
             .go_to_category()\
             .click_add()\
             .create_category(category_id, category_name)\
             .delete_category(category_name)\
             .get_delete_result()
         assert "成功" in res
