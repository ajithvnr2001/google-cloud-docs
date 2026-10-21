---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/decrypt/
title: gcloud beta kms decrypt \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:58.033363+00:00
---

# gcloud beta kms decrypt  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/decrypt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta kms decrypt Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta kms decrypt - decrypt a ciphertext file using a Cloud KMS key 
SYNOPSIS
    

`gcloud beta kms decrypt` `--ciphertext-file`=`CIPHERTEXT_FILE` `--plaintext-file`=`PLAINTEXT_FILE` [`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--skip-integrity-verification`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta kms decrypt` decrypts the given ciphertext file using the given Cloud KMS key and writes the result to the named plaintext file. Note that to permit users to decrypt using a key, they must be have at least one of the following IAM roles for that key: `roles/cloudkms.cryptoKeyDecrypter`, `roles/cloudkms.cryptoKeyEncrypterDecrypter`. 

Additional authenticated data (AAD) is used as an additional check by Cloud KMS to authenticate a decryption request. If an additional authenticated data file is provided, its contents must match the additional authenticated data provided during encryption and must not be larger than 64KiB. If you don't provide a value for `--additional-authenticated-data-file`, an empty string is used. For a thorough explanation of AAD, refer to this guide: <https://cloud.google.com/kms/docs/additional-authenticated-data>

If `--ciphertext-file` or `--additional-authenticated-data-file` is set to '-', that file is read from stdin. Note that both files cannot be read from stdin. Similarly, if `--plaintext-file` is set to '-', the decrypted plaintext is written to stdout. 

By default, the command performs integrity verification on data sent to and received from Cloud KMS. Use `--skip-integrity-verification` to disable integrity verification. 

EXAMPLES
     To decrypt the file 'path/to/ciphertext' using the key `frodo` with key ring `fellowship` and location `global` and write the plaintext to 'path/to/plaintext.dec', run: 
    
    
    gcloud beta kms decrypt --key=frodo --keyring=fellowship --location=global --ciphertext-file=path/to/input/ciphertext --plaintext-file=path/to/output/plaintext.dec

To decrypt the file 'path/to/ciphertext' using the key `frodo` and the additional authenticated data that was used to encrypt the ciphertext, and write the decrypted plaintext to stdout, run: 
    
    
    gcloud beta kms decrypt --key=frodo --keyring=fellowship --location=global --additional-authenticated-data-file=path/to/aad --ciphertext-file=path/to/input/ciphertext --plaintext-file='-'

REQUIRED FLAGS
    

`--ciphertext-file`=`CIPHERTEXT_FILE`
     File path of the ciphertext file to decrypt. This file should contain the result of encrypting a file with `[gcloud kms encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/encrypt)`. 
`--plaintext-file`=`PLAINTEXT_FILE`
     File path of the plaintext file to output. 
OPTIONAL FLAGS
    

`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`
     File path to the optional file containing the additional authenticated data. 
`--key`=`KEY`
     Cloud KMS key to use for decryption. 

  * For symmetric keys, Cloud KMS detects the decryption key version from the ciphertext. If you specify a key version as part of a symmetric decryption request, an error is logged and decryption fails. 
  * For asymmetric keys, the encryption key version can't be detected automatically. You must keep track of this information and provide the key version in the decryption request. The key version itself is not sensitive data and does not need to be encrypted. 


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
    
    
    [gcloud kms decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/decrypt)
    
    
    [gcloud alpha kms decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/decrypt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
