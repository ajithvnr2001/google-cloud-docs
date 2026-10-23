---
url: https://docs.cloud.google.com/data-studio/community-connector-authorization/
title: Community connector authorization \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:59.084429+00:00
---

# Community connector authorization  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/community-connector-authorization/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Community connector authorization Stay organized with collections  Save and categorize content based on your preferences. 

Community connectors are developed by 3rd parties, not by Google. If you are using a community connector to access data that requires authorization you'll need to provide the proper information to do so. Community connectors can use the methods that are described on this page to authenticate users.

## How community connector authorization works

When you use a community connector, you grant Data Studio permission to interact with that connector on your behalf. In addition, depending on the requirements of that connector, you may be prompted to provide additional credentials to the connector so that it can access your data from the 3rd party service.

Community connectors can use the following authentication methods:

### OAuth 2.0

[OAuth 2.0](https://oauth.net/2/) is the industry-standard protocol for authorization. Community connectors that use OAuth 2.0 present users with an authorization button, letting them access the 3rd party connector's data via that protocol.

### Username and password

Sites that require a username and password can request those using the community connector.

**Important:** The username and password being requested here is not your Google username and password. Be sure you trust the connector developer before supplying your login information.

### API token

Sites may require you to enter an API token as an authentication method. This is a unique identifier supplied by the service to which you are connecting.

### Notes

Data Studio never stores your credentials. Your username and password, or API token, is sent to the community connector, and the connector tells Data Studio whether or not it was valid. From this point on, Data Studio can only ask the connector if you provided the correct credentials, not what the credentials were.

It is your responsibility to know how the community connector uses your information. Consult the connector's documentation for details.

## Revoke your access

To remove your authorization from a community connector:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the [**Data sources**](https://datastudio.google.com/#/navigation/datasources) tab.
  3. Locate the connector's card in the list, then in the upper right of the card, click more_vert **More option**.
  4. Click **Revoke Access**.



## Related resources

[Learn more about community connectors authentication](https://developers.google.com/looker-studio/connector/auth).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
