---
url: https://docs.cloud.google.com/looker/docs/new-explore-experience-overview/
title: The new Looker Explore and Merge Query experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:29.837790+00:00
---

# The new Looker Explore and Merge Query experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/new-explore-experience-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  The new Looker Explore and Merge Query experience Stay organized with collections  Save and categorize content based on your preferences. 

The [**New Looker Explore and Merge Query Experience** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#new-looker-explore-and-merge-query-experience) lets individual users have the option to try the redesigned Looker Explore and Merge Query interfaces. The streamlined interfaces make the Explore experience more intuitive and let Looker users find connections and gain insights from their data more quickly.

This page presents the following topics, which guide you through the new Explore experience:

  * User and instance requirements
  * Enabling the new Explore and Merge Query experience
  * Finding Explores in Looker
  * Accessing the new Explore experience
  * Supported visualization types
  * List of documentation



## User and instance requirements

To enable and use the [**New Looker Explore and Merge Query Experience** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#new-looker-explore-and-merge-query-experience), the following requirements must be met:

  * Your Looker (original) or Looker (Google Cloud core) instance must be running Looker 26.6 or later, and your Looker (original) instance must be [Looker-hosted](https://docs.cloud.google.com/looker/docs/glossary#looker-hosted).
  * You must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) to enable the **New Looker Explore and Merge Query Experience** preview feature.
  * To view, create, or edit Explores, including Explore visualizations and merging queries, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or another role that contains the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission.
  * To access [Explore features for developers](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#features-for-developers), which includes the ability to see LookML information about fields, you must have the **User** [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#user) or another role that contains either the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission or the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) permission.



## Enabling the new Explore and Merge Query experience

The [**New Looker Explore and Merge Query Experience** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#new-looker-explore-and-merge-query-experience) is enabled by default.

Admins can disable or enable the **New Looker Explore and Merge Query Experience** preview feature by following these steps:

  1. In Looker, click the **Admin** option in the [main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu).
  2. Click the **Preview** option under the **General** section to open the [**Preview Features** page](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features).
  3. Adjust the **New Looker Explore and Merge Query Experience** switch to disable or enable the preview feature.

**Tip:** For an AI-assisted experience, enable additional options on the [**Gemini in Looker**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) page in the **Platform** section of the **Admin** panel.

## Finding Explores in Looker

You can find prebuilt Explore queries in Looker in several ways, including the following:

  * Click the **Explore from Here** link while editing [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#editing_a_looks_source_query) or [dashboard tiles](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles).
  * Click the **Explore from Here** link on [Alerts](https://docs.cloud.google.com/looker/docs/alerts-overview) and [scheduled deliveries](https://docs.cloud.google.com/looker/docs/scheduling).
  * Follow links that are [shared by other users](https://docs.cloud.google.com/looker/docs/sharing-urls).
  * Use [Quick Start analyses](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience#quick_start) or [Insight Assistant](https://docs.cloud.google.com/looker/docs/gemini-insight-asst) as a starting point in a blank Explore.
  * [Upload a CSV file, an XLS file, or an XLSX file](https://docs.cloud.google.com/looker/docs/exploring-self-service#uploading_data_to_create_a_self-service_explore). You can also use the explore **Explore** section in the [main navigation panel](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu) to open a blank Explore.



## Accessing the new Explore experience

To access the new Explore experience, the [**New Looker Explore and Merge Query Experience** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) must be enabled for your instance. If you are not a Looker admin, ask an admin to enable the feature.

From an Explore page, click **Try the new Explore** to turn on the new Explore experience for all Explores that you interact with. To switch back to the classic experience, click **Switch to classic Explore**.

## Supported visualization types

The new Explore experience only supports the following [visualization types](https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience):

  * Bar charts
  * Column charts
  * Line charts
  * Single value charts
  * Table charts



If you select an unsupported chart type, the visualization will render the Explore data, but there will be no configuration options available in the **Style** tab.

## List of documentation

The following pages provide an overview of the new Explore and Merge Query experience:

  * [Viewing and interacting with Explores in the new Explore experience](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-new-explore-experience): Learn how to view, discover, and share insights in Explore queries.
  * [Creating and editing Explores in the new Explore experience](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience): Learn to build queries, display results, use features for developers, and discover insights in Looker.
  * [Filtering and limiting data in the new Explore experience](https://docs.cloud.google.com/looker/docs/filtering-and-limiting-new-explore-experience): Limit your results to the data you're interested in.
  * [Joining data from multiple queries in the new Explore experience](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore): Learn how to join queries from multiple Explores and edit merge query tiles directly in the dashboard edit canvas.
  * [Configuring and editing visualizations in the new Explore experience](https://docs.cloud.google.com/looker/docs/editing-visualizations-new-explore-experience): Create visualizations and graphs based on the results of your queries.
  * [Using the Gemini Insight Assistant](https://docs.cloud.google.com/looker/docs/gemini-insight-asst): Ask questions to gain insights into an Explore, and then use the results to build or modify the Explore.
  * [Using Gemini in Looker to generate Quick Start analyses](https://docs.cloud.google.com/looker/docs/gemini-quick-starts): Populate Explores with fields, filters, and sorts instantly to significantly reduce time-to-insight.
  * [Using the Expression Assistant](https://docs.cloud.google.com/looker/docs/gemini-expression-asst): Use Gemini in Looker guidance to write expressions for [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) and [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
