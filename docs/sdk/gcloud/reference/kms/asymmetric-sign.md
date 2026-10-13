---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign/
title: gcloud kms asymmetric-sign \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:43.422034+00:00
---

# gcloud kms asymmetric-sign  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms asymmetric-sign Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms asymmetric-sign - sign a user input file using an asymmetric-signing key version 
SYNOPSIS
    

`gcloud kms asymmetric-sign` `--input-file`=`INPUT_FILE` `--signature-file`=`SIGNATURE_FILE` [`--digest-algorithm`=`DIGEST_ALGORITHM`] [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--skip-integrity-verification`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a digital signature of the input file using the provided asymmetric-signing key version and saves the base64 encoded signature. 

The required flag `signature-file` indicates the path to store signature. 

By default, the command performs integrity verification on data sent to and received from Cloud KMS. Use `--skip-integrity-verification` to disable integrity verification. 

For the ML-DSA EXTERNAL-MU algorithms, the digest `external-mu` should be used that depends on the public key. This command will fetch the public key from KMS and compute the `external-mu` digest. Note that this requires `signer` permissions on the associated CryptoKeyVersion. 

EXAMPLES
     The following command will read the file '/tmp/my/file.to.sign', digest it with the digest algorithm 'sha256' and sign it using the asymmetric CryptoKey `dont-panic` Version 3, and save the signature in base64 format to '/tmp/my/signature'. 
    
    
    gcloud kms asymmetric-sign --location=us-central1 --keyring=hitchhiker --key=dont-panic --version=3 --digest-algorithm=sha256 --input-file=/tmp/my/file.to.sign --signature-file=/tmp/my/signature

REQUIRED FLAGS
    

`--input-file`=`INPUT_FILE`
     Path to the input file to sign. 
`--signature-file`=`SIGNATURE_FILE`
     Path to the signature file to output. 
OPTIONAL FLAGS
    

`--digest-algorithm`=`DIGEST_ALGORITHM`
     The algorithm to digest the input. `DIGEST_ALGORITHM` must be one of: `external-mu`, `sha256`, `sha384`, `sha512`. 
`--key`=`KEY`
     to use for signing. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--skip-integrity-verification`
     Skip integrity verification on request and response API fields. 
`--version`=`VERSION`
     Version to use for signing. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms asymmetric-sign](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/asymmetric-sign)
    
    
    [gcloud beta kms asymmetric-sign](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/asymmetric-sign)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
