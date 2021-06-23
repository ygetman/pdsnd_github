import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #cities = ('chicago', 'new york', 'washington')
    while True:
        city = input("\nWould you like to see data for Chicago, New York, or Washington?\n").lower()
        if city not in CITY_DATA:
            print("\nYou have entered an invalid option. Please enter Chicago, New York or Washington\n")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time = input("\nWould you like to filter the data by month, day, or not at all? Please type 'none' if no filters need to be applied.\n").lower()
        if time == 'month':
            day = 'all'
            month = input("\nWhich month? January, Feburary, March, April, May or June?\n").lower()
            if month not in months:
                print("\nYou have entered an invalid option. Please enter January, Feburary, March, April, May or June\n")
                continue
            else:
                break
            break


        elif time == 'day':
            month = 'all'
            day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n").lower()
            if day not in days:
                print("\nYou have entered an invalid option. Please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday\n")
                continue
            else:
                break
            break


        elif time == 'none':
            month = 'all'
            day = 'all'
            break

        else:
            input("\nYou entered an invalid option. Please type month, day or none\n")
            break

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # extract day from the Start Time column to create an day column
    # df['day_of_week'] = df['Start Time'].dt.week # initial attempt

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable + indexing month for name to number conversion
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month #  googled how to get the highest frequency item & found .idxmax, think on stackoverflow.
    most_common_month = df['month'].mode()[0]
    print("The most common month is ", most_common_month)

    # TO DO: display the most common day of week

    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is ", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_str_station = df['Start Station'].value_counts().idxmax()
    print("\nThe most commonly used start station is ",common_str_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("\nThe most commonly used end station is ",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo'] = df['Start Station']+' to '+df['End Station']
    common_combo_station = df['Combo'].value_counts().idxmax()
    print("\nThe most frequent combination of start and end station trip is ",common_combo_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_total_travel = df['Trip Duration'].sum()
    print('Total travel time is {} seconds.'.format(tot_total_travel))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is {} seconds.'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
   # Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user types: \n" + str(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Gender Counts are: \n" + str(gender))
    else:
        print("No gender information available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        print("The earliest year of birth is ", int(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print("The most recent year of birth is ", int(most_recent_birth))
        most_common_birth = df['Birth Year'].mode()[0]
        print("The most common year of birth is ", int(most_common_birth))
    else:
        print("No year of birth information available.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    # Displays statistics on bikeshare users.
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data == 'yes':
            print(df.iloc[start_loc : start_loc + 5])
            start_loc += 5
            view_data = input("Do you want to see the next 5 rows of data?: ").lower()
        elif view_data == 'no':
            break
        else:
            view_data = input("\nYou have entered an invalid option. Please enter 'yes' or 'no'.\n")

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
