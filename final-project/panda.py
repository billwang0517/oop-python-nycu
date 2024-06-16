import pandas as pd
import json
import matplotlib.pyplot as plt

# 读取JSON文件并将其转换为字典列表
with open('./oop-python-nycu/final-project/player_data.json', 'r') as f:
    data = json.load(f)

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 计算每个玩家的跳跃次数、射击次数和炸弹次数的平均值
player1_jump_mean = df['player1_jump_count'].mean()
player1_shoot_mean = df['player1_shoot_count'].mean()
player1_bomb_mean = df['player1_bomb_count'].mean()

player2_jump_mean = df['player2_jump_count'].mean()
player2_shoot_mean = df['player2_shoot_count'].mean()
player2_bomb_mean = df['player2_bomb_count'].mean()

# 计算每个玩家的跳跃次数、射击次数和炸弹次数的标准差
player1_jump_std = df['player1_jump_count'].std()
player1_shoot_std = df['player1_shoot_count'].std()
player1_bomb_std = df['player1_bomb_count'].std()

player2_jump_std = df['player2_jump_count'].std()
player2_shoot_std = df['player2_shoot_count'].std()
player2_bomb_std = df['player2_bomb_count'].std()

# 绘制折线图：每个玩家的跳跃次数、射击次数和炸弹次数
plt.figure(figsize=(12, 8))

# Player 1
plt.plot(df.index, df['player1_jump_count'], label='Player 1 Jump Count', linestyle='-', marker='o')
plt.plot(df.index, df['player1_shoot_count'], label='Player 1 Shoot Count', linestyle='-', marker='o')
plt.plot(df.index, df['player1_bomb_count'], label='Player 1 Bomb Count', linestyle='-', marker='o')

# Player 2
plt.plot(df.index, df['player2_jump_count'], label='Player 2 Jump Count', linestyle='--', marker='x')
plt.plot(df.index, df['player2_shoot_count'], label='Player 2 Shoot Count', linestyle='--', marker='x')
plt.plot(df.index, df['player2_bomb_count'], label='Player 2 Bomb Count', linestyle='--', marker='x')

plt.xlabel('Game Index')
plt.ylabel('Count')
plt.title('Player Actions Over Games')
plt.legend()
plt.grid(True)
plt.show()

# 绘制条形图：每个玩家的死亡次数对比
plt.figure(figsize=(10, 6))
bar_width = 0.35

# Player 1
plt.bar(df.index - bar_width/2, df['player1_death_count'], bar_width, label='Player 1 Death Count')

# Player 2
plt.bar(df.index + bar_width/2, df['player2_death_count'], bar_width, label='Player 2 Death Count')

plt.xlabel('Game Index')
plt.ylabel('Death Count')
plt.title('Player Death Counts Over Games')
plt.legend()
plt.xticks(df.index)
plt.show()

# 输出每个玩家的平均值和标准差
print("Player 1 Statistics:")
print("  - Jump Mean:", player1_jump_mean)
print("  - Shoot Mean:", player1_shoot_mean)
print("  - Bomb Mean:", player1_bomb_mean)
print("  - Jump Std:", player1_jump_std)
print("  - Shoot Std:", player1_shoot_std)
print("  - Bomb Std:", player1_bomb_std)

print("\nPlayer 2 Statistics:")
print("  - Jump Mean:", player2_jump_mean)
print("  - Shoot Mean:", player2_shoot_mean)
print("  - Bomb Mean:", player2_bomb_mean)
print("  - Jump Std:", player2_jump_std)
print("  - Shoot Std:", player2_shoot_std)
print("  - Bomb Std:", player2_bomb_std)
