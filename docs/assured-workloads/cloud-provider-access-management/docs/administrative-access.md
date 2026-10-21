---
url: https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access/
title: Overview of administrative access controls \u00a0|\u00a0 Cloud provider access management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:56.574932+00:00
---

# Overview of administrative access controls  |  Cloud provider access management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of administrative access controls

This page provides an overview of the core underlying principles based on which Google Cloud's administrative access controls are designed.

## What is administrative access

Administrative access includes access to Customer Data by Google personnel by administrative means. For example, a Google employee utilizing an internal support tool to access the contents of a Spanner database to diagnose a customer-raised support case that cites database issues.

An example of non-administrative access is granting a Google employee direct IAM access at the project-level by assigning standard user permissions in the user space. Access by this Google employee in the project where you explicitly granted access doesn't constitute administrative access.

The objective of the administrative access controls is to ensure that Customer Data on Google Cloud isn't accessible to Google employees without an auditable justification, and optionally, an explicit approval.

## Core principles

This section describes the core principles that Customer Data access at Google Cloud adheres to.

### Deny access by default: User content belongs explicitly to the user organization

Google Cloud is strongly committed to ensuring that Customer Data belongs to the customers. This stance is the default posture of every Google employee towards Customer Data.

### Content owner's control over administrative access is a core commitment

Access events are a standard operational element of any cloud-based business. For example, support personnel might need to access Customer Data to provide the requested support, and engineers might need to do it to dig deeper to resolve an issue discovered during the support request investigation. Google Cloud's philosophy is to provide complete logging and approval support for content access with the Access Transparency and Access Approval features.

The following table explains the difference between automated and human access:

Automated access | Human access  
---|---  
No humans can access, view, or export any content handled by these systems. These content accesses are out of scope for the generation of [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) logs. For example, access through programs that periodically hash customer content to check for data corruption. | Human access consists of any access that grants or can grant a human access to user content. This access includes a human using an automated access path to grant indirect access to content. This content access is completely in scope for Access Transparency and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview).   
  
The following table explains the difference between emergency and non-emergency access:

Emergency access | Non-emergency access  
---|---  
This type of access occurs when there is an urgent threat to the integrity of Google's services, infrastructure, or to any customer services or content. An access with one of these justifications can override an organization's Access Approval policy. This rare type of access is logged in Access Approval with the `auto-approved` status. For more information about the `auto-approved` status, see [Status of an access request](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details#status_of_an_access_request). | This type of access consists of any you have filed a support request, and support personnel must look at Customer Data to be able to help. access that doesn't meet the requirements of an emergency access.   
  
### Every access requires a justification

Administrative access is gated behind an auditable, valid business justification with some exceptions.

For the complete list of business justifications for accessing Customer Data, see [Justification reason codes](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#justification_reason_codes).

### Access logging is universal

Administrative access to Customer Data is logged by default. After you have [enabled Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable), near real-time audit logs of any access by Google personnel to user content in the organization are published to each project's logs. These accesses are monitored internally by Google's auditors and are visible externally through Access Transparency logs. For information about viewing these logs, see [Understanding and using Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs).

### Use Assured Workloads for further coverage

Assured Workloads can provide administrative controls that meet the more stringent guidelines laid out by US government certifications, including restrictions on data access by non-US personnel. 

For more information, see [Personnel data access and support controls](https://docs.cloud.google.com/assured-workloads/docs/personnel-access-data-controls).

## What's next

  * [Privileged access at Google Cloud](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access)
  * [Whitepaper about managing and safeguarding your content stored on Google Cloud](https://services.google.com/fh/files/misc/072022_google_cloud_trust_whitepaper.pdf)
  * [Whitepaper about data residency, operational transparency, and privacy for European customers](https://services.google.com/fh/files/misc/googlecloud_european_commitments_whitepaper.pdf)
  * [Overview of Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)
  * [Overview of Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)
  * [Overview of Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
