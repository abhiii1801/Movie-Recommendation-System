import pandas as pd

File = pd.read_csv("titles - Copy.csv")

genre_list = ['animation', 'reality', 'romance', 'comedy', 'crime', 'documentation', 'western', 'history', 'music', 'fantasy', 'european', 'war', 'scifi', 'thriller', 'horror', 'family', 'action', 'sport', 'drama']

years_list = [1945, 1954, 1956, 1958, 1959, 1960, 1961, 1963, 1966, 1967, 1969, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

countries_list = ['KW', 'SE', 'CY', 'HR', 'RU', 'KG', 'PE', 'TH', 'AR', 'MY', 'UA', 'PK', 'JO', 'JP', 'LB', 'CA', 'AU', 'GH', 'BY', 'CU', 'RS', 'BE', 'IE', 'FI', 'IO', 'IT', 'NO', 'CO', 'CH', 'IS', 'LU', 'AL', 'IL', 'BF', 'DK', 'NA', 'RO', 'US', 'VE', 'VA', 'NZ', 'SY', 'VN', 'NL', 'IQ', 'KN', 'HK', 'LK', 'DE', 'GL', 'DZ', 'LT', 'CZ', 'GR', 'TR', 'ES', 'CD', 'BR', 'PY', 'MT', 'ZW', 'QA', 'EG', 'KE', 'GB', 'MA', 'PH', 'KR', 'PL', 'AE', 'AO', 'AT', 'TW', 'NP', 'CN', 'MC', 'XX', 'BS', 'MW', 'PR', 'NG', 'HU', 'IR', 'IN', 'AF', 'PT', 'GT', 'GE', 'FO', 'UY', 'MU', 'SU', 'MX', 'FR', 'BT', 'BG', 'ZA', 'TZ', 'ID', 'TN', 'KH', 'BD', 'SA', 'SN', 'PS', 'SG', 'CM', 'CL']


def info_f(m_index):
    title = str(File.loc[m_index, "title"])
    
    types = str(File.loc[m_index, "type"])
    
    year = int(File.loc[m_index, "release_year"])
    
    age = str(File.loc[m_index, "age_certification"])
    
    runtime = int(File.loc[m_index, "runtime"])
    
    season = File.loc[m_index, "seasons"]
    season = int(season) if isinstance(season, int) else str(season)
    
    score = File.loc[m_index, "imdb_score"]
    score = float(score) if isinstance(score, (int, float)) else str(score)
    
    votes = File.loc[m_index, "imdb_votes"]
    votes = int(votes) if isinstance(votes , int) else str(votes)
    
    genres = str(File.loc[m_index, "genres"]).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace(" ", "").split(",")    
    
    countries = str(File.loc[m_index, "production_countries"]).replace("[", "").replace("]", "").replace("'", "").replace("'", "").replace(" ", "").split(",")
    
    return title, types, year, age, runtime, genres, countries, season, score, votes 

def movies_w_genre(genre_list_in):
    movie_index = []
    for i in range(len(File)):
        title, types, year, age, runtime, genre, country, season, score, votes = info_f(i)
        for j in genre_list_in:
            if genre_list[j] in genre:
                movie_index.append(i)
    sorted_movie = sorted(movie_index,key=movie_index.count,reverse=True)
    sorted_movie_index = []
    [sorted_movie_index.append(x) for x in sorted_movie if x not in sorted_movie_index]
    
    return sorted_movie_index
    
def movies_w_year(year_list_in, movie_indices):
    f_year_index = years_list.index(year_list_in[0])
    s_year_index = years_list.index(year_list_in[1])
    
    
    inp_years_index = []
    for i in range(f_year_index,s_year_index+1):
        inp_years_index.append(i)
    
    inp_years_list = [years_list[i] for i in inp_years_index]
    
    movie_index = []
    for i in movie_indices:
        title, types, year, age, runtime, genre, country, season, score, votes = info_f(i)
        if year in inp_years_list:
            movie_index.append(i)
                
    return movie_index    

def movies_w_country(recom_movies_year, inp_country):
    recom_movies_country = []
    
    for i in recom_movies_year:
        title, types, year, age, runtime, genre, country, season, score, votes = info_f(i)
        if inp_country in country:
            recom_movies_country.append(i)
    
    return recom_movies_country

def print_movies(m_index):
    for index , m_index in enumerate(m_index):
        title, types, year, age, runtime, genre, country, season, score, votes = info_f(m_index)
        print(f"\n{index+1}. {title}\n")
        print("Want additional information on this Movie ?")
        print("Type 'y' for Yes (Any key to continue to next Film), 's' to stop showing more Movies ")
        inp = input(">> ")
        if inp.lower()=="y":
            print(f"\nTitle: {title}")
            print(f"Type: {types}")
            print(f"Year: {year}")
            print(f"Age Certification: {age}")
            print(f"Runtime: {runtime} minutes")
            print(f"Genres: {genre}")
            print(f"Countries: {country}")
            print(f"Seasons: {season}")
            print(f"Score: {score}")
            print(f"Votes: {votes}")
        elif inp.lower()=="s":
            break

def recommend_movies(input_genres):
    check_genres = all(1 <= i <= len(genre_list) for i in input_genres)
    if check_genres and len(input_genres) > 0:
        recom_movies_genre = movies_w_genre([i-1 for i in input_genres])
        print(f"\n{len(recom_movies_genre)} movies found\n")                
        print("Please Select the Year Range")
        print(years_list)
        year_range = list(map(int, input("\nStarting Year, Ending Year (Separated by Space)>> ").split(" ")))
        check_year = all(i in years_list for i in year_range)
        if len(year_range) == 2 and check_year:
            recom_movies_year = movies_w_year(year_range, recom_movies_genre)
            print(f"\n{len(recom_movies_year)} movies found \n")
            print("Would you like to specify Country ?")
            print("Type y for Yes (Any other key to get movies from all countries )")
            inp = input(">> ")
            if inp.lower() != 'y':
                print_movies(recom_movies_year)
            else:
                print("\nSelect Any one Country from the provided list: ")
                print(countries_list)
                inp_country = input(">> ")
                if inp_country.lower() in [i.lower() for i in countries_list]:
                    recom_movies_country = movies_w_country(recom_movies_year, inp_country.upper())
                    print(f"\n{len(recom_movies_country)} movies found \n")
                    print_movies(recom_movies_country)
                else:
                    print("\nInvalid input. Please select Country from provided List.\n")
                
        else:
            print("\nInvalid input. Please select years from year range.\n")
    else:
        print("\nInvalid input. Please select exactly 3 valid genres.\n")
    
def main():
    print("\tMovie Recommendation System")
    
    while True:
        print("\nHow would you like to get recommended movies:\n1. Based on Previous Movies\n2. Based on Genre\n3. Exit")
        inp = int(input(">> "))
        
        if inp == 1:
            print("Enter number of movies: ")
            nm = int(input(">> "))
            input_movies = []
            index_movies = []
            for i in range(nm):
                while True:
                    inp_mov = input("\nMovie Name: ")
                    if inp_mov.lower() in [i.lower() for i in File["title"].values]:
                        input_movies.append(inp_mov.lower())
                        break
                    else:
                        print("Movie not present in DataFrame")
            for movie in input_movies:
                i_of_movie = File.loc[File['title'].str.lower() == movie.lower()].index[0]
                index_movies.append(i_of_movie)

            movie_genre_set = set()

            for i in index_movies:
                title, types, year, age, runtime, genres, country, season, score, votes = info_f(i)
                movie_genre_set.update(genres)
            movie_genre_list = list(movie_genre_set)

            movie_genre_index_list = [genre_list.index(genre) + 1 for genre in movie_genre_list]

            recommend_movies(movie_genre_index_list)

        elif inp == 2:
            print("\nPlease select genres from the following:")
            print("1. Animation\t2. Reality\n3. Romance\t4. Comedy\n5. Crime\t6. Documentary\n7. Western\t8. History\n9. Music\t10. Fantasy\n11. European\t12. War\n13. Sci-Fi\t14. Thriller\n15. Horror\t16. Family\n17. Action\t18. Sport\n19. Drama")
            input_genres = list(map(int, input("(Separated by Space)>> ").split(" ")))
            recommend_movies(input_genres)
               
        elif inp == 3:
            break
        else:
            print("Invalid Input")

if __name__=="__main__":
    main()