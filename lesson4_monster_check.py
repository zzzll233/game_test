# 怪物列表
monster_names = ["哥布林", "兽人", "骷髅兵", "食人魔", "巨魔", "狼人", "吸血鬼", "精灵", "恶魔", "巨龙"]

print("欢迎来到怪物检查程序！")
print(monster_names[0]) # 第一个怪物
print(monster_names[-1]) # 最后一个怪物
print(len(monster_names)) # 怪物总数

monsters_data = [
    {"name": "史莱姆", "hp": 50, "attack": 10, "level": 2},
    {"name": "哥布林", "hp": 80, "attack": 15, "level": 3},
    {"name": "巨龙", "hp": 200, "attack": 50, "level": 10},
    {"name": "精灵", "hp": -5, "attack": 20, "level": 4},   # 故意放一个异常血量
    {"name": "骷髅兵", "hp": 60, "attack": -3, "level": 0}    # 攻击力异常
]

print("======怪物配置校验======")
error_details = []
for monster in monsters_data:
    errors = []
    if monster["hp"] <= 0:
       errors.append(f"血量异常{monster['hp']}")
    if monster["attack"] <= 0:
        errors.append(f"攻击力异常{monster['attack']}")
    if monster["level"] <= 0:
        errors.append(f"等级异常{monster['level']}")

    if errors:
        error_details.append({"name": monster["name"], "errors": errors})
        
if not error_details:
    print("所有怪物配置正常。")
else:
    print("异常怪物详情：")
    for detail in error_details:
        print(f"怪物名称: {detail['name']}, 异常信息: {', '.join(detail['errors'])}")   