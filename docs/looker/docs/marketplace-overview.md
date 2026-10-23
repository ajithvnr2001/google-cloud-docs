---
url: https://docs.cloud.google.com/looker/docs/marketplace-overview/
title: Looker Marketplace overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:34.670438+00:00
---

# Looker Marketplace overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/marketplace-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker Marketplace overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Looker Marketplace contents are not officially supported Google products.

The Looker Marketplace is a central location for finding, deploying, and managing [Looker Blocks](https://docs.cloud.google.com/looker/docs/glossary#block), [applications](https://docs.cloud.google.com/looker/docs/glossary#extension), [custom visualizations](https://docs.cloud.google.com/looker/docs/glossary#visualization), and [actions](https://docs.cloud.google.com/looker/docs/glossary#action-hub).

You can browse content on the Looker Marketplace from the following locations:

  * From the standalone Looker Marketplace instance at `marketplace.looker.com`
  * From the **Marketplace** storefront icon in the menu bar of your Looker instance



The Marketplace homepage shows popular Looker applications, models, and visualizations. This documentation page describes the different types of content that you can install from the Looker Marketplace.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-marketplace-2314.png)

The terminology of Looker Marketplace content differs between the two locations. See the following table for an overview of the different terms.

[marketplace.looker.com](http://marketplace.looker.com/) | Looker instance Marketplace | Description  
---|---|---  
Applications | Applications | Applications, also referred to as ["extensions"](https://docs.cloud.google.com/looker/docs/glossary#extension) throughout the documentation, are built with Looker components that are developed through the [Looker extension framework](https://docs.cloud.google.com/looker/docs/glossary#looker-extension-framework).  
Blocks | Models | Models, also referred to as ["Blocks"](https://docs.cloud.google.com/looker/docs/glossary#block) throughout the documentation, are prebuilt LookML models, including dashboards and Explores, for a variety of popular data sources.  
Plug-ins | Visualizations | Plug-ins are visualization types that you can install and add to Looker's built-in visualization library.  
  
No permissions are needed to browse content on the standalone Marketplace instance; however, you won't be able to install Marketplace content for use with your Looker instance. See the [Using the Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace#marketplace-permissions) documentation page for more information on the permissions that are required to install and use content from the Looker Marketplace.

## Limitations of the Looker Marketplace

Looker (Google Cloud core) instances that use [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa) connections don't support Marketplace. Looker (Google Cloud core) instances that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) connections can [connect to the Marketplace](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#connect-to-marketplace) through the Google Cloud console.

Customer-hosted Looker instances may require additional configuration to access Marketplace data:

  * If your instance is on Looker 23.10 or later, the server that is running the Looker instance must be configured to access the public internet server that is running at the URL `https://static-a.cdn.looker.app/`.
  * If your instance is on Looker 23.8 or earlier, the server that is running the Looker instance must be configured to access the public internet server that is running at the URL `https://marketplace-api.looker.com/`.
  * The server that is running the Looker instance must also be configured to access the public internet server that is running at the URL `https://github.com/`.



Additionally, customer-hosted deployments that are using clustered instances must set up a [shared (network) file system](https://docs.cloud.google.com/looker/docs/clustering-looker#shared_file_system) to install applications or tools from the Looker Marketplace.

## Marketplace content

From the Looker Marketplace, you can install and use the following types of content:

  * Looker Blocks
  * Visualizations
  * Applications
  * Actions



### Blocks

[Looker Blocks](https://docs.cloud.google.com/looker/docs/blocks) are prebuilt pieces of LookML that Looker customers can use as a starting point for quick and flexible data modeling. Blocks are designed to be plug-and-play, as long as you have the appropriate dataset in an existing Looker connection. You can [install a block](https://docs.cloud.google.com/looker/docs/marketplace) from the Marketplace, customize the LookML, and begin exploring.

#### Examples

Filter the [Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory?Type=tools) **Type** drop-down to **Blocks** to see available Blocks, such as:

  * [Google Analytics 360](https://marketplace.looker.com/marketplace/detail/ga360-v2) block: Understand how your users are engaging with your product or webpage
  * [Salesforce Analytics](https://marketplace.looker.com/marketplace/detail/salesforce-v2) block: Understand performance, prioritize opportunities, and close more deals
  * [BigQuery Information Schema Performance Monitoring](https://marketplace.looker.com/marketplace/detail/bigquery-information-schema) block: Monitor and Explore your BigQuery usage and performance



#### Getting started with Looker Marketplace Blocks

To use a Looker Block, follow these steps:

  1. [Install the Block from the Looker Marketplace into your Looker instance](https://docs.cloud.google.com/looker/docs/marketplace).
  2. [Customize the Block as needed](https://docs.cloud.google.com/looker/docs/marketplace-customize-blocks).



### Visualizations

Plug-ins are visualization types that you can install and add to Looker's [built-in visualization library](https://docs.cloud.google.com/looker/docs/visualization-types).

#### Examples

Filter the [Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory) **Type** drop-down to **Plug-ins** to see available visualizations. For examples, see the following visualizations:

  * [Aster Plot visualization](https://marketplace.looker.com/marketplace/detail/viz-aster_plot)
  * [Force-Directed Graph](https://marketplace.looker.com/marketplace/detail/viz-forcedirected)
  * [Gauge visualization](https://marketplace.looker.com/marketplace/detail/viz-gauge)



### Getting started with Looker Marketplace visualizations

You can [install a visualization](https://docs.cloud.google.com/looker/docs/marketplace) from the Marketplace and immediately select the new visualization type when exploring, building a new dashboard, and editing a dashboard.

### Applications

Applications, also referred to as "extensions" throughout the documentation, are built with Looker components that are developed through the Looker [extension framework](https://docs.cloud.google.com/looker/docs/glossary#looker-extension-framework).

#### Examples

Filter the [Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory) **Type** drop-down to **Applications** to see available applications. For examples, see the following pages:

  * [API Explorer](https://marketplace.looker.com/marketplace/detail/extension-api-explorer) application
  * [Data Dictionary](https://marketplace.looker.com/marketplace/detail/extension-data-dictionary) application



### Getting started with Looker Marketplace applications

You can [install an application](https://docs.cloud.google.com/looker/docs/marketplace) from the Marketplace and immediately use it in your Looker instance. You can also build your own extensions by using the Looker [extension framework](https://docs.cloud.google.com/looker/docs/glossary#looker-extension-framework) to use in your Looker instance.

### Actions

Actions, also called "integrations", deliver Looker data to third-party services. Each instance's Looker Action Hub has built-in actions that Looker admins can enable on the **Actions** page in a Looker instance's **Admin** panel. See the [List of integrated services](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#list_of_integrated_services) for a list of the built-in actions.

You can also set up a custom action hub that serves custom actions. See the [Building a custom action](https://docs.cloud.google.com/looker/docs/action-hub#building_a_custom_action) page for detailed instructions and guidelines on creating custom actions.

Once a Looker admin [enables an action](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#enabling_and_disabling_actions) from either the Looker Action Hub or from a custom action hub, users can select the action when sending or scheduling data deliveries.

#### Examples

Your Looker instance has built-in actions that you can enable on the **Actions** page in your instance's **Admin** panel. You can also filter the [Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory?Type=tools) **Type** drop-down to **Actions** to see available actions. For examples, see the following pages:

  * [Airtable](https://discuss.google.dev/t/looker-actions-airtable/111778) action
  * [Azure Storage](https://discuss.google.dev/t/looker-actions-azure-storage/111500) action



#### Getting started with actions

Rather than by installing actions from the Marketplace, a Looker admin must [enable each action](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#enabling_and_disabling_actions) from either the Looker Action Hub or from a custom action hub. Once the action is enabled, users can select the action when sending or scheduling data deliveries.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
