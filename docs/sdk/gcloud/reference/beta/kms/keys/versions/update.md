---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/update/
title: gcloud beta kms keys versions update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:09.117174+00:00
---

# gcloud beta kms keys versions update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta kms keys versions update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta kms keys versions update - update a key version 
SYNOPSIS
    

`gcloud beta kms keys versions update` `VERSION` [`--crypto-key-backend`=`CRYPTO_KEY_BACKEND`] [`--ekm-connection-key-path`=`EKM_CONNECTION_KEY_PATH`] [`--external-key-uri`=`EXTERNAL_KEY_URI`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--protection-level`=`PROTECTION_LEVEL`] [`--state`=`STATE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta kms keys versions update can be used to update the key versions. For keys of any protection level, you can update the key version's state to enable or disable it. 

For external keys, you can update the protection level to transition between the `external` and `external-vpc` protection levels. For key versions with the `external` protection level, you can also update the external key URI. For key versions with the `external-vpc` protection level, you can also update the ekm connection key path or the crypto key backend. 

EXAMPLES
     The following command enables the key version 8 of key `frodo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --state=enabled

The following command disables the key version 8 of key `frodo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --state=disabled

The following command updates the external key URI of version 8 of key `frodo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --external-key-uri=https://example.kms/v0/some/key/path

The following command updates the ekm connection key path of version 8 of key `bilbo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=bilbo --ekm-connection-key-path=v0/some/key/path

The following command updates the protection level to `external` and the external key URI of version 8 of key `frodo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=frodo --protection-level=external --external-key-uri=https://example.kms/v0/some/key/path

The following command updates the protection level to `external-vpc`, sets the crypto key backend, and sets the ekm connection key path of version 8 of key `bilbo` within keyring `fellowship` and location `us-east1`: 
    
    
    gcloud beta kms keys versions update 8 --location=us-east1 --keyring=fellowship --key=bilbo --protection-level=external-vpc --crypto-key-backend="projects/$(gcloud config get project)/locations/us-east1/ekmConnections/eagles" --ekm-connection-key-path=v0/some/key/path

POSITIONAL ARGUMENTS
    

`VERSION`
     Name of the version to describe. 
FLAGS
    

`--crypto-key-backend`=`CRYPTO_KEY_BACKEND`
     For key versions in the `external-vpc` protection level only, the resource name of the EkmConnection to be used by this key version. Required with the `--ekm-connection-key-path` flag when a key version is updated to the `external-vpc` protection level. 
`--ekm-connection-key-path`=`EKM_CONNECTION_KEY_PATH`
     The path to the external key material on the EKM for keys with protection level `external-vpc`. Required with the --crypto-key-backend flag when a key version is updated to the `external-vpc` protection level. 
`--external-key-uri`=`EXTERNAL_KEY_URI`
     The URI of the external key for keys with protection level `external`. 
`--key`=`KEY`
     The containing key. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--protection-level`=`PROTECTION_LEVEL`
     Protection level of the key version. Required when a key version is updated from `external` to `external-vpc` or from `external-vpc` to `external`. `PROTECTION_LEVEL` must be one of: `external`, `external-vpc`. 
`--state`=`STATE`
     State of the key version. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud kms keys versions update](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/update)
    
    
    [gcloud alpha kms keys versions update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
