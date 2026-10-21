---
url: https://docs.cloud.google.com/billing/docs/how-to/purchase-order/
title: Update your purchase order number on your invoices \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:13.625959+00:00
---

# Update your purchase order number on your invoices  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/purchase-order/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Update your purchase order number on your invoices Stay organized with collections  Save and categorize content based on your preferences. 

A purchase order number (also called PO number, IO number, CPE, or client code) is an identifier that appears in the header of your invoices. This document describes how to view, set, or update the purchase order number associated with your [_invoiced_ Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

**Note:** Purchase order numbers don't apply to [_self-serve/online_ Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

### Permissions required to manage purchase order numbers

To set or update the purchase order number used for your invoiced Cloud Billing account, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on the Cloud Billing account:

  * [`billing.accounts.update`](https://docs.cloud.google.com/billing/docs/how-to/billing-access)



To gain this permission using a predefined role, ask your administrator to grant you the role of [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on your Cloud Billing account.

For more information about billing permissions, see the following:

  * [Overview of access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



### View the purchase order associated with your invoiced billing account

To view the purchase order that is on each invoice, do the following:

  1. In the Google Cloud console, open your Cloud Billing account and go to the **Documents** table on the **Payment status** page.

[Go to the billing account](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** you want to view. The Billing Overview page opens.

  3. In the Billing navigation, select **Payment status** (available for _invoiced_ Cloud Billing accounts).

  4. On the **Payment status** dashboard, click **View all invoices and memos** to open the documents table.

  5. In the **Documents** table, look for the **Purchase order** column. If the value is blank for any invoice, this indicates that no purchase order number was set on the Cloud Billing account at the time that the invoice was generated.




### Set or update your purchase order number

To set or update the purchase order number that is associated with your invoiced Cloud Billing account, complete the following steps:

  1. In the Google Cloud console, go to the **Payment status** page, available for _invoiced_ Cloud Billing accounts.

[Go to the Payment status page](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** you want to view. The Billing Overview page opens for the billing account.

  3. In the Billing navigation, select **Payment status**.

  4. On the **Payment status** page, click edit **Set purchase order number**.

  5. Enter the new purchase order number.

  6. Click **OK**.




The new purchase order number is associated with _subsequent_ invoices when those invoices are generated. To update the purchase order number on a previously generated invoice, regenerate the invoice.

If you're on the **Payment status** page of your Cloud Billing account and you don't see or can't access the edit **Set purchase order number** button, the reasons could include the following:

  * The Cloud Billing account you are viewing isn't configured to be paid by invoice, but rather is an automatically paid, [self-serve/online account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). Purchase order numbers can only be set on Cloud Billing accounts that are configured as an [invoiced account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).
  * You don't have the Cloud Billing account permissions needed to set or update the purchase order number associated with your invoiced account. Contact your Cloud Billing account administrator.



### Update the purchase order number on previously issued invoices

To change the purchase order number on invoices that have already been issued, you can request a change to one or more invoices using the **Dispute or change invoices** form. After you submit the form, your invoices will be regenerated with the updated purchase order number.

To update the PO number on your invoices, do the following:

  1. In the Google Cloud console, go to the **Payment status** page, available for _invoiced_ Cloud Billing accounts.

[Go to the Payment status page](https://console.cloud.google.com/billing/overview)

  2. At the prompt, **choose the Cloud Billing account** you want to view. The Billing Overview page opens for the billing account.

  3. In the Billing navigation, select **Payment status**.

  4. On the **Payment status** dashboard, click **View all invoices and memos** to open the documents table.

  5. Select the checkbox next to each issued invoice that you want to update.

  6. From the **Actions** menu, select **Dispute or request a change**.

The **Dispute or change invoices** form opens.

  7. From the **What do you want to change** options, select **PO number**.

  8. If you selected multiple invoices to update, in the **How do you want to change these invoices?** section, choose one of the following options:

     * **Use one PO number for all invoices** : Apply the same new PO number across all of the selected invoices.
     * **Use one PO number per invoice** : You can specify a different PO number for each selected invoice.
  9. In the **What should the new PO number be?** section, enter the new PO number(s).

  10. Complete the contact information as needed.

  11. Click **Continue**.

  12. Review the details of your request. If all is correct, click **Submit**.

If you need to make changes, select **Back** to return to the editable form.




After you submit your request, if the invoices are eligible for automatic regeneration, the updates will appear in your _Payment status_ documents table and you will receive the updated invoices by email within 24 hours. Otherwise, we will review your request within 2 business days and send an update by email.

If after 48 hours you don't see the updated purchase order number on your regenerated invoices, [contact Customer Support](https://docs.cloud.google.com/support/docs/get-billing-support).

**Note:** Using the change form to update the purchase order numbers on previously issued invoices won't change the default purchase order number associated with your invoiced billing account.

## Related topics

  * [Get an invoice, statement, or receipt](https://docs.cloud.google.com/billing/docs/how-to/get-invoice)
  * [Understand your monthly invoice](https://docs.cloud.google.com/billing/docs/how-to/read-invoice)
  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [Split invoicing for agency model transactions](https://docs.cloud.google.com/billing/docs/how-to/split-invoice)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-10 UTC."],[],[]] 
