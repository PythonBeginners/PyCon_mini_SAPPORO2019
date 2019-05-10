import difflib

# textデータ読み込み
def read_text (path:str) -> str:
    y = ""
    with open(path) as f:
        y = f.read()
    return y

# 一行分のスコア算出
def calc_line_ratio (line1:str, text2:[str]) -> float:
    max_score = -1
    for line2 in text2:
        max_score = max(max_score, difflib.SequenceMatcher(None, line1, line2).ratio())
    
    max_score *= len(line1)
#     print(f"{line1} max_score={max_score}")  # 行ごとのスコアが見たい時はコメントアウトを外して下さい
    return max_score

# 前処理
def preprocessing_text (text1:str) -> [str]:
    result = []
    text1_array = text1.split("\n") # 改行で区切る
    for line1 in text1_array:
        line1 = line1.replace(' ', '') # スペースは削除
        if len(line1) < 1:  # 空文字列の場合は何もしない。
            continue
        result.append(line1)
    return result

# 複数行計算（独自実装）
def calc_text_ratio (text1:str, text2:str) -> float:
    text1_array = preprocessing_text(text1)
    text2_array = preprocessing_text(text2)
    sum_score = 0
    sum_length = 0
    for line1 in text1_array:
        sum_score += calc_line_ratio(line1, text2_array)
        sum_length += len(line1)
        
    if sum_length == 0:
        return 0.0
    return sum_score/sum_length

# tesseractの出力したbox情報から複数行の文字列情報を作成する
def concat_tesseract_boxes_result (tesseract_boxes):
    result = ""
    for box_index in range(len(tesseract_boxes)):
        tesseract_box = tesseract_boxes[box_index]
        result += tesseract_box.content
        result += "\n"
    return result    