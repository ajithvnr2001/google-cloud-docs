---
url: https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup/
title: gcloud topic startup \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:37.498957+00:00
---

# gcloud topic startup  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud topic startup Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud topic startup - supplementary help for gcloud startup options 
DESCRIPTION
     This page provides supplementary help for configuring the gcloud command-line tool's startup behavior, including Python interpreter selection and environment variables. 
CONFIGURING THE PYTHON INTERPRETER
     The `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` CLI requires a compatible Python version (3.10-3.15) to run. In most gcloud CLI installations, the gcloud installer manages the Python installation (version 3.14) for the user. Configuring the Python interpreter is only supported in specific scenarios described below. 
When to Use `CLOUDSDK_PYTHON` environment variable
     You can ONLY consider using the CLOUDSDK_PYTHON environment variable when you are on: 

  * `Linux`: Installing from a versioned archives (`*.tar.gz*`) on ARM or x86 architectures where Python is NOT included as part of the installation, gcloud will search for a compatible Python on your system PATH (looking for python3 then python). You can set the `CLOUDSDK_PYTHON` environment variable to the full path of your preferred compatible Python interpreter if the default one found on PATH is not desired. 
  * `macOS`: Available only for archived install and where the Python version matches the Python version managed by the gcloud CLI Tools install. Note that this is not available for Homebrew installations of gcloud CLI Tools. 
  * `Windows`: gcloud installer includes the required Python interpreter by default. Only use `CLOUDSDK_PYTHON` if you need to use a different Python installation. 



Example Usages: 
    
    
    # Use the python3 interpreter on your path
    export CLOUDSDK_PYTHON=python3
    
    
    # Use a python you have installed in a special location
    export CLOUDSDK_PYTHON=/usr/local/my-custom-python-install/python

Other Components
     `gsutil` versions 5.0 and later support Python 3.10-3.14. To use a different interpreter for `gsutil` than for the other Python tools, set the `CLOUDSDK_GSUTIL_PYTHON` environment variable to the interpreter that you want. 

`bq` versions 2.0.99 and later support Python 3.10-3.15. To use a different interpreter for `bq` than for the other Python tools, set the `CLOUDSDK_BQ_PYTHON` environment variable to the interpreter that you want. 

SETTING CONFIGURATIONS AND PROPERTIES
     Your active configuration can also be set via the environment variable `CLOUDSDK_ACTIVE_CONFIG_NAME`. This allows you to specify a certain configuration in a given terminal session without changing the global default configuration. 

In addition to being able to set them via `[gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set)`, each `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` property has a corresponding environment variable. They take the form: `CLOUDSDK_SECTION_PROPERTY`. For example, if you wanted to change your active project for just one terminal you could run: 
    
    
    export CLOUDSDK_CORE_PROJECT=my-project

For more information, see `[gcloud topic configurations](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations)`. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha topic startup](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/startup)
    
    
    [gcloud beta topic startup](https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/startup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
