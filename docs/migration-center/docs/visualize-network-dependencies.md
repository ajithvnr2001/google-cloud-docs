---
url: https://docs.cloud.google.com/migration-center/docs/visualize-network-dependencies/
title: Visualize network dependencies \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:31.104700+00:00
---

# Visualize network dependencies  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/visualize-network-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Visualize network dependencies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to visualize network dependencies between discovered server assets in Migration Center. You can view a graph showing network connections for a specific group or subset of server assets to help you understand your infrastructure and plan your application migration.

Visualization is based on the network connection data collected during discovery. The graph includes connections to server assets in other groups, as well as connections to unknown server assets external to your environment. You can access dependency visualization from the following pages:

  * **Reports:** Visualize your server asset network relationships
  * **Groups:** Visualize network dependencies for groups
  * **Assets:** Visualize network dependencies for specific server assets



## Before you begin

Before you can visualize network dependencies for your server assets, collect network dependency data using the [discovery client](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) and sync it with Migration Center, or use the [`mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/discovery-client-cli-overview) to perform guest discovery and export data to Migration Center.

Migration Center identifies connections to discovered server assets, manually imported server assets, or unknown server assets external to your environment. For more information, see [Start an asset discovery](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

**Permissions**

  * `migrationcenter.assets.list` to view assets in Migration Center.
  * `migrationcenter.groups.list` to view groups in Migration Center.



**Roles**

  * Migration Center Viewer (`roles/migrationcenter.viewer`) to view network dependency visualizations.



## Limitations

Network dependency visualization has the following limitations:

  * You can only visualize network dependencies for server assets. Migration Center collects network dependency data only for servers.
  * You can visualize up to 10 groups and up to 10,000 server assets in total. If you select more server assets or groups, or if the selected server assets have a large number of network connections, you might experience slower performance when visualizing the graph.



## Visualize your server asset network relationships

To visualize your server asset network relationships, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=network_dependencies)

  2. Click **Network relations visualization**.

  3. Click **Groups** to visualize dependencies for one or more groups, or click **Servers** to visualize dependencies for one or more server assets.

  4. From the table, select the items you want to visualize.

  5. Click **Visualize**.

The network dependency graph is displayed.

  6. To view information about a server asset, hold the pointer over the server asset. You can see the following information:

     * Node type
     * Connected nodes
     * Total number of inbound and outbound connections
     * IP address
  7. To view more details about a server asset, click it. In the details pane, you can perform the following actions:

     * To view the network connections of the selected server asset, click **Network**.
     * To view the asset inventory information, click **Properties**.
     * To view and manage the groups and labels associated with the server asset, click **Actions**.
     * To export the asset inventory details, click **Export** and select a file format.
  8. Optional: Filter the dependency graph.




## Visualize network dependencies for groups

To visualize network dependencies for a group, follow these steps:

  1. Go to the **Groups** page.

[Go to Groups](https://console.cloud.google.com/migration/discovery/groups)

  2. From the list, select one or more groups to visualize.

  3. Click **Visualize**.

The network dependency graph is displayed. The graph shows server assets as nodes and connections as edges.

  4. Optional: Filter the dependency graph.




## Visualize network dependencies for specific server assets

To visualize network dependencies for specific server assets, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page.

[Go to Assets](https://console.cloud.google.com/migration/discovery/assets?gtm_source=documentation&gtm_source_id=view_assets)

  2. Select the server assets for which you want to view the network dependencies.

  3. Click **Visualize**.

The network dependency graph is displayed. The graph shows server assets as nodes and connections as edges.

  4. Optional: Filter the dependency graph.




## Filter the dependency graph

After you generate the network dependency graph, you can filter it based on the following criteria:

  * **Groups:** To hide groups from the graph, in the **Groups** section, clear the checkbox for a group.
  * **Network**
    * **Assets without network connections:** hide assets that have been discovered but have no observed network traffic.
    * **Unscanned devices:** hide connections to devices that are not discovered but are communicating with discovered assets.
    * **Show connected assets:** show assets that do not match other filters but are directly connected to assets that do.
  * **Asset details**
    * **Detected software:** from the **Detected software** list, select the software components to include in the graph.
    * **Operating system:** from the **Operating system** list, select the operating systems to include in the graph.
    * **Labels:** from the **Labels** list, select the labels to include in the graph.



## What's next

  * Learn how to [generate and analyze network dependency report](https://docs.cloud.google.com/migration-center/docs/network-dependencies-report).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
