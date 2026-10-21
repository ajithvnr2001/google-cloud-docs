---
url: https://docs.cloud.google.com/database-center/docs/generative-views/
title: Generate dashboard views using Gemini \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:12.067919+00:00
---

# Generate dashboard views using Gemini  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/generative-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Generate dashboard views using Gemini Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Generative views**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Database Center includes a feature called _generative views_ , which uses Gemini to let you create customized dashboards by using natural language prompts. Instead of being limited to predefined layouts, you can describe the database fleet information and metrics that you want to view. Gemini processes these prompts to generate a dashboard layout of widgets and data visualizations that matches your request.

Generative views let you query your database fleet's state, configuration, and performance metrics. For example, you can request views showing resources with specific characteristics, such as resources with high CPU usage in a specific region, or databases that don't adhere to certain best practices. You can save the generated dashboards, which lets you return to these custom views to see updated data. You can also modify your original prompts to iterate on and generate new dashboards.

## Before you begin

  * [Ensure that Database Center is set up for your organization](https://docs.cloud.google.com/database-center/docs/set-up-database-center).



## Create a generative view

To create a generative view, do the following:

  1. In the Google Cloud console, go to the **Database Center** page.

[Database Center](https://console.cloud.google.com/database-center)

  2. In the navigation pane, click **Generative views**.

  3. Click add **New**.

  4. In the **Ask Gemini to build a dashboard** field, enter your prompt. For a list of sample prompts, see Sample prompts.

  5. To preview the generated dashboard layout, click send.

  6. To save the view, do the following:

     1. Click **Save custom view**.

     2. In the **Dashboard name** field, review the dashboard name and make any changes you want.

     3. Click **Save**.




## Delete a generative view

To delete a generative view, do the following:

  1. In the Google Cloud console, go to the **Database Center** page.

[Database Center](https://console.cloud.google.com/database-center)

  2. In the navigation pane, click **Generative views**.

  3. Click the generative view that you want to delete.

  4. Click **Delete**.

  5. To confirm the deletion, click **Confirm**.




## Sample prompts

To help you write your prompts, you can use the following sample prompts to get started:

  * "Show me resources with high CPU usage in `us-west1`."

  * "Show me all the databases (all engines) violating configuration best practices for Availability and Data Protection."

  * "Show me a heat map of all production Cloud SQL Postgres instances where CPU utilization has exceeded 80 % in the last 24 hours. Filter for instances with at least 16 vCPUs."

  * "Display a widget of all AlloyDB for PostgreSQL, Cloud SQL and Spanner instances across the organization that don't have high availability (HA) features enabled and are currently running on a version older than the latest minor release."

  * "What are my top 5 prod Cloud SQL instances across the fleet by CPU utilization? Only include the instances which are higher than 8 vCPUs and 8 GB memory."




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
