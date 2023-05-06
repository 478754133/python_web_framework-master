from selenium.webdriver.common.by import By


class SaleOrderManagementLocators:
    #新建按钮
    newbuilt_loc = (By.CSS_SELECTOR, ".el-col > .el-button--primary > span")

    #批量删除
    batchdeletebtn_loc = (By.CSS_SELECTOR, "button[title='批量删除']")
    #提示框删除确认-确认
    promptdelete_loc = (By.XPATH,"//div[3]/div/div[3]/button[2]/span")

    #批量作废
    batchcancelbtn_loc = (By.CSS_SELECTOR, "button[title='批量作废']")
    # 提示框作废信息填写
    prompcancelinfotext_loc = (By.CSS_SELECTOR, "textarea[placeholder='请输入内容']")
    # 提示框作废确认-确认
    prompcancelconfirm_loc = (By.CSS_SELECTOR, "(//button/span[text()='确 定'])[3]")

    #批量暂挂
    #批量取消暂挂

    #发货通知
    shipnotice_loc = (By.CSS_SELECTOR, "button[title='发货通知']")

    #直接出库
    directoutbound_loc = (By.CSS_SELECTOR, "button[title='直接出库']")


    #第一个销售订单编号
    firstordercode_loc = (By.XPATH,"//div[3]/table/tbody/tr[1]/td[2]/div/span")
    #第一个客户名称
    firstcutomname_loc = (By.XPATH,"//div[3]/table/tbody/tr[1]/td[3]/div/span")

    #第一个操作下拉图标
    icon_arrowdown_loc = (By.XPATH,"(//div[5]/div[2]/table/tbody/tr/td[28]/div/div/span/i)[1]")

    #销售订单列表选择复选框--全选
    list_checkbox_loc = (By.XPATH, "//*[@id='hcBox']/div/div[2]/div/div[4]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/label/span/span")
    #销售订单复选框--选泽第一个
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









