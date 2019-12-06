import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = str(input("Please enter a city from the cities below to fetch data from: \n Chicago \n New York City \n Washington \n: ")).lower()
    while True:
        if city in CITY_DATA:
            break
        else:
            city = str(input("Wrong Input!!! \n Please enter a city from the cities below to fetch data from: \n  Chicago \n  New York City \n  Washington \n: ")).lower()
            

    # get user input for month (all, january, february, ... , june)
    months_inputs = ["January", "February", "March", "April", "May", "June", "All"]
    month = str(input("Please enter a month from the months below: \n January \n February \n March \n April \n May \n June \n All \n: ")).title()
    while True:
        if month in months_inputs:
            break
        else:
            month = str(input("Wrong Input!!! \n Please enter a month from the months below: \n  January \n  February \n  March \n  April \n  May \n  June \n  All \n: ")).title()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_inputs = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "All"]
    day = str(input("Please enter a day of the week from the below list \n Sunday \n Monday \n Tuesday \n Wednesday \n Thursday \n Friday \n Saturday \n All \n: ")).title()
    while True:
        if day in day_inputs:
            break
        else:
            day = str(input("Wrong Input!!! \n Please enter a day of the week from the below list \n  Sunday \n  Monday \n  Tuesday \n  Wednesday \n  Thursday \n  Friday \n  Saturday \n  All \n: ")).title()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Weekday"] = df["Start Time"].dt.weekday_name
    df["Hour"] = df["Start Time"].dt.hour
    if month != "All":
        months = ["January", "February", "March", "April", "May", "June"]
        month = months.index(month) + 1
        df = df[df["Month"] == month]
    if day != "All":
        df = df[df["Weekday"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    print("\n The most common month is: ", df["Month"].mode()[0])
    
    # display the most common day of week
    print("\n The most common day of the week is: ", df["Weekday"].mode()[0])

    # display the most common start hour
    print("\n The most common hour is: ", df["Hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is: ", df["Start Station"].mode()[0])

    # display most commonly used end station
    print("The most commonly used end station is: ", df["End Station"].mode()[0])

    # display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is: ", df.groupby(["Start Station", "End Station"]).max)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: ", df["Trip Duration"].sum())

    # display mean travel time
    print("The mean travel time is: ", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("The counts of user types are:\n", df["User Type"].value_counts())

    # Display counts of gender
    #print("\n The counts of gender are:\n", df["Gender"].value_counts())
    if "Gender" in df.columns:
        print("The counts of gender are:\n", df["Gender"].value_counts())

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("The earliest year of birth is: \n", df["Birth Year"].min())
        print("The most recent year of birth is: \n", df["Birth Year"].max())
        print("The most common year of birth is: \n", df["Birth Year"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    data = input("Do you want to see raw data? Enter yes or no \n").lower()
    start = 0
    end = 5
    while True:
        if data == "yes":
            print(df.iloc[start:end])
            data = input("Do you want to see more raw data? Enter yes or no. \n").lower()
            start +=5
            end +=5
        else:
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
