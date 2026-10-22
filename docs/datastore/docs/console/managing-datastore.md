---
url: https://docs.cloud.google.com/datastore/docs/console/managing-datastore/
title: Managing Firestore in Datastore mode from the Console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:18.570512+00:00
---

# Managing Firestore in Datastore mode from the Console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/console/managing-datastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Managing Firestore in Datastore mode from the Console Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view and manage the entities, indexes, and statistics for the data your application stores in your database.

## Viewing Datastore statistics

  1. In the Google Cloud console, go to the **Databases** page.

[Go to Databases](https://console.cloud.google.com/datastore/databases)

  2. Select the required database from the list of databases.

  3. In the navigation menu, click **Datastore Studio** to view data for the entities in your application, as well as statistics for the built-in and composite indexes.




The dashboard should look like:

![Datastore Dashboard](https://docs.cloud.google.com/static/datastore/images/datastore_admin_dashboard.png)

For more information about the statistics on this page, see [Viewing Statistics in the Console](https://docs.cloud.google.com/datastore/docs/console/datastore-statistics).

## Viewing indexes

  1. In the Google Cloud console, go to the **Databases** page.

[Go to Databases](https://console.cloud.google.com/datastore/databases)

  2. Select the required database from the list of databases.

  3. In the navigation menu, click **Indexes** to view a table of your application's indexes.




For each index, you should see its status, such as whether it is ready to serve your application. You should also see the amount of storage space used by the index and the number of entries in each index.

## Viewing entities

  1. In the Google Cloud console, go to the **Databases** page.

[Go to Databases](https://console.cloud.google.com/datastore/databases)

  2. Select the required database from the list of databases.

  3. In the navigation menu, click **Datastore Studio** to view the entities that your application stored in your database.




You should see:

![Datastore Studio page](https://docs.cloud.google.com/static/datastore/images/datastore_studio_page.png)

You can also create, update, delete, and query entities on this page. Learn how in the [Quickstart](https://docs.cloud.google.com/datastore/docs/store-query-data).

**Note:** While individual entities are removed almost immediately, a namespace container may remain visible for several days to a week after the final entity within it is removed.

## What's next?

  * Get details about [Statistics in the Console](https://docs.cloud.google.com/datastore/docs/console/datastore-statistics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
