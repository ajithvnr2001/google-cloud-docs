---
url: https://docs.cloud.google.com/spanner/docs/manual-data-compaction/
title: Manually trigger major compaction in a Spanner database \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:09.657816+00:00
---

# Manually trigger major compaction in a Spanner database  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/manual-data-compaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Manually trigger major compaction in a Spanner database Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

This document explains how to manually trigger a major compaction in a Spanner database.

Several storage-related features in Spanner, such as tiered storage or columnar engine, rely on a database-wide major compaction before they are fully enabled. By default, major compactions occur automatically across all tables over seven day periods. This means you might wait up to seven days for a new feature to be fully available. To make new features available immediately, you can manually trigger a major compaction.

The compaction process is a [long-running operation (LRO)](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations#check_the_progress_of_a_long-running_database_operation).

## Pricing

Manually triggering a major compaction temporarily increases [CPU utilization](https://docs.cloud.google.com/spanner/docs/cpu-utilization) on your Spanner instance. If additional [compute capacity](https://docs.cloud.google.com/spanner/pricing#compute-capacity) is required to offset this increase in CPU utilization, this will increase costs.

## Performance

Major compactions run as background operations. However, if your instance has consistently heavy CPU usage, the compaction workload might interfere with other critical operations. In such cases, you can temporarily scale up the instance to ensure stable performance during compaction.

## Manually trigger a major compaction

###  Google Cloud console 

  1. Open the Google Cloud console and select your instance.

[Go to Spanner instance](https://console.cloud.google.com/spanner/instances)

  2. Select a database.

  3. In the navigation menu, click **Spanner Studio**.

  4. Open a new tab by clicking add **New SQL editor tab** or add **New tab**.

  5. Run one of the following commands to start compaction, based on your database dialect:

###  GoogleSQL 
         
         CALL compact_all();
         

###  PostgreSQL 
         
         CALL spanner.compact_all();
         

This operation returns a long-running operation (LRO) ID that you can use to find the operation in the **Operations** list.

  6. To monitor the progress of the compaction operation, in the navigation menu, click **Operations**.




### C++

To trigger compactions programmatically using the C++ client library:
    
    
    void Compact(google::cloud::spanner::Client client) {
      namespace spanner = ::google::cloud::spanner;
    
      spanner::SqlStatement select("CALL compact_all()");
      using RowType = std::tuple<std::string>;
      auto rows = client.ExecuteQuery(std::move(select));
    
      for (auto& row : spanner::StreamOf<RowType>(rows)) {
        if (!row) throw std::move(row).status();
        std::cout << "Long-running operation ID: " << std::get<0>(*row) << "\n";
      }
    }
    

You can [check the progress of a long-running database operation](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations#check_the_progress_of_a_long-running_database_operation). You can also cancel the ongoing major compaction request using the LRO ID. For more information, see [Cancel a long-running database operation](https://docs.cloud.google.com/spanner/docs/manage-and-observe-long-running-operations#cancel_a_long-running_database_operation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
