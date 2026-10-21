---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/gen-config/
title: gcloud beta app gen-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:57.940013+00:00
---

# gcloud beta app gen-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/gen-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app gen-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app gen-config - generate missing configuration files for a source directory 
SYNOPSIS
    

`gcloud beta app gen-config` [`SOURCE_DIR`] [`--config`=`CONFIG`] [`--custom`] [`--runtime`=`RUNTIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` This command is deprecated and will soon be removed. 

As an alternative, create an app.yaml file yourself using the directions at <https://cloud.google.com/appengine/docs/flexible/reference/app-yaml> (App Engine flexible environment) or <https://cloud.google.com/appengine/docs/standard/reference/app-yaml> (App Engine standard environment) under the tab for your language. 

To create a custom runtime, please follow the instructions at <https://cloud.google.com/appengine/docs/flexible/custom-runtimes/> This command generates all relevant config files (app.yaml, Dockerfile and a build Dockerfile) for your application in the current directory or emits an error message if the source directory contents are not recognized. 

EXAMPLES
     To generate configs for the current directory: 
    
    
    gcloud beta app gen-config

To generate configs for ~/my_app: 
    
    
    gcloud beta app gen-config ~/my_app

POSITIONAL ARGUMENTS
    

[`SOURCE_DIR`]
     The source directory to fingerprint. 
FLAGS
    

`--config`=`CONFIG`
     The yaml file defining the service configuration. This is normally one of the generated files, but when generating a custom runtime there can be an app.yaml containing parameters. 
`--custom`
     If true, generate config files for a custom runtime. This will produce a Dockerfile, a .dockerignore file and an app.yaml (possibly other files as well, depending on the runtime). 
`--runtime`=`RUNTIME`
     Generate config files for a given runtime. Can be used in conjunction with \--custom. Allowed runtimes are: contrib-dart, dart, go, php, php55, php72, python, python27, python-compat, java, java7, java8, nodejs, ruby, go111, go112. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
