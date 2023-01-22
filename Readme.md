# <center> Want to see the Oscar race? Check out this project </center>

![Oscar](https://www.towncenterzumpango.com.mx/wp-content/uploads/2020/01/premios-oscar-2020.jpg)

Since we are in the Oscar season, to make the wait more enjoyable I have created this project to analyze the Oscar race. I have compiled, filtered, cleaned and graphed information about the awards, from 1990 to 2020, that I consider most relevant to this race; Golden Globes, SAG (Screen Actor Guild Awards), Critics' Choice Movie Awards and of course the Oscars. In order to see the correlation of the awards and in the future, be able to make a predictive analysis of the winners, and keep it updated!

## Table of Contents
1. [Getting Started](#getting-started)
2. [Usage](#usage)
3. [Examples](#examples)
4. [Documentation](#documentation)
5. [Support](#support)

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 or later
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (optional)

### Installation

1. Clone the repository:
https://github.com/JN2187/Oscar_Race.git
2. Create a virtual environment (optional but recommended)

### Dependencies

This project depends on the following libraries:
- pandas
- re
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://pypi.org/project/seaborn/)
- [pymongo](https://pypi.org/project/pymongo/)

### Troubleshooting

- If you run into issues installing the dependencies, make sure you have the latest version of pip and try again.


## Usage

Folder scheme: Inside Oscar_Race you can find a data folder, which contains all the csv files of this project. The ones I have used for the cleanup taken from [Kaggle](https://www.kaggle.com/);
- [the_oscar_award](https://www.kaggle.com/datasets/unanimad/the-oscar-award)
- [golden_globe_awards](https://www.kaggle.com/datasets/unanimad/golden-globe-awards)
- [screen_actor_guild_awards](https://www.kaggle.com/datasets/unanimad/screen-actors-guild-awards)

The ones I've created from these, with their respective cleaning and standardization;
- [Oscar_clean](data/Oscar_clean.csv)
- [Golden_Globes_clean](data/Golden_Globes_clean.csv)
- [SAG_clean](data/AG_clean.csv)

And also the ones I´ve created from [wikipedia's](https://en.wikipedia.org/wiki/Critics%27_Choice_Movie_Awards#Categories) web scraping and their respective cleaning and standardization;
- [Best_Picture_soup_cca](data/Best_Picture_soup_cca.csv)
- [Actor_In_A_Leading_Role_soup_cca](data/Actor_In_A_Leading_Role_soup_cca.csv)
- [Actor_In_A_Supporting_Role_soup_cca](data/Actor_In_A_Supporting_Role_soup_cca.csv)
- [Actress_In_A_Leading_Role_soup_cca](data/Actress_In_A_Leading_Role_soup_cca.csv)
- [Actress_In_A_Supporting_Role_soup_cca](data/Actress_In_A_Supporting_Role_soup_cca.csv)
- [CCA_clean](data/CCA_clean.csv)

And finally all awards gathered in a single csv:
- [Cinema_Awards](data/Cinema_Awards.csv)

In the notebooks folder you can find the code I've used for each of the cleaning, web scraping, storage and visualization tasks.

In the src folder there is a .py document called [support](src/support.py) where all the functions that I have created for this project are collected.


## Examples

In this project I have compiled information on the following categories, Best Actor and Actress, both lead and supporting, Best Director, Best Picture, Best Screenplay, both adapted and original since 1990 to 2020.

## Documentation

In this project I have used the following Python libraries: 
- pandas
- re
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [seaborn](https://pypi.org/project/seaborn/)
- [pymongo](https://pypi.org/project/pymongo/)

### Support

If you have any questions or run into any issues, please contact me at [juanoncorrea@gmail.com](mailto:juanoncorrea@gmail.com)

## <center>Enjoy! 🙌</center>
<center><img src="https://media2.giphy.com/media/AbDCwAI2xTwTm/giphy.gif?cid=790b761162ebc2b65306a1767bceffddf4021c5583ae566e&rid=giphy.gif&ct=g" width="400" height="400" style="display: block; margin: 0 auto;"></center>
