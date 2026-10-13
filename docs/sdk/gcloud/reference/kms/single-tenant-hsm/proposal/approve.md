---
url: https://docs.cloud.google.com/sdk/gcloud/reference/kms/single-tenant-hsm/proposal/approve/
title: gcloud kms single-tenant-hsm proposal approve \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:51.874828+00:00
---

# gcloud kms single-tenant-hsm proposal approve  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/kms/single-tenant-hsm/proposal/approve/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud kms single-tenant-hsm proposal approve Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud kms single-tenant-hsm proposal approve - approve a single tenant HSM instance proposal 
SYNOPSIS
    

`gcloud kms single-tenant-hsm proposal approve` (`SINGLE_TENANT_HSM_INSTANCE_PROPOSAL` : `--location`=`LOCATION` `--single_tenant_hsm_instance`=`SINGLE_TENANT_HSM_INSTANCE`) (`--quorum-challenge-replies`=`QUORUM_CHALLENGE_REPLIES` `--required-challenge-replies`=`REQUIRED_CHALLENGE_REPLIES`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     The following command approves a single tenant HSM instance proposal with quorum challenge replies: 
    
    
    gcloud kms single-tenant-hsm proposal approve projects/my-project/locations/us-east1/singleTenantHsmInstances/ my_sthi/proposals/my_proposal --quorum-challenge-replies="[('signed_challenge_1.txt','public_key_1.pem'),
    
    
    
     ('signed_challenge_2.txt','public_key_2.pem'),
    ('signed_challenge_3.txt','public_key_3.pem')]"

To approve a proposal with required challenges and quorum challenges: 
    
    
    gcloud kms single-tenant-hsm proposal approve projects/my-project/locations/us-east1/singleTenantHsmInstances/ my_sthi/proposals/my_proposal --required-challenge-replies="[('required_challenge.txt','public_key_1.pem')]" --quorum-challenge-replies="[('quorum_challenge_1.txt','public_key_2.pem'),
    
    
    
     ('quorum_challenge_2.txt','public_key_3.pem')]"

POSITIONAL ARGUMENTS
    

SingleTenantHsmInstanceProposal resource - The KMS single tenant HSM instance proposal resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `single_tenant_hsm_instance_proposal` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`SINGLE_TENANT_HSM_INSTANCE_PROPOSAL`
     ID of the singleTenantHsmInstanceProposal or fully qualified identifier for the singleTenantHsmInstanceProposal. 

To set the `proposal` attribute: 

  * provide the argument `single_tenant_hsm_instance_proposal` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Google Cloud location for the singleTenantHsmInstanceProposal. 

To set the `location` attribute: 

  * provide the argument `single_tenant_hsm_instance_proposal` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--single_tenant_hsm_instance`=`SINGLE_TENANT_HSM_INSTANCE`
     The KMS single tenant HSM instance of the singleTenantHsmInstanceProposal. 

To set the `single_tenant_hsm_instance` attribute: 

  * provide the argument `single_tenant_hsm_instance_proposal` on the command line with a fully specified name; 
  * provide the argument `--single_tenant_hsm_instance` on the command line. 


REQUIRED FLAGS
    

Approval payload for the proposal. 

At least one of these must be specified: 

`--quorum-challenge-replies`=`QUORUM_CHALLENGE_REPLIES`
     The challenge replies to approve the proposal. Challenge replies can be sent across multiple requests. Each tuple should be ("signed_challenge_file", "public_key_file"). 
`--required-challenge-replies`=`REQUIRED_CHALLENGE_REPLIES`
     A list of tuples, each containing the file paths for a required challenge reply. Each tuple should be ("signed_challenge_file", "public_key_file"). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha kms single-tenant-hsm proposal approve](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/single-tenant-hsm/proposal/approve)
    
    
    [gcloud beta kms single-tenant-hsm proposal approve](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/single-tenant-hsm/proposal/approve)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
