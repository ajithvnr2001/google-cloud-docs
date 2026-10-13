---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1
title: Access Approval v1 API - Namespace Google.Cloud.AccessApproval.V1 (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:06.636599+00:00
---

# Access Approval v1 API - Namespace Google.Cloud.AccessApproval.V1 (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Access Approval v1 API - Namespace Google.Cloud.AccessApproval.V1 (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/2.5.0/Google.Cloud.AccessApproval.V1)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/2.4.0/Google.Cloud.AccessApproval.V1)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/2.3.0/Google.Cloud.AccessApproval.V1)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/2.2.0/Google.Cloud.AccessApproval.V1)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/2.1.0/Google.Cloud.AccessApproval.V1)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/2.0.0/Google.Cloud.AccessApproval.V1)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/1.4.0/Google.Cloud.AccessApproval.V1)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/1.3.0/Google.Cloud.AccessApproval.V1)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/1.2.0/Google.Cloud.AccessApproval.V1)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/1.1.0/Google.Cloud.AccessApproval.V1)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/1.0.0/Google.Cloud.AccessApproval.V1)



## Classes 

### [AccessApproval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApproval)

This API allows a customer to manage accesses to cloud resources by Google personnel. It defines the following resource model:

  * The API has a collection of [ApprovalRequest][google.cloud.accessapproval.v1.ApprovalRequest] resources, named `approvalRequests/{approval_request}`
  * The API has top-level settings per Project/Folder/Organization, named `accessApprovalSettings`



The service also periodically emails a list of recipients, defined at the Project/Folder/Organization level in the accessApprovalSettings, when there is a pending ApprovalRequest for them to act on. The ApprovalRequests can also optionally be published to a Pub/Sub topic owned by the customer (contact support if you would like to enable Pub/Sub notifications).

ApprovalRequests can be approved or dismissed. Google personnel can only access the indicated resource or resources if the request is approved (subject to some exclusions: <https://cloud.google.com/access-approval/docs/overview#exclusions>).

Note: Using Access Approval functionality will mean that Google may not be able to meet the SLAs for your chosen products, as any support response times may be dramatically increased. As such the SLAs do not apply to any service disruption to the extent impacted by Customer's use of Access Approval. Do not enable Access Approval for projects where you may require high service availability and rapid response by Google Cloud Support.

After a request is approved or dismissed, no further action may be taken on it. Requests with the requested_expiration in the past or with no activity for 14 days are considered dismissed. When an approval expires, the request is considered dismissed.

If a request is not approved or dismissed, we call it pending.

### [AccessApproval.AccessApprovalBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApproval.AccessApprovalBase)

Base class for server-side implementations of AccessApproval

### [AccessApproval.AccessApprovalClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApproval.AccessApprovalClient)

Client for AccessApproval

### [AccessApprovalServiceAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceAccount)

Access Approval service account related to a project/folder/organization.

### [AccessApprovalServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceAccountName)

Resource name for the `AccessApprovalServiceAccount` resource.

### [AccessApprovalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceClient)

AccessApprovalService client wrapper, for convenient use.

### [AccessApprovalServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceClientBuilder)

Builder class for [AccessApprovalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceClient) to provide simple configuration of credentials, endpoint etc.

### [AccessApprovalServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceClientImpl)

AccessApprovalService client wrapper implementation, for convenient use.

### [AccessApprovalServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceSettings)

Settings for [AccessApprovalServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceClient) instances.

### [AccessApprovalSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalSettings)

Settings on a Project/Folder/Organization related to Access Approval.

### [AccessApprovalSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalSettingsName)

Resource name for the `AccessApprovalSettings` resource.

### [AccessLocations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessLocations)

Home office and physical location of the principal.

### [AccessReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessReason)

### [AccessReason.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessReason.Types)

Container for nested types declared in the AccessReason message type.

### [ApprovalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApprovalRequest)

A request for the customer to approve access to a resource.

### [ApprovalRequestName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApprovalRequestName)

Resource name for the `ApprovalRequest` resource.

### [ApproveApprovalRequestMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApproveApprovalRequestMessage)

Request to approve an ApprovalRequest.

### [ApproveDecision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApproveDecision)

A decision that has been made to approve access to a resource.

### [DeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.DeleteAccessApprovalSettingsMessage)

Request to delete access approval settings.

### [DismissApprovalRequestMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.DismissApprovalRequestMessage)

Request to dismiss an approval request.

### [DismissDecision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.DismissDecision)

A decision that has been made to dismiss an approval request.

### [EnrolledService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.EnrolledService)

Represents the enrollment of a cloud resource into a specific service.

### [GetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.GetAccessApprovalServiceAccountMessage)

Request to get an Access Approval service account.

### [GetAccessApprovalSettingsMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.GetAccessApprovalSettingsMessage)

Request to get access approval settings.

### [GetApprovalRequestMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.GetApprovalRequestMessage)

Request to get an approval request.

### [InvalidateApprovalRequestMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.InvalidateApprovalRequestMessage)

Request to invalidate an existing approval.

### [ListApprovalRequestsMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ListApprovalRequestsMessage)

Request to list approval requests.

### [ListApprovalRequestsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ListApprovalRequestsResponse)

Response to listing of ApprovalRequest objects.

### [ResourceProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ResourceProperties)

The properties associated with the resource of the request.

### [SignatureInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.SignatureInfo)

Information about the digital signature of the resource.

### [UpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.UpdateAccessApprovalSettingsMessage)

Request to update access approval settings.

## Enums 

### [AccessApprovalServiceAccountName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceAccountName.ResourceNameType)

The possible contents of [AccessApprovalServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalServiceAccountName).

### [AccessApprovalSettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalSettingsName.ResourceNameType)

The possible contents of [AccessApprovalSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessApprovalSettingsName).

### [AccessReason.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.AccessReason.Types.Type)

Type of access justification.

### [ApprovalRequest.DecisionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApprovalRequest.DecisionOneofCase)

Enum of possible cases for the "decision" oneof.

### [ApprovalRequestName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApprovalRequestName.ResourceNameType)

The possible contents of [ApprovalRequestName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.ApprovalRequestName).

### [EnrollmentLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.EnrollmentLevel)

Represents the type of enrollment for a given service to Access Approval.

### [SignatureInfo.VerificationInfoOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AccessApproval.V1/latest/Google.Cloud.AccessApproval.V1.SignatureInfo.VerificationInfoOneofCase)

Enum of possible cases for the "verification_info" oneof.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
