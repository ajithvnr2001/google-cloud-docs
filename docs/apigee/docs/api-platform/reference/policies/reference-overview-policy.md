---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy/
title: Policy reference overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:39.745237+00:00
---

# Policy reference overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Policy reference overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee's policies augment your APIs to control traffic, enhance performance, enforce security, and increase the utility of your APIs, without requiring you to write code or modify backend services.

In addition, Apigee provides extension policies that let you implement custom logic in the form of JavaScript, Python, Java, and XSLT stylesheets.

## Policy categories and types

A policy's _category_ indicates the functional area (for example, security or mediation) for the policy. Policies are shown sorted by category below.

The policy type refers to how the policy can be used in Apigee:

  * **Standard policies** are suitable for internal development and lightweight API solutions. Standard policies can be used with any [environment type](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types). To see the list of standard policies, see Standard policies by category.
  * **Extensible policies** provide more functionality than standard policies, including for traffic management, mediation, and security. The extensible policies also include policies to implement custom logic in the form of JavaScript, Python, Java, and XSLT stylesheets.   
  
Extensible policies can be used with intermediate and comprehensive environment types only. Using an extensible policy automatically converts that proxy to an [Extensible proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types), which could have cost and other implications. Check the [Pay-as-you-go entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-entitlements) and [Subscription 2024](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements) for information.   
  
To see the list of extensible policies, see Extensible policies by category.



For [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) users, the types of policies you can use in a proxy depend on the [environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types) you plan to deploy that proxy to. See [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) for more information.

If there are two policies, one standard and one extensible, that would both perform the functions you need, use the standard policy.

## Standard policies by category

Select categoryExtension policiesMediation policiesSecurity policiesTraffic management policies

Following are the categories for the standard policies:

Category | Policy name | Description  
---|---|---  
  
### Extension policies

| 

  * [AssertCondition policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assert-condition-policy)
  * [ExternalCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy)

|  Let you define custom policy functionality, such as service callout and message data collection.   
  
### Mediation policies

| 

  * [CORS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/cors-policy)
  * [GraphQL policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy)
  * [HTTPModifier policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy)
  * [JSONtoXML policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy)
  * [OASValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy)
  * [PublishMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy)
  * [RaiseFault policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/raise-fault-policy)
  * [ReadPropertySet policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy)
  * [SOAPMessageValidation policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-validation-policy)
  * [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy)

|  Let you perform message transformation, parsing, and validation, as well as raise faults and alerts.   
  
### Security policies

| 

  * [AccessControl policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-control-policy)
  * [HMAC policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/hmac-policy)
  * JWT policies: 
    * [DecodeJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/decode-jwt-policy)
    * [VerifyJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jwt-policy)
  * [VerifyIAM policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-iam-policy)

| Let you apply security-related policies.  
  
### Traffic management policies

| 

  * [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy)

|  Let you control quotas and mitigate the effects of API traffic spikes.   
  
## Extensible policies by category

Select categoryAI policiesExtension policiesMediation policiesSecurity policiesTraffic management policies

Following are the extensible policies, by category. Proxies with extensible policies can only be deployed to intermediate and comprehensive environments. Extensible policies are indicated in the user interface with this icon: ![extensible policy icon](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/icon_policy_extensible.png)

Category | Policy name | Description  
---|---|---  
  
### AI policies

| 

  * [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy)
  * [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy)
  * [SemanticCacheLookup policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy)
  * [SemanticCachePopulate policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy)
  * [SanitizeUserPrompt policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)
  * [SanitizeModelResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy)

|  Let you optimize and secure the performance of AI workloads and models.   
  
### Extension policies

| 

  * [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy)
  * [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy)
  * [IntegrationCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy)
  * [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy)
  * [JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy)
  * [MessageLogging policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy)
  * [PythonScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy)
  * [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy)
  * [SetIntegrationRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-integration-request-policy)
  * [TraceCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/trace-capture-policy)

|  Let you define custom policy functionality, such as service callout, message data collection, and calling Java, JavaScript, and Python scripts.   
  
### Mediation policies

| 

  * [AccessEntity policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/access-entity-policy)
  * [AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy)
  * [ExtractVariables policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy)
  * [KeyValueMapOperations policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/key-value-map-operations-policy)
  * [MonetizationLimitsCheck policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/monetization-limits-check-policy)
  * [ParseDialogflowRequest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-dialogflow-request-policy)
  * [ParsePayload policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-payload-policy)
  * [SetDialogflowResponse policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-dialogflow-response-policy)
  * [XSLTransform policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xsl-transform-policy)

|  Let you perform message transformation, parsing, and validation, as well as raise faults and alerts.   
  
### Security policies

| 

  * [BasicAuthentication policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy)
  * [JSONThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy)
  * JWS policies: 
    * [DecodeJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/decode-jws-policy)
    * [GenerateJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jws-policy)
    * [VerifyJWS policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jws-policy)
  * JWT policies: 
    * [GenerateJWT policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy)
  * OAuth v2 policies: 
    * [DeleteOAuthv2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/delete-oauth-v2-info)
    * [GetOAuthv2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy)
    * [OAuthv2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy)
    * [RevokeOAuthv2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/revoke-oauth-v2-policy)
    * [SetOAuth v2 Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-oauth-v2-info-policy)
  * [RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection)
  * [SAMLAssertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy)
  * [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy)
  * [XMLThreatProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy)

|  Let you control access to your APIs with OAuth, API key validation, and other threat protection features.   
  
### Traffic management policies

| 

  * Caching policies: 
    * [InvalidateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/invalidate-cache-policy)
    * [LookupCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy)
    * [PopulateCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy)
    * [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy)
  * [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy)
  * [ResetQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reset-quota-policy)

|  Let you configure caching, control quotas, mitigate the effects of spikes, and perform other functions related to your API traffic.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
