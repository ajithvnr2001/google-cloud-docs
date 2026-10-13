---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/cmek-config/update/
title: gcloud beta tasks cmek-config update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:22.248555+00:00
---

# gcloud beta tasks cmek-config update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/cmek-config/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta tasks cmek-config update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta tasks cmek-config update - enable, disable, or edit CMEK configuration for Cloud Tasks in the specified location 
SYNOPSIS
    

`gcloud beta tasks cmek-config update` [`--location`=`LOCATION`] [`--clear-kms-key` | [`--kms-key-name`=`KMS_KEY_NAME` : `--kms-keyring`=`KMS_KEYRING` `--kms-project`=`KMS_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Enable, disable, or edit CMEK configuration for Cloud Tasks in the specified location. 
EXAMPLES
     To update a CMEK config: 
    
    
    gcloud beta tasks cmek-config update --kms-key-name=projects/my-project/locations/my-location/keyRings/my-keyring/cryptoKeys/key

FLAGS
    

`--location`=`LOCATION`
     Google Cloud location for the KMS key. 
Flags for Clearing or Updating CMEK Resource 

At most one of these can be specified: 

Flags for clearing CMEK Resource key. 
`--clear-kms-key`
     Disables CMEK for Cloud Tasks in the specified location by clearing the Cloud KMS cryptokey from the Cloud Tasks project and CMEK configuration. 
Flags for Updating CMEK Resource key 
`--kms-key-name`=`KMS_KEY_NAME`
     Fully qualified identifier for the key or just the key ID. The latter requires that the --kms-keyring and --kms-project flags be provided too. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     KMS keyring of the KMS key. 
`--kms-project`=`KMS_PROJECT`
     Google Cloud project for the KMS key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud tasks cmek-config update](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/cmek-config/update)
    
    
    [gcloud alpha tasks cmek-config update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/cmek-config/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
