---
url: https://docs.cloud.google.com/billing/docs/how-to/view-history/
title: View your cost and payment history \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:07.157098+00:00
---

# View your cost and payment history  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/view-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  View your cost and payment history Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Billing cost and payment history is available in the **Transactions** page for each Google payments account that is linked to your Cloud Billing account.

The Google payments account includes a payment instrument to which costs are charged (such as an invoice, credit card, or bank account).

![Illustrates how a Cloud Billing account is related to projects
     and to your Google payments profile and payments
     accounts. One side shows your Google Cloud resources
     \(a Cloud Billing account and its associated projects\) and the
     other side shows the Google payments center and how it's related to
     the Cloud Billing account \(with an associated Google payments
     profile and linked payments accounts\). Your projects' usage
     costs are tracked in your Cloud Billing account. The linked
     Google payments accounts manage payments-related information, including
     invoices and statements, and the payment instruments used to pay your
     bill.](https://docs.cloud.google.com/static/billing/docs/images/billing-project.png)

**Note:** If you **purchased Google Cloud from a _reseller_** , you can't access the **Transactions** page. To see detailed cost information, use the [Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

## Permissions required to view your cost and payment history

To access the **Transactions** page for the Google payments account that is linked to your Cloud Billing account, you need a role on your Cloud Billing account that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.accounts.getPaymentInfo`



To gain this permissions using a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions), you need to be assigned to one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

  * [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)



For more information about billing permissions, see:

  * [Overview of access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



## View transaction history

To view your transaction history, access the **Transactions** page for the Google payments account you want to view. Your Google payments account corresponds with your billing account's [charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle).

  * For _Postpay_ and _Invoicing_ charging cycles, you can access the Transactions page in the Cloud Billing console.
  * For _Prepay_ charging cycles, you can access the Transactions page in the [Google AI Studio](https://ai.google.dev/gemini-api/docs/billing#prepay) console.



### Postpay and Invoicing accounts

Follow these steps to access the Transactions page for your _Postpay_ or _Invoicing_ Google payments account:

  1. In the Google Cloud console, go to the **Transactions** page.

[ Go to the Transactions page](https://console.cloud.google.com/billing/history)
  2. At the prompt, **choose the Cloud Billing account** you want to view. 

The **Transactions** page opens for the Postpay or Invoicing payments account.

  3. If the Cloud Billing account was linked with different Google payments accounts in the past, click **View past accounts** to see transactions that were charged to an earlier payment method.



### Prepay account

Follow these steps to access the Transactions page for your _Prepay_ Google payments account:

  1. In the Google AI Studio console, go to Dashboard > Billing.

[ Go to the AI Studio Billing page](https://aistudio.google.com/billing)
  2. Locate the **Transactions** card and click **View transactions**. 

The **Transactions** page opens for the Prepay payments account.

  3. If the Cloud Billing account was linked with different Google payments accounts in the past, click **View past accounts** to see transactions that were charged to an earlier payment method.



On the **Transactions** page, the default view is a detailed transaction view of _all_ transactions for the last 3 months. Use the toggles on this page to do any of the following:

  * Select level of detail to display: Switch between a **Detailed transaction view** (default) and a **Summary view**.
  * View account history by transaction type: Select the type of transactions you want to view. Options include **All transactions** (default), or you can filter transactions by **Costs** , **Payments** , **Adjustments** (usually, any credits applied to your account), and **Taxes** (such as sales tax or Value Added Tax (VAT) that apply to your account).
  * Change the date range: The default date range is **Last 3 months**. You can choose one of the **pre-defined date ranges** , such as **Previous month** or **This year** , or select **Custom date range** to set a range you prefer.



## Access or download documents

On the **Transactions** page, you can access and download available documents (for example, invoices or statements) or payment receipts. The documents available to access and download depend on your [billing account type](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), [payments account charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle), as well as the views and filters you set on the **Transactions** page.

### Access statements or invoices

  1. In the **Transactions** table, expand the **Documents** row to view available documents.

     * If the available documents are _statements_ , click the **statement number** to download a PDF version of the statement.
     * If the available documents are _invoices_ , click **View invoices** to access the [**Invoices** page](https://docs.cloud.google.com/billing/docs/how-to/get-invoice#invoiced-account) where you can view and download your invoices.

Both statements and invoices include a summary of your monthly costs but don't include a breakdown of your cost details. To understand the cost details that reconcile to your invoice, including a granular view of your monthly costs such as project-level breakdowns and costs by subaccount (for resellers), use the Cloud Billing **Cost table report**. See [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for more information.




### Access payment receipts

  1. On the **Transactions** page, set the toggles above the table to control the view and filter the list of transactions: 
     1. In the **View** drop-down, select **Detailed transaction view**.
     2. In the **Transaction type** drop-down, select **Payments**. The list of transactions is filtered to display payments made.
     3. In the **Date range** drop-down, set the **date range** so that it corresponds to the receipts you want to view.
  2. From the list of transactions, in the **Description** column, click the **Payment** link to view the payment receipt. The receipt opens in a new browser window.



### Download or print account activities

  * To **download a CSV of the account activities** displayed in the **Transactions** table, in the table header, click **Download** get_app.

  * To **print a report of the account activities** displayed in the **Transactions** table, in the table header, click **Print** print.




### Missing transactions

Google Cloud and billing-eligible products such as Google Maps Platform, Google AI Studio, and Firebase report usage data to Cloud Billing at varying intervals. Due to the complexity of our billing and processing systems, you might see a delay between your use of services, the usage _charges_ being applied to your Google payments accounts, and the _usage and costs_ being available to view in the various cost reports and dashboards.

  * Typically, your cost details are available within a day, but can sometimes take more than 24 hours.
  * For self-serve, online accounts, it's possible that _charges_ for some usage might occur rapidly, such as 5 to 15 minutes after usage.
  * Because of this difference in timing, you might notice charges on your [Postpay or Prepay payments accounts](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle) occur before you can view the details of those charges in a cost report or billing dashboard. These system delays also impact budget alerts, anomaly detection, and billing data exported to BigQuery.



After accounting for processing and reporting delays, if you can't find a specific document or transaction related to your usage of resources and services in Google Cloud, Google Maps Platform, Firebase, and Google AI Studio, [contact Cloud Billing Support](https://docs.cloud.google.com/billing/docs/support) for assistance.

## Related topics

For detailed information about finding a Cloud Billing document, such as an invoice, statement, or receipt, see [Get an invoice, statement, or payment receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice).

For more information on Cloud Billing best practices and billing resource management, refer to the [Cloud Billing Onboarding Checklist](https://docs.cloud.google.com/billing/docs/onboarding-checklist) article.

Other related topics:

  * [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [Create, modify, or close your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
  * [Split invoicing for agency model transactions](https://docs.cloud.google.com/billing/docs/how-to/split-invoice)
  * [Split charging cycles for self-serve (online) Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
