# RECOVERY ISSUE

This project will allow your raspberry pi with a thermal printer to print ,independently, a little receipt for every issue open in one of your github's repository, you'll be able to select the issue to print from an html page . The recepit will contain title, repository, qrcode of the web page and number of the new issue open. My set up is a Mini Thermal Receipt Printer and a raspberry pi 3 with raspbian.

To connect and configure the thermal printer it's all well explained in my other repository **[github-issue-thermal-printer](https://github.com/filippofiocchi/github-issue-thermal-printer)** .

# Python script
You need to install python 3.7.0 or higher and set it as default, now clone this  github repository using git:
```
git clone https://github.com/filippofiocchi/recovery-issue.git
```
Now all you need are 2 tokens one for the Github API and one for the Bitly API, you need an account for both. Now move into the new directory *recovery-issue* and with nano modify the run2.sh file:

```
export TOKEN_GITHUB='your github token'

export TOKEN_BITLY='your bitlytoken'

export NAME_ORGANIZZATION='the name of the organizzation on github'
```
Insert your tokens in the respective variables and in the last one insert the name of the organizzation which you want the issues.
Now install a library of python :

```
pip3 install subprocess.run
```
Then run run2.sh with :
```
./run2.sh
```
wait a few seconds and in the browser serch the raspberry's IP addres:5000 for example :
```
192.168.1.3:5000
```
Then you'll be prompt to an html site where you can select the issue to print.
