---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/fraud-and-dispute-retail/
title: Retail fraud and dispute prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:43.014448+00:00
---

# Retail fraud and dispute prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/fraud-and-dispute-retail/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Retail fraud and dispute prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The retail fraud and dispute [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks a user's authentication level. Once the user has been authenticated, the component provides information about the user's most recent or past orders. The user may then submit a dispute related to an order or product. This component uses the [Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) prebuilt component to authenticate users. The component also uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) for post-call summarization.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Dispute for individual product

End-user has not been previously authenticated. The agent collects details about previous orders to verify the user's identity. Once the user has been authenticated, the agent collects information about the dispute including dispute reason and the specific product the user would like to dispute. After collecting required details, the agent then submits the dispute and provides the user with the confirmation number.

User input | Agent response  
---|---  
| Hello John. In order to verify yourself, we'll need your order ID, transaction date, and amount before filing your fraud or dispute case.  
| Could you please provide the last 5 digits of your order ID?  
12345 |   
| The last five digits of the order ID that we got are 12345, is that correct?  
yes |   
| Great, we are done collecting the order ID.  
  
Please provide your date of order. Please say your order month, followed by your order day, and then your order year.  
2023-10-12 |   
| Okay, your order date is October 12, 2023, is that correct?  
yes |   
| Great, we have collected your order date.  
  
Please tell us the dollar amount of your order. For example, if your order transaction amount was $100.30, say "100".  
97 |   
| Okay, your order transaction amount is $97, is that correct?  
yes |   
| Please specify the nature of fraud or dispute you want to report. You may say something like: payments or billing, product, returns & refund, data security or privacy concern, delivery or shipping, packaging, or say "others".  
product |   
| Thank you for letting us know. To confirm, the reason for fraud or dispute is product. Is this correct?  
yes |   
| Please tell us whether the selected issue is related to an entire order, an individual product, or any other concerns.  
product |   
| Are you calling about your most recent order number ending with 12345 containing 2 lamp, 1 shirt and 1 other product placed on 2023-11-10 at 06:00 PM?  
yes |   
| We've found some products in your order. Please tell us which product you would like to report. Product 1: Google lamp, Product 2: Google shirt, Product 3: Google jeans.  
  
Please say or enter the product number of the item you want to select, or say "next" to show more products.  
3 |   
| To verify, you are interested in raising fraud or dispute case for the Google jeans. Is this correct?  
yes |   
| In a few words, please tell us the detailed reason for this fraud or dispute.  
poor quality |   
| To confirm, the fraud or dispute reason provided is poor quality. Is this correct?  
yes |   
| Thanks for the confirmation. We have raised a ticket to our Fraud or Dispute team. You should hear from them shortly. Your ticket number is 6595513.  
  
Would you like to hear the confirmation number again?  
yes |   
| Your ticket number is 6595513.  
  
Would you like us to send a confirmation message containing the ticket number?  
yes |   
| Would you like to receive your confirmation message via your registered phone or email?  
phone |   
| Just to confirm, would you like to receive the confirmation message on your phone? Please say yes or no.  
yes |   
| Thanks. A confirmation message has been sent to your registered phone. This may take some time.  
  
Do you wish to raise fraud or dispute ticket for another order?  
no |   
| Thank you for calling us. Our team will follow up on your ticket.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Fraud and Dispute  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_product_dispute_reason  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_fraud_and_dispute_order:get_security_answers  
  
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
$flow.max_retry_telephone_number | Specifies the number of retries allowed when providing a registered telephone number. The default value is `2`. | integer  
$flow.max_retry_order_number | Specifies the number of retries allowed when providing the last five digits of an order number. The default value is `2`. | integer  
$flow.max_retry_another_order | Specifies the number of retries allowed when selecting another order for return in cases where the order ID is not found or the order is not eligible for return. The default value is `2`. | integer  
$flow.max_retry_select_order_number | Specifies the number of retries allowed when providing the full order number in cases where multiple orders share the same last five digits. The default value is `2`. | integer  
$flow.max_product_display_counter | Specifies the maximum number of products to present in a single turn. The default value is `2`. | integer  
$flow.max_product_display | Specifies the maximum number of products to present over the entire conversation. The default value is `9`. | integer  
$flow.max_retry_product_number_counter | Specifies the maximum number of retries allowed when selecting a product to return. The default value is `2`. | integer  
$flow.max_product_report_confirm | Specifies the maximum number of retries allowed when confirming the selected product. The default value is `2`. | integer  
$flow.max_retry_dispute_reason | Specifies the number of retries allowed when confirming the reason for dispute. The default value is `2`. | integer  
  
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
dispute_ticket_id | Ticket ID for the submitted dispute. | string  
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

If you have not previously configured external services required for authentication, you will need to configure them to enable authentication of users for this component. See [Verify user details webhook setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail#verify-user-details) for detailed instructions to set up the `prebuilt_components_retail_authentication:verify_user_details` webhook.

### Get order details

The `prebuilt_components_fraud_and_dispute_order:get_order_details` webhook is used by the component to retrieve order details for a specified order.

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
order_amount | Dollar amount for the order. | integer  
order_payment_mode | Indicates the payment mode used when placing the order. | string  
all_product_id | List of product IDs for all products within the order. | List (string)  
all_product_name | List of product names for all products within the order. | List (string)  
all_product_brand_name | List of brand names for all products within the order. | List (string)  
all_product_quantity | List of quantities for all products within the order. | List (string)  
  
####  To configure the Get order details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_fraud_and_dispute_order:get_order_details webhook. 
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



### Post reporting details

The `prebuilt_components_fraud_and_dispute_order:post_reporting_details` webhook is used by the component to submit a fraud or dispute ticket.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_id | Order ID to submit a ticket for. | string  
$flow.dispute_product_id | Product ID that the user wants to file a dispute for. | string  
$flow.order_product_dispute_reason | Dispute reasons for the disputed product. Valid values are defined by the `prebuilt_components_product_dispute_reason` entity. | string  
$flow.order_product_dispute_reason_other | If the user selected "others" as the dispute reason, this contains the specific dispute reason the user has provided. | string  
$flow.order_product_dispute_reason_detail | Detailed dispute reason. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
order_product_dispute_ticket_number | Ticket ID for the submitted dispute. | string  
  
####  To configure the Post reporting details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_fraud_and_dispute_order:post_reporting_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send message

The `prebuilt_components_fraud_and_dispute_order:send_message` webhook is used by the component to send confirmation details about the dispute to a user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.order_product_dispute_ticket_number | Confirmation number for the submitted dispute. | string  
$flow.confirmation_channel | The specific channel to send information to. Valid values are defined by the `prebuilt_components_channel_email_phone` entity. By default `phone` and `email` are supported. | string  
  
####  To configure the Send message webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_fraud_and_dispute_order:send_message webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Feedback  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/feedback)

[ Next Financial services steering  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/financial-services-steering)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
