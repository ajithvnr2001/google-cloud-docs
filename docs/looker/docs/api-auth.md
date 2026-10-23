---
url: https://docs.cloud.google.com/looker/docs/api-auth/
title: Looker API authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:17.448467+00:00
---

# Looker API authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/api-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker API authentication Stay organized with collections  Save and categorize content based on your preferences. 

You can authenticate requests to the Looker API to access and manage nearly all Looker functionality. Authentication is essential for integrating data and insights into your workflows. It helps ensure your API calls execute with the correct user permissions, so you can securely interact with Looker content, configurations, and users. The authentication process differs based on whether you use a Looker SDK or make direct API calls.

API credentials are always bound to a Looker user account. API requests execute "as" the user associated with the API credentials. Calls to the API will only return data that the user is allowed to see, and modify only what the user is allowed to modify.

To do anything with the Looker API, you'll first need to authenticate to it. The steps you'll need to take depend on whether or not you're using an SDK.

## Authentication with an SDK

This is the recommended method for API authentication:

  1. If you are using a Looker (original) instance, create your API credentials on the [Users page](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to create the API credentials for you.

If you are using a Looker (Google Cloud core) instance, enable management of your API credentials on the [Users page](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to enable API management for you. Once API management is enabled for your user, use your [**Account** page](https://docs.cloud.google.com/looker/docs/user-account) to manage your API keys.

  2. The API credentials that you generated include a client ID and a client secret. You'll need to provide these to the SDK. The instructions for doing so can be found in the [SDK documentation](https://docs.cloud.google.com/looker/docs/api-sdk).




The SDK will then take care of obtaining the necessary access tokens and inserting them into all subsequent API requests.

## Authentication without an SDK

API authentication with an SDK is the recommended method. To authenticate without an SDK:

  1. If you are using a Looker (original) instance, create your API credentials on the [Users page](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to create the API credentials for you.

If you are using a Looker (Google Cloud core) instance, enable management of your API credentials on the [Users page](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) in the Admin section of your Looker instance. If you're not a Looker admin, ask your Looker admin to enable API management for you. Once API management is enabled for your user, use your [**Account** page](https://docs.cloud.google.com/looker/docs/user-account) to manage your API keys.

  2. Obtain a short-term, OAuth 2.0 access token by calling the [`login`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/login) endpoint of the API. You'll need to provide the API credentials that you generated in step 1, which include a client ID and a client secret.

  3. Place that access token into the HTTP authorization header of Looker API requests. An example Looker API request with an authorization header might look like this:
         
         GET /api/4.0/user HTTP/1.1
         Host: test.looker.com
         Date: Wed, 19 Oct 2023 12:34:56 -0700
         Authorization: token mt6Xc8jJC9GfJzKBQ5SqFZTZRVX8KY6k49TMPS8F
         




The OAuth 2.0 access token can be used on multiple API requests, until the access token expires or is invalidated by calling the [`logout`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ApiAuth/logout) endpoint. API requests that use an expired access token will fail with a `401 Authorization Required` HTTP response.

## API interaction with user login settings

Looker API authentication is completely independent of Looker user login. User authentication protocols such as one-time passcodes (OTP, 2FA) and directory authentication (LDAP, SAML, and so on) don't apply to Looker API authentication.

Because of this, deleting a user's information from a user authentication protocol does not delete their API credentials. Using the procedures on the [Deleting Personal User Information](https://docs.cloud.google.com/looker/docs/deleting-personal-user-information) documentation page removes all of a user's personal data from Looker, preventing them from logging in at all, including through the API.

## Managing API credentials

  * Multiple sets of API credentials can be bound to a single Looker user account.
  * API credentials can be created and deleted without affecting the state of the user account.
  * Deleting a Looker user account invalidates all API credentials bound to the user account.
  * The API client secret must be kept private. Avoid storing API client secrets in source code or other places that can be seen by a lot of people.
  * In production, avoid using API credentials bound to Looker admin accounts. Create minimal privilege user accounts specifically for API activities (often called [**service accounts**](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#service-account)) and create API credentials on those accounts. Grant only the permissions needed for the intended API activities.



## Authentication using OAuth

Looker can use the [Cross-Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) protocol to let web applications make calls to the Looker API from outside a Looker instance's domain. See the [Looker API authentication using OAuth](https://docs.cloud.google.com/looker/docs/api-cors) documentation page for information about configuring CORS authentication.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
