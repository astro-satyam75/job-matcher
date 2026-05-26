import requests
import pandas as pd
import streamlit as st


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

            "description": item.get(
                "description",
                ""
            ),

            "apply_link": item.get(
                "url",
                ""
            )
        })

    return pd.DataFrame(jobs)