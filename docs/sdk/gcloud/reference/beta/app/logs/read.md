---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/logs/read/
title: gcloud beta app logs read \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:59.156046+00:00
---

# gcloud beta app logs read  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app/logs/read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app logs read Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app logs read - reads log entries for the current App Engine app 
SYNOPSIS
    

`gcloud beta app logs read` [`--level`=`LEVEL`; default="any"] [`--limit`=`LIMIT`; default=200] [`--logs`=`APP_LOG`,[`APP_LOG`,…]; default=`"stderr,`stdout,crash.log,nginx.request,request_log"] [`--service`=`SERVICE`, `-s` `SERVICE`] [`--version`=`VERSION`, `-v` `VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Display the latest log entries from stdout, stderr and crash log for the current Google App Engine app in a human readable format. This command requires that the caller have the logging.logEntries.list permission. 
EXAMPLES
     To display the latest entries for the current app, run: 
    
    
    gcloud beta app logs read

To show only the entries with severity at `warning` or higher, run: 
    
    
    gcloud beta app logs read --level=warning

To show only the entries with a specific version, run: 
    
    
    gcloud beta app logs read --version=v1

To show only the 10 latest log entries for the default service, run: 
    
    
    gcloud beta app logs read --limit=10 --service=default

To show only the logs from the request log for standard apps, run: 
    
    
    gcloud beta app logs read --logs=request_log

To show only the logs from the request log for Flex apps, run: 
    
    
    gcloud beta app logs read --logs=nginx.request

FLAGS
    

`--level`=`LEVEL`; default="any"
     Filter entries with severity equal to or higher than a given level. `LEVEL` must be one of: `critical`, `error`, `warning`, `info`, `debug`, `any`. 
`--limit`=`LIMIT`; default=200
     Number of log entries to show. 
`--logs`=`APP_LOG`,[`APP_LOG`,…]; default=`"stderr,stdout,crash.log,nginx.request,request_log"`
     Filter entries from a particular set of logs. Must be a comma-separated list of log names (request_log, stdout, stderr, etc). 
`--service`=`SERVICE`, `-s` `SERVICE`
     Limit to specific service. 
`--version`=`VERSION`, `-v` `VERSION`
     Limit to specific version. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud app logs read](https://docs.cloud.google.com/sdk/gcloud/reference/app/logs/read)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
