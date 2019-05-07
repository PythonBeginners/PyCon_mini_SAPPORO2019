
# textデータ読み込み
def read_text (path:str) -> str:
    y = ""
    with open(path) as f:
        y = f.read()
    return y
