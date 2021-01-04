# Rate My Professor Bot
 Takes in first, last, or both names of the Professor, scrapes json pages and outputs information.

## Usage
I placed all the functions used for retreiving the json pages and scraping it in a class, making it easier for other students in different universities to use this bot if necessary.  This can be used for ANY school on Rate My Professor. Simply change the current school ID(sid) to the school you want to scrape when creating the class. 
```python
from newsearch import University


def searchFull(name):
    UA = University(YOUR SCHOOL ID)
```
Aside from that, the commands are:
## ?search
This takes in a First and Last name, passes it to the searchFull function and outputs information from RateMyProfessor about the person searched. 
```
?search Eric Woods
```
![out for ?search](https://github.com/Mcheung7272/Rate-My-Professor-Bot/blob/master/exOutputRMP.png?raw=true "?search Output")

## ?ns
This command is used if the user only remembers the first or last name of the professor. 
```
?ns eric
```
![out for ?ns](https://github.com/Mcheung7272/Rate-My-Professor-Bot/blob/master/exOutputRMPns.png?raw=true "?ns Output")

## ?compare
This is a comparision feature, used to compare two professor's reviews side by side.
```
?compare "Eric Woods" "Eric Fowler"
```
![out for ?ns](https://github.com/Mcheung7272/Rate-My-Professor-Bot/blob/master/exOutputRMPcompare.png?raw=true "?ns Output")

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
