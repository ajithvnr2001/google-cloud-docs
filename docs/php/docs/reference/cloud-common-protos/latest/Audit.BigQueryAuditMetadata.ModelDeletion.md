---
url: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.ModelDeletion
title: Common Protos for Google Cloud APIs Client - Class ModelDeletion (1.0.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:49.885129+00:00
---

# Common Protos for Google Cloud APIs Client - Class ModelDeletion (1.0.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.ModelDeletion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Common Protos for Google Cloud APIs Client - Class ModelDeletion (1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.0  0.8.3  0.7.0  0.6.0  0.5.2  0.4.2  0.3.8 

Reference documentation and code samples for the Common Protos for Google Cloud APIs Client class ModelDeletion.

Model deletion event.

Generated from protobuf message `google.cloud.audit.BigQueryAuditMetadata.ModelDeletion`

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
`↳ reason` |  `int`   
Describes how the model was deleted.  
`↳ job_name` |  `string`   
The URI of the job that deleted a model. Present if the reason is QUERY. Format: `projects/<project_id>/jobs/<job_id>`.  
  
### getReason

Describes how the model was deleted.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Reason](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.ModelDeletion.Reason).  
  
### setReason

Describes how the model was deleted.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Reason](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/Audit.BigQueryAuditMetadata.ModelDeletion.Reason).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getJobName

The URI of the job that deleted a model.

Present if the reason is QUERY. Format: `projects/<project_id>/jobs/<job_id>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setJobName

The URI of the job that deleted a model.

Present if the reason is QUERY. Format: `projects/<project_id>/jobs/<job_id>`.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
