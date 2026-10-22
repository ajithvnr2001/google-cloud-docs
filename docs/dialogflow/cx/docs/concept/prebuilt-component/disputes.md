---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/disputes/
title: Disputes prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:41.061499+00:00
---

# Disputes prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/disputes/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Disputes prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The disputes [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) authenticates the user and allows them to dispute or contest charges, transactions and fees. This component uses a customized version of the [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component to authenticate account holders and cardholders. The component also uses a customized version of the [Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component to collect dates for disputed transactions.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Unauthenticated user with transaction dispute

The agent identifies that the user has not been previously authenticated and collects information to verify that the user is a registered account holder. The agent collects information about the dispute including the account number, dispute mode, date, and amount, and creates a new case for the dispute.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Remember that you can file a claim or dispute a charge on your online banking portal. Do you want to continue this conversation to file a claim or dispute?  
Yes, file a dispute |   
| Please tell us whether your dispute is related to credit card billing or transactions.  
It's about my transaction |   
| Please wait while we are fetching your account details.  
  
We have found that there are 2 accounts associated with your number. Please tell us the last 4 digits of the account you are referring to.  
1001 |   
| Thank you, the last 4 digits we've collected is 1001. Is that correct?  
Yes |   
| To begin, what was the date of the transaction?  
| _Agent collects date of transaction using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Can you confirm the amount you transferred? For example, if you want to find transaction above $100.30, say "100".  
15 dollars |   
| You have entered dispute amount of $15 for the date 2023-05-0. Do you want to raise a dispute on your account?  
Yes |   
| We have created a new case with your dispute. Your case number is 448639 and has been shared with your registered email address. After checking the information you gave us, we will refund your money back to your account ending with 1001.  
  
### Authenticated user with credit card dispute

The agent identifies that the user has been previously authenticated and retrieves information about the card registered to the user. The user selects to permanently lock the card, and the agent generates the permanently lock card request. The agent then asks the user whether they would like to reissue a new card for the permanently locked card, and creates a reissue request for the card.

User input | Agent response  
---|---  
| We have found that there are 2 credit cards associated with your number. Are you looking for a card number ending in 4321?  
Yes |   
| If your dispute is related to credit card billing, say "credit card billing".  
Credit card billing |   
| Do you want to raise a dispute related to an overcharge fee or an expense on your credit card bill?  
I was overcharged for a fee |   
| To begin, can you confirm in which month the potential issue happened?  
04 |   
| Can you confirm the amount you are looking to claim? For example, if you want to find claim above $100.30, say "100".  
4567 |   
| Thank you! Can you please confirm the description of the fee associated with this potential issue? You can choose from annual fees, transaction fees, late payment fees, or any other fees.  
It was an annual fee |   
| You have entered dispute amount of $4567 for the date 2023-04-01. Do you want to raise a dispute on your credit card?  
Yes |   
| We have created a new case with your dispute. Your case number is 111236 and has been shared with your registered phone number. Your case will be solved within the next 3 working days.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Disputes  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_disputes_dispute_type  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_disputes_dispute_reason  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_disputes:get_disputed_transaction  
  
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
$session.params.card_count | (optional) Number of credit cards associated with the authenticated user. | integer  
$session.params.account_count | (optional) The number of accounts associated with the registered telephone number. These accounts include self-accounts and accounts for which the user has power of attorney. | integer  
$session.params.last_four_digit_of_card_number | (optional) Last four digits of the card number for which the dispute may be raised. If the customer has a single card, this information is retrieved automatically post authentication. If the customer has multiple cards, the specific card number is collected from the customer. | string  
$session.params.last_four_digit_of_account_number | (optional) Last four digits of the customer account number for which the dispute may be raised. If the customer has a single account, this information is retrieved automatically post authentication. If the customer has multiple accounts, the specific account number is collected from the customer. | string  
$flow.max_dispute_month | Specifies the maximum number of months before the current date allowed for a disputed transaction date. By default, this value is `-6`, indicating that disputes may be raised for transactions no more than 6 months before the current date. | integer  
$flow.max_attempts | Specifies the number of retries allowed when collecting the one-time password (OTP) from the user. The default value is `2`. | integer  
flow.max_retry_counter | Specifies the number of retries allowed when collecting information from the user. The default value is `2`. | integer  
  
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
card_count | Number of credit cards associated with the authenticated user. | integer  
account_count | The number of accounts associated with the registered telephone number. These accounts include self-accounts and accounts for which the user has power of attorney. | integer  
last_four_digit_of_card_number | Last four digits of the card number for which the dispute was raised. | string  
last_four_digit_of_account_number | Last four digits of the customer account number for which the dispute was raised. | string  
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

### Get credit card details

The `prebuilt_components_account_services:get_credit_card_details` webhook is used by the component to get information about the credit card(s) registered to a user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
credit_card_count | The number of credit cards associated with the registered telephone number. | integer  
last_four_digit_of_credit_card_number | If a user has a single credit card, the last four digits of the card number are returned. If a user has more than one card, the value of this parameter is `null`. | string  
email | The email registered with the account. If there is no email registered with the account, the value of this parameter is `null`. | string  
  
####  To configure the Get credit card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_services:get_credit_card_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Validate credit card

The `prebuilt_components_disputes:validate_credit_card` webhook is used by the component to validate that a specified credit card is registered to the user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | The last four digits of the card number the user requested to raise a dispute for. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
card_found | Indicates whether the requested card exists. | boolean  
  
####  To configure the Validate credit card webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_disputes:validate_credit_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Validate account

The `prebuilt_components_account_services:validate_account` webhook is used by the component to verify that an account exists based on the user's registered phone number and the last four digits of the account number provided. The webhook also returns the account balance, if an account exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user requested to raise a dispute for. | string  
  
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



### Validate transaction

The `prebuilt_components_disputes:validate_transaction` webhook is used by the component to validate whether a specified transaction exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.dispute_type | The type of the disputed transaction. Valid values are defined by the `prebuilt_components_disputes_dispute_type` custom entity. | string  
$flow.dispute_date | The date of the disputed transaction in YYYY-MM-DD format. | string  
$flow.dispute_amount | The amount of the disputed transaction. | integer  
$flow.last_four_digits | The last four digits of the credit card or account number the disputed transaction is on. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
transaction_found | Indicates whether the requested transaction exists. | boolean  
  
####  To configure the Validate transaction webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_disputes:validate_transaction webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Create dispute case

The `prebuilt_components_disputes:create_dispute_case` webhook is used by the component to create a new case for a dispute.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.dispute_type | The type of the dispute. Valid values are defined by the `prebuilt_components_disputes_dispute_type` custom entity. | string  
$flow.dispute_date | The date of the disputed transaction in YYYY-MM-DD format. | string  
$flow.dispute_amount | The amount of the disputed transaction. | integer  
$flow.dispute_reason | The reason for the dispute. Valid values are defined by the `prebuilt_components_disputes_dispute_reason` custom entity. | string  
$flow.dispute_fee_type | Fee type for the dispute. Valid values are defined by the `prebuilt_components_disputes_fee_types` custom entity. | string  
$flow.last_four_digits | The last four digits of the credit card or account number the disputed transaction is on. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
dispute_case_number | The case number for the created dispute. | integer  
  
####  To configure the Create dispute case webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_disputes:create_dispute_case webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Date of birth collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection)

[ Next Exchange order  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
