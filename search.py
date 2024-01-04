import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers

client = Elasticsearch('http://localhost:9200')
index_name = "bank"
st.title("데이터 조회") 
bank_name = st.text_input('조회하려는 은행이름', value="기업")
bank_location = st.text_input('조회하려는 은행 위치', value="상암").lower()


def search_data_bank(bank_name, bank_location) :
    query = {
    "query": {
        "bool": {
            "must": [
                {
                    "query_string": {
                        "default_field": "location",
                        "query": f"*{bank_location}*"
                    }
                }],
            "filter": [
                {
                    "query_string": {
                        "default_field": "bank",
                        "query": f"*{bank_name}*"
                        }
                    }]
            }
        }
    }

    response = client.search(index=index_name, body=query)
    # data = response.to_dict()["hits"]["hits"]
    source_data = [entry["_source"] for entry in response["hits"]["hits"]]
    df = pd.DataFrame(source_data)
    st.dataframe(df, hide_index=True)
    # 결과 출력
    print("Indexing response:", response)
    st.write(f'은행 조회 성공!') 

clicked1 = st.button("값 조회")
if(clicked1 == True):
    try:
        search_data_bank(bank_name, bank_location)
    except:
        st.write("값 조회 실패...")
