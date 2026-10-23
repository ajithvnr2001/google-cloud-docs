---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview/
title: UI overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:08.918753+00:00
---

# UI overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  UI overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Apigee UI is a graphical user interface that you can use to manage the lifecycle of your APIs. You can use the Apigee UI to develop and deploy your API proxies, trace their execution, view API analytics, and manage other aspects of your Apigee organization and its environments. Access the Apigee UI in the Google Cloud console, making it easier to access and manage Apigee while working with other Google Cloud resources.

Using the Apigee UI, you can:

  * [Build an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy)
  * [Deploy and undeploy API proxies to your cluster](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview)
  * [Create, edit, and delete environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview)
  * [Assign environment-level access control to users](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users)
  * Work with [target servers](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-target-servers), [KVMs](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps), and [shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows)



## Use the Apigee UI

To open the Apigee UI, go to the **Apigee API management** page. 

[Apigee API management](https://console.cloud.google.com/apigee)

**Important usage note:** When using the Apigee UI with advanced data residency, you must use the jurisdictional Google Cloud console. For more information, see [Use the jurisdictional console](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#jurisdictional-console). You can use the jurisdictional console with data residency (at rest only) if your control data location is set to one of the [supported locations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision#locations). 

From the **Overview** page, you can: 

  * Get started as a new Apigee user
  * Test your Apigee runtime
  * View key resource usage metrics
  * Explore Apigee API management features



### Get started as a new Apigee user

If you just are new to Apigee, you can begin your API management journey with quickstart learning options launched from the **Overview** page: 

  * **Begin by deploying your first proxy** : Watch a [video tutorial](https://www.youtube.com/watch?v=79eUi6toj2c) that walks you through the steps required to create and deploy an API proxy. Once you are ready, click **Create new proxy** to get started. **Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 
  * **Start with VS Code** : Follow this step-by-step tutorial to [ Build and deploy your first API proxy locally using Apigee in VSCode](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/get-started).



For more advanced use cases, follow along with step-by-step video walkthroughs showcased in the **Tutorials** section of the page: 

![Tutorials in the Apigee UI Overview page](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/overview-tutorials.png)

### Test your Apigee runtime

If you just completed provisioning a new Apigee organization, use the **Test your Apigee runtime** card to deploy and call a proxy, as described below: 

### Pay-as-you-go organization

If you have a Pay-as-you-go organization: 

  1. Click **Deploy API** to deploy the sample `Hello World` proxy to the `test-env` environment in your new runtime instance. **Note** : The proxy is not fully deployed instantaneously. It can take up to a minute for the proxy to deploy. 
  2. Upon successful deployment, the console displays steps for sending a test request.



### Subscription organization

If you have a Subscription organization: 

  1. Configure DNS to enable external access to your new proxy For more information, see [ Call the proxy with external access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-sample#call-the-proxy-with-external-access).
  2. Click **Deploy API** to deploy the sample `Hello World` proxy to the `default-dev` environment in your new runtime instance. **Note** : The proxy is not fully deployed instantaneously. It can take up to a minute for the proxy to deploy. 
  3. Upon successful deployment, the console displays steps for sending a test request.



### View key resource usage metrics

You can view key usage metrics for your organization at a glance using the **Proxy Usage** and **Environment Usage** cards on the **Overview** page. The cards display the following metrics: 

  * **Proxy Usage** : 
    * **Total proxies created** : The total number of API proxies created, including deployed and undeployed proxies.
    * **Proxies deployed** : The total number of API proxies deployed across all environment(s) in the organization.
    * **Proxy deployment units** : The total number of API proxy and shared flow revisions deployed in your organization. Each deployment per environment, per instance, is counted as one unit.
    * **Proxies and shared flows deployed against limit** : Total number of API proxies and shared flows deployed in the organization, against the limit for your organization type.
    * **Extensible deployment units** : The number of extensible API proxy revisions deployed in your organization. Each deployment per environment, per instance, is counted as one unit.
    * **Standard deployment units** : The number of standard API proxy revisions deployed in your organization. Each deployment per environment, per instance, is counted as one unit.
  * **Environment Usage** : 
    * **Total environments** : The total number of active and inactive environments in the organization.
    * **Active environments** : The total number of environments attached to a minimum of one Apigee instance.

**Note** : If your organization is Apigee hybrid-enabled, only a sub-set of these usage metrics are displayed.

Whether you are a Pay-as-you-go or Subscription customer, this view provides you with a snapshot of key resource usage, as well as shortcuts to other monitoring and identity management resources for your organization, including: 

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)
  * [Cloud Billing](https://docs.cloud.google.com/billing/docs)
  * [Identity and Access Management](https://docs.cloud.google.com/iam/docs)



### Explore Apigee API management features

From the main navigation menu, you can explore the range of Apigee API management features available for your organization, as described in the table below: 

Main navigation menu | Purpose  
---|---  
**Proxy development** | Develop and deploy [ API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies).   
**Distribution** | Make your APIs [available to app developers.](https://docs.cloud.google.com/apigee/docs/api-platform/publish/publishing-overview)  
**Analytics** | [ Analyze](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview) API traffic data.   
**API security** | Identify security threats and vulnerabilities with [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security).  
**API hub** | View and manage your organization's APIs with [API hub (Preview)](https://docs.cloud.google.com/apigee/docs/api-hub/what-is-api-hub).  
**Management** | Manage Apigee [ users and roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview).   
  
### Apigee UI navigation

If you are a long-time Apigee user, you may be accustomed to navigating the previous Apigee UI to perform the tasks you complete most frequently. The current Apigee UI gives you the ability to manage all of your Apigee functionality in one place.

The following table maps each Apigee UI feature page to its current location in the Apigee UI:

**Feature** | **Apigee UI**  
---|---  
**Proxies** | Proxy development > API proxies [Go to API proxies](https://console.cloud.google.com/apigee/proxies)  
**Sharedflows** | Proxy development > Sharedflows [Go to Sharedflows](https://console.cloud.google.com/apigee/sharedflows)  
**Offline debug** | Proxy development > Offline debug [Go to Offline debug](https://console.cloud.google.com/apigee/offline-debug)  
**API products** | Distribution > API products [Go to API products](https://console.cloud.google.com/apigee/apiproducts)  
**Portals** | Distribution > Portals [Go to Portals](https://console.cloud.google.com/apigee/portals)  
**Monetization** | Distribution > Monetization [Go to Monetization](https://console.cloud.google.com/apigee/monetization/ratePlans)  
**Developers** | Distribution > Developers [Go to Developers](https://console.cloud.google.com/apigee/developers)  
**Apps** | Distribution > Apps [Go to Apps](https://console.cloud.google.com/apigee/apps)  
**API monitoring** | Proxy development > API monitoring [Go to API monitoring](https://console.cloud.google.com/apigee/apimonitoring)  
**API metrics** | Analytics > API metrics [Go to API metrics](https://console.cloud.google.com/apigee/analytics/proxy-performance)  
**Developer Engagement** | Analytics > Developer analysis [Go to Developer analysis](https://console.cloud.google.com/apigee/analytics/developer-analysis)  
**Traffic Composition** | Analytics > Developer analysis [Go to Developer analysis](https://console.cloud.google.com/apigee/analytics/developer-analysis)  
**Devices** | Analytics > End user analysis [Go to End user analysis](https://console.cloud.google.com/apigee/analytics/enduser)  
**Geomap** | Analytics > End user analysis [Go to End user analysis](https://console.cloud.google.com/apigee/analytics/enduser)  
**Custom reports** | Analytics > Custom reports [Go to Custom reports](https://console.cloud.google.com/apigee/analytics/custom-reports)  
**Instances** | Management > Instances [Go to Instances](https://console.cloud.google.com/apigee/instances)  
**Data collectors** | Management > Data collectors [Go to Data collectors](https://console.cloud.google.com/apigee/datacollectors)  
**Environments** | Management > Environments [Go to Environments](https://console.cloud.google.com/apigee/environments)  
**Endpoint attachments** | Management > Endpoint attachments [Go to Endpoint attachments](https://console.cloud.google.com/apigee/endpointAttachments)  
**Roles** | Identity and Access Management (IAM) > Roles [Go to Roles](https://console.cloud.google.com/iam-admin/roles)  
**Users** | IAM [Go to IAM](https://console.cloud.google.com/iam-admin/iam)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
