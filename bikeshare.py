import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Input Function

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    valid_cities = ['chicago','new york city','washington']
    valid_months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    valid_days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    print('-'*40)
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
# Grab City Input
    while True:
        try:
            city = input('Please select a city from the following: chicago, new york city, washtington.\n\n').lower()
            if city in valid_cities:
                break
            else:
                print('\nOops! This is an invalid city. Please select a city exactly as shown above.\n')
        except:
            print('\nAn error has occurred. Please try again.\n')
    print('\nYou have selected {}.\n'.format(city))

# Grab month input
    while True:
        try:
            month = input('Would you like to view data for a specific month? Or view data for all months combined? Please type all to view all months. Otherwise please make a selection from the following list: january, february, march, april, may, june.\n\n').lower()
            if month in valid_months:
                break
            else:
                print('\nOops! This is an invalid month. Please select a month exactly as shown above.\n')
        except:
            print('\nAn error has occurred. Please try again.\n')
    print('\nYou have selected {}.\n'.format(month))

# Grab day input
    while True:
        try:
            day = input('Would you like to view data for a specific day? Or view data for all days combined? Please type all to view for all days. Otherwise please make a selection from the following list: monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n\n').lower()
            if day in valid_days:
                break
            else:
                print('\nOops! This is an invalid day. Please select a day exactly as shown above.\n')
        except:
            print('\nAn error has occurred. Please try again.\n')
    print('\nYou have selected {}.\n'.format(day))
    
    print('-'*40)
    
    return city, month, day 


# Load Data Function

def load_data(city, month, day):
    """
    Loads data for the specified city and applies month and day filters if requested

    Args:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

# read in csv for selected city
    df = pd.read_csv(CITY_DATA[city])

# Convert Start Time to Date Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# Create Months and Weeks Columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['day_of_week_index'] = df['Start Time'].dt.dayofweek

# Create Months Filter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september','october','november','december']
        month = months.index(month) + 1
# Filter DF for Months Filter
        df = df[df['month'] == month]
    
# Create Weekday Filter
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
# Filter DF for Months Filter
        df = df[df['day_of_week_index'] == day]
    
    return df


# Time Stats Function

def time_stats(df,city,month,day):        
    """
    From the data selected in the load_data function calculates the most popular months, days and hours of travel for the specified location

    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyse
        (str) month - name of the month to analyse, or "all" if no filter
        (str) day - name of the day of week to analyse, or "all" if no filter
    Returns:
        summary statistics around the most popular travel times
    """
    
# load filtered data
    print('-'*40)
    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    time_df = df

# # Create Hour Columns
    time_df['Hour'] = time_df['Start Time'].dt.hour
    
# State User Selections     
    print('You are looking at data for:\nMonth(s): {}\nOn Day(s): {}\nIn: {}.\n'.format(month.title(),day.title(),city.title()))

# # Find Most Popular Month and its Count
    if month == 'all':
        popular_month = time_df['month'].mode()[0]
        month_counts = time_df['month'].value_counts()[popular_month]
        print('The most popular month is {} with a count of {}.\n'.format(popular_month,month_counts))

# # Find Most Popular Day and its Count
    if day == 'all':
        popular_day = time_df['day_of_week'].mode()[0]
        day_counts = time_df['day_of_week'].value_counts()[popular_day]
        print('The most popular day of the week is {} with a count of {}.\n'.format(popular_day,day_counts))
    
# # Find Most Popular Hour and its Count
    popular_hour = time_df['Hour'].mode()[0]
    hour_counts = time_df['Hour'].value_counts()[popular_hour]
    print('The most popular hour of the day is {} with a count of {}.\n'.format(popular_hour,hour_counts))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return 


def station_stats(df,city,month,day):
    """
    From the data selected in the load_data function calculates the most popular start station, end station and trip for the selected location

    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyse
        (str) month - name of the month to analyse, or "all" if no filter
        (str) day - name of the day of week to analyse, or "all" if no filter
    Returns:
        summary statistics around the most popular trips
    """

# load filtered data
    print('-'*40)
    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    station_df = df

    print('You are looking at data for:\nMonth(s): {}\nOn Day(s): {}\nIn: {}.\n'.format(month.title(),day.title(),city.title()))

# Find Most Popular start station and count
    popular_start_station = station_df['Start Station'].mode()[0]
    popular_start_station_count = station_df['Start Station'].value_counts()[popular_start_station]
    print('The most commonly used start station is {} with a count of {}.\n'.format(popular_start_station,popular_start_station_count))

# Find Most Popular end station and count
    popular_end_station = station_df['End Station'].mode()[0]
    popular_end_station_count = station_df['End Station'].value_counts()[popular_end_station]
    print('The most commonly used end station is {} with a count of {}.\n'.format(popular_end_station,popular_end_station_count))

# Find Most Trip - Start & Finish Location and count
    grouped_trips = station_df.groupby(['Start Station','End Station']).size().reset_index(name='Trip Count')
    sorted_trips = grouped_trips.sort_values('Trip Count', ascending=False)
    popular_trip = sorted_trips.iloc[0]
    start_popular = popular_trip['Start Station']
    end_popular = popular_trip['End Station']
    count_popular = popular_trip['Trip Count']
    print('The most common trip started at {} and finished at {} with a count of {}.\n'.format(start_popular,end_popular,count_popular))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return


# Trip Duration Function

def trip_duration_stats(df,city,month,day):
    """
    From the data selected in the load_data function calculates the total and average trip duration for the selected location

    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        Total and average trip duration for the period
    """
    
# load filtered data
    print('-'*40)
    print('Calculating Trip Duration...\n')
    start_time = time.time()

    duration_df = df
    
# State User Selections
    print('You are looking at data for:\nMonth(s): {}\nOn Day(s): {}\nIn: {}.\n'.format(month.title(),day.title(),city.title()))

# Calculate Total Travel Time
    total_travel_time = duration_df['Trip Duration'].sum()
    print('The total travel time of all trips was {}.\n'.format(total_travel_time))

# Calculate Ave Travel Time
    ave_travel_time = duration_df['Trip Duration'].mean()
    print('The mean travel time of a trip was {}.\n'.format(ave_travel_time))

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return


# User Stats Function
def user_stats(df,city,month,day):
    
    """
    From the data selected in the load_data function calculates statistics on users including the user type, gender and their year of birth

    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        user stats by type, gender and year of birth for the selected period
    """
    
# load filtered data    
    print('-'*40)
    print('Calculating User Stats...\n')
    start_time = time.time()

    userstats_df = df
    
# State User Selections
    print('You are looking at data for:\nMonth(s): {}\nOn Day(s): {}\nIn: {}.\n'.format(month.title(),day.title(),city.title()))

# User Type Count
    user_count = userstats_df['User Type'].fillna('Unknown').value_counts()
    print('Trips were made up of the following users:')
    for item, count in user_count.items():
        print('{}: {}'.format(item,count))
    
# Gender Count
    if 'Gender' not in userstats_df.columns:
        print('\nNo gender data is available.')
    else:
        gender_count = userstats_df['Gender'].fillna('Unknown').value_counts()
        print('\nTrips were made up of the following genders:')
        for item, count in gender_count.items():
            print('{}: {}'.format(item,count))
        
# Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in userstats_df.columns:
        print('\nNo age data is available.')
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        min_year = userstats_df['Birth Year'].min()
        max_year = userstats_df['Birth Year'].max()
        common_year = userstats_df['Birth Year'].mode()[0]
        common_year_count = userstats_df['Birth Year'].value_counts()[common_year]
        print('\nTrips were made up of the following birth years:')
        print('The earliest year of birth was {}\nThe latest year of birth was {}\nThe most common year of birth was {} with a count of {}.'.format(int(min_year),int(max_year),int(common_year),common_year_count))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        
        return
 
# Show Raw Data Function

def raw_data(df):
    """
    From the data selected in the load_data function shows the underlying raw data at the users request

    Args:
        df -  Pandas DataFrame containing city data filtered by month and day
    Returns:
        raw data output preview
    """  
    
# Load Raw Data and set starting index for loop    
    view_df = df
    print('-'*40)
    data_rows = len(view_df)
    starting_index = 0
    row_count = 5

# Request User input
    while True:
        show_data = input('Would you like to view raw data? Enter yes or no.\n\n').lower()
    
        if show_data == 'yes':
            window = view_df[min(starting_index,data_rows -1):min(starting_index + row_count, data_rows -1)]
            for index, row in window.iterrows():
                print()
                print('-'*40)
                print("Row", index+1)
                for column_name, value in row.items():
                    print(column_name + ": " + str(value))
            print()
            print('-'*40)
            starting_index += row_count
        else:
            break
        
    print('-'*40)
    
    return
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df,city, month, day)
        station_stats(df,city, month, day)
        trip_duration_stats(df,city, month, day)
        user_stats(df,city, month, day)
        raw_data(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
