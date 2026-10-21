---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update/
title: gcloud logging settings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:59:59.065098+00:00
---

# gcloud logging settings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging settings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging settings update - update the settings for the Cloud Logging Logs Router 
SYNOPSIS
    

`gcloud logging settings update` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID`) [`--disable-default-sink`] [`--storage-location`=`STORAGE_LOCATION`] [`--clear-kms-key` | [`--kms-key-name`=`KMS_KEY_NAME` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Use this command to update the `--kms-key-name, --storage-location, --disable-default-sink` and --analytics-mode associated with the Cloud Logging Logs Router. 

The Cloud KMS key must already exist and Cloud Logging must have permission to access it. 

The storage location must be allowed by Org Policy. 

Customer-managed encryption keys (CMEK) for the Logs Router can currently only be configured at the organization-level and will apply to all projects in the organization. 

EXAMPLES
     To enable CMEK for the Logs Router for an organization, run: 
    
    
    gcloud logging settings update --organization=[ORGANIZATION_ID] --kms-key-name='projects/my-project/locations/my-location/keyRings/my-keyring/cryptoKeys/key'

To disable CMEK for the Logs Router for an organization, run: 
    
    
    gcloud logging settings update --organization=[ORGANIZATION_ID] --clear-kms-key

To update storage location for the Logs Router for an organization, run: 
    
    
    gcloud logging settings update --organization=[ORGANIZATION_ID] --storage-location=[LOCATION_ID]

To update storage location for the Logs Router for a folder, run: 
    
    
    gcloud logging settings update --folder=[FOLDER_ID] --storage-location=[LOCATION_ID]

To disable default sink for the Logs Router for an organization, run: 
    
    
    gcloud logging settings update --organization=[ORGANIZATION_ID] --disable-default-sink=true

To enable default sink for the Logs Router for an organization, run: 
    
    
    gcloud logging settings update --organization=[ORGANIZATION_ID] --disable-default-sink=false

To enable analytics for the log buckets under an organization, run: 
    
    
    gcloud logging settings update --organization=[ORGANIZATION_ID] --disable-default-sink=false --analytics-mode=required

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder to update Logs Router settings for. 
`--organization`=`ORGANIZATION_ID`
     Organization to update Logs Router settings for. 
OPTIONAL FLAGS
    

`--disable-default-sink`
     Enable or disable `_Default` sink for the `_Default` bucket. Specify --no-disable-default-sink to enable a disabled `_Default` sink. Note: It only applies to the newly created projects and will not affect the projects created before. 
`--storage-location`=`STORAGE_LOCATION`
     Update the storage location for `_Default` bucket and `_Required` bucket. Note: It only applies to the newly created projects and will not affect the projects created before. 
At most one of these can be specified: 

`--clear-kms-key`
     Disable CMEK for the Logs Router by clearing out Cloud KMS cryptokey in the organization's CMEK settings. 
Or at least one of these can be specified: 

Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the logs being processed by the Cloud Logging Logs Router. The Cloud KMS CryptoKey Encrypter/Decryper role must be assigned to the Cloud Logging Logs Router service account. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key-name`=`KMS_KEY_NAME`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key-name` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key-name` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key-name` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key-name` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha logging settings update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/settings/update)
    
    
    [gcloud beta logging settings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/settings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
