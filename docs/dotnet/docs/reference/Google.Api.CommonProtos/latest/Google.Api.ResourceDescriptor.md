---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor
title: Class ResourceDescriptor (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:59.156356+00:00
---

# Class ResourceDescriptor (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class ResourceDescriptor (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.ResourceDescriptor)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.ResourceDescriptor)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.ResourceDescriptor)


    
    
    public sealed class ResourceDescriptor : IMessage<ResourceDescriptor>, IEquatable<ResourceDescriptor>, IDeepCloneable<ResourceDescriptor>, IBufferMessage, IMessage

A simple descriptor of a resource type.

ResourceDescriptor annotates a resource message (either by means of a protobuf annotation or use in the service config), and associates the resource's schema, the resource type, and the pattern of the resource name.

Example:
    
    
    message Topic {
      // Indicates this message defines a resource schema.
      // Declares the resource type in the format of {service}/{kind}.
      // For Kubernetes resources, the format is {api group}/{kind}.
      option (google.api.resource) = {
        type: "pubsub.googleapis.com/Topic"
        pattern: "projects/{project}/topics/{topic}"
      };
    }
    

The ResourceDescriptor Yaml config will look like:
    
    
    resources:
    - type: "pubsub.googleapis.com/Topic"
      pattern: "projects/{project}/topics/{topic}"
    

Sometimes, resources have multiple patterns, typically because they can live under multiple parents.

Example:
    
    
    message LogEntry {
      option (google.api.resource) = {
        type: "logging.googleapis.com/LogEntry"
        pattern: "projects/{project}/logs/{log}"
        pattern: "folders/{folder}/logs/{log}"
        pattern: "organizations/{organization}/logs/{log}"
        pattern: "billingAccounts/{billing_account}/logs/{log}"
      };
    }
    

The ResourceDescriptor Yaml config will look like:
    
    
    resources:
    - type: 'logging.googleapis.com/LogEntry'
      pattern: "projects/{project}/logs/{log}"
      pattern: "folders/{folder}/logs/{log}"
      pattern: "organizations/{organization}/logs/{log}"
      pattern: "billingAccounts/{billing_account}/logs/{log}"
    

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceDescriptor

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### ResourceDescriptor()
    
    
    public ResourceDescriptor()

### ResourceDescriptor(ResourceDescriptor)
    
    
    public ResourceDescriptor(ResourceDescriptor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)`  
  
  
## Fields 

### HistoryFieldNumber
    
    
    public const int HistoryFieldNumber = 4

Field number for the "history" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NameFieldFieldNumber
    
    
    public const int NameFieldFieldNumber = 3

Field number for the "name_field" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PatternFieldNumber
    
    
    public const int PatternFieldNumber = 2

Field number for the "pattern" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PluralFieldNumber
    
    
    public const int PluralFieldNumber = 5

Field number for the "plural" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SingularFieldNumber
    
    
    public const int SingularFieldNumber = 6

Field number for the "singular" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### StyleFieldNumber
    
    
    public const int StyleFieldNumber = 10

Field number for the "style" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TypeFieldNumber
    
    
    public const int TypeFieldNumber = 1

Field number for the "type" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### History
    
    
    public ResourceDescriptor.Types.History History { get; set; }

Optional. The historical or future-looking state of the resource pattern.

Example:
    
    
    // The InspectTemplate message originally only supported resource
    // names with organization, and project was added later.
    message InspectTemplate {
      option (google.api.resource) = {
        type: "dlp.googleapis.com/InspectTemplate"
        pattern:
        "organizations/{organization}/inspectTemplates/{inspect_template}"
        pattern: "projects/{project}/inspectTemplates/{inspect_template}"
        history: ORIGINALLY_SINGLE_PATTERN
      };
    }
    

**Property Value**  
---  
**Type** | **Description**  
`[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types)[History](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types.History)` |   
  
### NameField
    
    
    public string NameField { get; set; }

Optional. The field on the resource that designates the resource name field. If omitted, this is assumed to be "name".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parser
    
    
    public static MessageParser<ResourceDescriptor> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)` |   
  
### Pattern
    
    
    public RepeatedField<string> Pattern { get; }

Optional. The relative resource name pattern associated with this resource type. The DNS prefix of the full resource name shouldn't be specified here.

The path pattern must follow the syntax, which aligns with HTTP binding syntax:
    
    
    Template = Segment { "/" Segment } ;
    Segment = LITERAL | Variable ;
    Variable = "{" LITERAL "}" ;
    

Examples:
    
    
    - "projects/{project}/topics/{topic}"
    - "projects/{project}/knowledgeBases/{knowledge_base}"
    

The components in braces correspond to the IDs for each resource in the hierarchy. It is expected that, if multiple patterns are provided, the same component name (e.g. "project") refers to IDs of the same type of resource.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Plural
    
    
    public string Plural { get; set; }

The plural name used in the resource name and permission names, such as 'projects' for the resource name of 'projects/{project}' and the permission name of 'cloudresourcemanager.googleapis.com/projects.get'. One exception to this is for Nested Collections that have stuttering names, as defined in [AIP-122](https://google.aip.dev/122#nested-collections), where the collection ID in the resource name pattern does not necessarily directly match the `plural` value.

It is the same concept of the `plural` field in k8s CRD spec <https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/>

Note: The plural form is required even for singleton resources. See <https://aip.dev/156>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Singular
    
    
    public string Singular { get; set; }

The same concept of the `singular` field in k8s CRD spec <https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/> Such as "project" for the `resourcemanager.googleapis.com/Project` type.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Style
    
    
    public RepeatedField<ResourceDescriptor.Types.Style> Style { get; }

Style flag(s) for this resource. These indicate that a resource is expected to conform to a given style. See the specific style flags for additional information.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types)[Style](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor.Types.Style)` |   
  
### Type
    
    
    public string Type { get; set; }

The resource type. It must be in the format of {service_name}/{resource_type_kind}. The `resource_type_kind` must be singular and must not include version numbers.

Example: `storage.googleapis.com/Bucket`

The value of the resource_type_kind must follow the regular expression /[A-Za-z][a-zA-Z0-9]+/. It should start with an upper case character and should use PascalCase (UpperCamelCase). The maximum number of characters allowed for the `resource_type_kind` is 100.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public ResourceDescriptor Clone()

**Returns**  
---  
**Type** | **Description**  
`[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)` |   
  
### Equals(ResourceDescriptor)
    
    
    public bool Equals(ResourceDescriptor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Equals(object)
    
    
    public override bool Equals(object other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
**Overrides**

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object\))

### GetHashCode()
    
    
    public override int GetHashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### MergeFrom(ResourceDescriptor)
    
    
    public void MergeFrom(ResourceDescriptor other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.ResourceDescriptor)`  
  
  
### MergeFrom(CodedInputStream)
    
    
    public void MergeFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedInputStream.html)`  
  
  
### ToString()
    
    
    public override string ToString()

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### WriteTo(CodedOutputStream)
    
    
    public void WriteTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.CodedOutputStream.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
