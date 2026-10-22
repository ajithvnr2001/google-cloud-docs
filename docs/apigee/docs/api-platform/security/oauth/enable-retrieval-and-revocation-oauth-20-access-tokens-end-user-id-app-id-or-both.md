---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/enable-retrieval-and-revocation-oauth-20-access-tokens-end-user-id-app-id-or-both/
title: Revoke OAuth 2.0 access tokens by end user ID, app id, or both \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:51.225179+00:00
---

# Revoke OAuth 2.0 access tokens by end user ID, app id, or both  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/enable-retrieval-and-revocation-oauth-20-access-tokens-end-user-id-app-id-or-both/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Revoke OAuth 2.0 access tokens by end user ID, app id, or both Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can revoke OAuth 2.0 access tokens by end user ID, app ID, or both using the [RevokeOAuthV2](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/revoke-oauth-v2-policy) policy. By end user, we mean the user of the app that is calling the API.

**Warning:** OAuth tokens are cached for three minutes (180 seconds); therefore, a revoked token may still succeed for up to three minutes, until its cache limit expires.

## When to store the user ID in an access token

User IDs are not included in access tokens by default. Sometimes, it is useful to store the user ID in an access token. For example:

  * A feature for your website or app where users can see which third-party apps they have authorized, and to provide an option to revoke access to those apps.
  * A feature that allows an authorized user to revoke all access tokens associated with a specific Developer App.



## About OAuth access tokens

By default, when Apigee generates an OAuth 2.0 access token, the token has the format shown below:
    
    
    {
     "issued_at" : "1421847736581",
    ** "application_name" : "a68d01f8-b15c-4be3-b800-ceae8c456f5a",
    ** "scope" : "READ",
     "status" : "approved",
     "api_product_list" : "[PremiumWeatherAPI]",
     "expires_in" : "3599", //--in seconds
     "developer.email" : "tesla@weathersample.com",
     "organization_id" : "0",
     "token_type" : "BearerToken",
     "client_id" : "k3nJyFJIA3p62DWOkLO6OJNi87GYXFmP",
    ** "access_token" : "7S22UqXGJDTuUADGzJzjXzXSaGJL",
    ** "organization_name" : "myorg",
     "refresh_token_expires_in" : "0", //--in seconds
     "refresh_count" : "0"
    }

Note the following:

  * The application_name field contains the UUID of the app associated with the token. If you enable revocation of OAuth 2.0 access tokens by app ID, then this is the app ID you use.
  * The access_token field contains the OAuth 2.0 access token value.
  * There is no field for end user ID in the default OAuth access token.



To revoke OAuth 2.0 access tokens by end user ID, you have to configure the OAuth 2.0 policy to include the user ID in the token. After you configure the policy to include the end user ID in the token, it is included as the `app_enduser` field, as shown below:
    
    
    {
     "issued_at" : "1421847736581",
    ** "application_name" : "a68d01f8-b15c-4be3-b800-ceae8c456f5a",**
     "scope" : "READ",
    ** "app_enduser" : "6ZG094fgnjNf02EK",**
     "status" : "approved",
     "api_product_list" : "[PremiumWeatherAPI]",
     "expires_in" : "3599", //--in seconds
     "developer.email" : "tesla@weathersample.com",
     "organization_id" : "0",
     "token_type" : "BearerToken",
     "client_id" : "k3nJyFJIA3p62DWOkLO6OJNi87GYXFmP",
    ** "access_token" : "7S22UqXGJDTuUADGzJzjXzXSaGJL",**
     "organization_name" : "myorg",
     "refresh_token_expires_in" : "0", //--in seconds
     "refresh_count" : "0"
    }

## Configuring the policies

To revoke tokens by user ID, you must first configure the OAuth 2.0 policy to add the user ID to the access token. By including end user IDs in access tokens, you will then be able to revoke tokens by end user ID.

To configure the policy to include an end user ID in an access token, you must specify the input variable that contains the end user ID. Use the `<AppEndUser>` tag to specify the variable:
    
    
    <OAuthV2 async="false" continueOnError="false" enabled="true" name="GenerateAccessTokenClient">
      <DisplayName>OAuth 2.0.0 1</DisplayName>
      <ExternalAuthorization>false</ExternalAuthorization>
      <Operation>GenerateAccessToken</Operation>
      <SupportedGrantTypes>
        <GrantType>client_credentials</GrantType>
      </SupportedGrantTypes>
      <GenerateResponse enabled="true"/>
      <GrantType>request.queryparam.grant_type</GrantType>
    ** <AppEndUser>request.header.appuserID</AppEndUser>
    **  <ExpiresIn>960000</ExpiresIn>
    </OAuthV2>

Here is an example `RevokeOAuthV2` policy configured to revoke access by `EndUserId`: 
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <RevokeOAuthV2 continueOnError="false" enabled="true" name="GetOAuthV2Info-1">
        <DisplayName>Get OAuth v2.0 Info 1</DisplayName>
        <EndUserId ref="request.header.appuserID"></EndUserId>
        <Cascade>false</Cascade>
    </RevokeOAuthV2>

See also [Revoke OAuth V2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/revoke-oauth-v2-policy#developer-app-id). 

The following example command generates a token and passes the user ID in `appuserID` header:
    
    
    curl -H "appuserID:6ZG094fgnjNf02EK" \
    -H "Content-Type: application/x-www-form-urlencoded" \
      -H "Authorization: Basic c3FIOG9vSGV4VHo4QzAyg5T1JvNnJoZ3ExaVNyQWw6WjRsanRKZG5lQk9qUE1BVQ" \
      -X POST "https://apitest.acme.com/oauth/token" \
      -d "grant_type=client_credentials"
    

You can pass information as part of a request in other ways. For example, as an alternative, you can:

  * Use a form parameter variable: request.formparam.appuserID
  * Use a flow variable providing the end user ID



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
