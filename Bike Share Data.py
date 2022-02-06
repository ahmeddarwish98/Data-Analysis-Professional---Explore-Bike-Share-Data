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
    
    #Define the variable used for the city
    city = input("Please choose your city name: \n[ Chicago, New York City or Washington ] ").lower()  
    
    #use while loop to ensure the correct inputs from user
    while city not in CITY_DATA.keys():
            print("\nPlease check your input")
            print("Restarting... Please enter your city name")
            city = input("[ Chicago, New York City or Washington ] ").lower()
            
    print("\nGood.. you chose {} as your city.\n".format(city.title()))

        
    # get user input for month (all, january, february, ... , june)
    # create a dictionary to store data about month and define the variable used for the month
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = input("Please enter the month from: \n[ January, February, March, April, May, June, or All ] ").lower()
    
    #use while loop to ensure the correct inputs from user
    while month not in MONTH_DATA.keys():
        print("\nPlease check your input")
        print("Restarting... Please enter the month")
        month = input("[ January, February, March, April, May, June, or All ] ").lower()
            
    print("\nGood.. you chose {} as your month.\n".format(month.title()))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # create a dictionary to store data about day and define the variable used for the day
    DAY_DATA = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}
    day = input("Please enter the day from: \n[ Monday, Tuesday', Wednesday, Thursday, Friday, Saturday, Sunday, or All ] ").lower()
    
    #use while loop to ensure the correct inputs from user
    while day not in DAY_DATA:
        print("\nPlease check your input")
        print("Restarting... Please enter the day")
        day = input(" [ Monday, Tuesday', Wednesday, Thursday, Friday, Saturday, Sunday, or All ] ").lower()
    
    print("\nGood.. you chose {} as your day.\n".format(day.title()))

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
    # I used the Practice Solution #3 to the third form in the code
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month: {}".format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day: {}".format(common_day))

    # TO DO: display the most common start hour
    # First we must extract hour from the Start Time column to to create new column like month and day
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    print("Most common hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent station'] = df['Start Station'] + ".." + (df['End Station'])
    frequent_station = df['frequent station'].mode()[0]
    print("Most commonly frequent_station through trip: {}".format(frequent_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total travel time = {}".format(total_duration))

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    print("Mean travel time = {}".format(average_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# define the 'city' variable to use in the function
def user_stats(df, city):
    """
      Displays statistics on bikeshare users.
      Args:
        (str) city - name of the city to analyze
        
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # use pd.DataFrame to organize the results form for User Type
    user_type = pd.DataFrame(df['User Type'].value_counts())
    print("Total counts of user types = {}".format(user_type))

    # TO DO: Display counts of gender
    # we will use if ststement because washington don't have  a gender and birth year column
    if city != 'washington':
        #use pd.DataFrame to organize the results form for Gender#
        user_gender = pd.DataFrame(df['Gender'].value_counts())
        print("Total counts of user gender = {}".format(user_gender))
        
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min())
        print("Earliest year of birth = {}".format(earliest_birth_year))
        
        recent_birth_year = int(df['Birth Year'].max())
        print("Most recent year of birth = {}".format(recent_birth_year))
        
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("Most common year of birth = {}".format(common_birth_year))
  
    else:
        print("This city don't have data about gender and Birth Year.")
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
# TO DO: Display the data which user need to know
def display_data(df):
    '''
        prompt the user if they want to see 5 lines of raw data of choose  city,
        Display that data if the answer is 'yes',
        Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
        Stop the program when the user says 'no' or there is no more raw data to display.
    '''
    
    #disply  rows of data and ask user if he need more
    print(df.head())
    
    print("\nHello.. there is more data if you want to check it.")
    #index_user variable is initialized as a tag to ensure only details from
    user_index = 5
    answer = input("If you want to disply more data, please enter: [ yes or no ] ").lower()
    user_data = ['yes', 'no']
    
    #use while loop to ensure the correct inputs from user
    while answer not in user_data:
        print("\nPlease check your input")
        answer = input("Restarting... If you want to disply more data, please enter: [ yes or no ] ").lower()
        
    # use if to check the input from user  
    if answer == "yes":  
        while user_index < df.shape[0]:                     # df.shape[0] gives number of row count
            print(df.iloc[user_index:user_index+5])         # use iloc to Locate user index
            answer = input("If you want to disply more data, please enter: [ yes or no ] ").lower()
            user_index += 5
            if answer != "yes":
               print("Finally... we are finished.")
               break
               
    # answer != 'yes'
    else:
        print("Finally... we are finished.")
        
        
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)     # define the 'city' variable to use in the function
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
