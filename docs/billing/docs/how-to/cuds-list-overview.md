---
url: https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview/
title: View your commitments \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:21.387364+00:00
---

# View your commitments  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  View your commitments Stay organized with collections  Save and categorize content based on your preferences. 

The Committed use discounts (CUDs) page in the Google Cloud console shows a summary of your commitments.

The page provides an aggregated view for high-level metrics and lets you drill-down into the details of various types of CUDs. Use this page to view information about your commitments, and take actions such as changing the auto-renewal settings for resource-based CUDs, or viewing recommendations for additional commitments.

### Permissions required to view commitments

To view the Committed use discounts (CUDs) page for your Cloud Billing account, you must be a [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access) or [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on the Cloud Billing account.

## Access the commitments inventory page

To view the Committed use discounts (CUDs) page for your Cloud Billing account:

  1. In the **Billing** section of the Google Cloud console, click **Committed use discounts**.

[Go to Committed use discounts (CUDs)](https://console.cloud.google.com/billing/reports/commitments)

  2. At the prompt, **choose the Cloud Billing account** that you want to view.

The CUDs page opens and shows a list of the active commitments for the selected billing account.




## Information in the commitments table

![Example of the Committed use discounts \(CUDs\) page](https://docs.cloud.google.com/static/billing/docs/images/cud-dashboard.png)

![](https://docs.cloud.google.com/static/billing/docs/images/cud-dashboard.png)

To filter your commitments by their properties, select **Filter**. Your filter, column visibility, and sorting settings persist for your next visit.

You can use the columns in the table to get the following information:

  * Use the **Active CUDs** column to see the total quantity of commitments you've purchased for the filters that you select. For example, if you have multiple spend-based Cloud SQL commitments in `europe-west2`, the column shows the total amount for those commitments.

**Note:** If you've purchased a new spend-based commitment, the commitment is active at the beginning of the next hour.
  * If you have eligible usage that could be covered by an additional commitment, use the **Recommendation** column to view details about recommended commitments. To view your commitment recommendations, click **Recommendations** in the action bar.




To view additional columns, click the **Column display options** view_column, and select one or more of these columns:

### View commitment details

![Example of the CUD details page](https://docs.cloud.google.com/static/billing/docs/images/cud-details.png)

![](https://docs.cloud.google.com/static/billing/docs/images/cud-details.png)

To view detailed information about a specific commitment, click the row for that commitment in the table. This opens a side panel with additional details, including the historical utilization rate for each closed entitlement window. For resource-based commitments, you can also use the **Auto-renew** setting in the details panel to set up or cancel auto-renewal for the commitment. [Learn more about what you need to consider when you turn on auto-renewal](https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically).

From the detailed view, you can also access the following actions:

  * **Analysis** : Opens the CUD analysis report for the specific commitment.
  * **Recommendations** : View a summary and list of services with potential savings.
  * **Download CSV** : Download the information about your commitments as a comma-separated value (CSV) file. This option is also available from the summary view.
  * **Commitment fee SKU** : The SKU associated with the commitment fee. Use the Commitment fee SKU to get your current price in your [Pricing export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/pricing-data).



### Download your commitment data

You can download the information about your commitments as a comma-separated value (CSV) file for offline analysis. The CSV file contains the information you see on the **Committed use discounts (CUDs)** page.

You can use the subscription ID to join your CUDs data to your usage data in the BigQuery export. For example, you can import your BigQuery dataset and CSV file to Data Studio for analysis, and then [use data blends to combine the data sources](https://support.google.com/looker-studio/topic/9061419).

To download your commitment data, click **Download CSV** in the action bar.

**Note:** The legacy grouped list CSV download remains available until February 28, 2027.

[Go to legacy commitments report](https://console.cloud.google.com/billing/reports/commitments-legacy)

## Related topics

  * [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds)
  * [Calculate your savings with Compute Engine Flexible CUDs](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-flexible)



To learn how to purchase resource-based commitments for Compute Engine, see the following pages of the Compute Engine documentation:

  * [Purchase hardware commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments)
  * [Purchase hardware commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations)
  * [Purchase software commitments for OS licenses](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
