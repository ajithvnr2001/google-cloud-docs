---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail/
title: Retail authentication prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:51.177059+00:00
---

# Retail authentication prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Retail authentication prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The retail authentication [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) collects information from the user to authenticate them to the required authentication level. This component covers authentication requirements which are common, but not exclusive, to the retail industry. This component uses the [Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt component to collect and validate user details.

## Authentication levels

There are multiple levels of authentication required by different prebuilt components, with higher levels requiring more user information to authenticate the user. The retail authentication component allows users to authenticate to Level 0 (ANI Match) or Level 1 (Basic) as described in the Authentication Level table.

Authentication Level | Requirements  
---|---  
Level 0: ANI Match | User is authenticated by calling from or providing a phone number that corresponds to a registered account.  
  
A user can be authenticated to Level 0 by using the [Greeting prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/greeting).  
Level 1: Basic | User is authenticated by verifying a one-time password (OTP) code sent to their email or phone number.  
  
## Supported user types

The retail authentication component provides support for users with a registered phone number and email.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * OTPs will only be sent to a mobile number or email address previously registered to the user. The component won't use OTP to authenticate customers calling from an alternate phone number that is not registered with their account. When a user calls from an alternate phone number, security questions will be used to authenticate the caller.
  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Level 0 authentication success: ANI match

User calls from a phone number registered to an existing account, confirms their account, and is successfully authenticated to Level 0.

User input | Agent response  
---|---  
| Hello, the number you dialed is linked to John's account. Are you inquiring about another person's order? Please say yes if that's the case, else say no.  
No |   
| Thank you John. You have been successfully identified.  
  
### Level 1 authentication success: OTP

User calls from an unrecognized phone number. The component collects the user's registered phone number, then sends and asks user to confirm an OTP sent to the channel of the user's choice. User is able to provide a valid OTP and is successfully authenticated to Level 1.

User input | Agent response  
---|---  
We couldn't find this phone number associated with us. Kindly provide us with the registered phone number. |   
| _Agent collects telephone number using[Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt component_  
| Great, we are done collecting the telephone number.  
  
For security purposes, we need to validate your identity, so we will send you a code. Do you prefer to receive the code by phone or by email?  
phone |   
| Just to confirm, would you like to receive the OTP on your phone? Please say yes or no.  
yes |   
| We have sent a code to your registered phone number ending with 0000. This may take a few seconds. Can you please confirm the code?  
123457 |   
| Thank you John. You have been successfully identified.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Retail Authentication  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_retail_authentication_incorrect_phone_number  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_channel_email_phone  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_retail_authentication:verify_user_details  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level_req | Defines the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail#authentication-levels) the end-user will be authenticated to. Valid values are `0` or `1`. | integer  
$session.params.auth_level | (optional) Indicates the current [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail#authentication-levels) of the end-user. | integer  
$session.params.phone_number | (optional) End-user's phone number. If this parameter is not provided, the component will collect the phone number from the end-user. | string  
$flow.max_retry_phone_number | Specifies the number of retries allowed when collecting the user's telephone number. The default value is `3`. | integer  
$flow.max_retry_otp | Specifies the number of retries allowed when collecting the One Time Password (OTP). The default value is `3`. | integer  
$flow.max_retry_otp_not_received | Specifies the number of retries allowed when the One Time Password (OTP) is not received. The default value is `1`. | integer  
$flow.max_retry_otp_confirm_channel | Specifies the number of retries allowed when collecting the channel to receive the One Time Password (OTP). The default value is `3`. | integer  
  
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
auth_level | Indicates the current [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail#authentication-levels) of the end-user. | integer  
all_recent_order_id | This parameter lists order IDs associated with the authenticated user, sorted by the order placement date in descending order. The first element of the array represents the most recent order. If a user has no orders, the value of this parameter is `null`. | List (string)  
phone_number | User's local phone number, without the country code, used to identify the user. | string  
email | The email registered with the account. | string  
user_first_name | User's first name, used to greet and confirm ownership of the account. | string  
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

### Verify user details

The `prebuilt_components_retail_authentication:verify_user_details` webhook is used by the component to fetch user account details based on the provided telephone number.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
email | The email registered with the account. | string  
all_recent_order_id | List of order IDs associated with the authenticated user, sorted by the order placement date in descending order. The first element of the array represents the most recent order. If a user has no orders, the value of this parameter is `null`. | List (string)  
user_first_name | User's first name, used to greet and confirm ownership of the account. | string  
  
####  To configure the Verify user details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_retail_authentication:verify_user_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send OTP

The `prebuilt_components_retail_authentication:send_otp` webhook is used by the component to send a one-time password (OTP) to a registered channel selected by the end-user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.channel | The channel the user has selected to receive the OTP on. Valid values are defined by the `prebuilt_components_channel_email_phone` custom entity. By default `email` and `phone` are supported. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
generated_otp | The value of the OTP generated and sent to the user using the selected channel. | string  
  
####  To configure the Send OTP webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_retail_authentication:send_otp webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Authentication  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication)

[ Next Cancel order  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
