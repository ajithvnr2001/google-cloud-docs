---
url: https://docs.cloud.google.com/python/docs/setup/
title: Setting up a Python development environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:06.543359+00:00
---

# Setting up a Python development environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Setting up a Python development environment Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to prepare your local machine for [Python](https://python.org) development, including developing Python apps that run on Google Cloud.

If you already have a development environment set up, see [Python and Google Cloud](https://docs.cloud.google.com/python) to get an overview of how to run Python apps on Google Cloud.

Tip: If you want to get started quickly, [Cloud Shell Editor](http://shell.cloud.google.com/) provides IDE support for the full development cycle of Google Kubernetes Engine and Cloud Run applications. Cloud Shell Editor is based on [Code OSS](https://github.com/microsoft/vscode) and comes with the Google Cloud CLI and Cloud Code tools preinstalled. 

## Objectives

  * Install a [supported version of Python](https://docs.cloud.google.com/python/docs/supported-python-versions) compatible with Google Cloud.
  * Use `venv` to isolate dependencies.
  * Install an editor (optional).
  * Install the Google Cloud CLI (optional).
  * Install the Cloud Client Libraries for Python (optional).
  * Install other useful tools.
  * Set up authentication (optional).



## Installing Python

Python's installation instructions vary by operating system. Follow the guide for the operating system you're running in your development environment, macOS, Windows, or Linux.

### macOS

macOS includes a version of Python by default and uses it for its own purposes. To avoid interfering with macOS, we recommend creating a separate development environment and installing a [supported version of Python](https://docs.cloud.google.com/python/docs/supported-python-versions) for Google Cloud. To install Python, use [homebrew](https://brew.sh/).

  1. To use homebrew to install Python packages, you need a compiler, which you can get by installing [Xcode's command-line tools](https://developer.apple.com/library/content/technotes/tn2339/_index.html).
         
         xcode-select --install
         

  2. Install homebrew by following the instructions on the [homebrew homepage](https://brew.sh/), and then use homebrew to install Python as follows:
         
         brew install pyenv
         pyenv install PYTHON_VERSION
         

Python version number should be in the format of `x.y`. For example:
         
         pyenv install 3.12
         

  3. After the installations are complete, verify that Python 3 is available as `python` and `python3`, and that `pip` is also installed.

To verify that Python is available, run the following command:
         
         python3 --version
         

The output shows the version. You can learn about Python homebrew on the [Homebrew Python Formulae](https://formulae.brew.sh/formula/python@3.12) page, and then check your version.

To verify that `pip3` is available, run the following command:
         
         pip3 --version
         

If installed, the output shows the `pip3` version. For more about the latest version of `pip3`, see the [`pip` Release Notes](https://pip.pypa.io/en/stable/news/).

If the preceding command does not show the `pip3` version, make sure that `pip3` is installed correctly. If `pip3` is installed but not working, upgrade to the latest version using the following command:
         
         python -m pip install --upgrade pip
         

Homebrew installs the latest versions of Python available on your platform. The version numbers in the outputs might be different from [the latest official releases of Python](https://www.python.org/downloads/).




### Windows

  1. To install Python in a Windows environment, download the installer for the version of Python you need from the [Python website](https://www.python.org/downloads/windows/). For more information, see the [supported versions of Python](https://docs.cloud.google.com/python/docs/supported-python-versions) for Google Cloud.

  2. To access your version of Python, use [Python launcher for Windows](https://docs.python.org/3/using/windows.html#launcher).

To start the version of Python you installed, run the following command:
         
         py
         

To start the version of Python 3 you installed, run the following command:
         
         py -3
         

To verify the version of `pip` that is available, run the following command:
         
         py -m pip --version
         

The output shows the version from `C:\users\[USERNAME]\appdata\local\programs\python\python38-32\lib\site-packages`.

You can learn about the latest version of `pip` in the [`pip` Release Notes](https://pip.pypa.io/en/stable/news/).




### Linux

Most Linux distributions include recent versions of Python.

  1. To install Python in a Linux environment, install the appropriate packages for your distribution. For Debian and Ubuntu, these packages are [python3](https://packages.debian.org/stable/python3), [python3-dev](https://packages.debian.org/stable/python3-dev), [python3-venv](https://packages.debian.org/stable/python3-venv), and [python3-pip](https://packages.debian.org/stable/python3-pip),

Install these packages using the following commands:
         
         sudo apt update
         sudo apt install python3 python3-dev python3-venv python3-pip
         

  2. After the installations are complete, verify that you have `pip` installed:
         
         pip3 --version
         

You can learn about the latest version of `pip` in the [pip Release Notes](https://pip.pypa.io/en/stable/news/).




## Using venv to isolate dependencies

[_`venv`_](https://docs.python.org/3/library/venv.html) is a tool that creates isolated Python environments. These isolated environments can have separate versions of Python packages, which lets you isolate one project's dependencies from the dependencies of other projects. We recommend that you always use a per-project virtual environment when developing locally with Python.

  1. Use the `venv` command to create a virtual copy of the entire Python installation. This tutorial creates a virtual copy in a folder named `env`, but you can specify any name for the folder.

### macOS
         
         cd your-project
         python -m venv env
         

### Windows
         
         cd your-project
         py -m venv env
         

### Linux
         
         cd your-project
         python3 -m venv env
         

  2. Set your shell to use the `venv` paths for Python by activating the virtual environment:

### macOS
         
         source env/bin/activate
         

### Windows
         
         .\env\Scripts\activate
         

### Linux
         
         source env/bin/activate
         

  3. Now you can install packages without affecting other projects or your global Python installation:
         
         pip install google-cloud-storage
         

If you want to stop using the virtual environment and go back to your global Python, you can deactivate it:
         
         deactivate
         




You can read more about `venv` in the [`venv` docs](https://docs.python.org/3/library/venv.html).

**Note:** If you're using [Anaconda](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/), follow the instructions on their website.

## Installing an editor

To develop Python apps, you need an editor. Here are a few of the more popular editors (in no particular order):

  * [Visual Studio Code](https://code.visualstudio.com/) by Microsoft
  * [Sublime Text](https://www.sublimetext.com/) by Jon Skinner
  * [PyCharm](https://www.jetbrains.com/pycharm/) by JetBrains



## Installing the Cloud Client Libraries for Python

The Cloud Client Libraries for Python is how Python developers integrate with Google Cloud services like Datastore and Cloud Storage. To install the package for an individual API like Cloud Storage, use a command similar to the following:
    
    
    pip install --upgrade google-cloud-storage
    

## Installing the gcloud CLI

The [gcloud CLI](https://docs.cloud.google.com/sdk) is a set of command-line tools for Google Cloud. It contains `gcloud` and `bq`, which you can use to access Compute Engine, Cloud Storage, BigQuery, and other products and services from the command line. You can run these tools interactively or in your automated scripts.

### Set up authentication

To use the client library, you must first set up authentication.

If you're using a local shell, then create local authentication credentials for your user account: 
    
    
    gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

## What's next

  * Learn more about [Python on Google Cloud](https://docs.cloud.google.com/python).

  * Deploy a [Python service to Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service). 

  * Understand [Authentication methods at Google](https://docs.cloud.google.com/docs/authentication).

  * Browse the [documentation for Google Cloud products](https://cloud.google.com/products).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
