# DTP Website using Flask

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
git clone https://github.com/Eddyswj/DTP.git
```

Once you have downloaded the repository, you can go to the repository and to the folder called `DTP` for the website

Windows:
```dos
cd DTP
```

Unix/MacOS:
```shell
cd DTP
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

You should see the word `(mp_calc)` in your prompt something like:

Windows:
```dos
(DTP) folder >
```
Unix/MacOS:
```shell
(DTP) user $
```

To exit the virtual environment at the end of this mini project, simply type:_
```shell
exit
```
Now, you can run Flask by typing:

```shell
flask run
```

You should see that this output will be thrown out:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. 

To stop the web app, type `CTRL+C`.