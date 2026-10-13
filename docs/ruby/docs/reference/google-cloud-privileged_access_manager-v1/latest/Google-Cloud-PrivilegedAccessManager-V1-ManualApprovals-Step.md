---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-ManualApprovals-Step/
title: Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::ManualApprovals::Step (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:51.796502+00:00
---

# Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::ManualApprovals::Step (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-ManualApprovals-Step/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::ManualApprovals::Step (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Privileged Access Manager V1 API class Google::Cloud::PrivilegedAccessManager::V1::ManualApprovals::Step.

Step represents a logical step in a manual approval workflow.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #approvals_needed
    
    
    def approvals_needed() -> ::Integer

**Returns**

  * (::Integer) — Required. How many users from the above list need to approve. If there aren't enough distinct users in the list, then the workflow indefinitely blocks. Should always be greater than 0. 1 is the only supported value. 



### #approvals_needed=
    
    
    def approvals_needed=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. How many users from the above list need to approve. If there aren't enough distinct users in the list, then the workflow indefinitely blocks. Should always be greater than 0. 1 is the only supported value. 



**Returns**

  * (::Integer) — Required. How many users from the above list need to approve. If there aren't enough distinct users in the list, then the workflow indefinitely blocks. Should always be greater than 0. 1 is the only supported value. 



### #approver_email_recipients
    
    
    def approver_email_recipients() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Additional email addresses to be notified when a grant is pending approval. 



### #approver_email_recipients=
    
    
    def approver_email_recipients=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Additional email addresses to be notified when a grant is pending approval. 



**Returns**

  * (::Array<::String>) — Optional. Additional email addresses to be notified when a grant is pending approval. 



### #approvers
    
    
    def approvers() -> ::Array<::Google::Cloud::PrivilegedAccessManager::V1::AccessControlEntry>

**Returns**

  * (::Array<[::Google::Cloud::PrivilegedAccessManager::V1::AccessControlEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-AccessControlEntry)>) — Optional. The potential set of approvers in this step. This list must contain at most one entry. 



### #approvers=
    
    
    def approvers=(value) -> ::Array<::Google::Cloud::PrivilegedAccessManager::V1::AccessControlEntry>

**Parameter**

  * **value** (::Array<[::Google::Cloud::PrivilegedAccessManager::V1::AccessControlEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-AccessControlEntry)>) — Optional. The potential set of approvers in this step. This list must contain at most one entry. 



**Returns**

  * (::Array<[::Google::Cloud::PrivilegedAccessManager::V1::AccessControlEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-AccessControlEntry)>) — Optional. The potential set of approvers in this step. This list must contain at most one entry. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
