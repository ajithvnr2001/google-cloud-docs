---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Cors-Rule/
title: Cloud Storage API - Class Google::Cloud::Storage::Bucket::Cors::Rule (v1.62.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:09.359795+00:00
---

# Cloud Storage API - Class Google::Cloud::Storage::Bucket::Cors::Rule (v1.62.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Cors-Rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Storage API - Class Google::Cloud::Storage::Bucket::Cors::Rule (v1.62.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.62.1 (latest)  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.1  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.1  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.2  1.35.0 

Reference documentation and code samples for the Cloud Storage API class Google::Cloud::Storage::Bucket::Cors::Rule.

## Bucket Cors Rule

Represents a website CORS rule for a bucket. Accessed via [Google::Cloud::Storage::Bucket#cors](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket#Google__Cloud__Storage__Bucket_cors_instance_ "Google::Cloud::Storage::Bucket#cors \(method\)").

## Inherits

  * Object 



## Example

Retrieving the bucket's CORS rules.
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::Storage.new
    
    bucket = storage.bucket "my-bucket"
    bucket.cors.size #=> 2
    rule = bucket.cors.first
    rule.origin #=> ["http://example.org"]
    rule.methods #=> ["GET","POST","DELETE"]
    rule.headers #=> ["X-My-Custom-Header"]
    rule.max_age #=> 3600

## Methods 

### #headers
    
    
    def headers() -> String

The list of header field names to send in the Access-Control-Allow-Headers header in the preflight response. Indicates the custom request headers that may be used in the actual request.

**Returns**

  * (String) — the current value of headers 



### #headers=
    
    
    def headers=(value) -> String

The list of header field names to send in the Access-Control-Allow-Headers header in the preflight response. Indicates the custom request headers that may be used in the actual request.

**Parameter**

  * **value** (String) — the newly set value 



**Returns**

  * (String) — the newly set value 



### #max_age
    
    
    def max_age() -> String

The value to send in the Access-Control-Max-Age header in the preflight response. Indicates how many seconds the results of a preflight request can be cached in a preflight result cache. The default value is `1800` (30 minutes.)

**Returns**

  * (String) — the current value of max_age 



### #max_age=
    
    
    def max_age=(value) -> String

The value to send in the Access-Control-Max-Age header in the preflight response. Indicates how many seconds the results of a preflight request can be cached in a preflight result cache. The default value is `1800` (30 minutes.)

**Parameter**

  * **value** (String) — the newly set value 



**Returns**

  * (String) — the newly set value 



### #methods
    
    
    def methods() -> String

The list of HTTP methods permitted in cross origin resource sharing with the bucket. (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".

**Returns**

  * (String) — the current value of methods 



### #methods=
    
    
    def methods=(value) -> String

The list of HTTP methods permitted in cross origin resource sharing with the bucket. (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".

**Parameter**

  * **value** (String) — the newly set value 



**Returns**

  * (String) — the newly set value 



### #origin
    
    
    def origin() -> String

The [origin](http://tools.ietf.org/html/rfc6454) or origins permitted for cross origin resource sharing with the bucket. Note: "*" is permitted in the list of origins, and means "any Origin".

**Returns**

  * (String) — the current value of origin 



### #origin=
    
    
    def origin=(value) -> String

The [origin](http://tools.ietf.org/html/rfc6454) or origins permitted for cross origin resource sharing with the bucket. Note: "*" is permitted in the list of origins, and means "any Origin".

**Parameter**

  * **value** (String) — the newly set value 



**Returns**

  * (String) — the newly set value 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
