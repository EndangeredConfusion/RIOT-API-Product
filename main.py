import requests
from keys import API_KEY
import streamlit as st
import time


@st.cache_data
def get_puuid(username, tagline):
    request_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tagline}%20?api_key={API_KEY}"
    data = requests.request("get", request_url)
    return data.json().get("puuid")


@st.cache_data
def get_games(puuid):
    page_num = 0
    request_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={page_num}&count=100&api_key={API_KEY}"
    games = set()
    data = requests.request("get", request_url).json()

    games.update(data)

    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    break_flag = 0
    while not break_flag:
        for _ in range(19):
            page_num += 1
            request_url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={page_num}&count=100&api_key={API_KEY}"
            data = requests.request("get", request_url).json()
            # st.write(data)
            # print(data.get("status").get("status_code"))
            if not isinstance(data, list):
                st.write("pausing")
                time.sleep(10)
            else:
                if data[-1] in games:
                    break_flag = 1
                    break
                st.write(games)
                my_bar.progress(len(games)/70_000)
                games.update(data)
                # st.write(f"{len(games)} and {games[-1]}")
        time.sleep(.1)

    st.write(games)


def main():
    st.header("You Have The C", divider="red")

    username = st.text_input("Enter your username")
    tagline = st.text_input("Enter your tagline (without the #)")
    if username and tagline and st.button("Query"):
        puuid = get_puuid(username, tagline)
        games = get_games(puuid)


if __name__ == "__main__":
    main()
