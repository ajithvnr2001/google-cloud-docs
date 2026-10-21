---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/single-tenant-hsm/proposal/create/
title: gcloud kms single-tenant-hsm proposal create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:51.531697+00:00
---

# gcloud kms single-tenant-hsm proposal create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/single-tenant-hsm/proposal/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms single-tenant-hsm proposal create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms single-tenant-hsm proposal create - create a single tenant HSM instance proposal 
SYNOPSIS
    

`gcloud kms single-tenant-hsm proposal create` (`SINGLE_TENANT_HSM_INSTANCE` : `--location`=`LOCATION`) `--operation-type`=`OPERATION_TYPE` [`--crypto-key-version-name`=`CRYPTO_KEY_VERSION_NAME`] [`--member-public-key-pem`=`MEMBER_PUBLIC_KEY_PEM`] [`--required-approver-count`=`REQUIRED_APPROVER_COUNT`] [`--single-tenant-hsm-instance-proposal-id`=`SINGLE_TENANT_HSM_INSTANCE_PROPOSAL_ID`] [`--two-factor-public-key-pem`=`TWO_FACTOR_PUBLIC_KEY_PEM`] [`--two-factor-public-key-pems`=[`PEM_FILE_PATH`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
    
    
    
    gcloud kms single-tenant-hsm proposal create
      my_stchi
      --location=us-central1 \
      --required-approver-count=1  \
      --two-factor-public-key-pems=public_key_1.pem,public_key_2.pem

POSITIONAL ARGUMENTS
    

SingleTenantHsmInstance resource - The KMS single tenant HSM instance resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `single_tenant_hsm_instance` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`SINGLE_TENANT_HSM_INSTANCE`
     ID of the singleTenantHsmInstance or fully qualified identifier for the singleTenantHsmInstance. 

To set the `single_tenant_hsm_instance` attribute: 

  * provide the argument `single_tenant_hsm_instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Google Cloud location for the singleTenantHsmInstance. 

To set the `location` attribute: 

  * provide the argument `single_tenant_hsm_instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--operation-type`=`OPERATION_TYPE`
     The type of operation for the single tenant HSM instance proposal. 
OPTIONAL FLAGS
    

`--crypto-key-version-name`=`CRYPTO_KEY_VERSION_NAME`
     ID to use for the crypto key version. This field is required for upgrade_key_trust operation type. 
`--member-public-key-pem`=`MEMBER_PUBLIC_KEY_PEM`
     The PEM file containing the public key of the quorum member to add or remove. This field is required for add_quorum_member and remove_quorum_member operation types. 
`--required-approver-count`=`REQUIRED_APPROVER_COUNT`
     The number of approvers required for the single tenant HSM instance. This is the M value used for M of N quorum. Must be greater than or equal to 1 and less than or equal to the total approver count of the single tenant HSM instance minus 1. This field is required for the register_2fa_keys operation type. 
`--single-tenant-hsm-instance-proposal-id`=`SINGLE_TENANT_HSM_INSTANCE_PROPOSAL_ID`
     The ID to use for the single tenant HSM instance proposal, which will become the final component of the single tenant HSM instance resource name. 
`--two-factor-public-key-pem`=`TWO_FACTOR_PUBLIC_KEY_PEM`
     PEM file containing the two-factor public key. This field is required for upgrade_key_trust operation type. 
`--two-factor-public-key-pems`=[`PEM_FILE_PATH`,…]
     The PEM files containing the two factor public keys 2FA keys for M of N quorum auth tenant HSM instance. This field is required for register_2fa_keys operation type. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms single-tenant-hsm proposal create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/single-tenant-hsm/proposal/create)
    
    
    [gcloud beta kms single-tenant-hsm proposal create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/single-tenant-hsm/proposal/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
