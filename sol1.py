s = 'Ph03nix{n9h1adZ_d03s_n0Z_sTudY_1nf0rm4Z10n_4ssu4r4nc3}'
res = ''
for c in s:
    add = c
    if (c>='a' and c<='z'):
        add = chr((ord(c) - 97 + 7) % 26 + 97)
    else:
        if (c>='A' and c<='Z'):
            add = chr((ord(c) - 65 + 7) % 26 + 65)
    res += add
print(res)