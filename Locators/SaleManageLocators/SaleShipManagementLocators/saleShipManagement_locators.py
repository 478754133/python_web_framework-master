from selenium.webdriver.common.by import By


class SaleShipOrdersLocators:

    #新建
    newbuild_loc = (By.XPATH,"//button/span[text()='新建']")
    #发货单打印
    shiporder_print_loc = (By.XPATH,"//button/span[text()='发货单打印']")
    #码单导出
    exportcodeorder_loc = (By.XPATH, "//button/span[text()='码单导出']")
    #码单邮件
    emailcodeorder_loc = (By.XPATH, "//button/span[text()='码单邮件']")
    #发送记录
    sendmessage_loc = (By.XPATH, "//button/span[text()='发送记录']")
    #生成运输日计划
    deliveryplan_loc = (By.XPATH, "//button/span[text()='生成运输日计划']")
    #导出
    export_loc = (By.XPATH, "//button/span[text()='导出']")



    #第一个操作下拉图标
    icon_arrowdown_loc = (By.CSS_SELECTOR,"div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_25.operator > div > div > span > i")
    #出库
    generateoutbound_loc = (By.XPATH, "/html/body/ul/li[4]/span")


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