---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/create/
title: gcloud alpha kms keys versions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:44.231928+00:00
---

# gcloud alpha kms keys versions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms keys versions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms keys versions create - create a new version 
SYNOPSIS
    

`gcloud alpha kms keys versions create` [`--ekm-connection-key-path`=`EKM_CONNECTION_KEY_PATH`] [`--external-key-uri`=`EXTERNAL_KEY_URI`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--primary`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a new version within the given key. 
EXAMPLES
     The following command creates a new version within the `frodo` key, `fellowship` keyring, and `global` location and sets it as the primary version: 
    
    
    gcloud alpha kms keys versions create --location=global --keyring=fellowship --key=frodo --primary

The following command creates a new version within the `legolas` key, `fellowship` keyring, `us-central1` location, `https://example.kms/v0/some/key/path` as the address for its external key, and sets it as the key's primary version: 
    
    
    gcloud alpha kms keys versions create --location=us-central1 --keyring=fellowship --key=legolas --external-key-uri=https://example.kms/v0/some/key/path --primary

The following command creates a new version within the `bilbo` key, `fellowship` keyring, `us-central1` location, `v0/some/key/path` as the ekm connection key path for its external key, and sets it as the key's primary version: 
    
    
    gcloud alpha kms keys versions create --location=us-central1 --keyring=fellowship --key=bilbo --ekm-connection-key-path=v0/some/key/path --primary

FLAGS
    

`--ekm-connection-key-path`=`EKM_CONNECTION_KEY_PATH`
     The path to the external key material on the EKM for keys with protection level `external-vpc`. 
`--external-key-uri`=`EXTERNAL_KEY_URI`
     The URI of the external key for keys with protection level `external`. 
`--key`=`KEY`
     The containing key. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--primary`
     If specified, immediately makes the new version primary. This should only be used with the `encryption` purpose. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms keys versions create](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/create)
    
    
    [gcloud beta kms keys versions create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
