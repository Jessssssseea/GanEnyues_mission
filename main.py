'''
运行环境：
Python 3.11.6
matplotlib==3.10.5
numpy==2.3.2
'''
import matplotlib.pyplot as plt
import math
import numpy as np
import re

# 中文字体与负号正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ---------- 递归绘制分形树 ----------
def draw_tree(x, y, angle, depth, branch_length, branch_factor, branch_angle):
    """
    递归绘制分形树
    参数:
        x, y           : 起始坐标
        angle          : 当前分支的角度(弧度)
        depth          : 剩余分支次数
        branch_length  : 分支长度
        branch_factor  : 每次分支的数量
        branch_angle   : 分支角度(弧度)
    """
    if depth == 0:
        return

    # 计算当前分支的终点
    x_end = x + branch_length * math.cos(angle)
    y_end = y + branch_length * math.sin(angle)

    # 绘制当前分支
    plt.plot([x, x_end], [y, y_end], color='brown', linewidth=depth * 0.5)

    # 新的分支长度
    new_length = branch_length * 0.8

    # 递归绘制子分支
    if branch_factor == 1:
        draw_tree(x_end, y_end, angle, depth - 1, new_length, branch_factor, branch_angle)
    else:
        angle_range = (branch_factor - 1) * branch_angle
        start_angle = angle - angle_range / 2
        for i in range(branch_factor):
            new_angle = start_angle + i * branch_angle
            draw_tree(x_end, y_end, new_angle, depth - 1, new_length, branch_factor, branch_angle)

# ---------- 通用角度解析 ----------
def parse_angle(expr: str, unit: str) -> float:
    """
    解析角度输入
    unit='d'  -> 角度制，允许分数写法如 31/23
    unit='r'  -> 弧度制，允许分数写法，并支持 'pai' 作为 π
    返回：对应弧度值
    """
    expr = expr.strip().lower()

    if unit == 'd':
        if 'pai' in expr:
            raise ValueError("角度制下不能使用 pai，请直接输入数字或分数")
        # 支持分数
        if '/' in expr:
            m = re.fullmatch(r'\s*(-?\d+(?:\.\d+)?)\s*/\s*(-?\d+(?:\.\d+)?)\s*', expr)
            if not m:
                raise ValueError("分数格式错误")
            return math.radians(float(m.group(1)) / float(m.group(2)))
        return math.radians(float(expr))

    # unit == 'r'
    # 处理 pai
    if 'pai' in expr:
        expr = re.sub(r'\bpai\b', str(math.pi), expr)
    # 支持分数
    if '/' in expr:
        m = re.fullmatch(r'\s*(-?\d+(?:\.\d+)?(?:\.\d+)?(?:\*\d+\.\d+)?)\s*/\s*(-?\d+(?:\.\d+)?)\s*', expr)
        if not m:
            # 使用 eval 处理可能包含 π 的表达式
            pass
    try:
        # 安全求值：仅允许数值与运算符
        value = eval(expr, {"__builtins__": None}, {})
    except Exception:
        raise ValueError("弧度表达式格式错误")
    return float(value)

# ---------- 主程序 ----------
def main():
    # 基础参数
    depth = int(input("请输入分支次数: ")) + 1
    branch_factor = int(input("请输入每次分支的数量: "))

    # 角度单位选择
    unit = input("请输入角度单位 (d=度制, r=弧度制): ").strip().lower()
    while unit not in {'d', 'r'}:
        unit = input("请重新输入 (d=度制, r=弧度制): ").strip().lower()

    # 角度输入
    angle_str = input("请输入分支角度 (度制可写分数如 31/23，弧度制可写 pai/3、2*pai/5 等): ")
    try:
        branch_angle = parse_angle(angle_str, unit)
    except Exception as e:
        print("角度输入不合法:", e)
        return

    # 画布
    plt.figure(figsize=(10, 10))
    angle_display = f"{angle_str}°" if unit == 'd' else f"{angle_str} rad"
    plt.title(f"分形树 (分支次数: {depth - 1}, 分支数量: {branch_factor}, 分支角度: {angle_display})")

    # 绘制
    initial_length = 5.0
    draw_tree(0, 0, math.pi / 2, depth, initial_length, branch_factor, branch_angle)

    # 坐标轴设置
    plt.xlim(-initial_length * 3, initial_length * 3)
    plt.ylim(0, initial_length * 4)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()