---
url: https://docs.cloud.google.com/service-usage/docs/release-notes/
title: Service Usage release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:29.252299+00:00
---

# Service Usage release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ Resources ](https://docs.cloud.google.com/service-usage/docs/resources)



Send feedback 

#  Service Usage release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page details updates to Service Usage. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/service-usage-release-notes.xml) directly. 

## July 30, 2026

Deprecated

Support for managing Model Context Protocol (MCP) endpoint enablement using the Service Usage v2beta API is shut down.

For more information, see [Feature deprecations](https://docs.cloud.google.com/service-usage/docs/deprecations).

## July 24, 2026

Deprecated

As of July 30, 2026, support for managing Model Context Protocol (MCP) server enablement and consumer policies using the Service Usage v2beta API will be shut down.

For more information, see [Feature deprecations](https://docs.cloud.google.com/service-usage/docs/deprecations).

## June 03, 2026

Deprecated

Support for managing Model Context Protocol (MCP) server enablement and consumer policies using the Service Usage v2beta API is deprecated. MCP server enablement is no longer required. Enabling the underlying service is sufficient.

For more information, see [Feature deprecations](https://docs.cloud.google.com/service-usage/docs/deprecations).

## November 11, 2025

Feature

Service Usage support for [hierarchical service activation](https://docs.cloud.google.com/service-usage/docs/hierarchical-service-activation/overview) is available in [Preview](https://cloud.google.com/products/#product-launch-stages). This feature lets you enable and disable services across your organization's resource hierarchy.

## June 01, 2018

Feature

**Public v1 release** : Service Usage is now generally available. You can use version 1 of Service Usage to discover and manage other APIs and services in your Google Cloud project.

Change

The default behavior of the [`services.disable`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable) method now generates an error if any currently enabled services depend on the service you are trying to disable. If you set the `disableDependentServices` field to true, any enabled services that depend on the service you are disabling, are also disabled.

## March 01, 2018

Feature

When you call the [`services.list`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services/list) method, you can now filter for disabled APIs and services.

## February 01, 2018

Feature

**Public beta release** : Service Usage is an infrastructure service of Google Cloud that lets you discover and manage other APIs and services in your Cloud project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
