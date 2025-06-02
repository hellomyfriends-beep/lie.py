# lie_detector_simple.py

import streamlit as st

# 🎉 제목 및 설명
st.title("⚡찌릿! 진실 or 거짓 판별기")
st.markdown("심박수 변화량으로 간단히 거짓말을 판별해보는 웹서비스입니다!")
st.markdown("우리가 실험을 통해 직접 수집한 데이터를 바탕으로 만든 결과예요 😊")

# 🧾 사용자 입력
st.subheader("📥 심박수 입력")
first = st.number_input("측정 전 심박수 (first)", min_value=40, max_value=200, value=100)
last = st.number_input("측정 후 심박수 (last)", min_value=40, max_value=200, value=105)

# 🧠 간단한 룰 기반 판별
if st.button("🔍 판별하기!"):
    diff = last - first

    # 💡 간단한 기준: 심박수 증가가 5 이상이면 '거짓'이라고 판단
    if diff >= 5:
        st.error("🔴 결과: 거짓이에요! 심박수가 눈에 띄게 증가했어요 😳")
    elif diff <= -5:
        st.error("🔴 결과: 거짓이에요! 심박수가 비정상적으로 감소했어요 😮")
    else:
        st.success("🟢 결과: 진실이에요! 심박수 변화가 안정적이에요 😌")

# 📌 하단 설명
st.markdown("---")
st.caption("💡 본 서비스는 실제 학생들이 아두이노 센서로 수집한 데이터를 바탕으로 제작한 교육용 탐구 프로젝트입니다.")
