---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace/
title: Debugging monetization using the Debug tool \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:09.671686+00:00
---

# Debugging monetization using the Debug tool  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Debugging monetization using the Debug tool Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Debug monetization using Debug as described in the following sections. 

##  Debugging the authentication policy phase 

Apigee monetization uses the VerifyAPIKey or VerifyAccessToken policy to determine if an incoming request is monetizable by checking for the active published rate plan. For more information about adding the policy, see [Adding an authentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#auth). 

For example, the following image shows the details of the VerifyAPIKey policy phase in the request flow. 

![VerifyAPIKey policy phase details including the monetization flow variables](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/trace-mint-verifyapikey.png)

After authenticating the user, the VerifyAPIKey policy checks all published rate plans to determine which, if any, is active based on their activation and expiration times. If an active published rate plan is found, the following flow variables are populated:

Flow variable | Setting | `mint.mintng_is_apiproduct_monetized` | `true` if active published rate plan is found.  
---|---  
`mint.mintng_rate_plan_id` | Rate plan ID.  
`mint.rateplan_end_time_ms` | Expiration time for the rate plan. For example: `1619433556408`  
`mint.rateplan_start_time_ms` | Activation time of the rate plan. For example: `1618433956209`  
  
If no active published rate plan is found, the `mint.mintng_is_apiproduct_monetized` flow variable is set to `false` and the additional flow variables are not populated. 

For more information, see [mint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint) flow variables.

##  Debugging the MonetizationLimitsCheck policy phase 

Apigee monetization uses the MonetizationLimitsCheck policy to enforce app developer and AppGroup subscriptions to the API product. For more information about adding the policy, see [Enforcing subscriptions to API products](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#subscriptions). 

**Note:** The MonetizationLimitsCheck policy has no effect if no active published rate plan is found and the `mint.mintng_is_apiproduct_monetized` flow variable is set to `false`.

For example, the following image shows the details of the MonetizationLimitsCheck policy phase in the request flow. 

![MonetizationLimitsCheck policy phase details including the monetization flow variables](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/trace-monetizationlimitscheck.png)

If the app developer or AppGroup purchased a subscription to the API product, the following flow variables are populated:

Flow variable | Description | `mint.limitscheck.is_request_blocked` | `true` for blocked requests.  
---|---  
`mint.limitscheck.is_subscription_found` | `true` if an API subscription is found.  
`mint.limitscheck_purchased_product_name` | Name of the purchased API product. For example: `MyProduct`  
`mint.limitscheck.status_message` | Status message. For example: `limits_check_success`  
`mint.prepaid_developer_balance` | Current balance in the app developer's or AppGroup's prepaid account wallet associated with the rate plan's currency.  
`mint.prepaid_developer_currency` | Currency of the balance available in the `mint.prepaid_developer_balance` variable.  
`mint.subscription_end_time_ms` | End time of the API product subscription.  
`mint.subscription_start_time_ms` | Start time of the API product subscription. For example: `1618433956209`  
  
If the app developer or AppGroup did not purchase a subscription to the API product: 

  * `mint.limitscheck_is_subscription_found` flow variable is set to `false`
  * `mint.limitscheck.is_request_blocked` is set to `true`
  * No other flow variables are populated.



For more information, see [mint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint) flow variables. 

##  Debugging the Quota policy phase 

Apigee monetization uses the Quota policy to enforce the quotas defined at the API product level. Quotas define the number of requests allowed for an API product over a given time period. For more information about the adding the policy, see [Enforcing monetization quotas in an API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits#quotas). 

**Note:** The MonetizationLimitsCheck policy has no effect if no active published rate plan is found and the `mint.mintng_is_apiproduct_monetized` flow variable is set to `false`.

For example, the following image shows the details of the Quota policy phase in the request flow where the quota has been exceeded. 

![Quota policy phase details including the monetization flow variables](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/trace-monetization-quota.png)

In this example, the quota has been exceeded, an HTTP `429 Too Many Requests` status is returned, and the flow `ratelimit.*` flow variables are populated to provide more details about the quota exception. For a description of the `ratelimit.*`, see the [Quota policy flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#variables). 

## Debugging the DataCapture policy phase

Apigee uses the monetization variables captured by the DataCapture policy for rating, calculating revenue share, and analytics. For more information about the capturing the monetization variables in the policy, see [Capturing monetization data](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data). 

For example, the following image shows the details of the DataCapture policy execution phase in the response flow.

![DataCapture policy execution phase with the monetization flow variables](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/trace-mint-datacapture.png)

If there are no errors when capturing the monetization variables, the following flow variables are populated for a transaction: 

Flow variable | Description | `mint.mintng_currency` |  Currency for calculating the revenue. This flow variable has the value of the `currency` monetization variable.  
---|---  
`mint.mintng_price` |  Revenue for calculating the app developer's or AppGroup's share. This flow variable has the value of the `revShareGrossPrice` monetization variable.  
`mint.mintng_price_multiplier` |  Factor (multiplier) by which the per-transaction cost is multiplied. This flow variable has the value of the `perUnitPriceMultiplier` monetization variable.  
`mint.mintng_tx_success` |  Specifies if the transaction is monetized. This flow variable has the value of the `transactionSuccess` monetization variable.  
  
##  Debugging the monetized API proxy execution phase 

After the successful execution of the monetized API proxy, a set of flow variables are populated with information about the monetization consumption-based fees and rates charged.

For example, the following image shows the details of the **Proxy Execution** phase in the PostClient flow where the variables are populated.

![Proxy Execution phase details including the monetization flow variables](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/trace-monetization-execution.png)

If the monetized API proxy execution succeeds, the following flow variables are populated:

Flow variable | Description | `message.status.code` | HTTP status code of the response message from target. If you have any policy in your response, the value of this variable is overridden by status code returned by the policy.  
---|---  
`mint.limitscheck.is_request_blocked` | Flag that specifies whether the API request is blocked.  
`mint.mintng_consumption_pricing_rates` | Consumption-based fees set in the rate plan.  
`mint.mintng_consumption_pricing_type` | Consumption-based pricing type set in the rate plan. For example: `FIXED_PER_UNIT`  
`mint.mintng_dev_share` | Revenue to be shared with the app developer or AppGroup.  
`mint.mintng_price_multiplier` | Factor (multiplier) captured from the DataCapture policy. The per-transaction cost is multiplied by this factor.  
`mint.mintng_rate` |  Rate charged for the API call.  
`mint.mintng_rate_before_multipliers` | Rate charged for the API call without the `perUnitPriceMultiplier` calculation.  
`mint.mintng_revenue_share_rates` | Revenue share rates set in the rate plan.  
`mint.mintng_revenue_share_type` | Revenue share type set in the rate plan.  
`mint.prepaid_updated_developer_usage` | Current usage of the prepaid app developer or AppGroup.  
`mint.status` | Status of the monetized call. Populated only on error.  
`mint.status_code` | HTTP status code of the monetized call. Populated only on error.  
`mint.tx_success_result` | Indicates whether monetization is successful for the transaction.  
  
For a detailed description of all the variables, see [mint flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
