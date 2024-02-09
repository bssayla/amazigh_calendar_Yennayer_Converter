import calendar
import streamlit as st
import datetime

def convert_to_yennayer(year, month, day):
    yennayer_year = year + 950
    yennayer_month = month
    yennayer_day = day - 13

    if yennayer_day <= 0:
        yennayer_month = month - 1

        if yennayer_month == 0:
            yennayer_month = 12
            yennayer_year -= 1

        yennayer_day = calendar.monthrange(year, yennayer_month)[1] + yennayer_day

    return yennayer_year, yennayer_month, yennayer_day



st.title("Yennayer Converter")

today = datetime.date.today()

year = st.number_input("Enter Gregorian year:", value=today.year)
month = st.number_input("Enter Gregorian month (1-12):", value=today.month, min_value=1, max_value=12)
day = st.number_input("Enter Gregorian day:", value=today.day, min_value=1, max_value=calendar.monthrange(year, month)[1])


yennayer_day_name = calendar.day_name[datetime.date(year,month,day).weekday()]
yennayer_year, yennayer_month, yennayer_day = convert_to_yennayer(year, month, day)
st.write(f"Equivalent Yennayer date: {yennayer_year}-{yennayer_month}-{yennayer_day} - {yennayer_day_name}")


