---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/raw-encrypt/
title: gcloud alpha kms raw-encrypt \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:46.985759+00:00
---

# gcloud alpha kms raw-encrypt  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/raw-encrypt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms raw-encrypt Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms raw-encrypt - encrypt a plaintext file using a raw key 
SYNOPSIS
    

`gcloud alpha kms raw-encrypt` `--ciphertext-file`=`CIPHERTEXT_FILE` `--plaintext-file`=`PLAINTEXT_FILE` `--version`=`VERSION` [`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`] [`--initialization-vector-file`=`INITIALIZATION_VECTOR_FILE`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--skip-integrity-verification`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Encrypts the given plaintext file using the given CryptoKey containing a raw key and writes the result to the named ciphertext file. The plaintext file must not be larger than 64KiB. For the AES-CBC algorithms, no server-side padding is being done, so the plaintext must be a multiple of the block size. 

The supported algorithms are: `AES-128-GCM`, `AES-256-GCM`, `AES-128-CBC`, `AES-256-CBC`, `AES-128-CTR`, `and AES-256-CTR`. 

`AES-GCM` provides authentication which means that it accepts additional authenticated data (AAD). So, the flag `--additional-authenticated-data-file` is only valid with `AES-128-GCM` and `AES-256-GCM` algorithms. 

The initialization vector (flag `--initialization-vector-file`) is only supported for `AES-CBC` and `AES-CTR` algorithms, and must be 16B in length. 

Therefore, both additional authenticated data and initialization vector can't be provided during encryption. If an additional authenticated data file is provided, its contents must also be provided during decryption. The file must not be larger than 64KiB. 

The flag `--version` indicates the version of the key to use for encryption. 

If `--plaintext-file` or `--additional-authenticated-data-file` or `--initialization-vector-file` is set to '-', that file is read from stdin. Similarly, if `--ciphertext-file` is set to '-', the ciphertext is written to stdout. 

By default, the command performs integrity verification on data sent to and received from Cloud KMS. Use `--skip-integrity-verification` to disable integrity verification. 

EXAMPLES
     The following command reads and encrypts the file `path/to/input/plaintext`. The file will be encrypted using the `AES-GCM` CryptoKey `KEYNAME` from the KeyRing `KEYRING` in the `global` location using the additional authenticated data file `path/to/input/aad`. The resulting ciphertext will be written to `path/to/output/ciphertext`. 
    
    
    gcloud alpha kms raw-encrypt --key=KEYNAME --keyring=KEYRING --location=global --plaintext-file=path/to/input/plaintext --additional-authenticated-data-file=path/to/input/aad --ciphertext-file=path/to/output/ciphertext

The following command reads and encrypts the file `path/to/input/plaintext`. The file will be encrypted using the `AES-CBC` CryptoKey `KEYNAME` from the KeyRing `KEYRING` in the `global` location using the initialization vector stored at `path/to/input/aad`. The resulting ciphertext will be written to `path/to/output/ciphertext`. 
    
    
    gcloud alpha kms raw-encrypt --key=KEYNAME --keyring=KEYRING --location=global --plaintext-file=path/to/input/plaintext --initialization-vector-file=path/to/input/iv --ciphertext-file=path/to/output/ciphertext

REQUIRED FLAGS
    

`--ciphertext-file`=`CIPHERTEXT_FILE`
     File path of the ciphertext file to output. 
`--plaintext-file`=`PLAINTEXT_FILE`
     File path of the plaintext file to encrypt. 
`--version`=`VERSION`
     Version to use for encryption. 
OPTIONAL FLAGS
    

`--additional-authenticated-data-file`=`ADDITIONAL_AUTHENTICATED_DATA_FILE`
     File path to the optional file containing the additional authenticated data. 
`--initialization-vector-file`=`INITIALIZATION_VECTOR_FILE`
     File path to the optional file containing the initialization vector for encryption. 
`--key`=`KEY`
     The key to use for encryption. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms raw-encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt)
    
    
    [gcloud beta kms raw-encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/raw-encrypt)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
