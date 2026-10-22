---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/setting-api-key-validation/
title: Setting up API key validation \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:38.052406+00:00
---

# Setting up API key validation  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/setting-api-key-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Setting up API key validation Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can set up API key validation for an API by attaching a policy of type Verify API Key. The only required setting for a [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) is the expected location of the API key in the client request. The API proxy will check the location that you specify, and extract the API key. If the API key is not present in the expected location, then an error is thrown and the request is rejected. API keys can be located in a query parameter, a form parameter, or an HTTP header.

For example, the policy configuration below defines the expected key location as a query parameter named `apikey`. A successful request must present the API key as a query parameter appended to the request, for example,`?apikey=Y7yeiuhcbKJHD790`.

To verify API keys, create the following policy:
    
    
    <VerifyAPIKey name="APIKeyValidation">
      <APIKey ref="request.queryparam.apikey"/>
    </VerifyAPIKey>

This policy can be attached to any API that you need to protect.

Comprehensive documentation of this policy type can be found in the policy reference topic, [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy).

API proxies automatically pass through all HTTP headers and query parameters that are present on the request. Therefore, after the API key has been verified, it's a good idea to strip it from the message so that the API key is not sent over the wire to the backend service. You can do that using a policy of type `AssignMessage` as follows:
    
    
    <AssignMessage name="StripApiKey">
        <DisplayName>Remove Query Param</DisplayName>
        <Remove>
            <QueryParams>
                <QueryParam name="apikey"/>
            </QueryParams>
        </Remove>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
        <AssignTo createNew="false" transport="http" type="request"></AssignTo>
    </AssignMessage>

## Policy attachment

The policies must be attached to an API proxy Flow as processing Steps. By applying the policy to the request `PreFlow`, API keys are verified on every request received by the API proxy from a client app. After verification, the API key is stripped from the outbound request.

Attach the policies to the ProxyEndpoint of the API proxy to be protected as follows:
    
    
    <ProxyEndpoint name="default">
      <PreFlow>
        <Request>
          <Step><Name>APIKeyValidation</Name></Step>
          <Step><Name>StripApiKey</Name></Step>
        </Request>
      </PreFlow>
    

After you attach the policy, deploy the API proxy.

## Submitting a request with a valid API key

As an admin in your organization, you can retrieve any app's API key as follows:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /apps/**$APP** \
      -H "Authorization: Bearer $TOKEN"

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The app profile that is returned for this call provides the consumer key (API key) and secret. The consumer key value is the value you use for the API key in your request to the protected API.

For example, a request that does not include an API key results in an authorization failure.
    
    
    curl http://apitest.examplepetstore.com/weather/forecastrss?w=12797282

The failure message indicates that the policy checked for an API key but did not find a valid key:
    
    
    OAuth Failure : Could not resolve the app key with variable request.queryparam.apikey

When the consumer key for the app is included as a query parameter, the expected result is successful authorization:
    
    
    curl http://apitest.examplepetstore.com/weather/forecastrss?w=12797282&"apikey=PulSCqMnXGchW0pC0s5o9ngHVTWMeLqk"

The expected result is a successful response from the weather service.

Modifying the value of the API key value in the request results in an authorization failure:
    
    
    curl http://apitest.examplepetstore.com/weather?forecastrss?w=12797282&"apikey=PulSCqMnXGchW0"

Results in:
    
    
    OAuth Failure : Consumer Key is Invalid

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
