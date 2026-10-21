---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/raw-decrypt/
title: gcloud beta kms raw-decrypt \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:10.773596+00:00
---

# gcloud beta kms raw-decrypt  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/raw-decrypt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta kms raw-decrypt Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta kms raw-decrypt - decrypt a ciphertext file using a raw key 
SYNOPSIS
    

`gcloud beta kms raw-decrypt` `--ciphertext-file`=`CIPHERTEXT_FILE` `--plaintext-file`=`PLAINTEXT_FILE` `--version`=`VERSION` [`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`--initialization-vector-file`=`INITIALIZATION_VECTOR_FILE`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--skip-integrity-verification`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta kms raw-decrypt` decrypts the given ciphertext file using the given CryptoKey containing a raw key and writes the result to the named plaintext file. The ciphertext file must not be larger than 64KiB. 

The supported algorithms are: `AES-128-GCM`, `AES-256-GCM`, `AES-128-CBC`, `AES-256-CBC`, `AES-128-CTR`, `and AES-256-CTR`. 

`AES-GCM` provides authentication which means that it accepts additional authenticated data (AAD). So, the flag `--additional-authenticated-data-file` is only valid with `AES-128-GCM` and `AES-256-GCM` algorithms. If AAD is provided during encryption, it must be provided during decryption too. The file must not be larger than 64KiB. 

If `--plaintext-file` or `--additional-authenticated-data-file` or `--initialization-vector-file` is set to '-', that file is read from stdin. Similarly, if `--ciphertext-file` is set to '-', the ciphertext is written to stdout. 

By default, the command performs integrity verification on data sent to and received from Cloud KMS. Use `--skip-integrity-verification` to disable integrity verification. 

EXAMPLES
     The following command reads and decrypts the file `path/to/input/ciphertext`. The file will be decrypted using the CryptoKey `KEYNAME` containing a raw key, from the KeyRing `KEYRING` in the `global` location. It uses the additional authenticated data file `path/to/input/aad` (only valid with the `AES-GCM` algorithms) and the initialization vector file `path/to/input/iv`. The resulting plaintext will be written to `path/to/output/plaintext`. 
    
    
    gcloud beta kms raw-decrypt --key=KEYNAME --keyring=KEYRING --location=global --ciphertext-file=path/to/input/ciphertext --additional-authenticated-data-file=path/to/input/aad --initialization-vector-file=path/to/input/iv --plaintext-file=path/to/output/plaintext

REQUIRED FLAGS
    

`--ciphertext-file`=`CIPHERTEXT_FILE`
     File path of the ciphertext file to decrypt. 
`--plaintext-file`=`PLAINTEXT_FILE`
     File path of the plaintext file to store the decrypted data. 
`--version`=`VERSION`
     Version to use for decryption. 
OPTIONAL FLAGS
    

`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`
     File path to the optional file containing the additional authenticated data. 
`--initialization-vector-file`=`INITIALIZATION_VECTOR_FILE`
     File path to the optional file containing the initialization vector for decryption. 
`--key`=`KEY`
     The (raw) key to use for decryption. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--skip-integrity-verification`
     Skip integrity verification on request and response API fields. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud kms raw-decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt)
    
    
    [gcloud alpha kms raw-decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/raw-decrypt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
