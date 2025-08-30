# 分形树 Fractal Tree

用递归算法绘制一棵可交互的分形树：支持自定义分支次数、每次分支的数量以及分支角度（角度制或弧度制）。

## 运行环境

- Python == 3.11.6
- 依赖见 [`requirements.txt`](./requirements.txt)

## 快速开始

预览体验：[`https://jessssssseea.github.io/GanEnyues_mission/`](https://jessssssseea.github.io/GanEnyues_mission/)

1. 克隆或下载本仓库  
2. 安装依赖  
   ```bash
   pip install -r requirements.txt
   ```
3. 运行  
   ```bash
   python main.py
   ```
4. 按提示输入参数：  
   - **分支次数**  
   - **每次分支的数量**  
   - **角度单位**（`d` = 度制，`r` = 弧度制）  
   - **分支角度**  
     - 度制可输入 `30`、`31/23` 等  
     - 弧度制可输入 `pi/3`、`2*pai/5` 等  

程序会弹出窗口显示生成的分形树。关闭窗口即可结束程序。

## 示例参数

| 分支次数 | 分支数量 | 单位 | 角度  | 效果         |
|----------|----------|------|-------|--------------|
| 8        | 2        | d    | 30    | 经典二叉分形 |
| 5        | 3        | r    | pi/4  | 三叉雪花状   |
| 6        | 1        | d    | 0     | 直线干       |

## 文件说明

- `main.py` – 主程序  
- `requirements.txt` – 依赖列表  
- `README.md` – 本文档  

## 许可证

MIT License，可自由使用与修改。