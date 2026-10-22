---
url: https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account/
title: Modify your Cloud Billing account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:47.255412+00:00
---

# Modify your Cloud Billing account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Modify your Cloud Billing account Stay organized with collections  Save and categorize content based on your preferences. 

After you create a Cloud Billing account and its associated Google payments profile, you can change or update many account settings, with a few notable exceptions.

For information on how to create a Cloud Billing account, see [Create a new self-serve Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).

If you want to close, reopen, or delete an existing Cloud Billing account rather than updating the account, see [Close or reopen your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account).

## Account settings that you can modify

Here's a list of settings that you can modify on an existing Cloud Billing account or Google payments profile. Follow the links for guidance about completing these tasks.

Account settings that you can modify  
---  
Billing account name | The name of the billing account that displays in billing account selectors and tabular lists or reports that display the billing account name. If you have multiple Cloud Billing accounts with similar names, you might want to modify the name of each billing account to help you distinguish between accounts.  
Billing account organization | The [ organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) associated with the billing account. The organization resource represents an entity (such as a company) and serves as the root node of the Google Cloud resource hierarchy, acting as the parent to all folder and project resources. Changing the organization resource associated with a Cloud Billing account doesn't affect project services.  
Mailing addresses (all values except the _Country_) | There are one or more mailing addresses associated with your billing account, depending on the [ type of billing account (self-serve or invoiced)](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and the type of Google payments account connected to your Cloud Billing account. The mailing addresses can include the legally registered business address, and the addresses where invoices are mailed.  
[ Projects linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project) | A Cloud Billing account defines who pays for a given set of resources, and it's [ linked to one or more projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked). Project usage is charged to the linked Cloud Billing account. You can [ change the Cloud Billing account linked to each of your projects](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).  
[ Payment methods for a self-serve billing account](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) | Usage costs accrued for a self-serve Cloud Billing account are automatically charged to the payment instrument on file in the associated Google payments profile. These forms of payment typically include credit cards, debit cards, or bank accounts, depending on your [ country and currency](https://docs.cloud.google.com/billing/docs/resources/currency).  
[ Email addresses and email preferences for payments account notifications](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#update-payments-profile) | A Cloud Billing account is linked to a Google payments profile. You can update Google payments users and their notification settings to control who receives payments emails, and the types of emails they are sent.  
[ Cloud Billing account permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access) | You can add, remove, and update users and their level of access to Cloud Billing accounts. Billing account access is needed for many billing tasks, such as: viewing [ reports](https://docs.cloud.google.com/billing/docs/reports) and [ cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery); viewing [ documents](https://docs.cloud.google.com/billing/docs/how-to/get-invoice), like invoices and statements; configuring and managing [ budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets); purchasing and analyzing [ committed use discounts](https://docs.cloud.google.com/billing/docs/how-to/cud-analysis); and various account management tasks.  
[ Google payments profile permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) | You can add, remove, and update users and their level of access to Google payments _Organization_ profiles. Each Cloud Billing account is linked to a Google payments profile. Google payments profile access is needed to manage payments-related tasks, such as: add, edit, and remove [ payment methods](https://docs.cloud.google.com/billing/docs/how-to/payment-methods); update Google payments profile information, including  mailing addresses; manage Google payments users, including contact details, [ email preferences](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#email), and [ user permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions).  
[ Purchase Order number on invoices](https://docs.cloud.google.com/billing/docs/how-to/purchase-order) | For Cloud Billing accounts configured to be billed by a monthly invoice, you can set or modify the invoice's purchase order number (also called IO number, CPE, or client code), an identifier that appears in the header of your invoices.  
Email addresses for contacts to receive invoices by email | For Cloud Billing accounts configured to be billed by a monthly invoice, you can manage a list of contacts who receive invoices by email.  
  
## Account settings that you **_can't_** modify

Here's a list of settings that you can't modify on an existing Cloud Billing account or Google payments profile. In the event that you want or need to change these settings, read the following information for guidance and links to helpful documentation.

Account settings that you _can't_ modify  
---  
[ Currency of billing account](https://docs.cloud.google.com/billing/docs/resources/currency) | The currency for your Cloud Billing account is automatically assigned based on the _Country_ that corresponds with your billing mailing address. You can't choose a different currency for the account. If you need a Cloud Billing account that operates in a different currency, [ create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)*.  
[ Country setting on the billing account and payments profile](https://docs.cloud.google.com/billing/docs/resources/currency#list_of_countries_and_regions) | During the creation of a Cloud Billing account, you [ select the _Country_](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#create-new-billing-account) for your billing account (either directly, or inherited from an organization node). The linked Google payments profile uses the same country as the billing account. Each Cloud Billing account and Google payments profile can be associated with only one country due to tax regulations and currency restrictions. You can't change the country for an existing billing account or payments profile. To use a different country, [ create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)*.  
[ The Google payments profile that's linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account) | Each Cloud Billing account is linked to a Google payments profile when the billing account is created. You can't unlink the payments profile or link an existing Cloud Billing account to a different Google payments profile. To use a different payments profile, [ create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)*.  
[ The Account type of the Google payments profile](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#account_type) | When you create a Google payments profile, you're prompted to select the account type, to create either an "Individual" or "Organization" payments profile. In some countries, this selection affects your tax options. Also, only "Organization" types can have multiple payments profile users. You can't change the account type after signing up. To use a Google payments profile with a different account type, [ create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)*.  
  
* If you have a Cloud Billing account that's billed by invoice, then creating a new, _self-serve_ billing account might not be the best option for you. To modify the settings on your invoiced account, contact your [Google Cloud sales specialist](https://cloud.google.com/contact) or [Cloud Billing Support](https://docs.cloud.google.com/support/billing) for assistance.

## Rename a Cloud Billing account

The name of a Cloud Billing account appears in billing account selectors and tabular lists or reports that display the billing account name. If you have multiple Cloud Billing accounts with similar names, you might want to modify the name of each billing account to help you distinguish between accounts. Don't include sensitive information such as personally identifiable information (PII) or security data in your billing account name.

### Permissions required for this task

To change the Cloud Billing account name, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.accounts.update`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#account_management)



To gain this permission using a predefined role, ask your administrator to grant you the following role on the Cloud Billing account:

  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access)



### How to rename the Cloud Billing account

  1. In the Google Cloud console, go to the **Account management** page.

[Go to Account management in the Cloud Billing console](https://console.cloud.google.com/billing/manage)

  2. At the prompt, choose the Cloud Billing account that you want to update.

The **Account management** page opens for the selected Cloud Billing account.

  3. At the top of the page, click edit **Rename billing account**.

  4. Enter a new name for the Cloud Billing account.

**Caution:** Don't include sensitive information such as personally identifiable information (PII) or security data in your billing account name.
  5. Click **Rename** to save your changes.

You might need to refresh the page to see the new name on the **Account management** page.




**Why can't I see or access the edit Rename billing account button?**

If you're on the **Account Management** page of the Cloud Billing account you want to rename and you don't see or can't access the edit **Rename billing account** button, you might not have the permissions needed to rename this Cloud Billing account. Contact your [Cloud Billing account administrator](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator).

## Change the organization associated with a Cloud Billing account

You can create Cloud Billing accounts without an associated [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). If you are a Google Workspace or Cloud Identity customer with existing Cloud Billing accounts, you can migrate them to your organization resource. Migrating a Cloud Billing account into an organization resource doesn't affect project services.

### Permissions required for this task

To change the organization resource on a Cloud Billing account, you must have these roles:

  * For the **Cloud Billing account** that you want to update, you must be a **Billing Account Administrator**.

  * On the **organization resource** to which you want to migrate your Cloud Billing account, you must be a **Billing Account Creator**.

  * If you want to migrate a Cloud Billing account from an _existing_ organization resource, you must be a **Billing Account Administrator** for the **organization resource** from which you are migrating the Cloud Billing account.




To learn about granting these roles, see [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access) and [Manage access to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing).

### How to update the organization on a Cloud Billing account

To update the organization resource on your Cloud Billing account, complete the following steps:

  1. In the Google Cloud console, go to the **Billing account management** page.

[Go to Billing account management](https://console.cloud.google.com/billing)

  2. From the **Select an organization** menu, select an organization resource to see the Cloud Billing accounts associated with it, or select **None selected** to see all billing accounts. View the **Organization** column to see the organization that is assigned to each billing account.

  3. In the **Account name** column, click the name of the Cloud Billing account that you want to update. The billing account Overview page opens.

  4. In the Billing navigation menu, click **Account management**.

  5. At the top of the Account management page, click business **Change organization** , then select the organization resource to which you want to migrate the Cloud Billing account.




**Why can't I see or access the business Change organization button?**

If you're on the **Account Management** page of the Cloud Billing account that you want to migrate to a different organization resource, and you don't see or can't access the business **Change organization** button, you might not have the permissions needed to update the organization for this Cloud Billing account. Contact your [Cloud Billing account administrator](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator).

## Change the mailing addresses on the Cloud Billing account

The mailing addresses for a Cloud Billing account are stored on the associated Google payments profile. There are one or more mailing addresses associated with your billing account, depending on the [type of billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) (invoiced or self-serve) and the [type of Google payments profile](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) (Individual or Organization) connected to your Cloud Billing account. The mailing addresses can include the legally registered business address that gets printed on invoices, and the addresses where invoices are mailed.

### Permissions required for this task

To complete the steps to change the mailing addresses on the _Organization_ payments profile that is associated with your Cloud Billing account, you need a role that includes the following permission on the Cloud Billing account:

  * [`billing.accounts.updatePaymentInfo`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information)

To gain this permission using a predefined role, ask your administrator to grant you the [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in) role on the Cloud Billing account.




### Update the mailing addresses

The mailing addresses available for you to update depend on the [type of Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) (invoiced or self-serve) that you're updating. To change the mailing addresses on the Cloud Billing account, follow the instructions for your billing account type.

### Invoiced account

If your Cloud Billing account is configured as an [invoiced account](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle), there is more than one mailing address in the Google payments profile:

  * **Business name and address** : This is the _legally registered_ business name and address. This address is typically printed on invoices (unless you specify a different _Bill-to address_).
  * **Mail invoice delivery addresses** : Addresses entered here will receive invoices by mail. This doesn't impact the address that's printed on your documents; that is, only your bill-to address is printed on documents.
  * **Bill-to address** : This is the mailing address that appears on your invoices and statements. This address can be set to use the **business name and address** , or you can choose to configure a different address.



#### Update the Business name and address

If you pay by invoice, you can't update the **Business name and address** online, in the Google payments profile. Rather, we must perform this action for you.

If your company name or address has changed,contact your [Google Cloud sales specialist](https://cloud.google.com/contact) or [contact Cloud Billing Support](https://docs.cloud.google.com/support/billing) for assistance.

To update the information, we might request a scanned copy of your official registration documents stating your tax IDs (if applicable), registered company name, and legal address. After the changes are made, you can request a revision of the previously issued documents to reflect the corrected name and other details.

#### Update the _Mail invoice delivery_ addresses

Complete the following steps to add addresses where the invoices will be mailed:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account that you want to update.

The **Payment settings** page opens for the selected Cloud Billing account.

  3. Under **Payments account** , click the edit icon (edit) next to the **Mail invoice delivery** to open it for edit.

  4. Select **Add mailing address (optional)** , and choose an option:

     * Select an existing address from the list, and then click **Add**.
     * or Select **Add another address** , enter the address details, and then click **Add**.
  5. When you're done adding mailing addresses, click **Save**.




If you want to delete any _Mail invoice delivery_ addresses:

  1. Follow the previous steps to access the **Payments settings** page for the Cloud Billing account that you want to manage.
  2. Under **Payments account** , click the edit icon (edit) next to the **Mail invoice delivery** to open it for edit.
  3. Click the delete icon (cancel) next to each address that you want to remove.
  4. Click **Save** to save your changes and deletions.



#### Update the _Bill-to address_

The Bill-to address is the mailing address that's printed on your invoices and statements. By default, the Bill-to address is set to use the **Business name and address** on your Google payments profile. If you prefer, you can assign a different mailing address to appear on your invoices.

Complete the following steps to update the Bill-to address:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account that you want to update.

The **Payment settings** page opens for the selected Cloud Billing account.

  3. Under **Payments account** , click the edit icon (edit) next to the **Bill-to address** to open it for edit.

  4. Click the displayed address to choose an option:

     * Select an existing address from the list, and then click **Add**.
     * or Select **Add another address** , enter the address details, and then click **Add**.
  5. When you're done adding mailing addresses, click **Save**.

The updated Bill-to address will appear on newly-issued invoices. If you also want to update the Bill-to address on previously-issued invoices, you need to regenerate each invoice.




#### Update the Bill-to address on _previously-issued_ invoices

To change the _Bill-to address_ on invoices that have already been issued, after setting the new address, regenerate each invoice you want to update — one invoice at a time.

To regenerate an invoice, do the following:

  1. In the Google Cloud console, go to the **Invoices** page.

[Go to the Invoices page](https://console.cloud.google.com/billing/invoices)

  2. At the prompt, choose the Cloud Billing account you want to view.

  3. From the **Invoices** table, click the row of the invoice to view its details. A dialog opens, showing you document header details including the invoice or memo number, bill-to address, amount, status, purchase order number, and account details.

  4. In the top right of the invoice dialog, select **Actions**.

  5. To request a revision to your invoice, including updating the Bill-to address, select **Regenerate invoice with updated information**.

  6. Read the **Request status** confirmation, and then click **Got it** to return to the **Invoices** table. For each invoice you choose to regenerate, you must wait 48 hours to make another revision request on that same invoice.

To update the Bill-to address for another invoice, repeat the previous steps after the last invoice is successfully applied.

**Note:** Regenerating a past invoice might take some time. If after a few hours you don't see the updated Bill-to address on your regenerated invoice, [contact Customer Support](https://docs.cloud.google.com/support/billing).



### Self-serve account

There is one mailing address on a [self-serve (online) Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). This mailing address is the legally registered business address that gets printed on statements and tax invoices.

Complete the following steps to update the address:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account that you want to update.

The **Payment settings** page opens for the selected Cloud Billing account.

  3. Under **Payments profile** , click the edit icon (edit) next to the **name and address** to open it for edit.

  4. Update the mailing address information* and click **Save**.

* You can't edit the _country_ of the mailing address. If you need to change the country of the Cloud Billing account's address, you need to [create a new billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account#create_a_new_billing_account).




## Enable other contacts to receive invoices by email

If your Cloud Billing account is configured to be [paid by _Invoice_](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), _Google payments account users_ always receive invoices by email. If you want other people to receive invoices by email (that is, non-payments users), you can configure additional contacts to receive _only_ invoices by email. These contacts _don't_ need to be set up as payments account users to receive invoices by email.

Email notification preferences for _Google payments contacts_ are configured separately. Learn more about managing [Google payments users](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) and [notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#email).

Other types of billing documents, such as statements and receipts, aren't sent by email, but are available online in the Cloud Billing console and in the Google payments center. Learn how to [access all of your billing and payments documents online](https://docs.cloud.google.com/billing/docs/how-to/get-invoice).

### Permissions required for this task

For a Cloud Billing account paid by _invoice_ , to manage the email addresses where invoices are delivered, you need a role that includes the following permission on the Cloud Billing account:

  * [`billing.accounts.updatePaymentInfo`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information)



To gain this permission using a predefined role, ask your administrator to grant you the [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in) role on the Cloud Billing account.

### Add email addresses for invoice delivery

**Note:** This procedure is only applicable for Cloud Billing accounts that are paid using an _invoice_. Self-serve (automatic payments) accounts generate [statements](https://docs.cloud.google.com/billing/docs/how-to/get-invoice) rather than invoices, and the Google payments account settings are different for invoiced accounts compared to self-serve accounts.

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account that you want to update.

The **Payment settings** page opens for the selected Cloud Billing account.

  3. Within the **Payments account** section, click **Email invoice delivery** edit to open it for edit.

Email addresses for Google payments contacts are listed first, before any additional (non-payments users) email addresses.

  4. To add an email address for a non-payments user, select **Add new email address (optional)** , enter the email address where you want invoices to be sent, and then click **Add**.

Email addresses for non-payments users display "This invoice only" to indicate the type of email notifications this email account will receive.

  5. When you're done adding email addresses, click **Save**.

Email addresses must be verified. If this is the first time you've entered the email address for the Google payments account, Google will send a verification email with a subject line similar to _Action required for your Google Account_. The contact must open the email and click **Accept** to verify their email address and begin receiving communications, such as invoices, from the payments profile.




### Delete email addresses for invoice delivery

If you want to delete an _Email invoice delivery_ address:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account that you want to update.

The **Payment settings** page opens for the selected Cloud Billing account.

  3. Within the **Payments account** section, click **Email invoice delivery** edit to open it for edit.

  4. Next to each email address that you want to remove, click the delete icon (cancel).

**Note:** If you don't see the delete icon (cancel) next to an email address, this indicates that the email address belongs to a Google payments user. To manage the email preferences for a Google payments user, follow the procedure to [update settings for a payments profile user](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#update-user-settings). Learn more about [email preferences for each payments user](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#email).
  5. Click **Save** to save your deletions.




## Related topics

  * [Create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)
  * [Close or re-open your Cloud Billing account ](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account)
  * [View projects linked to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  * [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
  * [Resolve billing issues](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
