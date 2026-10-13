---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DisplayData/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::DisplayData (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:00.588152+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::DisplayData (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-DisplayData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::DisplayData (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::DisplayData.

Data provided with a pipeline or transform to provide descriptive info.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bool_value
    
    
    def bool_value() -> ::Boolean

**Returns**

  * (::Boolean) — Contains value if the data is of a boolean type.

Note: The following fields are mutually exclusive: `bool_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bool_value=
    
    
    def bool_value=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Contains value if the data is of a boolean type.

Note: The following fields are mutually exclusive: `bool_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — Contains value if the data is of a boolean type.

Note: The following fields are mutually exclusive: `bool_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #duration_value
    
    
    def duration_value() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Duration)) — Contains value if the data is of duration type.

Note: The following fields are mutually exclusive: `duration_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #duration_value=
    
    
    def duration_value=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Duration)) — Contains value if the data is of duration type.

Note: The following fields are mutually exclusive: `duration_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Duration)) — Contains value if the data is of duration type.

Note: The following fields are mutually exclusive: `duration_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #float_value
    
    
    def float_value() -> ::Float

**Returns**

  * (::Float) — Contains value if the data is of float type.

Note: The following fields are mutually exclusive: `float_value`, `str_value`, `int64_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #float_value=
    
    
    def float_value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Contains value if the data is of float type.

Note: The following fields are mutually exclusive: `float_value`, `str_value`, `int64_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Float) — Contains value if the data is of float type.

Note: The following fields are mutually exclusive: `float_value`, `str_value`, `int64_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #int64_value
    
    
    def int64_value() -> ::Integer

**Returns**

  * (::Integer) — Contains value if the data is of int64 type.

Note: The following fields are mutually exclusive: `int64_value`, `str_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #int64_value=
    
    
    def int64_value=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Contains value if the data is of int64 type.

Note: The following fields are mutually exclusive: `int64_value`, `str_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Integer) — Contains value if the data is of int64 type.

Note: The following fields are mutually exclusive: `int64_value`, `str_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #java_class_value
    
    
    def java_class_value() -> ::String

**Returns**

  * (::String) — Contains value if the data is of java class type.

Note: The following fields are mutually exclusive: `java_class_value`, `str_value`, `int64_value`, `float_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #java_class_value=
    
    
    def java_class_value=(value) -> ::String

**Parameter**

  * **value** (::String) — Contains value if the data is of java class type.

Note: The following fields are mutually exclusive: `java_class_value`, `str_value`, `int64_value`, `float_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Contains value if the data is of java class type.

Note: The following fields are mutually exclusive: `java_class_value`, `str_value`, `int64_value`, `float_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #key
    
    
    def key() -> ::String

**Returns**

  * (::String) — The key identifying the display data. This is intended to be used as a label for the display data when viewed in a dax monitoring system. 



### #key=
    
    
    def key=(value) -> ::String

**Parameter**

  * **value** (::String) — The key identifying the display data. This is intended to be used as a label for the display data when viewed in a dax monitoring system. 



**Returns**

  * (::String) — The key identifying the display data. This is intended to be used as a label for the display data when viewed in a dax monitoring system. 



### #label
    
    
    def label() -> ::String

**Returns**

  * (::String) — An optional label to display in a dax UI for the element. 



### #label=
    
    
    def label=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional label to display in a dax UI for the element. 



**Returns**

  * (::String) — An optional label to display in a dax UI for the element. 



### #namespace
    
    
    def namespace() -> ::String

**Returns**

  * (::String) — The namespace for the key. This is usually a class name or programming language namespace (i.e. python module) which defines the display data. This allows a dax monitoring system to specially handle the data and perform custom rendering. 



### #namespace=
    
    
    def namespace=(value) -> ::String

**Parameter**

  * **value** (::String) — The namespace for the key. This is usually a class name or programming language namespace (i.e. python module) which defines the display data. This allows a dax monitoring system to specially handle the data and perform custom rendering. 



**Returns**

  * (::String) — The namespace for the key. This is usually a class name or programming language namespace (i.e. python module) which defines the display data. This allows a dax monitoring system to specially handle the data and perform custom rendering. 



### #short_str_value
    
    
    def short_str_value() -> ::String

**Returns**

  * (::String) — A possible additional shorter value to display. For example a java_class_name_value of com.mypackage.MyDoFn will be stored with MyDoFn as the short_str_value and com.mypackage.MyDoFn as the java_class_name value. short_str_value can be displayed and java_class_name_value will be displayed as a tooltip. 



### #short_str_value=
    
    
    def short_str_value=(value) -> ::String

**Parameter**

  * **value** (::String) — A possible additional shorter value to display. For example a java_class_name_value of com.mypackage.MyDoFn will be stored with MyDoFn as the short_str_value and com.mypackage.MyDoFn as the java_class_name value. short_str_value can be displayed and java_class_name_value will be displayed as a tooltip. 



**Returns**

  * (::String) — A possible additional shorter value to display. For example a java_class_name_value of com.mypackage.MyDoFn will be stored with MyDoFn as the short_str_value and com.mypackage.MyDoFn as the java_class_name value. short_str_value can be displayed and java_class_name_value will be displayed as a tooltip. 



### #str_value
    
    
    def str_value() -> ::String

**Returns**

  * (::String) — Contains value if the data is of string type.

Note: The following fields are mutually exclusive: `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #str_value=
    
    
    def str_value=(value) -> ::String

**Parameter**

  * **value** (::String) — Contains value if the data is of string type.

Note: The following fields are mutually exclusive: `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Contains value if the data is of string type.

Note: The following fields are mutually exclusive: `str_value`, `int64_value`, `float_value`, `java_class_value`, `timestamp_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #timestamp_value
    
    
    def timestamp_value() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Timestamp)) — Contains value if the data is of timestamp type.

Note: The following fields are mutually exclusive: `timestamp_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #timestamp_value=
    
    
    def timestamp_value=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Timestamp)) — Contains value if the data is of timestamp type.

Note: The following fields are mutually exclusive: `timestamp_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Timestamp)) — Contains value if the data is of timestamp type.

Note: The following fields are mutually exclusive: `timestamp_value`, `str_value`, `int64_value`, `float_value`, `java_class_value`, `duration_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #url
    
    
    def url() -> ::String

**Returns**

  * (::String) — An optional full URL. 



### #url=
    
    
    def url=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional full URL. 



**Returns**

  * (::String) — An optional full URL. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
