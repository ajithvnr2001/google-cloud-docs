---
url: https://docs.cloud.google.com/api-keys/docs/overview/
title: API Keys Overview \u00a0|\u00a0 API Keys API Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:52.426387+00:00
---

# API Keys Overview  |  API Keys API Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-keys/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage/docs)
  * [ API Keys API Documentation ](https://docs.cloud.google.com/api-keys/docs)
  * [ Guides ](https://docs.cloud.google.com/api-keys/docs/how-to)



Send feedback 

#  API Keys Overview Stay organized with collections  Save and categorize content based on your preferences. 

An API key is a simple encrypted string that you can use when calling Google Cloud APIs. A typical use of an API key is to pass the key into a REST API call as a query parameter with the following format:
    
    
    http://example-library.googleapis.com/v1/publishers/mypublisher/books?key=API_KEY

API keys are useful for accessing public data anonymously, and are used to associate API requests with the consumer Google Cloud project for [quotas](https://docs.cloud.google.com/docs/quotas/overview) and [billing](https://docs.cloud.google.com/billing/docs). 

API Keys provides you a programmatic interface to create and manage API keys for your project. It provides you more control over API keys than the API key-related tasks that you can do [in the Google Cloud console](https://docs.cloud.google.com/docs/authentication/api-keys).

To learn more about authenticating to Google Cloud APIs and to determine the best authentication strategy for common scenarios, see [Authentication overview](https://docs.cloud.google.com/docs/authentication). To learn more about using API keys for Google Maps Platform APIs and SDKs, see the [Google Maps Platform documentation](https://developers.google.com/maps/api-key-best-practices). 

## Securing an API key

When you use API keys in your applications, ensure that they are kept secure during both storage and transmission. Publicly exposing your credentials can result in your account being compromised, which could lead to unexpected charges on your account. To help keep your API keys secure, follow these best practices:

  * Do not embed API keys directly in code. API keys that are embedded in code can be accidentally exposed to the public. For example, you may forget to remove the keys from code that you share. Instead of embedding your API keys in your applications, store them in environment variables or in files outside of your application's source tree.

  * [Add restrictions on the API key](https://docs.cloud.google.com/api-keys/docs/add-restrictions-api-keys). By adding restrictions, you can reduce the impact of a compromised API key.

  * Delete unneeded API keys to minimize exposure to attacks.

  * Rotate your API keys periodically. To rotate your API keys, [call the `CreateKey` method](https://docs.cloud.google.com/api-keys/docs/create-manage-api-keys#create). After the replacement keys are created, update your applications to use the newly-generated keys and delete the old keys.

  * Review your code before publicly releasing it. Ensure that your code does not contain API keys or any other private information before you make your code publicly available.




## What's next

  * [Why and when to use API keys](https://docs.cloud.google.com/endpoints/docs/openapi/when-why-api-key)


  * [Get started using the API Keys](https://docs.cloud.google.com/api-keys/docs/get-started-api-keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
