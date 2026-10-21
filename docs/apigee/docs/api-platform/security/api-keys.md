---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys/
title: API keys \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:32.457767+00:00
---

# API keys  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API keys Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

An _API key_ (known in Apigee as a _consumer key_) is a string value passed by a client app to your API proxies. The key uniquely identifies the client app.

API key validation is the simplest form of app-based security that you can configure for an API. A client app simply presents an API key with its request, then Apigee checks to see that the API key is in an approved state for the resource being requested. Internally, your proxies use policies to verify API key authenticity.

To support this simplicity, you'll need to do a bit of setup. To support API keys, you'll need to:

  * **Create an Apigee API product** that bundles the API proxies you want to protect using the API key.
  * **Create an Apigee developer app** that represents the client app developer whose app you'll be authenticating. 

In creating the developer app, you specify API products the developer's app will have access to -- and for which it will need to provide an API key.

  * To your proxies (the ones you included in your API product), **add policies** to verify that an incoming API key is valid.



The [Secure an API by requiring API keys](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/secure-calls-your-api-through-api-key-validation) tutorial is a quick way to learn how to control access to an API proxy with an API key.

**Note:** The security associated with API keys is limited. Because API keys can easily be extracted from app code and used to access an API, they work better as unique app identifiers, rather than security tokens. If you're looking for a way to implement security, be sure to see [OAuth home](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home).**Note:** API keys go by many names. You may see them referred to as app keys, developer app keys, consumer keys, or client IDs.**Sample:** A working sample API proxy that enforces API key validation is available in the [API Platform Samples](https://github.com/apigee/api-platform-samples) available on GitHub. You can use the sample API proxy to secure your own API. Locate the API proxy found under `/sample-proxies/apikey`. Modify the TargetEndpoint configuration to point to your URL. Then deploy.

## How API keys work

In Apigee, an API key is referred to as a consumer key. When you register developer apps, Apigee generates a consumer key and secret. Apigee stores the consumer key for future validation. Each consumer key is unique in the organization. The app developer embeds the consumer key in the client app. The client app must present the consumer key for each request. API Services verifies the consumer key before permitting the app's request.

### High-level steps

The following steps describe how API keys are used by Apigee. These steps include the possible presence of OAuth security as well, since it is often used in conjunction with API keys.

  1. **Create an API product** that includes API proxies that should be protected with the API key.
  2. You **register a developer app** in your organization. When you do Apigee generates a consumer key and a consumer secret.
  3. **Associate the developer app with at least one API product**. It is the product that associates resource paths and API proxies with key approval.
  4. At run time, when the client app makes a request to your API, the **client app sends the consumer key when making the request**. In practice, the consumer key might be either passed explicitly or it might be implicitly referred to via an OAuth token: 
     * When the API uses API key verification -- such as by implementing a VerifyAPIKey policy \-- the client app must pass the consumer key explicitly.
     * When the API uses OAuth token verification -- such as by implementing an OAuthV2 policy \-- the client app must pass a token that has been _derived from_ the consumer key.
  5. The **API Proxy validates the request** credentials through either a VerifyAPIKey policy or an OAuthV2 policy with a VerifyAccessToken operation. If you do not include a credential enforcement policy in your API Proxy, any caller can successfully invoke your APIs. For more information, see [Verify API Key policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy).



### Verifying request credentials

This is an overview. Be sure to see [Setting up API key validation](https://docs.cloud.google.com/apigee/docs/api-platform/security/setting-api-key-validation) for details and code examples.

  1. If you're using OAuth token verification -- you've implemented an OAuth policy to verify and the client app has passed an OAuth token: 
     * Apigee verifies that the token is not expired, and then looks up the consumer key that was used to generate the token.
  2. If you're using an API key -- you've implemented a VerifyAPIKey policy and the client app has passed its consumer key: 
     1. Apigee checks the list of API Products with which the consumer key has been associated.
     2. Apigee checks each API Product to see if the current API Proxy is included in the API Product, and if the current resource path (url path) is enabled on the API Product.
     3. Apigee also verifies that the consumer key is not expired or revoked, checks that the app is not revoked, and checks that the developer is not inactive.
     4. If all of those things are true -- the token is not expired (if applicable), the consumer key is valid and approved, the app is approved, the developer is active, the proxy is available in the product, and the resource is available on the product -- the credential verification succeeds.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
