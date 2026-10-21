---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/view-agent-registry-topology/
title: View topologies for an agent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:38.272059+00:00
---

# View topologies for an agent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/view-agent-registry-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  View topologies for an agent Stay organized with collections  Save and categorize content based on your preferences. 

In [Agent Registry](https://docs.cloud.google.com/agent-registry/overview) you can view a topology graph that shows traffic to and from an agent or AI application. Analyzing the graph helps you to understand if the agent or AI application is communicating with trusted agents, MCP servers, and endpoints.

To get more insights about your agent resources, use the query builder to on the [Topology page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/view-project-topology). You can visualize observability, security, software supply chain, and infrastructure resource data associated with your agents.

Some [limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology#limitations) apply to topology data.

## Before you begin

These instructions assume that you have [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup) and registered your agent resources.

  1. To view agent traffic, [instrument your AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview).

  2. Enable the App Hub, App Topology, Cloud Asset Inventory, and Observability APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=apphub.googleapis.com,cloudasset.googleapis.com,apptopology.googleapis.com,observability.googleapis.com&redirect=https%3A//console.cloud.google.com)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. If you are protecting services in a VPC Service Controls perimeter, update the perimeter to include App Topology and services that provide underlying data. [Learn more](https://docs.cloud.google.com/app-topology/use-vpc-sc).




### Required roles

To get the permissions that you need to view topology graphs in Agent Registry, ask your administrator to grant you the following IAM roles on the projects where you want to use App Topology: 

  * [App Topology Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apptopology#apptopology.viewer) (`roles/apptopology.viewer`)
  * [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view topology graphs in Agent Registry. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view topology graphs in Agent Registry:

  * Get discovered resource data: `apptopology.discoveredResourcesTopologies.generate`
  * Get resource data data: `apptopology.sreDomainTopologies.generate`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View an agent topology

  1. In the Google Cloud console, go to the Agent Registry page. 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/agents)

  2. In the project picker, select the project that contains your agents.

  3. On the **Agents** tab, click the name of the agent that you want to view.

  4. Click the **Topology** tab.

  5. In the **Quick Queries** section, click a query. If there are results that match your query, the topology graph is displayed.

  6. Explore the topology graph. The graph shows resources that match your query and the relationships between them.

     * Icons represent nodes, discovered and registered resources and their resource type.
     * Lines represent connections, the relationships between nodes.

![An example topology graph with a selected node](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/images/topology-graph.png)

You can interact with a topology in the following ways:

     * Change the visualization by zooming in or out or repositioning nodes.
     * View the label for a connection by hovering over the connection line between two nodes.
     * Get information about a node or connection by selecting it.
     * Hide or show the query panel by clicking **Toggle panel** first_page.



To view additional data about the selected agent, view the dashboards in [Application Monitoring](https://docs.cloud.google.com/monitoring/docs/application-monitoring-ai-resources).

## View an AI application topology

  1. In the Google Cloud console, go to the Agent Registry page. 

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry/agents)

  2. In the project picker, select the project that contains your AI application.

  3. On the **AI applications** tab, click the name of the agent that you want to view.

  4. Click the **Topology** tab.

  5. In the **Quick Queries** section, click a query. If there are results that match your query, the topology graph is displayed.

  6. Explore the topology graph. The graph shows resources that match your query and the relationships between them.

     * Icons represent nodes, discovered and registered resources and their resource type.
     * Lines represent connections, the relationships between nodes.

![An example topology graph with a selected node](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/images/topology-graph.png)

You can interact with a topology in the following ways:

     * Change the visualization by zooming in or out or repositioning nodes.
     * View the label for a connection by hovering over the connection line between two nodes.
     * Get information about a node or connection by selecting it.
     * Hide or show the query panel by clicking **Toggle panel** first_page.



To view additional data about the selected application, view the dashboards in [Application Monitoring](https://docs.cloud.google.com/monitoring/docs/application-monitoring-ai-resources).

## What's next

  * Visualize more data about your agent resources on the [Topology page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/view-project-topology).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
