---
url: https://docs.cloud.google.com/migration-center/docs/network-dependencies-report/
title: Generate and analyze network dependencies report \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:23.326727+00:00
---

# Generate and analyze network dependencies report  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/network-dependencies-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Generate and analyze network dependencies report Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to generate and analyze the network dependencies report in Migration Center. The network dependencies report provides monthly aggregated data about the connections to your servers and databases. The network dependencies report lets you see all the connections to the assets in your infrastructure, and the number of times the connection is observed by Migration Center, aggregated monthly.

To collect network dependencies data, let the [discovery client](https://docs.cloud.google.com/migration-center/docs/discovery-client-overview) run for a period of time and enable syncing the data with Migration Center. The longer you run the collection, the more data Migration Center has to analyze insights on your network dependencies. Migration Center then identifies all the network connections from the scanned assets. The target assets in a connection can be assets in your Migration Center inventory that you discovered with the discovery client, assets that you manually imported, or even unknown assets that are external to your environment.

The network dependencies report is useful in the following scenarios:

  * Collecting data about connections to servers and databases, to identify assets that belong to the same application
  * Identifying network connections of interest within a group of assets, such as all the servers using the MySQL standard port
  * Identifying missing assets in your inventory



You can download the network dependencies report as a CSV file from Migration Center. You can then perform your analysis using BigQuery and the sample queries provided by Migration Center, or use any other third-party tool.

## Limitations

  * To collect connection data in your infrastructure, you must use the discovery client.
  * Network connections data is collected only with the OS scan method only. The vSphere scan doesn't support network data collection.



## Before you begin

  * Before you create a network dependencies report, you must have performance collection working with the discovery client.

  * Before you analyze the network dependencies report with BigQuery, do the following:

    * Learn how to [import local data to BigQuery](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#loading_data_from_local_files).
    * Learn how to [run queries](https://docs.cloud.google.com/bigquery/docs/running-queries).



## Generate a network dependencies report

To generate a network dependencies report, follow these steps:

  1. In the Google Cloud console, go to the **Create reports** page.

[Go to Create reports](https://console.cloud.google.com/migration/all-reports?gtm_source=documentation&gtm_source_id=network_dependencies)

  2. Click **Network dependencies exports**.

  3. From the list of groups, select the groups for which you want to generate the report, then click **Export**.

  4. In the dialog that appears, click **Export**.

The exported report might take up to an hour to be generated. After your report is generated, the **Network dependencies** page opens.

**Note:** Migration Center stores up to six months of data. Each connection is aggregated by month. The `ConnectionCount` column in the report represents the number of times Migration Center observed the connection each month.
  5. To download a specific report, click download**Download**.




## Analyze the network dependencies report in BigQuery

The following sections provide you with some sample queries to analyze common scenarios in BigQuery. Before you can run a query, you must [upload your CSV file to BigQuery](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#loading_data_from_local_files).

To use BigQuery, you are billed according to the [BigQuery pricing](https://cloud.google.com/bigquery/pricing).

### Identify assets with most connections

The following query is useful to identify the assets that have the largest number of connections in the group.
    
    
    SELECT
     LocalVMName, SUM(ConnectionCount) as TotalCount
    FROM
     PROJECT.DATASET.TABLE
    GROUP BY ALL
    ORDER BY TotalCount DESC
    

Replace the following:

  * `PROJECT`: the Google Cloud project where you uploaded the CSV file.
  * `DATASET`: the BigQuery dataset.
  * `TABLE`: the BigQuery table.



The following is a sample output from this query:

LocalVMName | TotalCount  
---|---  
VM-x5ua3o2w | 9970  
VM-glg5np3w | 9763  
VM-q3z4zfp8 | 9557  
VM-2nnsrt37 | 9372  
VM-1oah56hn | 9350  
  
### Identify connections by graph's depth

The following query is useful to identify all the assets that connect to a given one with a specific number of intermediate connections. For example:

  * With graph depth equal to 1, you find all the assets directly connected to the main asset.
  * With graph depth equal to 2, you find all the assets directly connected to other assets, which are in turn directly connected to the main asset.


    
    
    DECLARE
     local_vm_name STRING DEFAULT MAIN_ASSET;
    DECLARE
     depth INT64 DEFAULT DEPTH;
    CREATE TEMP FUNCTION
     recursiveConnections(localVmName STRING,
       connectionsArray ARRAY<STRING>,
       depth INT64)
     RETURNS STRING
     LANGUAGE js AS r"""
     const connections = connectionsArray.map(connection => connection.split('|||'))
       .filter(connectionTuple => connectionTuple[1] !== 'Unscanned Device');
     const connectedAssets = new Set([localVmName]);
     for (let i = 0; i < depth; i++) {
       const currentSet = new Set(connectedAssets);
       for (const connection of connections) {
         /* Look for connections where the asset is the local asset */
         if (currentSet.has(connection[0])) {
           connectedAssets.add(connection[1]);
         }
         /* Look for connections where the asset is the remote asset */
         if (currentSet.has(connection[1])) {
           connectedAssets.add(connection[0]);
         }
       }
     }
     connectedAssets.delete(localVmName);
     return Array.from(connectedAssets).sort().join(', ');
    """;
    SELECT
     local_vm_name AS LocalVMName,
     recursiveConnections(local_vm_name,
       ARRAY_AGG(CONCAT(LocalVMName, '|||', RemoteVMName)),
       depth) AS Connections
    FROM
     PROJECT.DATASET.TABLE
    

Replace the following:

  * `MAIN_ASSET`: The name of the asset for which you want to identify the connections.
  * `DEPTH`: The depth of the graph.



The following is a sample output from this query:

LocalVMName | Connections  
---|---  
VM-lv8s148f | VM-2z8wp3ey,  
VM-66rq2x2y,  
VM-94uwyy8h,  
VM-ccgmqqmb,  
VM-ctqddf0u,  
VM-og4n77lb,  
...  
  
### Filter connections by IP and port ranges

The following query lets you identify assets that use IP addresses and ports in ranges that you define.
    
    
    CREATE TEMP FUNCTION
     ipBetween(value STRING,
       low STRING,
       high STRING) AS ( NET.IPV4_TO_INT64(NET.IP_FROM_STRING(value)) BETWEEN NET.IPV4_TO_INT64(NET.IP_FROM_STRING(low))
       AND NET.IPV4_TO_INT64(NET.IP_FROM_STRING(high)) );
    SELECT
     *
    FROM
     PROJECT.DATASET.TABLE
    WHERE
     ((LocalPort BETWEEN PORT_START
         AND PORT_END)
       OR (RemotePort BETWEEN PORT_START
         AND PORT_END))
     AND (ipBetween(LocalIP,
         IP_START,
         IP_END)
       OR ipBetween(RemoteIP,
         IP_START,
         IP_END))
    

Replace the following:

  * `PORT_START`: The initial port of the port range, for example `0`.
  * `PORT_END`: The final port of the port range, for example `1024`.
  * `IP_START`: The initial IP address of the range, for example `"10.26.0.0"`.
  * `IP_END`: The final IP address of the range, for example `"10.26.255.255"`.



The following is a sample output from this query:

SampleRange | LocalVMName | LocalAssetID | LocalGroups | LocalIP | LocalPort | Protocol | LocalProcessName | RemoteVMName | RemoteAssetID | RemoteGroups | RemoteIP | RemotePort | ConnectionCount  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
2025-06-02T05:59:53Z-2025-06-02T05:59:53Z | VM-0lf60off | projects/982941055174/locations/us-central1/assets/0lf60off | Group 1 | 10.0.45.138 | 272 | tcp | bash | VM-0spdofr9 | projects/982941055174/locations/us-central1/assets/0spdofr9 |  | 144.35.88.1 | 272 | 499  
2025-07-02T05:59:53Z-2025-07-02T05:59:53Z | VM-goa5uxhi | projects/982941055174/locations/us-central1/assets/goa5uxhi | Group 3 | 10.187.175.82 | 781 | tcp | bash | VM-27i5d2uj | projects/982941055174/locations/us-central1/assets/27i5d2uj |  | 22.99.72.109 | 781 | 980  
2025-08-02T05:59:53Z-2025-08-02T05:59:53Z | VM-7vwy31hg | projects/982941055174/locations/us-central1/assets/7vwy31hg | Group 1 | 10.58.166.132 | 21 | tcp | bash | VM-2gq0fl37 | projects/982941055174/locations/us-central1/assets/2gq0fl37 |  | 147.19.84.135 | 21 | 514  
  
### Identify unscanned assets in the network

The following query lets you identify any unscanned asset in your network. An unscanned asset is a connection to a remote IP address that is not associated to any asset in your Migration Center inventory. This lets you identify potentially missing assets that you need to scan for your assessment.
    
    
    CREATE TEMP FUNCTION
     ipBetween(value STRING,
       low STRING,
       high STRING) AS ( NET.IPV4_TO_INT64(NET.IP_FROM_STRING(value)) BETWEEN NET.IPV4_TO_INT64(NET.IP_FROM_STRING(low))
       AND NET.IPV4_TO_INT64(NET.IP_FROM_STRING(high)) );
    SELECT
     STRING_AGG(LocalIP, ', ') AS LocalIPs,
     RemoteIP
    FROM
     PROJECT.DATASET.TABLE
    WHERE
     RemoteVMName = 'Unscanned Device'
     AND ipBetween(LocalIP,
       IP_START,
       IP_END)
     AND ipBetween(RemoteIP,
       IP_START,
       IP_END)
    GROUP BY
     RemoteIP
    

Replace the following:

  * `IP_START`: The initial IP address of the range, for example `"10.26.0.0"`.
  * `IP_END`: The final IP address of the range, for example `"10.26.255.255"`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
