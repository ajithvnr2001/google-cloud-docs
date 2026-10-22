---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order/
title: Exchange order prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:33.253706+00:00
---

# Exchange order prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Exchange order prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The exchange order [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a user's authentication level. Once the user has been authenticated, the component provides information about the user's most recent or past orders. The user may then choose to exchange multiple items in an order and select options including refund and shipping methods. This component uses the [Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) prebuilt component to authenticate users. The component also uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) for post-call summarization and FAQs.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Store exchange for defective item

End-user has been previously authenticated. The agent confirms which items from the most recent order should be exchanged and collects the reason for exchange. The user selects to exchange the items at a store, and the agent provides a list of the nearest stores. The user selects a store, and the agent generates a shipping label that is sent to the user's registered channels.

User input | Agent response  
---|---  
| Are you calling about your most recent order number ending with 12375 containing 2 lamp, 2 Pixel, and 10 other products placed on 2023-11-10?  
yes |   
| We've found some eligible products in your order. Please tell us which product you would like to exchange. Product 1: Google lamp, Product 2: Google Pixel, Product 3: Google LED light.  
  
Please say or enter the product number of the item you want to select, or else say next to show more products.  
1 |   
| To confirm, you are interested in exchanging the Google lamp. Is this correct?  
yes |   
| We can see that the available quantity of the product that you have selected is 2. Please specify the quantity of products you wish to exchange.  
Two |   
| Please specify the reason for the exchange. You may say something like: Item defective or doesn't work, size or fit issue, incomplete order issue, style issue, incorrect color or else say others.  
Item defective |   
| Thank you for letting us know.  
  
As a last step, how would you like to exchange the product? You can say something like: Exchange at a store or Schedule for pickup.  
I want to exchange at a store |   
| Let's find a store near you.  
| _Agent collects zip code using[Zip code collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection) prebuilt component_  
| Here is the list of locations near the zip code you entered.  
Address 1: Google Texas, 500 W 2nd St, Suite 2900 Austin, Texas 78701, US.  
Address 2: Google California, 19510 Jamboree Road, Irvine, California 92612, US.  
  
Please say or enter the address number that you want to select, or say "next" to show more store addresses.  
The first store |   
| To confirm, you have selected Google Texas, 500 W 2nd St, Suite 2900 Austin, Texas 78701, US. Is that correct?  
yes |   
| Perfect. We have sent a shipping label and ticket number to your registered phone number and email. Please print it out and attach it to your package and drop your exchange off within 30 days. Once we receive the item at our warehouse, it will take 3 to 5 business days for your exchange, if any, to appear in your account. Please note: The refund amount will be excluding the shipping and handling charges.  
  
Your exchange product is of a higher value. The price difference is 20$. You will be receiving the payment link soon on your registered mobile number. Kindly, make the payment within 24 hours to place the exchange.  
  
Would you like to exchange another order?  
no that's it |   
| Thank you for calling.  
  
### Refund for price difference

End-user has been previously authenticated. The agent collects the order number, the product to be exchanged, and collects the reason for exchange. The user opts to exchange the items for a different size, and schedules a pickup. The agent identifies that the exchanged item is lower in price than the new item, and confirms with the user the method of payment for a refund.

User input | Agent response  
---|---  
| Are you calling about your most recent order number ending with 12345 containing 2 lamp placed on 2023-11-10?  
No |   
| Would you like to exchange another order?  
Yes |   
| Could you please provide the last 5 digits of your order ID that you want to exchange?  
12346 |   
| The last five digits of the order ID that we got are 12346, is that correct?  
Yes |   
| Great, we are done collecting the order ID.  
  
We've found some eligible products in your order. Please tell us which product you would like to exchange. Product 1: google water bottle, Product 2: google t-shirt.  
  
Please say or enter the product number of the item you want to select, or else say next to show more products.  
Two |   
| To verify, you are interested in exchanging the google t-shirt for exchange. Is this correct?  
Yes |   
| Please specify the reason for the exchange. You may say something like: Item defective or doesn't work, size or fit issue, incomplete order issue, style issue, incorrect color or else say others.  
Size or fit issue |   
| Thanks for letting us know the reason for exchange. Can you please tell us the size you would like to exchange with? We have the following sizes available:  
Say 1 for small.  
Say 2 for medium.  
Say 3 for large.  
Say 4 for XL.  
Say 5 for double-XL.  
1 |   
| As a last step, how would you like to exchange the product? You can say something like: Exchange at a store or Schedule for pickup.  
Schedule for pickup |   
| Perfect. We have sent a shipping label to your registered phone number and email. Please print it out and attach it to your package. Our team will contact you within the next 24 to 48 hours to schedule a pickup. Once we receive the item at our warehouse, it will take 3 to 5 business days for your exchange refund to appear in your account.  
  
Your exchanged product is of lower value and you are eligible for a refund of 5$.  
Please let us know where you would like to receive your refund. You can say something like store credit or source account.  
Store credit |   
| Thank you for verifying that you would like your refund to be returned to wallet.  
  
Would you like to exchange another order?  
no |   
| Thank you for calling.  
  
### Ineligible order

End-user has been previously authenticated. The agent checks the most recent order and finds there are no eligible products for exchange. The agent collects an order number from the user and finds that the provided order does not have any eligible products.

User input | Agent response  
---|---  
| We didn't find any products in your most recent order eligible for exchange.  
  
Would you like to exchange another order?  
yes |   
| Could you please provide the last 5 digits of your order ID that you want to exchange?  
23487 |   
| The last five digits of the order ID that we got are 23487, is that correct?  
yes |   
| Great, we are done collecting the order ID.  
| Sorry, there are no products in your order that are eligible for exchange based on our policies. You can find more information about our exchange policy on our website.  
  
Would you like to exchange another order?  
no |   
| Thank you for calling.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Order Status  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_exchange_order_location  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_exchange_order:get_product_exchange_availability  
  
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
$flow.max_retry_another_account | Specifies the number of retries allowed when selecting whether to continue with an alternate account. The default value is `3`. | integer  
$flow.max_retry_order_number | Specifies the number of retries allowed when providing the last five digits of an order number. The default value is `3`. | integer  
$flow.max_retry_another_order | Specifies the number of retries allowed when selecting another order for return in cases where the order ID is not found or the order is not eligible for the exchange. The default value is `2`. | integer  
$flow.max_retry_select_order_number | Specifies the number of retries allowed when providing the full order number in cases where more than one order share the same last five digits. The default value is `2`. | integer  
$flow.max_retry_exchange_reason | Specifies the number of retries allowed when providing the reason for exchange. The default value is `3`. | integer  
$flow.max_retry_exchange_reason_counter | Specifies the number of retries allowed when confirming the reason for exchange. The default value is `2`. | integer  
$flow.order_product_exchange_reason_others | Specifies the value of the `prebuilt_components_exchange_order_reason` entity indicating that the user has selected "others" exchange reason. The default value is `"others"`. | string  
$flow.max_product_display_counter | Specifies the maximum number of products to present in a single turn. The default value is `2`. | integer  
$flow.max_product_display | Specifies the maximum number of products to present over the entire conversation. The default value is `9`. | integer  
$flow.max_product_exchange_confirm | Specifies the maximum number of retries allowed when confirming the selected product. The default value is `2`. | integer  
$flow.max_retry_product_number_counter | Specifies the maximum number of retries allowed when selecting a product to exchange. The default value is `3`. | integer  
$flow.max_retry_select_quantity | Specifies the maximum number of retries allowed when selecting the quantity of product to exchange. The default value is `2`. | integer  
$flow.max_retry_size_number_counter | Specifies the maximum number of retries allowed when selecting the size to exchange. The default value is `2`. | integer  
$flow.max_retry_another_zip_code | Specifies the maximum number of retries allowed when providing a zip code. The default value is `2`. | integer  
$flow.max_store_display_counter | Specifies the maximum number of stores to present in a single turn. The default value is `1`. | integer  
$flow.max_store_display | Specifies the maximum number of stores to present over the entire conversation. The default value is `10`. | integer  
$flow.max_retry_store_number_counter | Specifies the maximum number of retries allowed when selecting a store. The default value is `2`. | integer  
$flow.max_retry_store_selection | Specifies the number of retries allowed when confirming the store selection. The default value is `3`. | integer  
$flow.max_available_address_reselection_counter | Specifies the number of retries allowed when confirming whether the user would like to select a different store address. The default value is `2`. | integer  
$flow.order_payment_mode_COD | Specifies the value of the `order_payment_mode` field returned by the `get_order_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order#webhook-setup) indicating a cash on delivery (COD) payment method. The default value is `"COD"`. | string  
$flow.order_payment_mode_store_credit | Specifies the value of the `order_payment_mode` field returned by the `get_order_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order#webhook-setup) indicating a store credit payment method. The default value is `"store_credit"`. | string  
$flow.order_refund_mode_source_account | Specifies the value of the `prebuilt_components_exchange_order_refund_mode` entity indicating that the user selected to refund to their source account. The default value is `source_account`. | string  
$flow.order_exchange_location_scheduled_for_pickup | Specifies the value of the `prebuilt_components_exchange_order_location` entity indicating that the user selected to schedule a pickup for the exchange. The default value is `scheduled_for_pickup`. | string  
  
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

The `prebuilt_components_exchange_order:get_order_details` webhook is used by the component to retrieve order details for a specified order.

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
exchangeable_product_id | List of product IDs for exchangeable products within the order. | List (string)  
exchangeable_product_name | List of product names for exchangeable products within the order. | List (string)  
exchangeable_product_brand_name | List of brand names for exchangeable products within the order. | List (string)  
exchangeable_product_quantity | List of quantities for exchangeable products within the order. | List (string)  
exchangeable_product_price | List of prices for exchangeable products within the order. | List (string)  
  
####  To configure the Get order details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_exchange_order:get_order_details webhook. 
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



### Get available exchange size

The `prebuilt_components_exchange_order:get_available_exchange_size` webhook is used by the component to retrieve available sizes for exchange in cases where the user would like to exchange an item due to size or fit issues.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.selected_order_product_id | Product ID of the product that the user wants to exchange. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
product_available_sizes | List of available sizes for the selected product. | List (string)  
  
####  To configure the Get available exchange size webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_exchange_order:get_available_exchange_size webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get product exchange availability

The `prebuilt_components_exchange_order:get_product_exchange_availability` webhook is used by the component to check whether the user's selected product, quantity, and optional size are available for exchange.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.order_id | Order ID to retrieve details for. | string  
$flow.selected_order_product_id | Product ID of the product that the user wants to exchange. | string  
$flow.order_product_quantity_exchange_count | Quantity of the product the user wants to exchange. | integer  
$flow.product_selected_size | Size of the product the user wants to exchange for. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
product_exchange_availability | Indicates whether the selected product, quantity, and size is available for exchange. | boolean  
product_exchange_price | Indicates the exchange price for a single item of the selected product and size. | number  
  
####  To configure the Get product exchange availability webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_exchange_order:get_product_exchange_availability webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Raise incomplete order ticket

The `prebuilt_components_exchange_order:raise_incomplete_order_ticket` webhook is used by the component to raise a ticket when the user wants to exchange a product within an order due to it being incomplete.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to submit a ticket for. | string  
$flow.selected_order_product_id | Product ID of the product that the user wants to exchange. | string  
$flow.order_product_quantity_exchange_count | Quantity of the product the user wants to exchange. | integer  
$flow.order_product_exchange_reason | The reason why the user wants to exchange the product. | string  
  
####  To configure the Raise incomplete order ticket webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_exchange_order:raise_incomplete_order_ticket webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get store details

The `prebuilt_components_exchange_order:get_store_details` webhook is used by the component to retrieve the list of stores near the user's provided zip code.

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
  6. Select the prebuilt_components_exchange_order:get_store_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Post exchange details

The `prebuilt_components_exchange_order:post_exchange_details` webhook is used by the component to submit an exchange.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to submit a ticket for. | string  
$flow.selected_order_product_id | Product ID of the product that the user wants to exchange. | string  
$flow.order_product_quantity_exchange_count | Quantity of the product the user wants to exchange. | integer  
$flow.product_selected_size | Size of the product the user wants to exchange for. | string  
$flow.order_product_exchange_reason | The reason why the user wants to exchange the product. | string  
$flow.order_exchange_location | The selected mode for the exchange. Valid values are defined by the `prebuilt_components_exchange_order_location` entity. | string  
$flow.order_exchange_store_id | The store ID for the store selected by the user for a store exchange. | string  
$flow.order_refund_mode | The payment mode for refund, if applicable. Valid values are defined by the `prebuilt_components_exchange_order_refund_mode` entity. If no refund is required, this value is `null`. | string  
$flow.total_refund_amount | The amount to be refunded, if the exchangeable product price is higher than the new product. If no refund is required, this value is `null`. | integer  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
order_exchange_ticket_id | Ticket ID for the submitted exchange. | string  
  
####  To configure the Post exchange details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_exchange_order:post_exchange_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send COD refund information

The `prebuilt_components_exchange_order:send_COD_refund_information` webhook is used by the component to send exchange-related payment information to a user.

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
  6. Select the prebuilt_components_exchange_order:send_COD_refund_information webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Disputes  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/disputes)

[ Next Feedback  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/feedback)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
