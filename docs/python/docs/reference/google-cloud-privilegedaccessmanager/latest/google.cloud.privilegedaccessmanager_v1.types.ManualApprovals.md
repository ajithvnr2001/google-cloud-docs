---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-privilegedaccessmanager/latest/google.cloud.privilegedaccessmanager_v1.types.ManualApprovals
title: Class ManualApprovals (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:14.123453+00:00
---

# Class ManualApprovals (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-privilegedaccessmanager/latest/google.cloud.privilegedaccessmanager_v1.types.ManualApprovals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ManualApprovals (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.9 
    
    
    ManualApprovals(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A manual approval workflow where users who are designated as approvers need to call the `ApproveGrant`/`DenyGrant` APIs for a grant. The workflow can consist of multiple serial steps where each step defines who can act as approver in that step and how many of those users should approve before the workflow moves to the next step.

This can be used to create approval workflows such as:

  * Require an approval from any user in a group G.
  * Require an approval from any k number of users from a Group G.
  * Require an approval from any user in a group G and then from a user U.



A single user might be part of the `approvers` ACL for multiple steps in this workflow, but they can only approve once and that approval is only considered to satisfy the approval step at which it was granted.

## Attributes  
  
---  
**Name** | **Description**  
`require_approver_justification` |  `bool`   
Optional. Do the approvers need to provide a justification for their actions?   
`steps` |  `MutableSequence[[google.cloud.privilegedaccessmanager_v1.types.ManualApprovals.Step](https://docs.cloud.google.com/python/docs/reference/google-cloud-privilegedaccessmanager/latest/google.cloud.privilegedaccessmanager_v1.types.ManualApprovals.Step)]`   
Optional. List of approval steps in this workflow. These steps are followed in the specified order sequentially. Only 1 step is supported.   
  
## Classes 

### Step
    
    
    Step(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Step represents a logical step in a manual approval workflow.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
