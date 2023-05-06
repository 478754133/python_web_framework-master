from selenium.webdriver.common.by import By


class SaleOutboundOrdersLocators:

    #发货出库
    shipoutbound_loc = (By.XPATH,"//button/span[text()='发货出库']")
    #订单出库
    orderoutbound_loc = (By.XPATH,"//button/span[text()='订单出库']")
    #批量入库
    batch_in_loc = (By.XPATH,"//button/span[text()='批量入库']")
    #批量退库
    batch_return_loc = (By.XPATH, "//button/span[text()='批量退库']")
    #出库单打印
    outbound_print_loc = (By.XPATH, "//button/span[text()='出库单打印']")
    #导出出库单
    exportoutbound_loc = (By.XPATH, "//button/span[text()='导出出库单']")
    #导出可拆分结算单
    exportsplitsettlement_loc = (By.XPATH, "//button/span[text()='导出可拆分结算单']")


    #第一个操作下拉图标
    # icon_arrowdown_loc = (By.XPATH,"(//div[5]/div[2]/table/tbody/tr/td[28]/div/div/span/i)[1]")

    #列表选择复选框--全选
    list_checkbox_loc = (By.XPATH, "//*[@id='hcBox']/div/div[2]/div/div[4]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span/span")
    #复选框--选泽第一个
    list_checkbox_loc_1 = (By.CSS_SELECTOR, ".el-table__fixed:nth-child(4) .el-table__row:nth-child(1) .el-checkbox__inner:nth-child(1)")

    #操作编辑按钮
    operatoreditbtn_loc = (By.XPATH, "//div[5]/div[2]/table/tbody/tr[1]/td[22]/div/button[1]/span/i")
    #操作提交按钮
    operatorsubmitbtn_loc = (By.XPATH, "//div[5]/div[2]/table/tbody/tr[1]/td[22]/div/button[2]/span/i")
    #操作审批按钮
    operatorauditbtn_loc = (By.XPATH,"//div[5]/div[2]/table/tbody/tr[1]/td[22]/div/button[3]/span/i")
    #操作删除按钮
    operatordeltebtn_loc = (By.XPATH, "//div[5]/div[2]/table/tbody/tr[1]/td[22]/div/button[4]/span/i")

    #弹框确定按钮
    prompt_comfirm_loc = (By.XPATH,".el-button--small.el-button--primary > span")