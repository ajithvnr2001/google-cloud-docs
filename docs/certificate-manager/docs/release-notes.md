---
url: https://docs.cloud.google.com/certificate-manager/docs/release-notes/
title: Certificate Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:53.957809+00:00
---

# Certificate Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/certificate-manager/docs/resources)



Send feedback 

#  Certificate Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for releases, features, and updates to Certificate Manager.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/certificate-manager-release-notes.xml) directly. 

## October 14, 2026

Change

Google-managed public SSL certificates signed by [Google Public CA](https://docs.cloud.google.com/certificate-manager/docs/public-ca) (pki.goog) are gradually transitioning from a 90-day validity period to a 45-day validity period to improve security.

To align with modern industry-wide security standards and promote shorter certificate lifespans, Google-managed public certificates now rotate more frequently. This proactive rotation enhances the overall security posture of load balancers. The transition requires no manual intervention or configuration changes as Certificate Manager automatically manages both issuance and renewal.

For more information, see [Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/core-components#google-managed-certificates) and [Use Google-managed certificates](https://docs.cloud.google.com/certificate-manager/docs/certificate-manager-best-practices#use_google_managed_certificates).

## September 24, 2026

Feature

You can now attach tags to Certificate Manager resources during creation. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Create and manage tags for Certificate Manager resources](https://docs.cloud.google.com/certificate-manager/docs/create-manage-tags).

## May 19, 2026

Feature

Certificate Manager (2nd gen) is available in [Preview](https://cloud.google.com/products#product-launch-stages). Certificate Manager (2nd gen) offers a unified control plane to observe, manage, and automate certificates across your organization.

For more information, see [Certificate Manager (2nd gen) overview](https://docs.cloud.google.com/certificate-manager/docs/v2/overview).

## December 05, 2024

Announcement

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) has passed HIPAA compliance validation and is [listed](https://docs.cloud.google.com/security/compliance/hipaa#covered-products) as a covered product in HIPPA compliance on Google Cloud.

## August 21, 2024

Feature

You can now update the "labels" and "descriptions" of your certificate issuance configurations using the Google Cloud CLI or API. For more information, see [Manage certificate issuance configuration](https://docs.cloud.google.com/certificate-manager/docs/issuance-configs#update).

Change

Regional Google-managed certificates are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

Change

Support for managing certificates independently in each project with separate authorization is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Manage DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/dns-authorizations).

## March 12, 2024

Feature

Certificate Manager supports integration with regional external Application Load Balancers and regional internal Application Load Balancers. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

## February 22, 2024

Feature

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) supports the management of certificates independently in each project with separate authorization. You can also issue regional managed certificates with Certificate Manager. This is a [public preview feature](https://cloud.google.com/products/#product-launch-stages). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

## September 28, 2023

Feature

[Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs) supports Mutual TLS (mTLS) authentication. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## August 18, 2023

Feature

Certificate Manager now supports integration with regional external Application Load Balancers and regional internal Application Load Balancers. This is a [public preview feature](https://cloud.google.com/products/#product-launch-stages). For more information, see [Certificate Manager overview](https://docs.cloud.google.com/certificate-manager/docs/overview).

## April 19, 2023

Change

The Certificate Authority Service integration feature is now generally available.

Feature

Certificate Manager now supports Mutual TLS (mTLS) authentication. This is a public preview feature. For more information, see [Trust configs](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#trust-configs).

## December 15, 2022

Feature

You can now view a list of certificates managed by Certificate Manager in your project in the Cloud Console. You can also view detailed information about each certificate. For instructions, see [Manage Certificates](https://docs.cloud.google.com/certificate-manager/docs/certificates). 

Load Balancing SSL certificates, previously available in the "Certificates" tab on the "Load Balancing" page, are now also available in the Certificate Manager page in the "Classic Certificates" tab.

## June 28, 2022

Announcement

This is the General Availability release of Certificate Manager.

## May 01, 2022

Announcement

Billing has been enabled. Certificate Manager usage is billed at 100% discount until the end of the Preview period.

## April 05, 2022

Feature

This release of Certificate Manager adds support for target SSL proxies and the global external HTTP(S) load balancer (preview).

## January 28, 2022

Announcement

This is the initial Preview release of Certificate Manager.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
