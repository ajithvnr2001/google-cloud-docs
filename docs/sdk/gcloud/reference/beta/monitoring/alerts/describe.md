---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/alerts/describe/
title: gcloud beta monitoring alerts describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:09:49.459363+00:00
---

# gcloud beta monitoring alerts describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/alerts/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta monitoring alerts describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta monitoring alerts describe - describe an alert 
SYNOPSIS
    

`gcloud beta monitoring alerts describe` `ALERT` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Describe an alert. 
EXAMPLES
     To describe an alert, run: 
    
    
    gcloud beta monitoring alerts describe MY-ALERT

To describe an alert in JSON, run: 
    
    
    gcloud beta monitoring alerts describe MY-ALERT --format=json

To describe an alert contained within a specific project, run: 
    
    
    gcloud beta monitoring alerts describe MY-ALERT --project=MY-PROJECT

To describe an alert with a fully qualified alert ID, run: 
    
    
    gcloud beta monitoring alerts describe projects/MY-PROJECT/alerts/MY-ALERT

POSITIONAL ARGUMENTS
    

Alert resource - The alert to describe. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `alert` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ALERT`
     ID of the alert or fully qualified identifier for the alert. 

To set the `alert` attribute: 

  * provide the argument `alert` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `monitoring/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/monitoring/api/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud monitoring alerts describe](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/alerts/describe)
    
    
    [gcloud alpha monitoring alerts describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/alerts/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
