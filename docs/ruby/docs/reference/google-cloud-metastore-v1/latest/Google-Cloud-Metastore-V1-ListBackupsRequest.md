---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-ListBackupsRequest/
title: Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::ListBackupsRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:26.097899+00:00
---

# Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::ListBackupsRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-ListBackupsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::ListBackupsRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Dataproc Metastore V1 API class Google::Cloud::Metastore::V1::ListBackupsRequest.

Request message for [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. The filter to apply to list results. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The filter to apply to list results. 



**Returns**

  * (::String) — Optional. The filter to apply to list results. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Specify the ordering of results as described in [Sorting Order](https://cloud.google.com/apis/design/design_patterns#sorting_order). If not specified, the results will be sorted in the default order. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specify the ordering of results as described in [Sorting Order](https://cloud.google.com/apis/design/design_patterns#sorting_order). If not specified, the results will be sorted in the default order. 



**Returns**

  * (::String) — Optional. Specify the ordering of results as described in [Sorting Order](https://cloud.google.com/apis/design/design_patterns#sorting_order). If not specified, the results will be sorted in the default order. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of backups to return. The response may contain less than the maximum number. If unspecified, no more than 500 backups are returned. The maximum value is 1000; values above 1000 are changed to 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of backups to return. The response may contain less than the maximum number. If unspecified, no more than 500 backups are returned. The maximum value is 1000; values above 1000 are changed to 1000. 



**Returns**

  * (::Integer) — Optional. The maximum number of backups to return. The response may contain less than the maximum number. If unspecified, no more than 500 backups are returned. The maximum value is 1000; values above 1000 are changed to 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)") call. Provide this token to retrieve the subsequent page.

To retrieve the first page, supply an empty page token.

When paginating, other parameters provided to [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)") must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)") call. Provide this token to retrieve the subsequent page.

To retrieve the first page, supply an empty page token.

When paginating, other parameters provided to [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)") must match the call that provided the page token. 




**Returns**

  * (::String) — Optional. A page token, received from a previous [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)") call. Provide this token to retrieve the subsequent page.

To retrieve the first page, supply an empty page token.

When paginating, other parameters provided to [DataprocMetastore.ListBackups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_list_backups_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#list_backups \(method\)") must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The relative resource name of the service whose backups to list, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups`. 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The relative resource name of the service whose backups to list, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups`. 




**Returns**

  * (::String) — Required. The relative resource name of the service whose backups to list, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}/backups`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
