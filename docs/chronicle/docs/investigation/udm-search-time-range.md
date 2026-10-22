---
url: https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-time-range/
title: Manage search details \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:12.905006+00:00
---

# Manage search details  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-time-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage search details

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Security Operations gives you the ability to search through up to a year of the enterprise data stored in your account. It also includes a number of tools that let you run multiple UDM search queries and later retrieve and share the results of those queries.

## Use UDM to search up to a year of data

You can conduct a UDM search on up to one year of your UDM data. To adjust the time period for your UDM search, complete the following steps:

  1. Go to **Investigation > SIEM Search**.
  2. Click the time selector field to open the time selector dialog.
  3. From the **Range** tab (the default tab), adjust the time range by selecting any of the options from **Last 5 minutes** to **Last year**.
  4. Use the **Start** and **End** fields to choose a more specific date range (for example, the first two weeks in November). 
  5. Adjust the times by selecting specific start and end values, for example, 03:00 and 08:30.
  6. Click **Apply** and then click **Run Search**.



## Run concurrent searches and manage search queries

Concurrent searches and stored results require the search history feature to be active. To ensure that search history is on, complete the following steps:

  1. Go to **Investigation > SIEM Search**.

  2. Click **History**. If the **Search History Is Disabled** message is displayed, proceed to the next step. If you don't see this message, then **Search History** is already enabled for your account.

  3. Click  more_vert  and select **Opt into search history**.




### Manage search queries

You can run multiple UDM searches, retrieve previous query search results, and share your query results with other members of your team:

  * **Run multiple UDM searches** : While a search query is in progress, you can run additional searches in the query editor. Google SecOps continues running your previous searches and runs the new searches in parallel.

  * **View query results** : Scroll through the query history and select search results within 24 hours of running a query. Click **History** and select one of your queries from the list.

In-progress queries are displayed with a circular status icon. Completed queries are displayed with a green check mark icon, along with a counter indicating the number of events returned by the query. Click a completed query to display the results. These results are cached and only include the data available at query run time. However, you can click  cached  **Rerun** to run the query against the latest data. This new run is added to the search history and the results are made available when the query completes.

  * **Share query results** : Copy the URL of the query results to share them with other users.

When search results are stored, the RBAC scopes of the user who ran the search are stored with them. When these results are viewed by another user, the viewer's RBAC scope is compared to the stored scopes. If the viewer's scopes are more restrictive, an error is displayed and they won't be able to view the results.

Stored search results expire 24 hours after a query is run. However, your search query is still available in the **History** pane. You can rerun your searches and the results are made available for up to 24 hours after the query run time.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
