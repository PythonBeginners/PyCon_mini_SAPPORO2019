import pyocr
import pyocr.builders

# PyOCRの初期化
def pyocr_init ():
    tools = pyocr.get_available_tools() # OCRツールの有無の確認
    if len(tools) == 0:
        print("No OCR tool found")

    # OCRツールを列挙してみる
    print(f"pyocr tools count = {len(tools)}")
    for tool_id in range(len(tools)):
        print(f"tool[{tool_id}].tool.get_name() = " + tools[tool_id].get_name())

    pyocr_tool = tools[0]
    print("use tool =" + (pyocr_tool.get_name()))

    langs = pyocr_tool.get_available_languages() # 使用できる言語の確認
    print("pyocr langs  = " + ", ".join(langs))
    
    return pyocr_tool