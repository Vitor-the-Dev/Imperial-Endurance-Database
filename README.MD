# What is the Imperial Endurance Database? #

The Imperial Endurance Database is a simple python script using the SWAPI (www.swapi.tech) to calculate how many stops a star wars ship will be required to make to ressuply given a distance x
for more information, please contact me on the email: 
## vitorferthedev@gmail.com


### Usage ###

Simply clone the repository, use your favorite python package manager to install requirements.txt and execute _main_.py. You will be prompted on your terminal a message requesting an input distance in Megalights.

### How does it work? ###

This project executes HTTP requests to the SWAPI to get a list of avaliable starships from the star wars universe. The next step is requesting (again via HTTP) the properties of the ship models we got the url in the last step. Finally, we simply calculate max range before a stop based on endurance(in hours) times speed (in megalights/hour), and simply divide our desired distance by range to discover how many stops for ressupplying a ship will require.