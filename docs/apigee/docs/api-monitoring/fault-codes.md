---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/fault-codes/
title: Fault codes \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:21:42.476601+00:00
---

# Fault codes  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/fault-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Fault codes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee provides a set of fault codes for various features that help you to diagnose issues. For example, a typical `4xx` or `5xx` HTTP status code can be classified using one or more fault codes.

Fault codes provide you with useful information about runtime errors, including information about the source and name of the error in the following format: `[prefix].[error_name]`

For example: `steps.raisefault.RaiseFault`

In this example:

  * `steps.raisefault` is the prefix that indicates the RaiseFault policy generated the error.
  * `RaiseFault` is the error name that helps you determine the cause of the error. In this case, more information would be provided by the fault string.

**Notes** : 
    * For policy errors, error-specific flow variables are populated that are useful for fault handling. See [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).
    * When [setting up alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications), fault codes are organized by category and subcategory, and display the human-readable name. When using the [Investigate](https://docs.cloud.google.com/apigee/docs/api-monitoring/investigate) dashboard, the raw fault codes are displayed.




The following table summarizes the fault codes, organized by category and sub-category.

Category | Sub-category | Name | Fault Code   
---|---|---|---  
  
## API protocol

| 

### HTTP

| HTTP BadFormData  | `protocol.http.BadFormData`  
HTTP BadRequestPath  | `protocol.http.BadPath`  
HTTP DuplicateHeader  | `protocol.http.DuplicateHeader`  
HTTP EmptyHeaderName  | `protocol.http.EmptyHeaderName`  
HTTP HeaderNameWithNonASCIICharacter  | `protocol.http.HeaderNameWithNonAsciiChar`  
HTTP HeaderWithInvalidCharacter  | `protocol.http.HeaderWithInvalidChar`  
HTTP InvalidRequestPath  | `protocol.http.InvalidPath`  
HTTP LengthRequired  | `messaging.adaptors.http.flow.LengthRequired`  
HTTP ProxyTunnelCreationFailed  | `protocol.http.ProxyTunnelCreationFailed`  
HTTP RequestHasABigBody  | `[protocol.http.TooBigBody](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#size)`  
HTTP RequestsHaveABigLine  | `protocol.http.TooBigLine`  
HTTP Response306IsReserved  | `protocol.http.Response306Reserved`  
HTTP Response405WithoutAllowHeader  | `protocol.http.Response405WithoutAllowHeader`  
ResponseWithBodyForIncorrectStatusCode  | `protocol.http.ResponseWithBody`  
HTTP TargetURLHasEmptyPath  | `protocol.http.EmptyPath`  
HTTP TooBigHeaders  | `protocol.http.TooBigHeaders`  
HTTP UnsupportedEncoding  | `protocol.http.UnsupportedEncoding`  
  
## Developer/app

| 

### Key Management

| KeyManagement AccessTokenNotApproved  | `keymanagement.service.access_token_not_approved`  
KeyManagement APIProductNotFound  | `keymanagement.service.InvalidAPICallAsNoApiProductMatchFound`  
KeyManagement AppNotApproved  | `keymanagement.service.invalid_client-app_not_approved`  
KeyManagement AppNotApproved  | `keymanagement.service.app_not_approved`  
KeyManagement AuthorizationCodeExpired  | `keymanagement.service.access_denied-authorization_code_expired`  
KeyManagement AuthorizationCodeinvalid  | `keymanagement.service.invalid_request-authorization_code_invalid`  
KeyManagement ClientIDAuthorizationCodeMismatch  | `keymanagement.service.invalid_client-client_id_authorzation_code_mismatch`  
KeyManagement ClientIDNotApproved  | `keymanagement.service.invalid_client-client_id_not_approved`  
KeyManagement CompanyStatusNotActive  | `keymanagement.service.CompanyStatusNotActive`  
KeyManagement Consumer Key Expired  | `keymanagement.service.consumer_key_expired`  
KeyManagement DeveloperNotActive  | `keymanagement.service.DeveloperStatusNotActive`  
KeyManagement InvalidAccessToken  | `keymanagement.service.oauth10_access_token_doesnotexist`  
KeyManagement InvalidClientID  | `keymanagement.service.InvalidClientIdForGivenResource`  
KeyManagement InvalidClientID  | `keymanagement.service.invalid_client-client_id_authorzation_code_mismatch`  
KeyManagement InvalidClientID  | `keymanagement.service.invalid_client-invalid_client_id`  
KeyManagement InvalidConsumerKey  | `keymanagement.service.invalid_consumer_key`  
KeyManagement InvalidRefreshToken  | `keymanagement.service.invalid_refresh_token`  
KeyManagement RefreshTokenExpired  | `keymanagement.service.refresh_token_expired`  
  
## Extension Policy

| 

### JavaCallout

| JavaCallout _errorname_ | See [JavaCallout policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#runtime-errors)  
  
### JavaScript Callout

| JavaScriptCallout _errorname_ | See [JavaScript policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy#runtime-errors)  
  
### MessageLogging

| MessageLogging StepDefinitionExecutionFailed  | `steps.messagelogging.StepDefinitionExecutionFailed`  
  
### Node Script

| NodeScript ExecutionError  | `scripts.node.ScriptExecutionError`  
  
### PythonScript

| PythonScript _errorname_ | See [PythonScript policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy#runtime-errors)  
  
### Script

| Script EvaluationFailed  | `steps.script.ScriptEvaluationFailed`  
  
### ServiceCallout

| ServiceCallout _errorname_ | See [ServiceCallout policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy#runtime-errors)  
  
## Gateway

| 

### Proxy

| Gateway APITimedOut  | `flow.APITimedOut`  
Gateway ApplicationNotFound  | `messaging.adaptors.http.flow.ApplicationNotFound`  
Gateway DecompressionFailureAtRequest  | `messaging.adaptors.http.flow.DecompressionFailureAtRequest`  
Gateway DecompressionFailureAtResponse  | `messaging.adaptors.http.flow.DecompressionFailureAtResponse`  
Gateway KeyAliasNotFound  | `security.util.KeyAliasNotFound`  
Gateway RouteToTargetFailed  | `messaging.runtime.RouteFailed`  
Gateway SharedFlowNotFound  | `flow.SharedFlowNotFound`  
Gateway TargetIsMissing  | `messaging.runtime.TargetMissing`  
  
### Target

| Gateway FailedHandshakeWithTargetEndpoint  | `messaging.adaptors.http.flow.SslHandshakeFailed`  
Gateway TimeoutWithTargetOrCallout  | `messaging.adaptors.http.flow.GatewayTimeout`  
Gateway TargetOrCalloutEndpointsNotAvailable  | `messaging.adaptors.http.flow.ServiceUnavailable`  
Gateway TargetServerConfiguredInLoadBalancerIsDown  | `messaging.adaptors.http.flow.NoActiveTargets`  
Gateway UnexpectedEOFAtTarget  | `messaging.adaptors.http.flow.UnexpectedEOFAtTarget`  
  
### Virtual Host

| VirtualHost InvalidKeystoreOrTrustStore  | `messaging.runtime.SecurityStoreNotConfigured`  
VirtualHost SecurityStoreNotConfigured  | `messaging.runtime.SecurityStoreNotConfigured`  
  
### Other

| Gateway HTTPErrorResponseCode  | `messaging.adaptors.http.flow.ErrorResponseCode`  
  
## Mediation Policy

| 

### AssignMessage

| AssignMessage _errorname_ | See [AssignMessage policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#runtime-errors)  
  
### ExtractVariables

| ExtractVariables _errorname_ | See [ExtractVariables policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/extract-variables-policy#runtime-errors)  
  
### JSONtoXML

| JSONtoXML _errorname_ | See [JSONtoXML policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-xml-policy#runtime-errors)  
  
### KeyValueMap

| KeyValueMap _errorname_ | See [KeyValueMapOperations policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference#keyvaluemapoperationspolicy)  
  
### MessageValidation

| MessageValidation _errorname_ | See [SOAPMessageValidation policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference#soapmessagevalidationpolicy)  
  
### RaiseFault

| RaiseFault RaiseFaultException  | `steps.raisefault.RaiseFault`  
  
### XMLtoJSON

| XMLtoJSON _errorname_ | See [XMLtoJSON policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy#runtime-errors)  
  
### XSLTransformation

| XSLTransformation _errorname_ | See [XSLTransform policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xsl-transform-policy#runtime-errors)  
  
## Monetization

|  | Mint UndefinedProduct  | `mintstep.undefinedProduct`  
  
## Security Policy

| 

### AccessControl

| AccessControl _errorname_ | See [AccessControl policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/error-code-reference#runtime-errors)  
  
### BasicAuthentication

| BasicAuthentication _errorname_ | See [BasicAuthentication policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/basic-authentication-policy#runtime-errors)  
  
### JSONThreatProtection

| JSONThreatProtection _errorname_ | See [JSONThreatProtection policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy#runtime-errors)  
  
### JWT

| JWT _errorname_ | See [JWT policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy#generate-jwt-runtime-errors)  
  
### OAuth

| OAuth _errorname_ | See [OAuth V2 policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#runtime-errors)  
  
### Regex Protection

| RegexProtection _errorname_ | See [RegularExpressionProtection policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection#runtime-errors)  
  
### SAMLAssertion

| SAMLAssertion InvalidKeyStore  | `steps.saml.generate.InvalidKeyStore`  
SAMLAssertion InvalidMediaType  | `steps.saml.generate.InvalidMediaTpe`  
SAMLAssertion InvalidTrustStore  | `steps.saml.validate.InvalidTrustStore`  
SAMLAssertion SAMLAssertionForNotBeforeConditionViolated  | `steps.saml.validate.NotBeforeConditionViolated`  
SAMLAssertion SignatureValidationFailed  | `steps.saml.validate.SignatureValidationFailed`  
SAMLAssertion XPathResolutionFailed  | `steps.saml.validate.XPathResolutionFailed`  
  
### XMLThreatProtection

| XMLThreatProtection _errorname_ | See [XMLThreatProtection policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy#runtime-errors)  
  
## Sense

| 

### Sense

| Sense RaiseFault  | `messaging.runtime.SenseRaiseFault`  
  
## Traffic Mgmt Policy

| 

### Caching

| Caching InvalidExpiryDatForCacheEntry  | `messaging.config.beans.InvalidExpiryDateForCacheEntry`  
  
### ConcurrentRateLimit

| ConcurrentRateLimit ConcurrentRateLimitViolation  | `policies.concurrentratelimit.ConcurrentRatelimitViolation`  
  
### Quota

| Quota _errorname_ | See [Quota policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#runtime-errors)  
  
### Quota or SpikeArrest

| QuotaOrSpikeArrest InvalidMessageWeight  | [policies.ratelimit.InvalidMessageWeight](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#runtime-errors)  
  
### ResetQuota

| ResetQuota _errorname_ | See [ResetQuota policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reset-quota-policy#errorcodes)  
  
### SpikeArrest

| SpikeArrest _errorname_ | See [SpikeArrest policy runtime errors](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#runtime-errors)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
