# app.py

from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

data_values = []

@app.route('/api/data', methods=['POST'])
def process_data():
    data_value = request.json.get('data_value')
    
    # 데이터 값을 리스트에 추가합니다.
    data_values.append(data_value)

    # 데이터를 시각화합니다.
    plt.plot(data_values)
    plt.xlabel("데이터 인덱스")
    plt.ylabel("데이터 값")
    plt.title("데이터 값 변화")

    # 그래프를 이미지로 변환합니다.
    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    return img_data.getvalue(), 200, {'Content-Type': 'image/png'}

if __name__ == '__main__':
    app.run(debug=True)
