---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicyOrBuilder
title: Interface AllocationPolicyOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:10.302689+00:00
---

# Interface AllocationPolicyOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AllocationPolicyOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public interface AllocationPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Custom labels to apply to the job and all the Compute Engine resources that both are created by this allocation policy and support labels.

Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see [Organize resources using labels](https://cloud.google.com/batch/docs/organize-resources-using-labels).

`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInstances(int index)
    
    
    public abstract AllocationPolicy.InstancePolicyOrTemplate getInstances(int index)

Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now.

`repeated .google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate instances = 8; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate)` |   
  
### getInstancesCount()
    
    
    public abstract int getInstancesCount()

Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now.

`repeated .google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate instances = 8; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInstancesList()
    
    
    public abstract List<AllocationPolicy.InstancePolicyOrTemplate> getInstancesList()

Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now.

`repeated .google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate instances = 8; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[InstancePolicyOrTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate)>` |   
  
### getInstancesOrBuilder(int index)
    
    
    public abstract AllocationPolicy.InstancePolicyOrTemplateOrBuilder getInstancesOrBuilder(int index)

Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now.

`repeated .google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate instances = 8; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.InstancePolicyOrTemplateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplateOrBuilder)` |   
  
### getInstancesOrBuilderList()
    
    
    public abstract List<? extends AllocationPolicy.InstancePolicyOrTemplateOrBuilder> getInstancesOrBuilderList()

Describe instances that can be created by this AllocationPolicy. Only instances[0] is supported now.

`repeated .google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate instances = 8; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplateOrBuilder>` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicyOrBuilder#com_google_cloud_batch_v1_AllocationPolicyOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Custom labels to apply to the job and all the Compute Engine resources that both are created by this allocation policy and support labels.

Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see [Organize resources using labels](https://cloud.google.com/batch/docs/organize-resources-using-labels).

`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Custom labels to apply to the job and all the Compute Engine resources that both are created by this allocation policy and support labels.

Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see [Organize resources using labels](https://cloud.google.com/batch/docs/organize-resources-using-labels).

`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Custom labels to apply to the job and all the Compute Engine resources that both are created by this allocation policy and support labels.

Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see [Organize resources using labels](https://cloud.google.com/batch/docs/organize-resources-using-labels).

`map<string, string> labels = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Custom labels to apply to the job and all the Compute Engine resources that both are created by this allocation policy and support labels.

Use labels to group and describe the resources they are applied to. Batch automatically applies predefined labels and supports multiple `labels` fields for each job, which each let you apply custom labels to various resources. Label names that start with "goog-" or "google-" are reserved for predefined labels. For more information about labels with Batch, see [Organize resources using labels](https://cloud.google.com/batch/docs/organize-resources-using-labels).

`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLocation()
    
    
    public abstract AllocationPolicy.LocationPolicy getLocation()

Location where compute resources should be allocated for the Job.

`.google.cloud.batch.v1.AllocationPolicy.LocationPolicy location = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.LocationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicy)` | The location.  
  
### getLocationOrBuilder()
    
    
    public abstract AllocationPolicy.LocationPolicyOrBuilder getLocationOrBuilder()

Location where compute resources should be allocated for the Job.

`.google.cloud.batch.v1.AllocationPolicy.LocationPolicy location = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.LocationPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.LocationPolicyOrBuilder)` |   
  
### getNetwork()
    
    
    public abstract AllocationPolicy.NetworkPolicy getNetwork()

The network policy.

If you define an instance template in the `InstancePolicyOrTemplate` field, Batch will use the network settings in the instance template instead of this field.

`.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy network = 7;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy)` | The network.  
  
### getNetworkOrBuilder()
    
    
    public abstract AllocationPolicy.NetworkPolicyOrBuilder getNetworkOrBuilder()

The network policy.

If you define an instance template in the `InstancePolicyOrTemplate` field, Batch will use the network settings in the instance template instead of this field.

`.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy network = 7;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.NetworkPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.NetworkPolicyOrBuilder)` |   
  
### getPlacement()
    
    
    public abstract AllocationPolicy.PlacementPolicy getPlacement()

The placement policy.

`.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy placement = 10;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.PlacementPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy)` | The placement.  
  
### getPlacementOrBuilder()
    
    
    public abstract AllocationPolicy.PlacementPolicyOrBuilder getPlacementOrBuilder()

The placement policy.

`.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy placement = 10;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.PlacementPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.PlacementPolicyOrBuilder)` |   
  
### getServiceAccount()
    
    
    public abstract ServiceAccount getServiceAccount()

Defines the service account for Batch-created VMs. If omitted, the [default Compute Engine service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. Must match the service account specified in any used instance template configured in the Batch job.

Includes the following fields:

  * email: The service account's email address. If not set, the default Compute Engine service account is used.
  * scopes: Additional OAuth scopes to grant the service account, beyond the default cloud-platform scope. (list of strings)



`.google.cloud.batch.v1.ServiceAccount service_account = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ServiceAccount)` | The serviceAccount.  
  
### getServiceAccountOrBuilder()
    
    
    public abstract ServiceAccountOrBuilder getServiceAccountOrBuilder()

Defines the service account for Batch-created VMs. If omitted, the [default Compute Engine service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. Must match the service account specified in any used instance template configured in the Batch job.

Includes the following fields:

  * email: The service account's email address. If not set, the default Compute Engine service account is used.
  * scopes: Additional OAuth scopes to grant the service account, beyond the default cloud-platform scope. (list of strings)



`.google.cloud.batch.v1.ServiceAccount service_account = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ServiceAccountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.ServiceAccountOrBuilder)` |   
  
### getTags(int index)
    
    
    public abstract String getTags(int index)

Optional. Tags applied to the VM instances.

The tags identify valid sources or targets for network firewalls. Each tag must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).

`repeated string tags = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tags at the given index.  
  
### getTagsBytes(int index)
    
    
    public abstract ByteString getTagsBytes(int index)

Optional. Tags applied to the VM instances.

The tags identify valid sources or targets for network firewalls. Each tag must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).

`repeated string tags = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tags at the given index.  
  
### getTagsCount()
    
    
    public abstract int getTagsCount()

Optional. Tags applied to the VM instances.

The tags identify valid sources or targets for network firewalls. Each tag must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).

`repeated string tags = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tags.  
  
### getTagsList()
    
    
    public abstract List<String> getTagsList()

Optional. Tags applied to the VM instances.

The tags identify valid sources or targets for network firewalls. Each tag must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).

`repeated string tags = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the tags.  
  
### hasLocation()
    
    
    public abstract boolean hasLocation()

Location where compute resources should be allocated for the Job.

`.google.cloud.batch.v1.AllocationPolicy.LocationPolicy location = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the location field is set.  
  
### hasNetwork()
    
    
    public abstract boolean hasNetwork()

The network policy.

If you define an instance template in the `InstancePolicyOrTemplate` field, Batch will use the network settings in the instance template instead of this field.

`.google.cloud.batch.v1.AllocationPolicy.NetworkPolicy network = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the network field is set.  
  
### hasPlacement()
    
    
    public abstract boolean hasPlacement()

The placement policy.

`.google.cloud.batch.v1.AllocationPolicy.PlacementPolicy placement = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the placement field is set.  
  
### hasServiceAccount()
    
    
    public abstract boolean hasServiceAccount()

Defines the service account for Batch-created VMs. If omitted, the [default Compute Engine service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. Must match the service account specified in any used instance template configured in the Batch job.

Includes the following fields:

  * email: The service account's email address. If not set, the default Compute Engine service account is used.
  * scopes: Additional OAuth scopes to grant the service account, beyond the default cloud-platform scope. (list of strings)



`.google.cloud.batch.v1.ServiceAccount service_account = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serviceAccount field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
