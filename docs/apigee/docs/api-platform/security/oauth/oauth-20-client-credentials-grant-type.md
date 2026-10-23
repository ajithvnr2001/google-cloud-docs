---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-20-client-credentials-grant-type/
title: Implementing the client credentials grant type \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:13.449583+00:00
---

# Implementing the client credentials grant type  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-20-client-credentials-grant-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Implementing the client credentials grant type Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

With the client credentials grant type, an app sends its own credentials (the Client ID and Client Secret) to an endpoint on Apigee that is set up to generate an access token. If the credentials are valid, Apigee returns an access token to the client app.

## About this topic

This topic offers a general description of the OAuth 2.0 client credentials grant type and discusses how to implement this flow on Apigee. 

## Use cases

Most typically, this grant type is used when the app is also the resource owner. For example, an app may need to access a backend cloud-based storage service to store and retrieve data that it uses to perform its work, rather than data specifically owned by the end user. This grant type flow occurs strictly between a client app and the authorization server. An end user does not participate in this grant type flow. 

## Roles

Roles specify the "actors" that participate in the OAuth flow. Let's do a quick overview of the client credentials roles to help illustrate where Apigee fits in. For a complete discussion of OAuth 2.0 roles, see the [ IETF OAuth 2.0 specification](https://tools.ietf.org/html/draft-ietf-oauth-v2-31). 

  * **Client App** \-- The app that needs access to the user's protected resources. Typically, with this flow, the app runs on server rather than locally on the user's laptop or device.
  * **Apigee** \-- In this flow, Apigee is the OAuth authorization server. Its role is to generate access tokens, validate access tokens, and pass authorized requests for protected resources on to the resource server. 
  * **Resource Server** \-- The backend service that stores the protected data that the client app needs permission to access. If you are protecting API proxies hosted on Apigee, then Apigee is also the resource server. 



## Code sample

You can find a complete, working [ sample implementation of the client credentials grant type](https://github.com/GoogleCloudPlatform/apigee-samples/tree/main/oauth-client-credentials) on GitHub. See Additional resources below for links to more examples. 

## Flow diagram

The following flow diagram illustrates the client credentials flow with Apigee serving as the authorization server. In general, Apigee is also the resource server in this flow -- that is, API proxies are the protected resources.

![The client credentials flow.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/oauth-client-cred-flow-3.png)  


## Steps in the client credentials flow

Here is a summary of the steps required to implement the client credentials code grant type where Apigee serves as the authorization server. Remember, with this flow, the client app simply presents its client ID and client secret, and if they are valid, Apigee returns an access token.

**Prerequisite:** The client app must be registered with Apigee to obtain the client ID and client secret keys. See [ Registering client apps](https://docs.cloud.google.com/apigee/docs/api-platform/security/registering-client-apps) for details. 

### 1\. Client requests an access token

To receive an access token, the client POSTs an API call to Apigee with the values for client ID and client secret obtained from a registered developer app (in this example, the values are [ Base64-encoded](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens#encodingbasicauthenticationcredentials) and passed in the `Authorization` header. In addition, the parameter `grant_type=client_credentials` must be passed as a query parameter. (However, you can configure the OAuthV2 policy to accept this parameter in the request header or body -- see [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) for details). 

For example:
    
    
    curl -H "Content-Type: application/x-www-form-urlencoded" \
      -H "Authorization: Basic c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ" \
      -X POST "https://apitest.acme.com/oauth/token" \
      -d "grant_type=client_credentials"
    

See also [Use the client credentials grant type](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens#requestinganaccesstokenclientcredentialsgranttype). 

### 2\. Apigee validates the credentials

Note that the API call is sent to the `/oauth/token` endpoint. This endpoint has a policy attached to it that validates the app's credentials. That is, the policy compares the submitted keys with the ones that Apigee created when the app was registered. If you'd like to learn more about OAuth endpoints on Apigee, see [Configuring OAuth endpoints and policies](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/configuring-oauth-endpoints-and-policies). 

### 3\. Apigee returns a response

If the credentials are okay, Apigee returns an access token to the client. If not, an error is returned. 

### 4\. The client calls the protected API

Now, with a valid access token, the client can make calls to the protected API. In this scenario, requests are made to Apigee (the proxy), and Apigee is responsible for validating the access token before passing the API call along to the target resource server. For an example, see Calling the protected API below. 

## Configuring flows and policies

As the authorization server, Apigee processes requests for access tokens. As the API developer, you need to create a proxy with a custom flow to handle token requests and add and configure an OAuthV2 policy. This section explains how to configure that endpoint.

### Custom flow configuration

The easiest way to show how the API proxy flow is configured is to show the XML flow definition. Here's an example API proxy flow designed to process an access token request. For example, when a request comes in and the path suffix matches `/oauth/token`, the GetAccessToken policy is triggered. See [Configuring OAuth endpoints and policies](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/configuring-oauth-endpoints-and-policies) for a quick overview of the steps needed to create a custom flow like this.
    
    
    <Flows>
      <Flow name="GetAccessToken">
             <!-- This policy flow is triggered when the URI path suffix
             matches /oauth/token. Publish this URL to app developers
             to use when obtaining an access token using an auth code
             -->
        <Condition>proxy.pathsuffix == "/oauth/token"</Condition>
        <Request>
            <Step><Name>GetAccessToken</Name></Step>
        </Request>
      </Flow>
    </Flows>

### Configure the flow with a policy

You need to attach a policy to the endpoint, as follows. See [Configuring OAuth endpoints and policies](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/configuring-oauth-endpoints-and-policies) for a quick overview of the steps needed to add an OAuthV2 policy to a proxy endpoint.

#### Get access token

This policy is attached to the `/oauth/token` path. It uses the OAuthV2 policy with the GenerateAccessToken operation specified.
    
    
    <OAuthV2 name="GetAccessToken">
      <Operation>GenerateAccessToken</Operation>
      <ExpiresIn>3600000</ExpiresIn>
      <SupportedGrantTypes>
        <GrantType>client_credentials</GrantType>
      </SupportedGrantTypes>
      <GenerateResponse/>
    </OAuthV2>

The API call to obtain the access token is a POST and includes an Authorization header with the [ Base64-encoded](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens#encodingbasicauthenticationcredentials) `client_id` \+ `client_secret` and the query parameter `grant_type=client_credentials`. It can also include [ optional parameters](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens#requestinganaccesstokenclientcredentialsgranttype-optionalparameters) for scope and state. For example:
    
    
    curl -i \
      -H 'Content-Type: application/x-www-form-urlencoded' \
      -X POST 'https://docs-test.apigee.net/oauth/accesstoken' \
      -d 'grant_type=client_credentials' \
      -H 'Authorization: Basic c3FIOG9vSGV4VHo4QzAySVgT1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ'
    

## Attaching the verify access token policy

To protect your API with OAuth 2.0 security, you need to add an OAuthV2 policy with the VerifyAccessToken operation. This policy checks that incoming requests have a valid access token. If the token is valid, Apigee processes the request. If it is not valid, Apigee returns an error. For the basic steps, see [Verifying access tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-access-tokens). 
    
    
    <OAuthV2 async="false" continueOnError="false" enabled="true" name="VerifyAccessToken">
        <DisplayName>VerifyAccessToken</DisplayName>
        <ExternalAuthorization>false</ExternalAuthorization>
        <Operation>VerifyAccessToken</Operation>
        <SupportedGrantTypes/>
        <GenerateResponse enabled="true"/>
        <Tokens/>
    </OAuthV2>

## Calling the protected API

To call an API that is protected with OAuth 2.0 security, you need to present a valid access token. The correct pattern is to include the token in an Authorization header, as follows: Note that the access token is also referred to as a "bearer token". 
    
    
    $ curl -H "Authorization: Bearer UAj2yiGAcMZGxfN2DhcUbl9v8WsR" \
      http://myorg-test.apigee.net/v0/weather/forecastrss?w=12797282
    

See also [Sending an access token](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/sending-access-token).

## Additional resources

  * Apigee offers online training for API developers, including a course on [API security](https://www.coursera.org/learn/api-security-apigee-gcp), which includes OAuth.
  * [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) \-- Has lots of examples showing how to make requests to the authorization server and how to configure the OAuthV2 policy.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
