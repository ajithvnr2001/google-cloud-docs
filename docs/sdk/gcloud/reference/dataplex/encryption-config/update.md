---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/update/
title: gcloud dataplex encryption-config update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:19.432583+00:00
---

# gcloud dataplex encryption-config update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/encryption-config/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataplex encryption-config update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataplex encryption-config update - update an Encryption Config 
SYNOPSIS
    

`gcloud dataplex encryption-config update` (`ENCRYPTION_CONFIG` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--enable-metastore-encryption`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an Encryption Config. 
EXAMPLES
     To update EncryptionConfig in organization `123` and location `us-central1`, run: 
    
    
    gcloud dataplex encryption-config update organizations/123/locations/us-central1/encryptionConfigs/default --enable-metastore-encryption

POSITIONAL ARGUMENTS
    

Encryption config resource - Arguments and flags that define the Dataplex EncryptionConfig you want to update. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`ENCRYPTION_CONFIG`
     ID of the encryption config or fully qualified identifier for the encryption config. 

To set the `encryption_config` attribute: 

  * provide the argument `encryption_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `encryption_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


`--organization`=`ORGANIZATION`
     The name of encryption config to use. 

To set the `organization` attribute: 

  * provide the argument `encryption_config` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


FLAGS
    

`--enable-metastore-encryption`
     Helps user to explicitly enable cmek encryption for dataplex metadata storage. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha dataplex encryption-config update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/encryption-config/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
