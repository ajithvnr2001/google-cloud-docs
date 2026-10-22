---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order/
title: Cancel order prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:17.065627+00:00
---

# Cancel order prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Cancel order prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The cancel order [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a user's authentication level. Once the user has been authenticated, the component provides information about the user's most recent or past orders. The user may then choose to cancel an entire order or cancel specific items in an order. This component uses the [Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) prebuilt component to authenticate users. The component also uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) for post-call summarization.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Cancel single product in recent order

End-user has been previously authenticated. The agent confirms which items from the most recent order should be cancelled. The agent checks the original method of payment and confirms the cancellation details with the user.

User input | Agent response  
---|---  
| Are you calling about your most recent order number ending with 12978 containing 5 water bottle and 1 t-shirt placed on 2023-11-09 at 08:00 PM?  
yes |   
| We've found some eligible products in your order. Please tell us which product you would like to cancel.  
Product 1: google water bottle, Product 2: google t-shirt.  
  
Please say or enter the product number of the item you want to select, or say "next" to show more products.  
next |   
| We didn't find any other items in our records. Please choose from the shared list.  
Product 1: google water bottle, Product 2: google t-shirt.  
  
Please say or enter the product number of the item you want to select, or say "next" to show more products.  
1 |   
| To verify, you are interested in canceling the google water bottle. Is this correct?  
yes |   
| We can see that the available quantity of the product that you have selected is 5. Please specify the quantity of products you wish to cancel.  
4 |   
| Please specify the reason for the cancellation. You may say something like: changed my mind, no longer needed, I would like to buy another item, delayed delivery, bought by mistake, want to change payment method, or say others.  
I would like to buy another item |   
| Thank you for letting us know.  
  
Would you like to cancel another product?  
no |   
| For purchases made using your wallet, refunds are credited to the wallet or store credit account. It will take 3 to 5 business days for your refund to appear in your account. Please note that the refund amount will exclude shipping and handling charges.  
  
### Cancel entire order

End-user has been previously authenticated. The agent confirms that the user wants to cancel a specific order, then collects the cancellation reason. The agent checks the original method of payment and confirms the cancellation details with the user.

User input | Agent response  
---|---  
| Are you calling about your most recent order number ending with 12345 containing 1 shirt placed on 2023-11-10 at 06:00 PM?  
no |   
| Would you like to cancel another order?  
yes |   
| Could you please provide the last 5 digits of your order ID that you want to track?  
12346 |   
| The last five digits of the order ID that we got are 12346, is that correct?  
yes |   
| Great, we are done collecting the order ID.  
  
Do you wish to cancel the entire order?  
yes |   
| Please specify the reason for the cancellation. You may say something like: changed my mind, no longer needed, I would like to buy another item, delayed delivery, bought by mistake, want to change payment method, or say others.  
no longer needed |   
| Thank you for letting us know.  
  
Your cancellation request has been generated.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Cancel Order  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_product_cancel_reason  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_cancel_order:post_cancellation_details  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | (optional) User's local phone number, without the country code, used to identify the user. | string  
$session.params.all_recent_order_id | (optional) This parameter lists order IDs associated with the authenticated user, sorted by the order placement date in descending order. The first element of the array represents the most recent order. If a user has no orders, the value of this parameter is `null`. | List (string)  
$session.params.email | (optional) The email registered with the account. | string  
$session.params.user_first_name | (optional) User's first name, used to greet and confirm ownership of the account. | string  
  
This prebuilt component allows the following optional parameters to configure the behavior of the component, including retries.

Parameter Name | Description | Format  
---|---|---  
$flow.max_retry_another_account_counter | Specifies the number of retries allowed when selecting whether to continue with an alternate account. The default value is `2`. | integer  
$flow.max_retry_order_number | Specifies the number of retries allowed when providing the last five digits of an order number. The default value is `2`. | integer  
$flow.max_retry_another_order | Specifies the number of retries allowed when selecting another order in cases where the order ID is not found or the order is not eligible for cancellation. The default value is `2`. | integer  
$flow.max_retry_select_order_number | Specifies the number of retries allowed when providing the full order number in cases where multiple orders share the same last five digits. The default value is `2`. | integer  
$flow.max_product_display_counter | Specifies the maximum number of products to present in a single turn. The default value is `2`. | integer  
$flow.max_product_display | Specifies the maximum number of products to present over the entire conversation. The default value is `9`. | integer  
$flow.max_retry_product_number_counter | Specifies the maximum number of retries allowed when selecting a product to cancel. The default value is `2`. | integer  
$flow.max_product_cancel_confirm_counter | Specifies the maximum number of retries allowed when confirming the selected product. The default value is `2`. | integer  
$flow.max_retry_select_quantity | Specifies the maximum number of retries allowed when selecting the quantity of product to cancel. The default value is `2`. | integer  
$flow.order_product_cancel_reason_others | Specifies the value of the `prebuilt_components_product_cancel_reason` entity indicating that the user has selected "others" cancel reason. The default value is `"others"`. | string  
$flow.max_retry_cancel_reason | Specifies the number of retries allowed when confirming the reason for cancel. The default value is `2`. | integer  
$flow.order_payment_mode_COD | Specifies the value of the `order_payment_mode` field returned by the `get_order_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order#webhook-setup) indicating a cash on delivery (COD) payment method. The default value is `"COD"`. | string  
$flow.order_payment_mode_store_credit | Specifies the value of the `order_payment_mode` field returned by the `get_order_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order#webhook-setup) indicating a store credit payment method. The default value is `"store_credit"`. | string  
  
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
  
## Generators

This component uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) to enable specific parts of the conversation.

### Summarization

The `Summarization` generator is used to generate a post-call summary describing the conversation handled by the component.

## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. Configure the provided [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with configuration describing your external services, see Webhook setup.



## Webhook setup

In order to use this component, you will need to configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Authentication

If you have not previously configured external services required for authentication, you will need to configure them to enable authentication of users for this component. See [Retail authentication webhook setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail#webhook-setup) for detailed instructions.

### Get order details

The `prebuilt_components_cancel_order:get_order_details` webhook is used by the component to retrieve order details for a specified order.

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
order_product_count | The number of unique products within an order. | integer  
order_payment_mode | Indicates the payment mode used when placing the order. | string  
cancelable_product_id | List of product IDs for cancelable products within the order. | List (string)  
cancelable_product_name | List of product names for cancelable products within the order. | List (string)  
cancelable_product_brand_name | List of brand names for cancelable products within the order. | List (string)  
cancelable_product_quantity | List of quantities for cancelable products within the order. | List (string)  
  
####  To configure the Get order details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_cancel_order:get_order_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get duplicate order details

The `prebuilt_components_retail_services:get_duplicate_order_details` webhook is used by the component to retrieve detailed information in order to distinguish between orders when multiple order numbers have the same last five digits.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.duplicate_order_id | List containing the last five digits of order numbers shared between one or more orders for the user. | List (string)  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
all_order_date | List of order dates for duplicate orders with the specified last five digits in `YYYY-MM-DD` format. Each element in this array corresponds to the same element in the `all_order_time` array. | List (string)  
all_order_time | List of order times for duplicate orders with the specified last five digits in `HH:MM` format. Each element in this array corresponds to the same element in the `all_order_date` array. | List (string)  
  
####  To configure the Get duplicate order details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_retail_services:get_duplicate_order_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Post cancellation details

The `prebuilt_components_cancel_order:post_cancellation_details` webhook is used by the component to submit a cancellation request.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to submit a ticket for. | string  
$flow.cancel_product_id_list | List of product IDs that the user wants to cancel. | List (string)  
$flow.cancel_product_quantity_list | List of product quantities that the user wants to cancel, corresponding to each element in `$flow.cancel_product_id_list`. | List (string)  
$flow.cancel_reason_list | List of cancel reasons for each cancelled product, corresponding to each element in `$flow.cancel_product_id_list`. | List (string)  
$flow.order_refund_mode | The payment mode for refund. Valid values are defined by the `prebuilt_components_cancel_mode_of_refund` entity. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
order_cancellation_ticket_id | Ticket ID for the submitted cancellation. | string  
  
####  To configure the Post cancellation details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_cancel_order:post_cancellation_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Authentication (Retail)  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail)

[ Next Credit card CVV collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
