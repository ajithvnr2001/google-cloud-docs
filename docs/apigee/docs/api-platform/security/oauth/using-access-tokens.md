---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-access-tokens/
title: Verifying access tokens \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:52.336603+00:00
---

# Verifying access tokens  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-access-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Verifying access tokens Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When you call an API proxy on Apigee that has OAuth security, Apigee is responsible for verifying access tokens. Think of Apigee as the gatekeeper -- no API call can pass through that does not have an access token that can be verified. 

**Tip:** When verifying an access token, if you happen to see this error: "Invalid API call as no apiproduct match found", go to this [ Apigee Community article](https://discuss.google.dev/t/oauth2-0-access-token-verification-throws-invalid-api-call-as-no-apiproduct-match-found-error/17064) for details on the cause of this error and steps to correct it. 

## Adding a VerifyAccessToken policy

To configure token verification, place an [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) with the **VerifyAccessToken** operation at the very beginning of the API proxy flow (the beginning of the ProxyEndpoint Preflow). If placed there, access tokens will be verified before any other processing takes place, and if a token is rejected, Apigee stops processing and returns an error back to the client. 

To access the API proxies page using the Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Proxy development** > **API proxies** page.

[Go to API proxies](https://console.cloud.google.com/apigee/proxies)

  2. From the list, select the proxy you wish to protect.
  3. In the proxy details page, click the **Develop** tab.
  4. In the navigation menu, under **Proxy endpoints** , **default** , click **PreFlow**. Typically, the endpoint you want is called **default** , although it is possible to create multiple proxy endpoints. If you do have multiple endpoints, you will probably want to follow these steps to perform token verification on each one. ![Navigation menu](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/preflow_nav.png)
  5. In the proxy flow editor, click control_point **Add policy step**.

![Select PreFlow for an endpoint listed under Proxy Endpoints.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/proxyfloweditor.png)
  6. In the **Add policy step** dialog, select **Create new policy**.
  7. From the policy list, under **Security** , select **OAuth v2.0**.
  8. Optionally, change the policy name and display name. For example, for better readability, you might change the **Display name** and **Name** both to **VerifyAccessToken**.
  9. Click **Add**.



The default policy is already configured with the VerifyAccessToken operation, so you do not have to do anything further:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <OAuthV2 async="false" continueOnError="false" enabled="true" name="OAuth-v20-1">
        <DisplayName>OAuth v2.0 1</DisplayName>
        <FaultRules/>
        <Properties/>
        <Attributes/>
        <ExternalAuthorization>false</ExternalAuthorization>
        <Operation>VerifyAccessToken</Operation>
        <SupportedGrantTypes/>
        <GenerateResponse enabled="true"/>
        <Tokens/>
    </OAuthV2>

**Note:** By default, VerifyAccessToken expects the access token to be sent in an Authorization header as a Bearer token. For example: 
    
    
    -H "Authorization: Bearer Rft3dqrs56Blirls56a"

You can change this default in the `<AccessToken> ` element in the OAuthV2 policy, as explained in the [OAuthV2 policy documentation](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#accesstokenelement).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
