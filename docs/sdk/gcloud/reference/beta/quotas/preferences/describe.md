---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/preferences/describe/
title: gcloud beta quotas preferences describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:17.482343+00:00
---

# gcloud beta quotas preferences describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/preferences/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta quotas preferences describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta quotas preferences describe - get details about a single QuotaPreference 
SYNOPSIS
    

`gcloud beta quotas preferences describe` `PREFERENCE_ID` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID_OR_NUMBER`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To get the details about quota preference `my-preference` for `projects/12321`, run: 
    
    
    gcloud beta quotas preferences describe my-preference --project=12321
    gcloud beta quotas preferences describe my-preference --project=my-project-id

To get the details about quota preference `my-preference` for `folders/123`, run: 
    
    
    gcloud beta quotas preferences describe my-preference --folder=123

POSITIONAL ARGUMENTS
    

`PREFERENCE_ID`
     ID of the Quota Preference object, must be unique under its parent. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder of the quota preference to describe. 
`--organization`=`ORGANIZATION_ID`
     Organization of the quota preference to describe. 
`--project`=`PROJECT_ID_OR_NUMBER`
     Project of the quota preference to describe. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud quotas preferences describe](https://docs.cloud.google.com/sdk/gcloud/reference/quotas/preferences/describe)
    
    
    [gcloud alpha quotas preferences describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/preferences/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
