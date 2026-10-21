---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api/
title: Manager API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:52:05.450640+00:00
---

# Manager API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/manager-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Manager API Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides a number of API endpoints to support integration with the platform. The manager API extends features related to the settings and configuration of the system as well as events and activities.

The manager API endpoints fall into a one of a few groupings:

  * **Agent** : individual agent resources

  * **Agent activity** : whenever an agent widget changes user status or receives a notification

  * **Campaigns** : the events associated with the outbound dialer

  * **Calls** : a single call resource

  * **Chats** : a single chat resource

  * **Emails** : a single email resource

  * **Menu** : the queues that agents are assigned to and that end users access to receive support from an agent.

  * **Team** : the teams that an agent belongs to

  * **User status** : individual statuses that the agent widget can be in




## Basic authentication

Requests use basic authentication. To create API credentials, follow these steps:

  1. Go to the CCAI Platform portal.

  2. Go to **Settings > Developer Settings > API Credentials**.

  3. Add a new API credentials and provide a name.


**Note:** The API key that you provide can't be retrieved later. Be sure to store it securely.

The credentials for API calls are as follows:

  * The subdomain is used as the `{username}` variable.

  * The token is used as the`{​password}` variable.




Every installation has its own subdomain. To find the subdomain, locate the URL in your browser. It should look similar to the following:

`https://customer.uc1.ccaiplatform.com`

Substitute the subdomain (`customer`, in this example) for the `\{subdomain\​}` variable. Substitute the remainder of the URL (`rest.of.url.com`, in this example) for the `\{domain\}` variable.

## Base URL

The API uses the following base URL for all of its API requests

`https://{subdomain}.{domain​}/apps/api/v1`

where a mention to `/calls` means `https://{subdomain​}.​{domain​}/manager/api/v1/calls`

## Rate Limits

The system limits requests to a rate of 10 request per second per customer.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
