---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListEntriesRequest/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::ListEntriesRequest (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:30.611124+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::ListEntriesRequest (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-ListEntriesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::ListEntriesRequest (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::ListEntriesRequest.

List Entries request.

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

  * (::String) — 

Optional. A filter on the entries to return. Filters are case-sensitive. You can filter the request by the following fields:

    * entry_type
    * entry_source.display_name
    * parent_entry

The comparison operators are =, !=, <, >, <=, >=. The service compares strings according to lexical order.

You can use the logical operators AND, OR, NOT in the filter.

You can use Wildcard "*", but for entry_type and parent_entry you need to provide the full project id or number.

You cannot use parent_entry in conjunction with other fields.

Example filter expressions:

    * "entry_source.display_name=AnExampleDisplayName"
    * "entry_type=projects/example-project/locations/global/entryTypes/example-entry_type"
    * "entry_type=projects/example-project/locations/us/entryTypes/a* OR entry_type=projects/another-project/locations/*"
    * "NOT entry_source.display_name=AnotherExampleDisplayName"
    * "parent_entry=projects/example-project/locations/us/entryGroups/example-entry-group/entries/example-entry"



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. A filter on the entries to return. Filters are case-sensitive. You can filter the request by the following fields:

    * entry_type
    * entry_source.display_name
    * parent_entry

The comparison operators are =, !=, <, >, <=, >=. The service compares strings according to lexical order.

You can use the logical operators AND, OR, NOT in the filter.

You can use Wildcard "*", but for entry_type and parent_entry you need to provide the full project id or number.

You cannot use parent_entry in conjunction with other fields.

Example filter expressions:

    * "entry_source.display_name=AnExampleDisplayName"
    * "entry_type=projects/example-project/locations/global/entryTypes/example-entry_type"
    * "entry_type=projects/example-project/locations/us/entryTypes/a* OR entry_type=projects/another-project/locations/*"
    * "NOT entry_source.display_name=AnotherExampleDisplayName"
    * "parent_entry=projects/example-project/locations/us/entryGroups/example-entry-group/entries/example-entry"



**Returns**

  * (::String) — 

Optional. A filter on the entries to return. Filters are case-sensitive. You can filter the request by the following fields:

    * entry_type
    * entry_source.display_name
    * parent_entry

The comparison operators are =, !=, <, >, <=, >=. The service compares strings according to lexical order.

You can use the logical operators AND, OR, NOT in the filter.

You can use Wildcard "*", but for entry_type and parent_entry you need to provide the full project id or number.

You cannot use parent_entry in conjunction with other fields.

Example filter expressions:

    * "entry_source.display_name=AnExampleDisplayName"
    * "entry_type=projects/example-project/locations/global/entryTypes/example-entry_type"
    * "entry_type=projects/example-project/locations/us/entryTypes/a* OR entry_type=projects/another-project/locations/*"
    * "NOT entry_source.display_name=AnotherExampleDisplayName"
    * "parent_entry=projects/example-project/locations/us/entryGroups/example-entry-group/entries/example-entry"



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Number of items to return per page. If there are remaining results, the service returns a next_page_token. If unspecified, the service returns at most 10 Entries. The maximum value is 100; values above 100 will be coerced to 100. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Number of items to return per page. If there are remaining results, the service returns a next_page_token. If unspecified, the service returns at most 10 Entries. The maximum value is 100; values above 100 will be coerced to 100. 



**Returns**

  * (::Integer) — Optional. Number of items to return per page. If there are remaining results, the service returns a next_page_token. If unspecified, the service returns at most 10 Entries. The maximum value is 100; values above 100 will be coerced to 100. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. Page token received from a previous `ListEntries` call. Provide this to retrieve the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Page token received from a previous `ListEntries` call. Provide this to retrieve the subsequent page. 



**Returns**

  * (::String) — Optional. Page token received from a previous `ListEntries` call. Provide this to retrieve the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`. 



**Returns**

  * (::String) — Required. The resource name of the parent Entry Group: `projects/{project}/locations/{location}/entryGroups/{entry_group}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
