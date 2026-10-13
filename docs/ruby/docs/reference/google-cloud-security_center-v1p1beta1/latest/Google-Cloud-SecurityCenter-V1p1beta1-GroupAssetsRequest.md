---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-GroupAssetsRequest/
title: Cloud Security Command Center V1p1beta1 API - Class Google::Cloud::SecurityCenter::V1p1beta1::GroupAssetsRequest (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:25.744215+00:00
---

# Cloud Security Command Center V1p1beta1 API - Class Google::Cloud::SecurityCenter::V1p1beta1::GroupAssetsRequest (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter-V1p1beta1-GroupAssetsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Command Center V1p1beta1 API - Class Google::Cloud::SecurityCenter::V1p1beta1::GroupAssetsRequest (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.2  0.13.2  0.12.0  0.11.2  0.10.0  0.9.0  0.8.0  0.7.5 

Reference documentation and code samples for the Cloud Security Command Center V1p1beta1 API class Google::Cloud::SecurityCenter::V1p1beta1::GroupAssetsRequest.

Request message for grouping by assets.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #compare_duration
    
    
    def compare_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Protobuf-Duration)) — When compare_duration is set, the GroupResult's "state_change" property is updated to indicate whether the asset was added, removed, or remained present during the compare_duration period of time that precedes the read_time. This is the time between (read_time - compare_duration) and read_time.

The state change value is derived based on the presence of the asset at the two points in time. Intermediate state changes between the two times don't affect the result. For example, the results aren't affected if the asset is removed and re-created again.

Possible "state_change" values when compare_duration is specified:

    * "ADDED": indicates that the asset was not present at the start of compare_duration, but present at reference_time.
    * "REMOVED": indicates that the asset was present at the start of compare_duration, but not present at reference_time.
    * "ACTIVE": indicates that the asset was present at both the start and the end of the time period defined by compare_duration and reference_time.

If compare_duration is not specified, then the only possible state_change is "UNUSED", which will be the state_change set for all assets present at read_time.

If this field is set then `state_change` must be a specified field in `group_by`. 




### #compare_duration=
    
    
    def compare_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Protobuf-Duration)) — When compare_duration is set, the GroupResult's "state_change" property is updated to indicate whether the asset was added, removed, or remained present during the compare_duration period of time that precedes the read_time. This is the time between (read_time - compare_duration) and read_time.

The state change value is derived based on the presence of the asset at the two points in time. Intermediate state changes between the two times don't affect the result. For example, the results aren't affected if the asset is removed and re-created again.

Possible "state_change" values when compare_duration is specified:

    * "ADDED": indicates that the asset was not present at the start of compare_duration, but present at reference_time.
    * "REMOVED": indicates that the asset was present at the start of compare_duration, but not present at reference_time.
    * "ACTIVE": indicates that the asset was present at both the start and the end of the time period defined by compare_duration and reference_time.

If compare_duration is not specified, then the only possible state_change is "UNUSED", which will be the state_change set for all assets present at read_time.

If this field is set then `state_change` must be a specified field in `group_by`. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Protobuf-Duration)) — When compare_duration is set, the GroupResult's "state_change" property is updated to indicate whether the asset was added, removed, or remained present during the compare_duration period of time that precedes the read_time. This is the time between (read_time - compare_duration) and read_time.

The state change value is derived based on the presence of the asset at the two points in time. Intermediate state changes between the two times don't affect the result. For example, the results aren't affected if the asset is removed and re-created again.

Possible "state_change" values when compare_duration is specified:

    * "ADDED": indicates that the asset was not present at the start of compare_duration, but present at reference_time.
    * "REMOVED": indicates that the asset was present at the start of compare_duration, but not present at reference_time.
    * "ACTIVE": indicates that the asset was present at both the start and the end of the time period defined by compare_duration and reference_time.

If compare_duration is not specified, then the only possible state_change is "UNUSED", which will be the state_change set for all assets present at read_time.

If this field is set then `state_change` must be a specified field in `group_by`. 




### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Expression that defines the filter to apply across assets. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.

Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the Asset resource. Examples include:

    * name
    * security_center_properties.resource_name
    * resource_properties.a_property
    * security_marks.marks.marka

The supported operators are:

    * `=` for all value types.
    * `>`, `<`, `>=`, `<=` for integer values.
    * `:`, meaning substring matching, for strings.

The supported value types are:

    * string literals in quotes.
    * integer literals without quotes.
    * boolean literals `true` and `false` without quotes.

The following field and operator combinations are supported:

    * name: `=`
    * update_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `update_time = "2019-06-10T16:07:18-07:00"` `update_time = 1560208038000`

    * create_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `create_time = "2019-06-10T16:07:18-07:00"` `create_time = 1560208038000`

    * iam_policy.policy_blob: `=`, `:`
    * resource_properties: `=`, `:`, `>`, `<`, `>=`, `<=`
    * security_marks.marks: `=`, `:`
    * security_center_properties.resource_name: `=`, `:`
    * security_center_properties.resource_name_display_name: `=`, `:`
    * security_center_properties.resource_type: `=`, `:`
    * security_center_properties.resource_parent: `=`, `:`
    * security_center_properties.resource_parent_display_name: `=`, `:`
    * security_center_properties.resource_project: `=`, `:`
    * security_center_properties.resource_project_display_name: `=`, `:`
    * security_center_properties.resource_owners: `=`, `:`

For example, `resource_properties.size = 100` is a valid filter string.

Use a partial match on the empty string to filter based on a property existing: `resource_properties.my_property : ""`

Use a negated partial match on the empty string to filter based on a property not existing: `-resource_properties.my_property : ""`




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Expression that defines the filter to apply across assets. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.

Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the Asset resource. Examples include:

    * name
    * security_center_properties.resource_name
    * resource_properties.a_property
    * security_marks.marks.marka

The supported operators are:

    * `=` for all value types.
    * `>`, `<`, `>=`, `<=` for integer values.
    * `:`, meaning substring matching, for strings.

The supported value types are:

    * string literals in quotes.
    * integer literals without quotes.
    * boolean literals `true` and `false` without quotes.

The following field and operator combinations are supported:

    * name: `=`
    * update_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `update_time = "2019-06-10T16:07:18-07:00"` `update_time = 1560208038000`

    * create_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `create_time = "2019-06-10T16:07:18-07:00"` `create_time = 1560208038000`

    * iam_policy.policy_blob: `=`, `:`
    * resource_properties: `=`, `:`, `>`, `<`, `>=`, `<=`
    * security_marks.marks: `=`, `:`
    * security_center_properties.resource_name: `=`, `:`
    * security_center_properties.resource_name_display_name: `=`, `:`
    * security_center_properties.resource_type: `=`, `:`
    * security_center_properties.resource_parent: `=`, `:`
    * security_center_properties.resource_parent_display_name: `=`, `:`
    * security_center_properties.resource_project: `=`, `:`
    * security_center_properties.resource_project_display_name: `=`, `:`
    * security_center_properties.resource_owners: `=`, `:`

For example, `resource_properties.size = 100` is a valid filter string.

Use a partial match on the empty string to filter based on a property existing: `resource_properties.my_property : ""`

Use a negated partial match on the empty string to filter based on a property not existing: `-resource_properties.my_property : ""`




**Returns**

  * (::String) — Expression that defines the filter to apply across assets. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.

Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the Asset resource. Examples include:

    * name
    * security_center_properties.resource_name
    * resource_properties.a_property
    * security_marks.marks.marka

The supported operators are:

    * `=` for all value types.
    * `>`, `<`, `>=`, `<=` for integer values.
    * `:`, meaning substring matching, for strings.

The supported value types are:

    * string literals in quotes.
    * integer literals without quotes.
    * boolean literals `true` and `false` without quotes.

The following field and operator combinations are supported:

    * name: `=`
    * update_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `update_time = "2019-06-10T16:07:18-07:00"` `update_time = 1560208038000`

    * create_time: `=`, `>`, `<`, `>=`, `<=`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `create_time = "2019-06-10T16:07:18-07:00"` `create_time = 1560208038000`

    * iam_policy.policy_blob: `=`, `:`
    * resource_properties: `=`, `:`, `>`, `<`, `>=`, `<=`
    * security_marks.marks: `=`, `:`
    * security_center_properties.resource_name: `=`, `:`
    * security_center_properties.resource_name_display_name: `=`, `:`
    * security_center_properties.resource_type: `=`, `:`
    * security_center_properties.resource_parent: `=`, `:`
    * security_center_properties.resource_parent_display_name: `=`, `:`
    * security_center_properties.resource_project: `=`, `:`
    * security_center_properties.resource_project_display_name: `=`, `:`
    * security_center_properties.resource_owners: `=`, `:`

For example, `resource_properties.size = 100` is a valid filter string.

Use a partial match on the empty string to filter based on a property existing: `resource_properties.my_property : ""`

Use a negated partial match on the empty string to filter based on a property not existing: `-resource_properties.my_property : ""`




### #group_by
    
    
    def group_by() -> ::String

**Returns**

  * (::String) — 

Required. Expression that defines what assets fields to use for grouping. The string value should follow SQL syntax: comma separated list of fields. For example: "security_center_properties.resource_project,security_center_properties.project".

The following fields are supported when compare_duration is not set:

    * security_center_properties.resource_project
    * security_center_properties.resource_project_display_name
    * security_center_properties.resource_type
    * security_center_properties.resource_parent
    * security_center_properties.resource_parent_display_name

The following fields are supported when compare_duration is set:

    * security_center_properties.resource_type
    * security_center_properties.resource_project_display_name
    * security_center_properties.resource_parent_display_name



### #group_by=
    
    
    def group_by=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. Expression that defines what assets fields to use for grouping. The string value should follow SQL syntax: comma separated list of fields. For example: "security_center_properties.resource_project,security_center_properties.project".

The following fields are supported when compare_duration is not set:

    * security_center_properties.resource_project
    * security_center_properties.resource_project_display_name
    * security_center_properties.resource_type
    * security_center_properties.resource_parent
    * security_center_properties.resource_parent_display_name

The following fields are supported when compare_duration is set:

    * security_center_properties.resource_type
    * security_center_properties.resource_project_display_name
    * security_center_properties.resource_parent_display_name



**Returns**

  * (::String) — 

Required. Expression that defines what assets fields to use for grouping. The string value should follow SQL syntax: comma separated list of fields. For example: "security_center_properties.resource_project,security_center_properties.project".

The following fields are supported when compare_duration is not set:

    * security_center_properties.resource_project
    * security_center_properties.resource_project_display_name
    * security_center_properties.resource_type
    * security_center_properties.resource_parent
    * security_center_properties.resource_parent_display_name

The following fields are supported when compare_duration is set:

    * security_center_properties.resource_type
    * security_center_properties.resource_project_display_name
    * security_center_properties.resource_parent_display_name



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 



**Returns**

  * (::Integer) — The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The value returned by the last `GroupAssetsResponse`; indicates that this is a continuation of a prior `GroupAssets` call, and that the system should return the next page of data. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The value returned by the last `GroupAssetsResponse`; indicates that this is a continuation of a prior `GroupAssets` call, and that the system should return the next page of data. 



**Returns**

  * (::String) — The value returned by the last `GroupAssetsResponse`; indicates that this is a continuation of a prior `GroupAssets` call, and that the system should return the next page of data. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Name of the organization to groupBy. Its format is "organizations/[organization_id], folders/[folder_id], or projects/[project_id]". 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the organization to groupBy. Its format is "organizations/[organization_id], folders/[folder_id], or projects/[project_id]". 



**Returns**

  * (::String) — Required. Name of the organization to groupBy. Its format is "organizations/[organization_id], folders/[folder_id], or projects/[project_id]". 



### #read_time
    
    
    def read_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time used as a reference point when filtering assets. The filter is limited to assets existing at the supplied time and their values are those at that specific time. Absence of this field will default to the API's version of NOW. 



### #read_time=
    
    
    def read_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time used as a reference point when filtering assets. The filter is limited to assets existing at the supplied time and their values are those at that specific time. Absence of this field will default to the API's version of NOW. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time used as a reference point when filtering assets. The filter is limited to assets existing at the supplied time and their values are those at that specific time. Absence of this field will default to the API's version of NOW. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
