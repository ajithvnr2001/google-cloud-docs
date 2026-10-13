---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job-List/
title: Cloud Spanner API - Class Google::Cloud::Spanner::Backup::Job::List (v2.36.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:08.185818+00:00
---

# Cloud Spanner API - Class Google::Cloud::Spanner::Backup::Job::List (v2.36.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job-List/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner API - Class Google::Cloud::Spanner::Backup::Job::List (v2.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.36.0 (latest)  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.1  2.11.0 

Reference documentation and code samples for the Cloud Spanner API class Google::Cloud::Spanner::Backup::Job::List.

## List

List is a special case Array with additional values for backup operations.

## Inherits

  * Array 



## Methods 

### #all
    
    
    def all(&block) { |job| ... } -> Enumerator

Retrieves remaining results by repeatedly invoking [#next](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job-List#Google__Cloud__Spanner__Backup__Job__List_next_instance_ "Google::Cloud::Spanner::Backup::Job::List#next \(method\)") until [#next?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job-List#Google__Cloud__Spanner__Backup__Job__List_next__instance_ "Google::Cloud::Spanner::Backup::Job::List#next? \(method\)") returns `false`. Calls the given block once for each result, which is passed as the argument to the block.

An Enumerator is returned if no block is given.

This method will make repeated API calls until all remaining results are retrieved. (Unlike `#each`, for example, which merely iterates over the results returned by a single API call.) Use with caution.

**Yields**

  * (job) — The block for accessing each backup job. 



**Yield Parameter**

  * **job** ([Google::Cloud::Spanner::Backup::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job)) — The backup job object. 



**Returns**

  * (Enumerator) 



**Examples**

Iterating each backup job by passing a block:
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    instance = spanner.instance "my-instance"
    
    jobs = instance.backup_operations
    jobs.all do |job|
      puts job.backup.backup_id
    end

Using the enumerator by not passing a block:
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    instance = spanner.instance "my-instance"
    
    jobs = instance.backup_operations
    all_backup_ids = jobs.all.map do |job|
      job.backup.backup_id
    end

### #next
    
    
    def next() -> Backup::Job::List

Retrieve the next page of backup jobs.

**Returns**

  * ([Backup::Job::List](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job-List)) 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    instance = spanner.instance "my-instance"
    
    jobs = instance.backup_operations
    if jobs.next?
      next_jobs = jobs.next
    end

### #next?
    
    
    def next?() -> Boolean

Whether there is a next page of backup jobs.

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    instance = spanner.instance "my-instance"
    
    jobs = instance.backup_operations
    if jobs.next?
      next_jobs = jobs.next
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-09 UTC."],[],[]] 
