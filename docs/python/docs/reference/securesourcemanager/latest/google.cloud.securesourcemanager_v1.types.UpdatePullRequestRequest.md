---
url: https://docs.cloud.google.com/python/docs/reference/securesourcemanager/latest/google.cloud.securesourcemanager_v1.types.UpdatePullRequestRequest
title: Class UpdatePullRequestRequest (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:50.450281+00:00
---

# Class UpdatePullRequestRequest (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securesourcemanager/latest/google.cloud.securesourcemanager_v1.types.UpdatePullRequestRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UpdatePullRequestRequest (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.17 
    
    
    UpdatePullRequestRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

UpdatePullRequestRequest is the request to update a pull request.

## Attributes  
  
---  
**Name** | **Description**  
`pull_request` |  `[google.cloud.securesourcemanager_v1.types.PullRequest](https://docs.cloud.google.com/python/docs/reference/securesourcemanager/latest/google.cloud.securesourcemanager_v1.types.PullRequest)`   
Required. The pull request to update.   
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. Field mask is used to specify the fields to be overwritten in the pull request resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The special value "\\*" means full replacement.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
