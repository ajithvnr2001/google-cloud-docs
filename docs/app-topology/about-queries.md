---
url: https://docs.cloud.google.com/app-topology/about-queries/
title: About queries \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:48.379801+00:00
---

# About queries  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/about-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ Guides ](https://docs.cloud.google.com/app-topology/overview)



Send feedback 

#  About queries Stay organized with collections  Save and categorize content based on your preferences. 

This document describes components of an App Topology query and the query syntax.

## Query components

App Topology queries consist of several components:

  * **Nodes** \- Discovered Google Cloud resources or resources registered in App Hub or Agent Registry. Examples of nodes include

    * A Compute Engine VM
    * A container image in Artifact Registry
    * An agent
    * A Cloud Monitoring [alert](https://docs.cloud.google.com/monitoring/alerts)
    * An App Hub application, service, or workload
    * A vulnerability

The resources that you can query depend on the domain that you choose. The `SRE` domain includes all supported resources.

  * **Properties** : Properties of a node that you can use to refine a query. For example, you can query for a vulnerability with a specific CVE ID.

  * **Edge** : A directional relationship between two nodes.




## Query structure

This section provides an overview of the query structure. For more details, see the reference documentation for the [generate_discovered_resources_topology tool](https://docs.cloud.google.com/app-topology//reference/mcp/tools_list/generate_discovered_resources_topology).

Queries use the [AIP-160](https://google.aip.dev/160) filtering syntax.

Key elements of a query include the following:

  * Queries begin with a `startingNode` that specifies a root node.
  * You define relationships with the root `startingNode` using `neighbor`. The `neighbor` element defines connected nodes and edges.
  * `LabelPropertiesPattern` specifies match expressions. 
    * `label_matcher_expr` \- A match expression for node or edge labels.
    * `property_matcher_expr` \- A match expression to filter for specific properties of a node or edge.
  * You define a directional relationship using the `direction` field.



The following example shows a query for alerts associated with the App Hub workload `foo` in the project `web-project`. It also shows the use of `alias` to label nodes so that they are easier to reference in subsequent expressions.
    
    
    {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "generate_discovered_resource_topology",
      "arguments": {
        "name": "projects/web-project/locations/global/discoveredResourcesTopology",
        "topologyDomains": ["projects/web-project/locations/global/domains/SRE"],
        "filter": {
            "startingNode": {
            "alias": "source",
            "labelPropertiesPattern": {
              "labelMatcherExpr": "Base/apphub.googleapis.com/Workload",
              "propertyMatcherExpr": "source.Base/app/workloadReferenceUri = 'foo'"
            }
          },
          "neighbors": [
              {
              "edge": {
                "labelPropertiesPattern": {
                    "labelMatcherExpr": "Observability/HAS_ALERT"
                },
                "direction": "TO"
              },
              "graph": {
                  "startingNode": {
                  "alias": "alert",
                  "labelPropertiesPattern": {
                    "labelMatcherExpr": "Observability/Alert"
                  }
                }
              }
            }
          ]
        }
      }
    },
    }
    

### Matching nodes

Specify resource types (nodes) using the `label_matcher_expr` match expression. You can match a single node type or multiple types.

A `label_matcher_expr` can use either `OR` or `AND` operators, but you can't mix both types of operators in a single match expression.

Examples:

  * Match App Hub workloads: `"Base/apphub.googleapis.com/Workload"`
  * Match discovered workloads or services: `"Base/DiscoveredWorkload OR Base/DiscoveredService"`



### Match properties

Filter attributes of a node using the `property_matcher_expr` match expression.

There are two types of properties:

  * Built-in system properties - Properties that apply to all nodes and edges: 
    * For nodes: `NodeName` (for nodes)
    * For edges: `EdgeName` (for edges)
  * Labels - The list of labels on a node or edge that can be used with property filter expressions. For example:
        
        (CONTAINS_ANY(alias.Labels, "Base/MCPServer") AND alias.Base/agentregistry/urn = "foo") OR (CONTAINS_ANY(alias.Labels, "Base/Agent") AND alias.Base/agent/framework = "bar")
        

  * Domain schema properties - Properties specific to a resource type, such as `Base/location`, `Observability/errorRate`, and `Base/app/state`. The `GetSchema` method returns these properties.

For example, to filter for a resource with the label `n` in the region `us-central1`, use the expression `n.Base/location = "us-central1"`.




For a list of supported operators in property match expressions, see [LabelPropertiesPattern](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology#labelpropertiespattern).

### Edge directions

For edges, `edge.direction` specifies the direction, and the default is `DIRECTION_UNSPECIFIED`. You can set one of the following values indicate the relationship between the source node and destination node.

  * `TO` \- From source to destination.
  * `FROM` \- From destination to source.
  * `ANY` \- The relationship between nodes is bidirectional.



When the direction is known, use `TO` or `FROM`. Bidirectional queries `"ANY"` expand traversal state combinatorially and increase API latency.

## Limitations

Query and topology size:

  * Query responses can take longer to return results if they are more complex. This includes the following conditions: 
    * `propertyMatcherExpr` includes more than 4 comparisons.
    * Topology traversal includes more than five hops in query execution.
  * Pagination is not supported for returned topology data.
  * The API returns a maximum of 1,000 unique paths.
  * For observability data: 
    * `Observability/Alert` nodes only support the equality (`=`) operator.
    * `Observability/SENDS_TRAFFIC` edges don't support property filters.



Data availability:

  * Google Cloud Observability doesn't support telemetry for all App Hub services and workloads. For a list of supported infrastructure resources, see [Application Monitoring supported infrastructure](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-services).
  * When viewing a topology for an App Hub application, resources that can be shared across applications aren't included in the visualization.
  * When you delete a Developer Connect insights event, the event might still appear in App Topology query results for a few days.
  * For security and compliance data provided by Security Command Center: 
    * The provided data is in [Preview](https://cloud.google.com/products#product-launch-stages)
    * Data is only available for projects and applications in a Google Cloud organization.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
