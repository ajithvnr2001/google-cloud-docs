---
url: https://docs.cloud.google.com/marketplace/docs/partners/release-notes/
title: Cloud Marketplace Partners release notes \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:37.540478+00:00
---

# Cloud Marketplace Partners release notes  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Resources ](https://docs.cloud.google.com/marketplace/docs/partners/release-notes)



Send feedback 

#  Cloud Marketplace Partners release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the latest release notes for features and updates for Cloud Marketplace Partners. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gcpmarketplacepartners-release-notes.xml) directly. 

## July 30, 2026

Change

We've added the `city` field to Customer Insights reports and Detailed Disbursements reports.

For more information, see [Customer Insights report fields](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight#report_fields) and [Detailed Disbursements report fields](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement#report_fields).

## July 24, 2026

Feature

You can now use the Cloud Commerce Producer API to programmatically create, manage, and publish private offers. The API lets you automate your private offer workflows, including configuring custom pricing models, attaching EULA or SOW documents, and determining which active offer to amend.

For more information, see [Create and manage private offers using the API](https://docs.cloud.google.com/marketplace/docs/partners/offers/commerce-producer-api) and [Determine which offer to amend](https://docs.cloud.google.com/marketplace/docs/partners/offers/commerce-producer-api#determine-which-offer-to-amend).

## May 27, 2026

Change

We've reduced the processing and delivery delay for Google Cloud Marketplace partner reports from 2 days (D+2) to 1 day (D+1), accelerating by one day the delivery of the [Customer Insights reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight) to Cloud Marketplace partners.

For information about processing times, see [Customer Insights report frequency](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight#report_frequency)

## December 04, 2025

Feature

You can now offer Terraform Kubernetes apps through Google Cloud Marketplace with usage-based pricing, in which customers pay for your app based on their usage of Google Kubernetes Engine (GKE) resources, such as vCPUs, GPUs, TPUs, or memory. To set up usage-based pricing for your Terraform Kubernetes apps, see [Pricing models for Terraform Kubernetes apps](https://docs.cloud.google.com/marketplace/docs/partners/terraform-kubernetes#pricing). For information about how pricing works for GKE resources, see [GKE pricing](https://docs.cloud.google.com/kubernetes-engine/pricing?e=13802955).

## October 06, 2025

Change

We've updated the Cloud Commerce Procurement API's `GET Account` resource to provide the reseller parent Cloud Billing account ID for transactions associated with resold Cloud Billing accounts. For transactions on direct Cloud Billing accounts, no value is returned for the reseller parent Cloud Billing account id. For details, see the [Cloud Commerce Procurement API documentation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts/get).

## July 17, 2025

Feature

The [Detailed Disbursements](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement) and [Customer Incremental Insights](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight#turn-on-customer-incremental-insights) ISV reports are now available in BigQuery. These reports leverage BigQuery's [out-of-the-box connectors](https://docs.cloud.google.com/integration-connectors/docs/connectors/bigquery/configure) to aggregate your Google Cloud Marketplace data with other data sources for your analysis, reporting, and data visualization needs.

[Learn how to enable these new reports from the Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports).

## April 21, 2025

Feature

Google Cloud Marketplace has introduced:

  * An improved revenue share program for new Google Cloud Marketplace deals.
  * Four new Private Offer deal types that you can select when you create an offer: 
    * New
    * Migration
    * Native renewal
    * Channel shift



For more information, see the [Vendor Net Revenue Schedule](https://cloud.google.com/terms/marketplace-revenue-share-schedule). This revenue share program is only available to eligible Google Cloud Build partners and their respective Cloud Marketplace product listings. For eligibility criteria, see [Vendor Net Revenue Schedule requirements](https://docs.cloud.google.com/marketplace/docs/partners/migrations/variable-revenue-share#variable-revenue-share-requirements).

## March 13, 2025

Change

To improve data quality, we've updated the data source for the domain field in the [detailed disbursement](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement) and [insights](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight) reports.

## July 10, 2024

Change

We've made the following changes to Cloud Marketplace partner reports:

  * We've added a new field, `extraordinary_payment_note`, to the [detailed disbursement report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement).
  * If an extraordinary payment is issued, the [disbursements report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-disbursement) includes a new row that contains information about it, including metadata to track the payment.
  * The [customer insights report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight) includes two new fields, `marketplace_fee_amount` and marketplace_fee_percent`.



## June 17, 2024

Announcement

You can now create custom private offers with flexible payment options, including a duration of up to 5 years, with an annual ratable commit drawdown schedule, if applicable. For more information about creating custom private offers, see [Set up your offer's pricing](https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model).

## May 27, 2024

Feature

We've added a new field, `cancellation_reason`, on the Entitlement resource that provides context around why an entitlement was cancelled.

## April 26, 2024

Feature

We've added a new field, `wholesale_charges`, to [Detailed Disbursements reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement) and [Customer Insights reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight) for Cloud Marketplace.

## April 25, 2024

Feature

You can now create multiple orders for the same product with flat fee pricing. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information about creating multiple orders, see [Create multiple orders of the same product](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-multiple-orders).

## April 22, 2024

Announcement

We've made the following updates to the the provider Entitlement resource:

  * A new field called `new_offer_start_time` is populated with the start time of an offer that's scheduled to start in the future. This field works the same way as the field in the Pub/Sub messages.
  * The existing field named `new_offer_end_time` is now also populated when an offer with a specified end date activates. The field is now empty only if the offer was created with a term instead of a specified end date, or if there is no upcoming offer.



## April 17, 2024

Announcement

We've made the following changes to Cloud Marketplace reports:

  * A new field, `offer_title`, has been added to the [Detailed disbursements report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement) and the [Customer Insights report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight).
  * The `entitlement_id` field from the Detailed disbursements report is now also available in the Customer Insights report.



## April 11, 2024

Announcement

If you've turned on [Marketplace reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-types) in Producer Portal, you now receive proactive email notifications from Google when reports are delayed, have inaccurate data, or have been regenerated. For steps to set up reports and receive these notifications, see [Set up to receive reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports).

## March 04, 2024

Change

When you create a new private offer, or replace an existing private offer, you select a payment frequency for how your customer is charged. This can be monthly, quarterly, annually, or custom. For more information, visit [Payment frequency for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule).

## March 01, 2024

Feature

You can now access **Detailed disbursements reports** with detailed breakdowns of the amount paid to you, for accounting and financial reconciliation purposes. For details, see [Detailed disbursements reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-detailed-disbursement).

## October 01, 2023

Change

Beginning in October 2023, Google Cloud Marketplace supports a new transaction model, the agency model. For details about the agency model and which transactions it applies to, see the [transaction models](https://docs.cloud.google.com/marketplace/docs/partners/transaction-models) documentation.

## September 25, 2023

Change

Your Customer Insights reports contain a new field, `transaction_type`. For more details, see [the field's documentation](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight#additional_information_for_the_agency_transaction_model).

## July 24, 2023

Change

We've made the following improvements to reports for Cloud Marketplace products:

  * We've added a `solution_name` column to Customer Insights reports, which contains the title of the listing that the SKU charge corresponds to. You can use this information to differentiate between identically-named SKUs from different product listings. For more information, visit the [Customer Insights report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight) documentation.

  * We've added a **Postpay Credits** column to Charges and Usage reports, and a `postpay_credits` column to Daily Insights reports and Monthly Insights reports. These columns indicate, as a number less than or equal to 0, how much of the amount charged was offset by commitment credits purchased through a private offer with a postpay payment schedule. These applied credits reduce the amount disbursed to you for the charges that they're applied to, as the payout comes from the charge for the commitment SKU. For more information, visit the [Charges and Usage report](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-charges-usage) documentation.




## July 19, 2023

Change

We've redesigned the [Private Offers](https://docs.cloud.google.com/marketplace/docs/partners/offers) experience to improve offer creation and management, including the following changes:

  * You can fill in information in any order, instead of having to enter it all at once.
  * We've added sectional cards with icons that show completion status, so that you can get a high-level overview of an offer from a single page.
  * We've added a summary panel showing key changes to deals.
  * We've made improvements to increase the product's adaptability and usability.



## June 05, 2023

Change

Independent software vendors (ISVs) offering their products through Cloud Marketplace can now offer discounts for reseller partners who sell their products to customers. For details, see [Configure discounts for resellers](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-incentives) and [Request a reseller discount from an ISV](https://docs.cloud.google.com/marketplace/docs/partners/resellers/request-incentive).

## May 08, 2023

Feature

When you create or amend a prepay private offer with the committed use discounts (CUDs) pricing model, you can choose whether unused commitment expires or rolls over between installments of the offer. You can also choose to add one-time credits that you sponsor to specific installments. For more information, visit [Set up your offer's pricing](https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model#pricing_and_payment_details).

## February 06, 2023

Feature

As part of a limited Preview program, you can [turn on automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for software as a service (SaaS) products. This enables you to schedule specific start dates for new private offers, or amendments to existing private offers.

## January 23, 2023

Change

You now receive an `ENTITLEMENT_OFFER_ACCEPTED` Pub/Sub message when a customer accepts a private offer. For details, refer to [List of event types for account tasks](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration#eventtypes).

## November 18, 2022

Feature

You can [download private offers as PDFs](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-private-offers#download-offer). Offers can be saved at any point in the offer process and can include internal notes and the EULA for the offer.

## November 07, 2022

Announcement

After your organization enrolls in [Partner Advantage portal](https://docs.cloud.google.com/partners/become-a-partner), you can start integrating your products with Google Cloud Marketplace and preparing to publish them at the same time that your organization completes the process of becoming an approved Google Cloud Build partner.

## September 28, 2022

Change

When you create a private offer for a customer, the offer expires at 11:45 PM US and Canadian Pacific Time (UTC-8) on the offer acceptance deadline, instead of 12:00 AM UTC-8.

## September 15, 2022

Feature

You can now provide Private Offers with more granular discounts on specific usage metrics to your customers by [enabling metric discounts](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers).

## July 26, 2022

Announcement

Private Offers, version 2, is now **generally available**. Customize quotes for specific customers, including offering flat fee, usage, and installment discount types.

To get started, see [Choosing your private offer pricing](https://docs.cloud.google.com/marketplace/docs/partners/offers/private-offer-pricing)

## July 14, 2022

Feature

Manage your private offers, including approving an offer, by using the [Private Offers page](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-private-offers).

## June 06, 2022

Announcement

If you've created [private offers that use a prepay payment schedule](https://docs.cloud.google.com/marketplace/docs/partners/offers/private-offer-pricing#payment-schedule), you see [new fields when you manage entitlements](https://docs.cloud.google.com/marketplace/docs/partners/offers/backend-integration#managing_entitlements) with the Partner Procurement API, and also [additional information in your Customer Insights report](https://docs.cloud.google.com/marketplace/docs/partners/reporting#additional_information_for_prepay_offers).

## May 25, 2022

Change

When creating software as a service (SaaS) products, the roles granted to `cloud-commerce-procurement@system.gserviceaccount.com` have changed.

The **Service Management Service Consumer** and **Service Management Service Controller** roles replace the **Service Management Admin** and **Service Usage Admin** roles. The previous roles are still valid, but new projects require that you grant the **Service Management Service Consumer** and **Service Management Service Controller** roles to `cloud-commerce-procurement@system.gserviceaccount.com`.

## February 07, 2022

Change

The deprecated `product` field on the provider [`Entitlement`](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements) resource has been updated. The field now correctly populates the product, quote, or offer depending on the entity that was purchased. If you want to use other fields to view this information, see [REST Resource: `providers.entitlements`](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements).

## September 28, 2021

Feature

You can now use Producer Portal's new guided configuration option to create deployment packages for your VM products directly in the Cloud Console.

## August 13, 2020

Feature

Google Cloud Marketplace supports filters, called Category IDs, that are available to customers within the Google Cloud console. When you add a Category ID, your solution shows up in the filtered view for that category when customers search for solutions in Cloud Marketplace. You can select up to two categories for each of your solutions.

To add or modify categories, go to the **Solutions Details** page and edit the **Category ID** section.

## April 16, 2020

Feature

You can now create private quotes for VM solutions ([alpha](https://cloud.google.com/products/?hl=EN#product-launch-stages)).

[Learn about creating quotes for specific customers](https://docs.cloud.google.com/marketplace/docs/partners/create-quotes).

## April 01, 2020

Feature

If you sell Kubernetes apps on Google Cloud Marketplace, you can now configure your app to target clusters where at least one node has a GPU. When users deploy the app, only clusters with GPUs are shown as valid deployment targets.

[Learn about modifying your app's `schema.md` to check for GPUs](https://github.com/GoogleCloudPlatform/marketplace-k8s-app-tools/blob/master/docs/schema.md#gpus).

[Read the overview of selling Kubernetes apps on Google Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions).

## January 27, 2020

Feature

If you sell Managed Services on Google Cloud Marketplace, you can now monitor your solution's analytics and track your marketing campaigns on the [Solution Analytics page](https://console.cloud.google.com/partner/analytics?_ga=2.65050663.883067678.1580151692-404355855.1580151692).

For information on interpreting the metrics and setting up tracking campaigns, see [Monitoring your solution's analytics](https://console.cloud.google.com/partner/analytics?_ga=2.65050663.883067678.1580151692-404355855.1580151692).

## December 10, 2019

Change

The SKUs for GCP Marketplace's VM solutions are changing, which may affect the data shown in your reports:

  * In your Customer Insights reports, the `sku_id` and `sku_description` columns will show new values to reflect the change in SKU.

  * If your VM solution is priced by usage, the usage report now shows only the resources that you use to set your price. For example, if you set your price by CPU usage, the report will only show information about the user's CPU usage.




For more information on the reports that you receive, see [Payments and reports](https://docs.cloud.google.com/marketplace/docs/partners/reporting).

## November 14, 2019

Feature

Private Pricing is now Generally Available (GA). With GCP Marketplace Private Pricing, you can create custom quotes for specific customers for Kubernetes applications or Integrated SaaS solutions.

To get started, see [Creating quotes for specific customers](https://docs.cloud.google.com/marketplace/docs/partners/create-quotes).

## October 31, 2019

Feature

**Application Manager (Beta)** : If you offer Kubernetes applications on GCP Marketplace, you can now enable managed updates for the application.

With managed updates, your users can update to new releases of your application from the GCP Console with a few clicks.

[Learn about supporting managed updates for your Kubernetes applications](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions/support-managed-updates).

## September 25, 2019

Feature

You can now receive your reports in a Google Drive folder, Cloud Storage bucket, or both. For steps to set up your reports, see [Payments and reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports).

## May 21, 2019

Feature

If you are selling managed services (Integrated SaaS) solutions, you can now offer subscription plans for specific periods. For example, you can create a subscription plan for users who sign up for one year, three years, or more.

Learn more about [selling managed services on GCP Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas).

## May 17, 2019

Feature

For your Kubernetes applications, you can now [set up your pricing model in Partner Portal](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions/select-pricing#add-in-partner-portal).

## May 10, 2019

Feature

If you sell Managed Services or Kubernetes applications on GCP Marketplace, you can now offer trials of your software. For information on setting up trials, see:

  * [Choosing a pricing model for Kubernetes Solutions](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions/select-pricing)
  * [Choosing a pricing model for Managed Services](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing)



## April 23, 2019

Change

We recommend using the [open source `deploymentmanager-autogen` tool](https://github.com/GoogleCloudPlatform/deploymentmanager-autogen) to generate Deployment Manager templates. With Autogen, your deployment package includes the following capabilities:

  * Quota checks for CPUs and GPUs, so that users cannot deploy your solution if they exceed the quota requirements.
  * Dynamic price updates in the Deployment Manager page.
  * Prevents users from choosing GPUs that are not available in the zone that they choose.



Learn more about [distributing VM-based solutions on GCP Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/vm).

Deprecated

GCP Marketplace no longer accepts new Standalone SaaS solutions. For information about your options, contact the Partner Onboarding team at [cloud-partner-onboarding+ss@google.com](mailto:cloud-partner-onboarding+ss@google.com). Learn more about [the solutions that you can distribute on GCP Marketplace](https://docs.cloud.google.com/marketplace/docs/partners#supported-solutions).

## April 09, 2019

Feature

Kubernetes applications on GCP Marketplace are now **Generally Available**.

For an overview of selling containerized applications on GCP Marketplace, see [Distributing Kubernetes Applications](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions).

Feature

You can now distribute Kubernetes applications that run on GKE On-Prem clusters, and clusters that run [Istio](https://istio.io/).

Review the [requirements to support GKE On-Prem](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions/create-app-package#on-prem-reqs), and the [considerations for making your application compatible with Istio](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions/create-app-package#istio-limitations).

## November 16, 2018

Feature

The documentation has been updated with information on selling Integrated SaaS solutions on Google Cloud Platform Marketplace. Integrated SaaS solutions are software solutions that run on your infrastructure, regardless of location, but are billed by Google.

For an overview of selling Integrated SaaS solutions on GCP Marketplace, see [Selling Managed Services](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas).

## November 01, 2018

Feature

Your monthly reports now include a Customer Insights report, which includes information on how your customers are using your software on GCP.

For information on Customer Insights reports, see [Customer Insights reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight).

## September 28, 2018

Feature

The documentation has been updated with steps to distribute Kubernetes applications on Google Cloud Platform Marketplace.

For an overview of selling containerized applications on GCP Marketplace, see [Distributing Kubernetes Applications](https://docs.cloud.google.com/marketplace/docs/partners/kubernetes-solutions).

## July 23, 2018

Feature

If you sell VM solutions on GCP Marketplace, you can now offer trials of your software. For information on setting up trials, see the [technical setup for VM solutions](https://docs.cloud.google.com/marketplace/docs/partners/vm/select-pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
