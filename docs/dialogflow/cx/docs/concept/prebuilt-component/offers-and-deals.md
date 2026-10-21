---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals/
title: Offers and deals prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:44.732392+00:00
---

# Offers and deals prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Offers and deals prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The offers and deals [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) checks whether the caller is a registered user. If the user has a registered account, the component can provide information about user-specific offers and deals. The user can also get details on general offers and deals or report issues with a specific coupon code. This component uses the [Alphanumeric collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection) prebuilt component to collect coupon codes. The component also uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) for post-call summarization, FAQs, and offer details.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called using telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### User-specific and general offers and deals

End-user has been previously authenticated. The user asks for their latest offers and the agent presents a list of offers specific to the user. The user asks some questions about the offers, then asks for offers in a specific category. The agent presents the list of offers in the category. The agent offers to send the offer details to the user and the user declines.

User input | Agent response  
---|---  
| Welcome! Would you like to explore our latest offers or are you experiencing any issues with a specific coupon code?  
I want to see the latest offers |   
| To confirm, you are looking for offers. Is that correct?  
yes |   
| We found the following offers for you, here are the details:  
Offer 1: Get 5% off on apparels, use code APPARELS5, valid until 2024-03-28.  
Offer 2: Get 15% off on grocery, use code GROCERY500, valid until 2024-03-28.8.  
  
Hope you find these offers interesting. Do you have any queries about offers or deals that we can answer for you?  
Is there a purchase minimum for the grocery offer? |   
| Yes, there is a minimum purchase value of 10 to avail the 15% off on grocery. Use code GROCERY500 to redeem this offer, valid until 2024-03-28.  
  
We hope to be able to provide you with the details you require. Do you have any queries about offers or deals that we can answer for you?  
Do you have any offers for electronics? |   
| Certainly! Here are the offer details:  
Offer 1: Enjoy 5% off on electronics, use code ELECTRIC5, valid until 2024-03-28.  
Offer 2: Get 15% off on electronics, use code ELECTRIC15, valid until 2024-03-28.  
  
We hope to be able to provide you with the details you require. Do you have any queries about offers or deals that we can answer for you?  
No I'm done |   
| Do you want offer details to be shared on your registered mobile or email?  
No thanks |   
| Thank you for calling.  
  
### Issue with a coupon code

End-user has been previously authenticated. The user mentions that they have an issue with a coupon code. The agent collects the coupon code and provides the user with details about the coupon code redemption. The user confirms that they are having an issue with the coupon code and the agent submits a ticket to report the issue.

User input | Agent response  
---|---  
| Welcome! Would you like to explore our latest offers or are you experiencing any issues with a specific coupon code?  
I'm having issues with a coupon code |   
| To confirm, you are looking for coupon codes. Is that correct?  
yes |   
| We're sorry to hear that. Could you please share the coupon code you're using?  
| _Agent collects the coupon code using[Alphanumeric collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection) prebuilt component_  
| The offer code APPARELS5 associated with apparels needed minimum purchase value of 100$ and valid till 2024-03-28, please ensure the conditions such as minimum purchase requirement are met.  
  
Is this information helpful for you?  
no |   
| Please specify the issue you are experiencing. You may say something like my coupon code isn't working, code is not working in my area.  
coupon code isn't working |   
| To confirm, the coupon code issue provided is coupon code isn't working. Is this correct?  
yes |   
| We've raised a ticket to report your issue. Thank you for calling.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Offers and Deals  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_offers_and_deals_category  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_offers_and_deals:get_offers_details  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | (optional) User's local phone number, without the country code, used to identify the user. | string  
  
This prebuilt component allows the following optional parameters to configure the behavior of the component, including retries.

Parameter Name | Description | Format  
---|---|---  
$flow.max_retry_concern_type | Specifies the number of retries allowed when selecting whether the user would like to hear offers or report an issue with a coupon code. The default value is `2`. | integer  
$flow.max_retry_offers_category | Specifies the number of retries allowed when providing a category to hear offers for. The default value is `2`. | integer  
$flow.max_retry_another_coupon_code | Specifies the number of retries allowed when providing the specific coupon code the user is having an issue with. The default value is `2`. | integer  
$flow.max_retry_coupon_code_issue_counter | Specifies the number of retries allowed when providing the issue the user is having with a coupon code. The default value is `2`. | integer  
$flow.max_retry_message_confirm_channel | Specifies the number of retries allowed when providing a channel to receive offer details on. The default value is `2`. | integer  
$flow.valid_coupon_code_status | Specifies the value of the `coupon_code_status` field returned by the `get_coupon_code_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals#webhook-setup) indicating that the coupon code is valid. The default value is `"valid"`. | string  
$flow.invalid_coupon_code_status | Specifies the value of the `coupon_code_status` field returned by the `get_coupon_code_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals#webhook-setup) indicating that the coupon code is invalid. The default value is `"invalid"`. | string  
$flow.expired_coupon_code_status | Specifies the value of the `coupon_code_status` field returned by the `get_coupon_code_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals#webhook-setup) indicating that the coupon code is expired. The default value is `"expired"`. | string  
  
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
  
## Generators

This component uses [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) to enable specific parts of the conversation.

### Summarization

The `Summarization` generator is used to generate a post-call summary describing the conversation handled by the component.

### General FAQ

The `General FAQ` generator is used to handle frequently-asked questions related to discounts, sales, purchases, and loyalty programs.

  * _Can I return sale products if I change my mind?_
  * _Can I get free samples or gifts with certain product purchases?_
  * _Do you offer price adjustments if the item I bought goes on sale later?_
  * _Is there a time limit for redeeming loyalty program rewards?_



### User-specific offer details

The `User-specific offer details` generator is used to provide details about user-specific offers based on the information provided by the `get_offers_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals#webhook-setup).

### Offers and deals details

The `Offers and deals details` generator is used to provide details about general offers and deals based on the information provided by the `get_offers_details` [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals#webhook-setup). The user can ask about offers in a specific category or ask for more detail about specific offers.

### Offers and deals FAQ

The `Offers and deals FAQ` generator is used to handle frequently-asked questions related to offers and deals.

  * _Are there special offers for new customers?_
  * _How can I be notified of upcoming deals?_
  * _Are there deals exclusively available in-store or online?_
  * _How often are new deals added to your platform?_



### Discount and promo code FAQ

The `Discount and promo code FAQ` is used to handle frequently-asked questions related to discounts and promotional codes.

  * _Can I use a discount code more than once?_
  * _Can I use multiple discounts on a single order?_
  * _How can I redeem a discount code during checkout?_
  * _What if I forgot to apply a discount code during checkout?_



## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).
  2. Configure the provided [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) with configuration describing your external services, see Webhook setup.



## Webhook setup

In order to use this component, you will need to configure the included [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to retrieve needed information from your external services.

### Get offers details

The `prebuilt_components_offers_and_deals:get_offers_details` webhook is used by the component to retrieve details about user-specific and general offers.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | Phone number to retrieve offer details for. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
active_category | List of offer categories available to the user. Valid values are defined by the `prebuilt_components_offers_and_deals_category` entity. | List (string)  
user_email | Email registered to the provided account, used to send offer details. | string  
user_offer | List of user-specific offer details. Each element of the list represents a single offer, with key-value pairs describing different attributes of the offer, for example `{"valid_from": "2024-01-29", "sale_type": "none", "valid_until": "2024-03-28", "offer_id": "G5E0M2D7A6Y4W9S", "discount_value": "5%", "coupon_code": "ELECTRIC5", "is_redeem_allowed": "true", "minimum_order_value": "1000", "maximum_discount_amount": "200", "offer_category_name": "electronics"}`. | List (object)  
all_offers | List of general offer details. Each element of the list represents a single offer, following the same format as the `user_offer` field. | List (object)  
  
####  To configure the Get offers details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_offers_and_deals:get_offers_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get coupon code details

The `prebuilt_components_offers_and_deals:get_coupon_code_details` webhook is used by the component to retrieve details about a specific coupon code that a user has reported issues with.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$flow.coupon_code | Coupon code to retrieve details for. | string  
$session.params.phone_number | Phone number associated with the user's account. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
offer_id | Offer ID for the coupon code. | string  
offer_category_name | Category for the coupon code. Valid values are defined by the `prebuilt_components_offers_and_deals_category` entity. | string  
coupon_code_status | Status of the coupon code. Valid values are defined by the `$flow.valid_coupon_code_status`, `$flow.invalid_coupon_code_status`, and `$flow.valid_coupon_code_status` [input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals#input-parameters). | string  
valid_until | Date the coupon code is valid until, in `YYYY-MM-DD` format. | string  
minimum_order_value | Minimum order value for the coupon code. | string  
  
####  To configure the Get coupon code details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_offers_and_deals:get_coupon_code_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Send message

The `prebuilt_components_offers_and_deals:send_message` webhook is used by the component to send a message containing offer details to the user's selected channel.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.confirmation_channel | Channel the user has selected to receive offer details on. Valid values are defined by the `prebuilt_components_channel_email_phone` entity. | string  
  
####  To configure the Send message webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_offers_and_deals:send_message webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Raise ticket

The `prebuilt_components_offers_and_deals:raise_ticket` webhook is used by the component to submit a ticket reporting a user issue with a coupon code.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.coupon_code | Coupon code the user has reported an issue for. | string  
$flow.offer_id | Offer ID for the provided coupon code. | string  
$flow.coupon_code_issue | User's provided issue for the coupon code. | string  
  
####  To configure the Raise ticket webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the rebuilt_components_offers_and_deals:raise_ticket webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Numeric collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/numeric-collection)

[ Next Open account  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
