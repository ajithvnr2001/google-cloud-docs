---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund/
title: Return and refund prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:45.072460+00:00
---

# Return and refund prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Return and refund prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The return and refund [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a user's authentication level. Once the user has been authenticated, the component provides information about the user's most recent or past orders. The user may then choose to return multiple items in an order and select options including refund and return methods. This component uses the [Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) prebuilt component to authenticate users. The component also uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) for post-call summarization and FAQs.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Store return for a single product

End-user has been previously authenticated. The agent confirms which items from the most recent order should be returned and collects the reason for return. The user selects to return the items at a store, and the agent provides a list of the nearest stores. The user selects a store, and the agent generates a shipping label that is sent to the user's registered channels.

User input | Agent response  
---|---  
| Are you calling about your most recent order number ending with 12345 containing 2 lamp placed on 2023-11-10?  
yes |   
| To confirm, you are interested in returning the Google lamp. Is this correct?  
yes |   
| We can see that the available quantity of the product that you have selected is 2. Please specify the quantity of products you wish to return.  
two |   
| Please specify the reason for return. You may say something like: item defective or doesn't work, no longer needed, size or fit issue, wrong item was sent, item arrived too late, bought by mistake or say others.  
others |   
| Please state the reason for your return.  
poor quality |   
| To verify, the reason for return is poor quality. Is this correct?  
yes |   
| Please let us know where you would like to receive your refund. You can say something like store credit or source account.  
source account |   
| Thank you for verifying that you would like your refund to be returned to the original payment method.  
  
As a last step, how would you like to return the product? You can say something like: Return at store or Drop off at location or Schedule for pickup.  
return at store |   
| Let's find a store near you.  
| _Agent collects zip code using[Zip code collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection) prebuilt component_  
| Here is the list of locations near the zip code you entered.  
Address 1: Google Texas, 500 W 2nd St, Suite 2900 Austin, Texas 78701, US.  
Address 2: Google California, 19510 Jamboree Road, Irvine, California 92612, US.  
  
Please say or enter the address number that you want to select, or say "next" to show more store addresses.  
1 |   
| To confirm, you have selected Google Texas, 500 W 2nd St, Suite 2900 Austin, Texas 78701, US. Is that correct?  
yes |   
| Perfect. We have sent a shipping label and ticket number to your registered phone number and email. Please print it out and attach it to your package and drop your return off within 30 days.  
Once we receive the item at our warehouse, it will take 3 to 5 business days for your refund to appear in your account. Please note: The refund amount will be excluding the shipping and handling charges.  
Thank you for calling.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Return & Refund  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_return_refund_mode_of_return  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_return_refund:post_return_details  
  
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
$flow.max_retry_order_number | Specifies the number of retries allowed when providing the last five digits of an order number. The default value is `3`. | integer  
$flow.max_retry_another_order | Specifies the number of retries allowed when selecting another order for return in cases where the order ID is not found or the order is not eligible for return. The default value is `2`. | integer  
$flow.max_retry_select_order_number | Specifies the number of retries allowed when providing the full order number in cases where multiple orders share the same last five digits. The default value is `2`. | integer  
$flow.max_product_display_counter | Specifies the maximum number of products to present in a single turn. The default value is `2`. | integer  
$flow.max_product_display | Specifies the maximum number of products to present over the entire conversation. The default value is `9`. | integer  
$flow.max_retry_product_number_counter | Specifies the maximum number of retries allowed when selecting a product to return. The default value is `2`. | integer  
$flow.max_product_return_confirm_counter | Specifies the maximum number of retries allowed when confirming the selected product. The default value is `2`. | integer  
$flow.max_retry_return_reason_counter | Specifies the number of retries allowed when confirming the reason for return. The default value is `2`. | integer  
$flow.order_product_return_reason_others | Specifies the value of the `prebuilt_components_return_refund_reason` entity indicating that the user has selected "others" return reason. The default value is `"others"`. | string  
$flow.max_retry_select_quantity | Specifies the maximum number of retries allowed when selecting the quantity of product to return. The default value is `2`. | integer  
$flow.max_store_display_counter | Specifies the maximum number of stores to present in a single turn. The default value is `1`. | integer  
$flow.max_store_display | Specifies the maximum number of stores to present over the entire conversation. The default value is `10`. | integer  
$flow.max_retry_store_number_counter | Specifies the maximum number of retries allowed when selecting a store. The default value is `2`. | integer  
$flow.max_retry_store_selection | Specifies the number of retries allowed when confirming the store selection. The default value is `2`. | integer  
$flow.max_retry_another_zip_code | Specifies the maximum number of retries allowed when providing a zip code. The default value is `2`. | integer  
$flow.order_payment_mode_COD | Specifies the value of the `order_payment_mode` field returned by the `get_order_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund#webhook-setup) indicating a cash on delivery (COD) payment method. The default value is `"COD"`. | string  
$flow.order_payment_mode_store_credit | Specifies the value of the `order_payment_mode` field returned by the `get_order_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund#webhook-setup) indicating a store credit payment method. The default value is `"store_credit"`. | string  
$flow.order_refund_mode_source_account | Specifies the value of the `prebuilt_components_return_refund_mode_of_refund` entity indicating that the user selected to refund to their source account. The default value is `source_account`. | string  
$flow.order_return_location_scheduled_for_pickup | Specifies the value of the `prebuilt_components_exchange_order_location` entity indicating that the user selected to schedule a pickup for the return. The default value is `scheduled_for_pickup`. | string  
  
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

### FAQ

The `FAQ` generator is used to handle frequently-asked questions about returns and exchanges, including:

  * _Is there a deadline for the return process?_
  * _Can I exchange a gift item?_
  * _The product price and the refund amount is different. Why is that?_



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

The `prebuilt_components_return_refund:get_order_details` webhook is used by the component to retrieve order details for a specified order.

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
order_product_count | The number of unique products within an order. | integer  
order_payment_mode | Indicates the payment mode used when placing the order. | string  
returnable_product_id | List of product IDs for returnable products within the order. | List (string)  
returnable_product_name | List of product names for returnable products within the order. | List (string)  
returnable_product_brand_name | List of brand names for returnable products within the order. | List (string)  
returnable_product_quantity | List of quantities for returnable products within the order. | List (string)  
  
####  To configure the Get order details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_return_refund:get_order_details webhook. 
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



### Get store details

The `prebuilt_components_return_refund:get_store_details` webhook is used by the component to retrieve the list of stores near the user's provided zip code.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.zip_code | Zip code to search for nearby stores. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
store_id | List of store IDs. | List (string)  
store_address | List of store addresses corresponding to each element of `store_id`. | List (string)  
  
####  To configure the Get store details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_return_refund:get_store_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Post return details

The `prebuilt_components_return_refund:post_return_details` webhook is used by the component to submit a return.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to submit a ticket for. | string  
$flow.return_product_id_list | List of product IDs that the user wants to return. | List (string)  
$flow.return_product_quantity_list | List of product quantities that the user wants to return, corresponding to each element in `$flow.return_product_id_list`. | List (string)  
$flow.return_reason_list | List of return reasons for each returned product, corresponding to each element in `$flow.return_product_id_list`. | List (string)  
$flow.order_return_location | The selected mode for the return. Valid values are defined by the `prebuilt_components_exchange_order_location` entity. | string  
$flow.order_return_store_id | The store ID for the store selected by the user for a store return. | string  
$flow.order_refund_mode | The payment mode for refund. Valid values are defined by the `prebuilt_components_return_refund_mode_of_return` entity. If no refund is required, this value is `null`. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
order_return_ticket_id | Ticket ID for the submitted return. | string  
  
####  To configure the Post return details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_return_refund:post_return_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send COD refund information

The `prebuilt_components_return_refund:send_COD_refund_information` webhook is used by the component to send return-related payment information to a user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to submit a ticket for. | string  
$flow.channel | The specific channel to send information to. Valid values are defined by the `prebuilt_components_channel_email_phone` entity. By default `phone` and `email` are supported. | string  
  
####  To configure the Send COD refund information webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_return_refund:send_COD_refund_information webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Order status  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/order-status)

[ Next Telecommunications steering  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telecommunications-steering)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
