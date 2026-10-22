---
url: https://docs.cloud.google.com/developer-connect/docs/release-notes/
title: Developer Connect release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:40:32.220824+00:00
---

# Developer Connect release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Resources ](https://docs.cloud.google.com/developer-connect/docs/release-notes)



Send feedback 

#  Developer Connect release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Developer Connect. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/developer-connect-release-notes.xml) directly. 

## September 22, 2026

Announcement

The Secret Manager API is no longer enabled by default when you enable the Developer Connect API. For Git repository connections, you must enable the Secret Manager API explicitly.

## September 01, 2026

Announcement

Developer Connect [account connectors](https://docs.cloud.google.com/developer-connect/docs/account-connectors) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## August 14, 2026

Announcement

[Developer Connect insights](https://cloud.google.com/developer-connect/docs/insights) is now [generally available](https://cloud.google.com/products#product-launch-stages).

Feature

VPC Service Controls support for Developer Connect is [generally available](https://cloud.google.com/products#product-launch-stages). For instructions on using this feature, see [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

## July 13, 2026

Security

For GitLab Enterprise and Bitbucket Data Center connections, Developer Connect now checks permissions on the calling principal.

When you create or update repository connections, Developer Connect uses Secret Manager secrets to authenticate to third-party Git providers. Previously, these referenced secrets were retrieved by the Developer Connect service agent (P4SA) on your behalf, checking permissions only against the P4SA's credentials rather than those of the calling principal. To adhere to the security principle of least privilege, Developer Connect now checks permissions on both the calling principal (using end-user credentials) and the P4SA, to ensure both have the `secretmanager.versions.access` IAM permission on the referenced secrets.

This check only affects GitLab Enterprise (GLE) and Bitbucket Data Center (BBDC) connections.

For instructions and more details, see the [Developer Connect security bulletin](https://cloud.google.com/developer-connect/docs/security-bulletins#gcp-2026-048).

## April 21, 2026

Feature

You can now create an account connector [using a custom OAuth client](https://docs.cloud.google.com/developer-connect/docs/configure-connectors#configure-custom-oauth).

Feature

You can now use Git proxy with [account connectors](https://docs.cloud.google.com/developer-connect/docs/configure-connectors).

## February 12, 2026

Feature

Developer Connect now supports [HTTP connections](https://docs.cloud.google.com/developer-connect/docs/http-connections), for access to arbitrary HTTP endpoints.

## February 06, 2026

Feature

You can now [connect to Secure Source Manager](https://docs.cloud.google.com/developer-connect/docs/connect-secure-source-manager) using Developer Connect. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 18, 2025

Change

The ability to use [Git proxy](https://docs.cloud.google.com/developer-connect/docs/configure-git-proxy) for Git calls to your SCM connections is now [generally available](https://cloud.google.com/products#product-launch-stages).

## April 09, 2025

Feature

You can now use [account connectors](https://docs.cloud.google.com/developer-connect/docs/account-connectors) to connect your Google Cloud account with individual accounts on supported non-Google Developer Tools providers. This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## February 19, 2025

Change

You can now use Developer Connect to act as a proxy to run Git commands on source code management tools. You can toggle [**Enable git proxy**](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo#connection) on in the Google Cloud console, or pass the `--git-proxy-config-enabled` flag in glcoud. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Developer Connect now lets you connect to repositories on private networks.

To get started, see the guide for your source code management provider:

  * [GitHub Enterprise](https://docs.cloud.google.com/developer-connect/docs/connect-github-enterprise-private)
  * [GitLab Enterprise](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab-enterprise-private)
  * [Bitbucket Data Center](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-data-center-private)



Once they're connected, you can use [Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) on source code repositories outside of Google Cloud.

## February 11, 2025

Feature

Developer Connect now supports connectivity with Bitbucket Cloud and Bitbucket Data Center. These features are [Generally Available (GA)](https://cloud.google.com/products/#product-launch-stages). Learn how to get started at [Connect to Bitbucket Cloud](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-cloud) and [Connect to Bitbucket Data Center](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-dc).

Change

Developer Connect `gcloud` commands are now [Generally Available (GA)](https://cloud.google.com/products/#product-launch-stages).

## December 18, 2024

Feature

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_developer_connect) support for Developer Connect is now in [Preview](https://cloud.google.com/products/#product-launch-stages).

Feature

You can now manage Developer Connect resources by using custom organization policies. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Create custom organization policies](https://docs.cloud.google.com/developer-connect/docs/custom-constraints).

## September 30, 2024

Feature

Developer Connect is now [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages). This launch introduces the following features:

  * **Connectivity with several more source code management tools,** including GitHub Enterprise Cloud, GitHub Enterprise, GitLab and GitLab Enterprise

  * **Integration with Gemini Code Assist** , helping you get coding tips tailored to your private repositories




Gemini Code Assist users can connect their source code on GitHub or GitLab repositories and GitHub Enterprise, GitHub Enterprise Cloud, GitLab Enterprise repositories hosted on networks that can be accessed via the public internet.

Learn more at [Developer Connect overview](https://docs.cloud.google.com/developer-connect/docs/overview).

## May 14, 2024

Announcement

Developer Connect, Google Cloud's tool for connectivity to third-party source code management platforms, is now available in [Preview](https://cloud.google.com/products#product-launch-stages). To get started, see [Quickstart](https://docs.cloud.google.com/developer-connect/docs/connect-repo).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
