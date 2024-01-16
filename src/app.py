import json
import streamlit as st
import yaml
import requests
import random

from lib.qiita_api import request_page

if True:
    CFG = yaml.safe_load(open("/app/conf/config.yml", "r"))
    PHASE = CFG["phase"]

random.seed(42)


# タイトルとヘッダー
st.image("src/images/Qiita_Logo.png")
st.title("QiiCast")
st.write("TODO: ここにQiiCastの説明を書く")

# ユーザからのタグ等の指定
tag = st.selectbox("タグを選択してください", ("VBA", "PHP", "Mac"))
topk = st.slider("上位何件を表示しますか", 3, 100, 10)

# BackendをAPIとして呼び出してページ取得・推論
url = 'http://127.0.0.1:8000/get_article'
data = {
   "tag" : tag,
   "num_articles" : topk
}
dl_data = requests.post(url, json=data).json()

# ratingの高い順にソートする
processed_data = sorted(dl_data, key=lambda x: x["rating"], reverse=True)

# rating上位の記事を表示
st.header("上位記事")
for rank in range(topk):
    st.subheader(f"{rank+1}位: {processed_data[rank]['title']} (rating: {processed_data[rank]['rating']:.2f})")
    st.write(f"URL: {processed_data[rank]['url']}")
    st.write(f"タグ: {', '.join([d['name'] for d in processed_data[rank]['tags']])}")
    st.write(f"投稿日: {processed_data[rank]['created_at']}")
    st.write(f"from: @{processed_data[rank]['user']['id']}")
