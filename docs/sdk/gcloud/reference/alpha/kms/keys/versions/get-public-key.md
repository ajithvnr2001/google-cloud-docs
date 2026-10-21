---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/get-public-key/
title: gcloud alpha kms keys versions get-public-key \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:45.727136+00:00
---

# gcloud alpha kms keys versions get-public-key  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/get-public-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms keys versions get-public-key Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms keys versions get-public-key - get the public key for a given version 
SYNOPSIS
    

`gcloud alpha kms keys versions get-public-key` `VERSION` [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--output-file`=`OUTPUT_FILE`] [`--public-key-format`=`PUBLIC_KEY_FORMAT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Returns the public key of the given asymmetric key version in the specified format. 

The optional flag `output-file` indicates the path to store the public key. If not specified, the public key will be printed to stdout. 

The optional flag `public-key-format` indicates the format in which the public key will be returned. For the NIST PQC algorithms, this must be specified and set to `nist-pqc`. For kem-xwing this must be specified and set to `xwing-raw-bytes`. For all other algorithms, this flag is optional and can be either `pem` or `der`; the default value is `pem`. See "Retrieve a public key" in the Cloud KMS documentation (https://cloud.google.com/kms/help/get-public-key) for more information about the supported formats. 

EXAMPLES
     The following command saves the public key for CryptoKey `frodo` Version 2 to '/tmp/my/public_key.file': 
    
    
    gcloud alpha kms keys versions get-public-key 2 --key=frodo --keyring=fellowship --location=us-east1 --public-key-format=pem --output-file=/tmp/my/public_key.file

POSITIONAL ARGUMENTS
    

`VERSION`
     Name of the version to get public key. 
FLAGS
    

`--key`=`KEY`
     The containing key. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--output-file`=`OUTPUT_FILE`
     Path to the output file to store public key. 
`--public-key-format`=`PUBLIC_KEY_FORMAT`
     The format in which the public key will be returned. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms keys versions get-public-key](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/get-public-key)
    
    
    [gcloud beta kms keys versions get-public-key](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/get-public-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
