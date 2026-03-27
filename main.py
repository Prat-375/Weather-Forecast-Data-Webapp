import streamlit as st
import plotly.express as px
from backend import get_data
from datetime import datetime

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("City :")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)
    if len(filtered_data) > 0:
        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Create a temperature plot
            figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }

            cols = st.columns(4)

            for i, item in enumerate(filtered_data):
                condition = item["weather"][0]["main"]
                image_path = images.get(condition, "images/cloud.png")

                raw_time = item["dt_txt"]
                formatted_time = datetime.strptime(raw_time, "%Y-%m-%d %H:%M:%S").strftime("%a %H:%M")

                with cols[i % 4]:
                    st.markdown(f"**{formatted_time}**")
                    st.image(image_path, width=70)
                    st.caption(condition)
    else:
        st.error("Data unavailable for the city mentioned")
else:
    st.text('Please enter a city name to see weather data')