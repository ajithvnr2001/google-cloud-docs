---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/encrypt/
title: gcloud beta kms encrypt \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:59.891156+00:00
---

# gcloud beta kms encrypt  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/encrypt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta kms encrypt Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta kms encrypt - encrypt a plaintext file using a key 
SYNOPSIS
    

`gcloud beta kms encrypt` `--ciphertext-file`=`CIPHERTEXT_FILE` `--plaintext-file`=`PLAINTEXT_FILE` [`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--skip-integrity-verification`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Encrypts the given plaintext file using the given CryptoKey and writes the result to the named ciphertext file. The plaintext file must not be larger than 64KiB. 

If an additional authenticated data file is provided, its contents must also be provided during decryption. The file must not be larger than 64KiB. 

The flag `--version` indicates the version of the key to use for encryption. By default, the primary version is used. 

If `--plaintext-file` or `--additional-authenticated-data-file` is set to '-', that file is read from stdin. Similarly, if `--ciphertext-file` is set to '-', the ciphertext is written to stdout. 

By default, the command performs integrity verification on data sent to and received from Cloud KMS. Use `--skip-integrity-verification` to disable integrity verification. 

EXAMPLES
     The following command will read the file 'path/to/plaintext', encrypt it using the CryptoKey `frodo` with the KeyRing `fellowship` and Location `global`, and write the ciphertext to 'path/to/ciphertext'. 
    
    
    gcloud beta kms encrypt --key=frodo --keyring=fellowship --location=global --plaintext-file=path/to/input/plaintext --ciphertext-file=path/to/output/ciphertext

REQUIRED FLAGS
    

`--ciphertext-file`=`CIPHERTEXT_FILE`
     File path of the ciphertext file to output. 
`--plaintext-file`=`PLAINTEXT_FILE`
     File path of the plaintext file to encrypt. 
OPTIONAL FLAGS
    

`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`
     File path to the optional file containing the additional authenticated data. 
`--key`=`KEY`
     The key to use for encryption. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--skip-integrity-verification`
     Skip integrity verification on request and response API fields. 
`--version`=`VERSION`
     Version to use for encryption. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud kms encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/encrypt)
    
    
    [gcloud alpha kms encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/encrypt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
