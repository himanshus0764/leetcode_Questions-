heights = [1,1,4,2,1,3]
sortheights=sorted(heights)
count=0
for i in range(len(heights)):
        if heights[i] != sortheights[i]:
            count+=1
print(count)