---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/secure-payments-add-providers/
title: Add payment providers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:02.874126+00:00
---

# Add payment providers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/secure-payments-add-providers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Add payment providers Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** For implementation and pricing, please contact your account team or Support.

The Secure Payments feature provides secure credit card processing. After payment is initiated by the agent, the customer is taken through a series of payment prompts.

The agent can watch payment progress on their Agent Adapter while the customer enters payment information but they are unable to hear the consumer side of the call.

## Prerequisite

  * Payment provider credentials are integrated with the CCAI Platform portal.



## Retrieve your payment gateway credentials

To retrieve your payment provider credentials, you can follow these instructions on a per provider basis.

### Stripe

  1. From your Stripe account, toggle **View Test Data** to on.

  2. **API Key** : The API key is the information you'll need in the next section.




### FreedomPay

  1. Set up a merchant account with payment gateway(s).

  2. From the FreedomPay portal, retrieve the following information:

     * Store ID.
     * Terminal ID for that merchant, specific to the Contact Center AI Platform (CCAI Platform) integration.



### Braintree

Retrieve the following credentials for your Braintree account: `Environment`, `Merchant ID`, `Public Key`, `Private Key`, `Tokenization Key`, and `Merchant Accounts`. See [Important Gateway Credentials](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials) in the Braintree documentation.

## Admin configuration

Additional settings can be configured by the administrator in the CCAI Platform portal. These settings are outlined in the following sections.

### Customize messages about payment details

A succession of messages are displayed to the agent while the caller is making their payment. These messages are standardized by default. To set custom messages, you can update the Text-to-Speech script at **Settings** > **Languages & Messages** > **IVR Purchase Flow Messages**.

See [IVR Purchase Flow Messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Customizing_Languages__Recordings____Messages#UUID-1ed7ab28-cbc0-ac39-3ad9-2478e29dde19) for sample scripted messages.

### Enable and add a provider

  1. Go to **Settings > Developer Settings**.

  2. In the **Credit Card Payment Providers** section, click **Manage Payment Providers**. Current providers previously set up in your environment are displayed.

  3. Click **+Add Provider**. You are brought to the Payment Provider details page.

  4. Enter a **Name** for the payment option.

  5. Select **Payment Provider**.

  6. Select **Type**. Dynamic fields to enter credentials will display after the provider type has been selected.

  7. Enter credentials:

     1. For Stripe, enter the `API secret key` found in your Stripe account.
     2. For FreedomPay, enter the Store ID and the Terminal ID. The format of these two IDs must be `storeID`, `terminalID`.
  8. Select the **currency** type. The default option is USD. Stripe and Braintree offer additional currency options. For more information, see the [multi-currency documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Secure_Payments_Multi_Currency).

  9. Click **Save**.




### Configure Secure Payments for inbound calls

  1. Go to **Settings** > **Queue** > **{select preferred channel}** > **select a queue** > **Credit Card Payment Settings**.

  2. Toggle the **Credit Card Payment Settings** to **Enable**.

  3. Select **Provider** from the drop-down menu.

  4. Select **Use ZIP Code** to have the customer verify their zip code during payment.

  5. Select **Currency** from the drop-down menu.

  6. Click **Save**.




## Configure payments for Web SDK outbound and scheduled calls

This section describes how to configure payments for Web SDK outbound calls and scheduled calls.

**Important:** Scheduled calls require both this Web queue configuration and the global **Payments for Outbound Calls** setting.

Web SDK outbound calls and scheduled calls are configured in the **Web queue** you use for those calls.

**Path** : **Settings** > **Queue** > **Web** > **select a queue** > **Credit Card Payment Settings**

  1. Toggle **Credit Card Payment Settings** to **Enable**.

  2. Select a **Provider**.

  3. (Optional) Select **Use ZIP Code**.

  4. Select **Currency**.

  5. Click **Save**.




#### Configure payments for outbound calls (global)

Payments for outbound calls are configured in **global settings**.

**Path** : **Settings** > **Developer Settings** > **Payment Providers** > **Payments for Outbound Calls**

![sec-pay-add-currency.png]()

  1. Toggle **Payments for Outbound Calls** to **On**.

  2. Select a **Provider**.

  3. (Optional) Select **Use ZIP Code**.

  4. Select **Default Currency**.

  5. Click **Save Payment**.




### Configure Secure Payments for outbound calls

  1. Toggle the **Payments for Outbound Calls** switch to **On**.

  2. Select an existing payment provider from the **Provider** drop-down.

  3. Select the **Use ZIP Code** checkbox is if you want to require the customer to verify their billing zip code during payment.

  4. Click **Save Payment**.




### Configure Secure Payments for multi-currency

When you set up secure credit card payment options through Stripe or Braintree, you have the option to select from the following international currencies:

  * United States Dollar - USD (default option)
  * British Pounds - EUR
  * Euros - EUR
  * Canadian Dollars - CAD



#### Set a new default currency

  1. Go to **Settings** > **Developer Settings** > **Credit Card Payment Providers**.

  2. Expand the **Default Currency** drop-down and select a currency option.

  3. Click **Save Payment**.




##### Apply multi-currency options to your payment provider

**Note:** Stripe and Braintree are the only providers that offer multi-currency.

  1. Go to **Settings** > **Developer Settings** > **Credit Card Payment Providers**.

  2. Click **Manage Payment Providers**.

  3. Click **+Add Provider**.

  4. Enter a name for the provider.

  5. Select the **Provider Type** from the drop-down menu. If you select Braintree, dynamic fields for adding a merchant account will appear. To add multiple currencies for Braintree, click **+Add Merchant Account** and enter the details.

  6. Click **+Add Currency** and select from the list. To add multiple currencies, keep clicking **Add currency**. Your selected currencies will appear in a list on the **Payment Provider** page. Click **X** to remove a currency type




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
