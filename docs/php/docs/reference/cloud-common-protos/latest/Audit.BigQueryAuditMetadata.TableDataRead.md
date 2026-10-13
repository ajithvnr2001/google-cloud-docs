---
url: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.TableDataRead
title: Common Protos for Google Cloud APIs Client - Class TableDataRead (1.0.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:44.112419+00:00
---

# Common Protos for Google Cloud APIs Client - Class TableDataRead (1.0.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.TableDataRead

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Common Protos for Google Cloud APIs Client - Class TableDataRead (1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.0  0.8.3  0.7.0  0.6.0  0.5.2  0.4.2  0.3.8 

Reference documentation and code samples for the Common Protos for Google Cloud APIs Client class TableDataRead.

Table data read event.

Generated from protobuf message `google.cloud.audit.BigQueryAuditMetadata.TableDataRead`

## Namespace

Google \ Cloud \ Audit \ BigQueryAuditMetadata

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ fields` |  `string[]`   
List of the accessed fields. Entire list is truncated if the record size exceeds 100K.  
`↳ fields_truncated` |  `bool`   
True if the fields list was truncated.  
`↳ policy_tags` |  `string[]`   
List of the referenced policy tags. That is, policy tags attached to the accessed fields or their ancestors. Policy tag resource name is a string of the format: `projects/<project_id>/locations/<location_id>/taxonomies/<taxonomy_id>/policyTags/<policy_tag_id>`  
`↳ policy_tags_truncated` |  `bool`   
True if the policy tag list was truncated. At most 100 policy tags can be saved.  
`↳ reason` |  `int`   
Describes how the table data was read.  
`↳ job_name` |  `string`   
The URI of the job that read a table. Present if the reason is JOB but can be redacted for privacy reasons. Format: `projects/<project_id>/jobs/<job_id>`.  
`↳ session_name` |  `string`   
The URI of the read session that read a table. Present if the reason is CREATE_READ_SESSION. Format: `projects/<project_id>/locations/<location>/sessions/<session_id>`.  
  
### getFields

List of the accessed fields. Entire list is truncated if the record size exceeds 100K.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setFields

List of the accessed fields. Entire list is truncated if the record size exceeds 100K.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFieldsTruncated

True if the fields list was truncated.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setFieldsTruncated

True if the fields list was truncated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPolicyTags

List of the referenced policy tags. That is, policy tags attached to the accessed fields or their ancestors.

Policy tag resource name is a string of the format: `projects/<project_id>/locations/<location_id>/taxonomies/<taxonomy_id>/policyTags/<policy_tag_id>`

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setPolicyTags

List of the referenced policy tags. That is, policy tags attached to the accessed fields or their ancestors.

Policy tag resource name is a string of the format: `projects/<project_id>/locations/<location_id>/taxonomies/<taxonomy_id>/policyTags/<policy_tag_id>`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPolicyTagsTruncated

True if the policy tag list was truncated. At most 100 policy tags can be saved.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setPolicyTagsTruncated

True if the policy tag list was truncated. At most 100 policy tags can be saved.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReason

Describes how the table data was read.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Reason](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.TableDataRead.Reason).  
  
### setReason

Describes how the table data was read.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Reason](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.TableDataRead.Reason).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getJobName

The URI of the job that read a table.

Present if the reason is JOB but can be redacted for privacy reasons. Format: `projects/<project_id>/jobs/<job_id>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setJobName

The URI of the job that read a table.

Present if the reason is JOB but can be redacted for privacy reasons. Format: `projects/<project_id>/jobs/<job_id>`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSessionName

The URI of the read session that read a table.

Present if the reason is CREATE_READ_SESSION. Format: `projects/<project_id>/locations/<location>/sessions/<session_id>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSessionName

The URI of the read session that read a table.

Present if the reason is CREATE_READ_SESSION. Format: `projects/<project_id>/locations/<location>/sessions/<session_id>`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
