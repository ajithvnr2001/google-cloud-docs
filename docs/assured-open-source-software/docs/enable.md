---
url: https://docs.cloud.google.com/assured-open-source-software/docs/enable/
title: Enable the Assured Open Source Software free tier \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:14.610235+00:00
---

# Enable the Assured Open Source Software free tier  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Enable the Assured Open Source Software free tier Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable the Assured Open Source Software free tier. To use the Assured OSS premium tier with Security Command Center, see [Integrate Assured OSS with Security Command Center](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).

## Before you begin

To use the free tier of Assured Open Source Software (Assured OSS), you must submit the [customer enablement form](https://developers.google.com/assured-oss#get-started). Complete the steps in this section before you fill out the form.

## Create accounts

You require at least one [service account](https://docs.cloud.google.com/iam/docs/service-accounts) or Amazon Web Services (AWS) account to access the following:

  * Google-managed [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) for the Assured OSS curated packages.
  * Google-managed [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs) APIs for the enriched package metadata.
  * Secured [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket with corresponding SPDX, VEX, package health and license files.
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) topic for notification on package status and vulnerability updates.
  * Scripts for performing signature verification, downloading metadata, and generating Python `requirements.txt` files.
  * The Assured OSS APIs.



In total, you can provide up to ten identities across both Google Cloud service accounts or AWS account IDs. Though you can use existing accounts, we recommend that you create new accounts to use exclusively for Assured OSS.

To use Assured OSS directly with Artifact Registry (without enabling a proxy), one of the service accounts that you must provide is the [Artifact Registry Service Agent](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account) for the project you want to use Assured OSS with.

To create service accounts, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create). To see the existing service accounts in a project, see [List and edit service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit).

To obtain your Amazon Web Services (AWS) account ID, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/signin/latest/userguide/console_account-alias.html).

## Set up Pub/Sub notifications

You can receive notifications when images are uploaded, new tags are added, or images are deleted.

To set up Pub/Sub so that you can receive notifications, see [Configuring Pub/Sub notifications](https://docs.cloud.google.com/artifact-registry/docs/configure-notifications).

## Complete the enrollment form

  1. Go to the [customer enablement form](https://developers.google.com/assured-oss#get-started).

  2. Set **Choose one of the actions to perform** to **Enable access**.

  3. Enter your company name and your contact information, including a valid corporate email address to share enablement confirmation and any opted-in notification emails. Google uses your company name to verify the match with your email address.

  4. Enter the service account and AWS account information.

  5. Add the [Pub/Sub endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#pubsub_endpoints).

  6. Review the [terms of service](https://cloud.google.com/assured-open-source-software/terms).

  7. Click **Submit**.




After the request is submitted, you receive a confirmation email indicating the enablement success. In rare cases, the enablement process can take an hour or more.

**Note:** We recommend that you save this email for your records as it includes the summary of the key information you require to update or change your configuration in the future.

The Assured OSS system grants the required permissions to access and download software packages and security metadata to the service accounts.

## Other enrollment website capabilities

In addition to enabling your initial access to the Assured OSS service, the enrollment website lets you perform several configuration and management actions.

### Add additional service accounts or AWS account IDs to be enabled for Assured OSS access

Complete and submit additional instances of the [customer enablement form](https://developers.google.com/assured-oss#get-started) with your corporate email ID if you need to add additional service accounts or AWS account IDs that need access to Assured OSS. The corporate email address can be same or different from previous form submissions. The corporate email must belong to the same company domain. After the request is submitted, you receive a confirmation email indicating the enablement success. In rare cases, the enablement process can take an hour or more.

### Update your notification preferences

If you want to modify notification preferences for specific registered corporate email identities, complete and submit the [access form](https://developers.google.com/assured-oss#get-started) with **Update notification preferences** selected. Note that updating notification preferences requires approval and confirmation from the registered administrator. This process happens offline. You receive a confirmation email after the process is completed.

### Disable one or more enabled service accounts or AWS account IDs from access

If you want to disable access from specific registered service accounts or AWS account IDs, complete and submit the [access form](https://developers.google.com/assured-oss#get-started) with **Disable access** selected. Note that disabling access requires approval and confirmation from the registered administrator and is an offline process. You receive a confirmation email after the process is completed.

### Halt usage and access and disconnect from the service completely

If you want to halt all access and usage and disconnect from the service completely, complete and submit the [access form](https://developers.google.com/assured-oss#get-started) with **Close all access** selected. Note that halting all access and usage and disconnecting from the service requires approval and confirmation from the registered administrator and is an offline process. You receive a confirmation email after the process is completed.

## What's next

  * [Validate your connection to Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection)
  * [Set up remote repository access](https://docs.cloud.google.com/assured-open-source-software/docs/remote-repository-access)
  * [Download Java packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-java-packages)
  * [Download Go packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-go-packages)
  * [Download Python packages using direct repository access](https://docs.cloud.google.com/assured-open-source-software/docs/download-python-packages)
  * [Set up virtual repository access](https://docs.cloud.google.com/assured-open-source-software/docs/virtual-repository-access)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
