from selenium.webdriver.common.by import By


class LoginLocator:
    username_loc = (By.CSS_SELECTOR, 'input[placeholder="请输入用户名"]')
    password_loc = (By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')
    vcode_loc = (By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]')
    login_btn_loc = (By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]')
    error_msg_loc = (By.CSS_SELECTOR, 'p[class="el-message__content"]')


