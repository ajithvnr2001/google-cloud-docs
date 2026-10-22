---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/estimate-projected-costs/
title: Estimate projected costs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:14.675125+00:00
---

# Estimate projected costs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/estimate-projected-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Estimate projected costs Stay organized with collections  Save and categorize content based on your preferences. 

The Projected Cost dashboard is a management tool that lets you anticipate future SKU costs for your invoices. You can filter the dashboard to view a custom projection cost of a given SKU through the task order (TO), contract line item number (CLIN), and month.

To get the permissions that you need to view the Projected Cost dashboard, ask your IAM Org Admin to grant you the corresponding project viewer role for the `platform-obs` project.

To access the Projected Cost dashboard in the GDC console, work through the following steps:

  1. Sign in to the GDC console.
  2. In the navigation menu, select **Billing > Reports**. The **Billing reports** page opens. 
  3. In the **Cost projection** section, click **View in Dashboard** to open the Invoice dashboard. 



The Projected Cost dashboard provides the unique values to view your future costs through the **Projected Cost Table**. The **Projected Cost Table** contains the following columns:

Column | Description  
---|---  
**SKU** | The resource ID and description.  
**Projected Total** | The projected total for each line item SKU.  
**Projected Total Cost (USD)** | The cumulative projected total cost in USD of all SKUs that appear in the dashboard.  
  
To filter the values in the **Projected Cost Table** , select the following items in the menu bar:

  * **SKU** : a drop-down that lets you select which SKU to view. This drop-down defaults to **All**.
  * **Task Order - CLIN** : a drop-down that lets you select a specific task order and contract line item number to view. This drop-down defaults to **All**.
  * **Months** : an input field to add the amount of months you want to view. For example, **1** displays one month of the cost of a given SKU, while **2** shows a value of two months.



After you select your unique values in the menu bar, you see the Projected Cost dashboard update to the future costs of a collection of SKUs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
