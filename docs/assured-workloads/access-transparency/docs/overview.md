---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview/
title: Overview of Access Transparency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:34:57.367094+00:00
---

# Overview of Access Transparency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of Access Transparency

This page provides an overview of Access Transparency, which is a part of Google's long-term commitment to transparency, user trust, and customer ownership of their data. [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) lets you authorize requests from Google personnel to access [Customer Data](https://cloud.google.com/terms/data-processing-addendum), and Access Transparency helps you discover information about when Customer Data is accessed. For customers who use access approvals that are signed with a customer-managed encryption key (CMEK), Google also provides users with visibility and control to key access requests through [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview).

These products together provide access management capabilities that give you control over and context for administrative requests to access Customer Data. 

## Overview

Access Transparency logs record the actions that Google personnel take when accessing Customer Data. Access Transparency log entries include details such as the affected resource and action, the time of the action, the reason for the action, and information about the accessor.

Access Transparency logs are designed to fulfill security and regulatory requirements to document, audit, and [restrict](https://docs.cloud.google.com/assured-workloads/access-approval) Google personnel access to your workloads.

The information about the accessor includes details about the physical location, employing entity, and job category of the Google employee. For more information about the details covered in Access Transparency logs, see [Log field descriptions](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#axt-log-entry-sample).

Access Transparency logs are similar to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit); however, Cloud Audit Logs records the actions that members of your Google Cloud organization have taken in your Google Cloud resources, whereas Access Transparency logs record the actions taken by Google personnel. When used together, Cloud Audit Logs and Access Transparency logs provide you audit logging on both customer actions and Google administrative access to Customer Data.

Note: If you need to approve access requests by Google personnel before they can access your Google Cloud resources, see the [Access Approval documentation](https://docs.cloud.google.com/assured-workloads/access-approval/docs). 

## When to use Access Transparency

You might need Access Transparency logs for the following reasons:

  * Verifying that Google personnel are accessing your content only for valid business reasons, such as fixing an outage or attending to your support requests.
  * Verifying that Google personnel access aligns with the products and data that you're seeking assistance with on a customer support case.
  * Verifying and tracking compliance with legal or regulatory obligations. 
  * Collecting and analyzing tracked access events through an automated security information and event management (SIEM) tool such as [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview). 



## Use Access Transparency logs to improve the overall security posture

Access Transparency logs are a valuable additional source of information in your security operations workstreams. By ingesting Access Transparency logs into your security information and event management (SIEM) tools for compliance or auditing purposes, you can augment any existing data, such as Security Command Center security findings. For more information about Access Transparency log ingestion, see [Ingest Google Cloud data to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#export-logs). 

## Google Cloud services that produce Access Transparency logs

For the list of Google Cloud services that produce Access Transparency logs, see [Supported services](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services).

## When can Google personnel access customer content?

Google personnel are strictly restricted in what is visible to them. All access to Customer Data requires a valid justification for [privileged access](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access#why-access). See [Justification reason codes](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs#justification_reason_codes) for the list of valid business justifications.

## How does Google train its employees on the confidentiality of customer content?

All Google employees are required to execute a confidentiality agreement and comply with [Google's Code of Conduct](https://abc.xyz/investor/other/google-code-of-conduct/). For more information on employee onboarding and security and privacy training, see the [Google security whitepaper](https://cloud.google.com/security/overview/whitepaper). 

## How does Google handle government requests for customer content?

If Google receives a government request for Customer Data, it is Google's policy to direct the government to request such data directly from the Google Cloud customer. For more information, see [Google Cloud Government Requests whitepaper](https://services.google.com/fh/files/misc/google_cloud_governmentrequestsfor_cloud_customer_data_v2_1018.pdf). 

## What's next

  * To learn the core principles behind controls preventing unauthorized administrative access, see [Overview of administrative access controls](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access).


  * To understand the contents of Access Transparency log entries, see [Understanding and using Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs).

  * For information on Google Cloud's privileged access principles, see [Privileged access](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/privileged-access).



  * For more information on the controls Google has put in place for protecting customer content, see the [Google security whitepaper](https://cloud.google.com/security/overview/whitepaper).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
