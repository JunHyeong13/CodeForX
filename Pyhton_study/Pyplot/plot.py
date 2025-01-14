import matplotlib.pyplot as plt
import numpy as np 

# # 데이터 설정
# y_values = range(1, 7)
# x_start = [0.25,0,0.85,0,0,0] # 0, 0.25, 0, 0, 0, 0, 0.65, 0, 0, 0.65
# x_end = [0.25, 1, 1, 1, 1, 0.55, 1, 1, 0.55, 1] # 0.25, 1, 1, 1, 1, 0.55, 1, 1, 0.55, 1
# x_lengths = [end - start for start, end in zip(x_start, x_end)]

# # 막대 색상 설정 (파란색)
# color = 'blue'

# # 가로 막대 그래프 생성
# plt.figure(figsize=(8, 6))
# plt.barh(y_values, x_lengths, color=color, edgecolor="black", left=x_start)

# # 축 설정
# plt.xlabel("Time (seconds)")
# plt.ylabel("Items (1-6)")
# plt.xlim(0, 3.8)  # 최대 시간을 조금 더 여유 있게 설정
# plt.ylim(0.5, 6.5)
# plt.xticks(np.arange(0, 3.8, 0.5))
# plt.yticks(y_values)

# # 그래프 제목
# plt.title("Surprised(KSL)")

# # 그래프 표시
# plt.tight_layout()
# plt.show()

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 4))

# Data for the bars
x_labels = ['1', '2', '3', '4', '5', '6']
y_segments = {
    '1': [(0, 1.28),(1.3, 3.4)],
    '2': [(0, 1.48),(1.5, 2.1),(2.15, 2.65),(2.7, 3.4)],
    '3': [(0, 3.4)],
    '4': [(0, 3.4)]
}
# Plot the bars
for i, (label, segments) in enumerate(y_segments.items()):
    for start, end in segments:
        ax.barh(label, end - start, left=start, color='blue')

# Set x and y axis limits
ax.set_xlim(0, 3.5)
ax.set_ylim(-0.5, len(x_labels) - 0.5)

# Add grid and labels
#ax.set_xticks([0, 1, 2, 3, 4]) 
plt.xticks(np.arange(0, 4.0, 0.5))
ax.set_yticks(range(len(x_labels)))
ax.set_yticklabels(x_labels)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Items (1-6)")

# Display the plot
plt.title("Sadness(KSL)")
plt.tight_layout()
plt.show()
