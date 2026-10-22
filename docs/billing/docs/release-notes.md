---
url: https://docs.cloud.google.com/billing/docs/release-notes/
title: Cloud Billing release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:10.720850+00:00
---

# Cloud Billing release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Resources ](https://docs.cloud.google.com/billing/docs/resources)



Send feedback 

#  Cloud Billing release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Billing. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/billing-release-notes.xml) directly. 

## October 13, 2026

Feature

**Spend cap budgets are now generally available for a limited set of services**

For [eligible services](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#eligible-services), you can configure a **spend cap budget** to automatically pause usage when your estimated spend exceeds the budget amount you set. You can manage spend cap budgets in the [Budgets page in the Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) and using the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap).

Spend caps are a cost control mechanism. A spend cap is enforced when usage costs exceed your budget target amount. When enforced, any new request to the eligible services, within the specified project, are paused and no further usage costs are accrued until the spend cap is lifted. You can manually lift an enforced spend cap, or wait until the start of the next month when the spend cap is automatically lifted.

Spend caps use _gross, estimated costs_ to trigger the alerts and caps, enforcing a cap much faster than the _actual costs_ are processed and appear on billing reports. Even though faster than reports, the enforcement of spend caps isn't instant and any cost overages are billed as normal.

**More information about spend cap budgets**

For managing spend cap budgets in the Google Cloud console, see:

  * [How spend cap budgets work to help you control spend](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#how-spend-cap-budgets-work)
  * [Limitations of spend cap budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#limitations)
  * [Configure a spend cap budget](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#configure-spend-cap)
  * [Lift an enforced spend cap](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#lift-spend-cap)



For managing spend cap budgets using the Cloud Billing Budget API, see:

  * [Using the Cloud Billing Budget API for spend cap budgets](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap)
  * [Spend cap budget concepts and limitations](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap#concepts-limitations)
  * [Create a spend cap budget](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap#create)
  * [Lift an enforced spend cap](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap#lift)
  * [Cloud Billing Budget API REST reference](https://docs.cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets)



## September 04, 2026

Change

**Introducing the Incentives page, for tracking spend-based milestone credits, RaMP, and other conditional incentives**

If you have a custom pricing contract, you might be enrolled in conditional incentives, where you earn credits or discounts for spending specific amounts on Google Cloud.

The [**Incentives page**](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker) replaces the [_Spend-based Milestones tab_](https://docs.cloud.google.com/billing/docs/release-notes#July_22_2024) that was located in the _Credits_ page. The Incentives page provides a consolidated and enhanced experience for tracking your progress towards conditional incentives, including spend-based milestone credits and Rapid Migration & Modernization Program (RaMP) credits and discounts.

Learn more about [tracking conditional incentives](https://docs.cloud.google.com/billing/docs/how-to/incentives-program-tracker).

## August 07, 2026

Feature

**New filter and group-by option available in Cloud Billing Reports**

In **Billing Reports** , Cloud Billing has added the **Originating products** [_filter_](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-orig-products) and [_Group by_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-orig-product) to provide additional options that let you analyze and understand your costs. _Originating products_ are Google Cloud products that cause usage in another product. For example, Gemini Enterprise is an originating product when it causes usage in the Gemini Enterprise app.

To help you **track and analyze your _AI spend_** , the _Originating products_ dimension is used in the following ways:

  * You can use the _Originating products_ filter and group by option to configure your Cloud Billing report to track and analyze your [Gemini Enterprise subscription and consumption costs](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).

  * The _Originating products_ dimension supports a new [_preset report_](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views) for quick report configuration, called [Gemini Enterprise costs by SKU](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs#preset-report).

  * When you are viewing your costs in the Gemini Enterprise console, on the _Gemini Enterprise > Usage & Spending_ page, the _Originating products_ dimension supports the functionality of the costs displayed on the [Gemini Enterprise Billing tab](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).




For more information, see the following resources:

  * [Learn how to view Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs)
  * [Learn more about analyzing billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [Learn how to view Gemini Enterprise costs in the Gemini Enterprise console](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs)



## July 27, 2026

Feature

**Spend cap budgets are now available for a limited set of services (Preview)**

Available in [Preview](https://cloud.google.com/products#product-launch-stages) for [eligible services](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#eligible-services), you can now configure a [**spend cap budget**](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) to automatically pause usage when your spend exceeds the budget amount you set.

Spend caps are a cost control mechanism. A spend cap is enforced when usage costs exceed your budget target amount. When enforced, any new request to the eligible services, within the specified project, are paused and no further usage costs are accrued until you manually lift the spend cap.

Spend caps typically use _estimated costs_ to trigger the alerts and caps, enforcing a cap much faster than the _actual costs_ are processed and appear on billing reports. Even though faster than reports, the enforcement of spend caps isn't instant and any cost overages are billed as normal.

For more information about spend cap budgets, see:

  * [How spend cap budgets work to help you control spend](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#how-spend-cap-budgets-work)
  * [Configure a spend cap budget](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#configure-spend-cap)
  * [Lift an enforced spend cap](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#lift-spend-cap)
  * [Limitations of spend cap budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps#limitations)



## July 24, 2026

Feature

**Early signals for AI workloads**

For AI workloads (such as Gemini API and Vertex AI), you can now view early anomalies. Early anomalies use near real-time cost estimates to provide daily, service-level insights before finalized billing occurs. You can view these alerts on the **By service (Early signals)** tab on the Anomalies dashboard in the Google Cloud console. User-configured thresholds do not apply to early anomalies.

For more information, see [View early anomalies for AI workloads](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies#view-early-anomalies).

## July 10, 2026

Feature

**Payments documents for invoiced billing accounts available on Payment status page**

For [Cloud Billing accounts that are paid by invoice](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), access to your payments documents, such as invoices and credit memos, is now available in the Cloud Billing console in the **Payment status** page.

The **Payment status** page replaces the **Invoices** page. Self-service (online) Cloud Billing accounts will continue to access Payments documents on the **Invoices** page.

The **Payment status** page provides a real-time and customizable view of your financial standing with your Cloud Billing account. The Payment status page is based on the [Google payments **Statement of account**](https://support.google.com/paymentscenter/answer/7520537) page, with your payments documents filtered by the _Google payments account_ that is linked to the Cloud Billing account that you are viewing.

For more information about payments documents, see:

  * [Get a Cloud Billing document such as an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [Google payments Statement of account](https://support.google.com/paymentscenter/answer/7520537)



## June 22, 2026

Feature

**Resource-based CUD recommendations available for Compute Engine GPUs, Local SSD disks, and OS licenses**

Resource-based committed use discount (CUD) recommendations are generally available (GA) for GPUs, Local SSD disks, and premium operating system (OS) licenses.

CUD recommendations provide insight into any additional commitments that you can purchase to optimize the costs of the resources that you run. You can use these recommendations and purchase commitments for resource usage that isn't covered by commitments and is being charged at list prices. Google Cloud analyzes your compute instance spending trends with and without a commitment and generates CUD recommendations on a monthly basis.

For more information about how CUD recommendations are generated, what resource types are supported, and how to use recommendations to purchase commitments, see [Get recommendations for committed use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds-recommender).

## June 17, 2026

Feature

**CUD dashboard redesign available (preview)**

The redesigned CUD dashboard is available in the Billing section of the Google Cloud console. It provides a consolidated view of all your resource-based and spend-based CUDs in a single place. The new design improves usability and scalability, helping you find information faster.

For more information, see [View your commitments](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview).

## June 15, 2026

Feature

**New filters and group-by options available in Cloud Billing Reports**

Cloud Billing has added two **filters** to the **Billing Reports** page to help you analyze and understand your costs:

  * **Products** : Google Cloud [Products](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-products) consist of a group of SKUs (potentially from more than one [Google Cloud _Service_](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-services)) that work together and are sold as a single service, sometimes referred to as a _logical_ product family or a subscription service. Examples include Gemini Enterprise and Firebase App Hosting.

  * **Originating services** : An [Originating service](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-orig-services) is a Google Cloud service that causes usage in another service. For example, Google Kubernetes Engine (GKE) can cause usage in Compute Engine. In this use case, when you are viewing the Compute Engine usage and costs, GKE is an originating service when it causes usage in Compute Engine.




You can also [**Group by**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) the new filters, to summarize your costs by the dimension you select.

  * **Product** : When you [group by _Product_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-product), the Report shows your costs and savings summarized by Product.
  * **Originating service > Service**: When you [group by _Originating service > Service_](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-orig-service), the Report shows your costs and savings summarized by Originating service. In the **report table** , you can expand each row for an _Originating service_ to see your costs summarized by each _Service_ that is associated with the _Originating service_.



Learn more about [analyzing billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports).

Learn how to [view Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).

## June 10, 2026

Feature

**Multi-project access to Cloud Billing cost views available in Preview**

In Cloud Billing accounts, multi-project access to usage costs lets project owners, solution owners, developers, and other non-billing admins see cost data for all of their authorized projects in a single view in the Cloud Billing console.

The multi-project view uses a combination of Cloud Billing account permissions and Google Cloud project permissions that let Cloud Billing administrators and organization administrators jointly control access to project-level cost data.

Using project-scoped Cloud Billing account permissions, Cloud Billing administrators can control which solution owners can view aggregated cost data in the Cloud Billing console.

  * Learn more about [cost management for project owners](https://docs.cloud.google.com/billing/docs/how-to/project-owners/overview).
  * Learn how to [set up multi-project access to costs views](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access).



## June 08, 2026

Feature

**FOCUS billing data export to BigQuery available in Preview**

[Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) now offers a FOCUS billing data export available in [Preview](https://cloud.google.com/products#product-launch-stages). The [_FinOps Open Cost and Usage Specification_ (FOCUS)](https://focus.finops.org/what-is-focus/) is an open specification that defines clear requirements for technology billing data generators to produce consistent cost and usage datasets. The Google Cloud billing data export using the [FOCUS specifications](https://focus.finops.org/focus-specification/) includes FOCUS columns up to [FOCUS version 1.2](https://focus.finops.org/focus-specification/v1-2/).

For more information about the FOCUS billing data export to BigQuery, refer to the following documentation:

  * [Set up FOCUS Cloud Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-focus-setup)
  * [Structure of the FOCUS data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export)
  * [FOCUS conformance report](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/focus-export#conformance-report)
  * [Query examples for FOCUS use cases](https://focus.finops.org/use-cases/?version=v1-2)



## June 01, 2026

Feature

**CUD Analysis is Generally Available**

CUD Analysis has reached general availability (GA). This tool supports the new spend-based CUD model and provides a unified interface for customers to examine both spend-based and resource-based CUDs. It offers a consolidated view of Compute resources including the benefits of both resource-based and spend-based CUDs.

You can use this tool to do the following:

  * **Understand savings** : Understand the financial impact of your commitments.
  * **Track key metrics** : Track how effectively your commitments are being used.
  * **Download data** : Download a CSV file of your daily usage for offline analysis and reporting.



For more information, see [Analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).

## April 27, 2026

Feature

**The AI Cost Summary Agent is now available in Preview**

You can now use the AI Cost Summary Agent to analyze your AI costs and gain critical insights into your AI-related spend. The agent analyzes spending related to Gemini usage, including Gemini API and Vertex AI.

This feature is available as a widget on the **Billing Overview** page for your Cloud Billing account.

For more information, see [Analyze your AI spend with the AI Cost Summary Agent](https://docs.cloud.google.com/billing/docs/how-to/gemini/ai-cost-summary).

## April 20, 2026

Feature

**GKE workload recommenders now available in the FinOps hub**

You can now view recommendations for right-sizing overprovisioned workloads and optimizing underprovisioned workloads for Google Kubernetes Engine (GKE) clusters directly in the FinOps hub.

For more information, see [Optimize workload resource utilization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-workload-resource-utilization).

## March 30, 2026

Feature

**Scenario modeling for CUD recommendations is generally available**

Scenario modeling for committed use discount (CUD) recommendations is now generally available (GA). You can simulate scenarios for both spend-based and resource-based CUDs, and customize recommendations to purchase a commitment that maximizes your savings.

For more information, see [Simulate scenarios for CUDs savings](https://docs.cloud.google.com/docs/cuds-recommender#simulate-scenarios).

## March 23, 2026

Change

**Billing account permissions now streamline access to Google payments profiles and payments accounts**

We've launched a billing IAM permissions update that simplifies and streamlines Cloud Billing account access to the associated [Google payments profiles and accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account), for users who have the `billing.accounts.updatePaymentInfo` permission on their Cloud Billing account.

**Prior to this update** : _While working in the Cloud Billing console_ , to access and edit the associated Google payments profile and account information, all Cloud Billing account users **needed _two_ sets of permissions**:

  * Identity and Access Management (IAM) [permissions on the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/billing-access) to access and manage the billing account.
  * Edit or Admin [access permissions on the associated Google payments profile](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions) in order to add and edit payment methods, make a manual payment, and update payments profile info such as the business name, address, tax info, and payments account settings.



**After this permissions update** : Cloud Billing account users with the `billing.accounts.updatePaymentInfo` permission on the billing account can access and edit Google payments profile and account information directly from the Cloud Billing console, without needing additional permissions on the payments profile itself. This includes users with the [Billing Account Administrator role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) (`roles/billing.admin`) and those granted this permission via a [custom role](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information).

Note that this permissions update applies only to Cloud Billing accounts associated with an [Organization (or Business)](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) Google payments profile type. You can verify your account type on the [Payment settings](https://console.cloud.google.com/billing/profile) page in the Cloud Billing console.

With the `billing.accounts.updatePaymentInfo` permission on the billing account, users can do the following:

  * [View payments history](https://docs.cloud.google.com/billing/docs/how-to/view-history) and [documents](https://docs.cloud.google.com/billing/docs/how-to/get-invoice) related to the associated Google payments profile.
  * [Add and edit payment methods](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) on a self-serve (online) billing account.
  * [Make a manual payment](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) to a self-serve (online) billing account.
  * [Update payments profile info](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account) such as the business name, address, tax info, and payments account settings.



Billing account users with the `billing.accounts.updatePaymentInfo` permission won't have the _Manage users_ or _Admin with all permissions_ level of access on the Google payments profile. To _fully manage_ a payments profile and gain [_Manage users_ and _Admin_ permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions), billing account users still require additional [_Google payments user permissions_](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) granted on the associated payments profile.

## January 21, 2026

Feature

**CUD recommendations support more machine types**

Resource-based CUD recommendations for cores and RAM now support additional machine series. For a complete list, see [Resource-based CUDs supported by recommendations](https://docs.cloud.google.com/docs/cuds-recommender#supported-resource-types-recommendation).

You can access these recommendations using the [FinOps hub user interface](https://console.cloud.google.com/billing/optimize), programmatically using the [Recommender API](https://docs.cloud.google.com/recommender/docs/apis), or when you [export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## December 16, 2025

Feature

**View granular cost data from Pub/Sub snapshot, subscription, and topic usage in Cloud Billing exports to BigQuery**

You can now view granular Pub/Sub cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed snapshot, subscription, and topic usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## October 30, 2025

Feature

**Anomaly Detection is generally available**

View and manage cost spikes that deviate from your typical spend patterns using the Anomalies dashboard, which is [generally available](https://cloud.google.com/products#product-launch-stages). Each anomaly includes a detailed root cause analysis that identifies the top services, regions, and SKUs that contributed to the spike.

With this launch, we've added the following features to Anomaly Detection:

  * Auto-generated anomaly thresholds that update daily based on your usage patterns.
  * Deviation percentage as a new threshold for you to configure for your anomalies.
  * Email alerts automatically set up for Billing administrators to help you proactively manage your costs.



[Learn more about using Anomaly detection to manage costs](https://cloud.google.com/billing/docs/how-to/manage-anomalies).

## August 08, 2025

Feature

**Personalized saved reports are available in cost Reports.**

For customers who have enabled [Gemini Cloud Assist in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview), your custom saved reports that you open frequently now appear in the reports carousel, for quick access. Previously, the reports carousel only provided access to Google-created preset reports.

For more information, see the following topics in the **Reports** dcoumentation:

  * [Save and share report views](https://docs.cloud.google.com/billing/docs/how-to/reports#saving-views)
  * [Use preset reports for quick configuration](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views)



## July 16, 2025

Feature

**Spend-based committed use discount (CUD) metadata export to BigQuery (public preview)**

You can now access spend-based CUD metadata programmatically through a BigQuery export. This data provides a comprehensive, daily snapshot of spend-based CUDs, which you can join with other billing data exports for improved CUD reporting and management. 

[Learn more about the CUD metadata export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/cud-export).

## July 07, 2025

Feature

**Tags data for _regional_ Secret Manager secret usage is available in both the [Standard usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [Detailed usage cost export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

Tags for Global secrets have been available since [August 8, 2024](https://docs.cloud.google.com/billing/docs/release-notes#August_08_2024). With this update, you can now tag _Regional secrets_ as well.

To learn more about Tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

## June 27, 2025

Change

**New fields added to Cloud Billing data exports to BigQuery**

To prepare for expanding the spend-based committed use discounts (CUD)s program, we added new data fields to the schema for Cloud Billing standard and detailed data exports to BigQuery. These new fields add more information about the prices charged for your Google Cloud usage and consumption models.

To learn more, see [Billing data and SKU updates for spend-based CUDs](https://docs.cloud.google.com/billing/docs/resources/multiprice-cuds).

## June 24, 2025

Feature

**New, enhanced forecasting model for increased accuracy in cost reports**

Cloud Billing forecasts now better account for seasonality trends, data irregularities, and missing data, using an enhanced forecasting model that leverages AI to factor in various scenarios, such as the following:

  * Intelligent handling of transient effects caused by known business events - for example, a new workload migration causing a usage spike.
  * Deeper understanding of seasonality - for example, various recurring patterns, such as daily, weekly and monthly cycles in your cloud spend; or for retailers, increases in usage during holiday seasons.
  * Adapting to trends to remain relevant in changing environments - for example, new AI spend.



These enhancements, powered by our new machine learning engine, translate to increased forecasting accuracy. By capturing complex trends, multiple seasonalities, and handling data anomalies more intelligently, you'll see a marked improvement in the precision of your cost forecasts.

For more information about the forecasted costs in reports, see [View you forecasted costs](https://docs.cloud.google.com/billing/docs/how-to/reports#cost-forecast).

## April 29, 2025

Feature

**Find and eliminate waste using FinOps hub 2.0 with Gemini Cloud Assist (preview)**

FinOps hub 2.0 adds a new dashboard, [**Utilization insights**](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights), designed to help you quickly identify and reduce cloud waste to get the most value from Google Cloud. You can do the following with FinOps hub's Utilization insights dashboard:

  * Assess estimated costs from underutilized resources (for example, idle, overprovisioned, underprovisioned and suboptimal configurations).
  * Use the visual [_Waste map_](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights#waste-map) to find the top waste drivers by projects and waste category, helping you focus your optimization efforts.
  * Leverage [data-driven recommendations](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights#resource-recommendations-table) to optimize [key services](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights#supported-services) (Compute Engine, Kubernetes Engine (GKE), Cloud SQL, and Cloud Run) and App Hub applications.



Use [**Gemini Cloud Assist in FinOps hub**](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview#ai-assistance-finops-hub) to save time and simplify collaboration. If you have [enabled Gemini Cloud Assist in Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/set-up-gemini), Gemini generates [summaries of top wasted usage insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights#gemini-insights) and [drafts email reports of utilization insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights#gemini-summarize-and-send) that you can share with your engineering teams for quicker remediation. 

For more information about the **FinOps hub Utilization insights** dashboard, see:

  * [Review utilization and wasted usage insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights)



For more information about **Gemini Cloud Assist features in FinOps hub** , see:

  * [Gemini Cloud Assist in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview)
  * [Set up Gemini Cloud Assist in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/set-up-gemini)



Feature

App Hub applications are now integrated with billing reports and the FinOps hub, to let you analyze costs by application. This integration provides detailed cost analysis for your specific applications, so FinOps and DevOps can see the cost of their applications and get recommendations on how to optimize their cloud efficiency.

  * In cost [Reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can configure your report to [Group by](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) Application, or [filter on Applications](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-application).
  * In the [Cost table](https://docs.cloud.google.com/billing/docs/how-to/cost-table) report, you can [filter on Applications](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filters).
  * In the [Cost breakdown](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown) report, you can [filter on Applications](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#filters).
  * In the FinOps hub [Utilization insights](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights) dashboard, you can view insights by [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) Application, to see the estimated costs of potentially wasted usage, and find recommendations to reduce waste and optimize your costs.



## April 23, 2025

Feature

**Cloud Billing supports Dark theme in the Google Cloud console (in preview)**

Dark theme is now available in the Billing section of the Google Cloud console (preview). To enable the Dark theme, in the Google Cloud console, click **Settings > Preferences > Appearance**. Choose **Dark** theme and click **Save**.

## March 13, 2025

Change

**Improved consistency in resource-based committed use discount (CUD) string names across experiences.**

We have improved consistency by standardizing CUD string names across the various experiences. This update helps provide a seamless experience in resource-based CUD purchase flows, recommendations, analysis, and the FinOps hub.

## February 03, 2025

Change

**Google Cloud Marketplace now uses the agency model for marketplace services for UK, FR, and DE customers.**

As part of this change, customers will receive separate invoices for Google Cloud and third-party vendor transactions in the Cloud Marketplace.

For more information, see [Split invoicing for agency model transactions](https://docs.cloud.google.com/billing/docs/how-to/split-invoice) and [Marketplace Agency Account Migration FAQ](https://support.google.com/cloud/answer/13855075).

## January 29, 2025

Feature

**Tags data for BigTable instances is available in both the[ _Standard usage cost_ export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [_Detailed usage cost_ export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)**.

To learn more about Tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see more [about tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

## December 18, 2024

Feature

**Simulate scenarios in FinOps hub to maximize your savings from resource-based CUDs**

In the FinOps hub, we added support for resource-based CUD recommendations as a starting point to simulate various usage scenarios, and customize the recommendation to purchase a CUD that maximizes your savings.

[Learn about simulating scenarios for resource-based CUDs](https://docs.cloud.google.com/docs/cuds-recommender#simulate-scenarios).

## September 30, 2024

Feature

**View and manage unexpected costs with Anomaly Detection (in preview)**

You can now view and manage cost spikes that deviate from your historical spend patterns using the Anomalies dashboard (preview). Each anomaly comes with a detailed root cause analysis that identifies the top services, regions, and SKUs that contributed to the spike.

[Learn more about using Anomaly Detection to manage costs](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies).

## September 27, 2024

Feature

**Avoid charges for underutilized Compute Engine reservations in the FinOps hub**

You can now get recommendations to modify or delete your underutilized, on-demand reservations for Compute Engine resources when you haven't consumed your specified threshold of resources for at least 7 days.

[Learn about reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview)   
[View and apply underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations)

## September 26, 2024

Feature

**Use Gemini AI assistant to find or create Billing Reports (preview)**

[Gemini Cloud Assist in Cloud Billing **Reports**](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview) provides FinOps-focused AI assistance to create the cost reports you need to analyze your cost trends and to summarize key insights from the cost reports.

Gemini Cloud Assist in Cloud Billing Reports helps you to:

  * [Use saved reports](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview#saved-reports): Quickly access existing reports to analyze your spending.
  * [Create new reports](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview#gemini-ai-reports): Configure custom reports with AI assistance to get the exact data you need.
  * [Summarize reports](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview#report-summaries): Get AI-powered summaries of your reports to quickly understand key cost trends and insights.



[Enable the Gemini for Google Cloud API](https://docs.cloud.google.com/billing/docs/how-to/gemini/set-up-gemini) in a project to turn on Gemini Cloud Assist in Cloud Billing Reports.

For more information about Gemini Cloud Assist features in Cloud Billing Reports, see:

  * [Gemini Cloud Assist in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview)
  * [Set up Gemini Cloud Assist in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/set-up-gemini)
  * [Analyze billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)



## August 13, 2024

Feature

**The _Carbon footprint dashboard_ in the FinOps hub now includes market-based emissions data (preview)**

Scope 2 market-based emissions data (preview) for the Carbon footprint dashboard are now available in the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub). The market-based emissions metric represents purchased electricity, incorporating Google's annual renewable energy purchases. You can use the data in the Carbon footprint dashboard to optimize your cloud spend and reduce your carbon impact.

  * To learn more about the methodology and the difference between location-based and market-based emission metrics, see the [carbon footprint documentation](https://docs.cloud.google.com/carbon-footprint/docs/methodology#market-based-allocation).

  * [Learn more about the FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).




## August 08, 2024

Feature

**Tags data for Secret Manager secret usage is available in both the[ _Standard usage cost export_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [_Detailed usage cost export_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

To learn more about Tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

Feature

**View granular cost data from Secret Manager secret usage in Cloud Billing exports to BigQuery**

You can now view granular Secret Manager secret cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed log bucket usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## July 22, 2024

Feature

**Track credits for your spend-based milestone credit programs (contract pricing)**

If you have a custom pricing contract, you might be enrolled in _spend-based milestone credit programs_ , where you earn promotional credits for spending specific amounts on Google Cloud.

In the Google Cloud console, you can now track the promotional credits for your spend-based milestone programs. The promotional credits that you receive act as a payment method, and are automatically applied to your costs.

[Learn about tracking spend-based milestone credits](https://docs.cloud.google.com/billing/docs/how-to/spend-milestone-credits).

## July 10, 2024

Feature

**You can now view granular AlloyDB for PostgreSQL usage in the Cloud Billing Detailed export to BigQuery**

You can now view granular **AlloyDB for PostgreSQL** _cluster_ , _instance_ , and _backup data_ in the Google Cloud Billing detailed export. Use the `resource.global_name` and `resource.name` fields in the export to view and filter your detailed AlloyDB cluster, instance, and backup usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

Feature

**Tags data for AlloyDB for PostgreSQL cluster, instance, and backup usage is available in both the[ _Standard usage cost export_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [_Detailed usage cost export_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

To learn more about Tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see [about tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

## July 02, 2024

Feature

**Simulate scenarios in FinOps hub to maximize your savings from spend-based CUDs**

In the FinOps hub, you can now use a spend-based CUD recommendation as a starting point to simulate various usage scenarios, and customize the recommendation to purchase a CUD that maximizes your savings.

[Learn about simulating scenarios for spend-based CUDs](https://docs.cloud.google.com/docs/cuds-recommender#simulate-scenarios).

## July 01, 2024

Feature

**View your Carbon Footprint in the FinOps hub**

In the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub#carbon-footprint-dashboard), you can now view the estimated greenhouse gas emissions for your Google Cloud usage by visiting the Carbon Footprint dashboard. 

[Learn about Carbon Footprint data](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data).

## June 24, 2024

Feature

**Avoid getting charged for idle Compute Engine reservations in the FinOps hub**

You can now get recommendations to modify or delete your idle, on-demand reservations for Compute Engine resources when you haven't consumed any resources for at least 7 days.

[Learn about idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/idle-reservation-recommendations-overview).

## June 04, 2024

Feature

**You can now view granular cost data for more Google Cloud services**

  * You can now view granular Cloud Logging log bucket cost data in the Google Cloud Billing detailed export. Use the `resource.global_name` field in the export to view and filter your detailed log bucket usage.
  * You can now view granular Managed Microsoft Active Directory cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed domain usage.
  * You can now view granular Dataproc Metastore cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed service usage.
  * You can now view granular Cloud Deploy cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed delivery pipeline usage.
  * You can now view granular Cloud Data Fusion cost data in the Google Cloud Billing detailed export. Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed instance usage.



[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## May 17, 2024

Deprecated

**The Cost Estimation API is deprecated**

To get estimates for your planned Google Cloud workloads, use the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator).

## May 16, 2024

Feature

**Generate a SQL query to BigQuery from your Cloud Billing Reports (in preview)**

In the cloud console, on the Billing **Reports** page, you use the [report settings and filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) to refine the data returned to your report. If you have enabled [**Cloud Billing data export to BigQuery**](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), you can analyze your [exported billing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables) using SQL queries. In Billing Reports, you can now click a button to [**generate a SQL query**](https://docs.cloud.google.com/billing/docs/how-to/reports#generate-query) in BigQuery that is configured to use the equivalent Billing Report settings and filters to query your exported billing data. When run against your exported billing data, the generated query returns the _equivalent results_ in BigQuery as the results in the Billing Report.

  * [Learn more about Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [Learn more about Billing data export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [Learn more about generating a SQL query from a billing report](https://docs.cloud.google.com/billing/docs/how-to/reports#generate-query)



## May 15, 2024

Change

Commitment recommendations in the **FinOps hub** now include a **Recommended quantity** column, so you can see more information about recommendations at a glance.

[Learn more about using the FinOps hub to optimize your costs](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).

## May 06, 2024

Feature

**Download committed use discount data as a CSV file**

You can now download data about all your committed use discounts (CUD) as a flat comma-separated value (CSV) file. The CSV file includes the subscription ID for each commitment, which you can use join your CUDs data to your usage data in the BigQuery export.

[Learn about downloading your CUDs data](https://docs.cloud.google.com/billing/docs/how-to/cuds-list-overview#download_csv).

## April 05, 2024

Feature

**The Cloud Billing FinOps hub is now Generally Available**

Use the FinOps hub to monitor and share your current savings, explore recommended opportunities to optimize costs, and plan your optimization goals. The FinOps hub dashboard generates recommendations based on historical usage, including recent usage and current commitments, and helps you gauge how well you're using Google Cloud tools to monitor and save costs.

[Learn about using FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).

## March 13, 2024

Feature

**You can now view granular Memorystore for Redis usage in the Cloud Billing Detailed export to BigQuery**

You can now view granular Memorystore for Redis cost data in the Google Cloud Billing detailed export. Use the `resource.global_name` and `resource.name` fields in the export to view and filter your detailed Memorystore for Redis usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

Feature

**You can now view granular Bigtable usage in the Cloud Billing Detailed export to BigQuery**

You can now view granular Bigtable instance cost data in the Google Cloud Billing detailed export. Use the `resource.global_name` field in the export to view and filter your detailed Bigtable instance usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## March 11, 2024

Feature

**Tags data for Google Cloud Storage buckets is available in both the[ _Standard usage cost_ export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [_Detailed usage cost_ export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).**

To learn more about Tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see more [about tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

## March 07, 2024

Feature

**Create your first budget with one click**

You can now create your first budget and receive budget alerts in one step using the **Create a budget alert** panel on the **Billing Overview** page. The tool shows you recommended budget amounts based on your usage patterns, and you will receive alerts when your actual spend reaches 50%, 75%, 100%, and 150% of your selected budget. You can later edit these settings in the **Manage budgets and alerts** section.

[Learn more about budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets).

## February 22, 2024

Change

Between **February 13, 2024** and **February 22, 2024** , some SKU IDs for your support subscriptions have changed. Use the following table to check whether you're affected by this change. If you have reports or BigQuery queries that depend on these IDs, edit them to use the new SKU IDs.

**Notes** : 

  * The SKU descriptions remain unchanged.
  * There's no change to billing or invoicing.

Subscription  | Legacy SKU IDs  | New SKU IDs   
---|---|---  
Premium  | Base Tier 1: F08D-670F-E528  Base Tier 2: 3ADC-4232-8F2F  Base Tier 3: 768B-9B76-8BFA  Variable: E4F5-0256-E0EE  | Base Tier 1: 5D14-41DF-B7BF  Base Tier 2: A73A-2FBD-A226  Base Tier 3: 7EFE-705D-1818  Variable: 5467-9D2D-5B98   
TAM  | Additional Coverage:  Included: 39DA-470F-1873  Additional Coverage:  Tier 1: 1D0C-C18F-A3E9  Tier 2: A4ED-26C4-BE0A  Tier 3: 7625-C72D-58B1  | Additional Coverage:  Included: FECC-20EE-2595  Additional Coverage:  Tier 1: 164C-4F75-934A  Tier 2: C9E4-CC90-085B  Tier 3: 0401-A11E-7A40   
Enhanced |  Base: D61B-E147-B8A6  Variable: 8D85-10F1-28B3  |  Base: 7F2E-344B-FBDD Variable: 0D7A-4FBF-FA55  
Gold |  Base: 118A-4BF5-51E1  |  Base: 0AD0-476B-879E  
Silver |  Base: 5D8F-0D17-AAA2  |  Base: F5D2-4995-B3D7  
  
[Learn about reports that you can use to analyze your costs](https://docs.cloud.google.com/billing/docs/reports).

## February 20, 2024

Change

**US-based billing accounts only** : In August 2023, Google Cloud Marketplace transitioned to the Agency model for marketplace services for US partners and US customers. As part of this change, the remittance information has changed on your Google Cloud invoices and in the Google Cloud console.

As part of this change, you can see the following information in your Cloud Billing tools:

  * [In the Cost Table report, use the **Seller Name** and **Transaction type** columns](https://docs.cloud.google.com/billing/docs/how-to/cost-table).
  * [In the Standard data export to BigQuery, use the `seller_name` and `transaction_type` columns](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#:%7E:text=June%2029%2C%202023.-,transaction_type,-String).



## February 13, 2024

Feature

**View granular cost data from Cloud Storage usage in Cloud Billing exports to BigQuery**

You can now view granular Cloud Storage bucket-level cost data in the Cloud Billing Detailed cost export. Use the `resource.global_name` field in the export to view and filter your detailed Cloud Storage bucket usage.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## January 26, 2024

Feature

**Recommendations for Compute Engine Flexible committed use discounts are now Generally Available**

Flexible CUDs add flexibility to your spending capabilities by eliminating the need to restrict your commitments to a single project, region, or machine series. Flexible CUDs recommendations in the FinOps Hub help you optimize costs by analyzing your spending trends and existing commitments to suggest purchase amounts for Flexible CUDs.

  * [Learn more about Flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based)
  * [Learn more about the FinOps Hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub)



## January 23, 2024

Feature

**Subscription IDs for your committed use discounts are now available in the Detailed cost data export**

**Note** : The new Detailed cost data export column has started rolling out to customers. You might not see this column in your BigQuery dataset until the rollout is complete.

You can now view a subscription ID associated with your resource-based and spend based Committed Use Discount (CUD) fees. This enables you to connect CUD fees to the corresponding CUD (subscription instance) to improve traceability of costs and savings calculations. Use the `subscription.instance_id` column in the Detailed cost data export to see your subscription ID.

  * [Learn about exporting your billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)



## October 23, 2023

Feature

**Control access to single-project budgets**

If you are a billing account-level user and are creating a budget for a single project, you can now prevent project users such as Project Owners and Project Editors from making changes to the budget. This prevents inadvertent changes to budgets that you might be tracking at the Cloud Billing account level.

[Learn more about creating Google Cloud budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets).

Feature

**Budgets for project users is now Generally Available**

Project users such as Project Owners, Project Editors, and Project Viewers in Google Cloud can now create budgets and stay on top of their cloud costs, without needing additional permissions to access Cloud Billing accounts. **Budgets for project users** enables project users to take ownership of their costs, plan for the spend in the projects that they own, and proactively manage cost exceptions.

You can now assign custom roles to users who can create, modify and delete single-project budgets for the projects they have access to.

Project users can use the Google Cloud console or the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview) to manage budgets for projects. 

  * [Take a 10-minute tutorial to get started with budgets for project users](https://console.cloud.google.com/?walkthrough_tutorial_id=billing--billing_budgets_for_projects)
  * [View the documentation to learn more about Google Cloud budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets)



## October 19, 2023

Feature

**View granular cost data from Dataflow usage in Cloud Billing exports to BigQuery**

You can now view granular Dataflow cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Use the `resource.name` or `resource.global_name` field in the export to view and filter your detailed Dataflow usage.

[Review the schema of the Detailed cost data export.](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

**View granular cost data from BigQuery usage in Cloud Billing exports to BigQuery**

View granular cost data from BigQuery in Cloud Billing exports to BigQuery You can now view granular BigQuery cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Use the `resource.name` or `resource.global_name` field in the export to view and filter your BigQuery Dataset and Jobs costs.

[Review the schema of the Detailed cost data export.](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

## August 31, 2023

Feature

You can now monitor and share your current savings, explore new recommended opportunities to optimize costs, and plan your optimization goals with the new FinOps Hub (Preview). The FinOps Hub dashboard generates recommendations based on historical usage metrics, including recent usage and current commitments, and helps you gauge how well you're using Google Cloud tools to monitor and save costs.

[Learn more about the FinOps Hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).

## August 22, 2023

Feature

**Budgets for project users now available (in preview)**

Now project users in Google Cloud can [create budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget) and stay on top of their cloud spend, without needing additional [permissions](https://docs.cloud.google.com/billing/docs/how-to/budgets#permissions_required_to_manage_budgets) to access Cloud Billing accounts. **Budgets for project users** enables engineers to take ownership of their costs, plan for the spend in the projects that they own, and proactively manage cost exceptions.

Project Owners, Project Editors, and Project Viewers can [view budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets) that are scoped to individual projects. Project Owners and Editors can also [create](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget), [modify and delete](https://docs.cloud.google.com/billing/docs/how-to/budgets#edit-or-delete-budget) single-project budgets for the projects they have access to. 

A new [email notification option](https://docs.cloud.google.com/billing/docs/how-to/budgets#email-notifications) is available for budgets scoped to a single project: _Email alerts to project owners_. All other [notification options](https://docs.cloud.google.com/billing/docs/how-to/budgets#manage-notifications) are also available for single-project budgets.

Project users can use the Google Cloud console or the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview) to manage budgets for projects. 

  * [Take a 10-minute tutorial to get started with budgets for project users](https://console.cloud.google.com/?walkthrough_tutorial_id=billing--billing_budgets_for_projects)
  * [View the documentation to learn more about Google Cloud budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets)



## August 21, 2023

Announcement

We added a new BigQuery example that helps you join your Price and Detailed Cost Data exports, so that you can compare your costs with detailed information from your Pricing BigQuery export.

[View the example query to join prices and costs](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#join-price-with-usage-costs).

## July 31, 2023

Feature

**Cloud Billing Pricing API now available in preview**

You can now get list prices, as well as account-specific custom prices and discounts for Google Cloud stock keeping units (SKUs) with the **Pricing API (preview)**. You can also use the Pricing API to get additional information about Google Cloud services, such as service-to-SKU mappings, information about SKU groups, SKU group to SKUs mapping, and geo and product taxonomy information. 

  * [Learn about using the API, with example API requests](https://docs.cloud.google.com/billing/docs/how-to/get-pricing-information-api)
  * [Get detailed information in the the API reference](https://cloud.google.com/billing/docs/reference/pricing-api/rest)



## July 27, 2023

Feature

**List Prices now available in cost data exports**

You can now view the list prices associated with all line items charged to your account in Google Cloud Billing standard and detailed export. Use the `cost_at_list` column to view list prices.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)  
[Review the schema of the Standard cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage)

Feature

**View granular cost data from Firestore and Datastore usage in Cloud Billing exports to BigQuery**

You can now view granular Firestore and Datastore cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) as part of your overall App Engine usage. For your detailed Firestore and Datastore usage, the `service.name` column contains _App Engine_. Use the `resource.name` or `resource.global_name` fields in the export to view and filter your detailed Firestore and Datastore usage.

[Review the schema of the Detailed cost data export.](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

## June 06, 2023

Feature

**Use folders and organizations in budgets** : When you set up budgets for your Cloud Billing account, you can set the budget's scope to one or more folders or organizations that are linked to your account, in addition to the current options for specific projects and labels.

When you create a budget that applies to a folder or organization, the budget also covers future projects that you create in the folder or organization.

[Learn about creating and modifying budgets for your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/budgets).

## April 18, 2023

Feature

**Cloud Billing Reports and Cost Breakdown report now support CSV downloads**

For Cloud Billing [Reports](https://cloud.google.com/billing/docs/how-to/reports) and [Cost Breakdown reports](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown), we have added the ability to download the data in the report table to a comma-separated values (CSV) file. With this update, the Download CSV feature is now available on most reports in the Cloud Billing console, including: [Cost Table](https://docs.cloud.google.com/billing/docs/how-to/cost-table#download-to-csv), [Pricing Table](https://docs.cloud.google.com/billing/docs/how-to/pricing-table#download-to-csv), [Reports](https://docs.cloud.google.com/billing/docs/how-to/reports#download-to-csv), [Cost Breakdown](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#download-to-csv), and the [Committed Use Discounts (CUDs) dashboard](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based).

## April 11, 2023

Feature

**View granular cost data from Cloud Spanner usage in Cloud Billing exports to BigQuery**

You can now view granular Cloud Spanner cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Use the `resource.global_name` field in the export to view and filter your detailed Cloud Spanner usage.

[Review the schema of the Detailed cost data export.](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

Feature

**View granular cost data from App Engine usage in Cloud Billing exports to BigQuery**

You can now view granular App Engine cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Use the `resource.global_name` field in the export to view and filter your detailed App Engine usage. Note that Firestore, App Engine Flex, and Datastore costs are not included in the granular App Engine instance costs.

[Review the schema of the Detailed cost data export.](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)

## March 17, 2023

Announcement

Starting from **March 15, 2023** , in your Billing BigQuery exports and all Cloud Billing reports in the Google Cloud console, the service description for Cloud Monitoring (formerly Stackdriver) has changed from `Stackdriver Monitoring` to `Cloud Monitoring`.

If you have BigQuery queries or visualizations that filter data based on the Cloud Monitoring service description, you must update those queries.

  * [Learn about the structure of the Cloud Billing data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).
  * [Read the announcement for Cloud Operations Suite (February 2020)](https://docs.cloud.google.com/blog/products/management-tools/cloud-operations-grows-with-monitoring-logging-more)



## January 18, 2023

Feature

**Committed Use Discounts: View your usage data at an hourly granularity in the CUD Analysis dashboard**

You can now analyze the effectiveness of your [spend-based](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based) or [resource-based](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-resource-based#accessing_the_report) committed use discounts at an hourly granularity. Previously, you could only analyze your CUDs at the daily level.

Access your usage data at an hourly granularity in the [CUD Analysis dashboard](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis).

## December 19, 2022

Feature

**View your Cloud SQL costs in Billing export to BigQuery**

You can now view your granular Cloud SQL instance cost data in the Cloud Billing Detailed cost export. Use the `resource.global_name` field in the export to view and filter your Cloud SQL instance data.

**Note:** Some _Network Egress_ , _Cloud SQL: Backups in specific locations_ , and _Storage PD Snapshot_ costs are not included in the granular CloudSQL instance costs in Billing export to BigQuery, though these exceptions make up very few cost instances.

## December 08, 2022

Feature

**Preview: Get estimated costs in the Google Cloud console**

You can now estimate the cost of Compute Engine and Cloud Storage workloads in the Google Cloud console. The Cost Estimation tool provides estimates that also include any custom contract prices on your Cloud Billing account. These cost estimates can help you make more informed business decisions.

[Learn about estimating costs in the Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/estimate-costs).

## December 05, 2022

Change

**View expiring commitments and automatically renew resource-based commitments with the Committed use discount dashboard**

In the Committed use discount dashboard, you can now see subscription expiration notifications for commitments that are expiring within the next 30 days. In the dashboard's auto renewal column, you can automatically renew your _resource-based_ commitments.

For more information about viewing the Commitment dashboard, see [Committed use discount overview](https://docs.cloud.google.com/docs/cuds#viewing).

## November 28, 2022

Feature

**View granular cost data from Cloud Run instances in Cloud Billing exports to BigQuery**

You can now view granular Cloud Run cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Use the `resource.global_name` field in the export to view and filter your Cloud Run instances.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

Feature

**View granular cost data from Cloud Function instances in Cloud Billing exports to BigQuery**

You can now view granular Cloud Function cost data in the [Google Cloud Billing detailed export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage). Use the `resource.global_name` field in the export to view and filter your Cloud Function instances.

[Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## October 18, 2022

Change

**Dataset configuration requirements have changed for Cloud Billing export to BigQuery**

When exporting [**_detailed usage cost_** data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) to BigQuery, when you select or [create a BigQuery dataset](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#create-bq-dataset) to be used for your [BigQuery tables](https://docs.cloud.google.com/bigquery/docs/tables-intro), you can now use [**_any supported location_**](https://docs.cloud.google.com/bigquery/docs/locations) when configuring your [dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro). Prior to this update, when you enabled the export of _detailed usage cost_ data to BigQuery, your [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) was limited to using a _multi-region_ location.

**Data availability tip** : The dataset location you select can influence whether the previous month's billing data is added to the dataset retroactively:

  * When you enable the _detailed usage cost_ data export for the _first time_ , if you select a dataset configured to use a [_multi-region_ location](https://docs.cloud.google.com/bigquery/docs/locations#multi-regions), Cloud Billing data will be available retroactively from the start of the previous month.
  * If you enable the _detailed usage cost_ data export and select a dataset that is configured to use a [_region_ location](https://docs.cloud.google.com/bigquery/docs/locations), your Cloud Billing data will be available starting from the date when you enabled the export, and after. That is, Google Cloud billing data is _not added retroactively_ for _non-multi-region dataset locations_ , so you won't see Cloud Billing data from before you enable export.
  * For more details, see [Data availability](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-availability)



For more information, [review the schema of the Cloud Billing detailed cost export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## October 14, 2022

Feature

**Generally available: View your Google Kubernetes Engine (GKE) costs in Cloud Billing reports and cost data export to BigQuery**

You can view your GKE costs by cluster, namespace, and pod labels in the Detailed cost export, and the built-in reports in the Google Cloud console.

**Cloud Billing export to BigQuery**

In the Detailed cost export to BigQuery, you can use the `labels.key` column to filter the data by these label keys:

  * `goog-k8s-cluster-name`: Filter your GKE resources by cluster.
  * `k8s-namespace`: Filter your GKE resources by namespace.
  * `k8s-label`: View all your GKE resources.



**Cloud Billing reports**

In the [Cloud Billing report](https://docs.cloud.google.com/billing/docs/how-to/reports), [Cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown), and [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table), you can use the **Label** selector to filter and group your data by cluster or namespace, using one of these label keys:

  * `goog-k8s-cluster-name`: Filter or group your GKE resources by cluster.
  * `k8s-namespace`: Filter or group your GKE resources by namespace.



**To start viewing and analyzing your GKE cost data, see these pages** :

  * [Enable cost allocation for your GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations#view_breakdown)
  * [Enable the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)
  * [View your Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports)



## September 30, 2022

Feature

**Tags data now available in cost data export in BigQuery**

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are attached to resources and support inheritance, centralized management, nomenclature standardization, and policy engine integration. For Cloud Billing, Tags help map costs across your organization. In cost reporting, you can [query on Tags to perform Cost Management tasks](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) like chargebacks, audits, and other cost allocations.

Tags data is available in both the [_Standard usage cost_ export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage) and the [_Detailed usage cost_ export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

To learn more about Tags, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). To learn about using Tags in your cost data exported to BigQuery, see more [about tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#tags) and [query examples with tags](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#query-with-tags).

## September 19, 2022

Change

**Non-USD accounts can now view more cost information with the Commitment Analysis Dashboard**

Customers with _non-USD billing accounts_ now have additional information (including local currency cost data) available to them within the committed use discount dashboard and have been granted access to the [Commitments Analysis Dashboard](https://cloud.google.com/billing/docs/how-to/cud-analysis-spend-based#non-usd).

Change

**View all on-demand spend applicable for committed use discounts (CUDs)**

You can now view all CUD-eligible usage _without any active commitments_ within the [Commitment Analysis Dashboard](https://cloud.google.com/billing/docs/how-to/cud-analysis-spend-based#understanding_dashboard) for further cost optimization opportunities.

## September 12, 2022

Feature

You can now estimate the cost of your workloads using the **Cost Estimation API (Preview)**. The Cost Estimation API provides customer-specific estimates that include all your discounts, such as those negotiated as part of a contract and those based on committed usage. These cost estimates can help you make more informed business decisions.

  * For information on using the API, and example API requests, see [Get cost estimates for your Google Cloud workloads](https://docs.cloud.google.com/billing/docs/how-to/cost-estimates-using-api).

  * For detailed information on the API request and response formats, see the [API overview](https://docs.cloud.google.com/billing/docs/reference/cost-estimation/rest).




## July 22, 2022

Feature

**Secure the link between a project and its billing account**

In the _Cloud Billing Console_ , you can now [lock the link](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link) between a project and its Cloud Billing account, in order to prevent accidental changes to the billing state, such as disabling billing or moving the project to a different billing account. You can also unlock this protected state if you want to unlink a project from a Cloud Billing account.

Google Cloud projects contain all the resources required for a system to operate. To pay for the usage of the Cloud resources (such as Compute Engine or Storage), each project must be linked to an active Cloud Billing account. If you unlink the project from a billing account, you disable billing on that project. When billing is disabled on a project, all resources contained within the project will shut down, which can cause outages to your normal business operation. 

To prevent unintentional outages due to billing issues, lock your valuable projects to their linked billing account. Locking creates a two-step process to change the billing state of a project, improving billing reliability and reducing accidental outages due to billing issues. 

[Learn how to secure the link between a project and a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link).

## June 30, 2022

Feature

**Preview: View your Google Kubernetes Engine (GKE) costs in Cloud Billing reports and cost data export to BigQuery**

You can view your GKE costs by cluster, namespace, and pod labels in the Detailed cost export, and the built-in reports in the Google Cloud console.

**Cloud Billing export to BigQuery**

In the Detailed cost export to BigQuery, you can use the `labels.key` column to filter the data by these label keys:

  * `goog-k8s-cluster-name`: Filter your GKE resources by cluster.
  * `k8s-namespace`: Filter your GKE resources by namespace.
  * `k8s-label`: View all your GKE resources.



**Cloud Billing reports**

In the [Cloud Billing report](https://docs.cloud.google.com/billing/docs/how-to/reports), [Cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown), and [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table), you can use the **Label** selector to filter and group your data by cluster or namespace, using one of these label keys:

  * `goog-k8s-cluster-name`: Filter or group your GKE resources by cluster.
  * `k8s-namespace`: Filter or group your GKE resources by namespace.



**To start viewing and analyzing your GKE cost data, see these pages** :

  * [Enable cost allocation for your GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations#view_breakdown)
  * [Enable the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup)
  * [Review the schema of the Detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage)
  * [View your Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports)



## June 28, 2022

Announcement

We've added new features to view your billing information and cost estimates in the Google Cloud Console mobile app. You can view your cost trends and forecasts, the costs for your top project, and how much you're spending on your top Google Cloud services.

To see your billing data in the app, select the Billing tab in the navigation bar, then select **Overview**.

[Get the Google Cloud Console app for iOS or Android](https://docs.cloud.google.com/console-app).

Change

**Attribution for your committed use discounts (CUDs) now appears at the same time as eligible usage.**

Previously, the subscription fees and credits associated with your CUDs would appear in billing reports and BigQuery usage cost exports after the corresponding eligible resource usage. This could result in apparent spikes in cost if you viewed your billing data before the attribution process completed.

With this release, subscription fees and credits appear at the same time as eligible usage, meaning that your net costs are always accurate whenever you view your billing data.

[Learn about how your CUD fees and credits are attributed across your resources](https://docs.cloud.google.com/docs/cuds-attribution).

## April 25, 2022

Feature

**Cost table report now supports updated filters, project ancestry, and report sharing**

In the _Cloud Billing Console_ [**Cost table report**](https://docs.cloud.google.com/billing/docs/how-to/cost-table), we've updated the report's [filters](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filters) and [invoice month selector](https://docs.cloud.google.com/billing/docs/how-to/cost-table#time-range) to function similarly to the Cloud Billing [Reports](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) page and [Cost breakdown](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#configure-report) page, added [project ancestry](https://docs.cloud.google.com/billing/docs/how-to/cost-table#project-hierarchy) functionality, and enabled [report sharing](https://docs.cloud.google.com/billing/docs/how-to/cost-table#share-report).

**Updated filters:** You use the **cost table** report to access the details of your invoices and statements. The report's filters and other settings allow you to [**configure the report views**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#customize_your_report_view) when you are analyzing the usage and cost data. You can also [download the cost table data to CSV](https://docs.cloud.google.com/billing/docs/how-to/cost-table#download-to-csv) for offline analysis. When you download the report to CSV, the data that downloads is limited by any [filters that you have set](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filters) and includes only the [columns that you have selected to view](https://docs.cloud.google.com/billing/docs/how-to/cost-table#column-selector).

**Project ancestry:** A new table column has been added to display project ancestry data. **_Starting_** with the **_January 2022_** invoice month:

  * [Historical project metadata](https://docs.cloud.google.com/billing/docs/how-to/cost-table#historical-cost-data) is available with the addition of [_Project hierarchy_ data](https://docs.cloud.google.com/billing/docs/how-to/cost-table#project-hierarchy).
  * Usage and cost data that was grouped by Project is now [_grouped by_ **_Project hierarchy_**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#project-hierarchy).
  * You can now [filter on Folders & Organizations](https://docs.cloud.google.com/billing/docs/how-to/cost-table#filter-by-folders-orgs), components of a [project's ancestry](https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy#about-project-hierarchy), to analyze costs by project hierarchy.
  * The values in the project hierarchy column are displayed only when you are viewing a [_flat table view_](https://docs.cloud.google.com/billing/docs/how-to/cost-table#flat-table-view) or when you are viewing a _nested table view_ [grouped by _Project > Service > SKU_](https://docs.cloud.google.com/billing/docs/how-to/cost-table#cost-grouping-options).
  * The report returns a row for each distinct combination of _Organization > Folder > Project_, and the table includes columns for _Project_ , _Project ID_ , _Project number_ , and _Project hierarchy_. The values listed in the [_Project hierarchy_ column](https://docs.cloud.google.com/billing/docs/how-to/cost-table#project-hierarchy) show _Organization name > Folder name_.



**Report sharing:** Along with the updated report filters, the **cost table** report now supports [**URL bookmarking and sharing**](https://docs.cloud.google.com/billing/docs/how-to/cost-table#share-report). As you configure your cost table report by setting the [invoice month](https://docs.cloud.google.com/billing/docs/how-to/cost-table#time-range), table view [cost grouping options](https://docs.cloud.google.com/billing/docs/how-to/cost-table#cost-grouping-options), and report [filters](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#filters), the **cost table URL** updates to include your selections. You can **save your report settings** by _bookmarking the URL_. You can **share the cost table report** by _copying the URL_.

For more details about the cost table report and using the updated features and functionality, see the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

## April 01, 2022

Feature

**Cost analysis by project ancestry, including folder-level costs, now available in BigQuery Export and Reports**

Viewing your costs by project ancestry helps you do things like analyze costs by folder or organization. For example, if you use folders in an organization to represent cost centers (such as _DevOps_ or _Finance_), you can effectively configure your report or query to group all costs by those cost centers.

**Billing Reports**

In the _Cloud Billing Console_ [**Reports page**](https://docs.cloud.google.com/billing/docs/how-to/reports), you can now Group by Project hierarchy and filter on Folders & Organizations, to analyze costs by project ancestry (such as folders or organizations).

  * **Group costs by project ancestry** – In the Reports page, when you [_group by_ **Project hierarchy**](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by-project-hierarchy), the report returns a row for each unique combination of _Organization > Folder > Project_, and the table includes columns for _Project_ , _Project ID_ , _Project number_ , and _Project hierarchy_. The values listed in the [_Project hierarchy_ column show _Organization name > Folder name_](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-project-hierarchy.png).

  * **Filter costs by project ancestor(s)** – In the Reports page, when you [_filter by_ **Folders & Organizations**](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-folders-orgs), the report returns costs for all projects that are associated with any of the selected folders/organizations in their project ancestry.




In the _Cloud Billing Console_ [**Cost breakdown report**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown), you can now filter on Folders & Organizations, to analyze costs by project ancestry (such as folders or organizations).

  * **Filter costs by project ancestor(s)** – In the Cost breakdown report, when you [_filter by_ **Folders & Organizations**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#filters), the report returns costs and credits aggregated for all projects that are associated with any of the selected folders/organizations in their project ancestry.



To learn more about organizations, folders, and project hierarchy, see [Billing reports: Analyzing your costs by project hierarchy](https://docs.cloud.google.com/billing/docs/how-to/reports-project-hierarchy).

**Cloud Billing data export to BigQuery**

In the Cloud Billing usage cost data that exports to BigQuery, you can now see resource hierarchy metadata that describes a project's ancestry, including: 

  * `project.ancestors.resource_name` – An identifier containing the resource hierarchy type and ID (for example, folders/234) 
  * `project.ancestors.display_name` – A name that you create for the resource (for example, DevOps) 



The `project.ancestors` metadata is available in both the _Standard usage cost_ export and _Detailed usage cost_ export. To help make resource hierarchy levels easier to identify in the BigQuery data tables, the ancestor data includes the resource display name (a human-readable name that you create) and the [relative resource hierarchy names](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) (immutable ID numbers representing each project/folder/organization). 

For more details about `project.ancestry_numbers` and `project.ancestors`, see

  * [Understand the Cloud Billing data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables)
  * [Query examples to use resource hierarchy filters to review project ancestry](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#use-resource-hierarchy-ancestry)



## March 08, 2022

Change

**Report filters now support the display of IDs in addition to names in the filter panels.**

In the _Cloud Billing Console_ , when you are viewing the options displayed in the filter panels for _Subaccounts_ , _Projects_ , _Services_ , and _SKUs_ , you can now see both the option name and the option ID (for example, project name and project ID). The ID displays below each option name. Previously, only the name was displayed when viewing the list of options in a filter panel. View an [example of the _Services_ filter panel, before and after the update](https://docs.cloud.google.com/static/billing/docs/images/relnotes-report-filters.png).

With the addition of the ID, you can do the following:

  * Within a filter panel, **search by name or by ID** (for example: "BigQuery" or "services/24E6-581D-38E5").
  * More easily **match a filter option to an invoice** line item. For example, instead of searching for the "Active Storage" SKU, you can search for SKU ID "services/24E6-581D-38E5/skus/947D-3B46-7781".
  * You can use **partial values when searching** within a filter panel, and you will get back all matching results. For example, you can _type to filter_ on "storage" or "24e6" or "7781".



Learn more about using filters in [Cloud Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) and the [Cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#filters).

## February 08, 2022

Change

Starting in **February 2022** , if you have committed use discounts (CUDs), Google Cloud Billing calculates the attribution for your fees and credits every hour, to help you track costs faster and more accurately.

[Learn about how your CUD fees and credits are attributed across your resources](https://docs.cloud.google.com/docs/cuds-attribution).

## February 01, 2022

Change

Starting on **February 1, 2022** , Google Cloud usage by customers in Bahrain is subject to 10% VAT.

[Learn about taxes applied in your country](https://docs.cloud.google.com/billing/docs/resources/vat-overview).

## November 01, 2021

Feature

**Prioritized attribution for your resource-based committed use discounts (CUDs) is now Generally Available**.

You can now specify how your credits and, where appropriate, the subscription fees from your resource-based committed use discounts are distributed among your Google Cloud projects.

[Learn about how you can allocate your commitments](https://docs.cloud.google.com/docs/cuds-attribution#type-prioritized).

## October 28, 2021

Feature

**Recommendations for _spend-based_ committed use discounts (CUDs) are now Generally Available**.

You can use these recommendations to optimize your project costs by analyzing your spending trends and signing up for committed use discounts. Recommendations are supported for Cloud Billing accounts billed in US Dollars (USD).

[Learn about commitment recommendations](https://docs.cloud.google.com/docs/cuds-recommender).

## September 17, 2021

Feature

**Cost breakdown report now supports new filters and report sharing**

In the _Cloud Billing Console_ [**Cost breakdown report**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown), you can now select the costs you want to analyze using the [**Time range**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#time_range) and other [**report filters**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#filters), such as projects, services, and SKUs. 

For detailed insights behind the results of your cost breakdown report, view the _Reports_ page. The _cost breakdown_ report is linked to the [Cloud Billing Reports page](https://docs.cloud.google.com/billing/docs/how-to/reports); the link uses the same _time range_ and _report filters_ you configure on your **cost breakdown** report. When you [open the Reports page from your cost breakdown report](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#report_summary), the report opens displaying the same totals as the cost breakdown report.

Along with the new report filters, the **cost breakdown** report now supports [**URL bookmarking** and **sharing**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#share-report). As you configure your cost breakdown report by setting the _time range_ and other _filters_ , the **cost breakdown URL** updates to include your selections. You can **save** your report settings by _bookmarking the URL_. You can **share** the cost breakdown report by _copying the URL_. 

For more details about the cost breakdown report and using the new report filters and sharing feature, see the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown).

## September 09, 2021

Feature

**Cloud Billing** **_Budgets & alerts_** **now support configurable budget time periods, beyond monthly budgets**

In the _Cloud Billing Console_ [Budgets & alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) settings, you can now specify the time period of your budgets. Using the [Time range](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) settings now available to budgets in the Cloud Console, you can configure the budget's time range to a [calendar period](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) or a [custom date range](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope), allowing you to create budgets to monitor spend for time frames beyond the default calendar month, such as a quarter, a year, or a custom date range that you specify.

With this update, you can create, view, and manage all budgets (monthly and non-monthly) in the [_Budgets & alerts_](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets) page in the Cloud Console or by using the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api).

For more information on budgets and alerts, see [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).

## August 27, 2021

Feature

The _detailed usage cost data_ export to BigQuery is now **generally available** (GA).

The _detailed_ export includes all of the data fields from the [_standard usage cost data_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#standard-usage-cost-data-schema) export, along with additional fields that provide resource-level cost data. The resource-level cost data available in the _detailed_ export is limited to Compute Engine resources, such as virtual machines or SSDs that generate service usage.

In your BigQuery dataset, the _detailed usage cost data_ is exported to a table named `gcp_billing_export_resource_v1_<BILLING_ACCOUNT_ID>`.

The following are the newly available fields:

  * `resource` (Struct) - The fields that describe the structure and value of information relevant to service resources (like a virtual machine or a SSD) that generate service usage.
  * `resource.global_name` (String) - A globally unique service identifier for the resource that generated relevant usage.
  * `resource.name` (String) - A service-specific identifier for the resource that generated relevant usage. This can be input generated by the user. _Note, the first full day of data with this field is August 11, 2021._



The _daily cost detail data_ export to BigQuery is now the [_standard usage cost data_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#standard-usage-cost-data-schema) export.

To understand the differences between the _standard_ and _detailed usage cost data_ exports to BigQuery, see the [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#standard-usage-cost-data-schema).

## August 23, 2021

Feature

_Proportional attribution_ for [spend-based committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based) is now **generally available** (GA).

Proportional attribution applies the subscription fees from your committed use discounts to the projects in your Cloud Billing account, directly in proportion to the amount of eligible credit consumed by each project. Any subscription fees that are not attributed to a project are charged at the Cloud Billing account level.

Starting from August 2021, all spend-based commitments you purchase for any of your Cloud Billing accounts use proportional attribution by default. If you purchased spend-based commitments before then, you can [request that they be converted](https://docs.cloud.google.com/docs/cuds-attribution#enable-proportional-attribution-spend-based) from account to proportional attribution.

To understand proportional attribution for your spend-based commitments and how to enable it, see the [documentation](https://docs.cloud.google.com/docs/cuds-attribution).

## July 01, 2021

Change

**(Customers in India only)** We have updated information about Google's tax compliance in India, for tax deducted at source (TDS). [Learn about Google Cloud India TDS certificates](https://docs.cloud.google.com/billing/docs/resources/tds#tax-compliance).

Change

**(Customers in India only)** Starting on **July 1, 2021** , the first page of your invoice shows a Unified Payment Interface (UPI) QR code. You can pay your invoice by scanning the QR code with any UPI-enabled application.

## June 29, 2021

Feature

**Summary bar now available in the Cost Table report**

To provide additional flexibility when analyzing your data in the [cost table](https://docs.cloud.google.com/billing/docs/how-to/cost-table) report, we've added the [summary bar](https://docs.cloud.google.com/billing/docs/how-to/cost-table#summary-bar) as another analysis tool.

When you select a subset of rows in your cost table, a floating [summary bar](https://docs.cloud.google.com/billing/docs/how-to/cost-table#summary-bar) opens and shows you the total gross costs, credits, the percentage of savings, and the total net costs, summarized for the selected rows. The summary bar is available for both the nested and flat table views.

For more information about using the summary bar on the Cost table report, see [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table#summary-bar).

## June 08, 2021

Feature

Committed use discounts for Google Kubernetes Engine (GKE) are now **Generally Available** to purchase for workloads running on GKE Autopilot.

They provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. The spend-based committed use discounts apply to all GKE Autopilot Pod workload CPU, memory, and ephemeral storage usage in the region in which you have committed. This gives you low, predictable costs, without the need to make any manual changes or updates yourself. This flexibility saves you time and helps you to save more by achieving high utilization rates across your commitments.

GKE Autopilot Mode commitments _do not apply_ to the [cluster management fee](https://cloud.google.com/kubernetes-engine/pricing#cluster_management_fee_and_free_tier) or to [GKE Standard mode compute nodes](https://cloud.google.com/kubernetes-engine/pricing#standard_mode).

See the [documentation](https://docs.cloud.google.com/kubernetes-engine/cud) for more details.

## May 13, 2021

Feature

Committed use discounts are now available for **public preview** to purchase for Cloud Run. They provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. The spend-based committed use discounts apply to all aggregated Cloud Run CPU, memory, and request usage in a region, giving you low, predictable costs when your code is running in one of the supported container ecosystems. 

Cloud Run commitments _do not apply_ to networking changes.

See the [documentation](https://docs.cloud.google.com/run/cud) for more details.

## May 10, 2021

Feature

**Cloud Billing Reports now show the target budget amount when you open the report from a budget**

In the Cloud Billing Console, [**Billing Budgets**](https://docs.cloud.google.com/billing/docs/how-to/budgets) are linked to the [**Billing Reports**](https://docs.cloud.google.com/billing/docs/how-to/reports) page. If you [open the **Reports** page from a **Budget**](https://docs.cloud.google.com/billing/docs/how-to/reports#budget-in-report), the [budget's scopes](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) are used to set the [report's filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filters) and the report opens displaying the costs tracked by the budget. Additionally, the [budget's target amount](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-amount) appears in the report chart as a red, dashed line, helping you to visualize the budget amount in the report while you are analyzing the specific, budget-related costs. You can open the cost report from the [list of budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets), or from a [budget's cost trend chart](https://docs.cloud.google.com/billing/docs/how-to/budgets#cost-trend-chart).

For more details about how budgets and cost reports are linked, see [Viewing a budget in your report](https://docs.cloud.google.com/billing/docs/how-to/reports#budget-in-report).

## April 19, 2021

Feature

**Budget API now supports configurable budget time periods, beyond monthly budgets**

Using the [**Cloud Billing Budget API**](https://docs.cloud.google.com/billing/docs/how-to/budget-api) to manage your budgets, you can now specify the time period of the budget. Prior to this update, you could only configure a budget to monitor costs incurred during a calendar month. Using the [`usage_period`](https://docs.cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets#filter) filter that is available in the Cloud Billing Budget API, you can configure the budget time period to a [`CalendarPeriod`](https://docs.cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets#calendarperiod) or a [`CustomPeriod`](https://docs.cloud.google.com/billing/docs/reference/budget/rest/v1/billingAccounts.budgets#customperiod), allowing you to create budgets to monitor time frames beyond the default calendar month, such as a quarter, a year, or a custom date range that you specify.

At this time, budgets configured with a non-monthly time period can only be viewed and managed using the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api). Non-monthly budgets are _not yet visible_ in the [_Budgets_ page](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets) in the Cloud Console.

For more information on using the Cloud Billing Budget API, see [Get started with the Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview).

## March 31, 2021

Breaking

**Effective April 1, 2021, for customers in India** : Due to new Reserve Bank of India (RBI) regulations, your bank might begin declining automatic card charges for recurring payments for your Google Cloud usage.

To avoid interruptions in service, if your automatic payments are being declined, we recommend that you [make a manual payment](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) for your usage.

## March 11, 2021

Feature

**List cost and Unrounded cost columns now available in the Cost Table report**

We've added two columns of data to the [Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table): _List cost_ and _Unrounded cost_.

  * **List cost** : The `List cost` column is available for Cloud Billing accounts **_associated with a negotiated pricing contract_** , and represents the monthly cost of your cloud usage calculated using [list prices](https://cloud.google.com/billing/docs/how-to/pricing-table). If your account has negotiated, custom pricing, you can compare `List cost` amounts to `Cost` amounts to determine how much you are saving with your negotiated prices.
  * **Unrounded cost** : The `Unrounded cost` column contains the calculated cost of the usage to a precision of up to six decimal places. Unrounded costs can be helpful when analyzing your cost details and understanding the source of any discrepancies due to rounding.



For more information on the Cost table report, see [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

## February 22, 2021

Feature

_Optimal Recommendations_ for Compute Engine committed use discounts are now **Generally Available**. Recommendations provide you opportunities to optimize your compute costs by analyzing your VM spending trends and recommending committed use discount contracts. 

Recommendations are presented in two forms:

  * _Optimal recommendations_ are based on overall usage and might cover resources that are not on all the time. 
  * _Stable usage_ recommendations cover minimum stable usage over time.



For understanding and purchasing committed use discount recommendations, see [the documentation](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-resource-based#understanding_commitment_recommendations).

## February 05, 2021

Feature

**PayPal now available as a form of payment in many countries**

If you have an [_online, auto-pay_ Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you might be able to add PayPal as a form of payment on that account.

To learn if PayPal is available for your Cloud Billing account in your country or region, visit one of these tools:

  * Cloud Billing docs: [Currencies and payment methods available for Cloud Billing auto-pay accounts](https://docs.cloud.google.com/billing/docs/resources/currency)
  * Google Payments: [Payment methods & terms of service finder](https://payments.google.com/u/0/paymentsinfofinder)



To learn how to update the form of payment on your [_online, auto-pay_ Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), see [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods).

## February 01, 2021

Change

**Invoices are now simpler, providing only your cost totals. View your cost details in the Cost Table and other reports in the Cloud Console.**

Beginning with your **January 2021 invoice or statement** (available in February 2021), we **_removed all cost details_** from your invoice and statement documents, including product-level costs and costs by subaccounts (for Resellers). Invoices and statements will continue to provide header information, such as business mailing address and billing account number, the _cost totals_ for the invoice or statement period, and remittance information.

The **cost details** of your invoice or statement are available in the Cloud Console, in the downloadable [**Cost Table report**](https://docs.cloud.google.com/billing/docs/how-to/cost-table). The Cost Table report reconciles to the invoice totals and includes the product-level costs and costs by subaccounts (for Resellers), along with additional details you might need, such as costs by projects, services, SKU IDs, and labels. You can also analyze your usage costs using the [**Reports** page](https://docs.cloud.google.com/billing/docs/how-to/reports) or [create custom reports](https://docs.cloud.google.com/billing/docs/how-to/visualize-data) using your [exported Cloud Billing data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

For guidance on using these reports, see:

  * [**Cost table** : View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [**Reports page** : View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [**Billing data** : Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [**Custom reports** : Visualize spend over time with Google Data Studio](https://docs.cloud.google.com/billing/docs/how-to/visualize-data)
  * [**Blog post** : Giving you better cost analytics capabilities—and a simpler invoice](https://docs.cloud.google.com/blog/topics/cost-management/cost-management-tools-in-google-cloud-console)



Feature

**Cloud Billing Budgets now shows your historic cost trends when you're planning your budget .**

In the Cloud Billing Console, the Cloud Billing Budget creation and edit experience has been updated to include a [**cost trend chart**](https://docs.cloud.google.com/billing/docs/how-to/budgets#cost-trend-chart) showing your summarized costs by month for the previous 12 months, helping you visualize how your targeted budget amount is tracking with your spend. Your cost trend chart will show different results based on the budget filters you set (for example, filtering on specific projects or services).

You can use the chart to identify previous spending trends and help forecast future needs as you plan your budget. If you need more detailed insights, the chart is linked to the [**Cloud Billing Reports** page](https://docs.cloud.google.com/billing/docs/how-to/reports); the link uses the same filters you set on your budget to configure your report view.

For more information on the cost trend chart, see [Set budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets#cost-trend-chart).

## January 28, 2021

Feature

**Pricing report access updated to allow _Billing Account Users_ to view a version of the report**

The Pricing report provides SKU prices for Google's cloud services, including Google Cloud, Google Maps Platform, and Google Workspace. Prior to this update, you could access the report only if you were a _Billing Account Administrator_ or a _Billng Account Viewer_. Now, _Billing Account Users_ can also access the report.

The data displayed in your report is dependent on your level of access to your Cloud Billing account. For more information, see [View and download prices for Google's cloud services](https://cloud.google.com/billing/docs/how-to/pricing-table).

## January 26, 2021

Change

The Cloud Billing Committed Use Discounts (CUD) Analysis report has been updated to include spend-based CUDs, allowing you to easily visualize the effectiveness and financial impact of discounts you have purchased. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-spend-based#understanding_analysis) for more details. Learn more about [spend-based committed use discounts](https://docs.cloud.google.com/docs/cuds-spend-based).

## December 17, 2020

Announcement

**Start using the Reports page and Cost Table in the Cloud Console for product-level cost details or subaccounts**

Beginning with your **January 2021 invoice or statement** (available in February 2021), to simplify the format, we are removing all cost details from your invoice and statement documents, including product-level costs and costs by subaccounts (for Resellers). To view all of the cost details on your invoice or statement, in the Cloud Console, access the downloadable [**Cost Table** report](https://docs.cloud.google.com/billing/docs/how-to/cost-table). The Cost Table report includes the product-level cost and cost by subaccounts (for Resellers), along with additional details you may need, such as costs by projects, services, SKU IDs, and labels. You can also analyze your usage costs using the [**Reports** page](https://docs.cloud.google.com/billing/docs/how-to/reports). 

For guidance on using these reports, see:

  * [**Cost table** : View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table)
  * [**Reports page** : View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [**Blog post** : Giving you better cost analytics capabilities—and a simpler invoice](https://docs.cloud.google.com/blog/topics/cost-management/cost-management-tools-in-google-cloud-console)



## December 16, 2020

Change

Recommendations for Compute Engine committed use discounts are now **Generally Available**. Recommendations provide you opportunities to optimize your compute costs by analyzing your VM spending trends and recommending committed use discount contracts. For understanding and purchasing committed use discount recommendations, see [the documentation](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-resource-based#understanding_commitment_recommendations).

## December 14, 2020

Feature

**Cloud Billing Reports page now allows you to save your report views.**

The Cloud Billing Reports in the Google Cloud Console allows you to view and visualize your Google Cloud spend over time. You can filter and break down your usage by different dimensions, including: time range, projects, products, SKUs, labels, and subaccounts. Prior to this update, if you wanted to save your filter settings, your only options were to bookmark or make a copy of your report's URL. To offer a better user experience, you can now save your custom report views and access your saved views.

For information on the _saved views_ feature, refer to [Saving and sharing report views](https://docs.cloud.google.com/billing/docs/how-to/reports#saving-views) in the Cloud Billing documentation.

## November 11, 2020

Feature

**Cost table report now includes invoice header information and project-level taxes.**

The cost table report presents a detailed, tabular view of your monthly costs for a given invoice or statement. The cost table has been updated to include invoice or statement header information that is viewable in the cost table page as well as downloadable to CSV.

Additionally, the cost table report now breaks out your [tax costs by each project](https://docs.cloud.google.com/billing/docs/how-to/cost-table#taxes). Prior to this update, your tax costs were listed at the end of the cost table as a row for each type of tax incurred, aggregated for the whole invoice or statement. To view the details of your tax costs, in the cost table, look for rows with a `Cost type`: **_Tax_** and `SKU description`: **_description and percentage of tax_** (for example, _PST/QST/RST (9.975%)_ or _State sales tax (4.71%)_).

For information on using the cost table report to view and analyze the details of your invoice or statement, refer to the [Cost table reports documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

## November 09, 2020

Feature

The **Cloud Billing Budgets API v1** is now available.

  * [Learn about the Cloud Billing Budgets REST API](https://docs.cloud.google.com/billing/docs/reference/budget/rest).
  * [Review examples of using the Billing Budgets REST API](https://docs.cloud.google.com/billing/docs/how-to/budget-api).
  * [Learn about the Cloud Billing Budgets API client libraries](https://docs.cloud.google.com/billing/docs/reference/budget/libraries).



## October 28, 2020

Change

Updated the schema for the Cloud Billing data tables in the Billing BigQuery usage export to provide more clarity and data to customers. New data fields have been added that detail project number & adjustments or corrections to cost obligations on your billing account. 

The following data fields have been added to the Billing BigQuery usage export schema: 

  * **project.number**
  * **adjustment_info**
  * **adjustment_info.id**
  * **adjustment_info.mode**
  * **adjustment_info.description**
  * **adjustment_info.type**



This data is new as of October 29, 2020, and will not be available for data export before then. Please update your integrations or automations based on the new schema by performing migrations, if and when necessary. For information on the data these new fields provide, refer to [Understanding Cloud Billing data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).

For examples of how to update your BigQuery queries, views, and dashboards for the data schema changes, see [Handling schema changes to BigQuery export data tables](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-examples).

## October 15, 2020

Feature

Discount sharing for committed use discounts is now **Generally Available**. With discount sharing enabled, you can apply your purchased commitments across multiple projects within a single Cloud Billing account. Discount sharing helps you minimize the overhead of managing each of your commitments individually and provides increased flexibility so that you can use the compute options that best suit your needs, while also increasing cost predictability. 

  * For more information about enabling committed use discount sharing, see [Turning on committed use discount sharing](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#turning_on_committed_use_discount_sharing).
  * For more information on the possible cost savings using committed use discount sharing, see [Understanding discount sharing](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis#understanding_discount_sharing).



## October 08, 2020

Change

**Cloud Billing budget settings** have been updated to support **credits by credit type**. We have added all possible [Cloud Billing credit types](https://docs.cloud.google.com/billing/docs/how-to/budgets#about_credit_types) to the [budget scope](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope), allowing you to set your budget amount to include or exclude specific credits by type, such as promotional credits, committed use discounts, and free tiers. **Previously** , the credits setting was an optional checkbox when setting the budget amount — the **_Include credits in cost option_** — and not the granular options now available in the budget scope. The previous credits checkbox setting could only include either all of the available credits or none of the credits. 

For budgets that were set up _before_ the granular credits budget scope feature became available:

  * In the budget amount, if you had enabled the **_Include credits in cost_** option, then all credits are included in the cost calculation.
  * In the budget amount, if you had deselected the **_Include credits in cost_** option, then none of the credits are included in the cost calculation.



To implement the new credits scope feature in existing budgets, [edit the budget's credit settings](https://docs.cloud.google.com/billing/docs/how-to/budgets#edit-or-delete-budget).

[Read more about credits and budget scope options](https://docs.cloud.google.com/billing/docs/how-to/budgets#budget-scope) in our documentation.

## October 07, 2020

Change

**Project-level tax information in BigQuery Export** tables: Starting on **September 1 2020** , your daily cost detail data in BigQuery shows taxes broken down by project, instead of aggregating taxes into a single line item. You don't need to make any changes to access the data.

If you have queries or visualizations that depend on tax data, you might need to update the queries to account for these changes.

[Learn about viewing your tax data in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#taxes).

## September 28, 2020

Change

**Budget alert email notifications** : Cloud Billing Budgets functionality has been updated to offer more control over recipients of alert emails. In [May 2020](https://docs.cloud.google.com/billing/docs/release-notes#May_18_2020), we announced that you can use _Monitoring notifications_ to customize your budget to send alert emails to up to five additional email recipients you specify, _in addition to the default email recipients_. Now, you can also **opt out of the default email settings** , choosing not to send budget alert emails to Billing Account Administrators and Billing Account Users on the target Cloud Billing account (that is, every user assigned a [billing role](https://docs.cloud.google.com/billing/docs/how-to/billing-access) of either roles/billing.admin or roles/billing.user). To opt out of the default behavior, in the Cloud Billing budget's **Manage notifications** settings, deselect _Email alerts to billing admins and users_. [Read more about email notification settings in our documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets#manage-notifications).

Change

Committed use discounts (CUDs) are now available to purchase for Cloud VMware Engine. CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. With spend-based committed use discounts for Cloud VMware Engine, you can earn a deep discount off your cost of use in exchange for committing to continuously use VMware Engine nodes in a particular region for a 1- or 3-year term. See the [documentation](https://docs.cloud.google.com/vmware-engine/docs/cud) for more details.

## September 23, 2020

Change

We've added .NET and Go client libraries for the Cloud Billing Budget API (Beta).

[Learn about using the Cloud Billing Budget client libraries](https://docs.cloud.google.com/billing/docs/reference/budget/libraries).

## September 10, 2020

Feature

The **Cloud Billing data export to BigQuery** [_daily cost detail data_](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-schema) now includes 3 additional fields to describe [**credits**](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits): [`credits.id`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits-id), [`credits.full_name`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits-full_name), and [`credits.type`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits-type). Including the credit details in the data export to BigQuery is especially useful for creating queries to analyze how credits impact your costs on a more granular level, such as understanding credits grouped by project, or for analyzing the source of multiple credits of the same type that were earned during the same invoice period (such as sustained usage discounts earned as usage increases).

See [Understanding the Cloud Billing data tables in BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#data-schema) for more details.

## August 12, 2020

Feature

Recommendations for Compute Engine committed use discounts are now available in **beta**. Recommendations provide you opportunities to optimize your compute costs by analyzing your VM spending trends and recommending committed use discount contracts. For understanding and purchasing committed use discount recommendations, see [the documentation](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis-resource-based#understanding_commitment_recommendations).

## August 07, 2020

Feature

You can now view a summary of all your spend-based committed use discounts (CUD) and purchase new commitments in the [commitment dashboard](https://docs.cloud.google.com/docs/cuds-spend-based#view_commitment_dashboard). The dashboard lists the **type** of commitment, **region** it's located, current **active** commitments, **term** length, and the **start** and **end** dates for the commitment. See [the documentation](https://docs.cloud.google.com/docs/cuds-spend-based#view_commitment_dashboard) for more details.

Feature

**New columns added to Cost Table report: Credit ID and Credit name.** Starting with your **July 2020** invoice month, the [cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) now includes columns for `Credit ID` and `Credit name`. Including credit details in the cost table report is especially useful for understanding project-level credits, or for analyzing the source of multiple credits of the same type, earned during the same invoice period (such as sustained usage discounts earned as usage increases).

When you first load the cost table report, the credit columns are hidden by default. You can use the [column selector to customize the columns](https://docs.cloud.google.com/billing/docs/how-to/cost-table#columns_in_the_cost_table) you view in the report as well as the columns you download to CSV. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for more details.

## August 06, 2020

Feature

If you have a **negotiated pricing contract** associated with your Cloud Billing account, **starting with your July 2020 invoice** , the [**Cloud Billing report**](https://docs.cloud.google.com/billing/docs/how-to/reports) and the [**Cost Breakdown report**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown) now support displaying your costs calculated using list prices, displaying your **negotiated savings** as a separate credit. This view helps you see how much money you are saving on your Google Cloud costs because of your negotiated pricing contract.

For information on how to view your list costs and negotiated savings in reports, see the documentation:

  * [Learn more about viewing negotiated savings in your **Cloud Billing report**](https://docs.cloud.google.com/billing/docs/how-to/reports#contract-pricing).
  * [Learn more about viewing negotiated savings in your **Cost Breakdown report**](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown#negotiated-savings).



## July 23, 2020

Feature

**Export your Cloud Billing account SKU prices to BigQuery.** You can now export your pricing information for Google Cloud and Google Maps Platform SKUs to BigQuery. Exporting your pricing data allows you to audit, analyze, and/or join your pricing data with your exported cost data. The pricing export includes list prices, pricing tiers, and, when applicable, any promotional or negotiated pricing. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) for more details.

## July 10, 2020

Feature

The [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) functionality has been updated to add a **Table configuration** interface that replaces the previous _Group by_ and _Label_ selectors. Use the new **Table configuration** dialog to choose a **Label key** and select your **Group by** options. Additionally, the available **Group by** options have been enhanced to include a new **Custom grouping** option. Use custom grouping to view a [nested cost table](https://docs.cloud.google.com/billing/docs/how-to/cost-table#nested_table_view) with your costs grouped by up to three dimensions that you choose, including label values. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for more details.

## June 23, 2020

Feature

Committed use discounts (CUDs) are now available to purchase for Cloud SQL. CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. With spend-based committed use discounts for Cloud SQL, you can earn a deep discount off your cost of use in exchange for committing to continuously use database instances in a particular region for a 1- or 3-year term. See the [blog](https://docs.cloud.google.com/blog/products/databases/cloud-sql-database-instances-now-discounted) and [documentation](https://docs.cloud.google.com/docs/cuds) for more details.

## May 29, 2020

Feature

[`Labels`](https://docs.cloud.google.com/billing/docs/how-to/cost-table#columns_in_the_cost_table) column added to the [flat table view](https://docs.cloud.google.com/billing/docs/how-to/cost-table#flat_table_view) of the Cloud Billing Cost Table report. The Cost Table report provides a tabular view of your invoice costs. You can quickly filter your costs by available fields, such as project, service, SKU, and labels (among other fields), and you can download the table to CSV for offline analysis. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for more details.

## May 27, 2020

Change

New data property now available for Cloud Billing budget alerts that are configured for [programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications). You set up a Cloud Billing budget to trigger an alert notification based on [threshold rules](https://docs.cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) for _Actual_ or _Forecasted_ spend. Programmatic notifications triggered on **Forecasted** costs are now identified with the `forecastThresholdExceeded` property in the JSON object. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification_format) for more details.

## May 21, 2020

Feature

Cloud Billing Budget API: new budget filters for groups of subaccounts and resource labels are now available in the Budget API. See the [documentation](https://docs.cloud.google.com/billing/docs/reference/budget/rest/v1beta1/billingAccounts.budgets) for more details.

## May 18, 2020

Feature

**Cloud Billing budgets emails** : ensure your budget alert emails are seen by the right people using Cloud Monitoring notifications on your Cloud Billing budgets. By default, alert emails are sent to Billing Account Administrators. With the _Monitoring notifications_ feature, you can customize your budget to send alerts to up to five additional email recipients you specify. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets-notification-recipients) for more details.

Feature

New information is now available on your **Cloud Billing** account **Overview** page in the **Cloud Console** , featuring at-a-glance summaries of the top five spending projects and top five spending products over the last 12 months.

To see the updated Billing Account Overview page, go to the [Manage billing accounts page](https://console.cloud.google.com/billing) in the Cloud Console and sign in, then select the name of the Cloud Billing account you want to view. The Billing Overview page is displayed with the **BILLING ACCOUNT OVERVIEW** tab selected. You might need to scroll the page to see all the features.

## April 23, 2020

Feature

For customers with [self-serve/online](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) Cloud Billing accounts, you can now find your Cloud Billing documents in the **Documents** page of the Cloud Billing console. In the Documents page, you can find your monthly invoices or statements, as well as tax documents, if applicable to your account. Before this launch, the Documents page was only available to customers viewing [invoiced](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) Cloud Billing accounts, while self-serve/online accounts were limited to finding their Cloud Billing documents in the Transactions page. See the [⁠documentation](https://docs.cloud.google.com/billing/docs/how-to/get-invoice) for more details.

Change

Cost forecasts in Cloud Billing reports has been updated to calculate your forecasted spend up to 12 months in the future. Previously, the calculation forecasted your spend for the next 30 days. Cost forecasts make it easier to see at a glance how your costs are trending and how much you are projected to spend over a time range you specify. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#cost-forecast) for more information.

## April 22, 2020

Feature

Budget alerts: new budget filters are now available. In addition to project and product filters, you can now scope your budgets and alerts for groups of subaccounts and resource labels. Budget alerts help you stay informed of how your spend is tracking against your budget so you can avoid billing surprises. (Note that these filters are not available in the Budgets API in this release.) See the [⁠documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets) for more details.

## April 16, 2020

Feature

Discount sharing for committed use discounts is now available in **beta**. With discount sharing enabled, you can apply your purchased commitments across multiple projects within a single Cloud Billing account. Discount sharing helps you minimize the overhead of managing each of your commitments individually and provides increased flexibility so that you can use the compute options that best suit your needs, while also increasing cost predictability. 

  * For more information about enabling committed use discount sharing, see [Turning on committed use discount sharing](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#turning_on_committed_use_discount_sharing).
  * For more information on the possible cost savings using committed use discount sharing, see [Understanding discount sharing](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis#understanding_discount_sharing).



Feature

Cloud Billing console now has a Pricing report, providing a tabular view of the prices of Google’s cloud services SKUs, including Google Cloud, Google Maps Platform, and Google Workspace. You can select to view the SKUs with historical usage on the billing account or all Google Cloud SKUs. If you have a negotiated contract, the pricing table will include the list price, the contract price and the effective discount. You can also download the table to CSV for offline analysis. See the [documentation](https://cloud.google.com/billing/docs/how-to/pricing-table) for more details.

## March 23, 2020

Feature

**Billing health checks** is now available on your **Cloud Billing** account **Overview** page in the **Cloud Console**. This feature automatically analyzes the health of your **Cloud Billing** account, then displays the results in a Billing health checks informational card, helping you avoid common billing-related issues and to adopt our [best-practice recommendations](https://docs.cloud.google.com/billing/docs/onboarding-checklist#checklist_3). In the info card, click **_View all health checks_** to view a page with detailed recommendations, explanations, and action items to remedy issues that could jeopardize the safety or condition of your Cloud Billing account.

To see the **Billing health checks** card, go to the [Manage billing accounts page](https://console.cloud.google.com/billing) in the Cloud Console and sign in, then select the name of the billing account you want to view. The Billing Overview page is displayed with the **BILLING ACCOUNT OVERVIEW** tab selected. Look for the card titled **Billing health checks**.

## March 02, 2020

Feature

The Cost Table report now includes a nested table view, providing a hierarchical, tree-structured view of your cost data which is helpful when analyzing your billing data online. You can select your grouping options, filter your costs by project, service, and SKU (among other fields), and specify the table columns to be displayed. You can also download the table to CSV for offline analysis. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for more details.

## December 04, 2019

Feature

The Cloud Billing reports now support filtering and grouping costs by User Labels. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) for more details. Learn more about [User Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

## December 01, 2019

Change

Starting with your November 2019 invoice, we have removed project-level cost detail from your [Google Cloud invoices and statements](https://docs.cloud.google.com/billing/docs/how-to/read-invoice). If your organization currently processes the invoice CSV and requires project-level cost detail, [download the CSV from the Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and process it in place of the invoice CSV.

## November 18, 2019

Feature

The Cloud Billing Committed Use Discounts (CUD) Analysis report is now available in GA. View the CUD Analysis report to easily visualize the effectiveness and financial impact of committed use discounts you have purchased. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis) for more details. Learn more about [Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

## November 13, 2019

Change

Cloud Billing data export to BigQuery now reports all service usage at an hourly granularity. For each reporting service in the export, this means that the `usage_start_time` and `usage_end_time` fields will report hourly data; that is, the usage end time will always be exactly one hour after the start time. This improves the consistency and data accuracy of your reporting data across all GCP services, while also providing support for future billing export changes. See the Cloud Billing [BigQuery export schema](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#billing_data_in) and [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) for more details.

## November 12, 2019

Feature

The Cloud Billing Budget API is now available in Beta. With the Budget API, you can view, create, and manage budgets programmatically at scale. Budget alerts help you stay informed of how your spend is tracking against your budget so you can avoid billing surprises. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview) for more details.

## September 25, 2019

Feature

The Cloud Billing reports page now supports URL bookmarking and sharing. As you configure your report by setting filters and groupings, your URL updates to include your selections. You can save your report settings by bookmarking the URL. You can share the report by copying the URL. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#changing_chart_settings) for more details.

## August 27, 2019

Feature

Set budget alerts on projects and products. New, more granular budget filters are now available, allowing you to scope your budgets and alerts for groups of projects and GCP services. Budget alerts help you stay informed of how your spend is tracking against your budget so you can avoid billing surprises. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets) for more details.

## August 26, 2019

Change

Billing Navigation—Invoices renamed to Documents: The **Invoices** page in the GCP Billing Console has been renamed to **Documents**. Additionally, the page has been refreshed to improve navigation. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/get-invoice#get_your_invoice) for more details.

## August 22, 2019

Feature

The Cost Table report is now available in Cloud Billing. Use Cost Table reports to get a tabular view of your invoice costs grouped by project and SKU. You can quickly filter your costs by project, service, and SKU (among other fields), and you can download the table to CSV for offline analysis. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-table) for more details.

## August 12, 2019

Change

The Billing Account Overview page in the GCP Console was redesigned to provide you with an at-a-glance summary of your charges to date, estimated end-of-month charges, and any credit balances. The functionality of the previous overview page, such as [viewing the projects linked to a billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked) or [viewing and updating billing permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access#update_billing_permissions), is now available in the new Account Management page.

  * To see the **updated Billing Account Overview page** , go to the Google Cloud Platform Console [Manage billing accounts page](https://console.cloud.google.com/billing) and sign in, then select the name of the billing account you want to view. The Billing Overview page is displayed with the **BILLING ACCOUNT OVERVIEW** tab selected. (Note that to view an at-a-glance summary of your payments and account balance, select the PAYMENT OVERVIEW tab.)
  * To see the **new Account Management page** , go to the Google Cloud Platform Console [Manage billing accounts page](https://console.cloud.google.com/billing), sign in, and select the name of the billing account you want to view. Then from the Billing menu on the left, click **Account management**.



## June 26, 2019

Feature

**Complete Billing Record in Reports** : Starting with your May 2019 invoice (issued in early June 2019), you can configure your Cloud Billing reports to view your charges by invoice, including invoice-level charges (for example, taxes, contractual credits, or surcharges) and any rounding errors. Use this view to reconcile your Cloud Billing reports to your invoice, to the penny. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#invoice-charges) for more details.

**Cost Breakdown Reports** : Cost Breakdown reports are now available in Cloud Billing. Use Cost Breakdown reports for a quick overview of how usage-based discounts and credits save you money on your GCP invoice. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cost-breakdown) for more details.

## June 11, 2019

Feature

The Cloud Billing Committed Use Discounts (CUD) Analysis report is now available in Beta. View the CUD Analysis report to easily visualize the effectiveness and financial impact of committed use discounts you have purchased. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis) for more details. Learn more about [Committed Use Discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

## May 22, 2019

Feature

The Cloud Billing reports now support filtering and grouping costs by location, specifically geography (such as _Americas_), multi-region (such as _US_), or region (such as _us-east1_). See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) for more details. Learn more about [Cloud locations](https://cloud.google.com/about/locations/).

## April 01, 2019

Change

Cost forecasts in the Cloud Billing reports now includes both your long term cost trend as well as any consistent monthly cycles such as sustained use discounts. Including monthly cycles in your cost forecast makes it easier to see at a glance how how much you are projected to spend by the end of the month. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#cost-forecast) for more details.

## March 14, 2019

Feature

Budget alerts against forecasted costs: You can now configure budget alerts for when your costs are forecasted to exceed your budget. For each budget you have configured, you can set multiple budget alert threshold rules, triggered against either actual costs or forecasted costs, so you can stay informed of how your spend is tracking against your budget and avoid billing surprises. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets) for more details.

## February 04, 2019

Feature

Cloud Billing reports now support detailed credit types in the report settings.

Previously, costs were reported as cost before credits, credits, and cost after credits. The credit amount displayed was a sum of all possible credit types.

With this launch, you can now see what types of credits (discounts, promotions, etc.) comprise the credit amount displayed in the report. In the report settings, you can toggle on and off the different types of credits to customize your report views. See the [billing reports documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#credits) for details.

## December 13, 2018

Feature

**Complete Billing Record in Export** : Starting with your January 2019 invoice (issued in early February 2019) you can reconcile your Cloud Billing export to BigQuery to your invoice, to the penny. The export now includes a `cost_type` field to identify regular, tax, adjustment, and rounding error costs. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#billing_data_in) and [example queries](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) for more details.

**Folders in Export** : Cloud Billing export to BigQuery now includes the folder(s) and organization (if applicable) that a project belongs to (its project ancestry). This helps you do things like query costs by folder. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#project_ancestry) for more details about `project.ancestry_numbers`.

## November 30, 2018

Feature

Cloud Billing reports now support a bar chart view. See the [billing reports documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#bar-chart) for details.

## September 17, 2018

Feature

Cloud Billing export to BigQuery now includes additional location and system label fields to let you examine your cost data in more granular detail. Location details allow you to view your costs in each GCP region and zone, where supported by the service. System labels allow you to segment your costs by virtual machine type, number of cores, or amount of RAM. The [`compute.googleapis.com/machine_spec`](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#available_system_labels) system label should now be used in place of `sku.description` to query costs by virtual machine family and geometry. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#system_labels) for more details about the new fields.

## August 06, 2018

Feature

A new Cloud Billing IAM permission is now available that gives you finer control over what cost data your users can see. You can now use [`billing.resourceCosts.get`](https://docs.cloud.google.com/billing/docs/how-to/billing-access) to grant project-specific access to cost data like [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports). The new permission was added on 08-6, 2018. To give you time to set up your users with the correct permissions, the new permission will not be enforced until 08-20, 2018. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/billing-access) for more details.

## July 09, 2018

Feature

Cost forecasts are now available as a GA feature in Cloud Billing reports. Cost forecasts make it easier to see at a glance how your costs are trending and how much you are projected to spend. See the [blog](https://cloudplatform.googleblog.com/2018/07/predict-your-future-costs-with-google-cloud-billing-cost-forecast.html) and [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports#cost-forecast) for more details.

## May 31, 2018

Feature

Cloud Billing export to BigQuery now includes the invoice month (`invoice.month`) that the cost line item appears on. See the [export schema documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery#billing_data_in) and [example queries](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) for more details.

## May 22, 2018

Feature

Cloud Billing programmatic notifications for budget alerts is now available in GA. You can configure programmatic notifications to receive Cloud Pub/Sub messages about the current status of your budget. See the [blog](https://cloudplatform.googleblog.com/2018/05/Better-cost-control-with-Google-Cloud-Billing-programmatic-notifications.html) and [documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets#manage-notifications) for more details.

## April 24, 2018

Feature

Cloud Billing reports are now available in GA. Billing reports let you quickly chart your billing account's cloud spending. See the [blog](https://cloudplatform.googleblog.com/2018/03/understand-your-spending-at-a-glance-with-Google-Cloud-Billing-reports-beta.html) and [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports) for more details.

## March 30, 2018

Feature

Cloud Billing programmatic notifications for budget alerts is now available in Beta. You can configure programmatic notifications to receive Cloud Pub/Sub messages about the current status of your budget. See the [documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets#manage-notifications) for more details.

## March 20, 2018

Feature

Cloud Billing reports are now available in Beta. Billing reports let you quickly chart your billing account's cloud spending. See the [blog](https://cloudplatform.googleblog.com/2018/03/understand-your-spending-at-a-glance-with-Google-Cloud-Billing-reports-beta.html) and [documentation](https://docs.cloud.google.com/billing/docs/how-to/reports) for more details.

## February 27, 2018

Feature

The Cloud Billing Catalog API is now available in GA. The Catalog API offers programmatic access to pricing metadata on [Cloud Platform SKUs](https://docs.cloud.google.com/skus). See the [blog](https://cloudplatform.googleblog.com/2018/02/introducing-Cloud-Billing-Catalog-API-GCP-pricing-in-real-time.html) and [documentation](https://docs.cloud.google.com/billing/v1/how-tos/catalog-api) for more details.

## November 15, 2017

Feature

Cloud Billing export to BigQuery is now available in GA. BigQuery billing export regularly publishes new SKU usage and cost data to your BigQuery dataset. You can write SQL queries to understand your spending and use the BigQuery dataset to drive visualization tools like [Data Studio](https://docs.cloud.google.com/data-studio). See the [blog](https://cloudplatform.googleblog.com/2017/11/monitor-and-manage-your-costs-with.html) and [documentation](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
