---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/transaction-history/
title: Transaction history prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:15.716143+00:00
---

# Transaction history prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/transaction-history/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Transaction history prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The transaction history [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a customer's [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels), then collects transactions time period and other filters which are applied when retrieving the transaction history. This component supports filters for:

  * Transaction type
  * Merchant name
  * Transaction amount



If the customer has multiple accounts, the component confirms the specific account the customer would like to retrieve transaction history for. This component uses the [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component to authenticate users and uses a customized version of [Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) to collect start and end dates for the transaction history.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Multiple accounts

End-user has multiple accounts; the agent confirms which account the user is requesting transaction history for. The agent collects the transactions start and end dates, any filters the user would like to apply to the transactions, and whether the user would like to encrypt the transaction history. The agent sends the transaction history to the user.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Please wait while we are fetching your account details.  
  
We have found that there are 2 accounts associated with your number.  
  
Can you please help us with the last 4 digits of the account you are referring to?  
1001 |   
| The last four digits of the account number that we got are 1001, is that correct?  
Yes |   
| Please provide your transactions start date, starting with the month, followed by day and then year. Please note that the transaction history will be provided only for the last 90 days.  
| _Agent collects transactions start date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we have collected your transactions start date.  
  
Please provide your transactions end date, starting with the month, followed by day and then year. Please note that the transaction history will be provided only for the last 90 days.  
| _Agent collects transactions start date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Thank you. Please confirm if you are looking for the transactions between 2023-06-25 to 2023-07-21?  
Yes |   
| Please tell us the name of the merchant you want to get transactions for.  
Google |   
| The merchant name we captured is "Google". Can you please confirm with a yes or no?  
Yes |   
| Do you want to see the transaction history for your debit or credit cards?  
Credit |   
| Please provide an amount to retrieve transactions at or over the given amount. For example, if you want to find transactions above $100.30, say "100".  
500 |   
| Please wait while we are fetching your transaction details.  
  
We found transactions from 2023-06-2 to 2023-07-21. Would you like to receive it via SMS or WhatsApp?  
SMS |   
| Do you want to encrypt the document before we share it with you?  
Yes please |   
| Password details will be shared on your registered mobile.  
  
You will receive the statement within 15 minutes on your registered mobile.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Transaction History  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_transaction_history_transaction_collection  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_transaction_history_det_cred  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_transaction_history:get_transactions  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
$session.params.auth_level_req | Indicates the [level of authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) needed before a user can access their transaction history. This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `1`. | integer  
$session.params.account_auth_enabled | Indicates whether the user should be authenticated as an account holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `true`. | boolean  
$session.params.card_auth_enabled | Indicates whether the user should be authenticated as a card holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `false`. | boolean  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$session.params.account_count | (optional) Number of accounts associated with the authenticated user. | integer  
$session.params.last_four_digit_of_account_number | (optional) Last four digits of the customer account number for which the transaction history needs to be provided. If the customer has a single account, this information is retrieved automatically post authentication. If the customer has multiple accounts, the specific account number is collected from the customer. | string  
$session.params.transaction_history_max_days | Specifies the maximum number of days before the current date allowed for a transactions start date. By default, this value is `-90`, indicating that transactions start dates may start no more than 90 days before the current date. This parameter is set in the start page `true` route. | integer  
$flow.max_retry_count | Specifies the number of retries allowed when prompting the end-user to provide valid transactions start and end dates. The default value is `3`. | integer  
  
####  To configure the input parameters for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Build** tab. 
  5. Click the imported component in the **Flows** section. 
  6. Click the Start Page in the **Pages** section. 
  7. Click the **true** Route in the Start Page. 
  8. In the Route window, edit the **Parameter Presets** values as needed. 
  9. Click **Save**. 



## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
auth_level | Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
phone_number | User's local phone number, without the country code, used to identify the user. | string  
account_count | The number of accounts associated with the registered telephone number. These accounts include self-accounts and accounts for which the user has power of attorney. | integer  
last_four_digit_of_account_number | If a user has a single account, the last four digits of the account number are returned. If a user has more than one account, the value of this parameter is the last four digits of the account number the user selected to receive transaction history for. | string  
transfer_reason | This parameter indicates the reason the flow exited, if it was not successful. The returned value is one of:  
  
`agent`: the end-user requested a human agent at some point during the conversation.  
  
`denial_of_information`: the end-user declined to share information requested by the component.  
  
`max_no_input`: the conversation reached the maximum number of retries for no-input events. See [no-input built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).  
  
`max_no_match`: the conversation reached the maximum number of retries for no-match events. See [no-match built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).  
  
`webhook_error`: a webhook error occurred. See [webhook.error built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).   
  
`webhook_not_found`: a webhook URL was unreachable. See [webhook.error.not-found built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in). | string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. Configure the provided [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with configuration describing your external services, see Webhook setup below.



## Webhook setup

In order to use this component, you will need to configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Authentication

If you have not previously configured external services required for authentication, you will need to configure them to enable authentication of users for this component. See [Authentication webhook setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#webhook-setup) for detailed instructions.

### Validate account

The `prebuilt_components_account_services:validate_account` webhook is used by the component to verify that an account exists based on the user's registered phone number and the last four digits of the account number provided. The webhook also returns the account balance, if an account exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to receive account statement information for. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
account_found | Indicates whether an account with the provided last four digits exists for the user's registered account. | boolean  
balance | The amount of the current balance on the account, if it exists. | number  
  
####  To configure the Validate account webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_services:validate_account webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get transactions

The `prebuilt_components_transaction_history:get_transactions` webhook is used by the component to retrieve the number of transactions for an account given the user's registered phone number, the last four digits of the account number, the transaction history period, and any filters selected by the user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to receive transaction history for. | string  
$flow.statement_start_date | The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.statement_end_date | (optional) The requested statement start date in "YYYY-MM-DD" format. If no value is provided by the user or caller declines to provide an end date, the value defaults to the current date. | string  
$flow.transaction_credit_debit | Transaction type requested by the user. Valid values are defined by the `prebuilt_components_transaction_history_det_cred` custom entity. By default `"credit"` and `"debit"` are supported. If the user declines to select a type, this value is an empty string `""` and transactions of any type should be counted. | string  
$flow.merchant_name | Merchant name requested by the user. If the user declines to provide a merchant name, this value is an empty string `""` and transactions from all merchants should be counted. | string  
$flow.high_amount_value | Minimum transaction amount requested by the user. If the user declines to provide an amount, this parameter has a default value of `0`. | integer  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
transactions_count | The number of transactions found for the specified account in the given statement period with the selected filters applied. | integer  
  
####  To configure the Get transactions webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_transaction_historyt:get_transactions webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send info

The `prebuilt_components_transaction_history:send_info` webhook is used by the component to send a transaction history to a selected channel given the user's registered phone number, the last four digits of the account number, the transaction history period, and any filters selected by the user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to receive transaction history for. | string  
$flow.statement_start_date | The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.statement_end_date | (optional) The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.transaction_credit_debit | Transaction type requested by the user. Valid values are defined by the `prebuilt_components_transaction_history_det_cred` custom entity. By default `"credit"` and `"debit"` are supported. If the user declines to select a type, this value is an empty string `""` and transactions of any type should be sent. | string  
$flow.merchant_name | Merchant name requested by the user. If the user declines to provide a merchant name, this value is an empty string `""` and transactions from all merchants should be sent. | string  
$flow.high_amount_value | Minimum transaction amount requested by the user. If the user declines to provide an amount, this parameter has a default value of `0`. | integer  
$flow.channel_medium | The channel the user has selected to receive the message on. Valid values are defined by the `prebuilt_components_transaction_history_phone` and `prebuilt_components_transaction_history_channel` custom entities, depending on whether the user has a registered email. By default `email`, `mobile` and `whatsapp` are supported. | string  
$flow.encryption_status | Indicates whether the user wants the document encrypted before sending to the specified channel. If no value is provided by the user or caller declines to provide an end date, the value defaults to `true`. | boolean  
  
####  To configure the Send info webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_transaction_history:send_info webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Telephone number collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection)

[ Next Waiting room  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/waiting-room)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
