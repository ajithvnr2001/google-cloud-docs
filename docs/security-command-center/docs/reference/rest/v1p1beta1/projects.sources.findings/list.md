---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/projects.sources.findings/list/
title: Method: projects.sources.findings.list \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:21.971956+00:00
---

# Method: projects.sources.findings.list  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/projects.sources.findings/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: projects.sources.findings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists an organization or source's findings.

To list across all sources provide a `-` as the source id. Example: /v1p1beta1/organizations/{organizationId}/sources/-/findings

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`GET https://securitycenter.googleapis.com/v1p1beta1/{parent=projects/*/sources/*}/findings`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the source the findings belong to. Its format is "organizations/[organizationId]/sources/[source_id], folders/[folder_id]/sources/[source_id], or projects/[projectId]/sources/[source_id]". To list across all sources provide a source_id of `-`. For example: organizations/{organizationId}/sources/-, folders/{folder_id}/sources/- or projects/{projects_id}/sources/-  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Expression that defines the filter to apply across findings. The expression is a list of one or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. Examples include:

  * name
  * sourceProperties.a_property
  * securityMarks.marks.marka

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
  * parent: `=`, `:`
  * resourceName: `=`, `:`
  * state: `=`, `:`
  * category: `=`, `:`
  * externalUri: `=`, `:`
  * eventTime: `=`, `>`, `<`, `>=`, `<=`
  * severity: `=`, `:`

Usage: This should be milliseconds since epoch or an RFC3339 string. Examples: `eventTime = "2019-06-10T16:07:18-07:00"` `eventTime = 1560208038000`securityMarks.marks: `=`, `:` sourceProperties: `=`, `:`, `>`, `<`, `>=`, `<=`For example, `sourceProperties.size = 100` is a valid filter string.Use a partial match on the empty string to filter based on a property existing: `sourceProperties.my_property : ""`Use a negated partial match on the empty string to filter based on a property not existing: `-sourceProperties.my_property : ""`  
`orderBy` |  `string` Expression that defines what fields and order to use for sorting. The string value should follow SQL syntax: comma separated list of fields. For example: "name,resourceProperties.a_property". The default sorting order is ascending. To specify descending order for a field, a suffix " desc" should be appended to the field name. For example: "name desc,sourceProperties.a_property". Redundant space characters in the syntax are insignificant. "name desc,sourceProperties.a_property" and " name desc , sourceProperties.a_property " are equivalent.The following fields are supported: name parent state category resourceName eventTime sourceProperties securityMarks.marks  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time used as a reference point when filtering findings. The filter is limited to findings existing at the supplied time and their values are those at that specific time. Absence of this field will default to the API's version of NOW.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`compareDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` When compareDuration is set, the ListFindingsResult's "stateChange" attribute is updated to indicate whether the finding had its state changed, the finding's state remained unchanged, or if the finding was added in any state during the compareDuration period of time that precedes the readTime. This is the time between (readTime - compareDuration) and readTime.The stateChange value is derived based on the presence and state of the finding at the two points in time. Intermediate state changes between the two times don't affect the result. For example, the results aren't affected if the finding is made inactive and then active again.Possible "stateChange" values when compareDuration is specified:

  * "CHANGED": indicates that the finding was present and matched the given filter at the start of compareDuration, but changed its state at readTime.
  * "UNCHANGED": indicates that the finding was present and matched the given filter at the start of compareDuration and did not change state at readTime.
  * "ADDED": indicates that the finding did not match the given filter or was not present at the start of compareDuration, but was present at readTime.
  * "REMOVED": indicates that the finding was present and matched the filter at the start of compareDuration, but did not match the filter at readTime.

If compareDuration is not specified, then the only possible stateChange is "UNUSED", which will be the stateChange set for all findings present at readTime.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`fieldMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` A field mask to specify the Finding fields to be listed in the response. An empty field mask will list all fields.  
`pageToken` |  `string` The value returned by the last `ListFindingsResponse`; indicates that this is a continuation of a prior `findings.list` call, and that the system should return the next page of data.  
`pageSize` |  `integer` The maximum number of results to return in a single response. Default is 10, minimum is 1, maximum is 1000.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListFindingsResponse](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/ListFindingsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
