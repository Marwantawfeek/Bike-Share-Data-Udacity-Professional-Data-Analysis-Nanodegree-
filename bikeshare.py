import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'ch':'chicago.csv',
              'new york city': 'new_york_city.csv',
              'ny': 'new_york_city.csv',
              'washington': 'washington.csv',
              'w':'washington.csv'}

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
    # get the user input about the city
    while True:
        city = input('\nPlease choose one of those 3 cities ( Chicago , New york city , Washington)\n').lower()
        if city  in CITY_DATA:
            break 
        else :
            print(input('\nPlease enter a valid name for a city or it\'s appreviation \n'))
                  
        

    # TO DO: get user input for month (all, january, february, ... , june)
    # get the user input about the month
    while True:    
        month = input('\nPlease choose the month you want from ( January , February , March , April , May , June ) or choose all\n ').lower()
        months = ['january' ,'february' ,'march' ,'april' ,'may' , 'june' , 'all']
        if month in months:
            break 
        else:
            print(input("\nPlease enter a valid month\n"))
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # get the user input about the day
    while True:
        day = input('\nPlease choose the day you want or choose all\n' ).lower()
        days = ['saturday' , 'sunday', 'monday', ' tuesday' ,'wednesday ' , 'thursday' , 'friday' , 'all']
        if day in days:
            break
        else:
            print(input('\nPlease enter a valid day \n'))  
                  
                  

    print('-'*80)
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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

        
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'no' :
            break
        
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month is : " , most_common_month)
   
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day is : " , most_common_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['Hour'].mode()[0]
    print("Most common Start hour is : " , most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common Start Station is : " , most_common_start_station)
   
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most common Start Station is : " , most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Make a new column with both start station and end station to find the most repeated one 
    
    df['the new column'] = df['Start Station'] + 'to' + df['End Station']
    most_popular_road_trip = df['the new column'].mode()[0]
    print('Most common road trip is :' , most_popular_road_trip )
                       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time" , total_travel_time )

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time', mean_travel_time)      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print('The number of user types' , count_of_user_types)

    # TO DO: Display counts of gender
    
    count_of_gender = df['Gender'].value_counts()
    print('The number of genders' , count_of_gender)
     

    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

    

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
