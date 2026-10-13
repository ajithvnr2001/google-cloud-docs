---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/enable/
title: gcloud beta kms keys versions enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:07.446812+00:00
---

# gcloud beta kms keys versions enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta kms keys versions enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta kms keys versions enable - enable a given version 
SYNOPSIS
    

`gcloud beta kms keys versions enable` `VERSION` [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Enables the specified version within the given key. 

Only a version which is Disabled can be Enabled. 

EXAMPLES
     The following command enables version 3 of key `frodo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions enable 3 --location=us-east1 --keyring=fellowship --key=frodo

POSITIONAL ARGUMENTS
    

`VERSION`
     Name of the version to enable. 
FLAGS
    

`--key`=`KEY`
     The containing key. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud kms keys versions enable](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/enable)
    
    
    [gcloud alpha kms keys versions enable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/enable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
