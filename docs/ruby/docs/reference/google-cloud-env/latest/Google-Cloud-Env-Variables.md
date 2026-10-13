---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-env/latest/Google-Cloud-Env-Variables/
title: Google Cloud Platform environment queries - Class Google::Cloud::Env::Variables (v2.4.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:17.951363+00:00
---

# Google Cloud Platform environment queries - Class Google::Cloud::Env::Variables (v2.4.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-env/latest/Google-Cloud-Env-Variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Platform environment queries - Class Google::Cloud::Env::Variables (v2.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.1 (latest)  2.4.0  2.3.1  2.2.2 

Reference documentation and code samples for the Google Cloud Platform environment queries class Google::Cloud::Env::Variables.

Access to system environment variables.

This is a hashlike object that controls access to environment variable data. It supports temporarily changing the data source (i.e. swapping ::ENV out for a different set of data) for mocking.

## Inherits

  * Object 



## Methods 

### #[]
    
    
    def [](key) -> String, nil

**Aliases**

  * [#get](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-env/latest/Google-Cloud-Env-Variables#Google__Cloud__Env__Variables_get_instance_)



Fetch the given environment variable from the backing data.

**Parameter**

  * **key** (String) 



**Returns**

  * (String, nil) 



### #backing_data
    
    
    def backing_data() -> Hash{String=>String}

The backing data is a hash or hash-like object that represents the environment variable data. This can either be the actual environment variables object (i.e. ENV) or a substitute hash used for mocking.

**Returns**

  * (Hash{String=>String}) 



### #backing_data=
    
    
    def backing_data=(value) -> Hash{String=>String}

The backing data is a hash or hash-like object that represents the environment variable data. This can either be the actual environment variables object (i.e. ENV) or a substitute hash used for mocking.

**Parameter**

  * **value** (Hash{String=>String}) 



**Returns**

  * (Hash{String=>String}) 



### #get
    
    
    def get(key) -> String, nil

**Alias Of** : [#[]](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-env/latest/Google-Cloud-Env-Variables#Google__Cloud__Env__Variables_\[\]_instance_)

Fetch the given environment variable from the backing data.

**Parameter**

  * **key** (String) 



**Returns**

  * (String, nil) 



### #initialize
    
    
    def initialize() -> Variables

Create an enviroment variables access object. This is initially backed by the actual environment variables (i.e. ENV).

**Returns**

  * ([Variables](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-env/latest/Google-Cloud-Env-Variables)) — a new instance of Variables 



### #with_backing_data
    
    
    def with_backing_data(temp_backing_data)

Run the given block with the backing data replaced with the given hash. The original backing data is restored afterward. This is used for debugging/testing/mocking.

**Parameter**

  * **temp_backing_data** (Hash{String=>String}) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
