---
url: https://docs.cloud.google.com/developer-device-platform/release-notes/
title: Developer Device Platform release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:10:38.903278+00:00
---

# Developer Device Platform release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Resources ](https://docs.cloud.google.com/developer-device-platform/resources)



Send feedback 

#  Developer Device Platform release notes Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page documents production updates to Developer Device Platform. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

See the [Device Run Google Cloud CLI - Release Notes](https://docs.cloud.google.com/sdk/docs/release-notes#device_run) for a summary of the latest features and fixes.

## October 8, 2026

**Feature** : The Device Run API now provides the [`sessions.batchGet`](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.sessions/batchGet) method, which retrieves up to 500 automation sessions in a single request. Sessions are returned in the same order as requested. To request a large number of sessions over REST, see [Why does `sessions.batchGet` return an HTML `400 Bad Request` error?](https://docs.cloud.google.com/developer-device-platform/troubleshooting#batchget-url-too-long)

## August 12, 2026

**Preview** : The Developer Device Platform enables remote device orchestration in an enterprise-scale, cloud-native device farm for developers to build and test applications without the overhead of purchasing myriad test devices.

See the [Introducing the Developer Device Platform for agentic mobile app development](https://cloud.google.com/blog/topics/developers-practitioners/announcing-developer-device-platform-on-google-cloud) blog post for a summary of the product.

The Preview launch offers these features:

  * [Device Catalog](https://docs.cloud.google.com/developer-device-platform/device-catalog) \- Describe all of the device types in the Developer Device Platform lab and delve into each type
  * [Device Run](https://docs.cloud.google.com/developer-device-platform/device-run) \- Run tests on devices in the Developer Device Platform lab and see the results in Google Cloud
  * [Find Logs](https://docs.cloud.google.com/developer-device-platform/device-run/find-logs) \- See your results at the command line and in the Google Cloud console
  * [Device Streaming API](https://docs.cloud.google.com/device-streaming/docs) \- Connect to remote physical Android devices and interact with your app as if it is connected to your local machine
  * [Agentic Development with Device Streaming](https://docs.cloud.google.com/developer-device-platform/agent-skill) \- Use Developer Device Platform agent skill to find, reserve and connect to devices in Developer Device Platform



Jump in with our [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) and see our [API Reference](https://docs.cloud.google.com/developer-device-platform/apis) for complete details.

This command line offering aimed at Android is just the beginning. We plan to provide Google Cloud console integration and iOS support. Stay tuned here for updates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
