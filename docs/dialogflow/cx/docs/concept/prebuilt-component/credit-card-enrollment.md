---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment/
title: Credit card enrollment prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:41.847746+00:00
---

# Credit card enrollment prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Credit card enrollment prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The credit card enrollment [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) allows new and existing customers to apply for a new credit card.

The component begins by collecting the end-user's telephone number to identify whether they are a new or existing customer. For a new user, the component will collect required details including their monthly income and category of expenses or card benefits the user is requesting. Once all required information has been collected, the component arranges a call back and provides the request number to the user.

For an existing customer, the component will retrieve registered user information and present available card options to the end-user based on their preferences and retrieved information including their credit score. Once the customer has selected a card option, the component will send a link to complete the enrollment procedure via registered channels including WhatsApp or SMS.

This component uses the [Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) and [Zip code collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection) prebuilt components to collect and validate user details.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### New user

Component checks whether the user is calling using a registered phone number and identifies that they are a new user. The component collects the category of card the user would like to enroll for and collects information to identify the user, including zip code and telephone number. The component then arranges a call back and gives the user the request number.

User input | Agent response  
---|---  
| Can you please confirm if you are an existing customer of our bank?  
I'm not |   
| We are glad that you would like to apply for a credit card with us. We have a wide range of credit cards that are suitable for you.  
  
To provide you with the best available cards, could you please state your monthly income in USD?  
5000 dollars |   
| Which expenses or benefits are you interested in? We have a range of options available, like travel, fuel, and shopping.  
I like shopping |   
| Your selected response falls under the shopping category. If you want to proceed further, say yes.  
Yes |   
| _Agent collects user's zip code using[Zip code collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection) prebuilt component_  
| You mentioned the zip code is 10011, is that correct?  
Yes that's right |   
| Great, we're done with collecting the zip code.  
| _Agent collects user's telephone number using[Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt component_  
| Got it. The number you mentioned is plus 1 6502530000, is that correct?  
Yes |   
| Great, we're done collecting the telephone number.  
  
One of our representatives will call you back for the related cards based on your criteria. Your request number is 993835.  
  
### Existing customer

Component identifies registered customer using their telephone number. The component then requests information like the category and type of card the user would like to enroll for. Once this information has been confirmed, the component asks the customer to select a channel to complete their enrollment process on, and sends the link to the customer's registered channel.

User input | Agent response  
---|---  
| We are glad that you continue selecting our product and services. We have a wide range of credit cards that are suitable for you.  
  
Which expenses or benefits are you interested in? We have a range of options available, like travel, fuel, and shopping.  
I want a card I can use when I go on my next vacation |   
| Your selected response falls under the travel category. If you want to proceed further, say yes.  
Yes |   
| There are 3 types of cards to suit your type of request: platinum travel card, gold travel card, classic travel card. Would you like to know information about all cards or a specific one? For example, if you are specifically looking for a classic card, please say classic card.  
Can you tell me about the platinum card? |   
| Sure, for a platinum travel card the annual fee is 95 dollars. Benefits include: get 10,000 bonus miles every year, earn unlimited 2x miles on all other purchases, miles are easy to earn and easy to use. You can find more information about benefits or bonuses on our website.  
  
Please confirm if you wish to enroll for the platinum travel card.  
Yes let's do that |   
| We will share a link with the enrollment procedure steps. Do you want us to share these card details with your mobile number through SMS or WhatsApp?  
SMS please |   
| Okay, we are sending the link to your registered mobile number. This action may take a few seconds. Can you please confirm if you have received the link by saying yes or no?  
I've got it |   
| Great, now you can open the link and check the card enrollment details. Once the data is completed, the issuance of the new card will be initiated and sent to your current address.  
  
### Denial of information

User declines to provide information required to enroll for a credit card. The component exits with a failure message.

User input | Agent response  
---|---  
| Can you please confirm if you are an existing customer of our bank?  
No I'm not |   
| We are glad that you would like to apply for a credit card with us. We have a wide range of credit cards that are suitable for you.  
  
To provide you with the best available cards, could you please state your monthly income in USD?  
I don't want to tell you that information |   
| Thank you for calling. We're sorry, but we are unable to proceed further without the requested information at this time.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Credit Card Enrollment  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_cc_enroll_collect_cardtype  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_cc_enroll_expense_category  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_credit_card_enrollment:get_available_card  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the current [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the end-user. | integer  
$session.params.phone_number | (optional) End-user's phone number. If this parameter is not provided, the component will collect the phone number from the end-user. | string  
$flow.max_retry_count | Specifies the number of retries given to the end-user. The default value is `3`. | integer  
$flow.currency_name | Specifies the currency expected when collecting monthly income details. The default value is `"USD"`. | string  
  
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
phone_number | User's local phone number, without the country code, used to identify the user. | string  
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

### Get account details

The `prebuilt_components_credit_card_enrollment:get_account_details` webhook is used by the component to retrieve the user's account details, if an account exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
account_count | The number of accounts associated with the registered phone number. | integer  
credit_score | The user's registered credit score. | integer  
  
####  To configure the Get account details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_enrollment:get_account_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get card count

The `prebuilt_components_credit_card_enrollment:get_card_count` webhook is used by the component to retrieve the number of credit cards associated with a registered user's account(s).

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
card_count | The total number of credit cards across a registered user's account(s). | integer  
  
####  To configure the Get card count webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_enrollment:get_card_count webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get available cards

The `prebuilt_components_credit_card_enrollment:get_available_card` webhook is used by the component to retrieve the list of cards available to the user for a specific category based on the user's credit score.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.expense_category | The expense category the user has selected to enroll in. Valid values are defined by the `prebuilt_components_cc_enroll_expense_category` custom entity. By default `fuel`, `shopping`, and `travel` are supported. | string  
$flow.credit_score | The user's credit score, retrieved by the component using the [Get account details](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment#get-account-details) webhook. | integer  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
available_card_names | List of cards available to the user, for example `["gold shopping card","classic shopping card"]`. | List (string)  
cards_count | The number of cards available to the user. | integer  
  
####  To configure the Get available cards webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_enrollment:get_available_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get selected card details

The `prebuilt_components_credit_card_enrollment:get_selected_card` webhook is used by the component to retrieve annual fees and benefits for the selected card.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.card_type | The card type the user has selected to enroll in. Valid values are defined by the `prebuilt_components_cc_enroll_card_type` custom entity. By default `classic`, `gold`, and `platinum` are supported. | string  
$flow.expense_category | The expense category the user has selected to enroll in. Valid values are defined by the `prebuilt_components_cc_enroll_expense_category` custom entity. By default `fuel`, `shopping`, and `travel` are supported. | string  
$flow.credit_score | The user's credit score, retrieved by the component using the [Get account details](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment#get-account-details) webhook. | integer  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
selected_card_benefits | Information about the benefits of the selected card. | string  
selected_card_annual_fee | The annual fee of the selected card. | integer  
selected_card_name | The name of the selected card. | string  
  
####  To configure the Get selected card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_enrollment:get_selected_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Submit enrollment request

The `prebuilt_components_credit_card_enrollment:submit_enroll` webhook is used by the component to create a card enrollment request based on the new user's provided preferences and user details.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.zipcode | User's provided zip code. | string  
$flow.monthly_salary | User's provided monthly salary. | integer  
$flow.currency_name | Currency of the monthly salary, configured in the component's input parameters. See [input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment#input-parameters). | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
request_number | Request number for the successful registration of the card enrollment request. | integer  
  
####  To configure the Submit enrollment request webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_enrollment:submit_enroll webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send message

The `prebuilt_components_credit_card_enrollment:send_message` webhook is used by the component to send a message containing a link to complete credit card enrollment for existing customers.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.channel | The channel the user has selected to receive the message on. Valid values are defined by the `prebuilt_components_cc_enroll_channel` custom entity. By default `SMS` and `WhatsApp` are supported. | string  
$flow.selected_card_name | List of cards selected by the user, for example `["gold shopping card","classic shopping card"]`. | List (string)  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
message_sent | Indicates whether the message was successfully sent to the channel specified by the user. | boolean  
  
####  To configure the Send message webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_credit_card_enrollment:send_message webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Credit card CVV collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection)

[ Next Credit card expiration date collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
