---
url: https://docs.cloud.google.com/storage/docs/user-accounts/
title: Accessing data on a user's behalf \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:30.921682+00:00
---

# Accessing data on a user's behalf  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/user-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Accessing data on a user's behalf Stay organized with collections  Save and categorize content based on your preferences. 

When your application needs to access data on a user's behalf, this is called a three-legged OAuth flow. In a three-legged OAuth flow, your application obtains credentials from an end user, who signs into their account to complete authentication. Your application then uses the end user's credentials to access Cloud Storage resources on the user's behalf. Here are examples of scenarios where this approach can be used:

  * Web server applications
  * Installed and desktop applications
  * Mobile applications
  * Client-side JavaScript
  * Applications on limited-input devices

For more information on these scenarios, see [OAuth 2.0 scenarios](https://developers.google.com/identity/protocols/OAuth2#scenarios). 

For other scenarios, you might want to use [service account credentials](https://docs.cloud.google.com/iam/docs/service-account-overview#credentials).

If you are designing an application to support multiple authentication options for end users, then use [Firebase Authentication](https://firebase.google.com/docs/auth/), which supports email and password authentication as well as federated sign in with identity providers such as Google, Facebook, Twitter, and GitHub. See [Where do I start with Firebase Authentication](https://firebase.google.com/docs/auth/where-to-start) for details on how to set up authentication systems for different use cases.

When an application is granted an access token by an end user to access data on the user's behalf, that access token only has the permissions available to the user who grants the token. For example, if jane@example.com has `read-only` access to `example-bucket`, an application which Jane has granted `read-write` access to will be unable to write to `example-bucket` on her behalf.

## What's next

  * Learn more about [authentication in Cloud Storage](https://docs.cloud.google.com/storage/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
