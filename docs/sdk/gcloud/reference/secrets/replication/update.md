---
url: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/replication/update/
title: gcloud secrets replication update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:41.369034+00:00
---

# gcloud secrets replication update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/replication/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud secrets replication update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud secrets replication update - update a secret replica's metadata 
SYNOPSIS
    

`gcloud secrets replication update` `SECRET` [`--remove-cmek` | `--location`=`REPLICA-LOCATION` `--set-kms-key`=`SET-KMS-KEY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a secret replica's metadata (e.g. cmek policy). This command will return an error if given a secret that does not exist or if given a location that the given secret doesn't exist in. 

The --remove-kms-key flag is only valid for Secrets that have an automatic replication policy or exist in a single location. To remove keys from a Secret with multiple user managed replicas, please use the set-replication command. 

EXAMPLES
     To remove CMEK from a secret called 'my-secret', run: 
    
    
    gcloud secrets replication update my-secret --remove-cmek

To set the CMEK key on an automatic secret called my-secret to a specified KMS key, run: 
    
    
    gcloud secrets replication update my-secret --set-kms-key=projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-key

To set the CMEK key on a secret called my-secret to a specified KMS key in a specified location in its replication, run: 
    
    
    gcloud secrets replication update my-secret --set-kms-key=projects/my-project/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key --location=us-central1

POSITIONAL ARGUMENTS
    

Secret resource - The secret to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `SECRET` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SECRET`
     ID of the secret or fully qualified identifier for the secret. 

To set the `secret` attribute: 

  * provide the argument `SECRET` on the command line. 


FLAGS
    

Replication update. 

At most one of these can be specified: 

`--remove-cmek`
     Remove customer managed encryption key so that future versions will be encrypted by a Google managed encryption key. 
Or at least one of these can be specified: 

CMEK Update. 
`--location`=`REPLICA-LOCATION`
     Location of replica to update. For secrets with automatic replication policies, this can be omitted. 
`--set-kms-key`=`SET-KMS-KEY`
     New KMS key with which to encrypt and decrypt future secret versions. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta secrets replication update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/secrets/replication/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
