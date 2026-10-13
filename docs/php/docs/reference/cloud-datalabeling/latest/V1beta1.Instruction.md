---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.Instruction
title: Google Cloud Datalabeling V1beta1 Client - Class Instruction (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:03.299053+00:00
---

# Google Cloud Datalabeling V1beta1 Client - Class Instruction (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.Instruction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Datalabeling V1beta1 Client - Class Instruction (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.2  0.6.3  0.5.7  0.4.2  0.3.1  0.2.0  0.1.14 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Datalabeling V1beta1 Client class Instruction.

Instruction of how to perform the labeling task for human operators.

Currently only PDF instruction is supported.

Generated from protobuf message `google.cloud.datalabeling.v1beta1.Instruction`

## Namespace

Google \ Cloud \ DataLabeling \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Output only. Instruction resource name, format: projects/{project_id}/instructions/{instruction_id}  
`↳ display_name` |  `string`   
Required. The display name of the instruction. Maximum of 64 characters.  
`↳ description` |  `string`   
Optional. User-provided description of the instruction. The description can be up to 10000 characters long.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Creation time of instruction.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. Last update time of instruction.  
`↳ data_type` |  `int`   
Required. The data type of this instruction.  
`↳ csv_instruction` |  `[CsvInstruction](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.CsvInstruction)`   
Deprecated: this instruction format is not supported any more. Instruction from a CSV file, such as for classification task. The CSV file should have exact two columns, in the following format: * * The first column is labeled data, such as an image reference, text. * * The second column is comma separated labels associated with data.  
`↳ pdf_instruction` |  `[PdfInstruction](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.PdfInstruction)`   
Instruction from a PDF document. The PDF should be in a Cloud Storage bucket.  
`↳ blocking_resources` |  `string[]`   
Output only. The names of any related resources that are blocking changes to the instruction.  
  
### getName

Output only. Instruction resource name, format: projects/{project_id}/instructions/{instruction_id}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Instruction resource name, format: projects/{project_id}/instructions/{instruction_id}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDisplayName

Required. The display name of the instruction. Maximum of 64 characters.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDisplayName

Required. The display name of the instruction. Maximum of 64 characters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. User-provided description of the instruction.

The description can be up to 10000 characters long.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. User-provided description of the instruction.

The description can be up to 10000 characters long.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Creation time of instruction.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Creation time of instruction.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. Last update time of instruction.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. Last update time of instruction.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataType

Required. The data type of this instruction.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DataType](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.DataType).  
  
### setDataType

Required. The data type of this instruction.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DataType](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.DataType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCsvInstruction

Deprecated: this instruction format is not supported any more.

Instruction from a CSV file, such as for classification task. The CSV file should have exact two columns, in the following format:

  * The first column is labeled data, such as an image reference, text.
  * The second column is comma separated labels associated with data.



**Returns**  
---  
**Type** | **Description**  
`[CsvInstruction](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.CsvInstruction)|null` |   
  
### hasCsvInstruction

### clearCsvInstruction

### setCsvInstruction

Deprecated: this instruction format is not supported any more.

Instruction from a CSV file, such as for classification task. The CSV file should have exact two columns, in the following format:

  * The first column is labeled data, such as an image reference, text.
  * The second column is comma separated labels associated with data.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CsvInstruction](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.CsvInstruction)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPdfInstruction

Instruction from a PDF document. The PDF should be in a Cloud Storage bucket.

**Returns**  
---  
**Type** | **Description**  
`[PdfInstruction](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.PdfInstruction)|null` |   
  
### hasPdfInstruction

### clearPdfInstruction

### setPdfInstruction

Instruction from a PDF document. The PDF should be in a Cloud Storage bucket.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PdfInstruction](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.PdfInstruction)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBlockingResources

Output only. The names of any related resources that are blocking changes to the instruction.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setBlockingResources

Output only. The names of any related resources that are blocking changes to the instruction.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
