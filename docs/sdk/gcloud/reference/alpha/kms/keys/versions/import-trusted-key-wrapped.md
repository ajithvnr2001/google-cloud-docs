---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/import-trusted-key-wrapped/
title: gcloud alpha kms keys versions import-trusted-key-wrapped \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:45.641856+00:00
---

# gcloud alpha kms keys versions import-trusted-key-wrapped  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys/versions/import-trusted-key-wrapped/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms keys versions import-trusted-key-wrapped Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms keys versions import-trusted-key-wrapped - import a trusted key wrapped CryptoKeyVersion 
SYNOPSIS
    

`gcloud alpha kms keys versions import-trusted-key-wrapped` `--algorithm`=`ALGORITHM` `--importing-key-version`=`IMPORTING_KEY_VERSION` [`--key`=`KEY`] [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--version`=`VERSION`] [`--wrapped-key-file`=`WRAPPED_KEY_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Imports a trusted key wrapped version. 
EXAMPLES
     The following command imports a key into version `1` of `frodo`: 
    
    
    gcloud alpha kms keys versions import-trusted-key-wrapped --version=1 --key=frodo --keyring=fellowship --location=us-east1 --importing-key-version=projects/my-project/locations/us-east1/keyRings/fellowship/cryptoKeys/samwise/cryptoKeyVersions/1 --algorithm=aes-256-gcm --wrapped-key-file=/tmp/my/wrapped_key.file

REQUIRED FLAGS
    

`--algorithm`=`ALGORITHM`
     The algorithm to assign to the new key version. For more information about supported algorithms, see <https://cloud.google.com/kms/docs/algorithms>. `ALGORITHM` must be one of: `aes-128-cbc`, `aes-128-ctr`, `aes-128-gcm`, `aes-256-cbc`, `aes-256-ctr`, `aes-256-gcm`, `aes-256-kwp`, `ec-sign-ed25519`, `ec-sign-p256-sha256`, `ec-sign-p384-sha384`, `ec-sign-secp256k1-sha256`, `google-symmetric-encryption`, `hmac-sha1`, `hmac-sha224`, `hmac-sha256`, `hmac-sha384`, `hmac-sha512`, `kem-xwing`, `ml-kem-1024`, `ml-kem-768`, `pq-sign-hash-slh-dsa-sha2-128s-sha256`, `pq-sign-ml-dsa-44`, `pq-sign-ml-dsa-44-external-mu`, `pq-sign-ml-dsa-65`, `pq-sign-ml-dsa-65-external-mu`, `pq-sign-ml-dsa-87`, `pq-sign-ml-dsa-87-external-mu`, `pq-sign-slh-dsa-sha2-128s`, `rsa-decrypt-oaep-2048-sha1`, `rsa-decrypt-oaep-2048-sha256`, `rsa-decrypt-oaep-3072-sha1`, `rsa-decrypt-oaep-3072-sha256`, `rsa-decrypt-oaep-4096-sha1`, `rsa-decrypt-oaep-4096-sha256`, `rsa-decrypt-oaep-4096-sha512`, `rsa-sign-pkcs1-2048-sha256`, `rsa-sign-pkcs1-3072-sha256`, `rsa-sign-pkcs1-4096-sha256`, `rsa-sign-pkcs1-4096-sha512`, `rsa-sign-pss-2048-sha256`, `rsa-sign-pss-3072-sha256`, `rsa-sign-pss-4096-sha256`, `rsa-sign-pss-4096-sha512`, `rsa-sign-raw-pkcs1-2048`, `rsa-sign-raw-pkcs1-3072`, `rsa-sign-raw-pkcs1-4096`. 
`--importing-key-version`=`IMPORTING_KEY_VERSION`
     The resource name of the CryptoKeyVersion to use as an importing key. 
OPTIONAL FLAGS
    

`--key`=`KEY`
     The containing key to import into. 
`--keyring`=`KEYRING`
     Key ring of the key. 
`--location`=`LOCATION`
     Location of the keyring. 
`--version`=`VERSION`
     Version to re-import into. Omit this field for first-time import. 
`--wrapped-key-file`=`WRAPPED_KEY_FILE`
     Path to the RSA/RSA+AES wrapped key file to import. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms keys versions import-trusted-key-wrapped](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/versions/import-trusted-key-wrapped)
    
    
    [gcloud beta kms keys versions import-trusted-key-wrapped](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/versions/import-trusted-key-wrapped)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
