---
url: https://docs.cloud.google.com/billing/docs/how-to/create-billing-account/
title: Create a new self-serve Cloud Billing account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:36.477541+00:00
---

# Create a new self-serve Cloud Billing account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/create-billing-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Create a new self-serve Cloud Billing account Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [self-serve, online Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) to automatically pay for your Google Cloud and Google Maps Platform usage costs. If you're interested in setting up a Cloud Billing account that is billed by invoice, visit [Apply for monthly invoiced billing](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing).

## Before you begin

Before you create a new billing account, we recommend you do the following:

  * Review the information about Cloud Billing accounts to determine if a new Cloud Billing account is the right solution for your needs.
  * Ensure that you have the required permissions to create a Cloud Billing account.



### About Cloud Billing accounts

  * Cloud Billing accounts pay for usage costs in Google Cloud projects and Google Maps Platform projects. Cloud Billing accounts _don't_ pay for Google Workspace accounts. Google Workspace customers need a separate Google Workspace billing account.

Product | Billing account needed to pay for product usage costs  
---|---  
Google Cloud | Cloud Billing account  
Google Maps Platform | Cloud Billing account  
Google Cloud & Google Maps Platform | 1 Cloud Billing account  
Google Workspace | Google Workspace billing account  
Google Cloud & Google Workspace | 1 Cloud Billing account + 1 Google Workspace billing account  
  * A project and its service-level resources are linked to one Cloud Billing account at a time.

  * A Cloud Billing account operates in a single currency and is linked to a [Google payments profile](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383).

  * A Cloud Billing account can be linked to one or more projects.

  * Usage costs are tracked by Project and are charged to the linked Cloud Billing account.

**Important** : Projects that are _not_ linked to an active Cloud Billing account can't use Google Cloud or Google Maps Platform services. This is true even if you only use [services that are free](https://docs.cloud.google.com/free/docs/gcp-free-tier).

  * If you want to change the Cloud Billing account that you're using to pay for a project (that is, link a project to a different Cloud Billing account), see [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

  * You can manage your Cloud Billing accounts using the Google Cloud console. For more information about the Google Cloud console, visit [General guide to the console](https://support.google.com/cloud/answer/3465889).




### Permissions required for this task

The permissions required to create a Cloud Billing account depend on your configuration of Google Cloud or Google Maps Platform.

Members of a Google Cloud Organization | Not using a Google Cloud Organization  
---|---  
If you manage your Google Cloud resources using an [ Organization node](https://docs.cloud.google.com/billing/docs/concepts#organization), and you are a member of that Google Cloud Organization, then you must be a [ Billing Account Creator](https://docs.cloud.google.com/resource-manager/docs/default-access-control) on the Organization node to create a new Cloud Billing account.  Specifically, if you're a Google Cloud user within an Organization, to perform this task, you must have the following [ permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing).

  * `billing.accounts.create`

Additionally, Cloud Billing accounts are linked to a Google payments profile. If you plan to use an _existing_ payments profile with your new billing account, you must be granted the [ Sign-up and purchase](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions) permission on the payments profile. |  If you're not a member of a Google Cloud Organization but instead are managing your Google Cloud resources or Google Maps Platform APIs using projects, you don't need any specific billing role or permission to create a Cloud Billing account. Additionally, Cloud Billing accounts are linked to a Google payments profile. If you plan to use an _existing_ payments profile with your new billing account, you must be granted the [ Sign-up and purchase](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions) permission on the payments profile.  
  
For more information about Cloud Billing permissions, see:

  * [Overview of access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



For more information about Google payments permissions, see [Manage payments users, permissions, and notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts).

## Add a new Cloud Billing account

To create a new self-serve (autopay) Cloud Billing account, complete the following steps.

**Note:** If you're getting started with Google Cloud, you create a self-serve Cloud Billing account as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

  2. Click **Create account**.

     1. Enter the **Name** of the Cloud Billing account. This is the name of the billing account that displays in billing account selectors and tabular lists or reports that display the billing account name.

**Caution:** Don't include sensitive information such as personally identifiable information (PII) or security data in your billing account name.
     2. Depending on your configuration, you also need to select one of the following:

        * **Organization** : If you see an **Organization** drop-down, then you must select an Organization before you can continue.
        * **Country** : If you are prompted to select a **Country** , select the country that corresponds with your billing mailing address.

          * The country you select affects the payment options available in the next step.
          * The currency for your Cloud Billing account is automatically assigned based on the country you select.
          * Your country determines what payment methods you can use to pay for your incurred usage costs.
          * Choose your country (and currency) carefully, as you can't change these selections later. If you need to edit the country on an existing Cloud Billing account, you'll need to create a new billing account.
**Prohibited Territories** : Google Cloud is available in most countries and regions. However, Google restricts access to some of its services in certain countries or regions, such as China, Crimea, Cuba, Iran, North Korea, and Syria. If a country isn't in the list, it might be due to restricted access to Google Cloud services.
     3. Click **Continue**.

  3. Choose the **[Google payments profile](https://support.google.com/paymentscenter/answer/9028746?ref_topic=9017383)** that will be associated with this Cloud Billing account. A payments profile is shared and used across all Google products (such as Google Workspace, Google Cloud, Google Fi, and more). You can choose an _existing_ Google payments profile, or _create a new_ payments profile. If you create a new profile, follow the instructions on the screen to set up your Google payments profile.

**Important: About the Google payments profile Account Type**

     * If you're creating a _new_ Google payments profile, when setting your **Account type** , be aware that this setting is _permanent_ and might be used for tax (such as [value-added tax (VAT)](https://docs.cloud.google.com/billing/docs/resources/vat-overview)) and identity verification.

**Choose your account type carefully:**

       * **Individual accounts** are designed for personal use and allow for only one user to be associated with the Google payments profile. If you are an individual, student, or not part of an organization, select **Individual**.

       * **Business accounts** (also known as 'Organization' accounts) are designed for multi-user, managed environments, such as companies, educational institutions, or non-profits. If you select **Business** without being part of an organization, you might encounter significant administrative overhead, receive notifications intended for larger entities, and face complexities or potential charges for managing or closing multiple associated billing accounts, even if no services are used.

For more information, see [Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).

     * Depending on your country's tax requirements, you might need to enter additional tax information.

     * If you're choosing an existing Google payments profile to be associated with this Cloud Billing account, select a _Business profile for Cloud_ account.

  4. When you're done setting all the options and details, click **Submit and enable billing**.




### About authorization requests

When you create a new Cloud Billing account, you might notice a temporary pre-authorization hold on your account statement.

This hold is not an actual charge. Instead, it is a verification request between the billing system and your card issuer to ensure that your card is valid and has sufficient credit available to cover your payments.

#### Key considerations

  * **No action required** : You don't need to contact Google Cloud support to remove the hold.
  * **Automatic removal** : The hold will automatically drop from your statement. This typically happens within a week, though the exact timing depends entirely on your bank's policies.
  * **When to contact your bank** : Because these holds are managed by your financial institution, Google Cloud can't expedite their removal. If you have questions about a hold that has not resolved itself after more than a week, contact your card issuer or bank directly for support.



Banks often display pre-authorizations under the same "Pending" section as standard transactions. The funds are _temporarily_ held to verify the account and will be released back to your available balance.

If a hold appears after you add a new payment method, allow up to 7 business days for your bank to clear it. For any ongoing discrepancies, contact your bank's customer service team.

For information about verifying bank accounts, see [Verify your bank account](https://docs.cloud.google.com/billing/docs/how-to/verify-bank).

For information about adding backup methods of payment, see [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods).

**Note:** If you haven't already verified your email address, you might need to do so before you can begin using the new Cloud Billing account.

## (India only) Verify your identity

Google is required to comply with applicable cybersecurity regulations in India when providing cloud services. If your Cloud Billing account address is in India, you must complete the mandatory identity verification process, described in this section.

After you create a new Cloud Billing account, you must complete the identity verification process within 30 days. If you don't complete the process within this timeframe, your Cloud Billing account and access to Google Cloud might be suspended.

  1. To start the verification, open the **Billing account overview** page. At the prompt, select your Cloud Billing account.

[Go to Billing account overview](https://console.cloud.google.com/billing/overview)

  2. If your account needs to be verified, the page shows a banner to complete your identity verification. Click **Verify now** , and follow the prompts to provide your information.




### Information required for organizations

If you're completing the verification for an organization, you must provide the following information:

  * Your mobile phone number. You receive a verification code on your device.

  * The names and designations of at least one individual who has executive management control, or influence over the management of the company.

  * You might need additional documents to verify your organization, such as business registration documents, and proof of address documents. You can upload one of the following documents for verification:

    * Certificate of incorporation
    * Certificate of registration on conversion
    * Certificate of provisional registration
    * Amended certificate of registration
    * Registration of society
    * Udyam registration certificate
    * GST registration certificate
    * VAT Certificate
    * Registration certificate (Jammu and Kashmir)
    * A utility or phone bill (with a date in the last 60 days)



### Information required for individuals

If you're using Google Cloud as an individual, you must provide documents that verify your identity and your address.

  1. As your proof of identity, upload one of the following documents:

     * Passport
     * Driver's license
     * PAN card
     * Election Commission ID card
  2. As your proof of address, upload one of the following documents:

     * A utility or phone bill (with a date in the last 60 days)
     * If your identity document also has your address on it, you can upload it again. Examples of identity documents with your address include the following:

       * Driver's license with address, either on the front or back
       * Election Commission ID card, with the address on the back
       * The last page of your Indian Passport



### Verify your identity using Aadhaar

To verify your identity using e-Aadhaar with provisioning obtained through DigiLocker, use the following steps. For more information, see [e-Aadhaar](https://uidai.gov.in/en/contact-support/have-any-question/283-faqs/aadhaar-online-services/e-aadhaar.html).

  1. Enter your name, address, and phone number in the form shown during the identity verification process. Make sure this information exactly matches the information on your Aadhaar Letter or Aadhaar PVC Card.
  2. Follow the prompts shown during the process and provide access to your e-Aadhaar information in DigiLocker.
  3. The name and address from your e-Aadhaar will then be matched to the information you entered to complete the verification.



## Verify your payments contact email address

To ensure you receive billing- and payments-related notifications, we might ask you to verify your email address on your Google payments profile.

To verify your email address, we'll send you a verification email to the email address you entered for your payments profile contact. To activate your Google payments email preferences, click the verification link in the email.

If you haven't received the verification email, here's how to request a new verification link:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, **choose the Cloud Billing account** that you want to verify.

The **Payment settings** page opens for the selected Cloud Billing account.

  3. Under **Payments users** , click **Manage payments users**.

  4. In the **Manage users** list, find the email address you want to verify and click **Resend verification email**. If the email address has already been verified, this link is not available.




Until your primary contact email address is verified, you'll see a notification banner on the [Payment Overview page](https://console.cloud.google.com/billing/payment) in Billing. This notification is similar to _"This payments profile has no verified primary contact. Critical email may not be received until the primary contact verifies their email"_.

## Recommended next steps

To ensure that you can maintain your Cloud Billing account, pay your bills, and monitor your costs, after you create a new billing account, we recommend you also do the following:

  * Configure access to billing accounts and payments profiles
  * Create a FinOps administration project
  * Set up budgets to track your spend
  * Enable billing data export to BigQuery



### Configure access to billing accounts and payments profiles

After you create a new Cloud Billing account, you might want to grant user permissions to _additional_ users to access your billing account and Google payments profile.

Each Cloud Billing account is linked to a Google payments profile. Access permissions for Cloud Billing and Google payments are configured in two different systems depending on what type of access you want to provide.

monetization_on Cloud Billing permissions |  payment Google payments settings & permissions  
---|---  
Access permissions for a **Cloud Billing account** are managed using [ **IAM roles**](https://docs.cloud.google.com/billing/docs/how-to/billing-access). Certain Cloud Billing account permissions also grant access to the associated Google payments profile to view payment details, edit forms of payment and payment profile settings, and make a manual payment. Billing account permissions can be configured to let users complete the following tasks: 

  * Open, close, and modify a Cloud Billing account.
  * View reports and cost data.
  * View payments details and documents (such as invoices and statements).
  * Add and edit (but not remove) payment methods.
  * Edit payments profile and account settings.
  * Make a manual payment.
  * Analyze and purchase committed use discounts (CUDs).
  * Enable and manage export of billing data.
  * Configure budgets and alerts.
  * Manage billing per project.
  * Manage user permissions for billing.
  * Contact billing support.

|  The access permissions to a **Google payments profile** are managed in [ **Google payments settings**](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts). Google payments permissions can be configured to let users complete the following tasks: 

  * Update payments profile info, including mailing addresses.
  * Add, edit, and remove payment methods.
  * Update the primary and backup payment methods assigned to each payments account.
  * Manage payments users, including contact details, email preferences, and user permissions.

With Google payments permissions, users can access and manage payments profiles and payments accounts directly in the Google payments center, without needing separate permissions on the Cloud Billing account. To _fully manage_ your payments profile and payments accounts from within the _Cloud Billing console_ , users need Cloud Billing permissions _and_ Google payments permissions. For example, a user with the [ Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#ba-viewer) role on the Cloud Billing account and assigned as an [ Admin with all permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions) on the associated Google payments profile will be able to fully manage the Google payments profile and accounts directly from the _Cloud Billing console_.   
  
#### Cloud Billing account user permissions

Each Cloud Billing account needs at least one [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in). By default, the person who creates the Cloud Billing account is a Billing Account Administrator for that billing account. For redundancy, we recommend you configure more than one administrator on each Cloud Billing account.

You can grant different levels of access to billing accounts to your users, depending on what they need to do (for example: track spend, review cost anomalies, manage budgets, optimize costs, or review and pay invoices).

For more information, see [Cloud Billing access control & permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access).

#### Google payments user permissions

Each Google payments account needs at least one [Admin with all permissions](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions), and one [Primary Contact](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#primary-contact) (the person Google will contact with any payments-related alerts or questions). By default, the person who creates the Google payments account is both the _Admin with all permissions_ , and the _Primary Contact_. For redundancy, we recommend that you configure more than one Google payments administrator.

You can add other users to any [Google payments _Organization_ profile](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) that you manage and grant different levels of access to your users, depending on what they need to do (for example: manage payment methods or payments profile details). You can also configure user email preferences for receiving billing and payments emails.

Not all payments-related tasks require you to be a Google payments user to gain the permissions required to access and edit Google payments profile information. Certain Cloud Billing IAM permissions will grant _equivalent_ payments permissions. Specifically, Cloud Billing account users with the `billing.accounts.updatePaymentInfo` permission on their billing account will be able to access and edit the associated Google payments profile and payments account directly from the Cloud Billing console, without needing additional permissions on the payments profile itself. This includes users with the [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) role (`roles/billing.admin`) and users granted this permission using a [custom role](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information).

For more information, see [Manage Google payments users, permissions, and notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts).

### Create a FinOps administration project

To use many of the powerful tools available in Cloud Billing, you need a [project that is linked to the billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked). We recommend that you configure a separate Google Cloud project to contain all of your FinOps and billing administration needs for a Cloud Billing account. There are many benefits to using a FinOps-focused project, including the following:

  * You can contain all of the billing tools that are project-dependent into one common project, where you can precisely control who has access to the project and the tools contained within.
  * If you want to use [Gemini Cloud Assist in Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/gemini/overview), billing users will also need access to a [project where the Gemini for Google Cloud API is enabled](https://docs.cloud.google.com/billing/docs/how-to/gemini/set-up-gemini).
  * To use any of the [billing APIs](https://docs.cloud.google.com/billing/docs/develop), each API you use needs to be enabled in a project. You can use the same project to contain all of the billing APIs.
  * Many of the billing tools partner with other Google Cloud products (such as [BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup#project) and [Pub/Sub](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#pub-sub-topic)) that require a project when you set up the tool.
  * There might be costs associated with the use of some billing tools (like the [cost of running queries](https://docs.cloud.google.com/billing/docs/how-to/reports#cost_of_use_to_generate_and_run_queries) against your [Cloud Billing cost data exported to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)). With a FinOps-dedicated project, you can track any FinOps-related costs separately from your other Google Cloud costs.



For detailed guidance about creating and configuring a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### Set up budgets to track your spend

You can create Cloud Billing budgets to monitor all of your Google Cloud charges in one place. A budget lets you track your actual Google Cloud spend against your planned spend. After you set a budget amount, you set budget alert threshold rules that are used to trigger email notifications. Budget alert emails help you stay informed about how your spend is tracking against your budget. You can also configure budget notifications to [automate cost control responses](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications).

For more information about budgets, see [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).

### Enable billing data export to BigQuery

Managing and reporting costs effectively is an important part of financial stewardship, no matter your budget. Making data-driven decisions about your Google Cloud costs and usage starts with collecting the data you'll need to inform those decisions.

Cloud Billing export to [BigQuery](https://docs.cloud.google.com/bigquery/what-is-bigquery) lets you export detailed Google Cloud billing data (such as usage, cost estimates, and pricing data) automatically throughout the day to a [BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets-intro) that you specify. Then you can access your Cloud Billing data from BigQuery for detailed analysis. You can also use this export method to export data to a JSON file.

Timing is important. To access a more complete set of Google Cloud billing data for your analysis needs, we recommend that you enable Cloud Billing data export to BigQuery on each of your Cloud Billing accounts, at the same time that you create the Cloud Billing accounts.

For comprehensive guidance, see [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## Related topics

  * [Modify your Cloud Billing account ](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account)
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
