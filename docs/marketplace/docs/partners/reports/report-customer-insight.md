---
url: https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight/
title: Customer Insights reports \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:27.480312+00:00
---

# Customer Insights reports  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/reports/report-customer-insight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Customer Insights reports Stay organized with collections  Save and categorize content based on your preferences. 

We provide a daily and monthly _customer insights report_ , which includes information about who your customers are, and how they are using your software. To access the customer insights report, visit the destination or the BigQuery dataset that you specified when you [set up to receive reports](https://docs.cloud.google.com/marketplace/docs/partners/reports/set-up-reports).

When a customer sets up their Cloud Billing account, they choose whether it's a business account or a personal account. We exclude identifying information from the customer insights report for those accounts that the customer identified as personal accounts. For those accounts, you see `n/a` in the columns.

## Report frequency

The daily reports are generated on a one-day delay, based on Pacific Time (PT). For example, the report for June 1, 2026 is generated on June 2, 2026. The monthly report is generated on the first calendar day of the subsequent month.

## Customer incremental insights reports

Optionally, you can turn on customer incremental insights reports to get more detailed versions of customer insights reports at the destination that you configured. Customer incremental insights reports contain all of the same information as customer insights reports, and also any usage from previous dates that wasn't included in previous reports. You might encounter this if you report usage to Google late, or if there are issues with Google's internal billing processes that delay the reporting.

We strongly recommend that you turn on customer incremental insights reports, because they provide a more accurate picture of your customers' usage than non-incremental customer insights reports, and aid your reconciliation of reported usage with the monthly disbursement reports.

### Turn on customer incremental insights reports

If you've enabled BigQuery export, you've turned on customer incremental insights reports, and you don't need to take any additional action.

To turn on customer incremental insights reports in CSV Export, complete the following steps:

  1. In Producer Portal, visit the [Reports page](https://console.cloud.google.com/producer-portal/partner-report).

  2. Under **Configure reports** , select the report destination for which you want to turn on customer incremental insights reports.

  3. Under **Reports to export** , select the **Customer incremental insights** checkbox.




### Understand customer incremental insights reports

The following example shows how Cloud Marketplace handles usage that you report late, after you've turned on customer incremental insights reports:

  1. On June 1, 2026, your customer uses your product, but you don't report all or part of their usage.

  2. On June 2, 2026, Cloud Marketplace generates a Customer incremental insights report that includes all known data for June 1, 2026. Because you didn't report the previous usage from June 1 to Google, Cloud Marketplace doesn't include that usage in this report.

  3. On June 10, 2026, you report the usage from June 1, 2026 that you previously didn't report.

**Caution:** If you didn't turn on Customer incremental insights reports, the Customer insights report that Cloud Marketplace generates doesn't include the newly-reported previous usage.



In this example, the report named `2026-06-09 Incremental Daily Insights` in CSV Export, or BigQuery table `marketplace_report.incremental_insights` with `_PARTITIONDATE` as `2026-06-09`, has a column labeled `date`. One row has a value of `2026-06-01` for `date`, and the rest of the rows have a value of `2026-06-09` for `date`. You also see a new column labeled `report_date`, which has a value of `2026-06-09` for all rows, indicating that this report is intended for June 9, 2026. Depending on how you use data from reports, you might want to update your integrations to account for the new `report_date` field.

To track all usage of your products by a customer for a specific day or month, you might need to combine the rows for that day or month from across multiple Customer incremental insights reports.

For incremental monthly insights reports, like the usage data for June 2025, the naming conventions differ based on the export type. In a CSV export, the file is named `2025-06-01 Incremental Monthly Insights`. In a BigQuery export, the data is in the table `marketplace_report.incremental_monthly_insights` with `_PARTITIONDATE` as `2025-07-01`.

## Report fields

The sales report contains the following information, starting from July 13, 2018:

**Field** | **Description**  
---|---  
`report_date`(only for customer incremental insights report) | The primary date/month for which the report was generated, in US and Canada Pacific Time (the report was generated a few days after this date). You see this field after you turn on customer incremental insights reports. Each report has only one value for this field, which might be different from the date on which the usage happened. If you've imported your report into a database, you can use this to find all the rows for a specific report.  
`date` | The date/month when usage happened, in US and Canada Pacific Time. If you've turned on customer incremental insights reports, this date might match the `report_date`, or might be further in the past, if the usage was reported late.  
`company` | The customer's company name. For transactions that involve vendors reselling Cloud Marketplace products, this is the name of the vendor reselling the products to the customer. If the customer is using a personal account, the company name is excluded from the report.  
`domain` | The value of the `website` field for this account in Google's CRM system. For transactions that involve vendors reselling Cloud Marketplace products, this is the domain linked to the account of the reselling vendor. If the customer is using a personal account, we exclude the domain from the report.  
`external_account_id` | The Insights account ID, generated for the Cloud Billing account associated with the customer's project. This field is present for all customers, even those with personal accounts. You can use it to track revenue for the customer over time, free-to-paid conversion, and customer churn.  
`account_id` | The Cloud Billing account associated with the customer. If the customer is using a personal account, the account ID is excluded from the report.  
`country` | The customer's country.  
`state_or_province` | The customer's state or province, if applicable.  
`city` | The customer's city, if applicable.  
`postal_code` | The customer's postal code, if applicable. If the customer is using a personal account, the postal code is excluded from the report.  
`sku_id` | The SKU that the customer was charged for. Depending on how a product is configured, a single deployment might have multiple SKU IDs. For example, one SKU might cover the cost of using CPUs in the deployment, and another SKU ID might cover the cost of using RAM.  
`sku_description` | The description of the SKU. For example, if a customer deployed a WordPress product that charged by the number of CPU cores, the SKU description is similar to "Licensing Fee for Click to Deploy Wordpress (CPU cost)".  
`usage` | The quantity of resources used by the customer.  
`unit` | The metric that usage is measured as, such as hour or gibibyte hour.  
`currency` | The currency that you are paid in.  
`charges` | The charges that the customer was billed for during the period, in your currency.  
`due_vendor` | The amount that you receive for the usage. This is computed as `(charges - trial_use + prepay_credits + postpay_credits) * revenue share`. We add `prepay_credits` and `postpay_credits` because their values are negative numbers, when present. We subtract `trial_use` because its value is a positive number, when present.  
`trial_use` | Trial credits, coupon-created credits, and [product testing credits](https://docs.cloud.google.com/marketplace/docs/partners/testing-products#set-up-test-billing-account) consumed, if applicable.  
`num_vms` | The number of VMs that the customer has deployed the product on.  
`num_cpus` | The number of vCPU cores in the customer's deployment. If the number is a fraction, it indicates that the customer chose a [shared vCPU](https://docs.cloud.google.com/compute/docs/machine-types#sharedcore) machine type.  
`ram_mb` | The size of the RAM in the customer's deployment.  
`num_gpus` | The number of GPUs in the customer's deployment.  
`gpu_types` | A space-separated list of the GPU types in the customer's deployment. For example, the value "`NVIDIA_TESLA_P4 none NVIDIA_TESLA_P100`" indicates that at least one VM used an NVIDIA® Tesla® P4, at least one used a P100 GPU, and at least one VM had no GPU. For a list of GPUs available on Compute Engine, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).  
`earliest` | The earliest date (UTC) on which the customer created a VM that was live during the reporting period.  
`latest` | The latest date (UTC) on which the customer created a VM that was live during the reporting period.  
`machine_spec_sum` | A space-separated list of new and total counts per [machine type](/compute/docs/machine-types). For example, the value "`F1_MICRO:0/1 G1_SMALL:2/3`" indicates that 1 `f1-micro` VM and 3 `g1-small` VMs were used during the current period, of which 0 `f1-micro` VMs are new and 2 `g1-small` VMs are new.   
`quote_id` | If you've generated revenue from a private offer, the offer ID associated with the offer's product and billing account. (Older private offers were known as quotes, and we've kept the name for continuity of report processing.)  
`quote_creator` | If you've generated revenue from a private offer, the email address of the offer creator.  
`internal_note` | If you've generated revenue from a private offer, an optional internal note for the offer. You can use internal notes to tag offers for additional processing, such as tracking the revenue and/or usage data they generate. You specify the internal note when you create the offer.  
`usage_metric_discount_percent` | If the usage is related to a private offer that includes metric discounts for this SKU, then this is the discount percentage that can be applied, depending on the pricing model of the offer. This discount can apply to all usage or only to usage considered _overage_ , as determined by the terms of the offer. If there is no metric level discount for this SKU in the associated offer, the value is `NULL`.  
`payment_type` | The means by which you will receive the disbursement: If it is `old`, you receive payments from Google US or a regional Google entity to your US-based bank account. If it is `new`, you receive a single payment to your local bank account.  
`withheld` | If a Google Cloud customer's Cloud Billing account is placed on probation due to lack of payment, Google withholds disbursements until the account is back in good standing. This column tells you how much we would have paid you if we had collected it from the customer. When the billing account is back in good standing, we release the withheld funds in the next payment to you. If it never returns to good standing, we abandon the withheld funds.  
`released` | If Google had withheld funds, this column shows the total of the funds that are now released to you because the customer's billing account is back in good standing.  
`abandoned` | If Google had withheld funds, this column shows total of the funds are abandoned because we have terminated the billing account.  
`probation_start` | The first day that Google started withholding funds, in `YYYY-MM-DD` format, in US and Canada Pacific Time. If we're releasing or abandoning funds, this might be in an earlier month. If the account is still on probation, this is the first day in the current month where we withheld funds, but we might have started withholding before this.  
`probation_end` | The last day that Google withheld funds, in `YYYY-MM-DD` format, in US and Canada Pacific Time. The day after this, the account either returned to good standing, or we closed it. If this is blank, then the account is still on probation.  
`start_date` | The first day that the entitlement is active, in `YYYY-MM-DD` format, in US and Canada Pacific Time. The date is determined by the associated subscription or private offer for the entitlement. If the entitlement was created before `2021-01-10`, the value is `NULL`.  
`end_date` | The last day that the entitlement is active, in `YYYY-MM-DD` format, in US and Canada Pacific Time. The date is determined by the associated subscription or private offer for the entitlement. If the entitlement was created before `2021-01-10`, the value is `NULL`.  
`solution_name` | The name of the product that the customer is charged for.  
`postpay_credits` | The amount of `charges` that were covered by a [commitment credit](https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model#pricing_and_payment_details) purchased through a postpaid commitment. If present, it's a negative number that reduces the `due_vendor` amount, because it reduces the amount used to compute disbursement to you.  
`marketplace_fee_percent` | The percentage fee that Cloud Marketplace keeps as part of your revenue share agreement with Google.  
`marketplace_fee_amount` | The amount of the fee that Cloud Marketplace keeps as part of your revenue share agreement with Google.  
**Note** : You might see different values for usage in the customer insights report and the detailed disbursement report. This difference is because the detailed disbursement report includes usage that was _reported_ by the service during the covered month, while the customer insights report includes usage that _started_ during the month. This can result in different numbers when the usage occurs at the end of a month. 

For example, if a customer starts using your software on March 31 at 10 PM PT, and ends on April 1 at 3 AM, the 5 hours of usage are reported on April 1, and are shown on April's detailed disbursement report. However, because the usage started in March, it's shown in the customer insights report for March.

The difference in calculation ensures that if a usage report from your service or one of Google's services is delayed, you're still paid the correct amount.

## Additional information for private offers

If you've [created private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers) for specific customers, you might see the following additional information:

**Field** | **Description**  
---|---  
`payment_schedule` | The type of payment schedule for the offer. This can have the value `PREPAY`, `PREPAY_INSTALLMENTS`, or `POSTPAY`.  
  
**Note:** For private offers which use [ billing frequency](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule) (monthly, quarterly, annually or custom) instead of payment schedules at the time of their creation, this field is empty. For these offers, we recommend that you use the `billing_frequency` column instead.  
`private_offer_acceptance_date` | The date that the private offer was accepted by the customer.  
`private_offer_total_contract_value` | The total amount that the customer pays across all installments of the private offer.  
`term_total_contract_value` | The total amount that the customer pays across all installments of the offer's current term.  
`order_start_date` | The date that the private offer pricing takes effect.  
`order_end_date` | The date that the private offer pricing is no longer in effect.  
`billing_frequency` | Describes the recurring billing interval that was selected when the offer was created. Can have the value `monthly`, `quarterly`, `yearly`, `pay_go`, or `custom`.  
  
**Note:** For private offers which use payment schedules (prepay or postpay) instead of [ billing frequency](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule) (monthly, quarterly, annually or custom) at the time of their creation, this has the value of `prepay` or `postpay `.  
`installment_count` | The number of installments in the offer's current term.  
`first_installment_date` | The start date of the first installment of the offer's current term, in `YYYY-MM-DD` format.  
`final_installment_date` | The end date of the final installment of the offer's current term, in `YYYY-MM-DD` format.  
`prepay_credits` | The amount of `charges` that were covered by a [commitment credit](https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model#pricing_and_payment_details) purchased through a prepaid commitment. If present, it's a negative number that reduces the `due_vendor` amount, because it reduces the amount used to compute disbursement to you.  
`offer_title` | The text that you enter in the private offer's `Offer Title` field when you create the offer. This is visible to your customers. If the customer has purchased multiple private offers for the same product using the same Cloud Billing account, you can use this field to differentiate between those offers in your offer table and reports. For private offers that were created before this field was made available, this field has been backfilled with the product name for the offer.  
`entitlement_id` | Offer entitlement ID associated with the purchase made by the customer. If the customer has purchased multiple private offers for the same product using the same Cloud Billing account, you can use this field to differentiate between those offers in your offer table and reports.  
  
## Additional information for resold products

If you've [enabled reselling for your Cloud Marketplace products](https://docs.cloud.google.com/marketplace/docs/partners/resell/set-up-reselling), you might see the following additional information:

**Field** | **Description**  
---|---  
`channel` | Indicates whether the usage is for a product purchased directly from an independent software vendor (ISV) or through another company reselling an ISV's products.  
`reseller_discount` | The amount of the [reseller discount](https://docs.cloud.google.com/marketplace/docs/partners/resell/reseller-incentives) configured by the ISV.  
`parent_account_id` | The billing account associated with the reseller for this usage.  
`wholesale_charges` | For resold private offers (the `channel` field has a value of `RESOLD`), this shows the value: `charges - reseller_discount`.  
For private offers made directly to end customers (the `channel` field has a value of `DIRECT`), this field has the value `NULL`.  
  
## Additional information for the agency transaction model

**Field** | **Description**  
---|---  
`transaction_type` | Describes the relationship between the buyer, seller, and Google for the transaction. This can have the value `THIRD_PARTY_RESELLER` (Google is selling the ISV's products directly), or `THIRD_PARTY_AGENCY` (Google is acting as an agent for the seller).  
**Note:** As we add features and make improvements to Cloud Marketplace, we add columns as needed to existing reports. If you set up any automated processing of your reports, you should configure it so that it operates based on the names of the columns, and doesn't depend on the total number of columns staying the same.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
