---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-HiveJob/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::HiveJob (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:58.430791+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::HiveJob (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-HiveJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::HiveJob (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::HiveJob.

A Dataproc job for running [Apache Hive](https://hive.apache.org/) queries on YARN.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #continue_on_failure
    
    
    def continue_on_failure() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries. 



### #continue_on_failure=
    
    
    def continue_on_failure=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries. 



**Returns**

  * (::Boolean) — Optional. Whether to continue executing queries if a query fails. The default value is `false`. Setting to `true` can be useful when executing independent parallel queries. 



### #jar_file_uris
    
    
    def jar_file_uris() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. 



### #jar_file_uris=
    
    
    def jar_file_uris=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. 



**Returns**

  * (::Array<::String>) — Optional. HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. 



### #properties
    
    
    def properties() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in `/etc/hadoop/conf/*-site.xml`, /etc/hive/conf/hive-site.xml, and classes in user code. 



### #properties=
    
    
    def properties=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in `/etc/hadoop/conf/*-site.xml`, /etc/hive/conf/hive-site.xml, and classes in user code. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in `/etc/hadoop/conf/*-site.xml`, /etc/hive/conf/hive-site.xml, and classes in user code. 



### #query_file_uri
    
    
    def query_file_uri() -> ::String

**Returns**

  * (::String) — The HCFS URI of the script that contains Hive queries.

Note: The following fields are mutually exclusive: `query_file_uri`, `query_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query_file_uri=
    
    
    def query_file_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The HCFS URI of the script that contains Hive queries.

Note: The following fields are mutually exclusive: `query_file_uri`, `query_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The HCFS URI of the script that contains Hive queries.

Note: The following fields are mutually exclusive: `query_file_uri`, `query_list`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query_list
    
    
    def query_list() -> ::Google::Cloud::Dataproc::V1::QueryList

**Returns**

  * ([::Google::Cloud::Dataproc::V1::QueryList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-QueryList)) — A list of queries.

Note: The following fields are mutually exclusive: `query_list`, `query_file_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #query_list=
    
    
    def query_list=(value) -> ::Google::Cloud::Dataproc::V1::QueryList

**Parameter**

  * **value** ([::Google::Cloud::Dataproc::V1::QueryList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-QueryList)) — A list of queries.

Note: The following fields are mutually exclusive: `query_list`, `query_file_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dataproc::V1::QueryList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-QueryList)) — A list of queries.

Note: The following fields are mutually exclusive: `query_list`, `query_file_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #script_variables
    
    
    def script_variables() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Mapping of query variable names to values (equivalent to the Hive command: `SET name="value";`). 



### #script_variables=
    
    
    def script_variables=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Mapping of query variable names to values (equivalent to the Hive command: `SET name="value";`). 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Mapping of query variable names to values (equivalent to the Hive command: `SET name="value";`). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
