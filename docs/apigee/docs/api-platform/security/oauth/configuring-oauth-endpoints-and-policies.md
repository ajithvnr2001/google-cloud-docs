---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/configuring-oauth-endpoints-and-policies/
title: Understanding OAuth endpoints \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:41.539162+00:00
---

# Understanding OAuth endpoints  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/configuring-oauth-endpoints-and-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Understanding OAuth endpoints Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

To do its job as an OAuth2 authorization server, Apigee needs to expose endpoints where clients can request tokens and auth codes. This topic offers a quick introduction to these endpoints, and shows you how to set them up in Apigee.

## What is an OAuth2 endpoint?

An OAuth2 endpoint is a URL that clients call to request OAuth tokens (or auth codes). Here's an example request for an access token:
    
    
    $ curl -i -H "ContentType: x-www-form-urlencoded" \
    -X POST "https://apitest.acme.com/oauth/client_credential/accesstoken" \
    -d "grant_type=client_credentials" \
    -H "Authorization: Basic c3FIOG9vSGV4VHo4QzAySVg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ"
    

You need an OAuthV2 policy to process this request. As you can infer from the above example request, the policy must support the "client credentials" grant type, and execute on the path `/oauth/client_credentials/accesstoken`.

This is a sample OAuthV2 policy that is configured to accept the `client_credentials` grant type. For information on optional configuration elements that you can configure with this policy, see [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy).
    
    
    <OAuthV2 name="GenerateAccessToken">
        <Operation>GenerateAccessToken</Operation>
        <ExpiresIn>1800000</ExpiresIn> <!-- 30 minutes -->
        <SupportedGrantTypes>
          <GrantType>client_credentials</GrantType>
        </SupportedGrantTypes>
        <GenerateResponse enabled="true"/>
    </OAuthV2>

Here's a sample endpoint configuration for generating an access token. It'll execute the GenerateAccessToken policy, which must be configured to support the client_credentials grant type.
    
    
    ...
           <Flow name="generate-access-token">
                <Request>
                    <Step>
                        <Name>GenerateAccessToken</Name>
                    </Step>
                </Request>
                <Response/>
                <Condition>(proxy.pathsuffix MatchesPath "/token") and (request.verb = "POST")</Condition>
            </Flow>
    ...

If the client provides the correct credentials, the policy generates and returns a token; otherwise, it returns an error.

## Related topics

For detailed information on all of the supported grant types and sample code, see [Get OAuth 2.0 tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
