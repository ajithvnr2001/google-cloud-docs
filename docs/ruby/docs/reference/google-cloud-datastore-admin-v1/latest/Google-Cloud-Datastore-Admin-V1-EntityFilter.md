---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-admin-v1/latest/Google-Cloud-Datastore-Admin-V1-EntityFilter/
title: Firestore in Datastore mode Admin V1 API - Class Google::Cloud::Datastore::Admin::V1::EntityFilter (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:48.923704+00:00
---

# Firestore in Datastore mode Admin V1 API - Class Google::Cloud::Datastore::Admin::V1::EntityFilter (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-admin-v1/latest/Google-Cloud-Datastore-Admin-V1-EntityFilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode Admin V1 API - Class Google::Cloud::Datastore::Admin::V1::EntityFilter (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.1  0.8.0  0.7.1  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Firestore in Datastore mode Admin V1 API class Google::Cloud::Datastore::Admin::V1::EntityFilter.

Identifies a subset of entities in a project. This is specified as combinations of kinds and namespaces (either or both of which may be all, as described in the following examples). Example usage:

Entire project: kinds=[], namespace_ids=[]

Kinds Foo and Bar in all namespaces: kinds=['Foo', 'Bar'], namespace_ids=[]

Kinds Foo and Bar only in the default namespace: kinds=['Foo', 'Bar'], namespace_ids=['']

Kinds Foo and Bar in both the default and Baz namespaces: kinds=['Foo', 'Bar'], namespace_ids=['', 'Baz']

The entire Baz namespace: kinds=[], namespace_ids=['Baz']

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #kinds
    
    
    def kinds() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — If empty, then this represents all kinds. 



### #kinds=
    
    
    def kinds=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — If empty, then this represents all kinds. 



**Returns**

  * (::Array<::String>) — If empty, then this represents all kinds. 



### #namespace_ids
    
    
    def namespace_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — An empty list represents all namespaces. This is the preferred usage for projects that don't use namespaces.

An empty string element represents the default namespace. This should be used if the project has data in non-default namespaces, but doesn't want to include them. Each namespace in this list must be unique. 




### #namespace_ids=
    
    
    def namespace_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — An empty list represents all namespaces. This is the preferred usage for projects that don't use namespaces.

An empty string element represents the default namespace. This should be used if the project has data in non-default namespaces, but doesn't want to include them. Each namespace in this list must be unique. 




**Returns**

  * (::Array<::String>) — An empty list represents all namespaces. This is the preferred usage for projects that don't use namespaces.

An empty string element represents the default namespace. This should be used if the project has data in non-default namespaces, but doesn't want to include them. Each namespace in this list must be unique. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
