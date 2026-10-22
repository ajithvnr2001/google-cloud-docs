---
url: https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview/
title: Cloud OAuth API overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:55.803695+00:00
---

# Cloud OAuth API overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Cloud OAuth API overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud OAuth API (`cloudoauth.googleapis.com`) provides OAuth 2.0 and OpenID Connect (OIDC) token exchange and authentication for [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

The Cloud OAuth API authenticates Google Cloud users. This API lets your applications redirect users to the authorization endpoint (`https://auth.cloud.google/authorize`) to obtain authorization codes. Your applications can then exchange external credentials, authorization codes, or refresh tokens for short-lived OAuth 2.0 access tokens and OIDC ID tokens.

The API is based on the [OAuth 2.0 Token Exchange (RFC 8693)](https://tools.ietf.org/html/rfc8693) and [OAuth 2.0 Authorization Framework (RFC 6749)](https://tools.ietf.org/html/rfc6749) specifications.

## Comparison with Security Token Service

Historically, Google Cloud's [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) (`sts.googleapis.com`) handled token exchange for both Workforce Identity Federation and Workload Identity Federation.

The Cloud OAuth API supports the same token exchanges as Security Token Service but is dedicated to Workforce Identity Federation traffic. This separation isolates workforce token exchanges from workload traffic, which helps prevent cross-service disruptions and lets workforce capacity scale independently of Security Token Service. Depending on your integration status, follow these guidelines:

  * **New integrations** : Redirect users to the authorization endpoint (`https://auth.cloud.google/authorize`) and exchange tokens using the Cloud OAuth API (`cloudoauth.googleapis.com`).
  * **Existing integrations** : If you use Security Token Service (`sts.googleapis.com/v1/oauthtoken` or `sts.googleapis.com/v1/token`), transition to `cloudoauth.googleapis.com`.



## Supported endpoints

The following table lists the endpoints that you use in Cloud OAuth API integrations. Most of these endpoints are organization-scoped (single-tenant) endpoints that provide isolated key management and discovery when your client application and resources are restricted to a single Google Cloud organization.

In the organization-scoped endpoint URLs, replace `ORGANIZATION_ID` with your numeric Google Cloud organization ID:

Endpoint | Method | URL | Description  
---|---|---|---  
**OpenID Connect discovery ** | `GET` |  `https://auth.cloud.google/oidc/organizations/ORGANIZATION_ID/.well-known/openid-configuration` |  Returns the OpenID Connect Discovery 1.0 provider configuration metadata (discovery document) for the organization.   
**Authorization ** | `GET` | `https://auth.cloud.google/authorize` |  Redirects federated users to sign in with their identity provider (IdP) and returns an authorization code to your application's redirect URI.   
**[Token exchange](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens) ** | `POST` |  `https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/token` |  Exchanges authorization codes or refresh tokens for OAuth 2.0 access tokens and OIDC ID tokens.   
**JSON Web Key Set (JWKS) ** | `GET` |  `https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/.well-known/jwks.json` |  Returns the public JSON Web Keys (JWKs) used to verify the signatures of OIDC ID tokens issued for the organization.   
**[User info](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo) ** | `GET` |  `https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/userinfo` |  Retrieves OIDC standard claims, custom directory claims, and group memberships for the authenticated user.   
**[Enterprise groups](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups) ** | `GET` | `https://cloudoauth.googleapis.com/v1/common/groups` |  Retrieves paginated enterprise group memberships for the authenticated user.   
**Important:** The `/.well-known/openid-configuration`, `/.well-known/jwks.json`, `/userinfo`, and `/groups` endpoints are available only for Looker. 

## Authorization endpoint

In an OAuth 2.0 and OIDC authorization code flow, your application redirects federated users to Google Cloud's unified authorization endpoint (`https://auth.cloud.google/authorize`) to sign in with their IdP. After authentication succeeds, the authorization endpoint redirects the user to your application's redirect URI with an authorization code. Your application then exchanges this code for tokens at the [token exchange endpoint](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens).

## OIDC discovery and JWKS endpoints

For Looker OIDC integrations, the Cloud OAuth API provides public, unauthenticated organization-scoped endpoints for client configuration and token verification:

  * **OpenID Connect discovery endpoint** : Provides the [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) provider configuration metadata (discovery document) for the organization. The discovery document includes the organization's `issuer` identifier and endpoint URLs (`authorization_endpoint`, `token_endpoint`, `userinfo_endpoint`, and `jwks_uri`). It also lists the supported scopes, claims, signing algorithms (`RS256`), and Proof Key for Code Exchange (PKCE) code challenge methods (`S256`).
  * **JSON Web Key Set (JWKS) endpoint** : Provides the public [JSON Web Key Set (JWKS)](https://www.rfc-editor.org/rfc/rfc7517) for the organization. Applications use the public JSON Web Keys (JWKs) in the `keys` array to verify the cryptographic signature of an OIDC ID token (`id_token`) issued by the Cloud OAuth API.



In a typical OIDC integration, your application uses these endpoints in the following sequence:

  1. **Fetch the discovery document** : Send a `GET` request to the OpenID Connect discovery endpoint (`/.well-known/openid-configuration`) and read the endpoint URLs (`authorization_endpoint`, `token_endpoint`, `jwks_uri`, and `userinfo_endpoint`).
  2. **Request an authorization code** : Redirect the user to the `authorization_endpoint` (`https://auth.cloud.google/authorize`) to sign in with their IdP and receive an authorization code at your application's redirect URI.
  3. **Exchange the authorization code for tokens** : Send a `POST` request to the `token_endpoint` ([`/token`](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)) to exchange the authorization code for an OAuth 2.0 access token and an OIDC ID token (`id_token`).
  4. **Verify the ID token** : Fetch the organization's public keys from the `jwks_uri` (`/.well-known/jwks.json`) and use them to verify the cryptographic signature of the `id_token`.
  5. **Optional: Retrieve user info** : Send a `GET` request with the access token to the `userinfo_endpoint` ([`/userinfo`](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)) to retrieve additional user profile claims and group memberships.



## What's next

  * [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)
  * [Retrieve user info with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)
  * [Retrieve enterprise groups with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups)
  * [Manage OAuth applications for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app)
  * [Cloud OAuth REST API reference](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
