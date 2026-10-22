---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/read-pools/
title: Troubleshoot read pool queries \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:19.728084+00:00
---

# Troubleshoot read pool queries  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/read-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot read pool queries Stay organized with collections  Save and categorize content based on your preferences. 

This page describes techniques for investigating and debugging queries that AlloyDB for PostgreSQL sends to a read pool instance:

  * Seeing a detailed list of a read pool's constituent nodes, including their IP addresses.
  * Connecting directly to a node, for debugging purposes.
  * Examining AlloyDB logs to determine which particular node is handling any one query sent to a read pool.
  * Querying the logs for all recent activity from a given read pool node.
  * Viewing Google Cloud metrics associated with a read pool node.



Used together, these techniques give you diagnostic and debugging access to your read pools. For example, if one of your cluster's read pools is using an unusual amount of CPU while processing a long-running query, these techniques let you determine which node is handling that query, and then directly connect to that node to further examine or terminate the query.

**Warning:** These techniques exist to enable temporary, diagnostic connections to read pool nodes. Always configure your applications to connect to read pool instances, rather than specific nodes. For more information, see A note about node ephemerality.

## List details of a read pool's nodes

In normal AlloyDB use, you don't need to know the identities or addresses of the nodes that make up your read pools. However, when necessary, you can see a list of a read pool instance's nodes. Each listed node includes the following information useful for subsequent diagnostic and debugging:

  * The node's Google Cloud ID string, used for performing log queries about that node's recent activity.

  * The node's IP address within your cluster's Virtual Private Cloud (VPC), which you can use to connect directly to that node's PostgreSQL server.




To see the internal ID strings and IP addresses of a read pool's nodes, follow the `gcloud`-specific instructions on [View instance details](https://docs.cloud.google.com/alloydb/docs/instance-view), but add an additional `--view=FULL` command-line argument:

### gcloud
    
    
    gcloud alloydb instances describe READ_POOL_ID \
     --region=REGION_ID \
     --cluster=CLUSTER_ID \
     --project=PROJECT_ID \
     --view=FULL

Replace the following:

  * READ_POOL_ID: The ID of the read pool.
  * REGION_ID: The instance's region ID.
  * CLUSTER_ID: The ID of the instance's cluster.
  * PROJECT_ID: The ID of the instance's project.



The output includes a section labeled `nodes`, resembling this:
    
    
    nodes:
    - id: READ_POOL_INSTANCE_ID-edd4f6ed-hcfh
      ip: 10.90.80.57
      state: HEALTHY
      zoneId: us-central1-b
    - id: READ_POOL_INSTANCE_ID-edd4f6ed-ldbm
      ip: 10.90.80.56
      state: HEALTHY
      zoneId: us-central1-c

The `id` and `ip` fields for each entry are especially relevant to the other techniques described on this page:

  * The `ip` field shows the node's IP address within the cluster's VPC.

  * The `id` field contains the node's full Google Cloud ID string. Only the final four characters of this string appear in logged entries for a node.

For example, to find log entries involving the first of the two nodes in the previous sample output, query the logs using the ID string `hcfh`.




## Connect directly to a node

Once you know the IP address of a node, you can connect directly to its PostgreSQL server. For example, to use `psql` to connect to a VM in your cluster's VPC, follow the instructions in [Run the psql client](https://docs.cloud.google.com/alloydb/docs/connect-psql#run-psql). When you do, provide the node's IP address rather than that of its read pool instance:
    
    
    psql -h NODE_IP_ADDRESS -U USERNAME

## Find node activity in logs

AlloyDB includes node IDs in log entries about queries handled by read pools. Generally speaking, you can use these discovered IDs in two ways:

  * Determine that node's IP so you can connect to it.
  * Perform further log queries to learn more about the node's recent activity.



### Determine which node is handling a known query

If you know that a certain read pool is processing a long-running query, then Log Explorer can help you determine the ID of the particular node handling that query.

Note that this technique works only on read pool instances that have [enabled the pgAudit extension](https://docs.cloud.google.com/alloydb/docs/pgaudit/enable-audit).

  1. Visit the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the [query builder](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#query-builder), add `resource.labels.instance_id="READ_POOL_ID"` to the query-editor field, replacing READ_POOL_ID with the name of your read pool instance.

  3. Add the SQL statement you're investigating, in whole or in part, to the query editor field. For example: `select id from MyTable`. This input is not case-sensitive.

  4. Click **Run query**.

  5. Use Log Explorer's controls to tune and re-run the query as needed to filter the results down to the most relevant ones.

  6. Click a log entry in the results list to expand its display.

  7. Click the `labels` field in the entry's expanded display.

  8. Note the value of `NODE_ID` under `labels`.




The result is the four-character identifier of the node handling the query.

### Connect to a node mentioned in a log entry

If you want to connect directly to a particular node's PostgreSQL server based on its logged activity, follow these steps:

  1. Note the logged node's four-character ID string. You can find this ID in the log entry's `NODE_ID` field.

  2. List the nodes for the read pool.

  3. In that list, find a node with the ID string that ends wth the four characters you noted in the first step. It is possible that none of the listed nodes match.

  4. If you do find a matching node, use its matching IP address to connect to that node's PostgreSQL server.

Otherwise, if none of the read pool's nodes listed in the previous step have IDs matching the logged node, the read pool has decommissioned that node in the time that has passed since the original log entry. This is normal behavior for AlloyDB read pools, as described in A note about node ephermerality. In this case, you can't establish a direct connection to that node.




Once you connect to a node's PostgreSQL server, you can use standard PostgreSQL monitoring techniques, such as [`pg_stat_activity`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW), to further investigate the node's current processes, and adjust them as needed.

### See more log entries about a node

To see more recent logged activity about a node with a specific ID:

  1. Visit the Logs Explorer:

[Go to the Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Add `labels.NODE_ID=NODE_ID` to [the Logs Explorer query builder](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#query-builder), replacing NODE_ID with the node's four-character ID string.

  3. Click **Run Query** to see all activity from that node within the selected time window, or tune the query to filter it further.

  4. Repeat the previous step as needed to refine your search.




## Monitor node metrics

**Preview**

This product is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#0) of the Google Cloud Terms of Service. Pre-GA products might have limited support, and changes to pre-GA products might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can view metrics associated with individual nodes from the AlloyDB System insights dashboard. For more information about available node metrics, see the [System insights metrics reference](https://docs.cloud.google.com/alloydb/docs/reference/system-insights-metrics).

To learn which node IDs are associated with a particular read pool instance, see List details of a read pool's nodes.

For full reference documentation of these and other AlloyDB metrics, see [`alloydb`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-alloydb) in "Google Cloud metrics".

## A note about node ephemerality

While you can safely connect to a node for temporary investigation or debugging purposes, applications that use read pools should always connect to those pools at the instance level, using the IP address that [its cluster displays in its instance list](https://docs.cloud.google.com/alloydb/docs/cluster-list-instances).

AlloyDB treats its read pools' nodes as ephemeral, interchangeable resources. The service changes a read pool's roster of nodes as often as necessary in order to keep that read pool instance load-balanced and responsive. An application that connects directly to a read pool node, rather than to a read pool instance, runs the risk of abruptly disconnecting from your database whenever AlloyDB updates the instance's node roster.

Always let your applications connect to your read pools at the instance level, and let AlloyDB do the work of efficiently routing your queries to the proper nodes.

## What's next

  * Learn more about [using Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
