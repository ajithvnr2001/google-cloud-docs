---
url: https://docs.cloud.google.com/apigee/docs/apihub/release-notes/
title: Apigee API hub release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:30.843575+00:00
---

# Apigee API hub release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee API hub release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to API hub software in 2024 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

  
rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-api-hub-release-notes.xml) directly. 

## September 30, 2026

Feature

**Service type system attribute (GA)**

API hub now includes **Service type** , a system attribute that classifies an API as `Code`, `Model`, `Agent`, or `Skill`. Service type describes what a service is. **API style** describes how you call it. Use Service type to find and govern your APIs, agents, models, and skills.

Set Service type when you register or edit an API. To show only your agents, filter the API list by Service type, or select the new **Agent** chip. In the API, use the `service_type` field.

This feature is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Supported system attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#supported-system-attributes).

Feature

**AI performance and Tool performance dashboards in API insights**

API insights in API hub now includes two dashboards for AI and agent traffic:

  * **AI performance** reports token usage and model latency for the large language models called through your gateways, with filters for model and provider.
  * **Tool performance** reports traffic, throughput, payload sizes, and latency for your Model Context Protocol (MCP) tools, with filters for MCP server, deployment, and tool name.



For more information, see [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard).

## September 23, 2026

Feature

**Preview launch of AWS API Gateway and Azure API Management plugins**

API hub now includes two new built-in plugins for ingesting API metadata from third-party gateways: **AWS API Gateway** and **Azure API Management**. Both plugins are in [Public Preview](https://cloud.google.com/products#product-launch-stages), extending API hub's multi-cloud governance to give you a single pane of glass across your Google Cloud, AWS, and Azure APIs.

**What's new**

  * **Automated discovery and onboarding** : Connect your AWS account or Azure API Management (APIM) service and API hub automatically discovers your existing deployed APIs and related metadata.
  * **Scheduled pull sync** : A full metadata sync runs every 6 hours by default, with reconciliation (upserts and orphan deletes) to keep your catalog in sync with the source gateway.
  * **Optional near-real-time push sync** : Deploy a customer-managed AWS Lambda function (for AWS API Gateway) or Azure Function (for Azure API Management) to relay control-plane change events to API hub in near real time. For sample deployment code, see the [apigee-samples](https://github.com/GoogleCloudPlatform/apigee-samples/tree/main/apihub-plugins) repository.



For more information, see [About plugins](https://docs.cloud.google.com/apigee/docs/apihub/plugins), [Manage third-party plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-third-party-plugins), and [Create a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances).

Feature

**Spec-to-deployment linkage and gateway revision tracking in API hub (GA)**

API hub now provides a first-class, bidirectional link between API specifications, operations, and the deployments that serve them, together with native tracking of the underlying gateway revision.

**What's new**

  * **Direct visibility between specs and deployments** : See exactly which API specification and operations are served by a specific deployment, and navigate from a spec to the deployments that serve it.
  * **Native gateway revision tracking** : Deployments now capture and display their underlying gateway revision (for example, an Apigee proxy revision) via the new `source_revision` field on the Deployment resource.
  * **More accurate operation resolution** : When multiple revisions expose overlapping operations (same method and path), API hub associates each operation with its specific specification instead of dropping duplicates.
  * **Multiple spec revisions per API** : API hub can store multiple revisions of the same spec for an API deployed across different environments.



## August 12, 2026

Feature

**Configure and deploy MCP servers with gcloud CLI**

You can use the `gcloud apihub locations configure-and-deploy-server` command to configure and deploy API hub Model Context Protocol (MCP) servers to an attached Apigee runtime. Define MCP tools inline or by referencing a YAML or JSON specification file to expose your API hub operations for agent integrations.

For more information, see [gcloud CLI for API hub](https://docs.cloud.google.com/apigee/docs/apihub/gcloud-cli-apihub).

## July 24, 2026

Feature

**General availability (GA) launch of Model Context Protocol (MCP) in API hub**

The API hub MCP server is [Generally Available (GA)](https://cloud.google.com/products#product-launch-stages). This release enables seamless integration between your AI agents and API hub, allowing your applications to discover, query, and manage your API ecosystem using natural language.

**What's new in GA**

  * **Expanded read and write capabilities** : AI agents can create, update, and delete APIs, versions, specs, and deployments. They can also configure and deploy MCP discovery proxies in Apigee.
  * **Global endpoint routing** : Connect to the API hub MCP server using the global endpoint (`apihub.googleapis.com/mcp`), in addition to the supported regional endpoints. For a list of supported regions, see the [API hub MCP reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp#server-endpoints).
  * **Granular OAuth scopes** : Use service-specific OAuth scopes (`apihub.readonly` and `apihub.readwrite`) for more secure access.
  * **Model Armor integration** : Protect MCP tool invocations from prompt-injection and other attacks by integrating with Model Armor.



For configuration details and a complete list of available tools, see [API hub MCP reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp).

Feature

**Configure and deploy MCP servers with API hub RPC**

API hub now includes a new RPC, `ConfigureAndDeployServer`, which enables the configuration and deployment of Model Context Protocol (MCP) servers directly to an Apigee runtime.

For more information, see [Manage MCP proxies](https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-proxies) and the [API hub reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub).

## May 12, 2026

Feature

**MCP tools support for Agentic AI workflows (Preview)**

API hub now exposes read-only APIs as Model Context Protocol (MCP) tools. Agentic AI applications can now use the standard MCP `tools/list` and `tools/call` methods to list and inspect API hub resources, including APIs, specs, versions, and deployments.

This feature is in [Public Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [API hub MCP reference](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/mcp).

## May 07, 2026

Feature

**Unified MCP Proxy Configuration in API hub (Preview)**

API hub allows you to create and deploy Model Context Protocol (MCP) discovery proxies. Select specific API operations from your registered catalog, bundle them into an MCP server, and automatically deploy them as discovery proxies in your Apigee project. This feature eliminates the need to manually author MCP specifications in Apigee.

This feature is in [Public Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage MCP proxies](https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-proxies).

## April 06, 2026

Feature

**Agent Registry integration support for MCP metadata (Preview)**

API hub now includes a managed integration with Agent Registry to automatically synchronize Model Context Protocol (MCP) servers and tools metadata. This feature enables AI agents to discover and interact with the APIs registered in your hub without manual configuration.

This feature is in [Public Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage Agent Registry integration](https://docs.cloud.google.com/apigee/docs/apihub/manage-agent-registry-integration).

## March 10, 2026

Feature

**Security monitoring condition support in Advanced API Security for multi-gateway projects**

Advanced API Security's multi-gateway Risk Assessment feature (available through API hub) now includes support for security monitoring conditions and alerts.

Security monitoring conditions allow you to map resources (gateways) to security profiles. Cloud Monitoring can then use this mapping to create dedicated dashboards to track security scores over time and alert based on metric levels.

For information on monitoring conditions features and usage see [Manage monitoring conditions for multiple Apigee organizations and gateways](https://docs.cloud.google.com/apigee/docs/apihub/manage-monitoring-conditions-multi-gateway).

**Note:** Rollouts of this release to production instances might take up to 5 business days to complete across all Google Cloud zones. Your instances might not have the feature available until the rollout is complete.

Feature

**Support for Apigee Edge Private Cloud (OPDK) in Advanced API Security for multi-gateway projects**

API hub Advanced API Security for multi-gateway now includes support for the OPDK gateway type for risk assessment security profiles.

For information on risk assessment custom security profiles and gateway specification, see [Create a security profile](https://docs.cloud.google.com/apigee/docs/apihub/manage-security-profiles-multi-gateway#create-a-security-profile).

**Note:** Rollouts of this release to production instances might take up to 5 business days to complete across all Google Cloud zones. Your instances might not have the feature available until the rollout is complete.

## March 04, 2026

Feature

**gcloud CLI support for API hub**

The `gcloud CLI` now supports Apigee API hub, allowing you to manage your organization's API catalog, versions, and lifecycle metadata directly from the command line.

For more information see [gcloud CLI for API hub](https://docs.cloud.google.com/apigee/docs/apihub/gcloud-cli-apihub).

## February 23, 2026

Feature

**Preview release of specification boost**

API hub now supports the preview release of specification boost, an AI-powered add-on that lets you automatically enhance the readability and discoverability of your API specifications in API hub. It analyzes your existing specification files and generates boosted versions enriched with richer details, including additional examples, clearer descriptions, better error documentation, and more.

For more information see [Specification boost add-on](https://docs.cloud.google.com/apigee/docs/apihub/spec-boost).

**Note:** Rollouts of this release to production instances might take up to 5 business days to complete across all Google Cloud zones. Your instances might not have the feature available until the rollout is complete.

## January 12, 2026

Feature

**Ingest API Gateway metadata into API hub**

API hub now supports automatic metadata ingestion from [Google Cloud API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway). You can now [attach](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project) your API Gateway projects to API hub to enable auto-ingestion for all your APIs. For more information see [Centralize API management using API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-overview).

**Note:** Rollouts of this release to production instances might take up to 5 business days to complete across all Google Cloud zones. Your instances might not have the feature available until the rollout is complete.

## December 17, 2025

Feature

**Advanced API Security for multi-gateway projects**

Apigee Advanced API Security can now centrally manage and govern the security posture of your APIs across multiple Apigee projects, environments, and gateways. This enhancement leverages API hub to provide a single, unified view of your API security, helping you to identify risks and enforce standards consistently across your entire organization.

This enhancement introduces the following key capabilities:

  * **Unified risk assessment:** view and manage security scores for all your APIs in a centralized dashboard, regardless of which project, environment, or gateway they are deployed in.
  * **Customizable security profiles:** create and manage custom security profiles and apply them consistently across your multi-gateway landscape.



Supported gateways:

  * Apigee X
  * Apigee hybrid
  * Apigee Edge Public Cloud



To enable this feature, navigate to the **Add-on management page** in API hub and enable the **Apigee Advanced API Security** add-on.

Advanced API Security currently has limited support for VPC Service Controls (VPC-SC). To avoid potential feature limitations, we recommend enabling this add-on for API hub instances associated with Apigee organizations that don't have VPC-SC enabled.

For more information, see [Advanced API Security for multiple Apigee organizations and gateways](https://docs.cloud.google.com/apigee/docs/apihub/advanced-api-security-multi-gateway).

**Note:** Rollouts of this feature will begin today, and may take five or more business days to be completed across all Google Cloud zones. You may not be able to view or use this feature until the rollout is complete.

## December 15, 2025

Feature

**New API card view**

A new card view is now available for APIs in API hub. This view provides a more visual and comprehensive way to browse, edit, and manage your APIs, complementing the existing list view. 

The card view highlights key information for each API, such as the owner, last modified date, target users, gateway, API style, and business unit, to enhance discoverability and provide a richer at-a-glance overview of your API landscape.

You can switch between the list and card views from the **API hub > APIs** page.

## December 11, 2025

Feature

**Model Context Protocol (MCP) support in API hub**

API hub now supports the Model Context Protocol (MCP) as a first-class API style. This enables you to ingest, register, and manage MCP APIs and their associated tools.

**Key capabilities include:**

  * **MCP API registration:** Register MCP APIs manually or via API hub APIs to create a single registry for your agentic services.
  * **MCP tools:** Attach MCP specification files to your APIs. API hub parses these files to automatically extract and display the MCP tools in the UI.



For more information, see [API resources overview](https://docs.cloud.google.com/apigee/docs/apihub/apis-intro), [Register MCP APIs](https://docs.cloud.google.com/apigee/docs/apihub/register-mcp-apis), and [Manage MCP tools](https://docs.cloud.google.com/apigee/docs/apihub/manage-mcp-tools).

**Note:** Rollouts of this feature will begin today, and may take five or more business days to be completed across all Google Cloud zones. You may not be able to view or use this feature until the rollout is complete.

## December 09, 2025

Feature

**New add-on management page in API hub**

A new **Add-on Management** page is now available in API hub. This page serves as a centralized location to enable, configure, and manage all your add-on services.

For more information, see [Manage add-ons](https://docs.cloud.google.com/apigee/docs/apihub/manage-add-ons).

Change

**Actions tab changes**

The **Actions** tab previously located in the **API hub > Settings** page is now removed, accounting for the following UI changes:

  * You can now find and configure add-on services like Specification Linter and Semantic Search under the new unified [Add-on Management](https://docs.cloud.google.com/apigee/docs/apihub/manage-add-ons) page, alongside other API hub add-ons.
  * The deprovisioning function is now moved to a dedicated top-level tab called **Deprovision**.



## November 18, 2025

Feature

**New API deployments view**

API deployment information is now available as a separate tab in the **API details** page. You can view your API deployment details, create new deployments, and manage existing deployments using the API deployments tab.

For more information, see [Manage deployments](https://docs.cloud.google.com/apigee/docs/apihub/manage-api-deployments).

Fixed

The issue relating to API hub provisioning failures in data residency enabled Apigee organizations is now resolved. You can now provision API hub within an Apigee organization that has data residency enabled.

For information about provisioning API hub, see [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision).

Change

**New tutorial: Ingest Microsoft Azure API data into API hub**

A new tutorial is available for ingesting Microsoft Azure API data into API hub.

This tutorial shows you how to ingest API metadata from Azure API Management (APIM) into Apigee API hub. It uses a pre-built Application Integration template and a set of custom scripts on GitHub to perform a manual, on-demand ingestion of your API data.

For more information, see [Ingest Microsoft Azure API data into API hub](https://docs.cloud.google.com/apigee/docs/apihub/tutorials/ingest-azure-api-hub).

## November 04, 2025

Feature

**Filter APIs by user-defined attributes**

You can now filter APIs using your custom, user-defined attributes from the **APIs** page in the Google Cloud console.

For more information, see [Filter resources based on attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources).

## November 03, 2025

Issue

**API hub provisioning fails in data residency enabled Apigee organizations**

Currently, API hub can't be provisioned within an Apigee organization that has data residency enabled. Attempts to provision API hub in a data residency-enabled Apigee organization will result in a timeout error.

**Workaround:** There is no workaround available at this time. If your existing Apigee organization has data residency enabled, you will not be able to provision API hub until this limitation is resolved in a future release.

## October 28, 2025

Feature

**Detailed API resource insights**

A new **Insights** tab is now available on the API details page, providing API-centric analytics to help you understand usage patterns and performance for each of your APIs.

You can now analyze key metrics such as total traffic, average TPS, request/response latencies, and more, directly from the API details page.

For more information, see [View API resource insights](https://cloud.google.com/apigee/docs/apihub/view-api-resource-insights).

Feature

**API insights in API hub**

API insights is now available in API hub, providing a unified view of your API traffic and performance across all connected gateways. With API insights, you can gain a holistic understanding of your API ecosystem's health and quickly identify areas for optimization.

Currently, API insights supports data sources from Apigee, Apigee hybrid, Apigee Edge Public Cloud, and Apigee Edge Private Cloud (OPDK).

**Note:** Data residency (DRZ) and VPC-SC are not supported with API insights at this time.

For more information, see [API insights overview](https://cloud.google.com/apigee/docs/apihub/api-insights-overview).

## October 16, 2025

Change

**Create and manage API operations in the UI**

You can now create and manage API operations for your API versions from the **API details** page in the Google Cloud console.

For more information, see [Manage operations](https://cloud.google.com/apigee/docs/apihub/manage-operations).

## October 14, 2025

Change

**New MCP API style system attribute**

The system-defined API style attribute now includes a new value: **MCP**. This lets you classify and govern APIs based on the latest Model Context Protocol (MCP) standards.

For more information, see [System attributes](https://cloud.google.com/apigee/docs/apihub/manage-attributes#system-attributes).

## September 11, 2025

Change

**API hub navigation update**

The **API hub** section is now moved to the top level of the Apigee left navigation menu. This change improves discoverability and access to the API hub features.

Libraries

Updated Go client library. For more information, see [apihub: v0.2.0](https://github.com/googleapis/google-cloud-go/releases/tag/apihub/v0.2.0).

## September 08, 2025

Feature

**Enable and disable semantic search**

You can now enable and disable semantic search from the **API hub > Settings> Actions** page in the Google Cloud console.

For more information, see [Enable and disable semantic search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis#enable-semantic-search).

Deprecated

**Deprecation of Vertex AI Extensions in API hub**

The Vertex AI Extensions feature is no longer supported in API hub as of **September 8, 2025**.

Change

**Automatic discovery of OpenAPI Spec from Apigee proxy resources**

API hub now automatically discovers and ingests valid OpenAPI specifications when they are included in an Apigee API proxy resource. This applies to all new and existing Apigee and Apigee hybrid runtime projects that are attached in API hub.

For more information, see [Auto-discovery of OpenAPI specs from Apigee proxies](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#auto-oas-discovery).

## September 01, 2025

Change

**New API versions view**

API version information is now available as a separate tab in the **API details** page. You can view your API version details, copy API ID, create new API versions and more using the API versions tab.

For more information, see [Manage versions](https://docs.cloud.google.com/apigee/docs/apihub/manage-versions).

## August 22, 2025

Feature

**Deprovision API hub in the UI**

You can now deprovision an API hub instance from the **API hub > Settings > Actions** page in the Google Cloud console.

For more information, see [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision).

Feature

**Create and delete custom plugins in the UI**

You can now create and delete custom plugins from the **API hub > Settings > Plugins** page in the Google Cloud console.

For more information, see [Create custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/create-custom-plugins) and [Manage custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-custom-plugins).

## August 12, 2025

Feature

**API observations in API hub ([Preview](https://cloud.google.com/products#product-launch-stages))**

API observations in API hub helps you tackle the challenges of undocumented and unmanaged APIs in your API infrastructure. It leverages Apigee [shadow API discovery](https://docs.cloud.google.com/apigee/docs/api-observation/shadow-api-discovery) and uses automated discovery processes to bring all your APIs, **across Google Cloud projects** , into a unified, managed view. 

For more information, see [API observations in API hub](https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview).

**Note:** Rollouts of this feature will begin today, and may take five or more business days to be completed across all Google Cloud zones. You may not be able to view or use API observations until the rollout is complete. 

## July 31, 2025

Feature

**New data source support for plugins**

API hub now supports importing API metadata through new dedicated plugins for the following data sources:

  1. [Apigee Edge Public Cloud](https://docs.apigee.com/api-platform/get-started/apigee-edge-uapim)
  2. [Apigee Edge Private Cloud (OPDK)](https://docs.apigee.com/private-cloud/v4.53.00/privatecloud-uapim-overview)



For more information, see [Plugins overview](https://docs.cloud.google.com/apigee/docs/apihub/plugins).

Feature

**Create custom plugins [API only]**

You can now use the `Create Plugin` API to create custom plugins in API hub. Custom plugins are created manually to connect API hub to a specific API data source. 

For more information, see [Create custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/create-custom-plugins).

Feature

**Push-based plugin ingestion**

API hub now supports push-based plugin ingestion. This method allows for more real-time synchronization of API metadata. All new **Apigee, Apigee hybrid, Apigee Edge Public Cloud, and Apigee Edge Private Cloud (OPDK)** plugins are created with push-based ingestion by default.

For more information, see [Plugin data ingestion methods](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods).

**Note:** Rollouts of this feature will begin today, and may take five or more business days to be completed across all Google Cloud zones. You may not be able to create push-based plugins until the rollout is complete. 

Issue

**Default Apigee plugin instance not auto-created during runtime attachment**

**Issue:** When provisioning API hub as part of Apigee provisioning, the default `Apigee X and hybrid` plugin instance is not automatically created. This prevents API proxies from being auto-registered.

**Workaround:** You can manually attach an Apigee runtime instance and import the Apigee assets. See [Attach a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project).

Change

**New tutorial: Enrich API data in API hub**

A new tutorial is available for enriching API data in Apigee API hub.

It shows you how to use API hub's custom curation features to automatically fetch OpenAPI specifications from a Cloud Storage bucket and associate them with their corresponding Apigee API proxies. The custom curation logic is defined using an integration in Application Integration.

For more information, see [Enrich API data with custom curation in API hub](https://docs.cloud.google.com/apigee/docs/apihub/tutorials/enrich-api-data).

Change

**Provisioning changes and Apigee API proxy registration**

API hub changed how it registers API proxies from Apigee and how it creates default plugin instances during provisioning.

API hub now automatically creates a default `Apigee X and hybrid` plugin instance and auto-registers API proxies only when you provision it as part of Apigee provisioning. 

If you provision API hub directly from the API hub UI, API hub does not automatically create a default plugin instance, nor does it auto-register proxies.

For more information, see [Project attachments and plugins](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#project-associations-and-plugins).

Change

**Delete plugin instance changes**

API hub no longer retains any ingested metadata from a plugin after its deletion. Deleting a plugin instance also permanently deletes all the associated API data from API hub.

For more information, see [Delete a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances#delete-plugin-instance).

Deprecated

**Deprecation of pull-based ingestion for Apigee plugins**

[Pull-based ingestion](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods) is no longer supported for `Apigee and Apigee hybrid` plugins as of **July 31, 2025**. For existing projects that have pull-based Apigee X and hybrid plugins configured, these plugins will continue to function and will be automatically migrated to the push-based type starting **August 2025**.

Deprecated

**Deprecation of Apigee proxy deployment attributes**

As of **July 31st, 2025** , the `Apigee X and Hybrid Environment` and `Apigee X and Hybrid Organization` attributes will no longer be added to new Apigee proxy deployments. This change specifically applies when you import deployments into API hub by attaching a runtime project.

If your existing projects use these attributes in filtered search queries, we recommend updating them. To ensure your searches continue to work, use the `Source project` and `Source environment` fields as alternatives.

## July 22, 2025

Change

**API hub deprovisioning changes**

Deprovisioning an API hub instance now also deletes any associated Apigee organizations from your Google Cloud project, provided those Apigee organizations have no Apigee instances.

If you deprovision an API hub instance, you can reprovision it later, but you'll need to wait 7 days before you can do so.

For more information, see [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision).

Change

**VPC Service Controls (VPC-SC) is GA**

VPC Service Controls in API hub is now [GA](https://cloud.google.com/products#product-launch-stages).

For more information, see [VPC Service Controls for API hub](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control).

Change

**API hub provisioning now enables Apigee API**

When you provision API hub, it now enables the Apigee API (`apigee.googleapis.com`) in your Google Cloud project. If Apigee isn't already provisioned, an Apigee organization is also automatically created in your project as part of the provisioning process.

API hub remains a free service. Enabling the Apigee API has no additional pricing or billing implications for your project.

For more information, see [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision).

## July 18, 2025

Feature

**Apigee and hybrid plugin instance management**

You can now create and delete plugin instances for Apigee and Apigee Hybrid while associating the respective Apigee runtime projects to API hub.

For more information, see [Auto-register Apigee proxies](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies).

Breaking

**Apigee and Apigee hybrid plugin creation now requires source project ID**

When creating new instances of the **Apigee X and hybrid** plugin, you must now provide a source project ID. This source project ID is the Google Cloud project from which the plugin will import data. 

This is a breaking change and will affect any existing API calls that create these plugins without explicitly providing this ID.

**Action Required:** Update your API calls to include the appropriate source project ID when creating new Apigee X and hybrid plugins. Failing to do so will result in creation errors.

Change

**Edit plugin instances changes**

You can now change or modify the name and curation logic of your plugin instance.

For more information, see [Edit a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances#edit-plugin-instance).

Change

**Resource URI format for Apigee deployments**

To ensure optimal functionality and consistency while creating or updating **Apigee** deployments, we now recommend that the **Resource URI** conforms to the following format: `organizations/([^/]+)/environments/([^/]+)/apis/([^/]+)$`

For more information, see [Introduction to deployments](https://docs.cloud.google.com/apigee/docs/apihub/deployments-intro).

## June 03, 2025

Feature

**Apigee API hub is enabled for new Apigee organizations in supported regions.**

With this release, we are enabling [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) for new Apigee organizations [in regions where API hub is supported](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions). All new Apigee organizations, including hybrid organizations, that select an API hub-supported region _for their Apigee Analytics region_ during provisioning will have access to API hub features at no additional cost. 

API hub allows you to view, organize, and manage all of the APIs in your Apigee organization in one central location. To learn more, see [What is Apigee API hub?](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub)

No action on your part is required to provision API hub for your organization, with the following exceptions:

  * If your Apigee organization has Data Residency or VPC Service Controls enabled, you must configure your API hub instance manually to support these services. See [VPC Service Controls for API hub](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control) and [API hub and data residency](https://docs.cloud.google.com/apigee/docs/apihub/locations#drz-api-hub) for more information.
  * If your Apigee organization uses Customer-Managed Encryption Keys (CMEK), you must deprovision the Apigee API hub instance provided by default and recreate it to support CMEK. See [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision) and [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision) for step-by-step instructions.



Contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) for questions or assistance.

Announcement

On June 3, 2025, we released an updated version of Apigee.

## May 21, 2025

Announcement

Apigee API hub is now available in the following regions:

  * europe-west10 (Berlin)
  * us-east5 (Columbus)
  * us-south1 (Dallas)
  * me-central2 (Dammam)
  * asia-south2 (Delhi)
  * me-central1 (Doha)
  * europe-north1 (Finland)
  * europe-west3 (Frankfurt)
  * asia-east2 (Hong Kong)
  * asia-southeast2 (Jakarta)
  * africa-south1 (Johannesburg)
  * us-west4 (Las Vegas)
  * us-west2 (Los Angeles)
  * europe-southwest1 (Madrid)
  * australia-southeast2 (Melbourne)
  * europe-west8 (Milan)
  * northamerica-northeast1 (Montréal)
  * europe-west4 (Netherlands)
  * asia-northeast2 (Osaka)
  * us-west3 (Salt Lake City)
  * southamerica-west1 (Santiago)
  * asia-northeast3 (Seoul)
  * us-east1 (South Carolina)
  * asia-east1 (Taiwan)
  * me-west1 (Tel Aviv)
  * asia-northeast1 (Tokyo)
  * northamerica-northeast2 (Toronto)
  * europe-west12 (Turin)
  * europe-central2 (Warsaw)
  * europe-west6 (Zürich)



For more information, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations).

## May 16, 2025

Feature

**API overview and metrics**

The **Get Started with API hub** page now includes new charts and scorecards to provide a quick overview of your API landscape.

For more information see [Get started with API hub](https://docs.cloud.google.com/apigee/docs/apihub/getting-started-apihub#view-your-api-landscape-overview).

Change

**Attach and manage Tags**

You can now add custom tags to your APIs and API deployments, making it easier to organize, categorize, and discover your API resources in API hub. Tags can also be used to conditionally allow or deny policies to a specific resource.

For more information see [Attach and manage tags](https://docs.cloud.google.com/apigee/docs/apihub/attach-manage-tags).

Change

**Updated UI for API hub**

The API hub user interface is now updated to Google Material Design 2. This update provides a more consistent and modern look and feel, enhancing the overall user experience and aligning the UI with other Google Cloud products.

## April 29, 2025

Announcement

On April 29, 2025, we released an updated version of Apigee.

Feature

**Apigee API hub is enabled for existing Apigee organizations in supported regions.**

With this release, we are enabling [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) for existing Apigee organizations [in regions where API hub is supported](https://docs.cloud.google.com/apigee/docs/apihub/locations#supported-locations). All existing Apigee organizations, including hybrid organizations, that selected an API hub-supported region _for their Apigee Analytics region_ will have access to API hub features at no additional cost. 

API hub allows you to view, organize, and manage all of the APIs in your Apigee organization in one central location. To learn more, see [What is Apigee API hub?](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub)

The process of enabling API hub for these organizations will continue over the next several weeks until all eligible organizations are updated. No action on your part is required to provision API hub for your organization, with the following exceptions:

  * If your Apigee organization has Data Residency or VPC Service Controls enabled, you must configure your API hub instance manually to support these services. See [VPC Service Controls for API hub](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control) and [API hub and data residency](https://docs.cloud.google.com/apigee/docs/apihub/locations#drz-api-hub) for more information.
  * If your Apigee organization uses Customer-Managed Encryption Keys (CMEK), you must deprovision the Apigee API hub instance provided by default and recreate it to support CMEK. See [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision) and [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision) for step-by-step instructions.



Contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) for questions or assistance.

## April 02, 2025

Feature

**Data residency zone compliance**

API hub is now compliant with data residency Zone C3 requirements. 

**Note:** While API hub is data residency compliant as a standalone service, the automated provisioning of API hub for an Apigee organization that has data residency enabled is **not** currently supported.

For more information, see [API hub and data residency](https://docs.cloud.google.com/apigee/docs/apihub/locations).

Feature

**VPC Service Controls (VPC-SC) integration** ([Preview](https://cloud.google.com/products#product-launch-stages))

API hub now integrates with VPC Service Controls, providing enhanced network security for your API hub instance provisioned in Google Cloud. Establish service perimeters to control ingress and egress traffic. For more information, see [VPC Service Controls for API hub](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control).

Feature

**Terraform support for provisioning**

You can now provision API hub instances programmatically using Terraform for Google Cloud within Cloud Shell, enabling infrastructure-as-code practices. For more information, see [Provision API hub using Terraform](https://docs.cloud.google.com/apigee/docs/apihub/provision-terraform).

Feature

**Plugin Framework**

API hub now uses a plugin framework to connect and ingest API metadata from various Google Cloud services and external sources where your APIs are managed or defined. This provides a flexible and extensible way to integrate with your existing API landscape. For more information, see [Plugins overview](https://docs.cloud.google.com/apigee/docs/apihub/plugins).

Feature

**Enhancements to the Operations entity [API only]**

You can now add, edit, or delete operations for an API version even if it lacks a specification file or has an unparsable one. For more information, see [Manage operations](https://docs.cloud.google.com/apigee/docs/apihub/manage-operations).

Feature

**API Metadata Curations**

API hub introduces a curation process to transform and enrich API metadata ingested by plugins. This ensures consistency across different sources, enabling effective governance, discovery, and management of your APIs. For more information, see [Curations overview](https://docs.cloud.google.com/apigee/docs/apihub/curations).

Feature

**API Supply chain graph view**

Visualize and understand the dependencies within your API ecosystem with the new interactive API supply chain graph view. This directed graph allows you to explore the relationships between your APIs and API operations. For more information, see [API Supply chain views](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-views).

Feature

**Deprovision an API hub instance [API only]**

You can now delete an API hub instance from your Google Cloud project using the [ApiHubInstance](https://docs.cloud.google.com/apigee/docs/reference/apis/apihub/rest/v1/projects.locations.apiHubInstances) API. For more information, see [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision).

Change

**Attach API documents**

You can now enhance your API documentation by attaching additional relevant files, such as requirements, design documents, and functionality details, directly to your APIs in API hub.

## February 11, 2025

Feature

**IAM conditions for fine-grained access**

API hub now integrates with IAM Conditions, enabling you to define and enforce granular, conditional attribute-based access control for your API hub resources. For more information, see [Add IAM conditions](https://docs.cloud.google.com/apigee/docs/apihub/add-iam-conditions).

Change

**Enhanced onboarding experience**

After provisioning your API hub instance in your Google Cloud project, you'll now see an updated **Overview** page. You can also automatically attach your Apigee runtime projects right from this page. For more information, see [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision).

Change

**Auth support for Vertex AI extensions**

API hub now supports the following authentication configurations for creating Vertex AI extensions:

  * `API Key`: Authenticate using API keys stored in Secret Manager.
  * `HTTP Basic`: Authenticate using credentials stored in Secret Manager.



For more information, see [Create a Vertex AI extension](https://docs.cloud.google.com/apigee/docs/apihub/vertex-extensions#createextension).

Change

**Resource ID length limits increased**

The maximum allowed length for API hub resource IDs has been increased. The new limits are as follows:

  * **APIs:** API unique IDs can now be up to 500 characters long.
  * **Versions:** Version unique IDs can now be up to 700 characters long.
  * **Specs:** Specification unique IDs can now be up to 1000 characters long.



## January 15, 2025

Feature

**Resource filtering with user-Defined attributes**

You can now filter API hub resources based on user-defined attributes using a REST API call. For more information, see [Filter resources based on user attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources-based-on-user-attributes).

Change

**Validation for user-defined attributes**

API hub now supports JSON schema validation for user-defined attributes. This enhancement ensures data integrity and consistency for JSON data type inputs, improving the quality and reliability of API specifications.

## October 18, 2024

Feature

In addition to `us-central1` and `europe-west1`, Apigee API hub now supports the following new hosting regions:

Region Description | Region name  
---|---  
Northern Virginia | `us-east4`  
Oregon | `us-west1`  
London | `europe-west2`  
Singapore | `asia-southeast1`  
Mumbai | `asia-south`  
Sao Paulo | `southamerica-east1`  
Sydney | `australia-southeast1`  
  
See [Provision API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision).

Announcement

On October 18, 2024, Apigee announced the an update to Apigee API hub.

## September 26, 2024

Announcement

On September 26, 2024, Apigee announced the GA launch of Apigee API hub.

Feature

A new "Get started with API hub" page was added to the user interface. This new page includes valuable getting started information, including a new FAQ, to help you get the most out of API hub.

Feature

We added a new Supply chain page where you can create, view and manage your dependencies across API operations. The same dependencies can also be created from the API operations page. See [Manage dependencies](https://docs.cloud.google.com/apigee/docs/apihub/manage-dependencies).

Feature

We added support for GMEK and CMEK in the provisioning steps. While provisioning, you can also choose to host your Vertex search data in a different location or disable Vertex search altogether. See [Provision API hub](https://docs.cloud.google.com/apigee/docs/apihub/provision).

Feature

The Semantic Search (formerly Smart Search) user interface has been improved, and search results are shown across all API hub entities, such as APIs, deployments, specifications, and versions. See [Search and filter APIs](https://docs.cloud.google.com/apigee/docs/apihub/search-apis).

Feature

The List APIs for specifications, dependencies, and external APIs have been enhanced to return a complete response, including user-defined attributes.

Feature

We added support for [Cloud audit logging](https://docs.cloud.google.com/apigee/docs/apihub/audit-logging-apihub).

Feature

While you can use API hub by making direct REST over HTTP requests, we now provide client libraries for several popular languages. See [API hub client libraries](https://docs.cloud.google.com/apigee/docs/apihub/libraries).

Feature

Significant user interface improvements were made, such as standardization of cards on the API details page, unlinking of deployments, various performance fixes, and more.

## August 23, 2024

Announcement

On August 23, 2024, we updated the Preview release of Apigee API hub.

Feature

All API proxy endpoints auto-registered from Apigee will be prefixed with `https://` by default. Endpoints for existing API proxies that were added to API hub will be updated.

Feature

You can now choose in the Cloud console to restrict the upload of an API specification file that contains errors. By default, specs containing errors are uploaded. See [Add a spec to an existing version](https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications#addtoexistingversion).

Feature

User interface and performance improvements were made.

Feature

A validation check has been added to reject an API specification style guide upload if the style guide's `extends` property contains a URL. See [Upload a new style guide](https://docs.cloud.google.com/apigee/docs/apihub/validate-spec#upload-a-new-style-guide).

Feature

When an Apigee API proxy is auto-registered, its deployment type is now labeled either Apigee X or Apigee hybrid. Existing Apigee proxy deployments registered with API hub will also be labeled with the appropriate type. See [Auto-register Apigee proxies](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies).

Feature

You can now edit an uploaded API specification's metadata through the Cloud console. See [Edit specification metadata](https://docs.cloud.google.com/apigee/docs/apihub/manage-specifications#editspecification).

Fixed

Provisioning improvements were made to address potential failures.

## June 11, 2024

Feature

**Vertex AI extensions**

You can create [Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/overview) extensions for the APIs registered in API hub. These extensions can be integrated with Large Language Models (LLMs) to process real-time data. For more information, see [Create a Vertex AI extension](https://docs.cloud.google.com/apigee/docs/apihub/vertex-extensions#createextension).

Feature

**Eventarc triggers**

API hub is integrated with Google Cloud's [Eventarc](https://docs.cloud.google.com/eventarc/docs). You can now create Eventarc triggers to listen for specific events in API hub, and then trigger custom workflows based on the event. For more information, see [Create an Eventarc trigger](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-create-event-triggers).

Feature

**Multi-level delete**

By default, you can delete an API only if all underlying versions are deleted. Starting with this release, you can use the _force_ option to delete an API and its child resources in a single step. For more information, see [Delete an API resource](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis#deleteapi).

## May 06, 2024

Announcement

Apigee API hub is available in [preview](https://cloud.google.com/products#product-launch-stages).

With Apigee API hub, you can consolidate and organize critical information about your APIs in one place. Use API hub to accelerate the consistency, use, reuse, and governance of your API portfolio.

Use API hub to:

  * Create and manage a complete catalog of your APIs and API resources.
  * Add rich attributes to your APIs for tracking, organizing, and filtering.
  * Link to one or more Apigee projects to automatically fetch and store Apigee API proxy information.
  * Find APIs with powerful free-form semantic search capabilities.
  * Track compliance for your API specification files using Linting functionality.



To learn more about the features and functionality available, see [What is Apigee API hub?](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub)

**NOTE** : Rollouts of this feature will begin on May 6, 2024, and may take four or more business days to be completed across all Google Cloud zones. You may not be able to provision API hub until the rollout is complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
