# Crop Prediction for most yield

## Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

## Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
git clone https://github.com/Eddyswj/DTP.git
```

Once you have downloaded the repository, you can go to the repository and to the folder called `DTP` for the website

Windows:
```dos
cd DTP/Webapp
```

Unix/MacOS:
```shell
cd DTP/Webapp
```

## Create Virtual Environment 

First make sure that you have installed `pipenv` package.

```shell
python -m pip install --user pipenv
```

From the root folder, install the packages specified in the `Pipfile`.
```shell
python -m pipenv install
```
The above steps will install the following packages:
- Flask 
- Flask-socketio
- Numpy

The 'Bootstrap' package is not needed to be installed as we are referencing it through a CDN(Content Delivery Network)

To activate the virtualenv, run
```shell
python -m pipenv shell
```

You should see the word `(Webapp)` in your prompt something like:

Windows:
```dos
(Webapp) folder >
```
Unix/MacOS:
```shell
(Webapp) user $
```

To exit the virtual environment at the end of this mini project, simply type:_
```shell
exit
```
## Running the Website
Now, you can run Flask by typing:

```shell
flask run
```

You should see that this output will be thrown out:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. 

To stop the website, type `CTRL+C`.  

## On the Website

![](https://www.dropbox.com/scl/fi/kcqwayc26x3kexp3zrhqa/Screenshot-2024-11-29-at-4.14.02-PM.png?raw=1)

Follow the clear and simple instructions on each page to discover the **best crop type** for achieving **maximum yield**. With just a few steps, you'll be on your way to making a more productive farming decisions. 

Here's to your success in agriculture!

