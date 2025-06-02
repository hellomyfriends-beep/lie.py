# lie_detector_app.py

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. 데이터 준비
data = {
    'first': [102, 100, 100, 98, 77, 87, 75, 95, 95, 100, 99, 110, 100, 83, 97, 94, 64, 63, 97, 96, 91, 90, 95,
              117, 117, 120, 126, 126, 75],
    'last': [103, 107, 92, 102, 86, 89, 82, 97, 99, 105, 99, 109, 100, 83, 97, 94, 61, 64, 96, 96, 87, 91, 95,
             117, 116, 126, 126, 126, 82],
    'label': ['진실', '거짓', '진실', '진실', '거짓', '진실', '거짓', '진실', '진실', '거짓', '진실', '진실',
              '진실', '진실', '진실', '진실', '거짓', '진실', '진실', '진실', '진실', '진실', '진실',
              '진실', '진실', '진실', '진실', '진실', '거짓']
}

df = pd.DataFrame(data)

# 라벨 인코딩
df['label'] = df['label'].map({'진실': 1, '거짓': 0})

# 2. 모델 학습
X = df[['first', 'last']]
y = df['label']

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 3. Streamlit UI 구성
st.title("⚡찌릿! 진실 혹은 거짓 판별기")
st.markdown("심박수를 입력하면 우리가 만든 AI가 진실인지 거짓인지 알려드려요!")

# 사용자 입력
first = st.number_input("측정 전 심박수 (first)", min_value=40, max_value=200, value=100)
last = st.number_input("측정 후 심박수 (last)", min_value=40, max_value=200, value=105)

# 예측 버튼
if st.button("판별하기!"):
    prediction = model.predict([[first, last]])[0]
    result = "🟢 진실!" if prediction == 1 else "🔴 거짓!"
    st.subheader(f"결과: {result}")
