# LinkedIn-auto_connect
A code snippet to auto connect with people in LinkedIn.
There are several ways to do it, well like anything else in the world really.
I chose to search for a certain job (I did it with 'Data Scientist'), then connect all people the search engine found until the limit set by LinkedIn is reached.

Requirements : selenium, Chromedriver stable release

HOW TO : 

Firstly, download linkedin_auto_connect.py.
Then, open a jupyter notebook instance in the same folder as linkedin_auto_connect.py and write in a cell (or put in a script in the same folder) the following :

from linkedin_auto_connect import auto_connector
auto_connector(mail, password, job) #replace the arguments


That's it.

Disclaimer : use at your own risk. I am not responsible if LinkedIn bans your account, even if this program is not illegal.

PS : You may have to change the path for the chromedriver, and will have to if you are not using a Linux distribution.
I haven't tested with another driver, it should work though.
