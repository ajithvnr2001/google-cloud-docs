---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job/
title: Cloud Spanner API - Class Google::Cloud::Spanner::Backup::Job (v2.36.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:04.189652+00:00
---

# Cloud Spanner API - Class Google::Cloud::Spanner::Backup::Job (v2.36.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner API - Class Google::Cloud::Spanner::Backup::Job (v2.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.36.0 (latest)  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.1  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.1  2.11.0 

Reference documentation and code samples for the Cloud Spanner API class Google::Cloud::Spanner::Backup::Job.

## Job

A resource representing the long-running, asynchronous processing of backup creation. The job can be refreshed to retrieve the backup object once the operation has been completed.

See [Database#create_backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Database#Google__Cloud__Spanner__Database_create_backup_instance_ "Google::Cloud::Spanner::Database#create_backup \(method\)")

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false
    job.reload! # API call
    job.done? #=> true
    
    if job.error?
      status = job.error
    else
      backup = job.backup
    end

## Methods 

### #backup
    
    
    def backup() -> Backup, nil

The backup is the object of the operation.

**Returns**

  * ([Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup), nil) — The backup, or `nil` if the operation is not complete. 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false
    job.reload!
    job.done? #=> true
    backup = job.backup

### #cancel
    
    
    def cancel()

Cancel the backup job.

**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false
    job.cancel

### #cancel_time
    
    
    def cancel_time() -> Time, nil

The operation canceled time.

**Returns**

  * (Time, nil) 



### #done?
    
    
    def done?() -> boolean

Checks if the processing of the backup operation is complete.

**Returns**

  * (boolean) — `true` when complete, `false` otherwise. 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false

### #end_time
    
    
    def end_time() -> Time, nil

The operation end time.

**Returns**

  * (Time, nil) 



### #error
    
    
    def error() -> Google::Cloud::Spanner::Status, nil

The status if the operation associated with this job produced an error.

**Returns**

  * ([Google::Cloud::Spanner::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Status), nil) — A status object with the status code and message, or `nil` if no error occurred. 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.error? # true
    
    error = job.error

### #error?
    
    
    def error?() -> boolean

Checks if the processing of the backup operation has errored.

**Returns**

  * (boolean) — `true` when errored, `false` otherwise. 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.error? #=> false

### #progress_percent
    
    
    def progress_percent() -> Integer

The operation progress in percentage.

**Returns**

  * (Integer) 



### #refresh!
    
    
    def refresh!() -> Google::Cloud::Spanner::Backup::Job

**Alias Of** : [#reload!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job#Google__Cloud__Spanner__Backup__Job_reload!_instance_)

Reloads the job with current data from the long-running, asynchronous processing of a backup operation.

**Returns**

  * ([Google::Cloud::Spanner::Backup::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job)) — The same job instance. 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false
    job.reload! # API call
    job.done? #=> true

### #reload!
    
    
    def reload!() -> Google::Cloud::Spanner::Backup::Job

**Aliases**

  * [#refresh!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job#Google__Cloud__Spanner__Backup__Job_refresh!_instance_)



Reloads the job with current data from the long-running, asynchronous processing of a backup operation.

**Returns**

  * ([Google::Cloud::Spanner::Backup::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner/latest/Google-Cloud-Spanner-Backup-Job)) — The same job instance. 



**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false
    job.reload! # API call
    job.done? #=> true

### #start_time
    
    
    def start_time() -> Time, nil

The operation start time.

**Returns**

  * (Time, nil) 



### #wait_until_done!
    
    
    def wait_until_done!()

Reloads the job until the operation is complete. The delay between reloads will incrementally increase.

**Example**
    
    
    require "google/cloud/spanner"
    
    spanner = Google::Cloud::Spanner.new
    
    database = spanner.database "my-instance", "my-database"
    expire_time = Time.now + 36000
    job = database.create_backup "my-backup", expire_time
    
    job.done? #=> false
    job.wait_until_done!
    job.done? #=> true

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-09 UTC."],[],[]] 
