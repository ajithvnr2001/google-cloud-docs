---
url: https://docs.cloud.google.com/database-center/docs/view-filter-database-health-issues/
title: View and filter database health issues \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:44.723163+00:00
---

# View and filter database health issues  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/view-filter-database-health-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  View and filter database health issues Stay organized with collections  Save and categorize content based on your preferences. 

In Database Center, you can filter database issues and view an aggregation of recent health issues. Use these tools to manage information that helps you troubleshoot your database fleet health.

## Before you begin

  * [Ensure Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).



## Filter database health issues

To specify which database health issues you care about and the thresholds you consider relevant, follow these steps:

  1. Go to the **Database Center** page in the Google Cloud console.

[Database Center](https://console.cloud.google.com/database-center)

  2. Click **All Resources**.

  3. Click **Filter**.

  4. In the **Properties** drop-down, enter a property name, like **Country:United States**. To refine your query, enter a value like **Or** and another property name like **Country:Canada**. Database Center displays only those health issues related to the property name.

  5. Click **Show Resource Details** to show database resource details. Click **Hide Resource Details** to hide database resource details.

  6. Click a health issue to learn health issue details, including recommended resolutions.

  7. Click **Go to Resource** to display detailed information about the database resource experiencing the database health issue.




You can also filter database health issues by clicking one of the database health categories, like **Availability Configuration** , **Data Protection** , **Security** , **Industry Compliance** , **Performance and Capacity** , and **Cost**. These fields only appear if there are database issues with database resources in those categories.

## View recent health issues by category

**Preview — View recent health issues by category**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To view recent health issues that occurred in a category in the last seven days, follow these steps:

  1. Go to the **Database Center** page in the Google Cloud console.

[Database Center](https://console.cloud.google.com/database-center)

  2. Click **Overview**.

  3. Filter the database health issues so the database issues you want to see are visible in the Database Center dashboard.

  4. In **Fleet issues** , you can see how many new issues were found in the last seven days for each category.

  5. Click **View** to see the health issues that were found. If no new issues were found for a category, then the section for that category that shows the number of new issues and the **View** button isn't displayed.

  6. For each health issue in the list of recently found health issues, click the button in the **Issue** column to learn more.




## What's next

  * [View recently added database resources](https://docs.cloud.google.com/database-center/docs/view-filter-database-fleet-health-information#view-recently-added-resources).
  * [Troubleshoot database fleet health issues](https://docs.cloud.google.com/database-center/docs/troubleshoot-database-health-issues).
  * [Monitor your database fleet with alerting policies](https://docs.cloud.google.com/database-center/docs/alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
