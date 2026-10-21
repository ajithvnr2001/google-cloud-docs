---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/
title: gcloud alpha kms \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:56.588862+00:00
---

# gcloud alpha kms  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms - manage cryptographic keys in the cloud 
SYNOPSIS
    

`gcloud alpha kms` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud kms command group lets you generate, use, rotate and destroy Google Cloud KMS keys. 

Cloud KMS is a cloud-hosted key management service that lets you manage encryption for your cloud services the same way you do on-premises. You can generate, use, rotate and destroy AES256 encryption keys. Cloud KMS is integrated with IAM and Cloud Audit Logging so that you can manage permissions on individual keys, and monitor how these are used. Use Cloud KMS to protect secrets and other sensitive data which you need to store in Google Cloud Platform. 

More information on Cloud KMS can be found here: <https://cloud.google.com/kms/> and detailed documentation can be found here: <https://cloud.google.com/kms/docs/>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[autokey-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/autokey-config)`
     `(ALPHA)` Update and retrieve the AutokeyConfig. 
`[ekm-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/ekm-config)`
     `(ALPHA)` Update and retrieve the EkmConfig. 
`[ekm-connections](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/ekm-connections)`
     `(ALPHA)` Create and manage ekm connections. 
`[import-jobs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/import-jobs)`
     `(ALPHA)` Create and manage import jobs. 
`[inventory](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/inventory)`
     `(ALPHA)` Manages the KMS Inventory and Key Tracking commands. 
`[kaj-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/kaj-config)`
     `(ALPHA)` Update and retrieve KAJ-related configs. 
`[kaj-enrollment](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/kaj-enrollment)`
     `(ALPHA)` Retrieve KAJ enrollment configs. 
`[key-handles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/key-handles)`
     `(ALPHA)` Create and manage KeyHandle resources. 
`[keyrings](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keyrings)`
     `(ALPHA)` Create and manage keyrings. 
`[keys](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/keys)`
     `(ALPHA)` Create and manage keys. 
`[locations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/locations)`
     `(ALPHA)` View locations available for a project. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/operations)`
     `(ALPHA)` Commands for managing operations. 
`[retired-resources](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/retired-resources)`
     `(ALPHA)` Manage retired resources. 
`[single-tenant-hsm](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/single-tenant-hsm)`
     `(ALPHA)` Commands for managing single tenant HSM instances. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[asymmetric-decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/asymmetric-decrypt)`
     `(ALPHA)` Decrypt an input file using an asymmetric-encryption key version. 
`[asymmetric-sign](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/asymmetric-sign)`
     `(ALPHA)` Sign a user input file using an asymmetric-signing key version. 
`[decapsulate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/decapsulate)`
     `(ALPHA)` Decapsulate an input file using a key-encapsulation key version. 
`[decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/decrypt)`
     `(ALPHA)` Decrypt a ciphertext file using a Cloud KMS key. 
`[encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/encrypt)`
     `(ALPHA)` Encrypt a plaintext file using a key. 
`[mac-sign](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/mac-sign)`
     `(ALPHA)` Sign a user input file using a MAC key version. 
`[mac-verify](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/mac-verify)`
     `(ALPHA)` Verify a user signature file using a MAC key version. 
`[raw-decrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/raw-decrypt)`
     `(ALPHA)` Decrypt a ciphertext file using a raw key. 
`[raw-encrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/raw-encrypt)`
     `(ALPHA)` Encrypt a plaintext file using a raw key. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms](https://docs.cloud.google.com/sdk/gcloud/reference/kms)
    
    
    [gcloud beta kms](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
