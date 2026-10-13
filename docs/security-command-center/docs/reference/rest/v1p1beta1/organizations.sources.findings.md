---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings
title: REST Resource: organizations.sources.findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:59:42.124234+00:00
---

# REST Resource: organizations.sources.findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  REST Resource: organizations.sources.findings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Finding
    * JSON representation
  * State
  * SecurityMarks
    * JSON representation
  * Severity
  * Methods



## Resource: Finding

Security Command Center finding.

A finding is a record of assessment data (security, risk, health or privacy) ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, an XSS vulnerability in an App Engine application is a finding.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "resourceName": string,
      "state": enum ([State](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#State)),
      "category": string,
      "externalUri": string,
      "sourceProperties": {
        string: value,
        ...
      },
      "securityMarks": {
        object ([SecurityMarks](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#SecurityMarks))
      },
      "eventTime": string,
      "createTime": string,
      "severity": enum ([Severity](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#Severity)),
      "canonicalName": string
    }  
  
Fields  
---  
`name` |  `string` The relative resource name of this finding. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Example: "organizations/{organizationId}/sources/{source_id}/findings/{findingId}"  
`parent` |  `string` The relative resource name of the source the finding belongs to. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> This field is immutable after creation time. For example: "organizations/{organizationId}/sources/{source_id}"  
`resourceName` |  `string` For findings on Google Cloud resources, the full resource name of the Google Cloud resource this finding is for. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name> When the finding is for a non-Google Cloud resource, the resourceName can be a customer or partner defined string. This field is immutable after creation time.  
`state` |  `enum (`[State](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#State)`)` The state of the finding.  
`category` |  `string` The additional taxonomy group within findings from a given source. This field is immutable after creation time. Example: "XSS_FLASH_INJECTION"  
`externalUri` |  `string` The URI that, if available, points to a web page outside of Security Command Center where additional information about the finding can be found. This field is guaranteed to be either empty or a well formed URL.  
`sourceProperties` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Source specific properties. These properties are managed by the source that writes the finding. The key names in the sourceProperties map must be between 1 and 255 characters, and must start with a letter and contain alphanumeric characters or underscores only.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`securityMarks` |  `object (`[SecurityMarks](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#SecurityMarks)`)` Output only. User specified security marks. These marks are entirely managed by the user and come from the SecurityMarks resource that belongs to the finding.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the event took place, or when an update to the finding occurred. For example, if the finding represents an open firewall it would capture the time the detector believes the firewall became open. The accuracy is determined by the detector. If the finding were to be resolved afterward, this time would reflect when the finding was resolved. Must not be set to a value greater than the current timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the finding was created in Security Command Center.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings#Severity)`)` The severity of the finding. This field is managed by the source that writes the finding.  
`canonicalName` |  `string` The canonical name of the finding. It's either "organizations/{organizationId}/sources/{source_id}/findings/{findingId}", "folders/{folder_id}/sources/{source_id}/findings/{findingId}" or "projects/{project_number}/sources/{source_id}/findings/{findingId}", depending on the closest CRM ancestor of the resource associated with the finding.  
  
## State

The state of the finding.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The finding requires attention and has not been addressed yet.  
`INACTIVE` | The finding has been fixed, triaged as a non-issue or otherwise addressed and is no longer active.  
  
## SecurityMarks

User specified security marks that are attached to the parent Security Command Center resource. Security marks are scoped within a Security Command Center organization -- they can be modified and viewed by all users who have proper permissions on the organization.

JSON representation  
---  
      
    
    {
      "name": string,
      "marks": {
        string: string,
        ...
      },
      "canonicalName": string
    }  
  
Fields  
---  
`name` |  `string` The relative resource name of the SecurityMarks. See: <https://cloud.google.com/apis/design/resource_names#relative_resource_name> Examples: "organizations/{organizationId}/assets/{asset_id}/securityMarks" "organizations/{organizationId}/sources/{source_id}/findings/{findingId}/securityMarks".  
`marks` |  `map (key: string, value: string)` Mutable user specified security marks belonging to the parent resource. Constraints are as follows:

  * Keys and values are treated as case insensitive
  * Keys must be between 1 - 256 characters (inclusive)
  * Keys must be letters, numbers, underscores, or dashes
  * Values have leading and trailing whitespace trimmed, remaining characters must be between 1 - 4096 characters (inclusive)

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`canonicalName` |  `string` The canonical name of the marks. Examples: "organizations/{organizationId}/assets/{asset_id}/securityMarks" "folders/{folder_id}/assets/{asset_id}/securityMarks" "projects/{project_number}/assets/{asset_id}/securityMarks" "organizations/{organizationId}/sources/{source_id}/findings/{findingId}/securityMarks" "folders/{folder_id}/sources/{source_id}/findings/{findingId}/securityMarks" "projects/{project_number}/sources/{source_id}/findings/{findingId}/securityMarks"  
  
## Severity

The severity of the finding. This field is managed by the source that writes the finding.

Enums  
---  
`SEVERITY_UNSPECIFIED` | No severity specified. The default value.  
`CRITICAL` | Critical severity.  
`HIGH` | High severity.  
`MEDIUM` | Medium severity.  
`LOW` | Low severity.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/create)`

|  Creates a finding.  
  
### `[group](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/group)`

|  Filters an organization or source's findings and groups them by their specified properties.  
  
### `[list](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/list)`

|  Lists an organization or source's findings.  
  
### `[patch](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/patch)`

|  Creates or updates a finding.  
  
### `[setState](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/setState)`

|  Updates the state of a finding.  
  
### `[updateSecurityMarks](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1p1beta1/organizations.sources.findings/updateSecurityMarks)`

|  Updates security marks.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-02 UTC."],[],[]] 
