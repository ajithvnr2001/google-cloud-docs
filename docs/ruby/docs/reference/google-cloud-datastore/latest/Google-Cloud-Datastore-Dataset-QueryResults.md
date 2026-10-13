---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults/
title: Firestore in Datastore mode API - Class Google::Cloud::Datastore::Dataset::QueryResults (v2.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:21.797025+00:00
---

# Firestore in Datastore mode API - Class Google::Cloud::Datastore::Dataset::QueryResults (v2.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode API - Class Google::Cloud::Datastore::Dataset::QueryResults (v2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.4 

Reference documentation and code samples for the Firestore in Datastore mode API class Google::Cloud::Datastore::Dataset::QueryResults.

QueryResults is a special case Array with additional values. A QueryResults object is returned from Dataset#run and contains the Entities from the query as well as the query's cursor and more_results value.

Please be cautious when treating the QueryResults as an Array. Many common Array methods will return a new Array instance.

## Inherits

  * Array 



## Examples
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    tasks = datastore.run query
    
    tasks.size #=> 3
    tasks.cursor.to_s #=> "c2Vjb25kLXBhZ2UtY3Vyc29y"

Caution, many Array methods will return a new Array instance:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query("Task")
    tasks = datastore.run query
    
    tasks.size #=> 3
    tasks.cursor.to_s #=> "c2Vjb25kLXBhZ2UtY3Vyc29y"
    descriptions = tasks.map { |t| t["description"] }
    descriptions.size #=> 3
    descriptions.cursor #=> raise NoMethodError

## Methods 

### #all
    
    
    def all(request_limit: nil, &block) { |result| ... } -> Enumerator

Retrieves all query results by repeatedly loading [#next](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults#Google__Cloud__Datastore__Dataset__QueryResults_next_instance_ "Google::Cloud::Datastore::Dataset::QueryResults#next \(method\)") until [#next?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults#Google__Cloud__Datastore__Dataset__QueryResults_next__instance_ "Google::Cloud::Datastore::Dataset::QueryResults#next? \(method\)") returns `false`. Calls the given block once for each query result, which is passed as the parameter.

An Enumerator is returned if no block is given.

This method may make several API calls until all query results are retrieved. Be sure to use as narrow a search criteria as possible. Please use with caution.

**Parameter**

  * **request_limit** (Integer) _(defaults to: nil)_ — The upper limit of API requests to make to load all query results. Default is no limit. 



**Yields**

  * (result) — The block for accessing each query result. 



**Yield Parameter**

  * **result** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — The query result object. 



**Returns**

  * (Enumerator) 



**Examples**

Iterating each query result by passing a block:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.all do |t|
      puts "Task #{t.key.id} (#cursor)"
    end

Using the enumerator by not passing a block:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.all.map(&:key).each do |key|
      puts "Key #{key.id}"
    end

Limit the number of API calls made:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.all(request_limit: 10) do |t|
      puts "Task #{t.key.id} (#cursor)"
    end

### #all_with_cursor
    
    
    def all_with_cursor(request_limit: nil, &block) { |result, cursor| ... } -> Enumerator

Retrieves all query results and cursors by repeatedly loading [#next](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults#Google__Cloud__Datastore__Dataset__QueryResults_next_instance_ "Google::Cloud::Datastore::Dataset::QueryResults#next \(method\)") until [#next?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults#Google__Cloud__Datastore__Dataset__QueryResults_next__instance_ "Google::Cloud::Datastore::Dataset::QueryResults#next? \(method\)") returns `false`. Calls the given block once for each result and cursor combination, which are passed as parameters.

An Enumerator is returned if no block is given.

This method may make several API calls until all query results are retrieved. Be sure to use as narrow a search criteria as possible. Please use with caution.

**Parameter**

  * **request_limit** (Integer) _(defaults to: nil)_ — The upper limit of API requests to make to load all tables. Default is no limit. 



**Yields**

  * (result, cursor) — The block for accessing each query result and cursor. 



**Yield Parameters**

  * **result** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — The query result object. 
  * **cursor** ([Cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Cursor)) — The cursor object. 



**Returns**

  * (Enumerator) 



**Examples**

Iterating all results and cursors by passing a block:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.all_with_cursor do |task, cursor|
      puts "Task #{task.key.id} (#cursor)"
    end

Using the enumerator by not passing a block:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.all_with_cursor.count # number of result/cursor pairs

Limit the number of API calls made:
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.all_with_cursor(request_limit: 10) do |task, cursor|
      puts "Task #{task.key.id} (#cursor)"
    end

### #batch_read_time
    
    
    def batch_read_time() -> Google::Protobuf::Timestamp

Read timestamp this batch was returned from. This applies to the range of results from the query's `start_cursor` (or the beginning of the query if no cursor was given) to this batch's `end_cursor` (not the query's `end_cursor`).

In a single transaction, subsequent query result batches for the same query can have a greater timestamp. Each batch's read timestamp is valid for all preceding batches. This value will not be set for eventually consistent queries in Cloud Datastore.

**Returns**

  * (Google::Protobuf::Timestamp) 



### #cursor
    
    
    def cursor() -> Google::Cloud::Datastore::Cursor

**Alias Of** : [#end_cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults#Google__Cloud__Datastore__Dataset__QueryResults_end_cursor_instance_)

The end_cursor of the QueryResults.

**Returns**

  * ([Google::Cloud::Datastore::Cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Cursor)) 



### #cursor_for
    
    
    def cursor_for(result) -> Cursor

Retrieve the [Cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Cursor "Google::Cloud::Datastore::Cursor \(class\)") for the provided result.

**Parameter**

  * **result** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — The entity object to get a cursor for. 



**Returns**

  * ([Cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Cursor)) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    
    first_task = tasks.first
    first_cursor = tasks.cursor_for first_task

### #each_with_cursor
    
    
    def each_with_cursor() { |result, cursor| ... } -> Enumerator

Calls the given block once for each result and cursor combination, which are passed as parameters.

An Enumerator is returned if no block is given.

**Yields**

  * (result, cursor) — The block for accessing each query result and cursor. 



**Yield Parameters**

  * **result** ([Entity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Entity)) — The query result object. 
  * **cursor** ([Cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Cursor)) — The cursor object. 



**Returns**

  * (Enumerator) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    tasks.each_with_cursor do |task, cursor|
      puts "Task #{task.key.id} (#cursor)"
    end

### #end_cursor
    
    
    def end_cursor() -> Google::Cloud::Datastore::Cursor

**Aliases**

  * [#cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults#Google__Cloud__Datastore__Dataset__QueryResults_cursor_instance_)



The end_cursor of the QueryResults.

**Returns**

  * ([Google::Cloud::Datastore::Cursor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Cursor)) 



### #explain_metrics
    
    
    def explain_metrics() -> Google::Cloud::Datastore::V1::ExplainMetrics, nil

Query explain metrics. This is only present when the [RunQueryRequest.explain_options][google.datastore.v1.RunQueryRequest.explain_options] is provided, and it is sent only once with or after the last QueryResults batch.

To retrieve metrics, iterate over all QueryResults (e.g. with `next`). The explain_metrics field will be set on final QueryResults object.

**Returns**

  * (Google::Cloud::Datastore::V1::ExplainMetrics, nil) 



### #explain_options
    
    
    def explain_options() -> Google::Cloud::Datastore::V1::ExplainOptions, nil

The options for query explanation.

This is a copy of the input parameter supplied to the [#run](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_run_instance_ "Google::Cloud::Datastore::Dataset#run \(method\)") function.

**Returns**

  * (Google::Cloud::Datastore::V1::ExplainOptions, nil) 



### #more_after_cursor?
    
    
    def more_after_cursor?() -> Boolean

Convenience method for determining if the `more_results` value is `:MORE_RESULTS_AFTER_CURSOR`

**Returns**

  * (Boolean) 



### #more_after_limit?
    
    
    def more_after_limit?() -> Boolean

Convenience method for determining if the `more_results` value is `:MORE_RESULTS_AFTER_LIMIT`

**Returns**

  * (Boolean) 



### #more_results
    
    
    def more_results() -> Symbol

The state of the query after the current batch.

Expected values are:

  * `:NOT_FINISHED`
  * `:MORE_RESULTS_AFTER_LIMIT`
  * `:MORE_RESULTS_AFTER_CURSOR`
  * `:NO_MORE_RESULTS`



**Returns**

  * (Symbol) 



### #next
    
    
    def next() -> QueryResults

Retrieve the next page of results.

**Returns**

  * ([QueryResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset-QueryResults)) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    
    if tasks.next?
      next_tasks = tasks.next
    end

### #next?
    
    
    def next?() -> Boolean

Whether there are more results available.

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/datastore"
    
    datastore = Google::Cloud::Datastore.new
    
    query = datastore.query "Task"
    tasks = datastore.run query
    
    if tasks.next?
      next_tasks = tasks.next
    end

### #no_more?
    
    
    def no_more?() -> Boolean

Convenience method for determining if the `more_results` value is `:NO_MORE_RESULTS`

**Returns**

  * (Boolean) 



### #not_finished?
    
    
    def not_finished?() -> Boolean

Convenience method for determining if the `more_results` value is `:NOT_FINISHED`

**Returns**

  * (Boolean) 



### #read_time
    
    
    def read_time() -> Time, nil

Time at which the entities are being read. This would not be older than 270 seconds.

This is a copy of the input parameter supplied to the [#run](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore/latest/Google-Cloud-Datastore-Dataset#Google__Cloud__Datastore__Dataset_run_instance_ "Google::Cloud::Datastore::Dataset#run \(method\)") function.

**Returns**

  * (Time, nil) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
