import pytest
import sys
import os
from PageObjects.SaleContractManagementPage.salecontract_page import SaleConstractPage
from TestDatas.LoginDatas import login_datas as LD
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config
from PageObjects.LoginPage.login_page import LoginPage
import time
from PageObjects.IndexPage.index_page import IndexPage
from Common.plugs.basepage import BasePage
from PageObjects.SaleContractManagementPage.salecontract_page import SaleConstractPage


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(BASE_DIR)
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)


@pytest.mark.usefixtures('start_ses sion')
@pytest.mark.usefixtures('refresh_page')
class TestCancelConstract():
    # 正常用例
    @pytest.mark.lucas
    # 删除列表第一个合同
    def test_cancelsalecontract(self, start_session):
        SaleConstractPage(start_session[0]).enterinterface()
        SaleConstractPage(start_session[0]).cancelconstract()
        try:
            assert IndexPage(start_session[0]).isExist_cancelsucess_prompt()
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("删除合同成功-正常截图")
        except:
            logger.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("删除合同失败-异常截图")
            raise
