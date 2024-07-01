import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

              #CSV files will not be provided on Github

def get_filters():
    """
    Asks user to specify a city, month and day to analyze.
          
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington). Using a while loop to handle invalid inputs
    while True:
        name_city = input('Would you like to see data for Chicago, New York City or Washington? ').lower()
        if name_city in CITY_DATA.keys():
            city = name_city
            break
        else:
            print ('The entry is not recognized. Please enter one of the tree cities: Chicago, Washinton, or New York City. You need to type in FULL names')

  # Get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        name_month = input("Which month are you interested in? Please select out of January, February, March, April, May, or June. Or type in 'All'   to see all of them. ").lower()
        if name_month in months:
            month = name_month 
            break
        else:
            print ('The entry is not recognized. Please enter one of the months January, February, March, April, May, or June  or type in '"All"' .')


    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
       name_day = input("Which day should we look up? Please select one of the days of the week: Monday, teusday, Wednesday, Thursday, Friday, Saturday, or Sunday. You can also type in 'All' for non-specified view. ").lower()
       if name_day in days:
            day = name_day
            break
       else:
           print("The entry is not recognized. Please enter one of the days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday, or type 'all'.")
    
    print('-'*40)
    return city, month, day
                           
city, month, day = get_filters()
print(f'City selected: {city}')
print(f'Month specified: {month}')
print(f'Day specified: {day}')                           

def load_data(city, month, day):
    """
    The code used is based on Practice Solution 3 from this project. 
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
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

df = load_data(city, month, day)

def time_stats(df):
    """
    The idea for this code is from Practice solution 1 from this lesson.
    Displays statistics on the most frequent times of travel.
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
       
    df['Start Time'] = pd.to_datetime(df['Start Time'])
  
    
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month is',popular_month)
        
    # extract day from the Start Time column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day is',popular_day)
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour is',popular_hour)

 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    start_station = df['Start Station']
    end_station = df['End Station']
                  
    # display most commonly used start station
    popular_start = start_station.mode()[0]
    print("\nThe most commonly used start station is ", popular_start)

    # display most commonly used end station
    popular_end = end_station.mode()[0]
    print("\nThe most commonly used end station is ", popular_end)
    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print("\nThe most frequent trip route is ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print("\nTotal travel time amounted to ", total_duration)                 

    # display mean travel time
    average_duration = df['Trip Duration'].mean()
    print("\nAverage travel time was ", average_duration)   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
trip_duration_stats(df)

def user_stats(df):
    """
    Code based on practice solution 2 from this project,
    and pieces of code are inspired by Knowledge Q&A replies to other students questions. 
    Displays statistics on bikeshare users.
    
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe breakdown of users by type was as follows: \n ", user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        user_genders  = df['Gender'].value_counts()
        print("\nThe breakdown of users by gender was as follows: \n", user_genders)
    else:
        print ("\nNo 'Gender' related information available.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year  = df['Birth Year']
        earliest_YOB =  df['Birth Year'].min()
        print("The oldest user was born in ", earliest_YOB)
        most_recent_YOB = df['Birth Year'].max()
        print("The yongest user was born in ", most_recent_YOB)
        common_YOB = df['Birth Year'].mode()[0]
        print("Most common year of birth among the users is ", common_YOB)    
    else:
        print("\nNo 'Birth Year' related information available in the data base. ") 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
user_stats(df)

def raw_data(df):
    """ Asks user answer yes or no to the prompt of showing 5 lines of data. Returns 5 lines of data per iteration at a time. """
    
    print("\nRequesting user input for raw data display?")
    
    user_input = input('Would you like to display first 5 records of raw data (yes/y or no/n)? ').lower()
    
    if user_input in ("yes", "y"):
        i = 0
        while i < len(df):
            print(df.iloc[i:i + 5])
            i += 5
            if i < len(df):
                add_data = input('Would you like to display further 5 records of raw data (yes/y or no/n)? ').lower()  
                if add_data not in ("yes", "y"):
                    print("\nNot displaying further raw data.")
                    break

        else:
            print("\nNo data entires left.\n")
           
    elif user_input in ("no", "n"):
        print("\nNot displaying raw data.")
        
        
    else:
        print("\nInput no recognized. Please type in 'yes' or 'no'.")
        
    while True:
        restart = input('\nWould you like to restart? Enter yes/y or no/n. ').lower()
        if restart in ('yes', 'y'):
            return True
        elif restart in ('no', 'n'):
            exit()
        else:
            print("\nInput not recognized. Please type 'yes' or 'no'.")
 

raw_data(df)              

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # request user input (for raw data display)
                
        restart = raw_data(df)
        if not restart:
            break
      


if __name__ == "__main__":
	main()