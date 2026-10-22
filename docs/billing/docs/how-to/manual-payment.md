---
url: https://docs.cloud.google.com/billing/docs/how-to/manual-payment/
title: Make a manual payment or pay early \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:15.941611+00:00
---

# Make a manual payment or pay early  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/manual-payment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Make a manual payment or pay early Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to make a manual payment to your [_Postpay_](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle) Google payments account that is linked to your [self-serve, online Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). _Postpay_ payments accounts accrue charges over time and then are automatically paid based on the account's [charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).

You can make a manual payment to your _Postpay_ payments account at any time. The payment is applied to your accrued costs. If your payment is larger than the amount you owe, the balance is applied like a credit to reduce the amount of your next automatic charge.

If your Cloud Billing account is set up as an [invoiced account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and you want to learn how to pay your Google Cloud invoice, visit [Make a payment to an invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/pay-invoice).

## Why make a manual payment or pay earlier than your _Postpay_ automatic charge?

You might choose to make a manual payment for these reasons:

  * **More control over how and when you're automatically charged.** With a manual payment, you can pay the entire account balance, just a fraction of it, or more than your balance to cover future costs. If making a payment to cover future costs, to prevent an automatic payment, you must make a manual payment large enough to cover your anticipated usage.
  * **Divide your payment among several payment methods.** This can help delay when your primary form of payment is charged. In rare cases, if you make a manual payment near to the time that an automatic payment is due, you might be charged twice.
  * **Your Google Cloud account has had activity often associated with increased fraud.** When this occurs, your account might be suspended and you might need to make a payment to reactivate your account. In these cases, the Google Cloud / API Trust & Safety Team sends an email requesting that you make a payment of $100 towards any of your Cloud Billing accounts. This payment appears as a credit in your billing account and is applied to any future charges.
  * **Your credit or debit card was declined and you want your services to continue running.** If your card was declined, you can make a manual payment to continue running your services while you [resolve the declined payment issue](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#resolving_declined_payments). If you make a payment by bank transfer or direct debit, your account will start running again when we've received the payment (there is a possible delay of up to seven days while waiting to receive confirmation of payment from the bank).

**Caution:** If you already fixed an issue with the payment method on your _Postpay_ payments account, such as by adding a new payment method to your account, your balance is automatically charged and you _don't_ need to make a manual payment. However, if you make a duplicate payment, the additional amount is used as a credit to pay for your future usage costs.



## Permissions required to make a manual payment

You can make a manual payment to a Cloud Billing account from either the Google Cloud console or directly from the Google payments center. The permissions required to make a payment depend on the [type of Google payments profile](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) that is associated with the Cloud Billing account, and which payment process you choose.

  * If you created a self-serve, online Cloud Billing account and set up and registered your payments profile as an [_Individual_ type](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types), then only you can make a manual payment to your Cloud Billing account.
  * If your Cloud Billing account is associated with an [_Organization_ type](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) of payments profile, then you can grant user permissions in either Cloud Billing or Google payments, or both, as described in the following table:

From the Cloud Billing console, make a payment to the Cloud Billing account | In the Google payments center, make payment to a Google Cloud payments account  
---|---  
From the Billing section of the Google Cloud console, to make a manual payment to a self-service, online Cloud Billing account, you need a role on your Cloud Billing account that includes the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.accounts.getPaymentInfo`
  * `billing.accounts.updatePaymentInfo`

To gain these permissions using a [ predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions), ask your administrator to grant you the following [ Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) role on your Cloud Billing account:

  * Billing Account Administrator

|  To make a payment to your Google Cloud account directly from the Google payments center, you need payments permissions on the _Organization Google payments profile_ that is linked to your Cloud Billing account:

  * On your Google payments profile, you must be [ added as a payments user](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts) with at least the [ _Edit payments profile_](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions) level of permissions.

  
For more information about Cloud Billing permissions, see:

  * [ Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [ Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [ Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)

|  For more information about Google payments permissions, see:

  * [ Manage Google payments users, permissions, and notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts)

  
  
## Make a manual payment

To make a manual payment to a _Postpay_ account, access the _Postpay Google payments account_ that is linked to your Cloud Billing account. You can access the Google payments account from either the Billing section of the Google Cloud console, or directly from the Google payments center. Depending on the status of your Google Cloud account, you might not be able to access your Cloud Billing account in the Google Cloud console. In those instances, you can access the _Google payments account_ directly in the Google payments center to make a manual payment.

###  Google Cloud console 

In the **Google Cloud console** , to make a manual payment to your _Postpay Google payments account_ , complete the following steps:

  1. In the Google Cloud console, sign in to the **Payment overview** page for your Cloud Billing account.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/payment)

  2. At the prompt, **choose the Cloud Billing account** for which you want to make a manual payment. The Billing **Payment overview** page opens for the selected billing account.

  3. To open the payment form, click **Make a payment** or **Pay early**.

  4. Select the payment method you want to use to make the payment, or add a new payment method. Use any payment method available in your location and currency. [Check to see the payment methods available to you](https://docs.cloud.google.com/billing/docs/resources/currency).

**Caution:** **Payment processing delays** – Depending on the payment method you select, it can take from 24 hours to a week or more for your payment to reach your account. If you're paying using a bank account, it can take up to 10 business days for your bank account payment to be processed successfully.  
  
If you experience service restrictions and want to immediately start using Google Cloud and other impacted services like Google Maps Platform, Firebase, and Gemini API in AI Studio, we recommend that you make a manual payment using a credit card, and pay for the full outstanding balance.
  5. Enter the **amount of the payment** you want to make, and select **Continue**.

Depending on the payment method you are using, you might need to enter a minimum amount, usually USD $10, or the equivalent in your local currency.

  6. Review your payment details, then click **Pay now** to complete the transaction.




###  Google payments center 

To make a manual payment in the **Google payments center** , complete the following steps:

  1. Sign in to the [**Google payments center**](https://payments.google.com/payments/home).

**Tip** : If you have more than one Google payments _profile_ , the payments profile that you most recently viewed opens. To manage a different payments profile, select the payments profile from the drop-down menu at the top of the page.

  2. Select the **Subscriptions & services** tab.

The Subscriptions and Services page opens, where you can access the _Active_ and _Canceled_ Google Cloud accounts and other Google subscriptions that are associated with the Google payments profile that you are viewing.

  3. Locate the **_Google Cloud_** subscription card for the _Postpay_ Google payments account that you want to pay, and click **Manage**.

Each _Google Cloud_ subscription card represents a _Google payments account_ that is linked to a _Cloud Billing account_ , and includes the [billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id) of the linked Cloud Billing account.

Your Cloud Billing account might also have a _Prepay_ payments account that you use to purchase credits to pay-in-advance for your usage costs of Gemini API in AI Studio. While in the Google payments center, if you choose to [buy more credits](https://ai.google.dev/gemini-api/docs/billing#buy-credits) for your _Prepay_ payments account, those credits only pay for your Gemini API in AI Studio usage costs, and not for Google Cloud, Google Maps Platform, or Firebase usage costs. [Learn more about Prepay and Postpay split charging cycles](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle).

  4. To open the payment form, click **Make a payment** or **Pay early**.

  5. Select the payment method you want to use to make the payment, or add a new payment method. Use any payment method available in your location and currency. [Check to see the payment methods available to you](https://docs.cloud.google.com/billing/docs/resources/currency).

**Caution:** **Payment processing delays** – Depending on the payment method you select, it can take from 24 hours to a week or more for your payment to reach your account. If you're paying using a bank account, it can take up to 10 business days for your bank account payment to be processed successfully.  
  
If you experience service restrictions and want to immediately start using Google Cloud and other impacted services like Google Maps Platform, Firebase, and Gemini API in AI Studio, we recommend that you make a manual payment using a credit card, and pay for the full outstanding balance.
  6. Enter the **amount of the payment** you want to make, and select **Continue**.

Depending on the payment method you are using, you might need to enter a minimum amount, usually USD $10, or the equivalent in your local currency.

  7. Review your payment details, then click **Pay now** to complete the transaction.




## Related topics

  * [Make a payment to an invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/pay-invoice)
  * [Learn more about _Prepay_ billing accounts](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
