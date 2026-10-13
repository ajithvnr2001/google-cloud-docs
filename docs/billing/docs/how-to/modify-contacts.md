---
url: https://docs.cloud.google.com/billing/docs/how-to/modify-contacts/
title: Manage Google payments users, permissions, and notification settings \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:19.916712+00:00
---

# Manage Google payments users, permissions, and notification settings  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/modify-contacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Manage Google payments users, permissions, and notification settings Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure access permissions for Google payments accounts and profiles.

A Google payments profile stores the following information:

  * Name, address, and tax ID (when required legally) of who is responsible for the profile.
  * Credit cards, debit cards, bank accounts, and other payment methods you've used to buy through Google in the past.
  * Receipts and other information about past transactions.



Every Cloud Billing account is associated with a Google payments profile, and linked to one or more Google payments accounts.

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

Access permissions for Google payments profiles and Cloud Billing accounts are configured in two different systems depending on what type of access you want to provide.

If you need to configure access permissions for a Cloud Billing account, see [Manage access to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing).

## Google payments users and permissions

Google payments users, payments permissions, and email notification options are managed from the _Google payments center_ **Settings** page. These settings are connected to the Google payments center and to your payments profile. See [Cloud Billing concepts](https://docs.cloud.google.com/billing/docs/concepts#billing_account) for more information.

You can add other users to any [Google payments _Organization_ profile](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) that you manage. For each person you add to a payments profile, you decide if they can invite other users, buy or sign up for paid Google services, view your payment history, or make changes to the profile. You can also set their email notification preferences.

**Note:** Certain Cloud Billing IAM permissions grant a subset of _equivalent payments_ permissions that allow billing account users to access and edit the associated [_Organization_ Google payments profile](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) and linked payments account from within the Cloud Billing console, without needing direct permissions on the payments profile itself. These _acquired_ Google payments permissions allow billing account users to view payment information and documents, add or edit payment methods, edit certain details on the payments profile such as the business name, address, and tax information, and make manual payments to a self-serve, online Cloud Billing account. The _acquired_ permissions **don't** grant the [_Manage users_ or _Admin with all permissions_ level of access](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions) on the Google payments profile.

This document describes how to manage the user accounts of the Google payments profile linked to your Cloud Billing account. You can manage the payments users by accessing the **Payment settings** page in the **Billing** section of the Google Cloud console.

You can also manage your Google payments profile and payments users in the [Google payments center](https://payments.google.com/payments/home#settings). See [Google payments help ](https://support.google.com/paymentscenter/answer/7162853) for more information.

### About payments profile account types

Google payments profiles can be set up as one of two account types: _Organization_ or _Individual_. The account type is used for tax and identity verification. After the payments profile is created, the account type can't be changed. Make sure to choose the one that best fits how you plan to use your Google payments profile.

  * If you want more than one user on your payments profile, then you must set the account type to _Organization_.
  * If you create a payments profile with an account type set as _Individual_ , only one user — the creator of the Google payments profile — is associated with the payments profile, and no other users can be added.



### Permissions required to manage payments users

To make the changes described in this document, you need the following permissions.

If you want to manage payments users from the **Payment settings** page in the Cloud Billing console, you need permissions on your Cloud Billing account _and_ your Google payments profile.

  1. On the _Cloud Billing account_ , you must be either a _Billing Account Administrator_ or _Billing Account Viewer_. For more information, see [Overview of Cloud Billing Access Control](https://docs.cloud.google.com/billing/docs/how-to/billing-access).
  2. On the _Google payments profile_ , at a minimum, you need the _Manage users_ permission, but you might need the _Admin_ permission to complete some of the user management tasks. For more information, see the payments help center article on [managing user permissions](https://support.google.com/paymentscenter/answer/7162853)



If you want to manage payments users in the _Google payments center_ , you only need [permissions on your Google payments profile](https://support.google.com/paymentscenter/answer/7162853). You don't need Cloud Billing account permissions if you're not accessing the **Payment settings** page in the **Billing** section of the _Google Cloud console_.

Tips:

  * The creator of the Google payments profile is automatically granted the _Admin with all permissions_ permission on the _payments profile_.
  * The payments profile _Admin_ can manage all users of the payments profile, including adding or removing users, and setting or modifying all payments profile permissions for a user.
  * On the payments profile, the _Manage users_ permission lets you add and update payments contacts, but you can't assign admin-level permissions to users, and you might not be able to remove an existing user.



## Accessing the payments settings page

You can access the **Payment settings** page of your Google payments profile from either the Google Cloud console or Google payments center.

###  Google Cloud console 

To access the **Payment settings** page in the **Google Cloud console** , do the following:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to Payment settings in Cloud Billing console](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account connected to the payments profile that you want to update.

The **Payment settings** page opens for the selected Cloud Billing account.




###  Google payments center 

To access the payments **Settings** page in the Google payments center, do the following:

  1. Sign in to the [ Google payments center](https://payments.google.com/payments/home).

If you have more than one Google payments account, the payments profile that you most recently viewed opens. To manage a different payments profile, select the payments profile from the drop-down menu at the top of the page.

  2. Select the **Settings** tab.




## Updating payments profile users and notification settings

To change the payments profile users or the notifications you want to receive, do any of the following.

### Add a user to a payments profile

  1. Access the payments profile **Settings** page using either the Google Cloud console or Google payments center.
  2. On the payments **Settings** page, under **Payments users** , click **Manage payments users**.
  3. On the **Manage users** page, click **\+ Add a new user**.
  4. Enter the contact's name, phone number (optional), and email address.
  5. To choose the new user's permissions, click visibility **Permissions**. Learn more about profile permissions.
  6. To choose the new user's email preferences, click email **Email preferences**. Learn more about email preferences.
  7. Optional: Select the Primary contact checkbox to designate this user as the primary contact. Every profile must have a primary contact. There can be only one primary contact on a profile.
  8. When you're finished, click **Invite**.

The user's name displays as _Pending_ until they accept your invitation. To use the payments profile, the user must accept your invitation within two weeks.

To accept your invitation, users must do the following:

     1. Open the email invitation.
     2. Click **Review and accept**.
     3. At the bottom of the next screen, click **Accept**.



#### Why can't I add a new user to my payments profile?

If you go to the Google payments settings and access the **Manage users** page and you don't see an option to add a new user, the reasons could include the following:

  * The payments profile is set up as an _Individual_ account rather than an _Organization_ account. You can't add users to an individual account. This setting can't be changed.
  * You don't have the permissions needed to add a new payments user. Contact your Cloud Billing account administrator or Google payments profile administrator.



### Resend an email invitation

To resend an email invitation to a user, follow these steps:

  1. Access the payments profile settings page using either the Google Cloud console or Google payments center.
  2. On the payments **Settings** page, under **Payments users** , click **Manage payments users**.
  3. Locate the user you sent an invite to.
  4. Open their contact record by clicking the Down arrow keyboard_arrow_down.
  5. Click **Resend invitation**.



### Update settings for a payments profile user

  1. Access the payments profile **Settings** page using either the Google Cloud console or Google payments center.
  2. On the payments **Settings** page, under **Payments users** , click **Manage payments users**.
  3. To open a user's record, click the Down arrow keyboard_arrow_down on the name of the contact you want to update.

To update the contact details:

     1. Under **Contact details** , click **Edit** edit.
     2. Enter the updated contact information.
     3. Click **Save**.

**Note:** You can't update the email address for a user. If you need to update a user's email address, you need to add them as a new user.

To update the user permissions:

     1. Under **Permissions** , click **Edit** edit.
     2. Choose the Google payments permissions for this user.
     3. Click **Save**.

**Can't edit the permissions?** If you don't see the edit icon, the reasons could include the following:

        * The user you want to edit is the only administrator-level user on this Google payments profile. Every profile must have at least one user designated as a payments profile _Admin_. To edit the user permissions, first grant the administrator permissions to another user.
        * You don't have the necessary permissions to edit the payments user. Contact your Cloud Billing account administrator or Google payments profile administrator.

To update payments notifications for a user:

     1. Under **Email preferences** , click **Edit** edit.
     2. Select the type of notification level: **All payments email** , **Administrative payments email only** (for example, account suspension notices), or **No payments email**.
     3. Click **Save**.

**Can't edit the email preferences?** If you don't see the edit icon, the reasons could include the following:

        * The user you want to edit is an _Admin_ or the primary contact. The primary contact and all administrator-level users must use the **All payments email** preference, to receive all payments notifications.
        * You don't have the necessary permissions to edit the payments user. Contact your Cloud Billing account administrator or Google payments profile administrator.



### Remove a user from a payments profile

  1. Access the payments profile **Settings** page using either the Google Cloud console or Google payments center.
  2. On the payments **Settings** page, under **Payments users** , click **Manage payments users**.
  3. To open the user's record you want to remove, click the Down arrow keyboard_arrow_down next to the name of the user.
  4. Choose **Remove**.
  5. To confirm you want to remove that user permanently, click **Yes**.



#### Why can't I remove a user from the payments profile?

If you go to the Google payments **Manage users** page and expand the user you want to remove, but you don't see an option to remove the user, the reasons could include the following:

  * The user is set up as the primary contact. Every payments profile must have a primary contact. You can't remove a user who is designated as the primary contact. To remove the user, first reassign the primary contact role to another user.
  * The user is set up as the only _Admin_ for this profile. Every payments profile must have at least one user designated as a profile administrator. To remove the user, first grant the _Admin_ role to another user.
  * You don't have the permissions needed to remove a payments user. Contact your Cloud Billing account administrator or Google payments profile administrator.



## About the primary contact

Each Google payments profile has one primary contact who receives all payments emails. This is the person Google will contact with any payments-related questions.

Every payments profile must have a primary contact. You can't remove a user who is designated as the primary contact, but you can reassign that role to another user.

To reassign the primary contact:

  1. Access the payments profile **Settings** page using either the Google Cloud console or Google payments center.
  2. On the payments **Settings** page, under **Payments users** , click **Manage payments users**.
  3. To open a user's record, click the Down arrow keyboard_arrow_down on the name of the contact you want to designate as the primary contact.
  4. Select the **Primary contact** checkbox.
  5. Click **Save**.



For some products, the primary contact might get an email receipt when anyone makes a payment using that Google payments profile.

## About payments profile permissions

Set the permissions to give different users different levels of access to the same Google payments profile. A user can receive email notifications even if no permissions are selected. You can set permissions as follows:

  * **Read access** : Users can view all information and documents related to all products linked to this payments profile.

  * **Edit payments profile** : Users can edit the following information in the payments profile:

    * Business name
    * Address
    * Payments methods
    * Tax information
    * Payments account settings

Note that users with the _edit_ permission can [make manual payments](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) to an automatically paid, self-serve Cloud Billing account, as long as that user is also a _Billing Account Administrator_ or a _Billing Account Viewer_ on the Cloud Billing account.

  * **Sign-up and purchase** : Users can use the payments profile to buy or sign up for more Google products or services.

**Note:** Some Google products and services don't let users switch between multiple profiles.
  * **Manage users** : Users can add, edit, and remove users of the payments profile and change their permissions.

**Note:** Users with this permission can only give other users up to the same level of permissions they have and can only remove users at the same or lower permission level. Users might need administrator-level permissions to remove other user accounts.
  * **Admin with all permissions** : Users have all current and future permissions as they become available, and can add, edit, manage, and remove users for the payments profile.




To set the _Admin_ permission for a user, you must be an _Admin_ on this Google payments profile. Users with the _Manage users_ permission can set only up to the same level of permissions that they're granted on their user account. For example, a user with _Read access_ , _Edit payments profile_ , and _Manage users_ permissions can add a new user and assign the new user the same or fewer permissions.

## About email preferences

You can set email preferences for each Google payments user. Additionally, if your Cloud Billing account is configured for _invoiced_ billing, you can separately configure a list of contacts to receive invoices by email.

To route general billing notifications to specific teams without granting them broader IAM roles, configure custom contacts using [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

### Email preferences for Google payments users

Set the types of email notifications the payments user receives. Note that if the user is designated as the _primary contact_ or if the user is granted _admin_ permissions, you must set email preferences to **All payments email**.

  * **All payments email** : All payments email includes administrative email, as well as transactional messages such as payout alerts, or when there might be issues with [test deposits to verify your bank account](https://docs.cloud.google.com/billing/docs/how-to/verify-bank).

  * **Administrative payments email only** : Administrative email includes account management messages about tax forms, customer suspensions, Terms of Service updates, and account closure.

  * **No payments email** : No notification messages are sent.




### Send invoices by email to contacts you specify

In addition to the email preferences for Google payments account users, if your Cloud Billing account is configured to be [paid by _Invoice_](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you can also configure additional contacts to receive _only_ invoices by email. These contacts don't need to be set up as payments account users to receive invoices by email.

For guidance on how to add email addresses for non-payments users, see [Enable other contacts to receive invoices by email](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#send-invoices-by-email).

## Related topics

  * [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
  * [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  * [Make a manual payment or pay early](https://docs.cloud.google.com/billing/docs/how-to/manual-payment)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
