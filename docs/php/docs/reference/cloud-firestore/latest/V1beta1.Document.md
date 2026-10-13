---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Document
title: Cloud Firestore V1beta1 Client - Class Document (2.2.0-RC1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:38.920462+00:00
---

# Cloud Firestore V1beta1 Client - Class Document (2.2.0-RC1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Document

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore V1beta1 Client - Class Document (2.2.0-RC1) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Cloud Firestore V1beta1 Client class Document.

A Firestore document.

Must not exceed 1 MiB - 4 bytes.

Generated from protobuf message `google.firestore.v1beta1.Document`

## Namespace

Google \ Cloud \ Firestore \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
The resource name of the document, for example `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`↳ fields` |  `array|[Google\Protobuf\Internal\MapField](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Internal/MapField)`   
The document's fields. The map keys represent field names. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by the simple or quoted field names of the containing fields, delimited by `.`. For example, the structured field `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be represented by the field path `foo.x&y`. Within a field path, a quoted field name starts and ends with `` ` and may contain any character. Some characters, including `` `, must be escaped using a `\`. For example, ``x&y` ` represents `x&y` and ``bak\`tik` ` represents `bak`tik`.  
`↳ create_time` |  `[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)`   
Output only. The time at which the document was created. This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query.  
`↳ update_time` |  `[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)`   
Output only. The time at which the document was last changed. This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query.  
  
### getName

The resource name of the document, for example `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The resource name of the document, for example `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFields

The document's fields.

The map keys represent field names. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by the simple or quoted field names of the containing fields, delimited by `.`. For example, the structured field `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be represented by the field path `foo.x&y`. Within a field path, a quoted field name starts and ends with `` ` and may contain any character. Some characters, including `` `, must be escaped using a `\`. For example, ``x&y` ` represents `x&y` and ``bak\`tik` ` represents `bak`tik`.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Internal\MapField](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Internal/MapField)` |   
  
### setFields

The document's fields.

The map keys represent field names. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by the simple or quoted field names of the containing fields, delimited by `.`. For example, the structured field `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be represented by the field path `foo.x&y`. Within a field path, a quoted field name starts and ends with `` ` and may contain any character. Some characters, including `` `, must be escaped using a `\`. For example, ``x&y` ` represents `x&y` and ``bak\`tik` ` represents `bak`tik`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|[Google\Protobuf\Internal\MapField](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Internal/MapField)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time at which the document was created.

This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)` |   
  
### setCreateTime

Output only. The time at which the document was created.

This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The time at which the document was last changed.

This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)` |   
  
### setUpdateTime

Output only. The time at which the document was last changed.

This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Timestamp](https://protobuf.dev/reference/php/api-docs/Google/Protobuf/Timestamp)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
