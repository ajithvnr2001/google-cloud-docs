---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-api-dependencies/
title: Manage API-specific supply chain dependencies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:23.021799+00:00
---

# Manage API-specific supply chain dependencies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-api-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage API-specific supply chain dependencies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

The API-specific supply chain feature provides a visual graph within the API details view, to help you identify, visualize, and manage resource dependencies across your APIs. This graph illustrates the upstream and downstream relationships, clarifying how consumers invoke suppliers for a specific operation.

## View the supply chain graph

To view the dependency graph for a specific API:

  1. In the Google Cloud console, go to **API hub > APIs**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. From the API list, select the API for which you want to view the supply chain graph.
  3. In the API details view, select the **Supply chain** tab.
  4. To generate and view the graph, you must select a specific operation (for example, the "get products" operation of a specific API version).



When you select an operation, the graph populates with the upstream and downstream dependencies for that specific resource. The dependencies graph is visible only if dependencies exist for the selected operation. 

## Explore the supply chain graph

The supply chain graph offers several interactive features to help you visualize dependencies effectively:

  1. **View dependency details:** Click on any of the edges (connecting lines) in the graph to view additional details about that specific dependency.
  2. **Expand and collapse nodes:** You can expand or collapse nodes in both upstream and downstream directions to simplify complex views or drill down into deeper dependency chains.



For more information about the supply chain graph, see [API supply chain graph view](https://docs.cloud.google.com/apigee/docs/apihub/api-supply-chain#api-supply-chain-graph-view).

## Create a dependency

In addition to viewing existing relationships, you can manually define new dependencies directly from the supply chain view:

  1. In the Google Cloud console, go to **API hub > APIs**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. From the list of APIs, select the API for which you want to create the dependency.
  3. Select the **Supply chain** tab.
  4. In the **Supply chain** tab, select an operation from the operations list.
  5. Click **Create dependency**.
  6. Enter a description for the dependency. (Optional)
  7. Select the **Resource type** for the operation.
  8. Enter the **Consumer** or **Supplier details**. You must specify the exact operations and versions.
  9. Click **Create dependency**.



The new dependency immediately appears in the supply chain graph, keeping your dependency mapping up to date.

## Edit a dependency

**Note:** The only editable attribute is the dependency description. 

To edit the description of an existing dependency:

  1. In the Google Cloud console, go to **API hub > APIs**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Select the API for which you want to edit the dependency.
  3. Select the **Supply chain** tab.
  4. In the **Supply chain** tab, select an operation from the operations list.
  5. From the graph, select the dependency you want to edit.
  6. In the **Dependency** pane, update the description.
  7. Click **Save**.



## Delete a dependency

To delete an existing dependency:

  1. In the Google Cloud console, go to **API hub > APIs**.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Select the API for which you want to delete the dependency.
  3. Select the **Supply chain** tab.
  4. In the **Supply chain** tab, select an operation from the operations list.
  5. From the graph, select the dependency you want to delete.
  6. Click delete **(Delete dependency)** to delete the dependency.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
