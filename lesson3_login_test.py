# 模拟从数据库取出的账号密码
current_usersname = "tester"
current_password = "123456"


error_count = 0
while error_count < 3:
# 模拟玩家输入
    input_username = input("请输入用户名: ")
    input_password = input("请输入密码: ")

    # 判空处理
    if not input_username or not input_password:
        print("用户名或密码不能为空，请重新输入。")
        continue

    # 验证账号密码是否正确
    if input_username == current_usersname and input_password == current_password:
        print("登录成功！")
        break
    else:
        print("用户名或密码错误，请重新输入。")
        if input_username != current_usersname:
            print("用户名错误。")
        if input_password != current_password:
            error_count += 1
            if error_count == 3:
                print("账户已被锁定，请联系管理员。")
            else:
                 print(f"密码错误，您还有 {3 - error_count} 次机会。")
