---
url: https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information/
title: Filter resources and export fleet inventory information \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:47.634237+00:00
---

# Filter resources and export fleet inventory information  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Filter resources and export fleet inventory information Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to filter the database fleet information that is displayed in your Database Center dashboard, and describes how to export database fleet inventory information into a CSV file.

You can filter the following information in the Database Center dashboard:

  * Database products and versions
  * Regions
  * Labels
  * Tags
  * Google Cloud projects, if you select a folder or organization in the **Open project picker** in the Google Cloud console.



## Filter by labels and tags

You can filter resources that appear in the Database Center dashboard by using labels and tags. Filtering database resources by labels and tags lets you do the following:

  * Focus on the database groups that matter to you.
  * Filter out non-critical information, like databases used for non-production purposes (development, testing, staging, and benchmarking).



If you filter by both labels and tags, then all resources with either a selected label or a selected tag are displayed in the dashboard. For example, if you filter by labels and tags with `env - prod`, then database resources with either are listed.

A _label_ is a key-value pair that you can assign to Google Cloud resources. You can use labels to help you organize these resources and manage your costs at scale. Labels are imported from your organization or Google Cloud projects. Database Center uses the labels associated with your organization's Google Cloud projects. To learn more, see [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels).

A _tag_ is a key-value pair that can be attached to a Google Cloud resource. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. To learn more, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

To learn more about labels and tags, see [Differences between labels and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels).

## Before you begin

  * [Ensure that Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).



## Filter database resources

  1. In the Google Cloud console, go to the **Overview** page in **Database Center**.

[Database Center](https://console.cloud.google.com/database-center/resources)

  2. From the drop-down in the Google Cloud console menu bar, select a database scope—for example, a Google Cloud project, folder, or organization.

  3. Optional: Click **Labels** to add labels to your filter. Click **Tags** to add tags to your filter. For more information, see [Filter by labels and tags](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information).

  4. Click **Products** , **Locations** , **Labels** , **Tags** , and **Issues** to select the products, locations, label, tag, and issue filters you want to apply to your dashboard. The data in your Database Center dashboard view changes based on your filter selections. For more information, see [Filter by labels and tags](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information)

  5. You can apply additional filters to the **Resources** table based on properties like resource name, CPU count, memory size, and peak storage utilization. Click filter_list **Filter** and select one or more filters.

  6. Optional: To choose your column display options, click .




## Export database fleet inventory information

You can export database fleet inventory information to a comma-separated values (CSV) file. Exporting to a CSV file is useful when you want to work with and analyze database fleet information in a spreadsheet.

  1. In the Google Cloud console, go to the **Database Center** page.

[Database Center](https://console.cloud.google.com/database-center)

  2. From the drop-down in the Google Cloud console menu bar, select a database scope—for example, a Google Cloud project, folder, or organization.

  3. Click **CSV Export**. Database Center downloads fleet inventory information for your database scope (Google Cloud project, folder, or organization) resources to a CSV file.




## What's next

  * [Analyze your database inventory](https://docs.cloud.google.com/database-center/docs/analyze-database-inventory).
  * [Troubleshoot database health issues](https://docs.cloud.google.com/database-center/docs/troubleshoot-database-health-issues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
