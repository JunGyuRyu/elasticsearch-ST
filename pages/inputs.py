import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers

st.title("데이터 삽입") 

def insert_data_bank(bank_id, date_str, bank_name, bank_no, bank_location, customers_cnt) :
    client = Elasticsearch('http://localhost:9200')
    # 입력할 데이터
    data = {
        "date": date_str,
        "bank": bank_name,
        "branch": bank_no,
        "location": bank_location,
        "customers": customers_cnt
    }
    # index 메소드를 사용하여 데이터 색인화
    index_name = "bank"
    doc_id = bank_id  # 원하는 문서의 고유 식별자
    response = client.index(index=index_name, id=doc_id, body=data)
    # 결과 출력
    print("Indexing response:", response)
    st.write(f'{bank_name} - {bank_location} 삽입 성공!') 


id_str = st.number_input('ID', value=11111)
date_str = st.date_input("방문날짜", value="today")
bank_name = st.text_input('은행이름', value="기업은행")
bank_no = st.text_input('호점', value="123123호점")
bank_location = st.text_input('위치', value="상암").lower()
customers_cnt = st.number_input('방문고객수', value=77777)

clicked1 = st.button("값 삽입")
if(clicked1 == True):
    insert_data_bank(id_str, date_str, bank_name, bank_no, bank_location, customers_cnt)



















