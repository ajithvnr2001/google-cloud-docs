---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create/
title: gcloud kms import-jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:45.173086+00:00
---

# gcloud kms import-jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/import-jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms import-jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms import-jobs create - create a new import job 
SYNOPSIS
    

`gcloud kms import-jobs create` `IMPORT_JOB` `--import-method`=`IMPORT_METHOD` `--protection-level`=`PROTECTION_LEVEL` [`--keyring`=`KEYRING`] [`--location`=`LOCATION`] [`--single-tenant-hsm-instance`=`SINGLE_TENANT_HSM_INSTANCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new import job within the given keyring. 
EXAMPLES
     The following command creates a new import job named `strider` within the `fellowship` keyring, and `us-central1` location: 
    
    
    gcloud kms import-jobs create strider --location=us-central1 --keyring=fellowship --import-method=rsa-oaep-3072-sha256-aes-256 --protection-level=hsm

The following command creates a new import job named `strider` within the `fellowship` keyring, and `us-central1` location: 
    
    
    gcloud kms import-jobs create strider --location=us-central1 --keyring=fellowship --import-method=rsa-oaep-3072-sha256-aes-256 --protection-level=hsm-single-tenant --single-tenant-hsm-instance=my_sthi

POSITIONAL ARGUMENTS
    

`IMPORT_JOB`
     Name of the import job to create. 
REQUIRED FLAGS
    

`--import-method`=`IMPORT_METHOD`
     The wrapping method to be used for incoming key material. For more information about choosing an import method, see <https://cloud.google.com/kms/docs/key-wrapping>. `IMPORT_METHOD` must be one of: `hpke-kem-ml-kem-1024-hkdf-sha256-aes-256-gcm`, `hpke-kem-ml-kem-768-hkdf-sha256-aes-256-gcm`, `hpke-kem-xwing-hkdf-sha256-aes-256-gcm`, `rsa-oaep-3072-sha1-aes-256`, `rsa-oaep-3072-sha256`, `rsa-oaep-3072-sha256-aes-256`, `rsa-oaep-4096-sha1-aes-256`, `rsa-oaep-4096-sha256`, `rsa-oaep-4096-sha256-aes-256`. 
`--protection-level`=`PROTECTION_LEVEL`
     Protection level of the import job. `PROTECTION_LEVEL` must be one of: `software`, `hsm`, `hsm-single-tenant`. 
OPTIONAL FLAGS
    

`--keyring`=`KEYRING`
     Key ring of the import job. 
`--location`=`LOCATION`
     Location of the import job. 
`--single-tenant-hsm-instance`=`SINGLE_TENANT_HSM_INSTANCE`
     The single tenant HSM instance to use for the import job. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms import-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/import-jobs/create)
    
    
    [gcloud beta kms import-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/import-jobs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
