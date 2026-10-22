---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits/
title: Enforce monetization limits in API proxies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:08.268359+00:00
---

# Enforce monetization limits in API proxies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enforce-monetization-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enforce monetization limits in API proxies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to enforce monetization limits by attaching policies to API proxies in a monetized API product.

## Add an authentication policy

Apigee monetization uses the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) or the [ VerifyAccessToken operation of the OAuth2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#verifyingaccesstokens) to determine if an incoming request is monetizable by checking for the active published rate plan. 

Attach the policy to the API proxy using the Apigee UI or the API. See [Editing an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy) for information on editing a proxy. 

See also: 

  * [Attaching a policy to a flow](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#attaching-a-policy-to-a-flow)
  * [Verifying access tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-access-tokens)
  * [Monitoring and debugging the authentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace#auth) using Debug



## Enforce subscriptions on API products

Attach the [ MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy) to API proxies to enforce subscriptions on the API product by developer or AppGroup: 

  * If no active rate plan exists for the API product fetched during the proxy call execution, the product is deemed non-monetized, the MonetizationLimitsCheck policy does not fetch any further data, and the policy has no effect. 
  * If a rate plan is found but a subscription is not found for the API developer or AppGroup, the MonetizationLimitsCheck policy raises a fault and blocks the API call. 



When you attach the MonetizationLimitsCheck policy to an API proxy, Apigee populates the `mint.limitscheck.*` and `mint.subscription_*` flow variables, as described in [Debugging the MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace#monetizationlimitscheck) and the [mint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint) flow variable reference. 

**Note** : To prevent specific transactions from getting billed, you can use the **transactionSuccess** monetization variable. For more information about using the **transactionSuccess** variable, see [Monetization variables](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data#monetization-variables). 

For more information, see:

  * [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy#apigee-ui)
  * [Editing an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy)
  * [Attaching a policy to a flow](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#attaching-a-policy-to-a-flow)
  * [Debugging the MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace#monetizationlimitscheck) using Debug
  * [MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy)



## Enforce monetization quotas in API proxies

**Note:** If you add a quota after the API product has been in use, the quota calculation starts from the next monetized transaction. 

A quota defines the number of requests allowed for an API product over a given time period. To enforce quotas for monetization, it is recommended that you set the quota value when [creating an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products). 

Defining a quota value for an API product does not automatically enforce restrictions on the number of calls that can be made through the API product. You must also add Quota policies to the API proxies that are referenced by the API product to ensure the quota value defined at the API product-level is enforced. 

Edit the Quota policy to enable the [<UseQuotaConfigInAPIProduct>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#usequotaconfiginapiproduct) element to use the quota configuration defined at the API product-level. 

For example:
    
    
    <Quota continueOnError="false" enabled="true" name="impose-quota">
        <DisplayName>Impose Quota</DisplayName>
        **< UseQuotaConfigInAPIProduct stepName="verify-api-key">
            <DefaultConfig>
                <Allow>10000</Allow>
                <Interval>1</Interval>
                <TimeUnit>week</TimeUnit>
            </DefaultConfig>
        </UseQuotaConfigInAPIProduct>**
        <Distributed>true</Distributed>
        <Synchronous>true</Synchronous>
        <StartTime>2021-01-01 12:00:00</StartTime>
    </Quota>
    

**Notes:**

  * You can define the default configuration `<DefaultConfig>` to use if the quota configuration is not defined in the API product, but the quota configuration defined at the API product-level takes precedence. 
  * When you add the `<UseQuotaConfigInAPIProduct>` element to the Quota policy, then Apigee ignores any `<Allow>`, `<Interval>`, and `<TimeUnit>` child elements of `<Quota>`. 



When you attach the Quota policy to an API proxy, the `ratelimit.*` flow variables are populated, as described in [Debugging the Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace#quota) and the Quota policy [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#variables) reference. 

For more information, see:

  * [Editing an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy)
  * [ Attaching a policy to a flow](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui#attaching-a-policy-to-a-flow)
  * [ Debugging the Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/debug-trace#quota) using Debug 
  * [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
