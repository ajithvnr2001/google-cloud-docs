---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.WriteOrBuilder
title: Interface WriteOrBuilder (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:18.128786+00:00
---

# Interface WriteOrBuilder (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.WriteOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WriteOrBuilder (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public interface WriteOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCurrentDocument()
    
    
    public abstract Precondition getCurrentDocument()

An optional precondition on the document.

The write will fail if this is set and not met by the target document.

`.google.firestore.v1.Precondition current_document = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Precondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Precondition)` | The currentDocument.  
  
### getCurrentDocumentOrBuilder()
    
    
    public abstract PreconditionOrBuilder getCurrentDocumentOrBuilder()

An optional precondition on the document.

The write will fail if this is set and not met by the target document.

`.google.firestore.v1.Precondition current_document = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PreconditionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.PreconditionOrBuilder)` |   
  
### getDelete()
    
    
    public abstract String getDelete()

A document name to delete. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

`string delete = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The delete.  
  
### getDeleteBytes()
    
    
    public abstract ByteString getDeleteBytes()

A document name to delete. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

`string delete = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for delete.  
  
### getOperationCase()
    
    
    public abstract Write.OperationCase getOperationCase()

**Returns**  
---  
**Type** | **Description**  
`[Write.OperationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Write.OperationCase)` |   
  
### getTransform()
    
    
    public abstract DocumentTransform getTransform()

Applies a transformation to a document.

`.google.firestore.v1.DocumentTransform transform = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DocumentTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentTransform)` | The transform.  
  
### getTransformOrBuilder()
    
    
    public abstract DocumentTransformOrBuilder getTransformOrBuilder()

Applies a transformation to a document.

`.google.firestore.v1.DocumentTransform transform = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DocumentTransformOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentTransformOrBuilder)` |   
  
### getUpdate()
    
    
    public abstract Document getUpdate()

A document to write.

`.google.firestore.v1.Document update = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Document)` | The update.  
  
### getUpdateMask()
    
    
    public abstract DocumentMask getUpdateMask()

The fields to update in this write.

This field can be set only when the operation is `update`. If the mask is not set for an `update` and the document exists, any existing data will be overwritten. If the mask is set and the document on the server has fields not covered by the mask, they are left unchanged. Fields referenced in the mask, but not present in the input document, are deleted from the document on the server. The field paths in this mask must not contain a reserved field name.

`.google.firestore.v1.DocumentMask update_mask = 3;`

**Returns**  
---  
**Type** | **Description**  
`[DocumentMask](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentMask)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract DocumentMaskOrBuilder getUpdateMaskOrBuilder()

The fields to update in this write.

This field can be set only when the operation is `update`. If the mask is not set for an `update` and the document exists, any existing data will be overwritten. If the mask is set and the document on the server has fields not covered by the mask, they are left unchanged. Fields referenced in the mask, but not present in the input document, are deleted from the document on the server. The field paths in this mask must not contain a reserved field name.

`.google.firestore.v1.DocumentMask update_mask = 3;`

**Returns**  
---  
**Type** | **Description**  
`[DocumentMaskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentMaskOrBuilder)` |   
  
### getUpdateOrBuilder()
    
    
    public abstract DocumentOrBuilder getUpdateOrBuilder()

A document to write.

`.google.firestore.v1.Document update = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DocumentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentOrBuilder)` |   
  
### getUpdateTransforms(int index)
    
    
    public abstract DocumentTransform.FieldTransform getUpdateTransforms(int index)

The transforms to perform after update.

This field can be set only when the operation is `update`. If present, this write is equivalent to performing `update` and `transform` to the same document atomically and in order.

`repeated .google.firestore.v1.DocumentTransform.FieldTransform update_transforms = 7; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentTransform.FieldTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentTransform.FieldTransform)` |   
  
### getUpdateTransformsCount()
    
    
    public abstract int getUpdateTransformsCount()

The transforms to perform after update.

This field can be set only when the operation is `update`. If present, this write is equivalent to performing `update` and `transform` to the same document atomically and in order.

`repeated .google.firestore.v1.DocumentTransform.FieldTransform update_transforms = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUpdateTransformsList()
    
    
    public abstract List<DocumentTransform.FieldTransform> getUpdateTransformsList()

The transforms to perform after update.

This field can be set only when the operation is `update`. If present, this write is equivalent to performing `update` and `transform` to the same document atomically and in order.

`repeated .google.firestore.v1.DocumentTransform.FieldTransform update_transforms = 7; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FieldTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentTransform.FieldTransform)>` |   
  
### getUpdateTransformsOrBuilder(int index)
    
    
    public abstract DocumentTransform.FieldTransformOrBuilder getUpdateTransformsOrBuilder(int index)

The transforms to perform after update.

This field can be set only when the operation is `update`. If present, this write is equivalent to performing `update` and `transform` to the same document atomically and in order.

`repeated .google.firestore.v1.DocumentTransform.FieldTransform update_transforms = 7; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentTransform.FieldTransformOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.DocumentTransform.FieldTransformOrBuilder)` |   
  
### getUpdateTransformsOrBuilderList()
    
    
    public abstract List<? extends DocumentTransform.FieldTransformOrBuilder> getUpdateTransformsOrBuilderList()

The transforms to perform after update.

This field can be set only when the operation is `update`. If present, this write is equivalent to performing `update` and `transform` to the same document atomically and in order.

`repeated .google.firestore.v1.DocumentTransform.FieldTransform update_transforms = 7; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.firestore.v1.DocumentTransform.FieldTransformOrBuilder>` |   
  
### hasCurrentDocument()
    
    
    public abstract boolean hasCurrentDocument()

An optional precondition on the document.

The write will fail if this is set and not met by the target document.

`.google.firestore.v1.Precondition current_document = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the currentDocument field is set.  
  
### hasDelete()
    
    
    public abstract boolean hasDelete()

A document name to delete. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.

`string delete = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the delete field is set.  
  
### hasTransform()
    
    
    public abstract boolean hasTransform()

Applies a transformation to a document.

`.google.firestore.v1.DocumentTransform transform = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transform field is set.  
  
### hasUpdate()
    
    
    public abstract boolean hasUpdate()

A document to write.

`.google.firestore.v1.Document update = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the update field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

The fields to update in this write.

This field can be set only when the operation is `update`. If the mask is not set for an `update` and the document exists, any existing data will be overwritten. If the mask is set and the document on the server has fields not covered by the mask, they are left unchanged. Fields referenced in the mask, but not present in the input document, are deleted from the document on the server. The field paths in this mask must not contain a reserved field name.

`.google.firestore.v1.DocumentMask update_mask = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
