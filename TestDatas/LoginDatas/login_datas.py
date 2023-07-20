# 正常场景测试数据
success_data = {'name': '登录功能-正常测试', 'username': '00005907', 'password': 'Jxtr!2023'}

# 异常场景测试 - username
error_usernameFormat_data = [
    {'name': '登录功能-异常测试-用户名为空', 'username': '', 'password': 'a123456', 'errorMsg': '用户名密码不能为空'},
    {'name': '登录功能-异常测试-用户名不存在', 'username': 'xxoo', 'password': 'a123456', 'errorMsg': '用户名或密码错误'},
]

# 异常场景测试 - password
error_passwordFormat_data = [
    {'name': '登录功能-异常测试-密码为空', 'username': 'admin', 'password': '', 'errorMsg': '用户名密码不能为空'},
    {'name': '登录功能-异常测试-密码错误', 'username': '00056062', 'password': '1234567', 'errorMsg': '用户名或密码错误'},
]
