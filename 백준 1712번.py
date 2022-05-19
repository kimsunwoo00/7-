a,b,c = map(int, input().split())


if b>c:
    print("손익분기점을 계산할 수 없습니다.")
else:
    print(a/(c-b)+1)
