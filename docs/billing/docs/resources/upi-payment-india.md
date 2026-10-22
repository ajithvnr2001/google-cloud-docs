---
url: https://docs.cloud.google.com/billing/docs/resources/upi-payment-india/
title: Use UPI for Google Cloud payments \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:31.417391+00:00
---

# Use UPI for Google Cloud payments  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/resources/upi-payment-india/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Resources ](https://docs.cloud.google.com/billing/docs/resources)



Send feedback 

#  Use UPI for Google Cloud payments Stay organized with collections  Save and categorize content based on your preferences. 

This document applies to Google Cloud India customers.

If you're a qualified organization in India, you can use Unified Payments Interface (UPI) to make a manual payment or set up monthly recurring payments for your Google Cloud subscription.

## Review the requirements

To pay with UPI, you must:

  * Have a billing address and bank account in India.
  * Pay for your Google Cloud subscription with Indian Rupees (INR).
  * Have a configured and registered UPI account with a financial institution.



Before you can use UPI as a payment method, you need to make a prepayment, typically 500 to 1000 INR.

## Make a _manual_ payment with UPI

###  Google Cloud console 

In the **Google Cloud console** , to make a manual payment to your Cloud Billing account, complete the following steps:

  1. In the Google Cloud console, sign in to the **Payment overview** page for your Cloud Billing account.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/payment)

  2. At the prompt, **choose the Cloud Billing account** for which you want to make a manual payment. The Billing **Payment overview** page opens for the selected billing account.

  3. To open the payment form, in **Your balance** card, click **Make a payment** or **Pay early**.

  4. On the **Make a payment** page, change your _Payment method_ to select **Pay with UPI**.

  5. Enter the **amount of the payment** you want to make, and select **Continue**.

  6. Review your payment details, then click **Pay now**.

A QR code is displayed.

  7. On your mobile device:

     1. Open your UPI app and scan the QR code.
     2. Follow the instructions to complete your payment.



###  Google payments center 

To make a manual payment in the **Google payments center** , complete the following steps:

  1. Sign in to the [**Google payments center**](https://payments.google.com/payments/home).

**Tip** : If you have more than one Google payments _profile_ , the payments profile that you most recently viewed opens. To manage a different payments profile, select the payments profile from the drop-down menu at the top of the page.

  2. Select the **Subscriptions & services** tab.

The Subscriptions and Services page opens, where you can access the _Active_ and _Canceled_ Google Cloud accounts and other Google subscriptions that are associated with the Google payments profile that you are viewing.

  3. Locate the **_Google Cloud_** subscription card for the Google payments account that you want to pay, and click **Manage**.

Each _Google Cloud_ subscription card represents a _Google payments account_ that is linked to a _Cloud Billing account_ , and includes the [billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id) of the linked Cloud Billing account.

Your Cloud Billing account might also have a _Prepay_ payments account that you use to purchase credits to pay-in-advance for your usage costs of Gemini API in AI Studio. While in the Google payments center, if you choose to [buy more credits](https://ai.google.dev/gemini-api/docs/billing#buy-credits) for your _Prepay_ payments account, those credits only pay for your Gemini API in AI Studio usage costs, and not for Google Cloud, Google Maps Platform, or Firebase usage costs. [Learn more about Prepay and Postpay split charging cycles](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle).

  4. To open the payment form, in **Your balance** card, click **Make a payment** or **Pay early**.

  5. On the **Make a payment** page, change your _Payment method_ to select **Pay with UPI**.

  6. Enter the **amount of the payment** you want to make, and select **Continue**.

  7. Review your payment details, then click **Pay now**.

A QR code is displayed.

  8. On your mobile device:

     1. Open your UPI app and scan the QR code.
     2. Follow the instructions to complete your payment.



You can review your payment history on the [Transactions page](https://docs.cloud.google.com/billing/docs/how-to/view-history) for your Cloud Billing account.

## Set UPI as a _primary_ payment method for _automatic_ payments

To set UPI as the primary payment method for automatic payments to your Cloud Billing account, first add UPI as a payment method, then set UPI as the Primary payment method.

  1. In the **Google Cloud console** , go to the **Payment method** page.

[Go to the Payment method page](https://console.cloud.google.com/billing/settings)

  2. At the prompt, choose the Cloud Billing account you want to update.

The **Payment method** page opens for the Cloud Billing account.

  3. On the Payment method page, click **Add payment method**.

  4. From the list of available payment method types, select **Pay with UPI**.

UPI is added as an "Other" form of payment.

  5. Next, in the payment method info card for the UPI payment method, look for the drop-down list in the bottom-left of the card that displays **_Other_**.

  6. Expand the list, and then select **Primary**. A QR code is displayed.

  7. On your mobile device:

     1. Open your UPI app and scan the QR code.
     2. Follow the app instructions to set up and approve the mandate to use UPI for automatic payments.
  8. The payment method previously marked as Primary will be marked as Other, and the payment method info cards will shuffle on the page, so that the Primary payment method is displayed first.




## Related topic

[Learn more about UPI](https://www.npci.org.in/product/upi).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
