---
url: https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types
title: Package types (1.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:02.601780+00:00
---

# Package types (1.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.2  1.15.0  1.14.1  1.13.5  1.12.0  1.11.3  1.10.1  1.9.1  1.8.0  1.7.5  1.6.1  1.5.1  1.4.1  1.3.5  1.2.0  1.1.1  1.0.0  0.2.2  0.1.0 

API documentation for `accessapproval_v1.types` package.

## Classes 

### [AccessApprovalServiceAccount](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.AccessApprovalServiceAccount)

Access Approval service account related to a project/folder/organization.

### [AccessApprovalSettings](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.AccessApprovalSettings)

Settings on a Project/Folder/Organization related to Access Approval.

### [AccessLocations](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.AccessLocations)

Home office and physical location of the principal.

### [AccessReason](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.AccessReason)

### [ApprovalRequest](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ApprovalRequest)

A request for the customer to approve access to a resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ApproveApprovalRequestMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ApproveApprovalRequestMessage)

Request to approve an ApprovalRequest.

### [ApproveDecision](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ApproveDecision)

A decision that has been made to approve access to a resource.

### [DeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.DeleteAccessApprovalSettingsMessage)

Request to delete access approval settings.

### [DismissApprovalRequestMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.DismissApprovalRequestMessage)

Request to dismiss an approval request.

### [DismissDecision](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.DismissDecision)

A decision that has been made to dismiss an approval request.

### [EnrolledService](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.EnrolledService)

Represents the enrollment of a cloud resource into a specific service.

### [EnrollmentLevel](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.EnrollmentLevel)

Represents the type of enrollment for a given service to Access Approval.

### [GetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.GetAccessApprovalServiceAccountMessage)

Request to get an Access Approval service account.

### [GetAccessApprovalSettingsMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.GetAccessApprovalSettingsMessage)

Request to get access approval settings.

### [GetApprovalRequestMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.GetApprovalRequestMessage)

Request to get an approval request.

### [InvalidateApprovalRequestMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.InvalidateApprovalRequestMessage)

Request to invalidate an existing approval.

### [ListApprovalRequestsMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ListApprovalRequestsMessage)

Request to list approval requests.

### [ListApprovalRequestsResponse](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ListApprovalRequestsResponse)

Response to listing of ApprovalRequest objects.

### [ResourceProperties](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.ResourceProperties)

The properties associated with the resource of the request.

### [SignatureInfo](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.SignatureInfo)

Information about the digital signature of the resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/python/docs/reference/accessapproval/latest/google.cloud.accessapproval_v1.types.UpdateAccessApprovalSettingsMessage)

Request to update access approval settings.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
