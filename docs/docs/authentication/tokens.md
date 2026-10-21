---
url: https://docs.cloud.google.com/docs/authentication/tokens/
title: Tokens overview \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:22:43.793119+00:00
---

# Tokens overview  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/tokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Tokens overview Stay organized with collections  Save and categorize content based on your preferences. 

This document and the [Token types](https://docs.cloud.google.com/docs/authentication/token-types) document cover the multiple tokens used by Google Cloud for authentication and authorization. They're intended for people who want to learn how token-based authentication works, or who want to implement authentication without using the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).

You don't need to know this information when you interact with Google Cloud APIs using the Cloud Client Libraries, the Google Cloud console, or the Google Cloud CLI—the process of selecting the right type of token, and obtaining and refreshing those tokens is handled automatically for you.

## User authentication

When human users interact with Google Cloud, they don't interact with Google Cloud APIs directly. Instead, they use a _client_ to act on their behalf. The client that they use might be a web application, a desktop application, or a utility like the Google Cloud CLI or `curl`.

Because the client makes requests and not the user, Google Cloud can't request identity information from the user directly to check if they have permission to use an API. Instead, this identity is passed to the API through the client in the form of a token, which is included in each API request.

A user authentication token encodes the following information:

  * The identity of the user.

  * The identity of the client.

  * Assurance that the client is allowed to act on behalf of the user.




Authenticating the user and authorizing the client involves the following parties:

  * A user.

  * A client that acts on behalf of the user.

  * An authorization server, which Google APIs rely on to authenticate the client.

  * A Google Cloud API that the client interacts with.




Clients can't issue tokens themselves. Instead, they must work with an authorization server to do the following:

  1. Authenticate the user.

  2. Authenticate the client.

  3. Authorize the client to act on the user's behalf.

  4. Issue a token to the client.


![A relationship diagram of a user authenticating through a client](https://docs.cloud.google.com/static/docs/authentication/images/user-token.svg) A user who authenticates by signing in to their Google Account is a [_user_ principal](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_identities). The principal has a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers) similar to the following: 
    
    
    user:alex@example.com
    

A user who authenticates using [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) and an external identity provider is a _workforce identity pool_ principal. The principal has a principal identifier similar to the following:
    
    
    principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/raha@altostrat.com
    

## Workload authentication

Some clients need to interact with Google APIs on their own behalf. For example, a scheduled job might need to read data from BigQuery or Cloud Storage without any human user being involved.

Clients that act unattended and on their own behalf are referred to as _workloads_. Unlike user authentication, workload authentication combines authenticating the user and authorizing the client into a single step. Because of this, a workload authentication token encodes the identity of only the client.

Workload authentication and authorization involves the following parties:

  * A workload, acting as both a client and a user, and on its own behalf.

  * An authorization server, which Google APIs rely on to authenticate the client.

  * A Google Cloud API that the client interacts with.




To access Google Cloud APIs, clients must work with an authorization server to do the following:

  1. Authenticate the client.

  2. Authorize the client.

  3. Issue a token to the client.


![A relationship diagram of a workload authenticating through a client](https://docs.cloud.google.com/static/docs/authentication/images/workload-token.svg)

An authenticated workload is also referred to as a principal, but workloads use different principal identifiers than users.

A workload that authenticates using a service account is a [_service account_ principal](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#service_account). The principal has a principal identifier similar to the following:
    
    
    serviceAccount:my-service-account@my-project.iam.gserviceaccount.com
    

A workload that authenticates using [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) is a _workload identity pool_ principal. The principal has a principal identifier similar to the following:
    
    
    principal://iam.googleapis.com/projects/PROJECT_NAME/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE
    

## Authorization servers

Google Cloud shares specific authentication and authorization facilities with other Google services. Shared facilities include [Sign in with Google](https://developers.google.com/identity/siwg), and the [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect) and [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) services provided by [Google Identity](https://developers.google.com/identity).

Other authentication-related services, such as Workload Identity Federation and Workforce Identity Federation, are specific to Google Cloud and can't be used for other Google services.

Because of this split, Google Cloud uses two authorization servers. One is shared with other Google services, and the other is specific to Google Cloud. The following table describes the different servers and their properties.

Authorization server | Authentication type | Authentication APIs | Principals  
---|---|---|---  
Google authorization server | 

  * User authentication
  * Workload authentication

| 

  * [ Google OAuth 2.0 API](https://developers.google.com/identity/protocols/oauth2)
  * [ SAML](https://docs.cloud.google.com/identity-platform/docs/web/saml)

| 

  * User ([managed user](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account)) 
  * User ([consumer account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account)) 
  * [ Service account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#service_account)

  
Google Cloud Identity and Access Management (IAM) authorization server | 

  * User authentication
  * Workload authentication

| 

  * [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) (STS) API 
  * IAM [ Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest)
  * [ Metadata servers](https://docs.cloud.google.com/docs/authentication/get-id-token#metadata-server)

| 

  * [ Workforce identity pool principal](https://docs.cloud.google.com/iam/docs/principals-overview#workforce)
  * [ Workload identity pool principal](https://docs.cloud.google.com/iam/docs/principals-overview#workload)
  * [ Service account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#service_account)

  
  
The authorization servers are global services and can be accessed from any [Google Cloud region](https://cloud.google.com/about/locations). However, not all regions contain deployments of both authorization servers:

  * The Google authorization server is available in select regions.

  * The Google Cloud IAM authorization server is available in all regions.




To optimize reliability, use the Google Cloud IAM authorization server whenever possible. 

## What's next

Read about [token types](https://docs.cloud.google.com/docs/authentication/token-types). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
