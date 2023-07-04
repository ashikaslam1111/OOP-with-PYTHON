def fullName(f, l, **ad):
    name = f"{f} {l} {ad}"
    for k, v in ad.items():
        print(k, v)
    return name


name = fullName(f='ashik', l='aslam', t='md')
print(name)
