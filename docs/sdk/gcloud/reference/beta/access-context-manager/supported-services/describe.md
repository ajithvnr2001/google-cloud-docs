---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/describe/
title: gcloud beta access-context-manager supported-services describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:38.097793+00:00
---

# gcloud beta access-context-manager supported-services describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/supported-services/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-context-manager supported-services describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-context-manager supported-services describe - gets information about a VPC Service Controls Supported Service 
SYNOPSIS
    

`gcloud beta access-context-manager supported-services describe` `SERVICE_NAME` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get service information allowed in an access policy object. 
EXAMPLES
     To get VPC Service Controls support information for `bigquery.googleapis.com`, run: 
    
    
    gcloud beta access-context-manager supported-services describe bigquery.googleapis.com

POSITIONAL ARGUMENTS
    

Supported service resource - VPC Service Controls supported service. This represents a Cloud resource. 

This must be specified. 

`SERVICE_NAME`
     ID of the supported-service or fully qualified identifier for the supported-service. 

To set the `service_name` attribute: 

  * provide the argument `service_name` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-context-manager supported-services describe](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/supported-services/describe)
    
    
    [gcloud alpha access-context-manager supported-services describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/supported-services/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
