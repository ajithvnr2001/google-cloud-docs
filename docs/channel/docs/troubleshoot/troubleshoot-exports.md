---
url: https://docs.cloud.google.com/channel/docs/troubleshoot/troubleshoot-exports/
title: Troubleshoot issues with BigQuery exports \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:43.452005+00:00
---

# Troubleshoot issues with BigQuery exports  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/troubleshoot/troubleshoot-exports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Support ](https://docs.cloud.google.com/channel/docs/support)



Send feedback 

#  Troubleshoot issues with BigQuery exports Stay organized with collections  Save and categorize content based on your preferences. 

This page presents common issues you might encounter when using the Partner Sales Console to export rebilling data to BigQuery, and how to resolve these issues.

## No values for billable costs

Rows that represent taxes, adjustments, and rounding are specific to your invoice reconciliation process and do not contain values for billable costs to customers or channel partners.

## Charges without list costs

Some charges (for example, support charges) do not have an associated list cost. Repricing configurations for these charges that use the _List Cost_ rule will use the base cost to calculate the repriced cost.

When you create a BigQuery export using the Partner Sales Console, the line item for these types of charges will show `null` in the `cost_at_list` column. This may lead to a discrepancy when viewing the charge in the export and when viewing it on the Google Cloud console.

To resolve this issue, use `SUM(IFNULL(cost_at_list, cost))` instead of `SUM(cost_at_list)` when you query a rebilling export.

## Taxes in exported data

Taxes for every billing subaccount associated with your primary billing account are calculated based on the location listed in your account details. Your customers' locations will not affect taxes charged to their accounts.

If a billing subaccount has their `cost_type` set to `'tax'`, exported data will show our attribution of your local tax rate as it applies to that account. This value is based on the customer's portion of usage and any additional costs they incur.

### Null values for costs

Any rows in your exports that have a `cost_type` of `'tax'` will show `null` in the `customer_cost` and `channel_partner_cost` fields. Before you generate an invoice for this type of customer, make sure you review these rows and verify the correct values are in place.

## Unassigned and unassociated subaccounts

Creating a Google Cloud entitlement and linking it to a customer creates a billing subaccount for that customer. If you don't create this entitlement you may see unassigned billing subaccounts under your main billing account.

Using the Partner Sales Console to remove a customer that has assigned billing subaccounts will cause those subaccounts to become unassociated.

### Null values for subaccounts

[Using BigQuery to export data](https://docs.cloud.google.com/channel/docs/troubleshoot/channel/docs/rebilling/export-data-to-bigquery) that includes unassigned or unassociated subaccounts will cause the following columns to show a value of `null` for those subaccounts.

  * entitlement_name
  * customer_name
  * customer_cost
  * credits.customer_amount
  * channel_partner_name
  * channel_partner_cost
  * credits.channel_partner_amount



To resolve this issue, you should [assign these billing subaccounts to customers](https://support.google.com/channelservices/answer/10022594).

## Restoring export table to a previous state

If you accidentally dropped your export table or deleted some of its data, or if you want to revert the table to a previous state, you can recover it using the BigQuery [time travel](https://docs.cloud.google.com/bigquery/docs/time-travel) feature. For example, you can run the following command to restore the table to a previous state:
    
    
    bq cp PROJECT_ID:DATASET_ID.reseller_billing_detailed_export_v1@REVERT_TO PROJECT_ID:DATASET_ID.reseller_billing_detailed_export_v1
    

REVERT_TO represents the time, in seconds from the Unix epoch, that you want to revert to. Note that you can only go back up to 7 days, and your data isn't backfilled.

## Export is not adding new data

If no new rows are appearing in your export, there are several issues that could prevent it from working:

### You recently enabled exports

After exports are enabled, it might take up to a day for your usage to appear in your tables. If nothing is there for any longer than that, consider the other potential issues here.

### The dataset cannot be accessed by the service account

The dataset can't be updated if our service account doesn't have access to it. You can update this automatically by clicking update on the [Billing Export](https://channelservices.cloud.google.com/billing/billing-export) page in the Partner Sales Console.

### Billing is not enabled for the project

The export can stop working if billing is not enabled for your project. Follow [these instructions](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project) to enable billing. If you're using the [BigQuery Sandbox](https://docs.cloud.google.com/bigquery/docs/sandbox#upgrade), you must upgrade your account.

### Row or column-level access is enabled on the dataset

If the dataset has [row-level](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) or [column-level](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) access control, the export will fail. To re-enable, [delete the row-level access policy](https://docs.cloud.google.com/bigquery/docs/managing-row-level-security#delete_row-level_access_policies) and the [column-level access policy](https://docs.cloud.google.com/bigquery/docs/column-level-security#clear_policy).

### You have no parent Cloud Billing accounts

The export doesn't work if there are no parent Cloud Billing accounts to export. If product families don't have associated Cloud Billing accounts, they're automatically turned off. To fix this, ensure that there are active Cloud Billing accounts for your selected data source.

### The export has an invalid schema

It is not supported to modify the [schema](https://docs.cloud.google.com/channel/docs/rebilling/export-data-to-bigquery#table_schema) of the export table. If you want to add or remove columns, you can create a [view](https://docs.cloud.google.com/bigquery/docs/views-intro) or a [materialized view](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro), or you can join against your other tables in your queries. If your table gets in this state, you will need to revert it back to having all the correct columns and nothing else.

### Re-enabling your export

After you have found and remedied the issue, go to the [Billing Export](https://channelservices.cloud.google.com/billing/billing-export) page in the Partner Sales Console. Notice the error on the page saying that your export is disabled.

To re-enable your export, click **Update**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
