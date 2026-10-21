---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/users/set-superuser/
title: gcloud beta alloydb users set-superuser \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:39.107876+00:00
---

# gcloud beta alloydb users set-superuser  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/users/set-superuser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta alloydb users set-superuser Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta alloydb users set-superuser - update an AlloyDB user's superuser role within a given cluster and region 
SYNOPSIS
    

`gcloud beta alloydb users set-superuser` `USERNAME` `--cluster`=`CLUSTER` `--region`=`REGION` `--superuser`=`SUPERUSER` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an AlloyDB user's superuser role within a given cluster and region. 
EXAMPLES
     To update a user's superuser role, run: 
    
    
    gcloud beta alloydb users set-superuser my-username --cluster=my-cluster --region=us-central1 --superuser=true/false

POSITIONAL ARGUMENTS
    

`USERNAME`
     AlloyDB username 
REQUIRED FLAGS
    

`--cluster`=`CLUSTER`
     AlloyDB cluster ID 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
`--superuser`=`SUPERUSER`
     If true, user will have AlloyDB superuser privileges 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud alloydb users set-superuser](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/users/set-superuser)
    
    
    [gcloud alpha alloydb users set-superuser](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/set-superuser)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
