---
url: https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts-sankey/
title: Visualize data flows with Sankey charts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:59:39.829518+00:00
---

# Visualize data flows with Sankey charts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts-sankey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Visualize data flows with Sankey charts

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide helps security engineers and analysts visualize security events that involve multi-hop pathways, relationships, or directional flows using Sankey charts in [Google SecOps Dashboard](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboard-charts). These specialized charts display nodes (representing data points) connected by links (representing flow between data points). The width of each link is proportional to the volume or weight of the flow, allowing you to identify major data paths, bottlenecks, and anomalies.

**Note:** You must have the `chronicle.nativeDashboards.update` IAM permission to manage charts.

## Common use cases

Sankey charts are particularly useful for the following use cases:

### Network traffic analysis

  * **Objective** : Visualize traffic flowing from source IPs, through specific ports or firewall rules, to destination IPs.
  * **Value** : Spot anomalous traffic spikes, unauthorized egress ports, and potential lateral movement across your environment without sorting through thousands of raw network connection logs.



### Data exfiltration detection

  * **Objective** : Track the movement of data from internal systems (like databases and local storage) to external destinations (like cloud storage and external domains).
  * **Value** : Accelerate detection of insider threats and unauthorized data transfers by making large-volume egress flows to untrusted external domains, cloud services, or storage buckets visually obvious.



### Authentication flows

  * **Objective** : Map user login attempts by source country, identity provider, service targeted, and final authentication result.
  * **Value** : Identify credential stuffing, brute-force campaigns, and impossible travel anomalies by visualizing failed versus successful authentication patterns across locations and applications.



### SOC workflow monitoring

  * **Objective** : Visualize alert triaging steps from alert detection, through assignee, to the final verdict or status.
  * **Value** : Uncover triage bottlenecks, balance analyst workload, and evaluate detection rule fidelity by tracking how alerts move from generation to final resolution.



## Before you begin

To successfully render a Sankey chart, your dashboard query and configuration must meet the following technical requirements:

  * **Column count** : The query response must return at least **three** data columns.
  * **Column types** : The dataset must include: 
    * At least **two** categorical columns (for example, text strings representing nodes).
    * At least **one** numeric column representing the flow value or weight (like `sum` or `count`).
  * **Directed Acyclic Graph (DAG) structure** : Sankey charts only support directional, non-repeating paths: 
    * **No self-loops** : The source and target nodes at any given level cannot be identical (for example, `Node A flowing to Node A`).
    * **No cyclic dependencies** : Data relationships cannot form loops (for example, `Node A flowing to Node B with Node B flowing back to Node A`).



## Configure a Sankey chart

To create and configure a Sankey chart in a custom dashboard:

  1. Open your custom dashboard in Google SecOps and click **Add > Visualization**.
  2. Run a query that returns the required columns (for example, a YARA-L 2.0 query yielding source IP, destination IP, and event count).
  3. In the **Chart configuration** panel on the right, select the **Sankey** chart type.
  4. Under **Data Settings** , map the fields for your first flow level: 
     * **Source Node** : Select the column representing the origin of the flow.
     * **Target Node** : Select the column representing the destination of the flow.
     * **Value** : Select the numerical column representing the volume or weight of the link.
  5. (Optional) To build a multi-level path, click **Add Level** and configure the source, target, and value fields for the next hop. You can add up to five levels in a single Sankey chart.
  6. Click **Save** to add the chart tile to your dashboard.



## Interactive features

Sankey charts offer the following interactive features:

  * **Hover details** : Hover over any link to view details about the volume (weight) flowing between the source and target. Hover over any node to view the total incoming and outgoing volumes.
  * **Drill downs** : Click a specific node or flow link to open the context menu. You can perform drill-down actions to execute filtered queries on the raw data based on the selected node or pathway.



## Sample YARA-L 2.0 queries for Sankey charts

This section contains several accurate samples you can use to build Sankey charts in dashboard charts.

**Tip:** Best Practice: Keep **node cardinality** low. Sankey charts are designed to show aggregated flows between a small set of categories or steps. Mapping columns with high cardinality (such as raw IP addresses or unique timestamps) results in a dense "hairball" of thin lines that is difficult to read.

For the best visual results, group high-cardinality fields into categories (like using subnets, countries, asset categories, or firewall actions) or filter the query to focus only on key values (such as specific ports).

### Log ingestion flow visualization

This query visualizes the log pipeline flow from raw log types, to the respective security vendor, down to the specific products being ingested.
    
    
      metadata.log_type != ""
      $log_type = metadata.log_type
      $vendor = metadata.vendor_name
      $product = metadata.product_name
    
      match:
        $log_type, $vendor, $product
    
      outcome:
        $ingested_count = count(metadata.id)
    

**Configuration mapping** :

| Source Node | Target Node | Value  
---|---|---|---  
**Level 1** | $log_type | $vendor | $ingested_count  
**Level 2** | $vendor | $product | $ingested_count  
  
### Parent-to-child process execution chain

This query visualizes the hierarchy of process execution, tracking the parent process running a target binary and the resulting security action.
    
    
      metadata.event_type = "PROCESS_LAUNCH"
      $parent_process = principal.process.parent_process.file.full_path
      $target_process = principal.process.file.full_path
      $action = security_result.action
    
      match:
        $parent_process, $target_process, $action
    
      outcome:
        $execution_count = count(metadata.id)
    

**Configuration mapping** :

| Source Node | Target Node | Value  
---|---|---|---  
**Level 1** | $parent_process | $target_process | $execution_count  
**Level 2** | $target_process | $action | $execution_count  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
