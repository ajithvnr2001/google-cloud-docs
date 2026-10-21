---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-prepaid-balances/
title: Managing prepaid account balances \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:00:51.788271+00:00
---

# Managing prepaid account balances  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-prepaid-balances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing prepaid account balances Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** The monetization features specified in the [November 3 2021 Apigee Monetization release notes](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes#november-3,-2021---apigee-monetization) are supported only on Apigee.

This page describes how you can manage your prepaid billing accounts.

You can use the Apigee APIs to manage the prepaid billing accounts of your app developers and AppGroups. By using the APIs, you can perform the following tasks:

  * View monetization configuration
  * Update monetization configuration
  * View balance
  * Credit balance
  * Adjust balance

**Note** : Your rate plans determine how much money is deducted from the prepaid accounts. For information about configuring rate plans, see [Managing rate plans for API products](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans).

## View monetization configuration

To view the monetization configuration of an app developer, issue a `GET` request to the following API:

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/monetizationConfig`

To view the monetization configuration of an AppGroup, issue a `GET` request to this API:

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/appgroups/$APPGROUP_NAME/monetizationConfig`

With the API, you can view the billing type. For more information about the API, see [organizations.developers.getMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/getMonetizationConfig) or [organizations.appgroups.getMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/getMonetizationConfig).

The following example shows you how to view the monetization configuration for an app developer using the `curl` command:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
    https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/monetizationConfig
    

When you run the command, you can see a response similar to the following:
    
    
    {
      "billingType": "PREPAID"
    }

## Update monetization configuration

To update the monetization configuration of an app developer, issue a `PUT` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/monetizationConfig`

To update the monetization configuration of an AppGroup, issue a `PUT` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/appgroups/$APPGROUP_NAME/monetizationConfig`

With this API, you can update the billing type. For more information about the API, see [organizations.developers.updateMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/updateMonetizationConfig) or [organizations.appgroups.updateMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/updateMonetizationConfig).

The following example shows how to update the monetization configuration for an app developer using the `curl` command:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-type: application/json" \
    -X PUT \
    -d '{
    "billingType": "POSTPAID"
    }' \
    https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/monetizationConfig
    

When you run the command, you can see a response similar to the following:
    
    
    {
      "billingType": "POSTPAID"
    }

### Change of billing type

Your app developers and AppGroups can switch their billing from prepaid to postpaid and vice versa. This section describes the changes that happen in Apigee when changing a billing type.

#### Postpaid to prepaid

When switching from postpaid to prepaid, Apigee immediately sets the `billingType` to `PREPAID` in the configuration. The app developer or AppGroup can start using the APIs to the extent of the prepaid top-up amount. Based on your custom monetization reports, any existing usage in the postpaid account should be billed separately by you, the API provider.

#### Prepaid to postpaid

When switching from prepaid to postpaid, Apigee immediately sets the `billingType` to `POSTPAID` in the configuration. Your custom monetization reports show any existing balance (of all the currencies) in the prepaid account as a credit transaction. When calculating the amount due after the billing cycle, you (the API provider) must consider the credit balance in the account.

## View balance

To view the balance in an app developer's prepaid account, issue a `GET` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance`

To view the balance in an AppGroup's prepaid account, issue a `GET` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/appgroups/$APPGROUP_NAME/balance`

For more information about the API, see [organizations.developers.getBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/getBalance) or [organizations.appgroups.getBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/getBalance). 

The following example shows you how to view the balance in an app developer's prepaid account:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
    https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance
    

When you run the command, you can see a response similar to the following:
    
    
    {
      "wallets": [
        {
          "balance": {
            "currencyCode": "USD",
            "units": "150",
            "nanos": 500000000
          },
          "lastCreditTime": "1234567890"
        },
        {
          "balance": {
            "currencyCode": "INR",
            "units": "10000",
            "nanos": 600000000
          },
          "lastCreditTime": "9876543210"
        }
      ]
    }

In the sample response, the app developer has two prepaid account balances; one for each currency. You can find the balance amount in the `units` and the `nanos` fields. The `lastCreditTime` field is in epoch time format, and denotes the time at which the balance was last credited.

### Negative balance

If an app developer or AppGroup makes multiple API calls within a short time span, they could exceed the allowed API calls, resulting in a negative wallet balance.

This scenario occurs when multiple message processors are handling the API calls from the same app developer or AppGroup. Every message processor will have a copy of the balance based on which it allows the API calls. All message processors periodically sync their balances with the main balance. Because of the minor syncing delay, the wallet balance in a message processor might be out of sync with the main balance. For example, at a given point in time, if the wallet balance in a message processor is USD 2, the main balance might be USD 0. So the message processor allows the API calls, thinking that the wallet still has USD 2. 

Apigee syncs a message processor's wallet balance in near real time with minor delays, and you cannot control or configure this behavior of Apigee. However, in this situation the excess API calls are accounted for. After processing all the API calls from the app developer or AppGroup, the final amount in the wallet reflects the charge even for the excess API calls. So, when the app developer or AppGroup recharges the account next time, to have a positive wallet balance, the app developer or AppGroup must first pay up any negative balance amount in the wallet.

## Credit balance

To credit the balance in an app developer's prepaid account, issue a `POST` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance:credit`

To credit the balance in an AppGroup's prepaid account, issue a `POST` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/appgroups/$APPGROUP_NAME/balance:credit`

For more information about the API, see [organizations.developers.balance.credit](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/credit) or [organizations.appgroups.balance.credit](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance/credit). 

Crediting a balance involves the following steps, in order:

  1. An app developer or AppGroup tops-up the account from the developer portal by using a payment gateway.
  2. The developer portal generates a unique transaction ID for the top-up.
  3. The developer portal updates the developer balance by using the appropriate API whether it's an app developer or an AppGroup. 



The following example shows the API call for step 3 and credits an app developer's balance by USD 150.21. The `transactionId` is set to the value of the transaction ID of the top-up transaction (step 3).
    
    
    curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-type: application/json" \
    -X POST \
    -d '{
      "transactionAmount": {
         "currencyCode": "USD",
         "units": "150",
         "nanos": 210000000
      },
      "transactionId": "ab31b63e-f8e8-11eb-9a03-0242ac130003"
    }' \
    https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance:credit
    

When you run the command, you can see a response similar to the following:
    
    
    {
      "wallets": [
        {
          "balance": {
            "currencyCode": "USD",
            "units": "300",
            "nanos": 710000000
          },
          "lastCreditTime": "1234568890"
        },
        {
          "balance": {
            "currencyCode": "INR",
            "units": "10000",
            "nanos": 600000000
          },
          "lastCreditTime": "9876543210"
        }
      ]
    }

**Note** : After you credit a balance for a currency, it takes about 5 minutes for the new balance to reflect in all of Apigee's components. During this time, if you again try to credit the balance for the previously credited currency, the credit balance API reports an error. Therefore, as a best practice, wait about 5 minutes between two credits of a particular currency.

## Adjust balance

If you have under-charged or over-charged an account, you can use the `adjustBalance` API to debit or credit the account balance.

To adjust the balance in an app developer's prepaid account, issue a `POST` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance:adjust`

To adjust the balance in an AppGroup's prepaid account, issue a `POST` request to the following API: 

`https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/appgroups/$APPGROUP_NAME/balance:adjust`

For more information about the API, see [organizations.developers.balance.adjustBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/adjust) or [organizations.appgroups.balance.adjustBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance/adjust). 

If you want to debit the balance of an under-charged app developer or AppGroup, set the `units` field in the request to a positive value. The following example debits the balance in an app developer's prepaid account by USD `50`:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-type: application/json" \
    -X POST \
    -d '{
      "adjustment": {
        "units": "50",
        "currencyCode": "USD"
      }
    }' \
    https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance:adjust
    

When you run the command, you can see a response similar to the following:
    
    
    {
      "wallets": [
        {
          "balance": {
            "currencyCode": "USD",
            "units": "150"
          },
          "lastCreditTime": "1635489199530"
        }
      ]
    }
    

If you want to credit the balance of an over-charged app developer or AppGroup, set the `units` field in the request to a negative value. The following example credits the balance in an app developer's prepaid account by USD `50.1`:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
    -H "Content-type: application/json" \
    -X POST \
    -d '{
      "adjustment": {
        "units": "-50",
        "nanos": 100000000,
        "currencyCode": "USD"
      }
    }' \
    https://apigee.googleapis.com/v1/organizations/$YOUR_GOOGLE_PROJECT_ID/developers/$DEVELOPER_EMAIL_ID/balance:adjust
    

When you run the command, you can see a response similar to the following:
    
    
    {
      "wallets": [
        {
          "balance": {
            "currencyCode": "USD",
            "units": "200",
            "nanos": 100000000
          },
          "lastCreditTime": "1635489199530"
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
