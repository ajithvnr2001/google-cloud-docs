---
url: https://docs.cloud.google.com/alloydb/docs/monitor-health-clusters-instances/
title: Monitor the health of your clusters and instances \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:40.258752+00:00
---

# Monitor the health of your clusters and instances  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/monitor-health-clusters-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Monitor the health of your clusters and instances Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB for PostgreSQL integrates critical cluster and instance health issues and their recommended resolutions from [Database Center](https://docs.cloud.google.com/database-center/docs/overview) and displays this information in the Google Cloud console. You can use this information to monitor and improve the health of your AlloyDB for PostgreSQL clusters and instances.

Health issues have different priorities, and the most urgent issues—those marked as critical or high priority—are displayed in your AlloyDB cluster list so that you can do the following:

  * Organize, prioritize, assign, and close AlloyDB cluster issues.
  * Take action at an aggregate level.
  * Prevent cluster problems.
  * Use intelligent assistance to predict cluster issues before they occur.



You can view a list of all issues (critical, high, medium, and low) in your database fleet in Database Center. For more information, see [View and filter health issues and recommendations](https://docs.cloud.google.com/database-center/docs/health-issues-recommendations).

## Issue priority definitions

Health issues for AlloyDB are ranked by priority. Critical and high priority issues are displayed in the **Health issues** dashboard on the **Clusters** overview page in the AlloyDB console. Under the **Resources** table, you can view all issues of a cluster by clicking **View issues** in the **Issues** column.

**Note:** These priorities are general. Depending on your resource's environment—production, development, or test—and specific workloads, priorities can vary.Priority | Description  
---|---  
Critical | High risk, immediate service disruption, or a significant security vulnerability if the issue isn't resolved. **Immediate action is required**.****  
High | High risk, but less serious than _Critical_. Unresolved issues might lead to downtime, performance degradation, or data loss.  
Medium | Configurations that aren't recommended or deviations from best practices that require investigation to prevent performance or manageability issues.  
Low | Informational items that are useful but low risk.  
  
## Before you begin

To monitor AlloyDB health issues in the Google Cloud console, you must have the following (Identity and Access Management (IAM)) roles:

  * **AlloyDB Administrator** (`roles/alloydb.admin`) 
    * `alloydb.instances.list`
    * `alloydb.clusters.get`
  * **Monitoring Viewer** (`roles/monitoring.viewer`)

    * `monitoring.timeSeries.list` Note: This role is required to view insight charts in the **Clusters** page, but it isn't required to view Database Center health issues.
  * **Database Center Viewer** (`roles/databasecenter.viewer`) or **Database Center Administrator** (`roles/databasecenter.admin`)

    * `databasecenter.databaseGroups.list`
    * `databasecenter.fleetHealthStats.list`



## Monitor AlloyDB cluster health

The AlloyDB **Clusters** page in the Google Cloud includes a **Health issues** section, which displays the most critical cluster issues across your project.

### View critical and high-priority issues

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Review the **Health issues** dashboard displayed on the page.

This dashboard displays the aggregate count of critical and high priority issues affecting resources in your project. For more information about health issues, see [Database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

  3. To view a summary of all issues affecting the resource, find the resource in the list of **Resources**. Click **View issues** in the **Issues** column.

This opens the **Aggregated issues** side panel. For more information, see [View and filter database fleet health information](https://docs.cloud.google.com/database-center/docs/view-filter-database-fleet-health-information).




### Filter the cluster list by issue

The **Issues** column in the AlloyDB cluster list displays the number of active issues affecting that cluster or any of its primary and read pool instances.

  * To see which issues affect a specific cluster, click **View issues** in the **Issues** column for the resource.

This opens the **Aggregated issues** panel.

  * To view the list of resources affected by a specific issue type, click the issue name card in the **Health issues** dashboard.

This action automatically filters the cluster list to display only the affected resources.




### View and resolve issues for a specific instance

You can view a summarized list of health issues on the **Overview** page for any AlloyDB primary or read pool instance.

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of a cluster.

  3. Click the name of a primary or read pool instance to open the associated **Overview** page.

  4. Find the **Health issues** dashboard. If none of the resources have issues, then this section isn't displayed.

View health issues categorized by cluster or instance.

  5. To resolve an issue, do one of the following:

     * Click **Edit configuration** to display the required setting on the instance's **Edit** page—for example, for database flags or storage settings.
     * Click **Go to System insights** to validate the issue with performance metrics.



## View all AlloyDB issues in Database Center

Database Center provides a list of issues across your database fleet, including all medium and low priority AlloyDB issues. With Database Center you can also view database fleet health recommendations and ask questions about database fleet health issues, including availability configuration, data protection, security, and industry compliance. For more information, see [Database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

To view all AlloyDB issues in Database Center, follow these steps:

  1. In the Google Cloud console, go to the **Database Center** page.

[Go to Database Center](https://console.cloud.google.com/database-center)

  2. Click **Health issues** in the left navigation menu.

  3. Use the table to view all issues across your organization or project. You can filter the list by the following:

     * Priority
     * Product and version
     * Issue Category
     * Location
     * Labels
     * Tags
     * Issues
     * Implications



To download a report that you can use in external tracking systems like JIRA or internal dashboards, click **Export CSV of issue details**.

## What's next

  * Learn more about [Database Center](https://docs.cloud.google.com/database-center/docs/overview).
  * [Monitor AlloyDB instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance).
  * Learn [best practices for improving AlloyDB performance and availability](https://docs.cloud.google.com/alloydb/docs/best-practices-improve-performance-availability).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
