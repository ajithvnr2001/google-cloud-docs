---
url: https://docs.cloud.google.com/sdk/gcloud/reference/info/
title: gcloud info \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:40.231363+00:00
---

# gcloud info  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud info Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud info - display information about the current gcloud environment 
SYNOPSIS
    

`gcloud info` [`--anonymize`] [`--show-log` | [`--run-diagnostics` : `--check-certs`=`HOSTNAME`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Display information about the current gcloud environment. 
EXAMPLES
     To display information about the current gcloud environment including the Google Cloud account, project and directory paths for logs, run: 
    
    
    gcloud info

To check network connectivity and hidden properties, run: 
    
    
    gcloud info --run-diagnostics

To troubleshoot certificate verification failures for a given host e.g. `compute.googleapis.com` when using a proxy and custom CA certs, run: 
    
    
    gcloud info --run-diagnostics --check-certs=compute.googleapis.com

To print the contents of the most recent log file, run: 
    
    
    gcloud info --show-log

FLAGS
    

`--anonymize`
     Minimize any personal identifiable information. Use it when sharing output with others. 
At most one of these can be specified: 

`--show-log`
     Print the contents of the last log file. 
Or at least one of these can be specified: 

`--run-diagnostics`
     Run diagnostics on your installation of the Google Cloud CLI. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--check-certs`=`HOSTNAME`
     Run diagnostics on the certificate chain for a given host. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
