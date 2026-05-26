import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup

@st.cache_data(ttl=3600)
def fetch_remote_jobs():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    jobs = []

    for item in data:

        if not isinstance(item, dict):
            continue

        title = item.get("position", "")

        if not title:
            continue

        raw_description = item.get(
            "description",
            ""
        )

        clean_description = BeautifulSoup(
            raw_description,
            "html.parser"
        ).get_text(separator=" ")

        jobs.append({

            "title": title,

            "company": item.get(
                "company",
                ""
            ),

            "location": item.get(
                "location",
                "Remote"
            ),

            "description": clean_description,

            "apply_link": item.get(
                "url",
                ""
            )
        })