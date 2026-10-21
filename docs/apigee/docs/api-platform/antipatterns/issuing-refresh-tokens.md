---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/issuing-refresh-tokens/
title: Antipattern: Issuing refresh tokens without invoking refresh flow \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:17.468097+00:00
---

# Antipattern: Issuing refresh tokens without invoking refresh flow  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/issuing-refresh-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Issuing refresh tokens without invoking refresh flow Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/issuing-refresh-tokens) documentation._

Refresh tokens are used to obtain new access tokens after the original access token has expired or been revoked. Refresh tokens are optionally issued along with access tokens with some of the grant types. 

## Antipattern

Refresh tokens can be issued either by Apigee or via external resources. However, this is an antipattern if the refresh token is never used via the RefreshAccessToken operation. 

## Impact

Persisting refresh tokens unnecessarily negatively impacts both performance and reliability of the authentication system. 

## Best practice

### If the refresh token is never needed

If refresh tokens are not needed, developers should use the 'client credentials' or 'implicit' grant types when generating new access tokens. These grant types do not issue refresh tokens, which is desirable if the refresh token functionality is not required. 

### If the proxy performs only read operation with refresh tokens

Apigee offers [ GetOAuthV2Info](https://cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy#refresh-token) which can be used to retrieve refresh token attributes. Developers should not use this policy to validate refresh tokens. It is an antipattern that the refresh token is never used to exchange for a new access token. Note that Apigee can work with [ external access and refresh tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/use-third-party-oauth-system). If the refresh token flow happens outside of Apigee, it's highly recommended to use the RefreshAccessToken operation such that any imported refresh tokens no longer valid are properly removed from the Apigee system. 

## Further reading

[ Refreshing an access token](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens#refreshinganaccesstoken)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
