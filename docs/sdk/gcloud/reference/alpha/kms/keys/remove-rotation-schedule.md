---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/remove-rotation-schedule/
title: gcloud alpha kms keys remove-rotation-schedule \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:08:48.721589+00:00
---

# gcloud alpha kms keys remove-rotation-schedule  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/remove-rotation-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms keys remove-rotation-schedule Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms keys remove-rotation-schedule - remove the rotation schedule for a key 
SYNOPSIS
    

`gcloud alpha kms keys remove-rotation-schedule` (`KEY` : `--keyring`=`KEYRING` `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Removes the rotation schedule for the given key. 
EXAMPLES
     The following command removes the rotation schedule for the key named `frodo` within the keyring `fellowship` and location `global`: 
    
    
    gcloud alpha kms keys remove-rotation-schedule frodo --location=global --keyring=fellowship

POSITIONAL ARGUMENTS
    

Key resource - The KMS key resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `key` attribute: 

  * provide the argument `key` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--keyring`=`KEYRING`
     The KMS keyring of the key. 

To set the `keyring` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--keyring` on the command line. 


`--location`=`LOCATION`
     The Google Cloud location for the key. 

To set the `location` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms keys remove-rotation-schedule](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/remove-rotation-schedule)
    
    
    [gcloud beta kms keys remove-rotation-schedule](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/remove-rotation-schedule)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
