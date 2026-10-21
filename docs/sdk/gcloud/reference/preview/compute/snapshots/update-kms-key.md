---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/update-kms-key/
title: gcloud preview compute snapshots update-kms-key \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:45:43.470201+00:00
---

# gcloud preview compute snapshots update-kms-key  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/update-kms-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute snapshots update-kms-key Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute snapshots update-kms-key - update the KMS key of a Compute Engine standard or archive snapshot 
SYNOPSIS
    

`gcloud preview compute snapshots update-kms-key` `SNAPSHOT_NAME` [`--region`=`REGION`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute snapshots update-kms-key` updates the KMS key of a Compute Engine standard or archive snapshot by rotating it to the primary version of the key or to the primary version of a new KMS key. 
EXAMPLES
     To update the KMS key of a snapshot named `example-snapshot-1`, run: 
    
    
    gcloud preview compute snapshots update-kms-key example-snapshot-1

To update the KMS key of a snapshot named `example-snapshot-2` to a new KMS key named example-key in a key ring named example-key-ring in the global scope, run: 
    
    
    gcloud preview compute snapshots update-kms-key example-snapshot-2 --kms-key=example-key --kms-keyring=example-key-ring --kms-location=global

POSITIONAL ARGUMENTS
    

`SNAPSHOT_NAME`
     Name of the snapshot to update the KMS key for. 
FLAGS
    

`--region`=`REGION`
     The region of the snapshot to update. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the snapshot. The 'Compute Engine Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line; 
  * provide the argument `--region` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute snapshots update-kms-key](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/update-kms-key)
    
    
    [gcloud alpha compute snapshots update-kms-key](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/update-kms-key)
    
    
    [gcloud beta compute snapshots update-kms-key](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/update-kms-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
