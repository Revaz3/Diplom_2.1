import allure

from data import Data
from helpers import Helper
from api import InterfaceApi


class TestGetUserOrdersEndpoint:

    @allure.title('Проверка успешного получения списка заказов конкретного пользователя')
    def test_get_user_orders_success(self, headers_after_login):
        body_1 = Helper.create_body_for_order()
        InterfaceApi.create_order_auth(headers_after_login, body_1)
        body_2 = Helper.create_body_for_order()
        InterfaceApi.create_order_auth(headers_after_login, body_2)
        response = InterfaceApi.get_user_orders_with_auth(headers_after_login)

        assert response.status_code == 200 and len(response.json()['orders']) == 2

    @allure.title('Проверка получения списка заказов неавторизованным пользователем')
    def test_get_user_orders_without_auth(self):
        response = InterfaceApi.get_user_orders_without_auth()
        assert (response.status_code == 401 and response.json()['message'] ==
                Data.TEXT_ERROR_GET_USER_ORDERS_WITHOUT_AUTH)