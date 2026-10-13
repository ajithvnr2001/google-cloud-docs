---
url: https://docs.cloud.google.com/secure-source-manager/docs/release-notes/
title: Secure Source Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:35.130865+00:00
---

# Secure Source Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/secure-source-manager/docs/resources)



Send feedback 

#  Secure Source Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Secure Source Manager. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/secure-source-manager-release-notes.xml) directly. 

## September 29, 2026

Feature

Secure Source Manager webhooks now support service account authorization. For more information, see [Webhooks overview](https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview) and [Set up webhooks](https://docs.cloud.google.com/secure-source-manager/docs/set-up-webhooks).

## September 21, 2026

Feature

Secure Source Manager now supports rendering Mermaid diagrams in Markdown files, pull requests, issues, and comments. You can use standard `mermaid` fenced code blocks to create flowcharts, sequence diagrams, class diagrams, entity-relationship diagrams, state diagrams, and XY charts.

For more information, see [ Add diagrams with Mermaid](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests#add-diagrams-with-mermaid).

## September 16, 2026

Feature

Secure Source Manager webhooks now support **Pull request comment** trigger events. You can configure webhooks to trigger notifications whenever a comment is added, edited, or deleted on a pull request.

For more information, see the [ Pull request comment event payload](https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview#pull-request-comment-event-payload) in the [Webhooks overview](https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview).

## August 15, 2026

Feature

The Secure Source Manager Model Context Protocol (MCP) server is available in [Preview](https://docs.cloud.google.com/products#product-launch-stages). You can use the Secure Source Manager MCP server to connect AI tools and coding assistants directly to your repositories, branch rules, pull requests, and issues.

For more information, see the [ Secure Source Manager MCP reference](https://docs.cloud.google.com/secure-source-manager/docs/reference/mcp).

## July 02, 2026

Feature

Secure Source Manager is now compliant with EU VPAT / WCAG 2.2.

## May 28, 2026

Breaking

To enhance security and address potential vulnerabilities (such as GHSA-3m6q-h5gj-7mrw), the Secure Source Manager Git-over-SSH server configuration has removed support for several legacy and insecure SSH algorithms.

SSH clients must support one or more of the following modern algorithms to connect:

  * **Key Exchange Algorithms:** `curve25519-sha256`, `diffie-hellman-group14-sha256`
  * **Ciphers:** `chacha20-poly1305@openssh.com`, `aes128-ctr`, `aes192-ctr,aes256-ctr`, `aes128-gcm@openssh.com`, `aes256-gcm@openssh.com`
  * **MACs:** `hmac-sha2-256-etm@openssh.com`, `hmac-sha2-256`



Users with old or non-standard SSH clients lacking support for these algorithms will be unable to connect using SSH for Git operations. Ensure your SSH client is up-to-date.

## May 27, 2026

Feature

Secure Source Manager enforces a daily rate quota on the size of code scanned for credentials per instance. The default quota limit is 1 GB per day per instance. For more information, see [Quotas and limits](https://docs.cloud.google.com/secure-source-manager/docs/quotas).

## May 06, 2026

Feature

You can now use [CODEOWNERS files](https://docs.cloud.google.com/secure-source-manager/docs/codeowners) to define required reviewers for pull requests.

## February 06, 2026

Feature

You can now [connect to Secure Source Manager](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager) using Developer Connect.

## February 03, 2026

Feature

You can now assign custom domains for your private Secure Source Manager instance's HTML, API, Git HTTP, and Git SSH endpoints. To use custom domains, you must provide your own Certificate Authority (CA) certificate and CA pool during instance creation. You can only create custom domains using the API when you first create an instance. For more information, see [Create a Private Service Connect Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-private-service-connect-instance).

## February 02, 2026

Feature

Secure Source Manager is now available in the following [regions](https://docs.cloud.google.com/secure-source-manager/docs/locations#regions):

  * us-east1 (South Carolina)



## September 10, 2025

Announcement

Secure Source Manager is [compliant with the Health Insurance Portability and Accountability Act](https://docs.cloud.google.com/security/compliance/hipaa) (HIPAA), and is also [FedRAMP High compliant](https://docs.cloud.google.com/security/compliance/fedramp).

## August 21, 2025

Feature

You can now use a Google-managed certificate when you create a [create a Private Service Connect Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-private-service-connect-instance#create-private-service-connect-instance).

## August 14, 2025

Change

Integrated data loss prevention (DLP) is now [generally available](https://cloud.google.com/products#product-launch-stages)

## August 04, 2025

Announcement

Secure Source Manager is now [generally available](https://cloud.google.com/products#product-launch-stages) for all customers.

## July 08, 2025

Change

Secure Source Manager is now available in the following [regions](https://docs.cloud.google.com/secure-source-manager/docs/locations#regions):

  * australia-southeast1 (Sydney)
  * asia-northeast1 (Tokyo)



## April 15, 2025

Feature

Regional endpoints are now available in Secure Source Manager. For more information, see [Configure data locality by using regional endpoints](https://docs.cloud.google.com/secure-source-manager/docs/endpoints).

## December 19, 2024

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Secure Source Manager resources. For more information, see [Manage resources with custom constraints](https://docs.cloud.google.com/secure-source-manager/docs/custom-constraints).

## November 21, 2024

Feature

Secure Source Manager supports email notifications. For more information, see [Notifications overview](https://docs.cloud.google.com/secure-source-manager/docs/notifications-overview). To configure notifications, follow the instructions in [Set up notifications](https://docs.cloud.google.com/secure-source-manager/docs/set-up-notifications).

## November 14, 2024

Feature

Secure Source Manager supports [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

To create an instance with Workforce Identity Federation enabled, follow the instructions in [Create a Secure Source Manager instance to use with federated identities](https://docs.cloud.google.com/secure-source-manager/docs/create-instance-federated-identities).

## September 11, 2024

Feature

Secure Source Manager integration with Cloud Build lets you define your Cloud Build configuration and build triggers in your Secure Source Manager repository. To learn how to trigger builds automatically, see [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build).

Feature

Secure Source Manager branch protection is Generally Available. To learn more about branch protection, see the [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview) and [Configure branch protection](https://docs.cloud.google.com/secure-source-manager/docs/configure-branch-protection).

## October 12, 2023

Announcement

[Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) by invitation only.

## September 25, 2023

Change

Secure Source Manager is now available in the `northamerica-northeast1` (Montréal) [region](https://cloud.google.com/secure-source-manager/docs/locations#regions).

## August 14, 2023

Announcement

A one-time clean up of unused Secure Source Manager instances is scheduled for August 16, 2023. Instances that haven't been accessed or used for 30 days or more will be deleted.

We previously announced that this clean up policy would be an ongoing policy, but that has been changed based on user feedback. This will be a one-time clean up operation. 

To prevent deletion of your Secure Source Manager instance, you can perform any of the following actions: log in using the web interface, use Git to push or pull from your repository, or access the instance via the Secure Source Manager API.

## July 20, 2023

Feature

Secure Source Manager is now available in the `me-west1` (Tel Aviv) [region](https://docs.cloud.google.com/secure-source-manager/docs/locations#regions).

## July 17, 2023

Announcement

A new policy to clean up unused Secure Source Manager instances is now in effect. On August 16, 2023, instances that have not been accessed or used for 30 days or more will be deleted. 

To prevent deletion of your Secure Source Manager instance, you can perform any of the following actions: log in using the web interface, use Git to push or pull from your repository, or access the instance via the Secure Source Manager API.

## June 15, 2023

Announcement

Secure Source Manager is available in [Preview](https://cloud.google.com/products#product-launch-stages). 

Host your source code in a single tenant, regionally deployed, managed source code repository hosted on Google Cloud. 

For preview access, contact [secure-source-manager-support@google.com](mailto:secure-source-manager-support@google.com).

To get started with Secure Source Manager, [Enable the Secure Source Manager API](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable) and then [Deploy and access an instance](https://docs.cloud.google.com/secure-source-manager/docs/deploy-access-instance).

## April 28, 2023

Feature

Secure Source Manager is now available in `asia-east1` (Taiwan) and `europe-west4` (Netherlands) [regions](https://docs.cloud.google.com/secure-source-manager/docs/locations#regions).

## April 06, 2023

Change

Secure Source Manager has entered phase 2 of implementing the [Google Cloud project location restriction](https://docs.cloud.google.com/secure-source-manager/docs/overview#project_location_restriction). The changes are as follows:

  * New repositories must be created in the same project as their parent instance. 
  * A new Repo Creator role (`roles/securesourcemanager.repoCreator`) is available.
  * All repositories in separate projects from their parent instances will be deleted after May 1, 2023.
  * Repositories in separate projects from their parent instances can request to be migrated. For migration steps see [Migrate to single-project repositories](https://docs.cloud.google.com/secure-source-manager/docs/migrate-repositories).



If you have any questions, feel free to reach out to us at [secure-source-manager-support@google.com](mailto:secure-source-manager-support@google.com).

## March 10, 2023

Change

Repositories must be created in the same Google Cloud project as their parent Secure Source Manager instance. Customers can continue to use repositories previously created in separate projects from their parent instance.

For more details see [Google Cloud project location restriction](https://docs.cloud.google.com/secure-source-manager/docs/information-multi-project).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
