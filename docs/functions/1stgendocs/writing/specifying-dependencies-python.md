---
url: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-python/
title: Specify dependencies in Python (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:28.762564+00:00
---

# Specify dependencies in Python (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/writing/specifying-dependencies-python/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Specify dependencies in Python (1st gen)

There are two ways to specify dependencies for Cloud Run functions written in Python: using the [pip](https://pip.pypa.io/en/stable/) package manager's `requirements.txt` file or packaging local dependencies alongside your function.

Dependency specification using the Pipfile/Pipfile.lock standard is not supported. Your project should not include these files.

## Specify dependencies with pip

Dependencies in Python are managed with pip and expressed in a metadata file called [`requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files). This file must be in the same directory as the `main.py` file that contains your function code.

When you deploy or redeploy your function, Cloud Run functions uses pip to download and install the latest version of your dependencies as declared in the `requirements.txt` file. The `requirements.txt` file contains one line per package. Each line contains the package name, and optionally, the requested version. For more details, see the [`requirements.txt` reference](https://pip.pypa.io/en/stable/user_guide/#requirements-files).

To prevent your build from being affected by dependency version changes, consider pinning your dependency packages to a specific version.

The following is an example `requirements.txt` file:
    
    
    functions-framework
    requests==2.20.0
    numpy
    

The [Functions Framework](https://docs.cloud.google.com/functions/1stgendocs/functions-framework) is a required dependency for all functions. Although Cloud Run functions installs it on your behalf when the function is created, we recommend that you include it as an explicit dependency for clarity.

If your function relies on private dependencies, we recommend that you mirror `functions-framework` to your private registry. Include the mirrored `functions-framework` as a dependency to your function to avoid installing the package from the public internet.

## Package local dependencies

You can also package and deploy dependencies alongside your function. This approach is useful if your dependency is not available via the pip package manager or if your Cloud Run functions environment's internet access is restricted.

**Note:** You can still use a `requirements.txt` file to specify additional dependencies you haven't packaged alongside your function.

For example, you might use a directory structure such as the following:
    
    
    myfunction/
    ├── main.py
    └── localpackage/
        ├── __init__.py
        └── script.py
    

You can then import the code as usual from `localpackage` using the following `import` statement.
    
    
    # Code in main.py
    from localpackage import script
    

Note that this approach will _not_ run any `setup.py` files. Packages with those files can still be bundled, but may not run correctly on Cloud Run functions.

## Vendored dependencies

Vendored dependencies are dependencies whose source is included directly in your source code package and rebuilt alongside your own code. Use the GOOGLE_VENDOR_PIP_DEPENDENCIES build environment variable to create vendored pip dependencies and avoid installing them during deployment.

### Create vendored dependencies

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
            

Replace:

        * DIRECTORY: the name of the local directory to download to
        * PYTHON_RUNTIME_VERSION: the Python version to use for compatibility checks. For example `311` for Python 3.11.   
This version must match one of the [supported Python runtimes](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#python)

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
               

        2. If a dependency consists of code written in C or C++, you must download and compile it separately.

  5. Deploy your function and its vendored dependencies:
         
         gcloud functions deploy FUNCTION_NAME \
           --runtime PYTHON_RUNTIME_NAME \
           --set-build-env-vars GOOGLE_VENDOR_PIP_DEPENDENCIES=DIRECTORY
         

Replace:

     * FUNCTION_NAME: the name of the Cloud Run functions function you're deploying
     * PYTHON_RUNTIME_NAME: the name of one of the [supported Python runtimes](https://docs.cloud.google.com/functions/1stgendocs/concepts/execution-environment#python) to run your deployed function under - for example python311. This must be the same Python runtime version as you've used in your local development environment.
     * DIRECTORY:the name of the directory containing your vendored dependencies



For more details about using buildpacks, see [Build a function with buildpacks](https://docs.cloud.google.com/docs/buildpacks/build-function).

## Use private dependencies

### Private dependencies from Artifact Registry

An [Artifact Registry Python repository](https://docs.cloud.google.com/artifact-registry/docs/python/store-python) can host private dependencies for your Python function. When deploying to Cloud Run functions, the build process will automatically generate Artifact Registry credentials for the [Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account). You only need to include the Artifact Registry URL in your `requirements.txt` without generating additional credentials. For example:
    
    
    --index-url REPOSITORY_URL
    sampleapp
    Flask==0.10.1
    google-cloud-storage
    

If your build needs multiple repositories, use an [Artifact Registry virtual repository](https://cloud.google.com/artifact-registry/docs/repositories/virtual-repo) to safely control the order that pip searches your repositories.

### Private dependencies from other repositories

Dependencies are installed in a Cloud Build environment that does not provide access to SSH keys. Packages hosted in repositories that require SSH-based authentication must be vendored and uploaded alongside your project's code, as described in the previous section.

You can use the `pip install` command with the `-t DIRECTORY` flag to copy private dependencies into a local directory before deploying your app, as follows:

  1. Copy your dependency into a local directory:
         
         pip install -t DIRECTORY DEPENDENCY

  2. Add an empty `__init__.py` file to the `DIRECTORY` directory to turn it into a module.

  3. Import from this module to use your dependency:
         
         import DIRECTORY.DEPENDENCY




## Pre-installed packages

The following Python packages are automatically installed alongside your function during deployment. If you are using any of these packages in your function code, we recommend that you include the following versions in your `requirements.txt` file:

###  Python 3.7 
    
    
    aiohttp==3.14.3
    aiosignal==1.2.0
    async-timeout==4.0.2
    attrs==21.4.0
    cachetools==4.2.4
    certifi==2021.10.8
    chardet==4.0.0
    charset-normalizer==2.0.10
    click==8.0.3
    Flask==2.0.2
    frozenlist==1.2.0
    google-api-core==2.3.2
    google-api-python-client==2.34.0
    google-auth==2.3.3
    google-auth-httplib2==0.1.0
    google-cloud-core==2.2.1
    google-cloud-trace==1.5.1
    googleapis-common-protos==1.54.0
    grpcio==1.43.0
    grpcio-status==1.43.0
    httplib2==0.32.0
    idna==3.15
    itsdangerous==2.0.1
    Jinja2==3.1.6
    MarkupSafe==2.0.1
    multidict==5.2.0
    opencensus==0.8.0
    opencensus-context==0.1.2
    packaging==21.3
    proto-plus==1.19.8
    protobuf==3.19.1
    pyasn1==0.6.4
    pyasn1-modules==0.2.8
    pyparsing==3.0.6
    pytz==2021.3
    PyYAML==6.0
    requests==2.33.0
    rsa==4.8
    setuptools==83.0.0
    six==1.16.0
    uritemplate==4.1.1
    urllib3==1.26.7
    Werkzeug==2.0.2
    wrapt==1.13.3
    yarl==1.7.2
    

###  Python 3.8 and later 
    
    
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
    

**Note:** regardless of what's in your `requirements.txt` file, the following packages will always be pinned to a specific version:
    
    
    * `pip` (latest version)
    * `setuptools` (latest version)
    * `wheel` (determined by product requirements)
    

In addition, the Python runtime includes a number of [system packages](https://docs.cloud.google.com/functions/docs/reference/python-system-packages) in the execution environment. If your function uses a dependency that requires a system package that is not listed, you can [request a package](https://docs.cloud.google.com/functions/docs/reference/python-system-packages#requesting_a_package).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
