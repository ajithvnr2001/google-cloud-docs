---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate
title: Batch v1alpha API - Class AllocationPolicy.Types.InstancePolicyOrTemplate (1.0.0-alpha35) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:10.502905+00:00
---

# Batch v1alpha API - Class AllocationPolicy.Types.InstancePolicyOrTemplate (1.0.0-alpha35)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Batch v1alpha API - Class AllocationPolicy.Types.InstancePolicyOrTemplate (1.0.0-alpha35) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-alpha35 (latest)  1.0.0-alpha34 
    
    
    public sealed class AllocationPolicy.Types.InstancePolicyOrTemplate : IMessage<AllocationPolicy.Types.InstancePolicyOrTemplate>, IEquatable<AllocationPolicy.Types.InstancePolicyOrTemplate>, IDeepCloneable<AllocationPolicy.Types.InstancePolicyOrTemplate>, IBufferMessage, IMessage

Reference documentation and code samples for the Batch v1alpha API class AllocationPolicy.Types.InstancePolicyOrTemplate.

InstancePolicyOrTemplate lets you define the type of resources to use for this job either with an InstancePolicy or an instance template. If undefined, Batch picks the type of VM to use and doesn't include optional VM resources such as GPUs and extra disks.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AllocationPolicy.Types.InstancePolicyOrTemplate

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types)[InstancePolicyOrTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types)[InstancePolicyOrTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types)[InstancePolicyOrTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Batch.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha)

## Assembly

Google.Cloud.Batch.V1Alpha.dll

## Constructors 

### InstancePolicyOrTemplate()
    
    
    public InstancePolicyOrTemplate()

### InstancePolicyOrTemplate(InstancePolicyOrTemplate)
    
    
    public InstancePolicyOrTemplate(AllocationPolicy.Types.InstancePolicyOrTemplate other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types)[InstancePolicyOrTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate)`  
  
  
## Properties 

### BlockProjectSshKeys
    
    
    public bool BlockProjectSshKeys { get; set; }

Optional. Set this field to `true` if you want Batch to block project-level SSH keys from accessing this job's VMs. Alternatively, you can configure the job to specify a VM instance template that blocks project-level SSH keys. In either case, Batch blocks project-level SSH keys while creating the VMs for this job.

Batch allows project-level SSH keys for a job's VMs only if all the following are true:

  * This field is undefined or set to `false`.
  * The job's VM instance template (if any) doesn't block project-level SSH keys.



Notably, you can override this behavior by manually updating a VM to block or allow project-level SSH keys. For more information about blocking project-level SSH keys, see the Compute Engine documentation: <https://cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys>

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInstanceTemplate
    
    
    public bool HasInstanceTemplate { get; }

Gets whether the "instance_template" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstallGpuDrivers
    
    
    public bool InstallGpuDrivers { get; set; }

Set this field true if you want Batch to help fetch drivers from a third party location and install them for GPUs specified in `policy.accelerators` or `instance_template` on your behalf. Default is false.

For Container-Optimized Image cases, Batch will install the accelerator driver following milestones of <https://cloud.google.com/container-optimized-os/docs/release-notes>. For non Container-Optimized Image cases, following <https://github.com/GoogleCloudPlatform/compute-gpu-installation/blob/main/linux/install_gpu_driver.py>.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstallOpsAgent
    
    
    public bool InstallOpsAgent { get; set; }

Optional. Set this field true if you want Batch to install Ops Agent on your behalf. Default is false.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceTemplate
    
    
    public string InstanceTemplate { get; set; }

Name of an instance template used to create VMs. Named the field as 'instance_template' instead of 'template' to avoid C++ keyword conflict.

Batch only supports global instance templates from the same project as the job. You can specify the global instance template as a full or partial URL.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Policy
    
    
    public AllocationPolicy.Types.InstancePolicy Policy { get; set; }

InstancePolicy.

**Property Value**  
---  
**Type** | **Description**  
`[AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types)[InstancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicy)` |   
  
### PolicyTemplateCase
    
    
    public AllocationPolicy.Types.InstancePolicyOrTemplate.PolicyTemplateOneofCase PolicyTemplateCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AllocationPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types)[InstancePolicyOrTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate)[PolicyTemplateOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Batch.V1Alpha/latest/Google.Cloud.Batch.V1Alpha.AllocationPolicy.Types.InstancePolicyOrTemplate.PolicyTemplateOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
