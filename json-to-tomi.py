import toml
import json

# 입력 및 출력 파일 경로
input_file = "secrets.json"
output_file = ".streamlit/secrets.toml"

# JSON 파일을 읽어와서 문자열로 변환
with open(input_file) as json_file:
    json_data = json.load(json_file)  # JSON 파일을 파싱하여 dict 객체로 변환

# JSON 데이터를 TOML 형식으로 변환
toml_config = toml.dumps(json_data)

# TOML 형식으로 변환된 데이터를 파일에 작성
with open(output_file, "w") as target:
    target.write(toml_config)
