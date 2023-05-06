from selenium.webdriver.common.by import By
class SaleContractCreatLocators:
    '''------组件类按钮提示框-------'''
    #审批通过
    approvebtn_loc = (By.XPATH, "//button/span[text()='审批通过(测试用)']")

    #取消
    cancelbtn_loc = (By.XPATH, "//button/span[text()='取消']")
    #提示取消
    promptbtn_cancel_loc = (By.CSS_SELECTOR, ".el-message-box__btns > button:nth-child(1) > span")

    #预览合同
    preview_loc = (By.XPATH, "//button/span[text()='预览合同']")

    #保存
    savebtn_loc = (By.XPATH, "//button/span[text()='保存']")

    '''-------基本信息-------'''
    #合同名称
    constractname_loc = (By.CSS_SELECTOR, ".is-required > .el-form-item__content > .el-input > .el-input__inner")

    #签约主体

    #合同年份:start:开始年份  end:结束年份
    constractyear_stat_loc = '2023'
    constractyear_end_loc = (By.CSS_SELECTOR, ".el-date-editor:nth-child(3) > .el-input__inner")

    #业务类型:下拉
    businesstype_loc = (By.CSS_SELECTOR, ".el-col:nth-child(4) .el-input:nth-child(1) .el-select__caret")
    #业务类型->一般国内贸易
    businesstype_1_loc = (By.XPATH, "//li[contains(.,'一般国内贸易')]")

    #订单类型:下拉
    ordertype_loc = (By.CSS_SELECTOR, ".el-col:nth-child(5) .el-input:nth-child(1) .el-select__caret")
    #订单类型->产品销售
    ordertype_1_loc = (By.XPATH, "//span[text()='产品销售']")

    #币种:下拉
    currency_loc = (By.CSS_SELECTOR, "input[placeholder='请选择币种']")
    #币种->人民币
    currency_1_loc = (By.XPATH, "//li[contains(.,'人民币元')]")

    #合同有效期:start:开始日期  end:结束日期
    constractduration_start_loc = (By.CSS_SELECTOR, ".is-required .el-date-editor--date:nth-child(1) > .el-input__inner")
    constractduration_end_loc = (By.CSS_SELECTOR, ".is-success .el-date-editor:nth-child(2) > .el-input__inner")

    #收款条件
    collectionterms_loc = (By.CSS_SELECTOR, ".is-required .el-select__input:nth-child(1)")
    #收款条件->货到后付款
    collectionterms_1_loc = (By.XPATH, "//i[contains(.,'货到后付款')]")

    #收款条件说明
    collectiontermsexplain_loc = (By.CSS_SELECTOR, ".el-col:nth-child(9) .el-input__inner")

    #收款方式
    paymentmethod_loc = (By.CSS_SELECTOR, ".el-col:nth-child(10) .el-select__caret")
    #收款方式->电汇
    paymentmethod_1_loc = (By.XPATH, "//span[contains(.,'电汇')]")

    #对方合同编号
    contractnumberother_loc = (By.CSS_SELECTOR, ".el-col:nth-child(11) .el-input__inner")

    #合同签约地点

    #合同执行允差

    #产品大类
    productiontype_loc = (By.CSS_SELECTOR, ".el-col:nth-child(14) .el-select__caret")
    #产品大类—>阴极铜
    productiontype_1_loc = (By.XPATH, "//li/span[text()='阴极铜']")

    #收单地点
    receivinglocation_loc = ''

    #合同类型
    constracttype_loc = (By.CSS_SELECTOR, ".el-col:nth-child(16) .el-select__caret")
    #合同类型->零单合同
    constracttype_1_loc = (By.XPATH, "//span[contains(.,'零单合同')]")

    #标准类型
    standardtype_loc = (By.XPATH, "(//input[@class='el-input__inner' and @readonly='readonly'])[10]")
    #标准类型->非标准合同
    standardtype_1_loc = (By.XPATH, "//span[contains(.,'非标准合同')]")

    #创建人

    #创建部门
    createdepartment_loc = (By.CSS_SELECTOR, ".el-col:nth-child(19) .el-select__caret")
    #创建部门->多金属部门
    createdepartment_1_loc = (By.XPATH, "//li/span[contains(.,'多金属部')]")

    #合同第三方
    #合同摘要

    '''-----------客户信息------------'''
    # 新建客户信息按钮
    addcustominfo_loc = (By.CSS_SELECTOR, ".el-col > .el-button--primary > span")
    #客户信息->客户
    cutomer_loc = (By.XPATH, "(//input[@type='text'])[25]")

    '''-----------产品信息------------'''
    # 新建产品信息新增按钮
    addproductioninfo_loc = (By.CSS_SELECTOR, ".productInfo > .el-button > span")
    #产品信息->物料编码
    materialcode_loc = (By.CSS_SELECTOR, ".el-table__body-wrapper:nth-child(3) .el-table_3_column_37:nth-child(1) .el-input__inner:nth-child(1)")
    #产品信息->物料编码->物料选择->阴极铜
    materialcode_table_loc = (By.CSS_SELECTOR, ".el-tree-node:nth-child(1) .el-tree-node__label")
    #产品信息->物料编码->物料编码搜索栏
    materialcodesearch_loc = (By.CSS_SELECTOR, ".el-col:nth-child(1) > .search-item .el-input__inner")
    #产品信息->物料编码->物料编码查询按钮
    materialcodesearchbtn_loc = (By.CSS_SELECTOR, ".btn-area > .el-button--primary > span")
    #产品信息->物料编码->物料编码被选状态圆点
    materialcodesearchselected_loc = (By.XPATH, "(//div[2]/table/tbody/tr/td/div/label/span/span)[1]")
    #产品信息->物料编码->物料编码确定按钮
    materialcodesearchbtn_confirm_loc = (By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary:nth-child(2) > span")
    #产品信息->数量
    quantity_loc = (By.CSS_SELECTOR, ".el-table__body-wrapper:nth-child(3) .el-table_3_column_45:nth-child(9) .el-input__inner:nth-child(1)")

    '''-----------交货信息------------'''

    '''-----------合同文件及附加信息------------'''
    # 合同文件点击上传
    uploadconstractbtn_loc = (By.XPATH, "(//span[contains(.,'点击上传')])[1]")
    # 合同文件选择模板
    selecttemplate_loc = (By.XPATH, "//span[contains(.,'选择模板')]")
    # 选择模板被选圆点
    selecttemplate_selected_1_loc = (By.CSS_SELECTOR, ".el-table__fixed-body-wrapper .el-table__row:nth-child(1) .el-radio__inner")
    # 选择模板确定按钮
    selecttemplate_confirm_loc = (By.CSS_SELECTOR, "div:nth-child(2) > .el-button--primary:nth-child(2) > span")




















