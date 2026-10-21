---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth
title: Package com.google.appengine.api.oauth (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:38:30.838913+00:00
---

# Package com.google.appengine.api.oauth (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.oauth (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a method for clients to access server resources on behalf of a resource owner, as well as a process for end-users to authorize third-party access to their server resources without sharing their credentials. See Also: [com.google.appengine.api.oauth.OAuthService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthService), [The OAuth Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/oauth/).

## Classes 

### [IOAuthServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.IOAuthServiceFactoryProvider)

Factory provider for [IOAuthServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.IOAuthServiceFactory).

**Note:** This class is not intended for end users.

### [OAuthServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthServiceFactory)

Creates an OAuthService.

## Interfaces 

### [IOAuthServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.IOAuthServiceFactory)

Creates an OAuthService.

### [OAuthService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthService)

The OAuthService provides methods useful for validating OAuth requests. See Also: [RFC 5849](http://tools.ietf.org/html/rfc5849) for the OAuth specification.

## Exceptions 

### [InvalidOAuthParametersException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.InvalidOAuthParametersException)

`InvalidOAuthParametersException` is thrown when a request is a malformed OAuth request (for example, it omits a required parameter or contains an invalid signature).

### [InvalidOAuthTokenException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.InvalidOAuthTokenException)

`InvalidOAuthTokenException` is thrown when a request contains an invalid OAuth token (for example, a token that has been revoked by the user).

### [OAuthRequestException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthRequestException)

`OAuthRequestException` is thrown when a request is not a valid OAuth request.

### [OAuthServiceFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.oauth.OAuthServiceFailureException)

`OAuthServiceFailureException` is thrown when any unknown error occurs while communicating with the OAuth service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
