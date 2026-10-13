---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File-Updater/
title: Cloud Storage API - Class Google::Cloud::Storage::File::Updater (v1.62.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:40.979077+00:00
---

# Cloud Storage API - Class Google::Cloud::Storage::File::Updater (v1.62.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File-Updater/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Storage API - Class Google::Cloud::Storage::File::Updater (v1.62.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.62.1 (latest)  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.1  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.1  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.2  1.35.0 

Reference documentation and code samples for the Cloud Storage API class Google::Cloud::Storage::File::Updater.

Yielded to a block to accumulate changes for a patch request.

## Inherits

  * [Google::Cloud::Storage::File](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File)



## Methods 

### #metadata
    
    
    def metadata() -> Hash(String => String)

A hash of custom, user-provided web-safe keys and arbitrary string values that will returned with requests for the file as "x-goog-meta-" response headers.

**Returns**

  * (Hash(String => String)) 



### #metadata=
    
    
    def metadata=(metadata)

Updates the hash of custom, user-provided web-safe keys and arbitrary string values that will returned with requests for the file as "x-goog-meta-" response headers.

**Parameter**

  * **metadata** (Hash(String => String)) — The user-provided metadata, in key/value pairs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
