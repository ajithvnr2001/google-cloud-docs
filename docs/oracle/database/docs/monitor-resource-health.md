---
url: https://docs.cloud.google.com/oracle/database/docs/monitor-resource-health/
title: Monitor the health of your resources in Database Center \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:44.607981+00:00
---

# Monitor the health of your resources in Database Center  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/monitor-resource-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Monitor the health of your resources in Database Center Stay organized with collections  Save and categorize content based on your preferences. 

Oracle Database@Google Cloud integrates with [Database Center](https://docs.cloud.google.com/database-center/docs/overview) to provide fleet-wide insights, proactive alerts, and actionable recommendations for your Oracle Database@Google Cloud resources, including Oracle Exadata, VM Clusters, and Autonomous AI Databases.

You can use Database Center to view fleet inventory information and monitor your Oracle Database@Google Cloud resources for critical health issues.

## Before you begin

  * [Make sure that Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).

  * To monitor Oracle Database@Google Cloud resources and their health issues in Database Center, you must have the following Identity and Access Management (IAM) roles:

    * Database Center Viewer (`roles/databasecenter.viewer`) or Database Center Administrator (`roles/databasecenter.admin`): to view insights in the Database Center
    * Oracle Database@Google Cloud viewer (`roles/oracledatabase.viewer`): to view Oracle Database@Google Cloud resource details

For more information on how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## View fleet inventory

Database Center lets you view an inventory of the resources in your database fleet. The **Inventory** page shows you the following information:

  * The number and list of your resources, including including Oracle Exadata, VM Clusters, and Autonomous AI Databases.
  * The number of resources used by each product version in your fleet.
  * Your database inventory filtered by labels and tags.
  * The inventory of resources grouped by location.



For more information, see [View your fleet inventory](https://docs.cloud.google.com/database-center/docs/view-inventory).

## View and filter health issues and recommendations

Health issues for Oracle Database@Google Cloud are ranked by priority as follows:

**Note:** These priorities are general. Depending on your resource's environment—production, development, or test—and specific workloads, priorities can vary.Priority | Description  
---|---  
Critical | High risk, immediate service disruption, or a significant security vulnerability if the issue isn't resolved. **Immediate action is required**.****  
High | High risk, but less serious than _Critical_. Unresolved issues might lead to downtime, performance degradation, or data loss.  
Medium | Configurations that aren't recommended or deviations from best practices that require investigation to prevent performance or manageability issues.  
Low | Informational items that are useful but low risk.  
  
For a list of supported health issues in Database Center for Oracle Database@Google Cloud, see [Supported health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues#supported-health-issues). You can view a list of all issues in your database fleet in Database Center. For more information, see [View and filter health issues and recommendations](https://docs.cloud.google.com/database-center/docs/health-issues-recommendations).

## What's next

  * Learn more about [Database Center](https://docs.cloud.google.com/database-center/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
