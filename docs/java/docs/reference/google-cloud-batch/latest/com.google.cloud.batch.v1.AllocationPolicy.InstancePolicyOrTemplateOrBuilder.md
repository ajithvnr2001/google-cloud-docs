---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplateOrBuilder
title: Interface AllocationPolicy.InstancePolicyOrTemplateOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:09.234688+00:00
---

# Interface AllocationPolicy.InstancePolicyOrTemplateOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AllocationPolicy.InstancePolicyOrTemplateOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public static interface AllocationPolicy.InstancePolicyOrTemplateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBlockProjectSshKeys()
    
    
    public abstract boolean getBlockProjectSshKeys()

Optional. Set this field to `true` if you want Batch to block project-level SSH keys from accessing this job's VMs. Alternatively, you can configure the job to specify a VM instance template that blocks project-level SSH keys. In either case, Batch blocks project-level SSH keys while creating the VMs for this job.

Batch allows project-level SSH keys for a job's VMs only if all the following are true:

  * This field is undefined or set to `false`.
  * The job's VM instance template (if any) doesn't block project-level SSH keys.

Notably, you can override this behavior by manually updating a VM to block or allow project-level SSH keys. For more information about blocking project-level SSH keys, see the Compute Engine documentation: <https://cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys>




`bool block_project_ssh_keys = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The blockProjectSshKeys.  
  
### getInstallGpuDrivers()
    
    
    public abstract boolean getInstallGpuDrivers()

Set this field true if you want Batch to help fetch drivers from a third party location and install them for GPUs specified in `policy.accelerators` or `instance_template` on your behalf. Default is false.

For Container-Optimized Image cases, Batch will install the accelerator driver following milestones of <https://cloud.google.com/container-optimized-os/docs/release-notes>. For non Container-Optimized Image cases, following <https://github.com/GoogleCloudPlatform/compute-gpu-installation/blob/main/linux/install_gpu_driver.py>.

`bool install_gpu_drivers = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The installGpuDrivers.  
  
### getInstallOpsAgent()
    
    
    public abstract boolean getInstallOpsAgent()

Optional. Set this field true if you want Batch to install Ops Agent on your behalf. Default is false.

`bool install_ops_agent = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The installOpsAgent.  
  
### getInstanceTemplate()
    
    
    public abstract String getInstanceTemplate()

Name of an instance template used to create VMs. Named the field as 'instance_template' instead of 'template' to avoid C++ keyword conflict.

Batch only supports global instance templates from the same project as the job. You can specify the global instance template as a full or partial URL.

`string instance_template = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceTemplate.  
  
### getInstanceTemplateBytes()
    
    
    public abstract ByteString getInstanceTemplateBytes()

Name of an instance template used to create VMs. Named the field as 'instance_template' instead of 'template' to avoid C++ keyword conflict.

Batch only supports global instance templates from the same project as the job. You can specify the global instance template as a full or partial URL.

`string instance_template = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instanceTemplate.  
  
### getPolicy()
    
    
    public abstract AllocationPolicy.InstancePolicy getPolicy()

InstancePolicy.

`.google.cloud.batch.v1.AllocationPolicy.InstancePolicy policy = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.InstancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicy)` | The policy.  
  
### getPolicyOrBuilder()
    
    
    public abstract AllocationPolicy.InstancePolicyOrBuilder getPolicyOrBuilder()

InstancePolicy.

`.google.cloud.batch.v1.AllocationPolicy.InstancePolicy policy = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.InstancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrBuilder)` |   
  
### getPolicyTemplateCase()
    
    
    public abstract AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase getPolicyTemplateCase()

**Returns**  
---  
**Type** | **Description**  
`[AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.AllocationPolicy.InstancePolicyOrTemplate.PolicyTemplateCase)` |   
  
### hasInstanceTemplate()
    
    
    public abstract boolean hasInstanceTemplate()

Name of an instance template used to create VMs. Named the field as 'instance_template' instead of 'template' to avoid C++ keyword conflict.

Batch only supports global instance templates from the same project as the job. You can specify the global instance template as a full or partial URL.

`string instance_template = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the instanceTemplate field is set.  
  
### hasPolicy()
    
    
    public abstract boolean hasPolicy()

InstancePolicy.

`.google.cloud.batch.v1.AllocationPolicy.InstancePolicy policy = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policy field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
