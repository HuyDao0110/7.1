import streamlit as st

st.set_page_config(page_title='Thông tin bạn thân', page_icon=':busts_in_silhouette:', layout='wide')
st.title('Hãy chọn một người bạn thân')
col1, col2 = st.columns(2)

friends = {
    "Trịnh Trần Phương Tuấn": {
        "Ngày sinh": "32/13/2028",
        "Sở thích": "Đọc sách"
    },
    "Nguyễn Thúc Thùy Tiên": {
        "Ngày sinh": "34/14/2034",
        "Sở thích": "Nghe nhạc"
    }
}

with col1:
    b1 = st.button("Trịnh Trần Phương Tuấn")
with col2:
    b2 = st.button("Nguyễn Thúc Thùy Tiên")

if b1:
    with st.expander("Thông tin của Trịnh Trần Phương Tuấn"):
        st.write("Ngày sinh:", friends["Trịnh Trần Phương Tuấn"]["Ngày sinh"])
        st.write("Sở thích:", friends["Trịnh Trần Phương Tuấn"]["Sở thích"])

if b2:
    with st.expander("Thông tin của Nguyễn Thúc Thùy Tiên"):
        st.write("Ngày sinh:", friends["Nguyễn Thúc Thùy Tiên"]["Ngày sinh"])
        st.write("Sở thích:", friends["Nguyễn Thúc Thùy Tiên"]["Sở thích"])

with st.sidebar:
    st.title("Thông tin bạn đã chọn")
    if b1:
        st.write("Bạn chọn: Trịnh Trần Phương Tuấn")
    if b2:
        st.write("Bạn chọn: Nguyễn Thúc Thùy Tiên")
