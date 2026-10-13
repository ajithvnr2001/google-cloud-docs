---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/referencelist/verify-reference-list/
title: VerifyReferenceList parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:14.475433+00:00
---

# VerifyReferenceList parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/referencelist/verify-reference-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VerifyReferenceList parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Reference List API (**`VerifyReferenceList`**) to the modern Chronicle API (**`VerifyReferenceList`**).

## Protocol and mapping overview

Feature | Legacy API (`VerifyReferenceList`) | Modern Chronicle API (`VerifyReferenceList`)  
---|---|---  
**HTTP Method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/referenceLists.verifyReferenceList`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `VerifyReferenceListRequest` scopes verification under a target instance and standardizes list item entries into structured messages.

Legacy Field (`VerifyReferenceListRequest`) | Modern Field (`VerifyReferenceListRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / New Field:** Legacy validation was stateless and unconstrained by resource bounds. The modern API requires specifying the target environment instance path: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`content_type` | `syntax_type` | `enum` | **Renamed / Value Alignment:** Renamed from `content_type` to `syntax_type`. Enum value translations:  
• `CONTENT_TYPE_DEFAULT_STRING` $\rightarrow$ `REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING`  
• `REGEX` $\rightarrow$ `REFERENCE_LIST_SYNTAX_TYPE_REGEX` (for regular expressions)  
• `CIDR` $\rightarrow$ `REFERENCE_LIST_SYNTAX_TYPE_CIDR`. Rename to `syntaxType` in JSON.  
`lines` | `entries` | `repeated string` $\rightarrow$ `repeated ReferenceListEntry` | **Restructured:** Legacy flat array of string lines is restructured into a repeated list of `ReferenceListEntry` messages (`entries[].value`).  
  
### Nested ReferenceListEntry property mappings

The fields mapping inside individual `ReferenceListEntry` items is as follows:

Legacy Field (`lines[]` string item) | Modern Field (`ReferenceListEntry` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`lines[]` _(Plain text line string)_ | `value` | `string` | **Parity Mapped:** The individual string line item is encapsulated inside the required `value` property of each `ReferenceListEntry` object.  
  
* * *

## Response payload field-by-field parity

Both APIs return validation results and line-by-line syntax error arrays.

Legacy Field (`VerifyReferenceListResponse`) | Modern Field (`VerifyReferenceListResponse`) | Field type | Parity & Migration Notes  
---|---|---|---  
`success` | `success` | `bool` | **Parity Mapped:** Boolean flag returning true if the submitted list content passes validation without syntax errors.  
`errors` | `errors` | `repeated ReferenceListError` | **Parity Mapped / Restructured:** Array of encountered line-level syntax validation errors (mappings evaluated in the following table).  
  
### Nested ReferenceListError property mappings

The fields mapping inside individual `ReferenceListError` items is as follows:

Legacy Field (`ReferenceListLineError`) | Modern Field (`ReferenceListError` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`line_number` | `line_number` | `int32` | **Parity Mapped:** 1-indexed line number where the validation error occurred (general list-wide errors are indexed at -1). Rename to `lineNumber` in JSON.  
`error_message` | `error_message` | `string` | **Parity Mapped:** Diagnostic text explaining why the syntax or line entry is invalid. Rename to `errorMessage` in JSON.  
  
* * *

## Key differences

  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Payload Restructuring:**
    * Plain string line arrays in legacy `lines` are wrapped inside structured `ReferenceListEntry` messages under `entries` (for example, `repeated string` $\rightarrow$ `repeated ReferenceListEntry`).
  * **Syntax Type and Field Renaming:**
    * Legacy `content_type` is renamed to `syntax_type` with clearer enum prefixing (`REFERENCE_LIST_SYNTAX_TYPE_*`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
