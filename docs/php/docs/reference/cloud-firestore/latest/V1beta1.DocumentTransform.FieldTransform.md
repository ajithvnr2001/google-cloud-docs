---
url: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.DocumentTransform.FieldTransform
title: Cloud Firestore V1beta1 Client - Class FieldTransform (2.2.0-RC1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:27.122774+00:00
---

# Cloud Firestore V1beta1 Client - Class FieldTransform (2.2.0-RC1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.DocumentTransform.FieldTransform

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Firestore V1beta1 Client - Class FieldTransform (2.2.0-RC1) Stay organized with collections  Save and categorize content based on your preferences. 

2.3.3 (latest)  2.2.0-RC1  2.1.0  2.0.2-RC1  1.55.0  1.54.4  1.53.1  1.52.0  1.51.0  1.50.0  1.48.1  1.47.3  1.46.0  1.45.2  1.44.1  1.43.3  1.40.0  1.39.0  1.38.0  1.37.7  1.36.1  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.28.0  1.27.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Cloud Firestore V1beta1 Client class FieldTransform.

A transformation of a field of the document.

Generated from protobuf message `google.firestore.v1beta1.DocumentTransform.FieldTransform`

## Namespace

Google \ Cloud \ Firestore \ V1beta1 \ DocumentTransform

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ field_path` |  `string`   
The path of the field. See [Document.fields](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Document#_Google_Cloud_Firestore_V1beta1_Document__getFields__) for the field path syntax reference.  
`↳ set_to_server_value` |  `int`   
Sets the field to the given server value.  
`↳ increment` |  `[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)`   
Adds the given value to the field's current value. This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If either of the given value or the current field value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the field is resolved to the largest magnitude positive/negative integer.  
`↳ maximum` |  `[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)`   
Sets the field to the maximum of its current value and the given value. This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a maximum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the larger operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The maximum of a zero stored value and zero input value is always the stored value. The maximum of any numeric value x and NaN is NaN.  
`↳ minimum` |  `[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)`   
Sets the field to the minimum of its current value and the given value. This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the input value. If a minimum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the smaller operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The minimum of a zero stored value and zero input value is always the stored value. The minimum of any numeric value x and NaN is NaN.  
`↳ append_missing_elements` |  `[Google\Cloud\Firestore\V1beta1\ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)`   
Append the given elements in order if they are not already present in the current field value. If the field is not an array, or if the field does not yet exist, it is first set to the empty array. Equivalent numbers of different types (e.g. 3L and 3.0) are considered equal when checking if a value is missing. NaN is equal to NaN, and Null is equal to Null. If the input contains multiple equivalent values, only the first will be considered. The corresponding transform_result will be the null value.  
`↳ remove_all_from_array` |  `[Google\Cloud\Firestore\V1beta1\ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)`   
Remove all of the given elements from the array in the field. If the field is not an array, or if the field does not yet exist, it is set to the empty array. Equivalent numbers of the different types (e.g. 3L and 3.0) are considered equal when deciding whether an element should be removed. NaN is equal to NaN, and Null is equal to Null. This will remove all equivalent values if there are duplicates. The corresponding transform_result will be the null value.  
  
### getFieldPath

The path of the field. See [Document.fields](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Document#_Google_Cloud_Firestore_V1beta1_Document__getFields__) for the field path syntax reference.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFieldPath

The path of the field. See [Document.fields](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Document#_Google_Cloud_Firestore_V1beta1_Document__getFields__) for the field path syntax reference.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSetToServerValue

Sets the field to the given server value.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ServerValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.DocumentTransform.FieldTransform.ServerValue).  
  
### setSetToServerValue

Sets the field to the given server value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ServerValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.DocumentTransform.FieldTransform.ServerValue).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIncrement

Adds the given value to the field's current value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If either of the given value or the current field value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the field is resolved to the largest magnitude positive/negative integer.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)` |   
  
### setIncrement

Adds the given value to the field's current value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If either of the given value or the current field value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the field is resolved to the largest magnitude positive/negative integer.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaximum

Sets the field to the maximum of its current value and the given value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a maximum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the larger operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The maximum of a zero stored value and zero input value is always the stored value. The maximum of any numeric value x and NaN is NaN.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)` |   
  
### setMaximum

Sets the field to the maximum of its current value and the given value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a maximum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the larger operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The maximum of a zero stored value and zero input value is always the stored value. The maximum of any numeric value x and NaN is NaN.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMinimum

Sets the field to the minimum of its current value and the given value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the input value. If a minimum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the smaller operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The minimum of a zero stored value and zero input value is always the stored value. The minimum of any numeric value x and NaN is NaN.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)` |   
  
### setMinimum

Sets the field to the minimum of its current value and the given value.

This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the input value. If a minimum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the smaller operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The minimum of a zero stored value and zero input value is always the stored value. The minimum of any numeric value x and NaN is NaN.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Firestore\V1beta1\Value](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.Value)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAppendMissingElements

Append the given elements in order if they are not already present in the current field value.

If the field is not an array, or if the field does not yet exist, it is first set to the empty array. Equivalent numbers of different types (e.g. 3L and 3.0) are considered equal when checking if a value is missing. NaN is equal to NaN, and Null is equal to Null. If the input contains multiple equivalent values, only the first will be considered. The corresponding transform_result will be the null value.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Firestore\V1beta1\ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)` |   
  
### setAppendMissingElements

Append the given elements in order if they are not already present in the current field value.

If the field is not an array, or if the field does not yet exist, it is first set to the empty array. Equivalent numbers of different types (e.g. 3L and 3.0) are considered equal when checking if a value is missing. NaN is equal to NaN, and Null is equal to Null. If the input contains multiple equivalent values, only the first will be considered. The corresponding transform_result will be the null value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Firestore\V1beta1\ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRemoveAllFromArray

Remove all of the given elements from the array in the field.

If the field is not an array, or if the field does not yet exist, it is set to the empty array. Equivalent numbers of the different types (e.g. 3L and 3.0) are considered equal when deciding whether an element should be removed. NaN is equal to NaN, and Null is equal to Null. This will remove all equivalent values if there are duplicates. The corresponding transform_result will be the null value.

**Returns**  
---  
**Type** | **Description**  
`[Google\Cloud\Firestore\V1beta1\ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)` |   
  
### setRemoveAllFromArray

Remove all of the given elements from the array in the field.

If the field is not an array, or if the field does not yet exist, it is set to the empty array. Equivalent numbers of the different types (e.g. 3L and 3.0) are considered equal when deciding whether an element should be removed. NaN is equal to NaN, and Null is equal to Null. This will remove all equivalent values if there are duplicates. The corresponding transform_result will be the null value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Cloud\Firestore\V1beta1\ArrayValue](https://docs.cloud.google.com/php/docs/reference/cloud-firestore/latest/V1beta1.ArrayValue)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTransformType

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
