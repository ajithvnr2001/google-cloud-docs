---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/order-status/
title: Order status prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:58.311915+00:00
---

# Order status prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/order-status/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Order status prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The order status [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a customer's authentication level, then provides information about the user's most recent or past orders to an authenticated customer. This component uses the [Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) prebuilt component to authenticate users. The component also uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) for post-call summarization.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Recent order

End-user calls from an unregistered number; the agent authenticates the user, then provides detailed information about the shipments in the order. The user confirms that they would like an SMS sent to their registered phone number with additional details.

User input | Agent response  
---|---  
| _Agent authenticates user using[Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) prebuilt component_  
| Okay, John. Are you calling about your most recent order for John Doe containing lamp, shirt and 10 other items placed on 2023-11-10 at 06:00 PM?  
Yes |   
| Your order has 2 shipments, which will be delivered by 2024-01-15.  
  
Would you like to hear more about these shipments?  
Yes |   
| Shipment 1 containing jeans, belt and 2 other items is in-transit and will be delivered by 2024-01-12.  
  
Shipment 2 containing lamp, shirt and 6 other items was delivered on 2023-11-12.  
  
Would you like to receive an SMS with further details on your items?  
Yes |   
| We have sent you an SMS with a link to track the status of all your shipments. Thank you for calling us.  
  
### Duplicate orders

End-user has been previously authenticated. The user requests information about an order and provides the last five digits of the order. The agent identifies that multiple orders placed by this user share the same last five digits, so it confirms which order the user would like to hear the status of and provides the order status to the user.

User input | Agent response  
---|---  
| Okay, Amber. Are you calling about your most recent order for Amber Doe containing lamp, shirt and other 2 items placed on 2023-11-10 at 06:00 PM?  
No |   
| Could you please provide the last 5 digits of your order ID that you want to track?  
12355 |   
| The last five digits of the order ID that we got are 12355, is that correct?  
Yes that's right |   
| Great, we are done collecting the order ID.  
| As per our records, we have found 2 orders ending with the same 5 digits 12355. Which order are you looking for?  
  
Order number 1 which was placed on 2023-11-10 at 06:00 PM or Order number 2 which was placed on 2023-11-09 at 08:00 PM?  
  
To select order number one say 1, to select order number two, say 2. Else say No.  
Order one |   
| Your order has 2 shipments, which will be delivered by 2024-01-15.  
  
Would you like to hear more about these shipments?  
Yes |   
| Shipment 1 containing jeans is in-transit and will be delivered by 2024-01-15.  
  
Shipment 2 containing lamp, shirt and 1 other items is cancelled.  
  
Would you like to receive an SMS with further details on your items?  
No that's all |   
| Thank you for calling us.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Order Status  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_order_status:get_order_details  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | (optional) User's local phone number, without the country code, used to identify the user. | string  
$session.params.all_recent_order_id | (optional) This parameter lists order IDs associated with the authenticated user, sorted by the order placement date in descending order. The first element of the array represents the most recent order. If a user has no orders, the value of this parameter is `null`. | List (string)  
$session.params.email | (optional) The email registered with the account. | string  
$session.params.user_first_name | (optional) User's first name, used to greet and confirm ownership of the account. | string  
$flow.max_shipment | Specifies the number of shipments displayed to the user at a time. The default value is `2`. | integer  
$flow.tracking_status_delivered | Specifies the value returned by the webhook indicating a delivered order status. The default value is `"delivered"`. | string  
$flow.tracking_status_cancelled | Specifies the value returned by the webhook indicating a cancelled order status. The default value is `"cancelled"`. | string  
$flow.tracking_status_returned | Specifies the value returned by the webhook indicating a returned order status. The default value is `"returned"`. | string  
$flow.tracking_status_partially_returned | Specifies the value returned by the webhook indicating a partially returned order status. The default value is `"partially returned"`. | string  
$flow.max_retry_alternate_profile | Specifies the number of retries allowed when requesting order status from an unregistered phone number or alternate profile. The default value is `3`. | integer  
$flow.max_retry_order_number | Specifies the number of retries allowed when providing an order number. The default value is `3`. | integer  
$flow.max_retry_another_order_id | Specifies the number of retries allowed after providing an invalid order number. The default value is `3`. | integer  
  
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
all_recent_order_id | This parameter lists order IDs associated with the authenticated user, sorted by the order placement date in descending order. The first element of the array represents the most recent order. If a user has no orders, the value of this parameter is `null`. | List (string)  
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
  2. Configure the provided [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with configuration describing your external services, see Webhook setup.



## Webhook setup

In order to use this component, you will need to configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Authentication

If you have not previously configured external services required for authentication, you will need to configure them to enable authentication of users for this component. See [Retail authentication webhook setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail#webhook-setup) for detailed instructions.

### Get order details

The `prebuilt_components_order_status:get_order_details` webhook is used by the component to retrieve order details for a specified order.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.order_id | Order ID to retrieve details for. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
order_date | Date the order was placed, in `YYYY-MM-DD` format. | string  
order_time | Time the order was placed, in `HH:MM` format. | string  
order_status | Indicates status for the order. Example values include `"pending"`, `"processing"`, `"in-transit"`, `"on-hold"`, `"cancelled"`, `"delivered"`, `"returned"`, `"partially returned"`. | string  
order_product_name | List of product names within the order. | List (string)  
order_product_quantity | Total count of the number of products ordered for each product within an order. | integer  
order_product_count | The number of unique products within an order. | integer  
order_status_notification | Indicates whether notifications are enabled for this order. | boolean  
return_eligibility_date | List of dates until which each product within the order is eligible for return, in `YYYY-MM-DD` format. | List (string)  
order_customer_billing_name | First name of the customer's billing name for the order. | string  
order_latest_delivery_date | The latest delivery date across all estimated delivery dates for the shipments within the order, in `YYYY-MM-DD` format. | string  
order_shipment_multiple | Indicates whether the order contains multiple shipments. | boolean  
order_shipment_count | The number of shipments within the order. | integer  
order_shipment_product_count | Total product count in each shipment within the order. | List (integer)  
order_shipment_product_name | List of the product names in each shipment within the order. | List (string)  
order_estimated_delivery_date | List of estimated delivery dates for each shipment within the order, in `YYYY-MM-DD` format. | List (string)  
order_shipment_status | List indicating the status for each shipment within the order. Example values include `"pending"`, `"processing"`, `"in-transit"`, `"on-hold"`, `"cancelled"`, `"delivered"`, `"returned"`, `"partially returned"`. | List (string)  
  
####  To configure the Get order details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_order_status:get_order_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get duplicate orders

The `prebuilt_components_retail_services:get_duplicate_order` webhook is used by the component to retrieve detailed information in order to distinguish between orders when multiple order numbers have the same last five digits.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.duplicate_order_id | List containing the last five digits of order numbers shared between one or more orders for the user. | List (string)  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
all_order_date | List of order dates for duplicate orders with the specified last five digits in `YYYY-MM-DD` format. Each element in this array corresponds to the same element in the `all_order_time` array. | boolean  
all_order_time | List of order times for duplicate orders with the specified last five digits in `HH:MM` format. Each element in this array corresponds to the same element in the `all_order_date` array. | number  
  
####  To configure the Get duplicate orders webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_retail_services:get_duplicate_order webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send SMS

The `prebuilt_components_order_status:send_sms` webhook is used by the component to send order details to the specified phone number using SMS.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to send order details for. | string  
  
####  To configure the Send SMS webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_order_status:send_sms webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Enable notifications

The `prebuilt_components_order_status:enable_notification` webhook is used by the component to enable notifications for a user's registered phone number.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_notification | Indicates whether notifications should be enabled for the user. | boolean  
  
####  To configure the Enable notifications webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_order_status:enable_notification webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Open account  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account)

[ Next Return and refund  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
