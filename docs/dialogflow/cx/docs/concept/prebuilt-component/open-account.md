---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account/
title: Open account prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:42.865250+00:00
---

# Open account prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Open account prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The open account [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) allows new and existing users to open a new account or check the status of existing applications. This component uses the [Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection), [Name collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection), and [Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt components to collect user information to register a new account.

## Account types

By default, this component supports the following account types:

  * Savings accounts
  * Checking accounts, also known as current accounts
  * Demat accounts
  * Salary accounts



Supported account types may be added or removed by modifying the `prebuilt_components_open_account_account_type` custom entity.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### New user

The agent collects the user's phone number and identifies that the user is not registered for an account. The agent then collects details including the user's full name and date of birth, and generates an application which is sent to the user's provided telephone number.

User input | Agent response  
---|---  
| Please provide us with the telephone number for validation purposes.  
| _Agent collects user's telephone number using[Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt component_  
| Great, we are done collecting the telephone number.  
We are glad that you would like to open an account with us.  
| _Agent collects user's full name using[Name collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection) prebuilt component_  
| Thank you, John Doe.  
| _Agent collects user's telephone number using[Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we've collected your birthdate.  
  
What type of account are you looking to open? You can say savings, checking, salary, or demat.  
Current account |   
| To confirm, you would like to open a new checking account, is that correct?  
Yes |   
| Thanks for providing the information. Please wait while we generate your application.  
  
Your application ID is 81037. Please complete your application by clicking on the link provided on your registered mobile number.  
  
### Existing user

The agent identifies that the user has been previously authenticated and confirms what type of account the user would like to open. The agent creates an application to the user and sends instructions to the user's registered phone number.

User input | Agent response  
---|---  
| We are glad that you would like to open a new account with us.  
  
What type of account are you looking to open? You can say savings, checking, salary, or demat.  
Savings account please |   
| To confirm, you would like to open a new savings account, is that correct?  
Yes that's right |   
| Thanks for providing the information. Please wait while we generate your application.  
  
Your application ID is 21430. Please complete your application by clicking on the link provided on your registered mobile number.  
  
### Existing application

The agent identifies that the user has previously opened a single application and presents the user with the current status. The user declines to open another application for a new account.

User input | Agent response  
---|---  
| Please provide us with the telephone number for validation purposes.  
| _Agent collects user's telephone number using[Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt component_  
| Great, we are done collecting the telephone number.  
  
Your application with ID 12234 for opening a savings account is in progress. Would you like to open another account?  
No |   
| Okay, thank you for calling us.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Open Account  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_open_account_account_type  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_open_account_account_type  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_open_account:generate_application  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$session.params.min_age_limit | Specifies the minimum age allowed for users who are opening a new account. The default value is `18`. | integer  
$session.params.max_age_limit | Specifies the maximum age allowed for users who are opening a new account. The default value is `100`. | integer  
$flow.max_dob_retry_count | Specifies the number of retries allowed when collecting a valid date of birth. The default value is `2`. | integer  
$flow.max_retry_account_type | Specifies the number of retries allowed when collecting the type of account the user would like to open. The default value is `2`. | integer  
$flow.max_retry_another_account | Specifies the number of retries allowed when the user wants to change the type of account they have selected. The default value is `2`. | integer  
  
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

### Telephone verification

The `prebuilt_components_open_account:telephone_verification` webhook is used by the component to get information about registered accounts and previous application(s) associated with the user's telephone number.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
account_count | The number of accounts associated with the registered telephone number. These accounts include self-accounts and accounts for which the user has power of attorney. If there are no accounts associated with the given telephone number, this value is `null`. | integer  
user_first_name | The registered user's first name. If the telephone number is not associated with a registered account, this value is `null`. | string  
user_last_name | The registered user's last name. If the telephone number is not associated with a registered account, this value is `null`. | string  
user_dob | The registered user's date of birth in "YYYY-MM-DD" format. If the telephone number is not associated with a registered account, this value is `null`. | string  
application_count | The number of applications associated with the registered telephone number. If there are no applications associated with the given telephone number, this value is `null`. | integer  
application_id | List containing the application ID of each application associated with the given telephone number, for example `["00000", "11111", "22222"]`. Each element in this list represents the same application as the element with the same index in `account_type` and `application_status`. If there are no applications associated with the given telephone number, this value is `null`. | List (string)  
account_type | List containing the [account type](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account#account-types) of each application associated with the given telephone number, for example `["savings", "checking", "demat"]`. Each element in this list represents the same application as the element with the same index in `application_id` and `application_status`. If there are no applications associated with the given telephone number, this value is `null`. | List (string)  
application_status | List containing the status of each application associated with the given telephone number, for example `["in progress", "on hold", "completed"]`. Each element in this list represents the same application as the element with the same index in `application_id` and `account_type`. If there are no applications associated with the given telephone number, this value is `null`. | List (string)  
  
####  To configure the Telephone verification webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_open_account:telephone_verification webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Generate application

The `prebuilt_components_open_account:generate_application` webhook is used by the component to generate an application for a new account.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
user_first_name | User's first name. | string  
user_last_name | User's last name. | string  
user_dob | User's date of birth in "YYYY-MM-DD" format. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
application_id | Application ID generated for the new account application. | string  
  
####  To configure the Generate application webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_open_account:generate_application webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Offers and deals  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals)

[ Next Order status  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/order-status)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
