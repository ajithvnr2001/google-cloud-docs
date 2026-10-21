---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule/
title: gcloud compute resource-policies update instance-schedule \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:35:39.345037+00:00
---

# gcloud compute resource-policies update instance-schedule  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute resource-policies update instance-schedule Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute resource-policies update instance-schedule - update a Compute Engine Instance Schedule Resource Policy 
SYNOPSIS
    

`gcloud compute resource-policies update instance-schedule` `NAME` [`--description`=`DESCRIPTION`] [`--end-date`=`END_DATE`] [`--initiation-date`=`INITIATION_DATE`] [`--region`=`REGION`] [`--timezone`=`TIMEZONE`] [`--vm-start-schedule`=`VM_START_SCHEDULE`] [`--vm-stop-schedule`=`VM_STOP_SCHEDULE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Compute Engine Instance Schedule Resource Policy. 
EXAMPLES
     To update an instance schedule resource policy with specified parameters: 
    
    
    gcloud compute resource-policies update instance-schedule NAME --region=REGION --timezone=UTC --vm-start-schedule="0 7 * * *" --vm-stop-schedule="0 17 * * *"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the resource policy to operate on. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional, textual description for the backend. 
`--end-date`=`END_DATE`
     The expiration time of the schedule policy. The timestamp must be an RFC3339 valid string. 
`--initiation-date`=`INITIATION_DATE`
     The start time of the schedule policy. The timestamp must be an RFC3339 valid string. 
`--region`=`REGION`
     Region of the resource policy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--timezone`=`TIMEZONE`
     Timezone used in interpreting schedule. The value of this field must be a time zone name from the tz database <http://en.wikipedia.org/wiki/Tz_database>
`--vm-start-schedule`=`VM_START_SCHEDULE`
     Schedule for starting the instance, specified using standard CRON format. 
`--vm-stop-schedule`=`VM_STOP_SCHEDULE`
     Schedule for stopping the instance, specified using standard CRON format. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute resource-policies update instance-schedule](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/resource-policies/update/instance-schedule)
    
    
    [gcloud beta compute resource-policies update instance-schedule](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/update/instance-schedule)
    
    
    [gcloud preview compute resource-policies update instance-schedule](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/resource-policies/update/instance-schedule)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
