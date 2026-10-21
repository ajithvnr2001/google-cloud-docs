---
url: https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle/
title: Split charging cycles for online billing accounts \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:13.495504+00:00
---

# Split charging cycles for online billing accounts  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Split charging cycles for online billing accounts Stay organized with collections  Save and categorize content based on your preferences. 

To pay for the usage costs of some Google Cloud transactions, Google might configure your self-serve (online) Cloud Billing account to use two different charging cycles. A charging cycle represents _when_ you are charged for usage and can be either Postpay or Prepay. When split charging cycles apply, the Cloud Billing account is linked to two different Google payments accounts to separately manage payments for each [charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle).

## How split charging cycles work

As you use Google Cloud and other billing-eligible services, such as Google Maps Platform, Firebase, and Gemini API in AI Studio, your Cloud Billing account tracks all of the costs (charges and savings) incurred in all of the projects that are linked to the Cloud Billing account, then routes those costs to the appropriate _Google payments account_ (Postpay or Prepay) to be paid.

About _Postpay_ Google payments accounts | About _Prepay_ Google payments accounts  
---|---  
**Primary payments account** : All self-serve (online) Cloud Billing accounts are linked to a _Postpay_ payments account. With a _Postpay_ payments account, you **_pay later_** for the resources you consume during the billing cycle. The usage costs of eligible Google Cloud products and other services are routed to your _Postpay_ Google payments account, and are automatically charged based on your _Postpay_ billing cycle (for example, [ threshold billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#threshold-billing) or [ monthly billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle)). If there is an issue with your Postpay payments account, such as a delinquent account balance, a declined payment, or an invalid payment method, your _Cloud Billing account_ might be suspended until you resolve the issue. If your _Cloud Billing account_ is suspended, ALL services in _all_ of the [ projects that are linked to the _Cloud Billing account_](https://docs.cloud.google.com/billing/docs/how-to/view-linked) are stopped. This stoppage of service also affects services covered by prepaid credits. Learn how to [ resolve service disruptions due to the state of your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#resolve_limits). |  **Secondary payments account** : For certain users and Google products, a self-serve (online) Cloud Billing account might also require a _Prepay_ payments account. With a _Prepay_ payments account, you purchase credits to **_pay now_** before you can use any eligible resources. Your purchased credits are loaded into a separate _Prepay_ Google payments account. Your credits are used in near real time to pay for the usage costs of eligible services as they run. When your available credits are depleted, your services are stopped until you purchase more credits. This service stoppage only impacts your services that are paid for by the Prepay payments account. The overall billable status of your Cloud Billing account isn't affected. With a _Prepay_ payments account, you can enable _auto-reload_ to automatically purchase more credits whenever your balance falls below a value that you specify.  If your _Cloud Billing account_ is suspended for any reason, such as an issue on its linked _Postpay_ payments account, ALL services are stopped in _ALL_ of the [ projects that are linked to the _Cloud Billing account_](https://docs.cloud.google.com/billing/docs/how-to/view-linked), including any services that are paid for using Prepay credits.  
  
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

## Know when split charging cycles apply

During the [billing account creation process](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#create-new-billing-account), self-serve (online) Cloud Billing accounts are automatically configured with a _Postpay_ Google payments account.

In Google AI Studio, when you [set up billing for a project](https://ai.google.dev/gemini-api/docs/billing#setup-billing) and you select the Cloud Billing account to use to enable billing, you might be prompted to configure a _Prepay_ payments account and purchase credits. In these instances, split charging cycles apply.

For the selected self-serve (online) Cloud Billing account:

  * The _Prepay_ payments account is used to pay for your usage costs of Gemini API in AI Studio.
  * The _Postpay_ payments account is used to pay for the usage costs of all other Google Cloud products and other services you consume during the [billing cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle).



## Manage your Postpay and Prepay payments accounts

When split charging cycles apply, the Cloud Billing account is linked to two different Google payments accounts. Where you manage each payments account depends on the type, Postpay or Prepay:

_Postpay_ : managed in _Google Cloud console_ Billing pages | _Prepay_ : managed in _Google AI Studio_ Billing page  
---|---  
**Postpay** Google payments accounts that are linked to a self-serve, online Cloud Billing account are managed in the [ **Google Cloud console Billing**](https://console.cloud.google.com/billing/payment) pages. Here are a few of the payments account features that you can manage for a Postpay account:

  * View and update [ payment methods attached to the _Postpay_ account](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
  * View your [ account balance and assigned threshold billing amount](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#find-threshold-amount)
  * Make a [ manual payment or pay early](https://docs.cloud.google.com/billing/docs/how-to/manual-payment)
  * View the [ payments transactions for the _Postpay account_](https://docs.cloud.google.com/billing/docs/how-to/view-history)

|  **Prepay** Google payments accounts that are linked to a self-serve, online Cloud Billing account are managed in the [ **Google AI Studio Billing**](https://aistudio.google.com/billing) page. Here are a few of the payments account features that you can manage for a Prepay account:

  * View and update [ payment methods attached to the _Prepay_ account](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
  * View your [ credit balance and buy more credits](https://ai.google.dev/gemini-api/docs/billing#buy-credits)
  * Enable [ auto-reload to automate the purchase of credits](https://ai.google.dev/gemini-api/docs/billing#auto-reload)
  * View the [ payments transactions for the _Prepay account_](https://docs.cloud.google.com/billing/docs/how-to/view-history)

  
  
Alternatively, both types of Google payments accounts can be managed directly in the **Google payments center** , on the **Subscriptions and Services** page:

  1. Sign in to the [**Google payments center**](https://payments.google.com/payments/home).

**Tip** : If you have more than one _Google payments profile_ , the payments profile that you most recently viewed opens. To manage a different payments profile, select the payments profile from the drop-down menu at the top of the page.

  2. Select the **Subscriptions & services** tab.

The Subscriptions and Services page opens, where you can access the _Active_ and _Canceled_ Google Cloud accounts and other Google subscriptions that are associated with the Google payments profile that you are viewing.

  3. Locate the **_Google Cloud_** subscription card for the Google payments account that you want to access, and click **Manage**.

Each _Google Cloud_ subscription card represents a _Google payments account_ that is linked to a _Cloud Billing account_. You might have more than one Cloud Billing account that is associated with the _Google payments profile_ you are viewing, and each Cloud Billing account might be linked to a _Postpay_ and a _Prepay_ payments account. Each _Google Cloud_ subscription card includes the [billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id) of the linked Cloud Billing account to differentiate between multiple _Google Cloud_ subscription cards.

  4. From the _Subscriptions and services_ page for the Google payments account you are viewing, you can complete several tasks, such as:

     * View your _Postpay_ **account balance** or _Prepay_ **credit balance**.
     * [**Make a payment**](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) to a _Postpay_ account or [**Buy credits**](https://ai.google.dev/gemini-api/docs/billing#buy-credits) for a _Prepay_ account.
     * [**View transactions**](https://docs.cloud.google.com/billing/docs/how-to/view-history) for the _Postpay_ or _Prepay_ account.
     * [**Manage payment methods**](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) for the _Postpay_ or _Prepay_ account.
     * **Manage settings** for the _Postpay_ or _Prepay_ Google payments account.



## Make a payment to a Cloud Billing account

A Cloud Billing account is linked to one or more Google payments accounts to pay for your costs. Where and how you make a payment to a Cloud Billing account depends on which type of _Google payments account_ you are paying.

_Postpay_ : make payments in the _Cloud Billing console_ | _Prepay_ : buy credits in the _Google AI Studio_ Billing page  
---|---  
**Postpay** Google payments accounts that are linked to a self-serve, online Cloud Billing account are viewed and managed in the [ **Google Cloud console Billing**](https://console.cloud.google.com/billing/payment) pages. To make a manual payment to your **Postpay** payments account, in the **Google Cloud Billing console** , access the **Payment overview** page, then click **Make a payment** or **Pay early**. For more details about this process, see [ Make a manual payment or pay early](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) |  **Prepay** Google payments accounts that are linked to a self-serve, online Cloud Billing account are viewed and managed in the [ **Google AI Studio Billing**](https://aistudio.google.com/billing) page. To purchase credits for your **Prepay** payments account, access the **AI Studio Billing page** to [ buy credits](https://ai.google.dev/gemini-api/docs/billing#buy-credits). You can also configure [ auto-reload](https://ai.google.dev/gemini-api/docs/billing#auto-reload) to automatically purchase more credits whenever your credit balance falls below a value that you specify.  
  
## View your charges and costs for split charging cycles

Where you view Cloud Billing account charges and costs data can differ based on which type of Google payments account you are viewing.

### Charges

_Postpay_ : view charges in the _Cloud Billing console_ | _Prepay_ : view charges in the _Google AI Studio_ Billing page  
---|---  
**Postpay** Google payments accounts that are linked to a self-serve, online Cloud Billing account are viewed and managed in the [ **Google Cloud console Billing**](https://console.cloud.google.com/billing/payment) pages. To view the cost and payment history for a _Postpay_ Google payments account, view the [ **Transactions page**](https://docs.cloud.google.com/billing/docs/how-to/view-history) for the _Postpay account_. If your usage costs are subject to the [ Postpay with threshold billing](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#threshold-billing) charging cycle, you can be charged multiple times in the same month if your account balance reaches your assigned Cloud Billing payment threshold amount repeatedly over that time. In addition, you're charged on the first day of the next month for the balance of any additional costs that you accrue. |  **Prepay** Google payments accounts that are linked to a self-serve, online Cloud Billing account are viewed and managed in the [ **Google AI Studio Billing**](https://aistudio.google.com/billing) page. To view the cost and payment history for a _Prepay_ Google payments account, view the [ **Transactions page**](https://docs.cloud.google.com/billing/docs/how-to/view-history) for the _Prepay account_. If your usage costs for Gemini API services are subject to a [ Prepay charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#prepay-billing), the [ credits you purchase](https://ai.google.dev/gemini-api/docs/billing#buy-credits) are deducted in near real time based on your usage of the Gemini API in AI Studio. When your credit balance is depleted, your Gemini API services are stopped. If you've enabled the [ auto-reload feature](https://ai.google.dev/gemini-api/docs/billing#auto-reload) on your Prepay payments account, you are automatically charged for the amount of credits that you want added to your account when your balance falls below a value you specify.  
  
#### Delayed billing

Due to the complexity of our billing and processing systems for both Prepay and Postpay charging cycles, there might be delays in our ability to deduct from your prepaid credit balance or charge you as soon as your costs reach your billing thresholds.

  * For **Postpay with threshold billing** , this delay might cause the amount charged to exceed the payment threshold amount if the account accrues costs very quickly.
  * For **Prepay accounts with a positive credit balance** , this delay might cause excess usage charges that result in a negative credit balance in your AI Studio billing dashboard. If this happens, your service is paused, and your negative balance is deducted from your next credit purchase. To avoid a pause in your Gemini API service, we recommend setting up auto-reload to automatically purchase more credits when your balance falls below a threshold you specify. Learn more about [Prepay billing](https://ai.google.dev/gemini-api/docs/billing#prepay) and [auto-reload](https://ai.google.dev/gemini-api/docs/billing#auto-reload).



Also note that charges typically occur sooner than the usage and cost details are available to view in the various cost reports and dashboards. Typically, your cost details are available to view within a day, but can sometimes take more than 24 hours. Because of this difference in timing, you might notice charges on your Postpay or Prepay payments accounts occur before you can view the details of those charges in a cost report or billing dashboard. These system delays also impact budget alerts, anomaly detection, and billing data exported to BigQuery.

### Cost reports and dashboards

For all of the [projects that are linked to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked), all of the cost data that accrues in the Cloud Billing account is available to view and analyze in the various reports and dashboards in the Google Cloud console billing pages. This includes costs for Google Cloud, Google Maps Platform, Firebase, and Gemini API in AI Studio usage.

Report or Dashboard | Description  
---|---  
**Cost Reports** | Open the [ **Cost Reports page**](https://docs.cloud.google.com/billing/docs/how-to/reports) in the Google Cloud console to access a consolidated view of all costs accrued and paid for by the same _Cloud Billing account_ for all billing-eligible services, including Google Cloud, Google Maps Platform, Firebase, and Gemini API in AI Studio.  The report defaults to returning costs for all services and SKUs, grouped by _Service_ for the _Current month_ time range. You can customize your report views using many configurable [ settings and filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) to focus your cost analysis. To configure your cost report to show the granular details of your Gemini API in AI Studio costs, do the following:

  * [ **Group by:_SKU_**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) (or Date > SKU, or Month > SKU)
  * [ **Time range**](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range): whatever amount of time you want to analyze
  * [ **Services** filter](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-services): Select _Gemini API_ only

Using this configuration, your Cloud Billing cost report will return a cost line item for each Gemini API SKU you used that generated usage costs during the time range you selected.  
**Cost breakdown** | Use the [ **Cost breakdown report**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown) for an at-a-glance [waterfall chart](https://en.wikipedia.org/wiki/Waterfall_chart) of your costs and savings. For the selected [ date range and filters](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#configure-report), the Cost breakdown report shows your base usage cost (calculated from on-demand prices) and how discounts, credits, adjustments, and taxes affect the base cost to arrive at your cost total.  
**Cost table** | Use the [ **Cost table report**](https://docs.cloud.google.com/billing/docs/how-to/cost-table) to analyze and understand the costs that reconcile to your invoice or statement. The report gives you a detailed tabular view of your costs for the selected invoice (by Invoice month). A separate invoice is produced for each type of _Google payments account_. If your self-serve (online) Cloud Billing account has both a _Postpay_ and a _Prepay_ payments account, in the Cost table report, you will see two different [ invoices per month](https://docs.cloud.google.com/billing/docs/how-to/cost-table#time-range), one for the Postpay account, and one for the Prepay account.  
**Billing export** | If your Cloud Billing account is enabled to [ export billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), all of your cost data that is accrued in the Cloud Billing account will be exported to the assigned BigQuery dataset, including Gemini API in AI Studio usage costs.  
**FinOps hub**  
**Cost anomalies**  
**Budgets & alerts** | All of your cost data that is accrued in a Cloud Billing account, including your Gemini API in AI Studio usage costs, is available in the following cost monitoring and optimization pages in the Google Cloud console:

  * [**FinOps hub**](https://docs.cloud.google.com/billing/docs/how-to/finops-hub): Monitor and communicate your current savings, explore new recommended opportunities to optimize costs, and plan your optimization goals.
  * [**Cost anomalies**](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies): Monitor and manage unexpected costs across your Cloud Billing account's projects. Anomalies are spikes or deviations in usage costs that differ from your expected spend, when compared to historical spending patterns.
  * [**Budgets & alerts**](https://docs.cloud.google.com/billing/docs/how-to/budgets): Budgets let you track your accrued costs in a Cloud Billing account, compares actual costs against your planned costs, then triggers alerts to keep you informed about how your spend is tracking against your budget.

  
  
#### Delayed cost data

Google Cloud and billing-eligible products such as Google Maps Platform, Google AI Studio, and Firebase report usage data to Cloud Billing at varying intervals. Due to the complexity of our billing and processing systems, you might see a delay between your use of services, and the _usage and costs_ being available to view in Cloud Billing and other cost reports and billing dashboards. Typically, your cost details are available within a day, but can sometimes take more than 24 hours to appear.

## What's next

  * For more information about Prepay Google payments accounts and when they apply to Gemini API in AI Studio transactions, see [Learn more about Prepay](https://ai.google.dev/gemini-api/docs/billing#prepay).
  * For information about Cloud Billing accounts and charging cycles, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
