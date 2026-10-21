---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-view-metrics/
title: Observe metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:32:25.860658+00:00
---

# Observe metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-view-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Observe metrics Stay organized with collections  Save and categorize content based on your preferences. 

You can observe Database Service metrics with the monitoring instance. See [Monitoring and visualizing metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/observability-monitoring-and-visualizing) for general information about the monitoring and visualizing processes for Application Operators (AO) in GDC.

You must create a database cluster before you can observe its metrics.

## View diagnostic logs

  1. Navigate to the monitoring instance UI to access the database diagnostic logs for a database cluster.

  2. Click the explore **Explore** button from the menu to open the **Explore** page.

  3. Enter a query to search for Database Service logs using LogQL.

     1. Using the **Label filters** drop-down menu, create a filter for `service_name=dbs`.

     2. Click the add **Operations** button and select **Line contains**. Enter the database cluster's name in the text box.

     3. Click the add **Operations** button again and select **Line contains**. Enter PROJECT_NAME in the text box.

     4. Click the **Run query** button.




## View metrics

  1. Navigate to the monitoring instance UI to access the metrics for a database cluster.

  2. From the drop-down menu, select **prometheus** as the data source to retrieve metrics.

  3. Application operators can access Database Service metrics that have the `dbs_` prefix. Enter `dbs_` in the **Select a metric** text box in the **Metrics browser** panel to view all Database Service metric types.

  4. Application operators can also access metrics with the `pg_` prefix.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
