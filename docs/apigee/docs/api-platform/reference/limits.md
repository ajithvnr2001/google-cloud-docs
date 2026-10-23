---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits/
title: Limits \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:09.977190+00:00
---

# Limits  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Limits Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Consider the following product configuration limits as you build, manage, and review your API program implementation. We've designed the Apigee product for stability and performance when configured within these limits. Customers are responsible for tracking and ensuring they stay within the configuration limits. Customers exceeding the limits may experience one or more of these types of symptoms: high API latencies, low API throughput, and failing API calls. Customers filing support cases related to issues caused by limit exceptions may be asked to make necessary modifications to their configuration.

Limits may or may not be enforced automatically (see the **Currently enforced?** column below). As and when we automate limit enforcement for a limit currently not enforced, we will use commercially reasonable efforts to notify affected customers so they can take corrective actions in advance of such enforcement.

Some limits differ between Apigee and Apigee hybrid. The limits can also differ based on your Apigee subscription type. If you are using Apigee hybrid, the higher limits enabled by Subscription 2024 require a newly provisioned using hybrid version 1.14. or later. See [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/enhanced-proxy-limits) for details.

**Note:** This page describes _technical configuration limits_. Enforced limits are fixed and cannot be changed or increased for individual organizations or environments. Organization entitlement terms apply to all usage; exceeding entitlement limits can increase costs, even if usage is within the limits described on this page. See [Apigee Pricing](https://cloud.google.com/apigee/pricing) for details and pricing options.

Feature area | Limit | Apigee  
Currently enforced? | Apigee hybrid  
Currently enforced?  
---|---|---|---  
  
### **Apigee APIs**  
  
**User, service account, or Apigee UI initiated** | 6,000 per minute | Yes | Yes  
**Invoked by synchronizer** | 1,000 per minute | N/A | Yes  
**Invoked by UDCA** | 6,000 per minute | N/A | Yes  
  
### **Message logging**  
  
**Message logging payload** **Note:** [ The Cloud Logging limit](https://docs.cloud.google.com/logging/quotas#log-limits) is 256 KB.  | 11 MB | Planned | Planned  
  
### **API Proxies**  
  
**API proxy or shared flow zip file bundle size** | 15 MB | Yes | Yes  
**API proxy revisions** retained in history | 250 | Yes | Yes  
**API proxy shared flow revisions** retained in history | 250 | Yes | Yes  
**API proxy[resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) size** (such as XSL, JavaScript, Python, or JAR files).  | 15 MB | Yes | Yes  
**Deployed API proxies and shared flows per organization** |  **Apigee** : 6000 **Apigee hybrid** : 4,250 (Subscription 2021) **Apigee hybrid** : 6,000 (Subscription 2024) **Pay-as-you-go** : varies | Yes | Yes  
**Deployed proxies per environment** |  **Apigee** : 6,000 **Apigee hybrid** : 50  
(Subscription 2021) **Apigee hybrid** : 6,000 (Subscription 2024) **Pay-as-you-go** : varies | Yes | Yes  
**Deployed shared flows per environment** |  **Apigee** : 75 **Apigee hybrid** : 10  
(Subscription 2021) **Apigee hybrid** : 75  
(Subscription 2024) **Pay-as-you-go** : varies | Yes | Yes  
**Deployments perinstance** | 6,000 | Yes | Yes  
**API proxy endpoints per API proxy** **Best practice:** Implement a 1:1 ratio of API proxy endpoints to API proxy configuration where possible.Check usage:  
[/apis/revisions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions/get)  
[examine proxy bundle](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-apiproxyproxiesdefaultxml) | 10 | Yes | Yes  
**[Environment-scoped resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) per environment** | 100 | Yes | Yes  
**Maximum number of flows per API proxy** |  200 The proxy editor will not [ display the graph](https://docs.cloud.google.com/apigee/docs/api-platform/release-notes#November_17_2025) if the number of flows exceeds this limit. | Yes | Yes  
  
### **Quota**  
  
[Distributed quota synchronization interval](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#asynchronousconfiguration) | >= 10 seconds | Yes | Planned  
**Max Quota Interval** | 1 year  | Planned | Planned  
**Min Quota Interval** | 1 minute | Planned | Planned  
  
### **SpikeArrest**  
  
**[`Rate`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy#rate)** | Per second maximum: 4,000  
Per minute maximum: 240,000 | Planned | Planned  
  
### **Persistence: Cache, KVM, Property sets**  
  
**Caches at the environment scope** | 100 | Planned | Planned  
**Cache key size** | 2 KB | Yes | Planned  
**Cache value size** | 256 KB | Yes | Planned  
**Cache expiration** | >=1 second, <= 30 days | Yes | Yes  
**Cache resource deletion rate** | 1 per minute | Yes | Planned  
**Items in cache** | 10 million in each cache | Planned | Planned  
**Items in KVMs** across all KVMs in the organization | 5 million | Planned | Planned  
**Key Value Maps (KVMs)** at the organization scope | 100 | Planned | Yes  
**Key Value Maps (KVMs)** at the environment scope | 900 | Planned | Planned  
**Key Value Maps (KVMs)** at the proxy scope | 4,250 or 6,000 (the maximum number of API proxies that can be deployed in an organization) | Planned | Planned  
**Key Value Map (KVM) key size** | 2 KB | Planned | Planned  
**Key Value Map (KVM) value size** | 10 KB | Planned | Planned  
**Environment-scoped property sets per environment** | 10 | Planned | Planned  
**Proxy-scoped property sets per environment** | 50 | Planned | Planned  
**Size of property set file** | 110 KB | Planned | Planned  
  
### **Keys, Developers, Apps**  
  
**Consumer key (API key) size** | 2 KB | Yes | Planned  
**Consumer secret size** | 2 KB | Yes | Planned  
**Custom attributes** you can set on developers, developer apps, API products, OAuth access tokens, and other Apigee entities **Note:** Within an API product, the maximum custom attribute count for proxies, proxy operation groups, gRPC operation groups, and GraphQL operation groups is 3 attributes each. | 18  | Yes | Yes  
**Custom attribute name size** | 1 KB | Yes | Planned  
**Custom attribute value size** | 2 KB | Yes | Planned  
**Developers per organization** | 1 million | Planned | Yes  
**API Keys per app** | 10 | Planned | Planned  
**Apps per developer** | 100 | Planned | Planned  
**Apps per organization** | 1 million | Planned | Yes  
**Apps per[AppGroup](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#using-appgroups-to-organize-app-ownership)** | 30,000 | Planned | Planned  
**[AppGroups](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#using-appgroups-to-organize-app-ownership) per organization** | 1 million | Planned | Planned  
**API products per API Key** | 50 | Planned | Planned  
**API products per app** | 100 | Planned | Planned  
**API products per organization** | 5,000 | Planned | Yes  
  
### **API Products**  
  
**API Resources > Proxies** | 100 | Planned | Planned  
**API Resources > Paths** | 25 | Planned | Planned  
**REST and GraphQL Operations** | 50 | Yes | Yes  
**Environments** | 85 | Planned | Planned  
  
### **OAuth**  
  
**OAuth access token expiration** | >= 180 seconds, <= 30 days | Yes | Yes  
**OAuth refresh token expiration** | >= 1 day, <= 2 years | Yes | Yes  
**OAuth access and refresh token size** | 2 KB | Yes | Planned  
**External OAuth access token size** | 2 KB | Yes | Planned  
**Custom attributes** you can set on OAuth tokens | 18 | Yes | Planned  
**Custom attribute name size** | 1 KB | Yes | Planned  
**Custom attribute value size** | 2 KB | Yes | Planned  
  
### **Environment and Organization**  
  
**Environments per organization** | **Apigee:** Up to 85, but depends on contract  
**Apigee hybrid:** 85 | Yes | Yes  
**Environment groups per organization** | **Apigee:** Up to 85  
**Apigee hybrid:** 85 | Yes | Yes  
**Environment group attachments per org** | 100 | Yes | Yes  
**Instances per organization** **Note:** The maximum number of Cassandra pods per organization is 150. | 10 (11 for hybrid) | Yes | Planned  
**Instances per region** | 1 | Yes | N/A  
**Regions per organization** **Note:** The maximum number of Cassandra pods per organization is 150. | 10 (11 for hybrid) | Yes | N/A  
**API base paths per organization** **Note:** See `BasePath` in [ProxyEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-proxyendpointconfigurationelements) for information on base paths. | 6,000  | Yes | Yes  
**Hostnames per environment group** | 100 | Yes | Yes  
**Aliases per key** |  100  | Yes | Yes  
**Developer portals per organization** | 10  | Yes | Yes  
**[Developer accounts per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#exploring_the_users_page)** **Note:** This limit counts against the **Developers per organization** limit.  | 800 K  | Planned | Planned  
**Key stores per environment** | 100 | Yes | Yes  
**Kubernetes clusters per org** **Note:** The maximum number of Cassandra pods per organization is 150. | 10 | N/A | Planned  
**Orgs per Cassandra cluster** **Note:** For a 10-region multi-region installation, the limit is 1 organization per Cassandra cluster. | 5 | N/A | Planned  
**Target servers per environment** | 8,000 | Planned | Planned  
**Trust stores per environment** | 1,000 | Yes | Yes  
  
### **Portals**  
  
**[Maximum pages per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages#creating_a_page)** | 1,000 | Yes | Yes  
**[Maximum published APIs or API products per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#overview)** | 1,200 | Yes | Yes  
**[Maximum API documentation size for a published API](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#overview)** | 4 MB | Yes | Yes  
**[Maximum API categories per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#view-apis)** | 200 | Yes | Yes  
**[Maximum menu items per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-menus#explore-ui)** | 200 | Yes | Yes  
**[Maximum files per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-files#types)** | 500 | Yes | Yes  
**[Maximum file size](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-files#types)** | 10 MB | Yes | Yes  
**[Maximum file storage usage](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-files#upload-file)** | 100 MB | Yes | Yes  
**[Maximum audiences per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#exploring_the_audiences_page)** | 16 | Yes | Yes  
**[Maximum developer accounts per audience](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#manage_the_assignments_for_an_audience)** | 800 K (max users) | Planned | Planned  
**[Maximum developer teams per audience](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#manage_the_assignments_for_an_audience)** | 200 K | Yes | Yes  
**[Developer teams per portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#how_do_i_create_a_team)** | 200 K  | Planned | Planned  
**[Maximum developer teams a developer can be a member of](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#viewing_team_membership_by_user)** | 64  | Yes | Yes  
**[Maximum members in a developer team](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#viewing_developer_team_details)** | 100  | Yes | Yes  
**[Maximum characters in a portal's**Custom Scripts** JavaScript field](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-scripts)** | 150,000  | Yes | Yes  
  
### **Private Service Connect**  
  
**Private Service Connect Network Endpoint Groups (NEGs) for[northbound connections](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc)** | As of October 10, 2024, Apigee does not limit the number of Cloud projects that can connect to an Apigee instance through Private Service Connect; however, Google Cloud [Private Service Connect quota limits](https://docs.cloud.google.com/vpc/docs/quota) apply. Previously, the limit was 50 projects. For each project, you can now create up to 100 Private Service Connect NEGs. The previous limit was 20. For any Apigee instances created before October 10, 2024, you must [ update the consumer accept list for an Apigee instance ](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc#upgrading-an-apigee-instance) if you want to take advantage of these new limits. If you need to have more than 1000 Private Service Connect NEG connections in total across all of the Cloud projects connected to an Apigee instance, contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support). | Yes | N/A  
**Endpoint attachments per organization for[southbound connections](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#managing-endpoint-attachments)** | 1,000 | Yes | N/A  
  
### **DNS peering**  
  
**Number of peering zones per Apigee organization** | 1000  
This limit is a constraint imposed on Apigee by Cloud DNS. For details, see [Resource limits](https://docs.cloud.google.com/dns/quotas#resource_limits).  
Note: This limit applies only for Apigee organizations without VPC peering. | N/A | N/A  
  
### **System**  
  
**Target connection timeout** | 300 seconds | Planned | Planned  
**API proxy request URL size** | 10 KB | Yes | Yes  
**Request header size** | 60 KB | Yes | Yes  
**Response header size** | 60 KB | Yes | Yes  
**Request/response size for buffered (non-streamed) requests** | 30 MB | Yes | Yes  
**Request/response size for[streamed](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-streaming) requests** When streaming is enabled, payloads greater than **10 MB** are allowed; however, there could be performance implications.  | 10 MB | No | No  
**TLS / DTLS maximum handshake message size** | 128 KB | Yes | Yes  
**Target endpoints per proxy** | 1,000 | Yes | Yes  
  
### **Debug Sessions**  
  
**Maximum debug sessions** | You can create at most 100 debug sessions per minute per project | Yes | Yes  
**Maximum debug transactions per session** | 15 | Yes | Yes  
**Debug payload (per transaction)** | No limit | Yes | Yes  
**Maximum configurable sampling rate for[distributed tracing](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace#supported-distributed-tracing-systems)** | 0.5 | Yes | Yes  
**Maximum debug data size** | Payloads, headers, and flow variables are truncated. 10 KB | Yes | Yes  
  
### **Analytics APIs**  
  
**Maximum time range that can be queried via synchronous report** | 14 days for hybrid and 92 days for Apigee  
  
[Asyncronous queries](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/asynch-reports-api#time-limit-on-queries) enforce a 365 day maximum | Yes | Yes  
**Calls to the Analytics Metrics API** | 100 calls per minute | Yes | Yes  
**Calls to the Asynchronous Query API** | 300 calls per day | Yes | Yes  
**Calls to the Data Export API** | 500 calls per day | Yes | Yes  
  
### **API Monitoring**  
  
**Data retention period** | 6 weeks | Yes | Yes  
**Maximum latency observed** | 60 seconds | Yes | Yes  
  
### **Pay-as-you-go**  
  
**Max Base environments per org** | 5 | Yes | N/A  
**Max Intermediate environments per org** | 5 | Yes | N/A  
**Max Comprehensive environments per org** | 85 | Yes | N/A  
**Max proxy deployments per Base environment per region** | 20 | Yes | N/A  
**Max proxy deployments per Intermediate environment per region** | 50 | Yes | N/A  
**Max proxy deployments  per Comprehensive environment per region** | 100 includedAbility to purchase up to 6000 | Yes | N/A  
**Max shared flow deployments** , subject to restrictions per environment type | 75 | Yes | N/A  
  
### **Apigee Spaces**  
  
**Max number of Apigee Spaces per organization** | 20 | Yes | Yes  
**Max number of queries per second (QPS) for`list` operations for API proxy, API product, and shared flow endpoints** | 10 | Yes | Yes  
  
### **MCP in Apigee**  
  
**Number of MCP tools per organization** |  **Apigee** : 1000 **Apigee hybrid** : bounded by size, not by a fixed count. See [Estimate MCP tool capacity](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/enable-mcp#tool-capacity). | Yes | Yes  
  
**The information above represents current product limits. Google reserves the right to change product features and functionality or the above limits upon posting or otherwise making them accessible.**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
