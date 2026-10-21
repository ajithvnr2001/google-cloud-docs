---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/greeting/
title: Greeting prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:43.274113+00:00
---

# Greeting prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/greeting/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Greeting prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The greeting [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) retrieves the caller's phone number ([ANI](https://en.wikipedia.org/wiki/Automatic_number_identification)), if available. If the phone number is retrieved, the component does a soft-authentication using the phone number, validating it against registered phone numbers. The agent then greets the end-user with a personalized message based on their account information.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * The component assumes that the customer phone numbers are maintained in a CRM (Customer Relationship Management) system or other service.
  * Existing customers using an alternate phone number to contact will not be authenticated by this component.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Authenticated end-user

End-user is identified based on the calling number and receives a personalized greeting message.

User input | Agent response  
---|---  
| Hi [Caller First Name]. Thank you for contacting [Company Name], we are committed to your financial health. How may we assist you today?  
  
### Unidentified end-user

End-user's calling number is not identified and end-user is greeted with the standard greeting message.

User input | Agent response  
---|---  
| Thank you for contacting [Company Name], we are committed to your financial health. How may we assist you today?  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Greeting  
Parameter | [param_name] | ani_auth  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_greeting:get_account_details  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$flow.company_name | Captures the name of the company which will be used dynamically in the Greeting prompt. | string  
  
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
ani_auth | This parameter captures the result of ANI based authentication. By default, the value is false. | boolean  
auth_level | Indicates the authentication level of the caller. By default, the value is null. -1 indicates that the user was not authenticated by their ANI. 0 indicates that the ANI authentication was a success. | integer  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. Configure the provided [flexible webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with your external services, see Webhook setup below.



## Webhook setup

In order to use this component, you will need to configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Get account details

The `prebuilt_components_greeting:get_account_details` webhook is used by the component to identify the caller using their ANI. If the phone number of the caller exists in the configured external service, then the relevant information to personalize the experience is retrieved, including caller name and email.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Output Format  
---|---|---  
phone_number | Caller's phone number (ANI) | integer  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
user_first_name | End-user's first name, used to provide a personalized greeting. | string  
  
####  To configure the Get Account Details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_greeting:get_account_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhook should now be set up and ready to test.

[ Previous arrow_back  Financial services steering  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/financial-services-steering)

[ Next Lock card  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lock-card)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
