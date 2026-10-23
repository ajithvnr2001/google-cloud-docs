---
url: https://docs.cloud.google.com/looker/docs/api-getting-started/
title: Getting started with the Looker API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:18.826799+00:00
---

# Getting started with the Looker API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/api-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Getting started with the Looker API Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** As of Looker 22.4, the [Looker API 4.0 is generally available](https://docs.cloud.google.com/looker/docs/api-4-ga). In Looker 23.18, the [Looker API 3.1 has been removed](https://docs.cloud.google.com/looker/docs/api-3x-deprecation).

The Looker API is a secure, "RESTful" application programming interface for managing your Looker instance and fetching data through the Looker data platform. With the Looker API, you can write applications or automation scripts to provision new Looker user accounts, run queries, schedule data deliveries, etc. Just about anything you can do in the Looker application you can do via the Looker API.

## Looker API path and port

Access your Looker instance's API through its API URL.

Your Looker admin can specify an API path by entering it in the [**API Host URL**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url) field on the **Admin > API** page in the following format:
    
    
    https://<instance_name>.cloud.looker.com
    

Your Looker admin may also use the [**API Host URL**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url) field to assign an API path that is different from your Looker server machine name. This is common when your Looker installation is behind a load balancer, for example. In this case, contact your Looker admin for your API path.

If your Looker admin has not specified the **API Host URL** field, Looker uses the default API path. For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Service (AWS) that were created on or after 07/07/2020, the default Looker API path uses port `443`. For Looker instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port `19999`. The default API URL is in the following format:
    
    
    https://<instance_name>.cloud.looker.com:<port>
    

## Client SDKs

You can use the Looker API with any programming language or application environment that can make HTTPS requests and process JSON responses. You can construct Looker API HTTPS requests manually by using curl (or equivalent), by using the Looker Ruby SDK, or by generating a client SDK library for your language of choice. We recommend using an SDK because it takes care of the details of authentication and HTTPS requests for you, so that you can call the Looker API using simple function calls.

You'll find SDK details on our [Looker API SDKs](https://docs.cloud.google.com/looker/docs/api-sdk) documentation page.

## Authentication

Looker authenticates API requests by using an OAuth 2.0 bearer access token in the HTTP authorization header of the request. All Looker API endpoints require a secure HTTPS connection so that the access token will be secure in transit.

The steps for achieving this depend upon whether or not you are using an SDK. Detailed instructions can be found on our [Looker API authentication](https://docs.cloud.google.com/looker/docs/api-auth) documentation page.

## Interactive API documentation

For API reference documentation, the API Explorer extension is available from the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace). For more information, see the [Using the API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) documentation page. If you are a Looker admin, you can also access the API Explorer by clicking the **Use API Explorer** link on Looker's [**API** Admin page](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api).

## Versioning

API stability is an important consideration when building applications. In order to help you understand which endpoints may be changed in the future, and which should remain stable, we mark certain endpoints as being in beta. For more details, see the [Looker API versioning](https://docs.cloud.google.com/looker/docs/api-versioning) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
