---
url: https://docs.cloud.google.com/database-center/docs/fleet-maintenance/
title: View maintenance events and windows for your database fleet \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:46.640969+00:00
---

# View maintenance events and windows for your database fleet  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/fleet-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  View maintenance events and windows for your database fleet Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — View and set fleet maintenance windows**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Database Center lets you view maintenance windows and maintenance events—including upcoming, in-progress, and completed events—for resources in your database fleet. You can also view maintenance window recommendations to help you maintain your database fleet. Database Center uses factors, such as a resource's environment (production or non-production) and traffic, to create suggested maintenance windows. Database Center also identifies resources without a set maintenance window and provides recommendations to help you set a maintenance window for every resource in your database fleet.

Database Center supports viewing and creating maintenance window recommendations for AlloyDB for PostgreSQL resources and resources for all Cloud SQL engines (MySQL, PostgreSQL, and SQL Server).

A maintenance window defines the preferred time, by hour-of-the-day and day-of-the-week, for your resources to begin maintenance events. For example, you can set a resource to have a maintenance window that begins at 11 AM on Sundays (UTC). By default, database resources don't have a maintenance window. For more information about maintenance windows, see the following:

  * For AlloyDB for PostgreSQL resources, see [Maintenance timing and maintenance preferences](https://docs.cloud.google.com/alloydb/docs/maintenance).

  * For resources for Cloud SQL engines, see the following:

    * [View and set maintenance windows in Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window)
    * [View and set maintenance windows in Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/set-maintenance-window)
    * [View and set maintenance windows in Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/set-maintenance-window)



## Before you begin

  * [Ensure you set up Database Center for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).

  * Make sure your instance is set up:

    * For AlloyDB for PostgreSQL, see [Create and configure an AlloyDB for PostgreSQL cluster and instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

    * For Cloud SQL, see one of the following quickstarts:

      * [Create instances in Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-instance)
      * [Create instances in Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-instance)
      * [Create a database in Cloud SQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance)



## View database resource maintenance events and windows

To view information about database resource maintenance events and windows, go to the **Maintenance** page in Database Center.

[Go to Database Center](https://console.cloud.google.com/database-center/maintenance)

After the **Maintenance** page opens, review the following information about maintenance events and windows in your database fleet.

The **Summary** card shows you the following:

  * How many of your database resources have a configured maintenance window.

  * How many of your database resources have recommended maintenance windows created by Database Center.

  * How many of your database resources have a deny maintenance period configured. During a deny maintenance period, updates aren't allowed.




The **Managed maintenance updates** card has four tabs:

###  Upcoming 

The **Upcoming** tab shows you the following information about resources that have an upcoming maintenance event scheduled:

  * The database product.

  * The number of resources in your database fleet for each product.

  * The number of resources for the product without a configured maintenance window.

  * A link to the maintenance plan for the product.




###  In progress 

The **In progress** tab shows you the following information about resources that are undergoing maintenance.

  * The database product and version.

  * The status that indicates the number of updated resources.

  * A link to the maintenance plan for the product.




###  Completed 

The **Completed** tab shows you the following information about resources that have recently completed maintenance:

  * The database product and version.

  * The status that indicates the number of updated resources.

  * A link to the maintenance plan for the product.




###  Ready 

The **Ready** tab shows you the following information about resources that are ready to use:

  * The database product and version.

  * A link to view the maintenance plan.




The **Recommended maintenance windows by resource** card shows you information for each resource, including the following:

  * The name of the resource.

  * The database product name and version.

  * The most recent version of the product before the last update.

**Note:** Resource version history before April 22, 2026 isn't available.
  * The installed version of the product.

  * The number of days since the last version update.

  * The status of maintenance on the resource. This status indicates whether maintenance is scheduled, in progress, completed, or failed. Failure statuses include reasons such as a deny maintenance period or a stopped instance.

  * The current maintenance window configured for the resource. If a resource has no configured maintenance window, **None** appears.

  * A menu of maintenance windows that Database Center recommends. Learn how to set a recommended maintenance window.




## Set a recommended maintenance window

To set a recommended maintenance window for a database resource, complete these steps:

  1. Locate the resource for which you want to update the maintenance window by completing one of the following steps:

     * To locate a resource by product, click **View maintenance plan** for a product in the **Managed maintenance updates** card. In the table that appears, find the resource you want to update.

     * Find the resource in the **Recommended maintenance windows by resource** card.

  2. In the table row for the resource you want to update, click the **Recommended windows** drop-down menu. Then, find a recommended maintenance window you want to implement and make a note of its day and times. You need this information to set the maintenance window in the next step. Clicking a recommended maintenance window in the drop-down menu doesn't apply the maintenance window.

  3. Click the resource name or **Apply** to navigate to a page in the Google Cloud console where you can specify the recommended maintenance window you chose in the previous step. For information about how to specify a maintenance window for an AlloyDB for PostgreSQL resource (cluster), see  
[Set a maintenance window on a cluster](https://docs.cloud.google.com/alloydb/docs/maintenance-windows#set-window).




## What's next

  * Learn more about [Database Center](https://docs.cloud.google.com/database-center/docs/overview).

  * Learn how to [customize your database fleet view](https://docs.cloud.google.com/database-center/docs/customize-database-fleet-view).

  * Learn how to [analyze database fleet health using Gemini](https://docs.cloud.google.com/database-center/docs/analyze-database-using-gemini).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
