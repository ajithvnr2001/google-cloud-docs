---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/maintain-content-freshness/
title: Maintain freshness of in-memory column store data \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:47.240178+00:00
---

# Maintain freshness of in-memory column store data  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/maintain-content-freshness/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)



Send feedback 

#  Maintain freshness of in-memory column store data Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/columnar-engine/maintain-content-freshness)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/columnar-engine/maintain-content-freshness)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/columnar-engine/maintain-content-freshness)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/columnar-engine/maintain-content-freshness)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/columnar-engine/maintain-content-freshness)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/columnar-engine/maintain-content-freshness)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/maintain-content-freshness)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/columnar-engine/maintain-content-freshness)

This page describes how to maintain the freshness of data in the columnar engine's column store in AlloyDB Omni in a container. 

As table rows are added, deleted, or updated, the columnar engine doesn't immediately update data in the column store. Instead, it marks affected content in the column store as invalid, and queries are planned and executed using both column-oriented data from the column store and row-oriented data from the row cache and database storage.

Over time, as more and more data blocks become invalid, query performance improvements provided by the columnar engine are reduced to the point where the columnar data needs to be refreshed to regain query performance improvements. When this _refresh threshold_ is reached, the columnar engine uses a background job to refresh the invalid data in the column store. By default, the columnar engine uses a refresh threshold of 50, indicating that given content in the column store gets marked for refresh when 50% of its content has become invalid. You can change this refresh threshold to adjust the overhead of the automatic refresh and potentially gain better ongoing query performance for your application workload.

Additionally, you can manually refresh a table's data in the column store at any time. Usually, you perform a manual refresh when you want changes to a table to be reflected in the column store as soon as possible after making the changes.

## Change the refresh threshold of the columnar engine

Edit the value of the `google_columnar_engine.refresh_threshold_percentage` database flag to change the refresh threshold of the columnar engine.
    
    
        ALTER SYSTEM SET google_columnar_engine.refresh_threshold_percentage=THRESHOLD;
    

`THRESHOLD`: an integer value between `1` and `100`. This value specifies the percentage of data blocks in content that must become invalid for the content to be marked for refresh.

## Manually refresh a table's data in the column store

Execute the `google_columnar_engine_refresh` SQL function to manually refresh a table's data in the in-memory column store.
    
    
    SELECT google_columnar_engine_refresh(TABLE_NAME);
    

`TABLE_NAME`: a string containing the name of the table or the materialized view. If the table or the view is in a schema other than `public`, specify the name of the schema using the format `SCHEMA_NAME.TABLE_NAME`—for example, `myschema.mytable`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
