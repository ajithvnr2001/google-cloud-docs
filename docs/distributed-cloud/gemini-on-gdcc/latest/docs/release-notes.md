---
url: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/release-notes/
title: Gemini on Google Distributed Cloud connected API release notes \u00a0|\u00a0 Gemini on GDC API on GDC connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:11.761614+00:00
---

# Gemini on Google Distributed Cloud connected API release notes  |  Gemini on GDC API on GDC connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/release-notes/

**Gemini on GDC API on GDC connected Public Preview (current)**

For version information, see the [Gemini on GDC API on GDC connected release notes](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/release-notes). 

Available versions: **Public Preview**

  * [ Home ](https://docs.cloud.google.com/)
  * [ Gemini on GDC API on GDC connected ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest)
  * [ Documentation ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs)
  * [ Resources ](https://docs.cloud.google.com/distributed-cloud/gemini-on-gdcc/latest/docs/resources)



Send feedback 

#  Gemini on Google Distributed Cloud connected API release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for releases, features, and updates to Gemini on Google Distributed Cloud connected API connected.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gemini-on-gdcc-release-notes.xml) directly. 

## September 03, 2025

Announcement

This is the Public Preview release of Gemini on Google Distributed Cloud connected API.

Issue

This release of Gemini on GDC connected API contains the following known issues:

  * **Servo metrics not captured by Cloud Monitoring.** Servo metrics for Gemini on GDC connected API are not captured by Cloud Monitoring. Other supported metrics are captured as expected.

  * **User identity is not supported.** To successfully deploy a Gemini on GDC connected API endpoint, you must use a service account to generate the access credentials.

  * **Service account keys expire after 14 days.** If you use a service account key older than 14 days, you can't use it to generate endpoint access credentials. In such situations, you must generate a fresh service account key.

  * **Disabling Cloud projects or Cloud services is not supported.** To disable a Cloud project or a Cloud service on your Gemini on GDC connected API deployment, contact your Google representative.

  * **Model deployment might intermittently fail**. If you encounter a model deployment failure, contact your Google representative to resolve this issue.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
