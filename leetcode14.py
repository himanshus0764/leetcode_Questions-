strs = ["flower", "flow", "flight"]
st = ''
duplicate = ''

for i in strs:
    for j in i:
        st += j

for i in range(len(st)):
    if st.count(st[i]) > 2 and st[i] not in duplicate:
        duplicate += st[i]

print(duplicate)
