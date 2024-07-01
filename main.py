import requests
from keys import API_KEY
import streamlit as st

request_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/8ATpW0vDRTLpfXPkFRzwHNFqFYismMAs6D16N_GbO6QiwyXl1BeGSy9mjhAjmTRCfBwcWHCFTZCArQ?api_key=RGAPI-789dd8c0-2e04-4324-8b94-35388b1e7fc3"
@st.cache_data
def get_info():
    data = requests.request("get", request_url)

    return data


def main():
    st.write(get_info().json())


if __name__ == "__main__":
    main()
