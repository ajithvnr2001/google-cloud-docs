---
url: https://docs.cloud.google.com/mcp/release-notes/
title: Google Cloud MCP servers release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:11:50.970800+00:00
---

# Google Cloud MCP servers release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Resources ](https://docs.cloud.google.com/mcp/resources)



Send feedback 

#  Google Cloud MCP servers release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Cloud MCP servers. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.comhttps://docs.cloud.google.com/feeds/mcp-release-notes.xml) directly. 

## September 14, 2026

Feature

Google and Google Cloud MCP servers support [Version 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) of the Model Context Protocol. These changes are backward compatible with [Version 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25). For more information on MCP features and extensions, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview) and [MCP Key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## July 22, 2026

Fixed

Cursor has fixed the [issue](https://docs.cloud.google.com/mcp/release-notes#June_15_2026) with its desktop redirect URI and can be used with Google and Google Cloud MCP servers. To learn how to configure MCP servers for Cursor, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#cursor).

## July 02, 2026

Feature

You can use the `tool.name` attribute to control access to specific MCP tools in your Identity and Access Management (IAM) allow and deny policies. For more information see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## June 15, 2026

Issue

Due to an authentication issue, Google and Google Cloud remote MCP servers can't be used with [Cursor](https://cursor.com/docs).

Our OAuth 2.0 client ID creation flow doesn't allow adding custom URI schemas like Cursor's callback URL, `cursor://anysphere.cursor-mcp/oauth/callback`, as redirect URLs.

## May 01, 2026

Announcement

[Google and Google Cloud remote MCP servers](https://docs.cloud.google.com/mcp/overview) are generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Individual MCP servers might be in Preview or GA—to check the launch status of a product, search for the product in [Supported products](https://docs.cloud.google.com/mcp/supported-products).

To learn more about what you can do with MCP servers, read [50+ fully managed MCP servers now available for Google Cloud services](https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone).

## April 10, 2026

Feature

You can use Cloud Trace to get answers about your MCP server use, tool failures, and latency causes. To get started, see [Use Cloud Trace to monitor MCP use](https://docs.cloud.google.com/mcp/monitor-mcp-tool-use-with-cloud-trace).

## March 17, 2026

Deprecated

The custom constraint `gcp.managed.allowedMCPServices` and organization policy control of MCP use is deprecated and will no longer work.

You can use Identity and Access Management deny policies to control MCP use. For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

Change

Starting March 17, 2026, you no longer need to separately enable Model Context Protocol (MCP) servers. Remote MCP endpoints are available by default when you enable a [supported product](https://docs.cloud.google.com/mcp/supported-products) in your project. This update is rolling out gradually across regions.

## February 17, 2026

Change

After March 17, 2026, Google and Google Cloud remote Model Context Protocol (MCP) servers are automatically enabled when you enable a [supported service](https://docs.cloud.google.com/mcp/supported-products).

Deprecated

The custom constraint `gcp.managed.allowedMCPServices` and organization policy control of MCP use is deprecated. If you created an organization policy to control MCP use prior to February 17, 2026, then it won't work after March 17, 2026. If you don't use the `gcp.managed.allowedMCPServices` constraint, then effective February 17, 2026, you aren't able to use it.

You can use Identity and Access Management deny policies to control MCP use. For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam)

## December 10, 2025

Announcement

Support for Model Context Protocol (MCP) use is available in Preview for select Google and Google Cloud services.

To see a demo and read about why we're offering remote MCP servers available over HTTP instead of local MCP servers, read [Announcing official Model Context Protocol (MCP) support for Google services](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services).

For more information, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
