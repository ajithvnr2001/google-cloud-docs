---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment/
title: Make a payment prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:08.102492+00:00
---

# Make a payment prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Make a payment prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

The make a payment [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) authenticates the user and allows them to make a payment. This component uses a customized version of the [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component to authenticate account holders and cardholders. The component also uses the [Name collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection), [Credit card expiration date collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection), and [Credit card CVV collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection) prebuilt components to collect information required to make payments.

## Payment types

This component supports payments for credit card bills and beneficiary accounts. For credit card bills, users can choose to pay the minimum, total, or a custom amount towards their bill. The user may make payments from their bank account, debit or credit card, or mobile payment.

Payment type | Available payment methods | Available payment amounts  
---|---|---  
Credit card bill | Bank account, debit card, mobile payment | Minimum, total, custom amount  
Beneficiary account | Bank account, credit card, debit card, mobile payment | Custom amount  
  
## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not encrypt any data.



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Beneficiary account payment

The agent identifies that the user has not been previously authenticated and collects information to verify that the user is a registered user. The user indicates that they would like to make a payment to a beneficiary account, and the agent collects required information including beneficiary name and confirms the account number. Finally, the user selects to make a payment using their debit card, so the agent collects the debit card number, expiration date, CVV, and confirms the payment.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Would you like to pay your registered credit card bill or make a payment to an existing beneficiary account?  
Beneficiary |   
| _Agent collects beneficiary name using[Name collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection) prebuilt component_  
| Thank you, we have collected the beneficiary name.  
  
Okay, based on our records, we have the account number ending in 7821. Please say yes, to confirm the account number.  
Yes |   
| Please confirm the amount you want to pay. For example, if you want to pay $100.30, say 100 point 30.  
50 dollars |   
| Do you want to pay by your bank account, debit card, credit card or mobile payment?  
Debit |   
| Can you please help us with the last 4 digits of the debit card number you are referring to?  
1234 |   
| The last four digits of the debit card number that we got are 1234, is that correct?  
Yes that's right |   
| _Agent collects debit card expiration date using[Credit card expiration date collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection) prebuilt component_  
| Great, we are done with collecting the debit card's expiration date.  
| _Agent collects debit card CVV using[Credit card CVV collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection) prebuilt component_  
| Great, we are done with collecting the CVV.  
| Okay, we are going to make a payment of $50 to Jane with the debit card number ending in 1234. Do you confirm this action?  
Yes |   
| To proceed we will send you a code. Do you prefer to receive the code by phone or email?  
Email please |   
| We have sent a code to your registered email john.doe@google.com. This may take a few seconds. Can you please confirm the code?  
123456 |   
| Okay, please wait for a few seconds while we are making the payment.  
  
Your beneficiary account payment was successful.  
  
### Credit card bill payment

The agent identifies that the user has not been previously authenticated and collects information to verify that the user is a registered user. The user indicates that they would like to make a payment towards their credit card bill using their bank account. The agent confirms the payment amount and payment method details and completes the payment.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Would you like to pay your registered credit card bill or make a payment to an existing beneficiary account?  
Credit card bill |   
| Can you please help us with the last 4 digits of the credit card number you are referring to?  
4321 |   
| The last four digits of the credit card number that we got are 4321, is that correct?  
Yes |   
| Your total due amount is $300 and your minimum payment is $20. Do you wish to pay the total amount, the minimum amount, or any other amount?  
Total amount |   
| Do you want to pay by your bank account, debit card or mobile payment?  
Savings account |   
| We have found that there are 2 accounts associated with your number. Can you please help us with the last 4 digits of the account you are referring to?  
1001 |   
| The last four digits of the account number that we got are 1001, is that correct?  
Yes |   
| Okay, we are going to make a payment of $300 for your credit card bill ending in 4321 with the account number ending in 1001. Do you confirm this action?  
Yes |   
| To proceed we will send you a code. Do you prefer to receive the code by phone or email?  
Send it to my email |   
| We have sent a code to your registered email john.doe@google.com. This may take a few seconds. Can you please confirm the code?  
123456 |   
| Okay, please wait for a few seconds while we are making the payment.  
  
Your credit card payment was successful.  
  
### Insufficient funds or limits

The agent identifies that the user has not been previously authenticated and collects information to verify that the user is a registered user. The user attempts to make payments to their credit card bill using their bank account and their debit card, but both payments are declined due to insufficient funds or limits. Finally, the user opts to make a mobile payment and the agent sends them a link to complete the payment by mobile.

User input | Agent response  
---|---  
| _Agent authenticates user using[Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication) prebuilt component_  
| Thank you, you have been successfully authenticated.  
| Would you like to pay your registered credit card bill or make a payment to an existing beneficiary account?  
Credit card |   
| Can you please help us with the last 4 digits of the credit card number you are referring to?  
4321 |   
| The last four digits of the credit card number that we got are 4321, is that correct?  
Yes |   
| Your total due amount is $300 and your minimum payment is $20. Do you wish to pay the total amount, the minimum amount, or any other amount?  
Total amount |   
| Do you want to pay by your bank account, debit card or mobile payment?  
Savings |   
| We have found that there are 2 accounts associated with your number. Can you please help us with the last 4 digits of the account you are referring to?  
1002 |   
| The last four digits of the account number that we got are 1002, is that correct?  
Yes |   
| Okay, we are going to make a payment of $300 for your credit card bill ending in 4321 with the account number ending in 1002. Do you confirm this action?  
Yes |   
| To proceed we will send you a code. Do you prefer to receive the code by phone or email?  
Email |   
| We have sent a code to your registered email john.doe@google.com. This may take a few seconds. Can you please confirm the code?  
123456 |   
| Okay, please wait for a few seconds while we are making the payment.  
  
Your payment failed due to insufficient funds in the account. Do you want to retry the payment with another payment method?  
Yes |   
| Do you want to pay by your bank account, debit card or mobile payment?  
Debit card |   
| Can you please help us with the last 4 digits of the debit card number you are referring to?  
2345 |   
| The last four digits of the debit card number that we got are 2345, is that correct?  
Yes |   
| _Agent collects debit card expiration date using[Credit card expiration date collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection) prebuilt component_  
| Great, we are done with collecting the debit card's expiration date.  
| _Agent collects debit card CVV using[Credit card CVV collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection) prebuilt component_  
| Great, we are done with collecting the CVV.  
| Okay, we are going to make a payment of $300 for your credit card bill ending in 4321 with the debit card number ending in 2345. Do you confirm this action?  
Yes |   
| To proceed we will send you a code. Do you prefer to receive the code by phone or email?  
Email |   
| We have sent a code to your registered email john.doe@google.com. This may take a few seconds. Can you please confirm the code?  
123456 |   
| Okay, please wait for a few seconds while we are making the payment.  
  
Your payment failed since the limit was exceeded in the debit card. Do you want to retry the payment with another payment method?  
Yes |   
| Do you want to pay by your bank account, debit card or mobile payment?  
Mobile |   
| Okay, we are sending the payment link to your registered mobile number. This action can take a few seconds. Please confirm by saying yes if you have received it.  
Yes |   
| Great, now you can open the link and continue your payment.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Make A Payment  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_make_a_payment_payment_type  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_make_a_payment_payment_mode  
Webhook | prebuilt_components_[component_name]:[webhook_action] | prebuilt_components_make_a_payment:process_payment_credit_card  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$session.params.auth_level | (optional) Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
$session.params.auth_level_req | Indicates the [level of authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) needed before a user can access their transaction history. This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `1`. | integer  
$session.params.account_auth_enabled | Indicates whether the user should be authenticated as an account holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `true`. | boolean  
$session.params.card_auth_enabled | Indicates whether the user should be authenticated as a card holder as described in [Authentication types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-types). This value is configured in the [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) of the [page entry fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#use) in the `check auth level` page. By default this value is `false`. | boolean  
$session.params.phone_number | (optional) Customer's registered phone number used for authentication. | string  
$flow.payment_success_code | Specifies the value of the `payment_status_code` field returned by the `process_payment` [webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment#webhook-setup) indicating that the payment was successful. By default this value is `"200"`. | string  
$flow.insufficient_fund_code | Specifies the value of the `payment_status_code` field returned by the `process_payment` [webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment#webhook-setup) indicating that the payment could not be completed due to insufficient funds. By default this value is `"400"`. | string  
$flow.limit_exceed_code | Specifies the value of the `payment_status_code` field returned by the `process_payment` [webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment#webhook-setup) indicating that the payment could not be completed due to the daily limit being exceeded. By default this value is `"401"`. | string  
$flow.max_retry_mop_counter | Specifies the number of times a user is allowed to change their method of payment. The default value is `2`. | integer  
$flow.max_retry_credit_card_payment | Specifies the number of retries allowed when attempting to make a payment using a credit card as the method of payment. The default value is `3`. | integer  
$flow.max_retry_mobile_payment_counter | Specifies the number of retries allowed when attempting to make a payment using mobile payment as the method of payment. The default value is `2`. | integer  
$flow.max_retry_creditcard_count | Specifies the number of retries allowed when collecting a valid credit card number to make a payment. The default value is `3`. | integer  
$flow.max_retry_acc_number | Specifies the number of retries allowed when collecting valid account details to make a payment. The default value is `3`. | integer  
$flow.max_retry_debit_card_details | Specifies the number of retries allowed when collecting valid debit card details to make a payment. The default value is `3`. | integer  
$flow.max_retry_credit_card_details | Specifies the number of retries allowed when collecting valid credit card details to make a payment. The default value is `3`. | integer  
$flow.otp_length | Specifies the expected length of the one-time password sent to the user. The default value is `6`. | integer  
$flow.max_retry_otp_count | Specifies the number of retries allowed when collecting a valid one-time password (OTP) from the user. The default value is `3`. | integer  
$flow.max_waiting_room_counter | Specifies the number of times the user can ask the agent to wait as they receive the link for mobile payment. The default value is `2`. | integer  
  
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
auth_level | Indicates the [authentication level](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#authentication-levels) of the caller. | integer  
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

### Authentication

If you have not previously configured external services required for authentication, you will need to configure them to enable authentication of users for this component. See [Authentication webhook setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication#webhook-setup) for detailed instructions.

### Validate account

The `prebuilt_components_account_services:validate_account` webhook is used by the component to verify that an account exists based on the user's registered phone number and the last four digits of the account number provided. The webhook also returns the account balance, if an account exists.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.last_four_digit_of_account_number | The last four digits of the account number the user selected and confirmed to make a payment on. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
account_found | Indicates whether an account with the provided last four digits exists for the user's registered account. | boolean  
balance | The amount of the current balance on the account, if it exists. | number  
  
####  To configure the Validate account webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_account_services:validate_account webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### User card details

The `prebuilt_components_make_a_payment:user_card_details` webhook is used by the component to get details for a registered user's debit and credit cards.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
credit_card_count | Number of credit cards associated with the registered telephone number. | integer  
last_four_digit_of_credit_card_number | Last four digits of the user's credit card. If the customer has multiple credit cards, this value is `null`. | string  
debit_card_count | Number of debit cards associated with the registered telephone number. | integer  
last_four_digit_of_debit_card_number | Last four digits of the user's debit card. If the customer has multiple debit cards, this value is `null`. | string  
  
####  To configure the User card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:user_card_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Verify beneficiary name

The `prebuilt_components_make_a_payment:verify_beneficiary_name` webhook is used by the component to verify that a beneficiary account exists for the name provided by the user.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$session.params.name_collection_first_name | First name of the beneficiary. | string  
$session.params.name_collection_last_name | Last name of the beneficiary. | string  
$session.params.name_collection_middle_name | Middle name of the beneficiary. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
beneficiary_account_number | Last four digits of the beneficiary account number for the beneficiary name provided. If a beneficiary account for the provided name is not found, the value is `null`. | string  
  
####  To configure the Verify beneficiary name webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:verify_beneficiary_name webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Get due amount

The `prebuilt_components_make_a_payment:get_due_amount` webhook is used by the component to get information about the minimum and total amount due for the user's credit card bill.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.user_credit_card_number | Last four digits of the user's credit card. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
minimum_amount | Minimum amount due for the specified credit card bill. | number  
total_amount | Total amount due for the specified credit card bill. | number  
  
####  To configure the Get due amount webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:get_due_amount webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Verify credit card number

The `prebuilt_components_make_a_payment:verify_credit_card_number` webhook is used by the component to verify that the provided credit card number is registered to the user's account.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.user_credit_card_number | Last four digits of the user's credit card. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
card_found | Indicates whether the provided credit card was found. | boolean  
  
####  To configure the Verify credit card number webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:verify_credit_card_number webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Verify credit card details

The `prebuilt_components_make_a_payment:verify_credit_card_details` webhook is used by the component to verify that the provided details including expiration date and CVV are valid for the user's provided credit card.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.credit_card_number | Last four digits of the user's credit card. | string  
$flow.credit_card_exp_date | User's provided credit card expiration date for the specific credit card. | 
    
    
    {  
      "year": integer,  
      "month": integer  
    }  
  
$flow.credit_card_cvv_code | User's provided CVV code for the specified credit card. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
creditcard_verification_status | Indicates whether the provided credit card details were validated. | boolean  
  
####  To configure the Verify credit card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:verify_credit_card_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Verify debit card details

The `prebuilt_components_make_a_payment:verify_debit_card_details` webhook is used by the component to verify that the provided details including expiration date and CVV are valid for the user's provided debit card.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.debit_card_number | Last four digits of the user's debit card. | string  
$flow.debit_card_exp_date | User's provided debit card expiration date for the specified debit card. | 
    
    
    {  
      "year": integer,  
      "month": integer  
    }  
  
$flow.debit_card_cvv_code | User's provided CVV code for the specified debit card. | string  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
debitcard_verification_status | Indicates whether the provided debit card details were validated. | boolean  
  
####  To configure the Verify debit card details webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:verify_debit_card_details webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Process credit card payment

The `prebuilt_components_make_a_payment:process_payment_credit_card` webhook is used by the component to process a payment using the provided credit card details.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.payee_number | Last four digits of the payee's account number for the payment. | string  
$flow.payment_type | Payment type for the payment. Valid values are defined by the `prebuilt_components_make_a_payment_payment_type` custom entity. By default, this component supports `"beneficiary_pay"` and `"credit_card_pay"`. | string  
$flow.credit_card_number | Last four digits of the user's credit card. | string  
$flow.credit_card_exp_date | User's provided credit card expiration date for the specified credit card. | 
    
    
    {  
      "year": integer,  
      "month": integer  
    }  
  
$flow.credit_card_cvv_code | User's provided CVV code for the specified credit card. | string  
$flow.payment_amount | The amount the user has opted to pay. | number  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
payment_status_code | Indicates whether the payment was successful. Valid values are defined by the `$flow.payment_success_code`, `$flow.insufficient_fund_code`, and `$flow.limit_exceed_code` [configurable input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment#input-parameters). | string  
  
####  To configure the Process credit card payment webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:process_payment_credit_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Process debit card payment

The `prebuilt_components_make_a_payment:process_payment_debit_card` webhook is used by the component to process a payment using the provided debit card details.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.payee_number | Last four digits of the payee's account number for the payment. | string  
$flow.payment_type | Payment type for the payment. Valid values are defined by the `prebuilt_components_make_a_payment_payment_type` custom entity. By default, this component supports `"beneficiary_pay"` and `"credit_card_pay"`. | string  
$flow.debit_card_number | Last four digits of the user's debit card. | string  
$flow.debit_card_exp_date | User's provided debit card expiration date for the specified debit card. | 
    
    
    {  
      "year": integer,  
      "month": integer  
    }  
  
$flow.debit_card_cvv_code | User's provided CVV code for the specified debit card. | string  
$flow.payment_amount | The amount the user has opted to pay. | number  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
payment_status_code | Indicates whether the payment was successful. Valid values are defined by the `$flow.payment_success_code`, `$flow.insufficient_fund_code`, and `$flow.limit_exceed_code` [configurable input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment#input-parameters). | string  
  
####  To configure the Process debit card payment webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:process_payment_debit_card webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Process account payment

The `prebuilt_components_make_a_payment:process_payment_account` webhook is used by the component to process a payment using the provided account details.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.payee_number | Last four digits of the payee's account number for the payment. | string  
$flow.payment_type | Payment type for the payment. Valid values are defined by the `prebuilt_components_make_a_payment_payment_type` custom entity. By default, this component supports `"beneficiary_pay"` and `"credit_card_pay"`. | string  
$session.params.last_four_digit_of_account_number | Last four digits of the user's account. | string  
$flow.payment_amount | The amount the user has opted to pay. | number  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
payment_status_code | Indicates whether the payment was successful. Valid values are defined by the `$flow.payment_success_code`, `$flow.insufficient_fund_code`, and `$flow.limit_exceed_code` [configurable input parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment#input-parameters). | string  
  
####  To configure the Process account payment webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:process_payment_account webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Process mobile payment

The `prebuilt_components_make_a_payment:process_payment_mobile` webhook is used by the component to generate and send a mobile payment link for the user's selected payment details.

#### API request parameters

The following parameters are provided by the component as inputs to the API request.

Parameter Name | Description | Input Format  
---|---|---  
$session.params.phone_number | User's local phone number, without the country code, used to identify the user. | string  
$flow.payee_number | Last four digits of the payee's account number for the payment. | string  
$flow.payment_type | Payment type for the payment. Valid values are defined by the `prebuilt_components_make_a_payment_payment_type` custom entity. By default, this component supports `"beneficiary_pay"` and `"credit_card_pay"`. | string  
$flow.payment_amount | The amount the user has opted to pay. | number  
  
#### API response parameters

The following parameters are pulled from the API response to be used by the component.

Parameter Name | Description | Output Format  
---|---|---  
payment_link_generated | Indicates whether the mobile payment link was successfully generated and sent to the user. | boolean  
  
####  To configure the Process mobile payment webhook for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Manage** tab. 
  5. Click **Webhooks**. 
  6. Select the prebuilt_components_make_a_payment:process_payment_mobile webhook. 
  7. Replace the URL in the Dialogflow CX **Webhook URL** field with the endpoint for the service you want to integrate with. Select the proper **Method** in the dropdown. 
  8. Review and update the **Request body** to form the proper request format for your webhook. 
  9. Review and update the **Response configuration** to extract specific fields from your webhook's response. Do not modify the parameter names, as these are required by the component to access the returned field values. 
  10. Review and update the **Authentication** settings as needed. 
  11. Click **Save**. 



### Complete

Your agent and its webhooks should now be set up and ready to test.

[ Previous arrow_back  Lost and stolen card  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card)

[ Next Name collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
