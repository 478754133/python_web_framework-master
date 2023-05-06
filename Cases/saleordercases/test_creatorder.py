import pytest
import sys
import os
from PageObjects.SaleManagePage.SaleOrderManagementPage.saleorder_page import SaleOrderPage
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)



@pytest.mark.usefixtures('start_session')
@pytest.mark.usefixtures('refresh_page')
class TestCreatOrder:

    #正常用例
    @pytest.mark.lucas
    @pytest.mark.smoke

    def test_savesaleorder_success(self, start_session):

        logger.info("执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info("阴极铜销售订单保存测试用例 ")
        # 前置  访问登录页面
        # 步骤  新建销售订单
        # 断言  状态是否为新建
        start_session[1].savesaleorder_1()
        time.sleep(2)

    def test_submitsaleorder_success(self, start_session):

        logger.info("执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info("阴极铜销售订单保存测试用例 ")
        # 前置  访问登录页面
        # 步骤  新建销售订单
        # 断言  审批状态是否为审批通过
        start_session[1].submitsaleorder_1()


    def test_approvesaleorder_success(self, start_session):

        logger.info("执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info("阴极铜销售订单审批测试用例 ")
        # 前置  访问登录页面
        # 步骤  新建销售订单
        # 断言  审批状态是否为审批通过
        SaleOrderPage(start_session[0]).enterinterface()
        time.sleep(2)
        SaleOrderPage(start_session[0]).auditsaleorder()



