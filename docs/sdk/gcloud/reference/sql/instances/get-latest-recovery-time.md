---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time/
title: gcloud sql instances get-latest-recovery-time \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:39.474325+00:00
---

# gcloud sql instances get-latest-recovery-time  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql instances get-latest-recovery-time Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql instances get-latest-recovery-time - displays the latest recovery time to which a Cloud SQL instance can be restored to 
SYNOPSIS
    

`gcloud sql instances get-latest-recovery-time` `INSTANCE` [`--source-instance-deletion-time`=`SOURCE_INSTANCE_DELETION_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud sql instances get-latest-recovery-time` retrieves the latest recovery time for a Cloud SQL instance. This is the latest time that can be used to perform point in time recovery for the Cloud SQL instance. 
EXAMPLES
     To retrieve the latest recovery time for an instance: 
    
    
    gcloud sql instances get-latest-recovery-time instance-foo

To retrieve the latest recovery time for an instance that has been deleted: 
    
    
    gcloud sql instances get-latest-recovery-time instance-foo --source-instance-deletion-time '2012-11-15T16:19:00.094Z'

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
FLAGS
    

`--source-instance-deletion-time`=`SOURCE_INSTANCE_DELETION_TIME`
     The deletion time of the source instance. This is used to identify the instance if it has been deleted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql instances get-latest-recovery-time](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/get-latest-recovery-time)
    
    
    [gcloud beta sql instances get-latest-recovery-time](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/get-latest-recovery-time)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
