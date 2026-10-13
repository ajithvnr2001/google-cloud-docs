---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraintOrBuilder
title: Interface AnalyzerOrgPolicyConstraint.CustomConstraintOrBuilder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:25.013961+00:00
---

# Interface AnalyzerOrgPolicyConstraint.CustomConstraintOrBuilder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraintOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnalyzerOrgPolicyConstraint.CustomConstraintOrBuilder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.2-SNAPSHOT  3.6.0  3.4.1  3.3.1  3.2.17 
    
    
    public static interface AnalyzerOrgPolicyConstraint.CustomConstraintOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActionType()
    
    
    public abstract AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType getActionType()

Allow or deny type.

` .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType action_type = 5; `

**Returns**  
---  
**Type** | **Description**  
`[AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType)` | The actionType.  
  
### getActionTypeValue()
    
    
    public abstract int getActionTypeValue()

Allow or deny type.

` .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType action_type = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for actionType.  
  
### getCondition()
    
    
    public abstract String getCondition()

Organization Policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")'` or, `resource.management.auto_upgrade == true`

`string condition = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The condition.  
  
### getConditionBytes()
    
    
    public abstract ByteString getConditionBytes()

Organization Policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")'` or, `resource.management.auto_upgrade == true`

`string condition = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for condition.  
  
### getDescription()
    
    
    public abstract String getDescription()

Detailed information about this custom policy constraint.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Detailed information about this custom policy constraint.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

One line display name for the UI.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

One line display name for the UI.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getMethodTypes(int index)
    
    
    public abstract AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType getMethodTypes(int index)

All the operations being applied for this constraint.

` repeated .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType)` | The methodTypes at the given index.  
  
### getMethodTypesCount()
    
    
    public abstract int getMethodTypesCount()

All the operations being applied for this constraint.

` repeated .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of methodTypes.  
  
### getMethodTypesList()
    
    
    public abstract List<AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType> getMethodTypesList()

All the operations being applied for this constraint.

` repeated .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MethodType](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType)>` | A list containing the methodTypes.  
  
### getMethodTypesValue(int index)
    
    
    public abstract int getMethodTypesValue(int index)

All the operations being applied for this constraint.

` repeated .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType method_types = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of methodTypes at the given index.  
  
### getMethodTypesValueList()
    
    
    public abstract List<Integer> getMethodTypesValueList()

All the operations being applied for this constraint.

` repeated .google.cloud.asset.v1.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType method_types = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for methodTypes.  
  
### getName()
    
    
    public abstract String getName()

Name of the constraint. This is unique within the organization. Format of the name should be

  * `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example : "organizations/123/customConstraints/custom.createOnlyE2TypeVms"




`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the constraint. This is unique within the organization. Format of the name should be

  * `organizations/{organization_id}/customConstraints/{custom_constraint_id}`

Example : "organizations/123/customConstraints/custom.createOnlyE2TypeVms"




`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getResourceTypes(int index)
    
    
    public abstract String getResourceTypes(int index)

The Resource Instance type on which this policy applies to. Format will be of the form : "<canonical service name>/<type>" Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceTypes at the given index.  
  
### getResourceTypesBytes(int index)
    
    
    public abstract ByteString getResourceTypesBytes(int index)

The Resource Instance type on which this policy applies to. Format will be of the form : "<canonical service name>/<type>" Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the resourceTypes at the given index.  
  
### getResourceTypesCount()
    
    
    public abstract int getResourceTypesCount()

The Resource Instance type on which this policy applies to. Format will be of the form : "<canonical service name>/<type>" Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of resourceTypes.  
  
### getResourceTypesList()
    
    
    public abstract List<String> getResourceTypesList()

The Resource Instance type on which this policy applies to. Format will be of the form : "<canonical service name>/<type>" Example:

  * `compute.googleapis.com/Instance`.



`repeated string resource_types = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the resourceTypes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
