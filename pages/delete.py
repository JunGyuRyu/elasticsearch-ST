import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import pandas as pd
from elasticsearch import Elasticsearch

st.title("데이터 삭제") 
index_name = "bank"
client = Elasticsearch('http://localhost:9200')


def delete_data(bank_location, bank_name, branch) :
    must_list = []
    must_list.append({"term":{"location": bank_location}})
    must_list.append({"term":{"bank": bank_name}})
    must_list.append({"term":{"branch": branch}})
    query = {
    "query": {
        "bool": {
            "must": must_list
            }
        }
    }
    try:
        response = client.delete_by_query(index=index_name, body=query)
        print("Delete response:", response)
        st.write(f'{bank_name} - {branch} - {bank_location} 폐점 성공!')        
    except Exception as e:
        print("Error in deleting:", e)

bank_name = st.text_input('은행이름', value="기업은행")
branch = st.text_input('은행호점', value="1호점")
bank_location = st.text_input('위치', value="상암").lower()

clicked1 = st.button("은행 폐점")
if(clicked1 == True):
    delete_data(bank_location, bank_name, branch)

















