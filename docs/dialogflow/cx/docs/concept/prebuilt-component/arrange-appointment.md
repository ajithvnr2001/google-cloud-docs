---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment/
title: Arrange appointment prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:20.686170+00:00
---

# Arrange appointment prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Arrange appointment prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The arrange appointment [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) allows new and existing customers to book appointments. This component uses a customized version of the [Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component to collect appointment dates, and uses the [Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) and [Zip code collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection) prebuilt components to collect information about the user and appointment location.

## Appointment reasons and types

This component supports several categories of appointment reasons and offers different types of appointments depending on the user's selected reason.

Appointment reason | Available appointment types  
---|---  
Loans | In-person, virtual, phone  
Mortgages | In-person, virtual, phone  
Wealth management | In-person, virtual, phone  
Credit cards | Virtual, phone  
Other | Phone  
  
Appointment categories can be customized by modifying the `prebuilt_components_arrange_appt_reason` custom entity. Available appointment types for each category can be configured by modifying the [input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#input-parameters) for each appointment type.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Existing user books in-person appointment

The agent identifies that the user has been previously authenticated as an existing user. The user gives the reason for their appointment and selects to book an in-person appointment. The agent confirms that the user would like to go to the branch closest to their registered address, and confirms that the user's preferred date and time are available. The agent confirms the time and place and successfully schedules the appointment.

User input | Agent response  
---|---  
| Before scheduling an appointment, we will ask you a few questions. Can you tell us the reason for your appointment?  
I want to talk to someone about wealth management |   
| Are you looking for a phone, video call or in-person appointment at one of our branches?  
I'd like to go in person |   
| Okay, do you want to schedule an appointment in the branch located at 1600 Amphitheatre Pkwy, Mountain View, CA 94043?  
Yes |   
| Please provide your preferred appointment date. Please say your preferred month, followed by day and then year. Remember that our branches are open from Monday to Friday: 9 AM to 5 PM, Saturday: 9 AM to 1 PM.  
| _Agent collects user's preferred appointment date using[Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we are done with collecting your preferred date.  
  
Please provide your preferred time slot.  
10 AM |   
| You have selected 10:00 AM. To proceed further with the selected appointment time, say yes.  
Yes |   
| We will schedule an appointment at bank's address 1600 Amphitheatre Pkwy, Mountain View, CA 94043 on 2023-09-23 at 10:00 AM. Is that correct?  
Yes |   
| Okay, we have scheduled the appointment. Your confirmation number is 818452. Do you want to book another appointment?  
No that's all |   
| Thanks for connecting with us. Have a nice day!  
  
### New customer books multiple appointments

The agent identifies that the user has not been previously authenticated and collects the user's telephone number. The user requests a virtual appointment to discuss loans. The user's first preference for date and time is not available, so the agent offers available time slots to the user. The user selects an available time slot and the appointment is successfully scheduled. The user confirms that they would like to book a second appointment, and the agent successfully schedules a second appointment.

User input | Agent response  
---|---  
| _Agent collects user's telephone number using[Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection) prebuilt component_  
| Great, we are done collecting the telephone number.  
  
Before scheduling an appointment, we will ask you a few questions. Can you tell us the reason for your appointment?  
I want to get a loan |   
| Are you looking for a phone, video call or in-person appointment at one of our branches?  
Virtual appointment is fine |   
| Please provide your preferred appointment date. Please say your preferred month, followed by day and then year. Remember that our branches are open from Monday to Friday: 9 AM to 5 PM, Saturday: 9 AM to 1 PM.  
| _Agent collects user's preferred appointment date using[Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we are done with collecting your preferred date.  
  
Please provide your preferred time slot.  
3:00 would be good for me |   
| You have selected 03:00 PM. To proceed further with the selected appointment time, say yes.  
Yes |   
| We will schedule an appointment with our advisor on 2023-10-03 at 03:00 PM. Is that correct?  
Yes please |   
| Okay, we have scheduled the appointment. Your confirmation number is 754731.  
  
Do you want to book another appointment?  
Yeah |   
| Before scheduling an appointment, we will ask you a few questions. Can you tell us the reason for your appointment?  
I need an appointment for my credit card |   
| Are you looking for a phone or video call appointment with one of our branch representatives?  
Phone |   
| Please provide your preferred appointment date. Please say your preferred month, followed by day and then year. Remember that our branches are open from Monday to Friday: 9 AM to 5 PM, Saturday: 9 AM to 1 PM.  
| _Agent collects user's preferred appointment date using[Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection) prebuilt component_  
| Great, we are done with collecting your preferred date.  
  
Please provide your preferred time slot.  
Does 8 AM work? |   
| You have selected 08:00 AM. To proceed further with the selected appointment time, say yes.  
Yes |   
| Sorry, the selected time slot is not available. We have availability for 11:30 AM, 12:30 PM, 01:30 PM, and 03:00 PM on 2023-10-06. Would you like to change the time slot or schedule an appointment on a different date?  
Ok let's do 1:30 then |   
| You have selected 01:30 PM. To proceed further with the selected appointment time, say yes.  
Yes |   
| We will schedule an appointment with our advisor on 2023-10-06 at 01:30 PM. Is that correct?  
Yep |   
| Okay, we have scheduled the appointment. Your confirmation number is 714637.  
  
Do you want to book another appointment?  
No that's it |   
| Thanks for connecting with us. Have a nice day!  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Arrange Appointment  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_arrange_appt_change_date_slot  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_arrange_appt_reason  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_arrange_appointment:submit_appointment  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$session.params.auth_level | (optional) Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
$flow.all_appointment_type | Specifies the list of [appointment reasons](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#reasons-and-types) for which all types of appointments are available. The default value is `["loans", "wealth"]`. | List (string)  
$flow.video_phone_appointment_type | Specifies the list of [appointment reasons](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#reasons-and-types) for which all types of appointments are available. The default value is `["cards"]`. | List (string)  
$flow.appointment_services | Specifies the list of [appointment types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#reasons-and-types) for which branch location is not required and will not be collected from the user. The default value is `["video", "phone"]`. | List (string)  
$flow.working_hours | Specifies the opening hours of the branch, for example `"Monday to Friday: 9 AM to 5 PM, Saturday: 9 AM to 1 PM"`. | string  
$session.params.arrange_appointment_max_days | Specifies the maximum number of days after the current date allowed for an appointment booking. By default, this value is `90`, indicating that appointment dates may be booked no more than 90 days after the current date. This parameter is set in the start page `true` route. | integer  
flow.max_retry_count | Specifies the number of retries allowed when collecting information from the user. The default value is `3`. | integer  
  
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

### Get account

The `prebuilt_components_arrange_appointment:get_account` webhook is used by the component to get account details for a provided phone number, if a registered account exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
account_count | Number of accounts associated with the registered phone number. | integer  
cards_count | Number of cards associated with the registered phone number. | integer  
loans_count | Number of loans associated with the registered phone number. | integer  
mortgage_count | Number of mortgages associated with the registered phone number. | integer  
branch_code | Branch code associated with the registered phone number, used to identify a unique branch location. | string  
  
####  To configure the Get account webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_arrange_appointment:get_account webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get branch

The `prebuilt_components_arrange_appointment:get_branch` webhook is used by the component to retrieve information about a branch location given a branch code.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.branch_code | Branch code identifying a unique branch location. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
branch_address | Address of the branch. | string  
  
####  To configure the Get branch webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_arrange_appointment:get_branch webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Available branch

The `prebuilt_components_arrange_appointment:available_branch` webhook is used by the component to get the nearest branch location given a zip code.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.zip_code | Zip code provided by the end-user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
branch_address | Address of the branch. | string  
  
####  To configure the Available branch webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_arrange_appointment:available_branch webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get available slots

The `prebuilt_components_arrange_appointment:get_available_slots` webhook is used by the component to check available time slots for a user's preferred date and appointment type.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.preferred_date | Preferred date for the appointment provided by the end-user in "YYYY-MM-DD" format. | string  
$flow.appointment_type | The [appointment type](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#reasons-and-types) of the appointment. | string  
$flow.branch_code | Branch code identifying the unique branch location selected by the end-user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
available_slots | List of available appointment times for the specified date, in "HH:MM XM" format, for example `["09:00 AM", "2:30 PM"]`. If there are no available slots this parameter is an empty list `[]`. | List (string)  
  
####  To configure the Get available slots webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_arrange_appointment:get_available_slots webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Submit appointment

The `prebuilt_components_arrange_appointment:submit_appointment` webhook is used by the component to schedule an appointment for the user's selected date, time, branch, appointment reason, and appointment type.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.preferred_date | Preferred date for the appointment provided by the end-user in "YYYY-MM-DD" format. | string  
$flow.preferred_slot | Preferred time for the appointment provided by the end-user in "HH:MM XM" format. | string  
$flow.appointment_reason | The [appointment reason](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#reasons-and-types) for the appointment. | string  
$flow.appointment_type | The [appointment type](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment#reasons-and-types) of the appointment. | string  
$flow.branch_code | Branch code identifying the unique branch location selected by the end-user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
request_number | The request number for the scheduled appointment. | integer  
  
####  To configure the Submit appointment webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_arrange_appointment:submit_appointment webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Alphanumeric collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection)

[ Next Authentication  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
