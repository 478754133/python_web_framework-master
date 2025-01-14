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
class TestCreatConstract:

    #正常用例
    @pytest.mark.lucas
    @pytest.mark.smoke
    #新建合同并保存
    def test_savepurchasecontract_success(self, start_session):

        logger.info("执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info("创建采购合同测试用例 ")
        # 前置  访问登录页面
        # 步骤  新建销售合同
        # 断言  审批状态是否为审批通过
        start_session[1].savepurchaseconstract()
        time.sleep(2)
        try:

            assert IndexPage(start_session[0]).isExist_operatesucess_prompt()
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            time.sleep(2)
            start_session[1].save_pictuer("新建合同成功-正常截图")
        except:
            logger.error(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            time.sleep(2)
            start_session[1].save_pictuer("新建合同失败-异常截图")
            raise



