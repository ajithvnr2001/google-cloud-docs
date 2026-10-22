---
url: https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview/
title: Cloud OAuth API overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:19.134774+00:00
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

This document describes the Cloud OAuth API (`cloudoauth.googleapis.com`), which provides OAuth 2.0 and OpenID Connect (OIDC) token exchange and authentication for [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

The Cloud OAuth API authenticates Google Cloud users. Applications can exchange external credentials or authorization codes for short-lived OAuth 2.0 access tokens.

The API is based on the [OAuth 2.0 Token Exchange (RFC 8693)](https://tools.ietf.org/html/rfc8693) and [OAuth 2.0 Authorization Framework (RFC 6749)](https://tools.ietf.org/html/rfc6749) specifications.

## Comparison with Security Token Service

Historically, Google Cloud's [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) (`sts.googleapis.com`) handled token exchange for both Workforce Identity Federation and Workload Identity Federation.

The Cloud OAuth API supports the same token exchanges as Security Token Service but is dedicated to Workforce Identity Federation traffic. This separation isolates workforce token exchanges from workload traffic, helping prevent cross-service disruptions and allowing workforce capacity to scale independently of Security Token Service. Depending on your integration status, follow these guidelines:

  * **New integrations** : Use the Cloud OAuth API (`cloudoauth.googleapis.com`).
  * **Existing integrations** : If you use Security Token Service (`sts.googleapis.com/v1/oauthtoken` or `sts.googleapis.com/v1/token`), transition to `cloudoauth.googleapis.com`.



## Organization-scoped endpoint

The Cloud OAuth API provides the organization-scoped (single-tenant) endpoint: `https://cloudoauth.googleapis.com/v1/organizations/ORGANIZATION_ID/token`

Use this endpoint when your application and resources are restricted to a single Google Cloud organization, providing isolated key management and discovery. Replace `ORGANIZATION_ID` with your numeric Google Cloud organization ID.

## Supported endpoints

The Cloud OAuth API provides the following endpoints:

Endpoint | Method | Path | Description  
---|---|---|---  
**[Token exchange](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)** | `POST` | `/v1/organizations/ORGANIZATION_ID/token` | Exchanges authorization codes or refresh tokens for OAuth 2.0 access tokens and ID tokens.  
**[User info](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)** | `GET` | `/v1/organizations/ORGANIZATION_ID/userinfo` | Retrieves OIDC standard claims for the authenticated user.  
**[Enterprise groups](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups)** | `GET` | `/v1/common/groups` | Retrieves paginated enterprise group memberships for the authenticated user.  
**Important:** The `/userinfo` and `/groups` endpoints are available only for Looker. 

## What's next

  * [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)
  * [Retrieve user info with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)
  * [Retrieve enterprise groups with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups)
  * [Manage OAuth applications for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app)
  * [Cloud OAuth REST API reference](https://docs.cloud.google.com/iam/docs/reference/cloudoauth/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
