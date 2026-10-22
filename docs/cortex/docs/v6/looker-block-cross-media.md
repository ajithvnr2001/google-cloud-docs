---
url: https://docs.cloud.google.com/cortex/docs/v6/looker-block-cross-media/
title: Looker Block for Cross Media & Product Connected Insights \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:25.572853+00:00
---

# Looker Block for Cross Media & Product Connected Insights  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/looker-block-cross-media/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Looker Block for Cross Media & Product Connected Insights

This page describes the insights you can get from the Cortex Looker Block for Cross Media & Product Connected Insights. With this Looker Block you can get a comprehensive view of your campaign spend and performance by combining your campaign data from multiple paid media platforms including Google Ads, Meta, TikTok and YouTube (with DV360) into BigQuery with pre-packaged ingestion pipelines and reporting views provided by [Google Cloud Cortex Framework for Marketing](https://docs.cloud.google.com/cortex/docs/v6/overview).

This pipeline also includes an option to use a Gemini text generation model on Vertex AI to match textual representations of media campaigns with a single product hierarchy node. For example, a campaign named _"BMX - Reels - Reach"_ matches the product hierarchy node `['Fitness & Sports', 'Bicycles', 'Special Bikes','BMX Bikes']`.

See a high level breakdown of volume of impressions and clicks from each platform for campaigns relating to specific product category and product.

## Available insights

The Looker Block for Cross Media & Product Connected Insights in Cortex Framework offers the following insights.

## Overall campaign performance

Overview of high-level performance and engagement metrics including:

  * Total impressions
  * Total clicks
  * Click through rate (CTR)
  * Total Spend
  * Cost per Mille (CPM)
  * Cost per click (CPC)



### Media platform performance and spend by month

  * Spend by month and media platform
  * Cumulative monthly spend in total and by media platform



### Campaign performance

  * Campaigns in chronological view
  * Impressions, clicks, click through rate and cost per mille by media platform, campaign, and country
  * Detailed performance by campaign and country



## Required Data

Get the required BigQuery datasets for this block by following the installation instructions for [Cortex Framework](https://github.com/GoogleCloudPlatform/cortex-data-foundation).

## Repository

To access the Cortex Looker Block for Cross Media & Product Connected Insights, visit its official GitHub repository: [**block-cortex-cross-media**](https://github.com/looker-open-source/block-cortex-cross-media). This repository contains essential views, Explores and dashboards that enable you to seamlessly integrate data into your Looker environment. These resources provide a solid foundation for creating custom reports, visualizations, and dashboards tailored to your specific needs.

## Deployment

For instructions about how to deploy the Cortex Looker Block for Cross Media & Product Connected Insights, see [Deploy Looker Blocks for Cortex Framework](https://docs.cloud.google.com/cortex/docs/v6/looker-block-deployment).

### Other Considerations

For optimizing the performance and functionality of your Looker Block for Cross Media & Product Connected Insights consider the following:

  * **Liquid Templating Language** : Some constants, views, Explores and dashboards use liquid templating language. For more information, see Looker's [Liquid Variable Reference](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) documentation.
  * **Unhide additional dimensions and measures** : Many dimensions and measures are hidden for simplicity. If you find anything valuable missing, set field's `hidden` parameter value to `No` in the relevant views.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
