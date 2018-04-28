s = 'Wo03upe{u9o1hka_k03z_u0a_zAbkF_1um0yt4a10u_4zzb4y4uj3}'
#s = 'Wo03upe{u9o1hkG_k03z_u0G_zAbkF_1um0yt4G10u_4zzb4y4uj3}'
print s
amount = ord('W') - ord('P')
pair = [0] * 200
print(pair)
for i in range(300):
    if (i>=65 and i<=90): pair[(i - 65 + 7) % 26 + 65] = i
    if (i>=97 and i<=122): pair[(i - 97 + 7) % 26 + 97] = i
res = ''
print(pair[97])
for c in s:
    add = c
    if ((c>='a' and c<='z') or (c>='A' and c<='Z')):
        add = chr(pair[ord(c)])
    res += add
print res