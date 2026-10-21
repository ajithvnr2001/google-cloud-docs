---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/quota/update/
title: gcloud alpha services quota update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:22.389968+00:00
---

# gcloud alpha services quota update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/quota/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha services quota update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha services quota update - update a quota override for a consumer 
SYNOPSIS
    

`gcloud alpha services quota update` `--consumer`=`CONSUMER` `--metric`=`METRIC` `--service`=`SERVICE` `--unit`=`UNIT` `--value`=`VALUE` [`--dimensions`=[`KEY`=`VALUE`,…]] [`--force`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command updates a quota override for a consumer. The supported consumers are projects, folders, and organizations. The override ID can be found from list command output. 
EXAMPLES
     To update a quota override for project with project number, run: 
    
    
    gcloud alpha services quota update --service=example.googleapis.com --consumer=projects/12321 --metric=example.googleapis.com/default_requests --unit=1/min/{project} --value=360

To update a quota override for project with project ID, run: 
    
    
    gcloud alpha services quota update --service=example.googleapis.com --consumer=projects/hello --metric=example.googleapis.com/default_requests --unit=1/min/{project} --value=360

To update a quota override for an organization, run: 
    
    
    gcloud alpha services quota update --service=example.googleapis.com --consumer=organizations/555 --metric=example.googleapis.com/default_requests --unit=1/min/{project} --value=360

To force the update of a quota override, run: 
    
    
    gcloud alpha services quota update --service=example.googleapis.com --consumer=projects/12321 --metric=example.googleapis.com/default_requests --unit=1/min/{project} --dimensions=regions=us-central1 --dimensions=zones=us-central1-c --value=360 --force

REQUIRED FLAGS
    

`--consumer`=`CONSUMER`
     The consumer to update override for. 
`--metric`=`METRIC`
     The metric to update a quota override for. 
`--service`=`SERVICE`
     The service to update a quota override for. 
`--unit`=`UNIT`
     The unit of a metric to update a quota override for. 
`--value`=`VALUE`
     The value of the override. 
OPTIONAL FLAGS
    

`--dimensions`=[`KEY`=`VALUE`,…]
     The dimensions of the override, e.g. for specific locations. 
`--force`
     Force override update even if the change results in a substantial decrease in available quota. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
