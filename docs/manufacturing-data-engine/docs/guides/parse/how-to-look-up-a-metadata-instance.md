---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-look-up-a-metadata-instance/
title: Look up a metadata instance \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:38.705120+00:00
---

# Look up a metadata instance  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-look-up-a-metadata-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Look up a metadata instance

This guide describes how to use the Whistle function `mde:lookupByKey` in a Whistle script to look up a metadata instance object from a bucket.

## Reference data lookup

Manufacturing Data Engine (MDE) provides a custom Whistle function to retrieve a metadata instance object from a metadata bucket by natural key. Metadata instances can be retrieved from any bucket, but the function is commonly used to look up reference data from a [lookup bucket](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/metadata#lookup_buckets).

You can look up a metadata instance by its natural key by calling the `mde:lookupByKey` function in a Whistle script. The function takes the lookup`bucket_name`, `natural_key` and `bucket_version` of the instance as the arguments, and returns the latest metadata instance for the provided natural key. You can use the instance to populate fields in a proto record in the parser, like in the following example:

**Caution:** This example uses incomplete code for demonstration purposes and is not guaranteed to work.
    
    
    "data" : {
      "complex" : {
        "VIN" : mde::lookupByKey("vin-lookup-bucket", input.vinKey, 1).VIN,
        "vin_registration_time" : mde::lookupByKey("vin-lookup-bucket", input.vinKey, 1).vin_registration_time,
        "ResultValue" : 163.0482614,
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
