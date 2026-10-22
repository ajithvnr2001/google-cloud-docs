---
url: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview/
title: Overview of Key Access Justifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:13.628311+00:00
---

# Overview of Key Access Justifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Key Access Justifications ](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of Key Access Justifications

This page provides an overview of Key Access Justifications. Key Access Justifications is a part of Google's long-term commitment to transparency, user trust, and customer ownership of their data. Key Access Justifications directs Google systems to generate access [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes) for each cryptographic operation involving enrolled Cloud Key Management Service (Cloud KMS) keys.

Key Access Justifications works alongside [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) and [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) in the following way: Access Approval lets you authorize requests from Google personnel to access [Customer Data](https://cloud.google.com/terms/data-processing-addendum), Access Transparency helps you discover information about when Customer Data is accessed, and Key Access Justifications provides key access control for all interactions with at-rest Customer Data that is encrypted by a customer-managed key. Together, each of these products provide access management capabilities that give you control over and context for administrative requests to access Customer Data.

## Overview

Key Access Justifications lets you set a policy on Cloud Key Management Service (Cloud KMS) keys to view, approve, and deny key access requests depending on the provided [justification code](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes). For select external key management partners, you can configure Key Access Justifications policies outside of Google Cloud to be exclusively enforced by the external key manager rather than by Cloud KMS.

Depending on the [Assured Workloads control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) you choose, the following Key Access Justifications features are available:

  * For select [regional control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regional-controls), _Key Access Transparency_ logs these justification codes in your Cloud KMS [audit logs](https://docs.cloud.google.com/kms/docs/audit-logging).
  * For select regional, [regulatory](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regulatory-controls), or [sovereign](https://docs.cloud.google.com/assured-workloads/docs/control-packages#sovereign-controls) control packages, Key Access Justifications lets you set a policy on your keys to approve or deny key access requests depending on the provided justification code. Some regional data boundaries provide this feature in addition to Key Access Transparency.
  * For select sovereign control packages, you can use a supported external key management partners to configure Key Access Justifications policies outside of Google Cloud. These policies are exclusively enforced by the external key manager rather than by Cloud KMS.



In addition to these features, the Assured Workloads control package you choose will also determine which of the following Cloud KMS key types are available:

  * [Cloud EKM keys](https://docs.cloud.google.com/kms/docs/ekm#overview)
  * [Cloud HSM keys](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-kaj)
  * [Cloud KMS software keys](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-kaj)



## How encryption at rest works

Google Cloud encryption at rest works by encrypting your data stored on Google Cloud with an encryption key that lives outside the service where the data is stored. For example, if you encrypt data in Cloud Storage, the service only stores the encrypted information you have stored, whereas the key used to encrypt that data is stored in Cloud KMS (if you are using customer-managed encryption keys (CMEK)) or in your external key manager (if you are using Cloud EKM).

When you use a Google Cloud service, you want your applications to continue working as described, and this will require your data to be decrypted. For example, if you run a query using BigQuery, the BigQuery service needs to decrypt your data to be able to analyze it. BigQuery accomplishes this by making a decryption request to the key manager to get the required data.

## Why would my keys be accessed?

Your encryption keys are most often accessed by automated systems while servicing your own requests and workloads on Google Cloud.

In addition to customer-initiated accesses and automated system accesses, a Google employee might need to initiate operations which use your encryption keys for the following reasons:

  * **Back up your data** : Google might need to access your encryption keys to back up your data for disaster recovery reasons.

  * **Resolve a support request** : A Google employee might need to decrypt your data to fulfill the contractual obligation of providing support.

  * **Manage and troubleshoot systems** : Google personnel can initiate operations which use your encryption keys to perform technical debugging needed for a complex support request or investigation. Access might also be needed to remediate storage failure or data corruption.

  * **Ensure data integrity and compliance, and protect against fraud and abuse** : Google might need to decrypt data for the following reasons:

    * To ensure the safety and security of your data and accounts.
    * To make sure that you are using Google services in compliance with the [Google Cloud Terms of Service](https://cloud.google.com/terms).
    * To investigate complaints by other users and customers, or other signals of abusive activity.
    * To verify that Google Cloud services are being used in accordance with applicable regulatory requirements, such as anti-money laundering regulations.
  * **Maintain system reliability** : Google personnel can request access to investigate that a suspected service outage doesn't affect you. Also, access might be requested to ensure backup and recovery from outages or system failures.




For the list of justification codes, see [justification reason codes for Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).

## Managing access to your keys

Key Access Justifications provides a reason every time your Cloud KMS-managed keys or externally managed keys are accessed. When your key is used for any cryptographic operation, you receive a justification for both service-based access (for supported services) and direct API access.

After your key projects are enrolled in Key Access Justifications, you immediately begin receiving justifications for every key access for new keys. For previously existing keys, you will begin receiving justifications for every key access within 24 hours.

## Enabling Key Access Justifications

Key Access Justifications can only be used with Assured Workloads, and is enabled by default when you create a new Assured Workloads folder configured for a control package that includes Key Access Justifications. See the [Assured Workloads overview](https://docs.cloud.google.com/assured-workloads/docs/overview) for more information.

**Note:** It can take up to 24 hours to enable Key Access Justifications with external key managers after you've created your Assured Workloads folder. Therefore, we recommend that you don't reject key access requests in production environments during this time. There is no delay when using non-external Cloud KMS keys.

## Key Access Justifications exclusions

Key Access Justifications only applies to the following situations:

  * **Operations on encrypted data** : For the fields within a given service that are encrypted by a customer-managed key, refer to the service's documentation.
  * **The transition from data-at-rest to data-in-use** : While Google continues to apply protections to your data-in-use, Key Access Justifications only governs the transition from data-at-rest to data-in-use.



The following Compute Engine and Persistent Disk features are exempted when used with CMEK:

  * [Local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds)
  * [Automatic restart](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options)
  * [Machine image operations](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images)



## Key Access Justifications with Access Approval

For workloads with Access Approval enabled with a custom signing key, Key Access Justifications will also apply to processing signed access approval requests. Access Approval requests can only be processed if the associated justification for the key access associated is also permitted by the key's Key Access Justifications policy. When a customer signs an Access Approval request, the associated justification is reflected in the signing request for the approval.

All Customer Data accesses that occur from an approved, signed access approval request will appear in Access Transparency logs linked to the approval request.

## What's next

  * See [which services](https://docs.cloud.google.com/assured-workloads/docs/supported-products) are supported by Assured Workloads for [Sovereign Controls for EU](https://docs.cloud.google.com/assured-workloads/docs/control-packages#eu-sovereignty-controls) and the [list of additional KAJ-supported services](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/supported-services).
  * Read how to [view and act on justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/view-justifications).
  * Read where you can [get support for Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/getting-support).
  * Learn [what an Access Approval request looks like](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details).
  * Learn about the [core principles upon which controls that prevent unauthorized administrative access are based](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs/administrative-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
