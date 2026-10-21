---
url: https://docs.cloud.google.com/app-topology/setup/
title: Set up App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:26.643920+00:00
---

# Set up App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ Guides ](https://docs.cloud.google.com/app-topology/overview)



Send feedback 

#  Set up App Topology Stay organized with collections  Save and categorize content based on your preferences. 

Since App Topology correlates data across multiple Google Cloud services, the App Topology and the services that provide data to App Topology must be enabled.

  1. Identify the Google Cloud project where you want to set up App Topology.

     * Security and compliance data provided by Security Command Center is only available for projects and applications in a Google Cloud organization. If you want to migrate a project to an organization, see the [migration instructions](https://docs.cloud.google.com/resource-manager/docs/handle-special-cases#migrating_projects_no_org)
     * If you set up an [app-enabled folder](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-enabled-folder) for App Hub applications, enable APIs and grant permissions described in these instructions on the folder's management project.
  2. Set up the services that provide the resource data that you want to query:

     * To view software supply chain data such as build provenance, [configure Developer Connect insights](https://docs.cloud.google.com/developer-connect/docs/set-up-insights).

     * To view security and compliance data, set up Security Command Center for security and compliance data. [Activate Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) at the organization level and [configure](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center) the features that you want to use. Querying data from Security Command Center is only available for [Premium and Enterprise tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

  3. To view data for agent resources, register your agent resources and instrument your AI applications.

     * [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) and register your agents, endpoints, MCP servers, and AI applications.
     * [instrument your AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview).

  4. Enable the App Topology, Cloud Asset Inventory, and Observability APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudasset.googleapis.com  apptopology.googleapis.com observability.googleapis.com 

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. If you are protecting services in a VPC Service Controls perimeter, update the perimeter to include App Topology and services that provide underlying data. [Learn more](https://docs.cloud.google.com/app-topology/use-vpc-sc).




## What's next

  * Use the [App Topology MCP server](https://docs.cloud.google.com/app-topology/use-apptopology-mcp).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
