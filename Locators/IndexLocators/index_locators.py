from selenium.webdriver.common.by import By


class IndexLocator:
    #首页
    homepage_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-shouye"]+span'))
    #客商信息
    merchantinfo_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-keshangxinxi"]+span'))
    #基础设置
    basesetting_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-keshangxinxi"]+span'))
    #供应商管理
    suppliermanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-gongyingshangguanli"]+span'))
    #客户管理
    custommanagerment_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-kehuguanli"]+span'))
    #合同管理
    constractmanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-hetongguanli"]+span'))
    #合同管理->销售合同
    constractmanagement_saleconstract_tag = ((By.XPATH,'//span[@class="sub-title menu-item" and text()="销售合同"]'))
    #合同管理->销售合同->销售合同管理
    constractmanagement_saleconstract_sub1_tag = ((By.XPATH, '//li/span[text()="销售合同管理"]'))
    #销售管理
    salemanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-xiaoshouguanli"]+span'))
    #销售管理->销售订单管理
    saleordermanagement_tag = ((By.XPATH, '//span[text()="销售订单管理"]'))
    #销售管理->发货单管理
    saleshipmanagement_tag = ((By.XPATH, '//span[text()="发货单管理"]'))
    # 销售管理->出库单管理
    saleoutboundmanagement_tag = ((By.XPATH, '//span[text()="出库单管理"]'))
    # 销售管理->出库单管理->出库单
    saleoutbound_tag = ((By.XPATH, '//span[text()="出库单"]'))
    #销售管理->结算管理
    salesettlemanage_loc = ((By.XPATH, '(//span[text()="结算管理"])[1]'))
    # 销售管理->结算管理->结算单新增
    salesettleadd_loc = ((By.XPATH, '(//span[text()="结算单新增"])[1]'))
    # 销售管理->结算管理->结算单新增->无点价结算新增
    salesettleadd_2_loc = ((By.XPATH, '//span[text()="无点价结算新增"]'))
    #采购管理
    purchasemanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-caigouguanli"]+span'))
    #采购报表
    purchasereport_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-hetongguanli"]+span'))
    #风控管理
    riskmanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-fengkongguanli"]+span'))
    #价格管理
    pricemanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-jiageguanli"]+span'))
    #库存管理
    storemanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-kucunguanli"]+span'))
    #报关管理
    declaremanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-baoguanguanli"]+span'))
    #运输管理
    transportmanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-yunshuguanli"]+span'))
    #品质管理
    qualitymanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-pinzhiguanli"]+span'))
    #计划管理
    planmanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-jihuaguanli"]+span'))
    #系统管理
    systemmanagement_tag = ((By.CSS_SELECTOR, 'i[class="iconfont aside-icon icon-caidanlan-xitongguanli"]+span'))

    #新建销售合同标签
    newbuildconstract_tag = ((By.CSS_SELECTOR, '//div[text()="新建销售合同"]'))

    # 操作成功
    sucessoperate_prompt = (By.XPATH, "//p[@class='el-message__content' and text()='操作成功']")

    # 删除成功
    sucessdelete_prompt = (By.XPATH, "//p[@class='el-message__content' and text()='删除成功']")

    # 作废成功
    sucesscancel_prompt = (By.XPATH, "//p[@class='el-message__content' and text()='作废成功']")











