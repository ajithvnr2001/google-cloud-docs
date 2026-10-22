---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-package-changelog/
title: Salesforce package changelog \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:54.487780+00:00
---

# Salesforce package changelog  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-package-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Salesforce package changelog Stay organized with collections  Save and categorize content based on your preferences. 

This document is the Salesforce package changelog.

## 1.44

Fixed an issue where the canvas applications threw an undefined error.

Salesforce Connect app [Version 1.44](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKk0000011Nu5)

## 1.41

On June 15th 2025, Salesforce is rolling out an automatic upgrade to its International Components for Unicode (ICU) locale data. This affects how date, time, number, and currency formatting are handled across Apex, Visualforce, and Lightning components.

This change affects Salesforce integrations that are using Apex API version 45.0 or earlier. These integrations use the legacy Java locale behavior, which could cause formatting discrepancies, incorrect parsing, or runtime errors.

To maintain compatibility with the Salesforce ICU update and prevent any operational impact, you must [install the v1.41 update](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKk0000011MO1) before June 15th, 2025.

## 1.38

Fixed an issue when a customer used `Contact.Phone` as an encrypted field.

To allow queries on encrypted phone fields in Salesforce, we introduced a new option in the developer settings for Salesforce CRM. This lets customers who have those fields enabled on the lookup field convert queries in our backend to be exact match queries. This means that along with this checkbox they'll need to set a phone number format.

This update requires upgrading the Salesforce Connect app to [Version 1.38](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKk000000olnE).

**Note:** Only deterministic encryption is supported.

For information about installing the most current version of the Salesforce Connect app, see the [Salesforce](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide).

For information about enabling the search function for encrypted phone fields, see [Enable exact search queries for encrypted phone fields](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-exact-search-queries).

For information about enabling encryption, see [Enable encryption on standard properties](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-enable-encryption) for how to enable the search function for encrypted phone fields.

## 1.37

Fixed a chat adapter resizing bug.

Salesforce Connect app Version [1.37](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000YUY7).

## 1.36

Fixed an email component bug.

Salesforce Connect app [Version 1.36](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000YUXi).

## 1.33

Added the email Component.

Salesforce Connect app [Version 1.33](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t4M000000YUMo).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
