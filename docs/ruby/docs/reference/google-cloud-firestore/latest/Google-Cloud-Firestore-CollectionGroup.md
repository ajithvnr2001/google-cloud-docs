---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-CollectionGroup/
title: Cloud Firestore API - Class Google::Cloud::Firestore::CollectionGroup (v3.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:24.198715+00:00
---

# Cloud Firestore API - Class Google::Cloud::Firestore::CollectionGroup (v3.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-CollectionGroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore API - Class Google::Cloud::Firestore::CollectionGroup (v3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.1  3.0.0  2.16.1  2.15.1  2.14.0  2.13.1  2.12.0  2.11.0  2.10.1  2.9.1  2.8.0  2.7.2  2.6.6 

Reference documentation and code samples for the Cloud Firestore API class Google::Cloud::Firestore::CollectionGroup.

## CollectionGroup

A collection group object is used for adding documents, getting document references, and querying for documents, including with partitions.

See [Google::Cloud::Firestore::Client#col_group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Client#Google__Cloud__Firestore__Client_col_group_instance_ "Google::Cloud::Firestore::Client#col_group \(method\)") and [Query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query "Google::Cloud::Firestore::Query \(class\)").

## Inherits

  * [Google::Cloud::Firestore::Query](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-Query)



## Example
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    # Get a collection group
    col_group = firestore.col_group "cities"
    
    # Get and print all city documents
    col_group.get do |city|
      puts "#{city.document_id} has #{city[:population]} residents."
    end

## Methods 

### #partitions
    
    
    def partitions(partition_count, read_time: nil) -> Array<QueryPartition>

Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used as starting/end points for the query results.

**Parameters**

  * **partition_count** (Integer) — The desired maximum number of partition points. The number must be strictly positive. The actual number of partitions returned may be fewer. 
  * **read_time** (Time) _(defaults to: nil)_ — Reads documents as they were at the given time. This may not be older than 270 seconds. Optional 



**Returns**

  * (Array<[QueryPartition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore/latest/Google-Cloud-Firestore-QueryPartition)>) — An ordered array of query partitions. 



**Raises**

  * (ArgumentError) 



**Examples**
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    col_group = firestore.col_group "cities"
    
    partitions = col_group.partitions 3
    
    queries = partitions.map(&:to_query)

partition with read time
    
    
    require "google/cloud/firestore"
    
    firestore = Google::Cloud::Firestore.new
    
    col_group = firestore.col_group "cities"
    
    read_time = Time.now
    
    partitions = col_group.partitions 3, read_time: read_time
    
    queries = partitions.map(&:to_query)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
