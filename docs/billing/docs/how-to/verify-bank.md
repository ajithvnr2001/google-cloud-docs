---
url: https://docs.cloud.google.com/billing/docs/how-to/verify-bank/
title: Verify your bank account \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:34.968965+00:00
---

# Verify your bank account  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/verify-bank/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Verify your bank account Stay organized with collections  Save and categorize content based on your preferences. 

Depending on your country, you might need to verify your bank account to use it as a payment method by direct debit.

**Note:** To use a bank account as a primary payment method for self-serve (online) billing accounts, your account must have an established billing history with Google Cloud, including a minimum account age and a record of on-time payments. If your billing account does not meet the eligibility requirements, you must use a credit or debit card as your primary payment method instead.

A small test deposit will appear in your bank account within a few days of adding the account as a payment method. After you see the test deposit, you should verify the deposit as described in Find and enter a test deposit.

If your account has a billing address in the US, you can instantly verify your bank account rather than use the test deposit, as described in Verify your bank account instantly.

If you're verifying bank information while creating a new billing account, follow the instructions at [create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).

## Permissions required to verify your bank account

To complete the tasks on this page, you need a role on your Cloud Billing account that includes the following [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.accounts.getPaymentInfo`
  * `billing.accounts.updatePaymentInfo`



To gain these permissions using a [predefined billing IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions), you must be a [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access) on the Cloud Billing account.

## Before you begin

Depending on your country's regulations, you might have to accept a direct debit mandate, which gives Google permission to charge your bank account. Follow these steps to accept your direct debit mandate:

  1. In the Google Cloud console, go to the **Payment overview** page for your Cloud Billing account.

[Go to Payment overview](https://console.cloud.google.com/billing/payment)

  2. At the prompt, choose the Cloud Billing account with the associated bank account that you want to verify. The **Payment overview** page opens for the selected billing account.

  3. If you have a pending direct debit mandate, the Payment overview page shows an alert.

  4. Click **Sign mandate** , and follow the steps to sign the direct debit authorization.




## Find and enter a test deposit

Three to five business days after you add your bank account information to your Cloud Billing account, a small test deposit will appear in your bank account.

To verify the test deposit:

  1. Review your bank records and search for a deposit from Google Inc. or AFS, Google's payment partner. The deposit will be less than $1.00.
  2. When you find the deposit, note the exact amount of the deposit.
  3. In the Google Cloud console, go to the **Payment method** page.

[Go to the Payment method page](https://console.cloud.google.com/billing/settings)

  4. At the prompt, choose the Cloud Billing account with the associated bank account that you want to verify.

  5. On the **Payment method** page, find your bank account and click **Verify test deposit**.

  6. Enter the exact amount of the test deposit and click **Submit**.

  7. After you enter the correct amount, the account is verified and you can start using your bank account as your primary form of payment.




## Failed test deposits

On rare occasions, our attempt to make a test deposit doesn't work. If this happens, you'll receive an email and see a notice in **Billing accounts**. There are several reasons why the test deposit might not work, including:

  * Your bank account information is incorrect.
  * Your bank account no longer exists.
  * Your bank account has a restriction against automatic bank account payments.



If your test deposit failed, complete the following steps to check the accuracy of the bank account information you provided:

  1. In the Google Cloud console, go to the **Payment method** page.

[Go to the Payment method page](https://console.cloud.google.com/billing/settings)

  2. At the prompt, choose the Cloud Billing account with the associated bank account you want to verify.

  3. On the **Payment method** page, find your bank account. Review the account details for accuracy.

  4. After reviewing your account details, do one of the following:

     * If the bank account details are correct, contact your bank to ensure that there aren't any account restrictions that prevent you from using automatic bank account payments. Your bank might also call these types of payments direct debit payments. If your bank doesn't allow automatic payments then you can't use this account as a form of payment. If they do, then to reinstate the account, remove it from your Cloud Billing account and then add your bank account again as if it were a new form of payment.
     * If the bank account details are incorrect, you need to add your bank account again as a new form of payment. Later, you can remove the incorrect bank account from your Cloud Billing account payment methods.



For more information on what to do if your test deposit fails, see [Fix issues with payment method verification codes](https://support.google.com/googlepay/answer/12651770).

For more information about removing or adding your bank account as a form of payment, see [Add, Remove, or Update a Payment Method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods).

An alternative to a test deposit is to verify your US bank account with Instant bank verification.

## (US only) Verify your bank account instantly

We offer instant bank verification for Google Cloud customers with US bank accounts. Unlike the test deposit verification method, which takes several days to complete, instant bank verification lets you verify your bank account within seconds.

You can use instant bank verification in either of the following situations:

  * If you haven't entered your bank account information yet
  * If you've recently entered your bank account information



Each of these situations is described in the following sections.

**Note:** This service is available only to customers with a US bank account.

Keep in mind the following points when attempting instant verification:

  * Check that the name of your bank is correct. If it's wrong, go back to the **Payment Settings** page and verify the bank's details.
  * You need to enter the credentials that you use to sign in to your bank online, not the ones that you use for your Google Cloud account.
  * If instant verification fails because there was a problem connecting to your bank, you can try again later or use test deposit verification as described earlier.

**Caution:** We recommend that you take extra security precautions when verifying your account. Before you enter your account information, make sure your browser shows a secure connection. Google will never ask you for account information using email.

### If you haven't entered your bank account information yet

If you're entering your US bank account information for the first time, you can either verify instantly or verify using a test deposit. Follow these steps to add your US bank account information and to verify your bank account details using instant bank verification:

  1. In the Google Cloud console, go to the **Payment method** page.

[Go to the Payment method page](https://console.cloud.google.com/billing/settings)

  2. At the prompt, choose the Cloud Billing account with the associated bank account that you want to add and verify.

  3. To add the bank account information, on the **Payment method** page, click **Add payment method**.

     1. Select **Add a bank account**.
     2. Enter your bank account details.
     3. Click **Save**.
  4. On the **Verify your bank account** page, select **Verify by logging into your bank account** , and then click **Verify**.

  5. Enter the Online ID and Passcode that you use to sign in to your bank online.

**Note:** Google won't store your online banking credentials.
  6. Click **Verify**.




Your bank account is now verified.

### If you recently entered your bank account information

If you recently added a US bank account, you can use instant verification instead of the test deposit verification method. After entering your US bank account information, follow these steps to verify your bank account details using instant bank verification:

  1. In the Google Cloud console, go to the **Payment method** page.

[Go to the Payment method page](https://console.cloud.google.com/billing/settings)

  2. At the prompt, choose the Cloud Billing account with the associated bank account that you want to verify.

  3. On the **Payment method** page, find your bank account and click **Verify**.

  4. On the **Verify your bank account** page, select **Verify by logging into your bank account** , and then click **Verify**.

  5. Enter the Online ID and Passcode that you use to sign in to your bank online.

**Note:** Google won't store your online banking credentials.
  6. Click **Verify**.




Your bank account is now verified.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
