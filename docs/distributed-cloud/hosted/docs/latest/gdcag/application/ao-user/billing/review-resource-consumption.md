---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/billing/review-resource-consumption/
title: Review resource consumption \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:54.091072+00:00
---

# Review resource consumption  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/billing/review-resource-consumption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Review resource consumption Stay organized with collections  Save and categorize content based on your preferences. 

View the consumption of each resource through the Billing reports dashboards. These dashboards are available to track your resource consumption over a period of time, and help you manage your resources effectively.

To get the permissions you need to view the Billing Usage dashboards, ask your Organization IAM Admin to grant you the corresponding viewer role for your project.

The Billing Usage dashboards consist of the following:

  * **Storage Allocation** : tracks how much resource usage a given service in your project has consumed. Services include resources such as Backup, Marketplace, Database Service, and Vertex AI.

![Graphs for Pod and VM Backup counts ranging from 0 to 2000](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/ao-billing-services-usage-dash-.png)

**Important:** Metrics in the Services Usage dashboard is not a direct mapping to the price you might see in the Invoice dashboard. For example, the quantity of consumption you see in the Services Usage dashboard might not match the quantity GDC used to calculate the price in the Invoice dashboard.
  * **Compute Allocation** : tracks the metrics of resource usage on Storage and Compute services for a given period of time. This dashboard is available for monitoring purposes.

![Graphs for Compute Inventory showing node inventory and vCPU cores, and graphs for Compute Usage showing allocated memory, servers, and vCPU percentage](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/ao-billing-storage-compute-dash.png)




To view the Billing Usage dashboards, work through the following steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Billing > Reports**.
  3. In the **Billing reports** page, select the service that you want to view. For example, to view the metric consumption of the managed service, Vertex AI, click either `GPU` or `vCPU`.
  4. To view a certain period of time in a given dashboard, click the **Time** drop-down in the menu bar. The **Time** drop-down defaults to show the metrics of the last six hours.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
