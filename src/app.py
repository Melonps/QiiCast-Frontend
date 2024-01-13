import json
import streamlit as st
import yaml
import requests
import random
from streamlit_card import card
import numpy as np
from lib.qiita_api import request_page
import io
import os
from PIL import Image

if True:
    CFG = yaml.safe_load(open("/app/conf/config.yml", "r"))
    PHASE = CFG["phase"]

random.seed(42)

# タイトルとヘッダー
st.image("src/images/Qiita_Logo.png")
st.title("QiiCast")
st.write("QiiCastは、Qiitaの最新記事の中から「1か月後に人気の出る記事」をサジェストするWebアプリです。")

# ユーザからのタグ等の指定
tag = st.selectbox("タグを1つ選択してください", CFG["tags"])
topk = st.slider("表示件数：", 3, 100, 10)

# 記事を取得
request_page(save_path=CFG[PHASE]["downloaded_data"], tag=tag)
with open(CFG[PHASE]["downloaded_data"], "r") as f:
    dl_data = json.load(f)

# 推論
# TODO: ここにGBDTの推論を入れる？
# とりあえずダミーのratingを付与する
for page in dl_data:
    page["rating"] = random.random()

# ratingの高い順にソートする
processed_data = sorted(dl_data, key=lambda x: x["rating"], reverse=True)

# rating上位の記事を表示
st.header("1か月後に人気が出そうな記事ランキング")
for rank in range(topk):
    st.subheader(f"第{rank+1}位 (rating: {processed_data[rank]['rating']:.2f})")

    hasClicked = card(
        title=f"{processed_data[rank]['title']}",
        text=[
            f"#{' #'.join([d['name'] for d in processed_data[rank]['tags']])}",
            f"@{processed_data[rank]['user']['id']}, 投稿日: {processed_data[rank]['created_at'][:10]}",
        ],
        # image=image_path,
        image=processed_data[rank]['user']['profile_image_url'],
        url=processed_data[rank]['url'],
        styles={
            "card": {
                "width": "600px",
                "height": "150px",
                "border-radius": "10px",
                "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                "margin": "5px",
            },
            "title": {
                "font-size": "20px",
            }
        },
    )

