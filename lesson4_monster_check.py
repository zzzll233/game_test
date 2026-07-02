# 怪物列表
monsters = ["哥布林", "兽人", "骷髅兵", "食人魔", "巨魔", "狼人", "吸血鬼", "精灵", "恶魔", "巨龙"]

print("欢迎来到怪物检查程序！")
print(monsters[0]) # 第一个怪物
print(monsters[-1]) # 最后一个怪物
print(len(monsters)) # 怪物总数

monsters = [
    {"name": "史莱姆", "hp": 50, "attack": 10, "level": 2},
    {"name": "哥布林", "hp": 80, "attack": 15, "level": 3},
    {"name": "巨龙", "hp": 200, "attack": 50, "level": 10},
    {"name": "精灵", "hp": -5, "attack": 20, "level": 4},   # 故意放一个异常血量
    {"name": "骷髅兵", "hp": 60, "attack": -3, "level": 1}    # 攻击力异常
]

print