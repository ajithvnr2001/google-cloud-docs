---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/key-management/
title: Maintain partner-managed keys \u00a0|\u00a0 Sovereign Controls by Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:37.100035+00:00
---

# Maintain partner-managed keys  |  Sovereign Controls by Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/key-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs)
  * [ Guides ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/overview)



Send feedback 

#  Maintain partner-managed keys Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page only applies for customers who are using manually-created partner-managed keys. If you created a [coordinated external key for Cloud EKM](https://docs.cloud.google.com/kms/docs/create-external-key#create-coordinated), your keys can be rotated by following the steps in [Rotate a coordinated external key](https://docs.cloud.google.com/kms/docs/rotate-key#rotate-external-coordinated).

As a Sovereign Controls by Partners customer, you use a different workflow to manage your Cloud External Key Manager (Cloud EKM) keys. Instead of setting up and managing your own external key manager, Google Cloud and the partner handle these steps for you. This means that the partner manages your keys and key versions at your request.

This page describes how to submit requests for common key operations in a partner-managed Cloud Key Management Service project, commonly known as the **Key Management Project**.

## Before you begin

You need to have a key ring with at least one key before making key operation requests.

### Get the key's resource name

For any key operation request, you need to [provide the resource name](https://docs.cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version) of the key or key version to be modified.

  * You need to provide the **key** resource name to create a version or rotate a key.
  * You need to provide the **key version** resource name to update or destroy a key version.



### Issue Tracker requests

Issue Tracker is a tool used by Google and its partners to track requests for specialized projects. For partner-managed Cloud Key Management Service projects, you use the Issue Tracker to submit requests to the partner who then fulfills requests in your Cloud Key Management Service project and manages your keys in the external key manager.

You can find a link to your organization's Issue Tracker in your welcome email.

## Common key operations

### Create a key version

Use the Issue Tracker to submit a request for a new key version. The new key version is set as the primary version if it's the first key version, or if there are no other key versions.

In the Issue Tracker, select **Create key version** and provide the resource name of your key. Click **Create** to submit your request.

### Rotate key

In the Issue Tracker, indicate **Rotate key** in the ticket body and provide the resource name of your key. Click **Create** to submit your request.

When a key is rotated, the partner generates new key material in the EKM, creates a new key version in your Cloud Key Management Service project, and then sets the new key version as the primary version.

Rotating a key version causes all newly-created data protected with that key to be encrypted with new key material. Data protected with previous key material is not re-encrypted. As a result, your previous key material needs to remain available for use.

### Disable a key version

You can use the Google Cloud console, Google Cloud CLI, or a Cloud KMS client library to disable a key version in the **Enabled** state. When you disable a key version, its state changes to **Disabled**. See [Enabling and disabling key versions](https://docs.cloud.google.com/kms/docs/enable-disable#disable) in the Cloud KMS documentation for more information.

**Note:** Key versions in the **Disabled** state are billed as active key versions.

### Destroy a key version

**Caution:** Destroying a key is a permanent operation that can cause unrecoverable data loss. All key destruction actions will be permanent, and once destroyed, the key will be unrecoverable by you, the partner, or Google. Data that was encrypted with the key cannot be accessed.

To destroy a key version, [schedule the key version for destruction](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy) in Cloud KMS. This destroys the Cloud KMS key and data encrypted by the key will no longer be accessible.

If you'd also like to destroy the key in the partner's EKM:

  1. [Schedule the key version for destruction](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy).
  2. In the Issue Tracker, select **Destroy key version** in the ticket body and provide the resource name of the key version you would like to have destroyed.
  3. Click **Create** to submit your request.



The partner confirms your key destruction request with you before proceeding. When destruction is confirmed, the partner provides a date and time for when the key will be destroyed. You can restore the key before the destruction.

In the period before the key is destroyed, if you [restore your key version](https://docs.cloud.google.com/kms/docs/destroy-restore#restore), both the Cloud KMS key and the key in the partner's EKM will remain.

If the destruction continues as scheduled, the Cloud KMS key is deleted first, and then the key in the partner's EKM is deleted.

**Note:** Destroying a key version is not supported if your partner uses Thales Ciphertrust key manager (CCKM), you can only destroy the key and all its key versions.

## Response time

Use the Issue Tracker for routine key management operations only. Once an Issue Tracker request is submitted, you can expect to receive a response from your partner within one business day.

## See also

  * See a list of [supported products](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/supported-products)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
