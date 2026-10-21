---
url: https://docs.cloud.google.com/run/docs/runtimes/python/
title: The Python runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:51.998794+00:00
---

# The Python runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The Python runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [Python Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-python) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for Python development, see [Set up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

## Supported Python runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Python 3.14 | python314 | 
* google-24 (default)
* google-24-full
| 
* [google-24/python314](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/python314)
* [google-24-full/python314](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/python314)
| 2030-10-10 | 2031-04-10  
Python 3.13 | python313 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python313](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python313)
* [google-22-full/python313](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python313)
| 2029-10-10 | 2030-04-10  
Python 3.12 | python312 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python312](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python312)
* [google-22-full/python312](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python312)
| 2028-10-02 | 2029-04-02  
Python 3.11 | python311 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python311](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python311)
* [google-22-full/python311](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python311)
| 2027-10-24 | 2028-04-24 | Python 3.10 | python310 | 
* google-22 (default)
* google-22-full
| 
* [google-22/python310](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/python310)
* [google-22-full/python310](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/python310)
| 2026-10-04 | 2027-04-04  
Python 3.9 | python39 |  google-18-full  |  [google-18-full/python39](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python39) | 2025-10-05 | 2026-04-05  
Python 3.8 | python38 |  google-18-full  |  [google-18-full/python38](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python38) | 2024-10-14 | 2025-10-14  
Python 3.7 | python37 |  google-18-full  |  [google-18-full/python37](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/python37) | 2024-01-30 | 2025-01-30  
  
## Select your runtime

You can select one of the supported Python runtimes for your function during deployment. 

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [Python base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image python314
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a Python runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#python) for more information.

## Specify dependencies

There are several ways to specify dependencies for Cloud Run functions in Python: use a package manager's `requirements.txt` file, configure a `pyproject.toml` file as the standard project definition file, or package local dependencies alongside your function. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies).

Cloud Run functions doesn't support specifying dependencies with the `Pipfile/Pipfile.lock`, so your project shouldn't include these files.

## Environment variables

Your Python runtime automatically sets certain environment variables for your function to use as needed. For details, see [Configure environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
