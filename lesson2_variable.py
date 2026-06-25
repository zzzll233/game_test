# 角色属性
role_name = "野蛮人"
level = 5
hp =320
attack = 45
defense = 20

# 像测试报告一样打印它们

print("=======角色信息校验======")
print("名字：", role_name)
print("等级：", level)
print("血量：", hp)
print("攻击力：", attack)
print("防御力：", defense)

# 简单校验：血量是否大于0？
if hp > 0:
    print("✅ 血量正常")
else:
    print("❌ 血量异常！")
    
if attack > 0:
    print("✅ 攻击力正常")
else:
    print("❌ 攻击力异常！")