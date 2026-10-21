---
url: https://docs.cloud.google.com/apigee/docs/apihub/plugins/
title: Plugins overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:42:55.258519+00:00
---

# Plugins overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Plugins overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

## Plugins

Plugins enable API hub to connect and ingest API metadata from various Google Cloud services and API gateways where your APIs are managed or defined. They simplify and enhance the process of bringing your API metadata directly into API hub. 

Plugins serve as the underlying framework or capability that allows API hub to understand and integrate with different API management platforms and sources. They define how API hub can connect to a particular data source. 

## Plugin instances

A _plugin instance_ represents a configured and active connection between API hub and a specific API data source, facilitated by its associated plugin. It stores the unique configuration details required to connect to the data source, including connection credentials, [curation](https://docs.cloud.google.com/apigee/docs/apihub/curations) settings, and any data import schedules. Each plugin instance serves as the entry point for collecting API metadata from its designated source. 

Plugin instances are the configured deployments of a plugin. The actual ingestion of data and the registration of APIs as API resources in API hub is managed through plugin instances. Each instance serves as an active entry point for metadata collection from its designated source. 

Depending on the source, plugin instances are created in the following ways: 

  * **Automatic creation:** When you associate a Google Cloud runtime project with API hub, API hub automatically creates a plugin instance in the background for that specific gateway service. For more information, see [Auto-register APIs](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apis).
  * **Manual creation:** For third-party and custom gateways, you can explicitly create plugin instances that establish a configured connection to your gateways to manually bring in metadata. For more information, see [Create plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances) and [Create custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/create-custom-plugins).



## Plugin types and supported API sources

The following plugin types are supported in API hub: 

Plugin type  |  Description  |  Supported API sources  |  **Google Cloud plugins** |  These plugins are created and maintained by API hub to integrate with specific Google Cloud services and gateways. Plugin instances for these plugins are created automatically when you associate a Google Cloud runtime project with API hub. For more information, see [Manage project associations](https://docs.cloud.google.com/apigee/docs/apihub/manage-project-associations). **Note:** Plugin cards for these plugin are not displayed in the **API hub > Settings > Plugins** page.  | 

  * Apigee and Apigee hybrid
  * API Gateway

  
---|---|---  
**Third-party plugins** |  These plugins enable you to connect with third-party gateways and bring your API metadata to API hub. You can create and manage plugin instances for these plugins from the **API hub > Settings > Plugins** page. For more information, see [Create plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances).  | 

  * Apigee Edge Public Cloud
  * Apigee Edge Private Cloud (OPDK)
  * AWS API Gateway (Preview)
  * Azure API Management (Preview)

  
**Custom plugins** |  These plugins enable you to connect with your custom on-premises or multi-cloud to API hub. You can create and manage plugin instances for these plugins from the **API hub > Settings > Plugins** page. For more information, see [Create custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/create-custom-plugins).  | 

\- 
  
  
## Plugin data ingestion methods

The following data ingestion methods are available for plugins:

**Deprecated:** Pull-based ingestion is no longer supported for Apigee and Apigee hybrid plugins as of **July 31, 2025**. For existing projects that have pull-based Apigee and hybrid plugins configured, these plugins will continue to function and will be automatically migrated to the push-based type starting **August, 2025**. 

  * **Push-based ingestion:** the connected data source actively sends (pushes) API metadata updates to API hub as changes occur. This method allows for more real-time synchronization of API metadata. All new **Apigee, Apigee hybrid, Apigee Edge Public Cloud, and Apigee Edge Private Cloud** plugins are created with push-based ingestion by default. 

For the **AWS API Gateway** and **Azure API Management** plugins, push-based ingestion is optional and complements the default scheduled pull sync. To use this feature, deploy a customer-managed AWS Lambda or Azure Function to relay control-plane change events to API hub in near real time. For sample deployment code, see the setup instructions in [Manage third-party plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-third-party-plugins). 

  * **Pull-based ingestion:** API hub periodically polls the connected data source to retrieve API metadata. The **AWS API Gateway** and **Azure API Management** plugins use pull-based ingestion by default, running a full metadata sync every 6 hours. 



## What's next

  * Learn about [creating custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/create-custom-plugins).
  * Learn about [managing custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-custom-plugins).
  * Learn about [creating plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances).
  * Learn about [managing plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances).
  * Learn about [curations](https://docs.cloud.google.com/apigee/docs/apihub/curations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
