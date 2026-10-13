---
url: https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse
title: Class ListSingleTenantHsmInstanceProposalsResponse (3.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:11.776612+00:00
---

# Class ListSingleTenantHsmInstanceProposalsResponse (3.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ListSingleTenantHsmInstanceProposalsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListSingleTenantHsmInstanceProposalsResponse (3.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.18.0 (latest)  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.1  3.2.2  3.1.1  3.0.0  2.24.2  2.23.0  2.22.0  2.21.4  2.20.0  2.19.2  2.18.0  2.17.0  2.16.1  2.15.0  2.14.1  2.13.0  2.12.3  2.11.2  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.3  2.3.0  2.2.0  2.1.0  2.0.1  1.4.2  1.3.0  1.2.1  1.1.0 
    
    
    ListSingleTenantHsmInstanceProposalsResponse(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Response message for HsmManagement.ListSingleTenantHsmInstanceProposals.

## Attributes  
  
---  
**Name** | **Description**  
`single_tenant_hsm_instance_proposals` |  `MutableSequence[[google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal)]`   
The list of SingleTenantHsmInstanceProposals.   
`next_page_token` |  `str`   
A token to retrieve next page of results. Pass this value in ListSingleTenantHsmInstanceProposalsRequest.page_token to retrieve the next page of results.   
`total_size` |  `int`   
The total number of SingleTenantHsmInstanceProposals that matched the query. This field is not populated if ListSingleTenantHsmInstanceProposalsRequest.filter is applied.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
