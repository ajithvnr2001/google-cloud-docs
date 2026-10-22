---
url: https://docs.cloud.google.com/billing/docs/how-to/get-invoice/
title: Get a Cloud Billing document such as an invoice, statement, or receipt \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:40.919597+00:00
---

# Get a Cloud Billing document such as an invoice, statement, or receipt  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/get-invoice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Get a Cloud Billing document such as an invoice, statement, or receipt Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to find all of the Cloud Billing documents that are available for your [Cloud Billing account type](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

## About Cloud Billing documents

The billing documents that are available to you vary depending on the [type of billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) you are viewing.

  * **Self-service (online) accounts** : In the Google Cloud console, you can access most of your Cloud Billing documents in the **Invoices** page. You can look for specific documents (like statements or invoices), download them in bulk or individually, create custom filters for viewing your documents, and more.

If you're looking for a **payment receipt** , you can find those in the **Transactions** page of the Google Cloud console.

  * **Invoiced (offline) accounts** : In the Google Cloud console, you can access most of your Cloud Billing documents in the **Payment status** page, which provides a real-time and customizable view of your financial standing with Google for the Cloud Billing account that you are viewing. You can look for specific documents (like statements or invoices), download them in bulk or individually, create custom filters for viewing your documents, and more.

For **payment receipts** , you can find those in the **Transactions** page of the Cloud Billing console, or in the **Payments** page in the Google payments center.




### Statements

A statement isn't a bill. It's a summary of monthly billing activity, generated for Cloud Billing accounts that are set up as a [self-serve/online account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). Self-serve Cloud Billing accounts are configured to automatically pay for your Google Cloud costs based on your [billing cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle). In addition to automatic payments, if you prefer, you can [make a manual credit card payment](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) to your self-serve Cloud Billing account at any time.

A statement contains your legally registered business address, tax IDs, any payments made during the month, any taxes paid for the month, and a summary of your usage costs for the month.

Based on your charging cycle, or if you made a manual payment, it's possible to make more than one payment in a month. On your monthly statement, payments show up as transactions.

**Note:** If you're a self-serve, autopay customer, you get your statements and other Cloud Billing documents from the Google Cloud console.

### Invoices

An invoice contains your legally registered business address, tax IDs, any payments made during the month, any taxes paid for the month, balance due, and your payment terms (for example, Net 30). In general, a Cloud Billing account set up as an [invoiced account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) generates one invoice each month.

**Note:** (**Customers in India**) Starting on **July 1, 2021** , your invoice also shows a Unified Payments Interface (UPI) QR code. You can pay your balance by scanning the QR code with any UPI-enabled application.

You might receive multiple invoices that are split across a set of transactions, when they involve resellers or multiple countries. For more information, see [Split invoicing for agency model transactions](https://docs.cloud.google.com/billing/docs/how-to/split-invoice).

**Note:** (**Customers in Israel**) Starting on **June 1, 2025** , for agency model transactions involving customers in Israel, you don't receive an invoice. Customers in Israel receive a _Request for payment_ document. For more information, see [Split invoicing for agency transactions for organizations located in Israel](https://docs.cloud.google.com/marketplace/docs/migrations/split-invoicing-for-agency#split-invoicing-israel).

You can choose to receive a PDF version of your [invoice by email](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#send-invoices-by-email), and you can view and download your invoice online, in the [Cloud Billing **Payment status** page](https://docs.cloud.google.com/billing/docs/how-to/get-invoice#get-statement-or-invoice). Additionally, you can update your Google payments account with the delivery addresses to [receive invoices by mail](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#update_mailing_address).

An invoice for a particular month should be available by the fifth business day of the following month. For example, your September invoice will be ready no later than the fifth business day of October. Invoices aren't generated on weekends or bank holidays, so you should expect invoices to be delayed during those periods.

You pay your invoice balance according to the terms and conditions that you agree to when you enroll in monthly invoicing. [Learn how to pay your invoice](https://docs.cloud.google.com/billing/docs/how-to/pay-invoice).

**Note:** Invoices generally include all costs incurred during a given calendar month, but the cost for some products' usage at the very end of a calendar month might roll over to the next month's invoice.

### Payment receipts

Payment receipts are available for all [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). You can get a receipt for your records at any time in the **Transactions** page of the Cloud Billing console.

For customers who [pay by invoice](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you can also access your payment information in the [**Payments** page in the Google payments center](https://support.google.com/paymentscenter/answer/9924664).

## Permissions required to access billing and payments documents

Billing and payments documents are accessible in the Cloud Billing console, and in the Google payments center.

### Access documents in the Cloud Billing console

To access the **Payment status** , **Invoices** , or **Transactions** page for your Cloud Billing account, you need a role on your Cloud Billing account that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.accounts.getPaymentInfo`



To gain this permissions using a [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions), you need to be assigned to one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

  * [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)



For more information about billing permissions, see:

  * [Overview of access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



### Access documents in the Google payments center

For customers who [pay by invoice](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), to access your Google Cloud billing documents and payment information in the Google payments center, including full-featured access to the **Statement of account** page and the **Payments** page, you need [admin-level permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) on the [Google payments profile](https://docs.cloud.google.com/billing/docs/concepts#billing_account) that is associated with your Cloud Billing account.

To gain admin-level permissions, on your Google payments profile you need the following [permission](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts):

  * [`Admin with all permissions`](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions)



## Get your statement or invoice

The types of documents available are specific to the [type of Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) you are viewing.

  * **Self-service (online) accounts** : **Statements** and **invoices** are available in the **Invoices** page for each _self-service_ Cloud Billing account.
  * **Invoiced (offline) accounts** : **Invoices** and **statements** are available in the **Payment status** page for each _invoiced_ Cloud Billing account.

Additionally, if your Cloud Billing account is configured to be [paid by _invoice_](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you can [configure a list of contacts to receive invoices by email](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#send-invoices-by-email).




Looking for a **payment receipt**? Payment receipts are available in the **Transactions** page of your Cloud Billing console. For more information, follow the instructions at Get your payment receipt

To find your statement or invoice or other Cloud Billing documents, in the following section, select the tab that represents the [type of Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) (self-serve account or invoiced account) you're viewing, to see the instructions for finding your documents.

**Note:** If you aren't sure what type of billing account you're viewing, visit [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle) to learn more.

### Self-serve account

The types of documents available to self-serve (online) Cloud Billing accounts include statements, debit memos, credit memos, and tax invoices, as applicable to your specific Cloud Billing account.

You can find your Cloud Billing documents by accessing the Cloud Billing **Invoices** page in the Google Cloud console, or in the [ **Subscriptions & services** page of the Google payments center](https://support.google.com/googlepay/answer/11828789). The following information describes using the Google Cloud console to get your documents.

#### Access the Invoices page

To get your Google Cloud statement and other documents:

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

  2. **Click the name** of the Cloud Billing account for which you want to see statements.

The **Overview** page opens for the billing account.

  3. From the **Billing navigation menu** , click **Invoices**.

**Can't see or access the Invoices page?**
     * If you don't see the **Billing navigation menu** , you're likely still viewing the list of billing accounts. To view the navigation menu, open the billing account you want to analyze by clicking on the _name_ of the account (and not the check box). 
     * If you're on the **Overview** page of the Cloud Billing account and you can't access the **Invoices** page from the **Billing navigation menu** , you might not have the  permissions needed to view the **Invoices** page for this Cloud Billing account. Contact your Cloud Billing account administrator.
  4. If the Cloud Billing account was associated with different Google payments profiles in the past, click **View past accounts** to see documents for an earlier payment method.




### Invoices page

In **Invoices** , you can search for specific statements, download individual or multiple statements, create custom filters to view your statements, and more.

#### Select your document types

From the **drop-down menu at the top of the table** , select a preset or custom filter to control which types of documents are listed in the table.

  * The default option is **All statements and memos** , and shows all of your statements, debit and credit memos, and tax invoices, as applicable to your Cloud Billing account.

  * If applicable to your Cloud Billing account, other preset view options include:

    * **All statements** : Shows all available monthly statements.
    * **All credit memos** : Shows all of your credits.
    * **All tax and statutory documents** (if applicable to your country): Shows tax and statutory documents, such as _Usage VAT Invoice_ , _Proforma Invoice_ , _Act of Acceptance_ , and _Act of Reconcilitation_.



#### Filter your documents

You can customize the documents displayed in the table by adding filters:

  1. Above the table, click **\+ Add a filter**.
  2. Select the filter type that you want to apply.
  3. Enter any additional information needed to complete the filter.
  4. Click **Apply**. You can add more filters as needed.

     * For example, to view a list of statements generated for a date range, add an _Issue date_ filter and then set the start and end dates.

     * To remove a filter, click the **X** on the filter you want to remove.




#### Show or hide columns

You can select the columns to display in the table, as well as rearrange the order of the columns.

  1. In the column header row, at the far right of the table, click **Edit**.
  2. Select the columns you want to show or hide.
  3. To rearrange the order of the columns in the table, drag the column names in the **Edit** box.
  4. Click **Save**.



#### Sort the documents you see

You can change the sort order of the documents in your table by sorting on one of the visible columns.

  * To sort your documents in ascending or descending order, click the column header that you want to sort by.
  * Click the column header again to toggle between ascending and descending order.



#### Create and save custom filters for reuse

You can add columns, sort, and filter your documents to show only the documents you want to see (for example, all statements in descending order for an amount greater than $500), and then save this customization for future use.

  * To save your filter settings for reuse, select **Save custom filter** , enter a **name** for your custom filter, and click **Save new**.
  * To **use your saved custom filter** , click the **drop-down menu at the top of the table** , and scroll past the list of preset filters to the **Custom filters** section.
  * To delete a custom filter, first open the custom filter, then select **Save custom filter** , and click **Delete**.
  * To edit an existing custom filter, follow these steps: 
    1. Open the custom filter.
    2. Adjust your columns, sort, and filter settings.
    3. Select **Save custom filter**. 
       * To save as a **new custom filter** , edit the custom filter name to create a unique name, and then click **Save new**.
       * To replace the existing customer filter with the new filter settings, leave the name the same and click **Update**.



#### Download individual or multiple statements or other documents

Statements include a summary of your monthly costs and payments, and download in PDF format. To see a more granular view of your monthly costs, visit the [**Cost Table report**](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

**Note:** A row for the current month's statement is not available until the statement has been generated (after the end of the current month).

To download your documents, follow these steps:

  1. Check the box to the left of the statement or document that you want to download.

To select _all_ of the documents that appear in your table, check the box in the column header row of the table.

  2. Click **Download selected**.

If you have more than one page of documents and you selected to download all of them, you'll be prompted with the option to download just the documents on the page you're viewing, or to download all of the selected documents across all pages.

  3. If you selected one document to download, a PDF of that document is downloaded. If you selected multiple documents to download, a zip file is created and downloaded containing a PDF for each of the selected documents.




### Transactions page

You can also download your statements and other documents from the **Transactions** page:

  1. In the Google Cloud console, from the **Billing navigation menu** , click **Transactions**.

  2. On the **Transactions** page, use the toggles to adjust the data displayed and set the date range so that it corresponds to the invoices you want to download.

     * The default view is **Last 3 months** , which lets you access your most recent statements.
     * To access previous statements, adjust the date range using the menu options. For example, choose **This year** if you want to access statements for the current calendar year.
  3. In the **Transactions** table, expand the **Documents** row to view available documents.

  4. Click the statement number to download a PDF version of the statement.


**Note:** If you want to view detailed monthly costs for projects and SKUs, view your [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table). For additional analysis, you can download the cost table report to CSV.

### Invoiced account

The types of documents available to invoiced (terms) Cloud Billing accounts include invoices, debit memos, credit memos, and tax memos, as applicable to your specific Cloud Billing account.

**Note:** An invoice for a particular month should be available by the fifth business day of the following month. The PDF version is generated separately from the CSV version, and the CSV version may be available a day or two later than the PDF version. For more timely access to your costs, view your [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and download the cost table report to CSV.

You can find your Cloud Billing documents by accessing the Cloud Billing **Payment status** page in the Google Cloud console, or in the [ **Statement of account** page of the Google payments center](https://support.google.com/paymentscenter/answer/7520537). Additionally, if your Cloud Billing account is [paid by invoice](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you can [configure a list of contacts to receive invoices by email](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#send-invoices-by-email), and you can update your Google payments account with the delivery addresses to [receive invoices by mail](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#update_mailing_address).

The following information describes using the Google Cloud console to get your documents.

#### Access the Payment status page

To get your Google Cloud invoice and other documents:

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

  2. **Click the name** of the Cloud Billing account for which you want to see invoices.

The **Overview** page opens for the billing account.

  3. From the **Billing navigation menu** , click **Payment status**.

**Can't see or access the Payment status page?**
     * If you don't see the **Billing navigation menu** , you're likely still viewing the list of billing accounts. To view the navigation menu, you must open the billing account you want to analyze by clicking on the _name_ of the account (and not the check box). 
     * If you're on the **Overview** page of the Cloud Billing account and you can't access the **Payment status** page from the **Billing navigation menu** , you might not have the  permissions needed to view the **Payment status** page for this Cloud Billing account. Contact your Cloud Billing account administrator.
  4. If the Cloud Billing account was linked to different Google payments accounts in the past, click **View past accounts** to see documents for an earlier payments account.




### Payment status page

The Payment status page provides a real-time and customizable view of your financial standing with your Cloud Billing account. The Payment status page is based on the [Google payments **Statement of account**](https://support.google.com/paymentscenter/answer/7520537) page, with your payments documents filtered by the _Google payments account_ that is linked to the Cloud Billing account that you are viewing.

On the Payment status page, you can:

  * View owed balance information and invoices, broken out by aging status
  * Find and filter billing information by attributes like month of service, product, or currency
  * Find all billing documents, such as Monthly invoices, Credit memos, Debit memos, and Tax documents



#### Total amount due

The **Total amount due** card summarizes your open invoices by aging status:

  * **Not due yet** : Invoices that are open but not due soon
  * **Due soon** : Invoices that are coming due in the next 20 days
  * **Overdue** : Invoices that have become overdue
  * **At risk** : Invoices that have become overdue, and need to be paid to avoid suspension of services
  * **Suspended** : Invoices that need to be paid to reactivate suspended accounts



To find the specific invoices included in an amount, next to the amount, click **View**.

To find all of your invoices that are currently open, at the top right, click **View open invoices**.

#### View all invoices and memos

To view a table containing of all of your invoices and memos, including those that are closed or paid, click **View all invoices and memos**.

On the documents table, you can search for specific documents, download individual or multiple documents, create custom filters to view your documents, and more.

#### Filter your documents

You can customize the documents displayed in the table by adding filters.

  1. Above the table, click **Show filter** filter_list to view the Filters panel.

By default, the filters available to set include issue month, document type, and document status.

  2. For additional filters, click **Manage filters** , select the additional filter types you want to use, then click **Save filters**.

  3. Open each filter that you want to use, configure the options, and **Apply filter** to save your choices.

  4. To remove the filters you've set, click **Clear all**.




#### Find a specific invoice or document

You can _supplement your filters_ by using search **Search documents**.

  * Enter text that might help you find the invoice or document you're looking for. As long as the text appears on your document, it's searchable. To refine your search even further: 
    * Use AND (in uppercase letters) to find documents with both terms (for example: video AND game).
    * Use OR (in uppercase letters) to find documents with either term (for example: Nov OR Dec).



#### Show or hide columns

You can select the columns to display in the table, as well as rearrange the order of the columns.

  1. Next to the Search box, select  **Manage columns**.
  2. Select the columns you want to show or hide.
  3. To rearrange the order of the columns in the table, drag the column names up and down the list.
  4. Click **Apply** to save your selections.



#### Sort the documents you see

You can change the sort order of the documents in your table by sorting on one of the visible columns.

  * To sort your documents in ascending or descending order, click the column header that you want to sort by.
  * Click the column header again to toggle between ascending and descending order.



#### Create and save custom table views for reuse

You can add columns, sort, search for, and filter your documents to show only the documents you want to see (for example, all open invoices in descending order for a particular PO number), and then save this customization for future use.

  * To save a custom table view for reuse, after you have configured your filters, columns, and sorting options, select **Save view** , enter a **name** for your document view, and click **Save view**.
  * To **use a saved view** , open the **_views_ drop-down menu** at the top of the table, and select the **name of the saved view**.
  * To delete a saved view, open the **_views_ drop-down menu** at the top of the table, select **Delete saved views** , select which saved views you'd like to delete, and click **Delete saved views**. This action can't be undone.



#### Download individual or multiple invoices or other documents

To download your documents, follow these steps:

  1. For each document that you want to download, check the box next to the document number.

To select _all_ of the documents that appear in your table, check the box in header row of the _Document number_ column.

  2. Expand the **Actions** menu, and select **Download documents**.

  3. Choose the format that you want to use to download your documents (PDF is selected by default).

**Caution:** We removed the project-level cost detail from your invoices and statements. If your organization processes the invoice CSV and requires project-level cost detail, download the CSV from the [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and process it in place of the invoice CSV.
  4. Click **Download**.




#### Look at the details of a document

From the Documents table, click the row of the invoice or document that you want to see details for. A dialog opens, showing you document header details including the invoice or memo number, amount, status, purchase order number, account details, and more.

  * In the **Document Activity** section, you can see information including the addresses where the document was mailed and emailed, as well as invoices or credit memos that apply to the document.
  * In the **Associated documents** section, you can see a list of documents and document types that apply to the document you're viewing.
  * To close the dialog, click the **X** in the top left.
  * To download, or take other actions on your document, click **Actions** in the document dialog.

  * You can download both the PDF and CSV versions of your invoice.

**Caution:** Beginning with your January 2021 invoice or statement (available in February 2021), we removed all of the cost details from your invoices and statements, including costs broken down by product or subaccount (for resellers). If your organization previously processed the invoice CSV and you need the invoice cost details, download the CSV from the [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and process it in place of the invoice CSV.
  * In the **Actions** drop-down, you might see a link to **Regenerate invoice with updated information**. If you recently [updated your purchase order number](https://docs.cloud.google.com/billing/docs/how-to/purchase-order) or [changed your billing address](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#change_the_billing_address) you might need to [regenerate your invoice](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#regenerate-invoice) to reflect new information.


**Note:** A row for the current month's invoice is not available until the invoice has been generated (after the end of the current month).

The invoice total generally includes all costs incurred during a given calendar month. Sometimes, at the end of a calendar month, there is a slight delay in usage reporting. The cost of late-reported usage might not be included on that month's invoice and instead might roll over to the next month's invoice. As a result, your invoice total might include costs for _more than one_ calendar month. Usage is reported by _actual usage date_ when viewing your [invoice details](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and [online reports](https://docs.cloud.google.com/billing/docs/how-to/reports#invoice-charges).

### Transactions page

You can also access your invoices from the **Transactions** page:

  1. In the Google Cloud console, from the **Billing navigation menu** , click **Transactions**.

  2. On the **Transactions** page, use the toggles to adjust the data displayed and set the date range so that it corresponds to the invoices you want to download.

     * The default view is **Last 3 months** , which lets you access your most recent invoices.
     * To access previous invoices, adjust the date range using the menu options. For example, choose **This year** if you want to access invoices for the current calendar year.
  3. In the **Transactions** table, expand the **Documents** row to view links to available documents.

  4. Click a document link to access the documents for the Cloud Billing account. For example, click **View invoices** to access the **Invoices** page. On the **Invoices** page, you can download a CSV or PDF version of your invoices.


**Note:** If you want to understand monthly costs for projects and SKUs, view your [Cost Table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) and download it to CSV for analysis.

## Get your payment receipt

Receipts are available for all [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

### Transactions page

You can get a receipt for your records at any time in the **Transactions** section of the Cloud Billing console.

To get your receipt:

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

  2. **Click the name** of the Cloud Billing account for which you want to see payment receipts.

The **Overview** page opens for the billing account.

  3. From the **Billing navigation menu** , click **Transactions**.

**Can't see or access the Transactions page?**
     * If you don't see the **Billing navigation menu** , you're likely still viewing the list of billing accounts. To view the navigation menu, you must open the billing account you want to analyze by clicking on the _name_ of the account (and not the check box).
     * If you're on the **Overview** page of the Cloud Billing account and you can't access the **Transactions** page from the **Billing navigation menu** , you might not have the  permissions needed to view transactions for this Cloud Billing account. Contact your Cloud Billing account administrator.
  4. On the **Transactions** page, set the toggles above the table to control the view and filter the list of transactions:

     1. In the **View** drop-down, select **Detailed transaction view**.
     2. In the **Transaction type** drop-down, select **Payments**. The list of transactions is filtered to display payments made.
     3. In the **Date range** drop-down, set the **date range** so that it corresponds to the receipts you want to view.
  5. From the list of transactions, in the **Description** column, click the **Payment** link to view the payment receipt. The receipt opens in a new browser window.




### Payments page

For customers who [pay by invoice](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you can also access your payment information in the [**Payments** page in the Google payments center](https://support.google.com/paymentscenter/answer/9924664).

In the Google payments center, the **Payments** page shows you what payments Google has received from you and how they've been applied to your invoices.

## Missing charges or documents

Both statements and invoices include only a summary of your monthly costs but don't include a breakdown of your cost details. To view the details of specific charges on a document, access the cost table report. For more information, see [View and download the cost details of your invoice or statement](https://docs.cloud.google.com/billing/docs/how-to/cost-table).

If you can't find a document, or locate a specific charge or transaction related to a Google Cloud service or Google Maps Platform API, [contact Cloud Billing support](https://docs.cloud.google.com/billing/docs/support) for assistance.

## Related topics

For more information on Cloud Billing best practices and Google Cloud resource management, refer to the [Cloud Billing onboarding checklist](https://docs.cloud.google.com/billing/docs/onboarding-checklist) article.

Other related topics:

  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
  * [View your Cloud Billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [Create, modify, or close your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
  * [Split invoicing for agency model transactions](https://docs.cloud.google.com/billing/docs/how-to/split-invoice)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
