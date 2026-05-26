import os


def list_files(path):
    files = {}
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                files[entry.name] = entry.stat().st_size
    return files


def read_bytes(path):
    with open(path, "rb") as f:
        return f.read()


dir1 = input("첫 번째 디렉토리 이름: ")
dir2 = input("두 번째 디렉토리 이름: ")

if not os.path.isdir(dir1) or not os.path.isdir(dir2):
    print("디렉토리가 존재하지 않습니다.")
    raise SystemExit

files1 = list_files(dir1)
files2 = list_files(dir2)

print(f"\n[{dir1}] 파일 수: {len(files1)}")
print(f"[{dir2}] 파일 수: {len(files2)}")

if len(files1) != len(files2):
    print("=> 파일 수가 다릅니다.")
    raise SystemExit

print("=> 파일 수가 같습니다.\n")

names1 = set(files1.keys())
names2 = set(files2.keys())

if names1 != names2:
    print("=> 파일 이름이 일치하지 않습니다.")
    only1 = names1 - names2
    only2 = names2 - names1
    if only1:
        print(f"  {dir1}에만 있음: {sorted(only1)}")
    if only2:
        print(f"  {dir2}에만 있음: {sorted(only2)}")
    raise SystemExit

print("=> 파일 이름이 모두 같습니다.\n")

all_same = True
for name in sorted(names1):
    size1 = files1[name]
    size2 = files2[name]
    path1 = os.path.join(dir1, name)
    path2 = os.path.join(dir2, name)

    if size1 != size2:
        print(f"[{name}] 크기 다름: {size1} vs {size2}")
        all_same = False
        continue

    if read_bytes(path1) != read_bytes(path2):
        print(f"[{name}] 크기는 같지만 내용 다름 ({size1} bytes)")
        all_same = False
    else:
        print(f"[{name}] 동일 ({size1} bytes)")

print()
if all_same:
    print("=> 모든 파일이 이름, 크기, 내용까지 동일합니다.")
else:
    print("=> 일부 파일이 다릅니다.")
