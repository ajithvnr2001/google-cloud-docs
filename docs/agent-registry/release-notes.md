---
url: https://docs.cloud.google.com/agent-registry/release-notes/
title: Agent Registry release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:17.948148+00:00
---

# Agent Registry release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Resources ](https://docs.cloud.google.com/agent-registry/resources)



Send feedback 

#  Agent Registry release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Agent Registry. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/agent-registry-release-notes.xml) directly. 

## July 23, 2026

Feature

Agent skill governance is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Agent Registry supports standalone skill governance, helping enable secure, enterprise-level management and governance of standalone skills for AI agents. You can register skill resources, upload and validate ZIP payload packages, track version history through immutable skill revisions, and review verified skill publishers.

This release includes the following features:

  * **Lifecycle and versioning:** Register and manage standalone `Skill` resources, lifecycle states, and version snapshots (`SkillRevision`).
  * **Console support:** A dedicated **Skills** tab in Google Cloud Console to register, update, download, and monitor skills and revisions.
  * **Semantic search:** Query the registry to search and discover standalone skills.



For more information, see [Register skills](https://docs.cloud.google.com/agent-registry/register-skills) and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills).

## June 18, 2026

Announcement

Agent Registry is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

The following are features available in Agent Registry for the GA launch stage:

  * **API v1 and client libraries:** The `v1` version of the Agent Registry API is available. Cloud client libraries are available in C#, Go, Java, Node.js, PHP, Python, and Ruby.
  * **A2A v1 support:** Agent Registry supports Agent-to-Agent (A2A) protocol version `1.0`, letting you explicitly declare transport endpoints and bindings inside the `supportedInterfaces` array, in addition to the existing `0.3` schema support.
  * **Terraform support:** Terraform scripts for Application Default Credentials (ADC) have graduated to General Availability. You can use Terraform to configure and manage your agents, MCP servers, endpoints, and bindings.



## April 22, 2026

Issue

The following known issues affect Agent Registry:

  * **Search location filtering:** When calling the `SearchAgents` or `SearchMcpServers` APIs for the `global` location, the results might incorrectly include resources from `us` and `eu` multi-regions.
  * **URN mismatch:** When searching for agents or MCP servers in the Google Cloud console, the page might display an invalid URN format in the search results list.
  * **Console error:** Users who actively switch between tabs on the MCP server details page in the Google Cloud console might encounter an unexpected throttling error.



Announcement

The Agent Registry remote Model Context Protocol (MCP) server is available in [Preview](https://cloud.google.com/products#product-launch-stages). You can connect your AI applications to the Agent Registry MCP server to dynamically discover other agents, endpoints, and MCP servers available in your environment.

For more information, see [Use the Agent Registry remote MCP server](https://docs.cloud.google.com/agent-registry/use-agentregistry-mcp).

Announcement

Agent Registry is available in [Preview](https://cloud.google.com/products#product-launch-stages). Agent Registry is a centralized catalog for discovering and registering agents and Model Context Protocol (MCP) servers.

For more information, see the [Agent Registry overview](https://docs.cloud.google.com/agent-registry/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
