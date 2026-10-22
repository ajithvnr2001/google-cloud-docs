---
url: https://docs.cloud.google.com/database-center/docs/view-filter-database-fleet-health-information/
title: View and filter database fleet health information \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:44.989714+00:00
---

# View and filter database fleet health information  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/view-filter-database-fleet-health-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  View and filter database fleet health information Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to view and filter database fleet inventory and health issue information on your Database Center dashboard.

## Before you begin

  * [Ensure that Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).



## View database fleet health information

  1. In the Google Cloud console, go to the **Database Center** page.

[Database Center](https://console.cloud.google.com/database-center)

  2. To define the scope of your database fleet, use the drop-down in the Google Cloud console menu bar, select a Google Cloud project, folder, or organization.

  3. Select the Google Cloud project, products and versions, regions, and label and tag filters you want to apply to your dashboard. For more information about filtering by labels and tags, see [Filter database resources](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information#filter-database-resources).

  4. To view a summary of your database fleet inventory, click **Overview** and view the **Fleet inventory** pane.

  5. To view a summary of database fleet health issues, view the **Fleet issues** pane. To learn more about a specific issue, click the issue to see details and any relevant recommendations or next steps.




## View recently added database resources

**Preview — View recently added database resources**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To view the number of database resources added to your database fleet in the last seven days, follow these steps:

  1. Go to the **Database Center** page in the Google Cloud console.

[Database Center](https://console.cloud.google.com/database-center)

  2. Click **Overview**.

  3. In **Time range** , click time range you want for the recently added database resources. The options are:

     * **1 day**
     * **7 days** (default)
     * **30 days**
  4. In the **Fleet inventory** pane, click the **View inventory changes** link. The text of the link reflects the time range you clicked in the previous step.




## Filter database fleet health information

You can filter your database resources information to focus on the database fleet information that's important to you. Your filtering choices apply to the **Overview** and **All Resources** pages on the Database Center dashboard.

Your database fleet is represented as database groups and individual database resources. A _database group_ represents all database resources that serve the same data and replicate together (parents and children together as a family).

An individual _database resource_ is anything you provisioned that represents compute and storage (a single family member).

To filter your database resources, follow these steps:

  1. In the Google Cloud console, go to the **Database Center Overview** page.

[Database Center](https://console.cloud.google.com/database-center)

  2. To define the scope of your database fleet, use the drop-down in the Google Cloud console menu bar, select a Google Cloud project, folder, or organization.

  3. Click **Products** , **Locations** , **Labels** , **Tags** , and **Issues** to select the products, locations, label, tag, and issue filters you want to apply to your dashboard. The data in your Database Center dashboard view changes based on your filter selections. For more information, see [Filter by labels and tags](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information).

  4. You can apply additional filters to the **Resources** table based on properties like resource name, CPU count, memory size, and peak storage utilization. Click filter_list **Filter** and select one or more filters.

  5. In the **Fleet inventory** pane, select the fleet inventory filters you want to apply. For more information, see [Analyze your database inventory](https://docs.cloud.google.com/database-center/docs/analyze-database-inventory).

     * In **Segment 1** , choose how you want to group database resources in your inventory in the first column.

     * In **Segment 2** , choose how you want to group database resources in each row.

![Overview of the Database Center dashboard showing fleet inventory and health issues.](https://docs.cloud.google.com/static/database-center/images/database-center-overview-page.png)




## What's next

  * [Filter resources and export fleet inventory information](https://docs.cloud.google.com/database-center/docs/filter-resources-export-fleet-inventory-information).
  * [Analyze your database inventory](https://docs.cloud.google.com/database-center/docs/analyze-database-inventory).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
