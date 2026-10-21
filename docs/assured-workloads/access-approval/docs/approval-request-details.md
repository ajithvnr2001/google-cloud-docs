---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details/
title: Anatomy of an Access Approval request \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:50.557292+00:00
---

# Anatomy of an Access Approval request  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Anatomy of an Access Approval request

This page describes the information contained in Access Approval requests.

## Sample Access Approval request

The following code is a sample Access Approval request:
    
    
    {
      "name": "projects/123456/approvalRequests/xyzabc123",
      "requestedResourceName": "projects/123456",
    
      "requestedReason": {
        "detail":  "Case number: bar123",
        "type":  "CUSTOMER_INITIATED_SUPPORT"
      },
      "requestedLocations": {
        "principalOfficeCountry": "US",
        "principalPhysicalLocationCountry": "US"
      },
      "requestTime": "2018-08-28T19:07:12.286Z",
    
      "requestedExpiration": "2018-09-02T19:07:11.877Z"
    }
    

## Request fields

An Access Approval request contains the following fields:

Field | Description  
---|---  
`Resource` | The location of the resource that the Google employee is requesting access for. Google personnel can request access at the level of a resource or at the level of a specific project. Approving access for a given resource also grants access to any child resources. For example, if you make an approval for `projects/123456/buckets/bucket-123` project, an access request for `projects/123456/buckets/bucket-123/objects/file-1` child resource is also allowed.  
`Request time` | The time when Access Approval sent the access request to you.  
`Access expires` | The time when the requested access expires.  
`Office location` | Access is only allowed if the accessor has a permanent desk in this location. The location is one of an ISO 3166-1 alpha-2 country code, a 3-character continent identifier, or **ANY** to indicate that any location is allowed.  
`Physical location` | Access is only allowed if the accessor is physically located in this location. The location is one of an ISO 3166-1 alpha-2 country code, a location. The location is one of an ISO 3166-1 alpha-2 country code, a 3-character continent identifier, or **ANY** to indicate that any location is allowed.  
`Reason` | The reason for the access. For more information, see [Justification codes in Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#justification_reason_codes).  
  
For more information about the fields in an access request, see [Resource: ApprovalRequest](https://docs.cloud.google.com/assured-workloads/access-approval/docs/reference/rest/v1/folders.approvalRequests#ApprovalRequest).

## Historical Access Approval requests

Access Approval lets you view all the historical approved, auto-approved, dismissed, and expired access requests. You can use the Google Cloud console or `curl` to view historical access requests. For instructions, see [Viewing historical Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/view-historical-requests).

A historical access request log contains all the access request fields, and mentions the status and the response time of the request.

The following sections describe the **Approval status** and **Response time** fields.

### Status of an access request

An Access Approval request has one of the following statuses:

Status | Description  
---|---  
`pending` | Indicates that the access request is awaiting your action.  
`approved` | Indicates that you approved the access request.  
`dismissed` | Indicates that you dismissed the access request.  
`expired` | Indicates that the duration of access approved by you has expired.  
`policy-approved` | Indicates that the request was approved by the rules of a configured policy. For details, see [ Access Approval policy settings](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys#enrollment-mode).  
`auto-approved` | Indicates that Google personnel made a time-sensitive access to Customer Data. To make these accesses, Google personnel had to curtail the usual flow of getting Customer Data. Google personnel are required to make these accesses for a production outage investigation or a legal request.   
  
Previously, these accesses didn't trigger an Access Approval request. To ensure transparency about these accesses, Access Approval logs these accesses with the `auto-approved` status. You can view the details about these accesses in the **History requests** sections in the Access Approval page on Google Cloud console.  
  
The `auto-approved` accesses also generate the usual set of Access Transparency logs. Access Transparency logs provide information about the affected resources and the time of the action. For more information about viewing Access Transparency logs, see [Understanding and using Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs). For the list of actions that don't trigger an Access Approval request, see [ Access Approval exclusions](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview#exclusions).  
  
### Response time

This field indicates the time when you approved or dismissed the access request. A response time isn't applicable for requests that were dismissed due to inactivity.

## What's next

  * Learn how to [view historical Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/view-historical-requests).
  * Learn how to [approve access requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approve-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
