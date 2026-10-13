---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/feedback/
title: Feedback prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:43.340793+00:00
---

# Feedback prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/feedback/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Feedback prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The feedback [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) collects quantitative and qualitative feedback from the end-user.

The component first performs a lookup using the configured Check last feedback webhook to check whether recent feedback was provided by that particular end-user. If no recent feedback exists, the component asks the user to provide a quantitative feedback score between one and five. If the feedback is negative, the component can optionally collect freeform qualitative feedback from the user.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * The component assumes that the customer phone numbers are maintained in a CRM (Customer Relationship Management) system or other service.
  * Existing customers using an alternate phone number to contact will not be authenticated by this component.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Positive feedback

The response from the Check last feedback webhook indicates that the end-user has not provided feedback recently. Agent requests user's feedback score, and the user provides a score indicating a positive experience.

User input | Agent response  
---|---  
| Thank you for calling. Your feedback is important to us. Please take a moment to share your opinion of the service you received today by answering a few short questions.  
On a scale of 1 to 5, where 1 is most unsatisfied and 5 is most satisfied, how satisfied are you with the service you received today?  
5 |   
| Great, thank you for your positive feedback.  
  
### Negative feedback

The response from the Check last feedback webhook indicates that the end-user has not provided feedback recently. Agent requests user's feedback score, and the user provides a score indicating a negative experience. The agent then requests qualitative feedback from the user.

User input | Agent response  
---|---  
| Thank you for calling. Your feedback is important to us. Please take a moment to share your opinion of the service you received today by answering a few short questions.  
On a scale of 1 to 5, where 1 is most unsatisfied and 5 is most satisfied, how satisfied are you with the service you received today?  
2 |   
| Please tell us how we can improve this experience for you.  
Some of my questions weren't answered completely. |   
| Thanks for your feedback. We apologize for the inconvenience caused to you and strive to give you a better experience next time.  
  
### Recent feedback

The response from the Check last feedback webhook indicates that the end-user has provided feedback recently, so the agent does not ask the user for further input.

User input | Agent response  
---|---  
| Thank you for reaching out to us.  
  
### Invalid input

The response from the Check last feedback webhook indicates that the end-user has not provided feedback recently. Agent requests user's feedback score, and the user provides invalid input multiple times. The component ends the flow with failure.

User input | Agent response  
---|---  
| Thank you for calling. Your feedback is important to us. Please take a moment to share your opinion of the service you received today by answering a few short questions.  
On a scale of 1 to 5, where 1 is most unsatisfied and 5 is most satisfied, how satisfied are you with the service you received today?  
-1 |   
| Sorry, we didn't get that. Please tell us a feedback score that is 1, 2, 3, 4, or 5.  
100 |   
| Sorry, we didn't get that. Please tell us a feedback score that is 1, 2, 3, 4, or 5.  
Nice |   
| We're sorry, but the maximum number of retries has been exceeded. Please try again after some time.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Feedback  
Parameter | [param_name] | feedback_score  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_feedback:last_feedback_check  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, which is used to identify the user in API requests. The phone number should not include the country code. | string  
$flow.minimum_feedback_score | This parameter indicates the threshold for what is considered a negative or positive feedback score. A low score (equal to or less than this parameter's value) indicates a negative experience and a high score (greater than this parameter's value) indicates a positive experience. If a low score is provided by the end-user, qualitative feedback is be requested from the user, asking them how the experience can be improved. The default value for this parameter is `3`. | integer  
$flow.feedback_max_retry_count | This is a configurable parameter that captures the maximum number of retries that are provided to a user. The value assigned to this parameter should be one less than the number of the tries available. The default value is `2`, which means that the caller gets three tries to provide the requested information. | integer  
  
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
feedback_score | This parameter captures the feedback score provided by the end-user. Valid values are integers between one and five, inclusive. | integer  
feedback_comment | This parameter captures the qualitative comments provided by the end-user, if any. | string  
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
  2. Configure the provided [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with your external services, see Webhook setup below.



## Webhook setup

In order to use this component, you will need to configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Check last feedback

The `prebuilt_components_feedback:last_feedback_check` webhook is used by the component to check whether a user has provided feedback recently. The time period during which previously-provided feedback is considered recent is defined by the external service integrated with this webhook, which can be configured by the service's owner.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
phone_number | User's local phone number, without the country code, used to identify the user. | integer  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
last_feedback_time_elapsed | Indicates whether feedback has been provided by the user recently. `true` indicates a period of time has elapsed since the user last gave feedback and that no recent feedback was found. `false` indicates that feedback was provided recently, and not enough time has elapsed since the user last gave feedback. | boolean  
  
####  To configure the Check last feedback webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_feedback:last_feedback_check webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Update feedback

The `prebuilt_components_feedback:update_feedback` webhook is used by the component to send collected feedback to an external service.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
phone_number | User's local phone number, without the country code, used to identify the user. | string  
feedback_score | This parameter stores the feedback score provided by the end-user. Expected values are integers between one and five, inclusive. | integer  
feedback_comment | This parameter stores the qualitative feedback comment provided by the end-user. | string  
  
####  To configure the Update feedback webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_feedback:update_feedback webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Exchange order  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order)

[ Next Fraud and dispute (Retail)  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/fraud-and-dispute-retail)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
