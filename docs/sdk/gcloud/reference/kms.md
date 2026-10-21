---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/
title: gcloud kms \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:40.750133+00:00
---

# gcloud kms  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms - manage cryptographic keys in the cloud 
SYNOPSIS
    

`gcloud kms` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud kms command group lets you generate, use, rotate and destroy Google Cloud KMS keys. 

Cloud KMS is a cloud-hosted key management service that lets you manage encryption for your cloud services the same way you do on-premises. You can generate, use, rotate and destroy AES256 encryption keys. Cloud KMS is integrated with IAM and Cloud Audit Logging so that you can manage permissions on individual keys, and monitor how these are used. Use Cloud KMS to protect secrets and other sensitive data which you need to store in Google Cloud Platform. 

More information on Cloud KMS can be found here: <https://cloud.google.com/kms/> and detailed documentation can be found here: <https://cloud.google.com/kms/docs/>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[autokey-config](https://docs.cloud.google.com/sdk/gcloud/reference/kms/autokey-config)`
     Update and retrieve the AutokeyConfig. 
`[ekm-config](https://docs.cloud.google.com/sdk/gcloud/reference/kms/ekm-config)`
     Update and retrieve the EkmConfig. 
`[ekm-connections](https://docs.cloud.google.com/sdk/gcloud/reference/kms/ekm-connections)`
     Create and manage ekm connections. 
`[import-jobs](https://docs.cloud.google.com/sdk/gcloud/reference/kms/import-jobs)`
     Create and manage import jobs. 
`[inventory](https://docs.cloud.google.com/sdk/gcloud/reference/kms/inventory)`
     Manages the KMS Inventory and Key Tracking commands. 
`[key-handles](https://docs.cloud.google.com/sdk/gcloud/reference/kms/key-handles)`
     Create and manage KeyHandle resources. 
`[keyrings](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keyrings)`
     Create and manage keyrings. 
`[keys](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys)`
     Create and manage keys. 
`[locations](https://docs.cloud.google.com/sdk/gcloud/reference/kms/locations)`
     View locations available for a project. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/kms/operations)`
     Commands for managing operations. 
`[retired-resources](https://docs.cloud.google.com/sdk/gcloud/reference/kms/retired-resources)`
     Manage retired resources. 
`[single-tenant-hsm](https://docs.cloud.google.com/sdk/gcloud/reference/kms/single-tenant-hsm)`
     Commands for managing single tenant HSM instances. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[asymmetric-decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/asymmetric-decrypt)`
     Decrypt an input file using an asymmetric-encryption key version. 
`[asymmetric-sign](https://docs.cloud.google.com/sdk/gcloud/reference/kms/asymmetric-sign)`
     Sign a user input file using an asymmetric-signing key version. 
`[decapsulate](https://docs.cloud.google.com/sdk/gcloud/reference/kms/decapsulate)`
     Decapsulate an input file using a key-encapsulation key version. 
`[decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/decrypt)`
     Decrypt a ciphertext file using a Cloud KMS key. 
`[encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/encrypt)`
     Encrypt a plaintext file using a key. 
`[mac-sign](https://docs.cloud.google.com/sdk/gcloud/reference/kms/mac-sign)`
     Sign a user input file using a MAC key version. 
`[mac-verify](https://docs.cloud.google.com/sdk/gcloud/reference/kms/mac-verify)`
     Verify a user signature file using a MAC key version. 
`[raw-decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/raw-decrypt)`
     Decrypt a ciphertext file using a raw key. 
`[raw-encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/kms/raw-encrypt)`
     Encrypt a plaintext file using a raw key. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms)
    
    
    [gcloud beta kms](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
