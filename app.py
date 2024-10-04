import streamlit as st

st.set_page_config(page_title="FnDL창립기념", page_icon="💯")

st.header("[FnDataLab] 2024.12.06 창립기념일", divider='rainbow')
st.error("기념 상품 증정 !!! 두둥~~~")
st.divider()

# 상품 데이터를 리스트로 정의
products = [
    {
        "img_path": "https://gdimg.gmarket.co.kr/3954993352/still/280?ver=1727659336",
        "name": "다이슨 에어랩 멀티 스타일러 컴플리트 롱",
        "description": "생활/미용가전,열기드라이기/고데기",
        "price": "683,050원",
        "discount": "5%",
        "original_price": "719,000원",
        "rating": "★ 113",
        "purchases": "구매 431"
    },
    {
        "img_path": "https://gdimg.gmarket.co.kr/3905954555/still/280?ver=1718690193",
        "name": "Apple 정품 아이패드 에어 5세대 + 스마트키보드 10.9형 WIFI 블루 64GB",
        "description": "모바일/태블릿",
        "price": "810,800원",
        "discount": "4%",
        "original_price": "849,000원",
        "rating": "★ 106",
        "purchases": "구매 448"
    },
    {
        "img_path": "https://gdimg.gmarket.co.kr/2901637487/still/280?ver=1727019516",
        "name": "토리버치 키라 쉐브론 90446 001 숄더백 크로스백",
        "description": "가방,잡화/여성가방/숄더백",
        "price": "672,590원",
        "discount": "25%",
        "original_price": "908,900원",
        "rating": "★ 14",
        "purchases": "구매 32"
    }
]

# 라디오 버튼으로 상품 선택
selected_product = st.radio(
    "상품 선택 :",
    [product['name'] for product in products]  # 상품 이름을 라디오 버튼에 표시
)
st.divider()
# 각 상품에 대한 레이아웃 설정
for product in products:
    # 라디오 버튼에서 선택한 상품에 대한 정보를 비교하여 출력
    if product['name'] == selected_product:
        col1, col2 = st.columns([4, 4])  # 두 개의 컬럼, 왼쪽은 이미지, 오른쪽은 설명

        with col1:
            st.image(product['img_path'], width=350)  # 이미지 크기를 조정하여 표시

        with col2:
            st.write(f"**{product['name']}**")
            if product['discount']:
                st.write(f"**{product['discount']} {product['price']}**")
                st.write(f"~~{product['original_price']}~~")
            else:
                st.write(f"**{product['price']}**")
            st.write(f"{product['description']}")
            st.write(f"{product['rating']} ({product['purchases']})")
