---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/sending-access-token/
title: Sending an access token \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:47.504910+00:00
---

# Sending an access token  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/sending-access-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Sending an access token Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

As an app developer, you need to include an access token in any request to Apigee for a protected resource (an API that is protected with a VerifyAccessToken policy). Note that access tokens are also called _bearer tokens_. 

## Sending an access token in a request

When you put a VerifyAccessToken policy at the front of your API proxy flow, apps must present a verifiable **access token** (also called a _bearer token_) to consume your API. To do this, the app sends the access token in the request as an **Authorization HTTP header**.

For example:
    
    
    $ curl -H "Authorization: Bearer ylSkZIjbdWybfs4fUQe9BqP0LH5Z" http://{org_name}-test.apigee.net/weather/forecastrss?w=12797282
    

Apigee will verify that the access token presented is valid, and then grant access to the API, returning the response to the app that made the request.

## Related information

For information on obtaining an access token, see [Get OAuth 2.0 tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens). 

For information on verifying access tokens, see [Verifying access tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-access-tokens). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
