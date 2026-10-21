---
url: https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens/
title: Exchange tokens with the Cloud OAuth API \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:00.163500+00:00
---

# Exchange tokens with the Cloud OAuth API  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Exchange tokens with the Cloud OAuth API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide describes how to exchange external credentials, authorization codes, or refresh tokens for Google Cloud access tokens by using the Cloud OAuth API (`cloudoauth.googleapis.com`) in [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) integrations.

## Before you begin

  1. Configure a workforce identity pool and provider. For more information, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).
  2. Register an OAuth client and create client credentials. For more information, see [Manage OAuth applications](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app).
  3. Enable the Cloud OAuth API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudoauth.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Authentication methods

The Cloud OAuth API supports two client authentication methods:

  * **HTTP Basic authentication (recommended)** : Pass the Base64-encoded client ID and client secret in the `Authorization` header:
        
        -H "Authorization: Basic $(echo -n 'CLIENT_ID:CLIENT_SECRET' | base64)"
        

  * **Request body parameters** : Pass the `client_id` and `client_secret` parameters in the request body.


**Note:** Use only one authentication method per request. Combining multiple authentication methods returns an error. JWT bearer token client assertions (`client_assertion`) are not supported. 

## Exchange an authorization code for tokens

To exchange a Google Cloud authorization code for an access token and a refresh token, send an HTTP `POST` request:

  * **Organization-scoped (single-tenant) endpoint**
        
        curl -X POST https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/token \
        -H "Authorization: Basic BASE64_ENCODED_CREDENTIALS" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "grant_type=authorization_code" \
        --data-urlencode "code=AUTHORIZATION_CODE" \
        --data-urlencode "redirect_uri=REDIRECT_URI"
        

**Request body credentials**
        
        curl -X POST https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/token \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "grant_type=authorization_code" \
        --data-urlencode "code=AUTHORIZATION_CODE" \
        --data-urlencode "redirect_uri=REDIRECT_URI" \
        --data-urlencode "client_id=CLIENT_ID" \
        --data-urlencode "client_secret=CLIENT_SECRET"
        




Replace the following:

  * `BASE64_ENCODED_CREDENTIALS`: the Base64-encoded string of `CLIENT_ID:CLIENT_SECRET`.
  * `AUTHORIZATION_CODE`: the authorization code issued by Google Cloud.
  * `REDIRECT_URI`: the redirect URI configured on your OAuth client.
  * `ORGANIZATION_ID`: your numeric Google Cloud organization ID.
  * `CLIENT_ID`: your registered OAuth client ID.
  * `CLIENT_SECRET`: your OAuth client secret.



## Refresh an access token

When an access token expires, use the `refresh_token` grant type to obtain a new short-lived access token:

  * **Organization-scoped (single-tenant) endpoint**
        
        curl -X POST https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/token \
        -H "Authorization: Basic BASE64_ENCODED_CREDENTIALS" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "grant_type=refresh_token" \
        --data-urlencode "refresh_token=REFRESH_TOKEN" \
        --data-urlencode "redirect_uri=REDIRECT_URI"
        




Replace `REFRESH_TOKEN` with the refresh token that the token endpoint previously returned.

## Token response fields

When a token exchange succeeds, the Cloud OAuth API returns an HTTP `200 OK` status containing the following fields:

Field | Type | Description  
---|---|---  
`access_token` | `string` | The OAuth 2.0 access token issued by the Cloud OAuth API to call Google Cloud APIs.  
`refresh_token` | `string` | The refresh token used to obtain new access tokens when the current token expires.  
`expires_in` | `integer` | The remaining lifetime of the access token in seconds (typically `3599`).  
`token_type` | `string` | The token type (for example, `Bearer`).  
`scope` | `string` | The list of scopes associated with the token.  
`id_token` | `string` | The OIDC ID token containing authenticated identity claims.  
  
For information about error responses returned by the Cloud OAuth API, see [Cloud OAuth API token exchange errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#cloud-oauth-api-errors).

## What's next

  * [Retrieve user info with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)
  * [Retrieve enterprise groups with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups)
  * [Cloud OAuth API overview](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview)
  * [Manage OAuth applications for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app)
  * [Cloud OAuth REST API reference](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
