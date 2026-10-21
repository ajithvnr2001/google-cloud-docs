---
url: https://docs.cloud.google.com/looker/docs/embed-reports/
title: Embed Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:26:07.444419+00:00
---

# Embed Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/embed-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Embed Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

Looker lets you embed Explores, reports, [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore) (saved visualized query results), and [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) (collections of tiles that show visualized query results) in any HTML-formatted web page, portal, or application. You can embed Looker reports with the private embed or signed embed methods. Like other Looker content, access to embedded reports is controlled by [access levels](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) and user permissions.

**Important:** Embedded reports are _view only_ and are supported only for Looker (original) instances. Reports can be edited only within the Looker application.

This page guides you through the methods and requirements of embedding reports. Read the following sections to learn about these concepts:

  * Things to know about embedding reports
  * Requirements and permissions
  * View embedded reports
  * Embed reports
  * Related resources



## Things to know about embedding reports

In addition to the requirements and permissions, which are described next, there are several things to know about embedding reports:

  * Embedding for reports is available only for [Looker-hosted](https://docs.cloud.google.com/looker/docs/choosing-hosting-option#looker-hosted-pros-cons) Looker (original) instances.
  * Embedded reports are _view only_. Reports can be edited only within the Looker application.
  * The permissions that can be implemented for reports that are embedded with the [signed embed method](https://docs.cloud.google.com/looker/docs/signed-embedding) are limited to content permissions (`access_data`, and `see_looks` or `see_user_dashboards` permissions) and folder access.



The following features are not available for embedded reports:

  * Downloading of embedded reports
  * Printing of embedded reports
  * Scheduling of embedded reports
  * Alerting for embedded reports
  * Custom theming of embedded reports
  * Mobile embedding of reports



## Requirements and permissions

Embedding reports requires that the [**Looker reports**](https://docs.cloud.google.com/looker/docs/enabling-studio-in-looker) feature be enabled.

Embed users must have the following types of access to see embedded reports:

  * The `access_data`, and `see_looks` or `see_user_dashboards` permissions
  * **View** or **Manage Access, Edit** access to the parent folder where an embedded report is saved.



## Development requirements

Detailed instructions for setting up a development server, in addition to development considerations for reports, can be found in the [Looker Embed SDK GitHub repository](https://github.com/looker-open-source/embed-sdk?tab=readme-ov-file#looker-javascript-embed-sdk).

## View embedded reports

Users can navigate folders and view embedded reports [the same way that they can view other embedded Looker content](https://docs.cloud.google.com/looker/docs/viewing-embedded-items#using_embedded_folders_to_find_looks_and_dashboards).

**Caution:** Reports can't be copied or moved to folders that are more than five levels deep, or to folders that have [custom access levels](https://docs.cloud.google.com/looker/docs/access-levels#configure_groups_to_provide_granular_access).

See [Move, share, and copy reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) for more information about the access and permissions that are required to move, copy, and delete reports.

## Embed reports

You can embed reports by using the [private embed](https://docs.cloud.google.com/looker/docs/private-embedding), [cookieless embed](https://docs.cloud.google.com/looker/docs/cookieless-embed) and [signed embed](https://docs.cloud.google.com/looker/docs/signed-embedding) methods. The process for embedding a report using private embed or signed embed is the same as for embedding a dashboard or a Look. For example, the URL for a report is `https://instance_name.cloud.looker.com/reporting/bafbc704-c8fd-4ebc-aa57-21c4fe407e0b`. The format for the URL is as follows:

  * [**Host name**](https://docs.cloud.google.com/looker/docs/gs-private-embedding#part_1_hostname): The name of your Looker instance. For example: `https://instance_name.cloud.looker.com`
  * [**Path**](https://docs.cloud.google.com/looker/docs/gs-private-embedding#part_2_path): The name of the folder that a report is saved in, called `reporting`, and the ID of the report. For example: `/reporting/bafbc704-c8fd-4ebc-aa57-21c4fe407e0b`



To construct an embed URL, prefix the folder name and report ID in the URL with `/embed/`, like you would for a dashboard or a Look. For example, `https://instance_name.cloud.looker.com/embed/reporting/bafbc704-c8fd-4ebc-aa57-21c4fe407e0b`.

## Provide feedback and report issues

If you experience an issue with embedding Looker reports, or would like to provide feedback, [submit a feedback form](https://docs.google.com/forms/d/12VhN-nC2FG_Qt2XMnCjim8qQPgdvXJPbD-6AmLclHuA/viewform?edit_requested=true).

## Related resources

  * [Get started with private embedding](https://docs.cloud.google.com/looker/docs/gs-private-embedding#3_create_your_iframe)
  * [Getting started with embedding — enabling signed embedding](https://docs.cloud.google.com/looker/docs/embed-enable)
  * [Private embedding](https://docs.cloud.google.com/looker/docs/private-embedding)
  * [Signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding)
  * [Cookieless embedding](https://docs.cloud.google.com/looker/docs/cookieless-embedding)
  * [Introduction to the Embed SDK](https://docs.cloud.google.com/looker/docs/embed-sdk-intro)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
