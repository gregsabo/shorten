shorten
=======

An example URL shortener using Python and Redis.

This is intended to be a demonstration of a URL shortener which can be reasonably implemented on a whiteboard in under an hour.

More information in [the blog post](http://www.doesnotcompute.biz/programming-interview-code-a-url-shortener-on-a-whiteboard-in-5-steps)

Running
=========
Clone this repo and make a virtualenv:


```
mkvirtualenv shorten
```

If you don't have the `mkvirtualenv` command then you probably need to install [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html) and try again.

Next, make sure you're in the repo's root directory and your new virtualenv is activated. Install the python requirements:

```
pip install -r requirements.txt
```

Now make sure you have [Redis](http://redis.io/) installed and running. For example, via [Homebrew](http://brew.sh/):

```
brew install redis
redis-server
```

Finally, you can kick off the server by simply runing any of the files with python:

```
python iteration1.py
```

You can then see the output by visiting [localhost:5000](http://localhost:5000).

Additionally, you can run the tests for a file with [Nose](https://nose.readthedocs.org/en/latest/) like so:

```
nosetests iteration5.py
```
