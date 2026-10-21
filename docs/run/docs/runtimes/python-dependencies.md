---
url: https://docs.cloud.google.com/run/docs/runtimes/python-dependencies/
title: Specify dependencies in Python \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:20.786381+00:00
---

# Specify dependencies in Python  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/python-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Specify dependencies in Python Stay organized with collections  Save and categorize content based on your preferences. 

Specify your application dependencies for [supported Python versions](https://docs.cloud.google.com/docs/buildpacks/runtime-support#python) using any of the following approaches:

  * Use a `requirements.txt` file in the root directory. This file must be in the same directory as the `main.py` file that contains your source code. The `requirements.txt` file contains one line per package. Each line contains the package name, and optionally, the requested version. To prevent your build from being affected by dependency version changes, consider pinning your dependency packages to a specific version.

The following is an example `requirements.txt` file:
        
        functions-framework
        requests==2.20.0
        numpy
        

  * Use a `pyproject.toml` file to specify dependencies. If you manage your application dependencies in a `pyproject.toml` file instead of the `requirements.txt` file, the Python buildpack determines the package manager based on the configuration you specify in the `pyproject.toml` file. For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

If your application uses both the `pyproject.toml` file and the `requirements.txt` file, the `requirements.txt` file takes precedence.

    * The following is an example `pyproject.toml` file:
          
          [project]
          name = "demo-app"
          version = "0.1.0"
          description = ""
          requires-python = ">=3.10"
          dependencies = [
              "flask>=3.1.1",
              "gunicorn>=23.0.0",
          ]
          
          [build-system]
          requires = ["setuptools>=61.0"]
          build-backend = "setuptools.build_meta"
          



  * [Package local dependencies](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies#package-local-dependencies) alongside your function.

Dependency specification using the `Pipfile/Pipfile.lock` standard is not supported. Your project shouldn't include these files.

If you use a `requirements.txt` file to manage dependencies, Cloud Run installs the [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-python) on your behalf when you create a function. However, we recommend that you include Functions Framework as an explicit dependency to avoid discrepancies.

When you use a `pyproject.toml` file, you must include the [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-python) as a dependency because Cloud Run doesn't install it on your behalf.




## Package manager

If you manage your dependencies using a `requirements.txt file`, the default package manager varies based on the Python version you configure.

If you use a `pyproject.toml` file to manage dependencies instead of a `requirements.txt` file, the Python buildpack determines the package manager based on your configuration settings in the `pyproject.toml` file. The buildpack supports pip, uv and Poetry package managers. For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

###  Python 3.14 and later 

Starting from Python version 3.14 and later, the Python buildpack uses the [uv](https://docs.astral.sh/uv/) package manager as the default installer for the dependencies you specify in your `requirements.txt` file.

To use [`pip`](http://pip.readthedocs.org/) as the package manager, configure the environment variable `GOOGLE_PYTHON_PACKAGE_MANAGER="pip"`.

Run the `gcloud run deploy` command to set the package manager environment variable to `pip`:
    
    
    gcloud run deploy SERVICE --source . \
      --set-build-env-vars=GOOGLE_PYTHON_PACKAGE_MANAGER=pip
    

Replace SERVICE with the name of your Cloud Run service.

###  Python 3.13 and earlier 

For Python version 3.13 and earlier, the Python buildpack uses the [pip](http://pip.readthedocs.org/) package manager to install dependencies you define in the [`requirements.txt`](http://pip.readthedocs.org/en/stable/user_guide/#requirements-files) file.

To use [uv](https://docs.astral.sh/uv/) as the package manager, configure the environment variable `GOOGLE_PYTHON_PACKAGE_MANAGER="uv"`.

Run the `gcloud run deploy` command to set the package manager environment variable to `uv`:
    
    
    gcloud run deploy SERVICE --source . \
      --set-build-env-vars=GOOGLE_PYTHON_PACKAGE_MANAGER=uv
    

Replace SERVICE with the name of your Cloud Run service. 

## Package local dependencies

Package and deploy dependencies alongside your function. This approach is useful if your dependency isn't available when you use a [supported package manager](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml) or if your Cloud Run environment's internet access is restricted.

You can also use a `requirements.txt` file to specify additional dependencies you haven't packaged alongside your function. For example, you might use the following directory structure:
    
    
    myfunction/
    ├── main.py
    └── localpackage/
        ├── __init__.py
        └── script.py
    

Import the code from `localpackage` using the following `import` statement:
    
    
    # code in main.py
    from localpackage import script
    

This approach won't run any `setup.py` files. You can bundle the packages with those files, but the package might not run correctly on Cloud Run functions.

## Copied dependencies

Copied dependencies are dependencies whose source is included directly in your source code package and rebuilt alongside your own code. Use the `GOOGLE_VENDOR_PIP_DEPENDENCIES` build environment variable to create copied pip dependencies and avoid installing them during deployment.

### Create copied dependencies

  1. Ensure that [python3](https://docs.cloud.google.com/python/docs/setup#installing_python) is installed on your development system.

  2. [Declare your application dependencies](https://docs.cloud.google.com/docs/buildpacks/python#specifying_dependencies_with_pip) in a `requirements.txt` file in the root directory of your development tree.

  3. Declare Functions Framework as a requirement by including `functions-framework` on a separate line in your `requirements.txt` file.

  4. Download your function's dependencies to your local directory. The steps to do this depend on whether the dependency is a Python wheel (*.whl) file or a tar file (*.tar.gz).

     1. If the dependency is a Python wheel (*.whl), download it into the root directory of your development tree with this pip command:
            
            python3 -m pip download -r requirements.txt --only-binary=:all: \
               -d DIRECTORY \
               --python-version PYTHON_RUNTIME_VERSION \
               --platform manylinux2014_x86_64 \
               --implementation cp
            

Replace the following:

        * DIRECTORY: the name of the local directory to download to.
        * PYTHON_RUNTIME_VERSION: the Python version to use for compatibility checks. For example `314` for Python 3.14.   
This version must match one of the [supported Python runtimes](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#python).

The resulting directory structure should look like this: 
    
    myfunction/
    ├── main.py
    └── requirements.txt
    └── DIRECTORY
       ├── dependency1.whl
       └── dependency2.whl
    

     2. If the dependency is a tar file (*.tar.gz):

        1. If the dependency is written in Python, use pip to download it:
               
               python3 -m pip download -r requirements.txt \
                  -d DIRECTORY
               

        2. If a dependency consists of code written in C or C++, download and compile the code separately.

  5. Deploy your function and its copied dependencies:
         
         gcloud functions deploy FUNCTION_NAME \
           --runtime PYTHON_RUNTIME_NAME \
           --set-build-env-vars GOOGLE_VENDOR_PIP_DEPENDENCIES=DIRECTORY
         

Replace the following:

     * FUNCTION_NAME: the name of the function you're deploying.
     * PYTHON_RUNTIME_NAME: the name of one of the [supported Python runtimes](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#python) to run your deployed function under - for example python311. This must be the same Python runtime version as you've used in your local development environment.
     * DIRECTORY: the name of the directory containing your copied dependencies.



For more details about using buildpacks, see [Build a function with buildpacks](https://docs.cloud.google.com/run/docs/building/functions).

## Use private dependencies

You can use private dependencies from Artifact Registry or from other repositories.

### Private dependencies from Artifact Registry

An [Artifact Registry Python repository](https://docs.cloud.google.com/artifact-registry/docs/python/store-python) hosts private dependencies for your Python function. When deploying to Cloud Run, the build process automatically generates Artifact Registry credentials for the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). Include the Artifact Registry URL in your `requirements.txt` without generating additional credentials. For example:
    
    
    --index-url REPOSITORY_URL
    sampleapp
    Flask==0.10.1
    google-cloud-storage
    

If your build needs multiple repositories, use an [Artifact Registry virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) to safely control the order that pip searches your repositories.

### Private dependencies from other repositories

Buildpacks installs dependencies in a Cloud Build environment that doesn't provide access to SSH keys. Copy the packages you host in repositories that require SSH-based authentication and upload the packages with your project's code.

Use the `pip install` command with the `-t DIRECTORY` flag to copy private dependencies into a local directory before deploying your app, as follows:

  1. Copy your dependency into a local directory: 
         
         pip install -t DIRECTORY DEPENDENCY

  2. Add an empty `__init__.py` file to the `DIRECTORY` directory to turn it into a module.
  3. Import from this module to use your dependency: 
         
         import DIRECTORY.DEPENDENCY




## Pre-installed packages

The Python buildpack installs the following Python packages when you deploy your function. If you are using any of these packages in your function code, include the following versions in your `requirements.txt` file:

To avoid issues with dependency version updates, pin the package to a specific version.
    
    
    anyio==4.14.2
    blinker==1.8.2
    click==8.1.8
    cloudevents==1.11.0
    deprecation==2.1.0
    exceptiongroup==1.3.0
    Flask==3.0.3
    functions-framework==3.10.2
    gunicorn==23.0.0
    h11==0.16.0
    idna==3.15
    importlib_metadata==8.5.0
    itsdangerous==2.2.0
    Jinja2==3.1.6
    MarkupSafe==2.1.5
    packaging==25.0
    sniffio==1.3.1
    # Install starlette 0.44.0 for Python 3.8
    starlette==0.44.0; python_version == '3.8'
    # Install starlette 0.49.1 for Python 3.9
    starlette==0.49.1; python_version == '3.9'
    # Install starlette 1.0.1 for Python 3.10+
    starlette==1.3.1; python_version >= '3.10'
    typing_extensions==4.13.2
    uvicorn==0.33.0
    uvicorn-worker==0.2.0
    watchdog==4.0.2
    Werkzeug==3.0.6
    zipp==3.20.2
    

The Python buildpack installs the following packages pinned to a specific version:

  * `pip` (latest version)
  * `setuptools` (latest version)
  * `wheel` (determined by product requirements)



The Python runtime also includes a number of [system packages](https://docs.cloud.google.com/docs/buildpacks/stacks) in the execution environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
