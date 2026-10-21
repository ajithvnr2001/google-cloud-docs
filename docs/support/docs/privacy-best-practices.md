---
url: https://docs.cloud.google.com/support/docs/privacy-best-practices/
title: Privacy best practices when working with Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:04.070557+00:00
---

# Privacy best practices when working with Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/privacy-best-practices/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Privacy best practices when working with Cloud Customer Care Stay organized with collections  Save and categorize content based on your preferences. 

When you open support cases or share diagnostic data with Cloud Customer Care, following privacy best practices helps you protect sensitive data, credentials, and personal information while resolving technical issues. To obtain guidance on specific requirements applicable to your organization, consult with a legal expert, as this document does not constitute legal advice.

## Removing sensitive data when creating a support case

As part of a support case, we may collect customer contact information, case details, support interactions, and customer feedback. We consider this data to be _Service Data_ , the processing of which is covered in the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

When you reach out to Customer Care through different channels, you see a notification in the user interface to remind you to omit or remove any sensitive data (for example, credit card numbers, passwords, health information, and government ID numbers) when creating a support case.

Occasionally, you might send sensitive data to Customer Care. You can ask the support agent to remove such content in the support ticket. Support personnel follow an internal process to proactively identify such sensitive information stored in the support ticket. Support personnel are empowered and trained to flag any case that could potentially compromise personal information or Google data and escalate review to a designated internal team to evaluate these cases and take appropriate action.

Google also builds support tools to help you sanitize the sensitive information. For example, Google created a HAR (HTTP Archive) Analyzer tool to help you screen HAR files, which alerts you not to disclose sensitive data such as cookies, passwords, and credit card numbers. Google uses the HAR file to investigate if requests get a specific error-response code or if the request is aborted. Google also examines the HAR file to find out if the issue is caused by non-error responses or if the HAR file failed to capture the error causing the issue.

**Note:** HAR is a JSON-formatted archive file format for logging a web browser's interaction with a website.

## Sharing files with Customer Care

You may need to share files with Customer Care for troubleshooting purposes. When sharing through case (preferred method) is not feasible you can host a file using Cloud Storage buckets and grant viewer permissions to Support.

To share a file with Customer Care, you can grant the Storage Object Viewer (`roles/storage.objectViewer`) role at the bucket level to a service account created on a per support case basis.

**Note:** As a Google Cloud customer, you receive an email with instructions about how to share files with Customer Care.

## Subprocessor security and access

Customer Care engages third-party entities (see [Google Cloud Platform Subprocessors](https://cloud.google.com/terms/subprocessors)) to perform limited activities in connection with Customer Care. The support subprocessors don't have default access to Customer Data stored or processed by the Google Cloud services. The support subprocessors only have access to Customer Data (for example, database contents, cloud bucket data) if you explicitly elect to share your Customer Data in the course of a support case.

The following security safeguards are in place to control access to Customer Data by such subprocessors:

Subprocessors exclusively use Google-managed machines to access corporate resources. Google's internal systems have built-in interconnected controls that will grant or deny access to a support agent depending on systematized checks that are performed (for example, to confirm the owner of a support case). System access by subprocessors is systematically logged and periodically audited to ensure appropriate use.

## Retention and deletion

You can initiate a case deletion by contacting Customer Care and the support team will review the request. In certain cases, support will need to retain certain information for an extended period of time for legitimate business or legal purposes, for example, in case there's a billing dispute, or otherwise to comply with our legal obligations.

## Access to your Support interactions

If you need access to your support interactions, and if those interactions aren't available in the Google Cloud console, you can request a copy of your support interactions by opening a standard support case. You can request communications including call recordings, chat transcripts, and emails for the case you need information for.

## How Customer Care uses support case data

Customer Care uses support case data to keep a consistent record of your support issues. This can be informative when addressing future support issues or situations related to your customer account. Additionally, Customer Care uses support case data in accordance with the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice), including to conduct quality reviews, build automated solutions for customer responses, and improve the customer support experience.

## How resold customers receive Support help

If you purchase Google Cloud from a [Google reseller](https://cloud.google.com/find-a-partner/), you can receive support help related to your account projects and billing directly from the reseller.

Depending on the services purchased from the reseller, there are several ways to contact Customer Care. For example, you can directly open a support case through the Google Cloud console, or a reseller can open a support ticket on your behalf. To provide the reseller with visibility into cases opened directly with Google you can [enable case sharing](https://docs.cloud.google.com/support/docs/customer-care-procedures#enable_case_sharing).

If you only have a support contract with the reseller, it's the reseller's responsibility to provide the appropriate level of support. Google Cloud doesn't have control or visibility into these agreements. If you have a direct Support contract with your reseller, we suggest that you apply privacy best practices during your support interactions with them.

## Access control

As part of Google's long-term commitment to security and transparency, you can use [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) to review logs of actions taken by Google personnel when accessing customer content.

You have access to this service if you have a supported edition.

Access Transparency is available for [supported Google Cloud services](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services). By reviewing the Access Transparency logs, you can verify that Google is accessing customer content for valid business reasons, such as fixing a problem or responding to a request. When accessing customer content for troubleshooting purposes, support agents are required to enter a valid business reason—such as an active support case number or bug number for the cases they have owned. You'll see the following justification reason in the description field:

`CUSTOMER_INITIATED_SUPPORT`.

## Data protection expertise

Google has a dedicated internal support team to answer questions on privacy and data protection to ensure Google Cloud services can help meet your compliance needs. To contact the Google Cloud Data Protection Team, use the [Google Cloud Platform Data Privacy Inquiry form](https://support.google.com/cloud/contact/dpo).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
