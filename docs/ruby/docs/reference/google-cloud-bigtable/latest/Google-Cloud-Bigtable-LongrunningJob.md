---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-LongrunningJob/
title: Cloud Bigtable API - Class Google::Cloud::Bigtable::LongrunningJob (v2.13.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:03.569673+00:00
---

# Cloud Bigtable API - Class Google::Cloud::Bigtable::LongrunningJob (v2.13.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-LongrunningJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable API - Class Google::Cloud::Bigtable::LongrunningJob (v2.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.13.0 (latest)  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.5 

Reference documentation and code samples for the Cloud Bigtable API class Google::Cloud::Bigtable::LongrunningJob.

## LongrunningJob

A resource representing the long-running, asynchronous processing operation. The job can be refreshed to retrieve the result object once the operation has been completed.

## Inherits

  * Object 



## Methods 

### #done?
    
    
    def done?() -> boolean

Checks if the processing of the instance operation is complete.

**Returns**

  * (boolean) — `true` when complete, `false` otherwise. 



### #error
    
    
    def error() -> Object, Google::Rpc::Status, nil

The status when the operation associated with this job produced an error.

**Returns**

  * (Object, Google::Rpc::Status, nil) — A status object with the status code and message, or `nil` if no error occurred. 



### #error?
    
    
    def error?() -> boolean

Checks if the processing of the instance operation has errored.

**Returns**

  * (boolean) — `true` when errored, `false` otherwise. 



### #reload!
    
    
    def reload!() -> Google::Cloud::Bigtable::Instance::Job

Reloads the job with current data from the long-running, asynchronous processing of an operation.

**Returns**

  * ([Google::Cloud::Bigtable::Instance::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-Instance-Job)) — The same job instance. 



### #results
    
    
    def results() -> Object, nil

Gets the result object of the operation.

**Returns**

  * (Object, nil) — `nil` if the operation is not complete. 



### #wait_until_done!
    
    
    def wait_until_done!()

Reloads the job until the operation is complete. The delay between reloads will incrementally increase.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
