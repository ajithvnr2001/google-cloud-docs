---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lock-card/
title: Lock card prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:57.033222+00:00
---

# Lock card prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lock-card/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Lock card prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The lock card [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) authenticates the user, retrieves cards registered to the user, and allows the user to lock a card temporarily, lock a card permanently, or reactivate a card. After confirming a locked card, the component allows the user to request a new card. This component uses a customized version of the [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component to authenticate cardholders.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Unauthenticated user with multiple cards

The agent identifies that the user has not been previously authenticated and collects information to verify that the user is a registered cardholder. Once the user has authenticated, the agent retrieves information about the cards registered to the user. The user confirms they would like to temporarily lock a selected card, and the agent generates the lock card request.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Please wait while we are fetching your card details.  
  
We have found multiple cards registered with your number. We have a Visa ending in 5555, a Visa ending in 6666, a MasterCard ending in 4444, and a MasterCard ending in 4449.  
  
Please tell us the last 4 digits of the card you would like to lock or reactivate.  
4444 |   
| The last four digits of the card number that we got is 4444, is that correct?  
Yes |   
| Do you want to lock your card temporarily or permanently?  
I want to lock it temporarily |   
| Please tell us why you are locking your card. You can choose from options like damaged, stolen, lost or others.  
It got damaged |   
| Sorry to hear that. For security purposes, we need to validate your identity, so we will send you a code. Do you prefer to receive the code by phone or by email?  
Send it to my phone |   
| Okay, before proceeding, we will send a code to your registered mobile number. Can you please confirm your code to validate the request?  
123456 |   
| Okay, your card ending with 4444 will be temporarily locked. Once locked, you will not be able to make any transactions online or on POS machines with that card. Do you confirm this action?  
Yes |   
| Your card was locked successfully. Your request number is 9711485 and has been shared successfully with your registered mobile number.  
  
### Authenticated user with single card

The agent identifies that the user has been previously authenticated and retrieves information about the card registered to the user. The user selects to permanently lock the card, and the agent generates the permanently lock card request. The agent then asks the user whether they would like to reissue a new card for the permanently locked card, and creates a reissue request for the card.

User input | Agent response  
---|---  
| Please wait while we are fetching your card details.  
  
We have found your MasterCard ending in 4444. Do you want to lock your card temporarily or permanently?  
Permanently |   
| Please tell us why you are locking your card. You can choose from options like damaged, stolen, lost or others.  
It was damaged |   
| Sorry to hear that. Don't worry, we will permanently lock your card. Can you please confirm if the card ends with 4444?  
Yes |   
| Okay, before proceeding, we will send a code to your registered mobile number. Can you please confirm your code to validate the request?  
123456 |   
| Okay, your card ending with 4444 will be temporarily locked. Once locked, you will not be able to make any transactions online or on POS machines with that card. Do you confirm this action?  
Yes |   
| Your card was locked successfully. Your request number is 6108410 and has been shared successfully with your registered mobile number.  
  
Do you want to reissue a new card?  
Yes |   
| We will deliver the card to your registered address. Can you please confirm your delivery address zip code 12345?  
That's correct |   
| Okay, please wait for a few seconds while we are raising the request for reissuing a new card.  
  
The reissue request for the new card was successful. Your request number is 3808109 and has been shared successfully with your registered mobile number.  
  
The card will be delivered to your registered address in 3 working days. To use the card please follow the instructions shared with the card.  
  
### Reactivate card

The agent identifies that the user requires additional authentication and sends a one-time password to verify the user's identity. The user requests to reactivate a card, and the agent transfers them to a human agent to continue.

User input | Agent response  
---|---  
| For security purposes, we need to validate your identity, so we will send you a code. Do you prefer to receive the code by phone?  
Yes |   
| We have sent a code to your registered phone number ending with 5041. This may take a few seconds. Can you please confirm the code?  
123456 |   
| Thank you, you have been successfully validated.  
  
Please wait while we are fetching your card details.  
  
We have found multiple cards registered with your number. We have a Visa ending in 1456, a MasterCard ending in 1457, a American Express ending in 1345, and a Visa ending in 3456.  
  
Please tell us the last 4 digits of the card you would like to lock or reactivate.  
1456 |   
| The last four digits of the card number that we got is 1456, is that correct?  
Yes |   
| The requested card is already in a temporary locked status. Do you want to reactivate the card, or block it permanently?  
Reactivate it |   
| Please hold while we transfer your call in order to assist you better.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Lock Card  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_lock_card_locked_reason  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_lock_card:lock_card_ticket_number  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
$session.params.auth_level_req | Indicates the [level of authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) needed before a user can access their transaction history. This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `1`. | integer  
$session.params.account_auth_enabled | Indicates whether the user should be authenticated as an account holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `false`. | boolean  
$session.params.card_auth_enabled | Indicates whether the user should be authenticated as a card holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `true`. | boolean  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$session.params.card_count | (optional) Number of credit cards associated with the authenticated user. | integer  
$flow.card_status_active | Specifies the value of the parameter returned by the [Validate card webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card#validate-card) to indicate the selected card is currently active. By default the value is `"active"`. | string  
$flow.card_status_lock_temp | Specifies the value of the parameter returned by the [Validate card webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card#validate-card) to indicate the selected card is temporarily locked. By default the value is `"inactive"`. | string  
$flow.card_status_lock_permanent | Specifies the value of the parameter returned by the [Validate card webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card#validate-card) to indicate the selected card is permanently locked. By default the value is `"blocked"`. | string  
$flow.card_status_reactivate | Specifies the value of the parameter returned by the [Validate card webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card#validate-card) to indicate the selected card is reactivated. By default the value is `"reactivate"`. | string  
$flow.max_retry_card_number | Specifies the number of retries allowed when collecting the last four digits of the credit card. The default value is `3`. | integer  
$flow.max_otp_retry_count | Specifies the number of retries allowed when collecting the one-time password (OTP) from the user. The default value is `3`. | integer  
  
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
auth_level | Indicates the authentication level of the caller. | integer  
phone_number | User's local phone number, without the country code, used to identify the user. | string  
card_count | The number of cards associated with the registered telephone number. | integer  
last_four_digit_of_card_number | If a user has a single card, the last four digits of the card number are returned. If a user has more than one card, the value of this parameter is the last four digits of the card the user selected to lock or reissue a new card for. | string  
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

### Get card details

The `prebuilt_components_account_services:get_card_details` webhook is used by the component to get information about the card(s) registered to a user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
last_four_digit_of_all_cards | List containing the last four digits of each card registered to the user, for example `["0000", "1111", "2222"]`. Each element in this list represents the same card as the element with the same index in `card_vendor_all`. | List (string)  
card_vendor_all | List containing the credit card vendor for each card registered to the user, for example `["Visa", "Mastercard", "Discover"]`. Each element in this list represents the same card as the element with the same index in `last_four_digit_of_all_cards`. | List (string)  
card_count | Number of cards associated with the authenticated user. | integer  
  
####  To configure the Get card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_services:get_card_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Validate card

The `prebuilt_components_lock_card:validate_card` webhook is used by the component to get information about a specific card registered to a user's account.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | The last four digits of the card number the user requested to lock. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
zip_code | Zip code registered to the user's account. | string  
card_vendor | The credit card vendor for the selected card. | string  
card_status | Indicates the current status of the card. By default, valid values are active, temporarily blocked, or permanently blocked. These status are specified by the parameters `$flow.card_status_active`, `$flow.card_status_lock_temp`, and `$flow.card_status_lock_permanent`. See [input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lock-card#input-parameters). | string  
  
####  To configure the Validate card webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_lock_card:validate_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Lock card

The `prebuilt_components_lock_card:lock_card_ticket_number` webhook is used by the component to create a request to lock a selected card.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | The last four digits of the card number the user requested to lock. | string  
$flow.lock_type | Indicates the type of lock to be applied to the user's card. Valid values are defined by the `prebuilt_components_lock_card_lock_type_active` custom entity. By default `"blocked"` (permanent lock) and `"inactive` (temporary lock) are supported. | string  
$flow.lock_reason | Indicates the reason the user requested the card to be locked. Valid values are defined by the `prebuilt_components_lock_card_locked_reason` custom entity. By default `"damaged"`, `"stolen"`, `"lost"`, and `"others"` are supported. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
ticket_number | The ticket number for the created lock card request. | integer  
  
####  To configure the Lock card webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_lock_card:lock_card_ticket_number webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Reissue card

The `prebuilt_components_lock_card:reissue_card_number` webhook is used by the component to create a request to reissue a new or upgraded card.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_card_number | The last four digits of the card number the user requested to lock. | string  
zip_code | Zip code registered to the user's account. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
acknowledgement_number | The ticket number for the created reissue card request. | integer  
  
####  To configure the Reissue card webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_lock_card:reissue_card_number webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Greeting  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/greeting)

[ Next Lost and stolen card  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
