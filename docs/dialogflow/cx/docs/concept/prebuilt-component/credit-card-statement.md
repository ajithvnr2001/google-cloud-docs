---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-statement/
title: Credit card statement prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:08.402890+00:00
---

# Credit card statement prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-statement/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Credit card statement prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The credit card statement [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a customer's [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels), then sends the credit card statement for a specified period of time to an authenticated customer. If the customer has multiple credit cards, the component confirms the specific card the customer would like to retrieve a credit card statement for. This component uses a customized version of the [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component to authenticate cardholders and uses a customized version of [Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) to collect start and end dates for the statement period.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Single credit card

End-user has a single credit card. The agent collects the statement start and end dates, whether the user would like to encrypt the statement, and sends the credit card statement to the user.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Please wait while we are fetching your card details.  
  
We have found a card number ending with 1002 associated with your number.  
| Please provide credit card statement start date, starting with the month, followed by day and then year. Please note that the credit card statement will be provided only for the last 180 days.  
| _Agent collects statement start date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we have collected your credit card statement start date.  
  
Please provide credit card statement end date, starting with the month, followed by day and then year. Please note that the credit card statement will be provided only for the last 180 days.  
| _Agent collects statement end date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we have collected your credit card statement end date.  
  
Thank you. Please confirm if you are looking for the statement between 2023-06-01 and 2023-06-30.  
Yes |   
| Please wait while we are fetching your statement details.  
  
We found transactions between 2023-06-01 and 2023-06-30. Would you like to receive it via email, SMS, or WhatsApp?  
Send it to my email |   
| Do you want to encrypt the document before we share it with you?  
No thanks |   
| You will receive the statement within 15 minutes on your registered email.  
  
### Multiple credit cards

End-user has multiple credit cards; the agent confirms which card the user is requesting a credit card statement for. The agent collects the statement start and end dates, whether the user would like to encrypt the statement, and sends the credit card statement to the user.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully validated.  
| Please wait while we are fetching your card details.  
  
We have found that there are 2 cards associated with your number. Can you please help us with the last 4 digits of the card you are referring to?  
1122 |   
| The last four digits of the card number that we got is 1122, is that correct?  
Yes |   
| Please provide credit card statement start date, starting with the month, followed by day and then year. Please note that the credit card statement will be provided only for the last 180 days.  
| _Agent collects statement start date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we have collected your credit card statement start date.  
  
Please provide credit card statement end date, starting with the month, followed by day and then year. Please note that the credit card statement will be provided only for the last 180 days.  
| _Agent collects statement end date using[Date of birth](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we have collected your credit card statement end date.  
  
Thank you. Please confirm if you are looking for the statement between 2023-07-13 and 2023-07-14.  
Yes |   
| Please wait while we are fetching your statement details.  
  
We found transactions between 2023-07-13 and 2023-07-14. Would you like to receive it via email, SMS, or WhatsApp?  
SMS |   
| Do you want to encrypt the document before we share it with you?  
Yes |   
| Password details will be shared on your registered mobile.  
  
You will receive the statement within 15 minutes on your registered mobile.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Credit Card Statement  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_statement_channel_all  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_credit_card_statement:request_statement  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
$session.params.auth_level_req | Indicates the [level of authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) needed before a user can access their credit card statement. This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `1`. | integer  
$session.params.account_auth_enabled | Indicates whether the user should be authenticated as an account holder as described in [Authentication levels](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `false`. | boolean  
$session.params.card_auth_enabled | Indicates whether the user should be authenticated as a card holder as described in [Authentication levels](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `true`. | boolean  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$session.params.credit_card_count | (optional) Number of credit cards associated with the authenticated user. | integer  
$session.params.last_four_digit_of_card_number | (optional) Last four digits of the customer card number for which the statement needs to be provided. If the customer has a single card, this information is retrieved automatically post authentication. If the customer has multiple cards, the specific card number is collected from the customer. | string  
$session.params.credit_card_statement_max_days | Specifies the maximum number of days before the current date allowed for a statement start date. By default, this value is `-180`, indicating that statement start dates may start no more than 180 days before the current date. This parameter is configured in the start page `true` route. | integer  
$flow.max_retry_count | Specifies the number of retries allowed when prompting the end-user to provide a valid statement end date. The default value is `3`. | integer  
  
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
credit_card_count | The number of credit cards associated with the registered telephone number. | integer  
last_four_digit_of_card_number | If a user has a single card, the last four digits of the card number are returned. If a user has more than one card, the value of this parameter is the last four digits of the card number the user selected to receive credit card statement information for. | string  
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

The `prebuilt_components_credit_card_statement:credit_card_details` webhook is used by the component to retrieve credit card details for a registered telephone number.

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
credit_card | Last four digits of the customer's credit card number. If the customer has multiple cards, this value is `null`. | string  
email | The user's registered email. If there is no email registered to the telephone number, this value is `null`. | string  
  
####  To configure the Get credit card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_statement:credit_card_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Validate card

The `prebuilt_components_credit_card_statement:validate_date` webhook is used by the component to validate whether a given credit card exists for a registered telephone number.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | Last four digits of the user's provided credit card number. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
valid_card | Indicates whether the given card was found for the registered telephone number. | boolean  
  
####  To configure the Validate card webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_statement:validate_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get transactions

The `prebuilt_components_credit_card_statement:card_transaction_details` webhook is used by the component to retrieve the transactions for a card given the user's registered phone number, the last four digits of the card number, and the statement period.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | The last four digits of the card number the user selected and confirmed to receive credit card statement information for. | string  
$flow.statement_start_date | The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.statement_end_date | (optional) The requested statement start date in "YYYY-MM-DD" format. If no value is provided by the user or caller declines to provide an end date, the value defaults to the current date. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
transactions_count | The number of transactions found for the specified credit card in the given statement period. | integer  
  
####  To configure the Get transactions webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_statement:card_transaction_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Request statement

The `prebuilt_components_credit_card_statement:request_statement` webhook is used by the component to send a statement for a credit card to a selected channel given the user's registered phone number, the last four digits of the credit card number, and the statement period.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | The last four digits of the card number the user selected and confirmed to receive credit card statement information for. | string  
$flow.statement_start_date | The requested statement start date in "YYYY-MM-DD" format. | string  
$flow.statement_end_date | (optional) The requested statement start date in "YYYY-MM-DD" format. If no value is provided by the user or caller declines to provide an end date, the value defaults to the current date. | string  
$flow.channel_medium | The channel the user has selected to receive the message on. Valid values are defined by the `prebuilt_components_statement_channel_phone` and `prebuilt_components_statement_channel_all` custom entities, depending on whether the user has a registered email. By default `email`, `mobile` and `WhatsApp` are supported. | string  
$flow.encryption_status | Indicates whether the user wants the document encrypted before sending to the specified channel. If no value is provided by the user or caller declines to provide an end date, the value defaults to `true`. | boolean  
  
####  To configure the Request statement webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_statement:request_statement webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Credit card number collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-number-collection)

[ Next Date of birth collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
