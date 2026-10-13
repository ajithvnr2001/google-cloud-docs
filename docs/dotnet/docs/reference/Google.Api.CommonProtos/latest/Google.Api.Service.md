---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service
title: Class Service (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:01.416278+00:00
---

# Class Service (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Class Service (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Api.Service)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Api.Service)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Api.Service)


    
    
    public sealed class Service : IMessage<Service>, IEquatable<Service>, IDeepCloneable<Service>, IBufferMessage, IMessage

`Service` is the root object of Google API service configuration (service config). It describes the basic information about a logical service, such as the service name and the user-facing title, and delegates other aspects to sub-sections. Each sub-section is either a proto message or a repeated proto message that configures a specific aspect, such as auth. For more information, see each proto message definition.

Example:
    
    
    type: google.api.Service
    name: calendar.googleapis.com
    title: Google Calendar API
    apis:
    - name: google.calendar.v3.Calendar
    
    visibility:
      rules:
      - selector: "google.calendar.v3.*"
        restriction: PREVIEW
    backend:
      rules:
      - selector: "google.calendar.v3.*"
        address: calendar.example.com
    
    authentication:
      providers:
      - id: google_calendar_auth
        jwks_uri: https://www.googleapis.com/oauth2/v1/certs
        issuer: https://securetoken.google.com
      rules:
      - selector: "*"
        requirements:
          provider_id: google_calendar_auth
    

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Service

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals\(system-object-system-object\))

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

## Namespace

[Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api)

## Assembly

Google.Api.CommonProtos.dll

## Constructors 

### Service()
    
    
    public Service()

### Service(Service)
    
    
    public Service(Service other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)`  
  
  
## Fields 

### ApisFieldNumber
    
    
    public const int ApisFieldNumber = 3

Field number for the "apis" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### AuthenticationFieldNumber
    
    
    public const int AuthenticationFieldNumber = 11

Field number for the "authentication" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### BackendFieldNumber
    
    
    public const int BackendFieldNumber = 8

Field number for the "backend" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### BillingFieldNumber
    
    
    public const int BillingFieldNumber = 26

Field number for the "billing" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ConfigVersionFieldNumber
    
    
    public const int ConfigVersionFieldNumber = 20

Field number for the "config_version" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ContextFieldNumber
    
    
    public const int ContextFieldNumber = 12

Field number for the "context" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ControlFieldNumber
    
    
    public const int ControlFieldNumber = 21

Field number for the "control" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DocumentationFieldNumber
    
    
    public const int DocumentationFieldNumber = 6

Field number for the "documentation" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### EndpointsFieldNumber
    
    
    public const int EndpointsFieldNumber = 18

Field number for the "endpoints" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### EnumsFieldNumber
    
    
    public const int EnumsFieldNumber = 5

Field number for the "enums" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### HttpFieldNumber
    
    
    public const int HttpFieldNumber = 9

Field number for the "http" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### IdFieldNumber
    
    
    public const int IdFieldNumber = 33

Field number for the "id" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LoggingFieldNumber
    
    
    public const int LoggingFieldNumber = 27

Field number for the "logging" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LogsFieldNumber
    
    
    public const int LogsFieldNumber = 23

Field number for the "logs" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MetricsFieldNumber
    
    
    public const int MetricsFieldNumber = 24

Field number for the "metrics" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MonitoredResourcesFieldNumber
    
    
    public const int MonitoredResourcesFieldNumber = 25

Field number for the "monitored_resources" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MonitoringFieldNumber
    
    
    public const int MonitoringFieldNumber = 28

Field number for the "monitoring" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NameFieldNumber
    
    
    public const int NameFieldNumber = 1

Field number for the "name" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ProducerProjectIdFieldNumber
    
    
    public const int ProducerProjectIdFieldNumber = 22

Field number for the "producer_project_id" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PublishingFieldNumber
    
    
    public const int PublishingFieldNumber = 45

Field number for the "publishing" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### QuotaFieldNumber
    
    
    public const int QuotaFieldNumber = 10

Field number for the "quota" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SourceInfoFieldNumber
    
    
    public const int SourceInfoFieldNumber = 37

Field number for the "source_info" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SystemParametersFieldNumber
    
    
    public const int SystemParametersFieldNumber = 29

Field number for the "system_parameters" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TitleFieldNumber
    
    
    public const int TitleFieldNumber = 2

Field number for the "title" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Types_FieldNumber
    
    
    public const int Types_FieldNumber = 4

Field number for the "types" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### UsageFieldNumber
    
    
    public const int UsageFieldNumber = 15

Field number for the "usage" field.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Properties 

### Apis
    
    
    public RepeatedField<Api> Apis { get; }

A list of API interfaces exported by this service. Only the `name` field of the [google.protobuf.Api][google.protobuf.Api] needs to be provided by the configuration author, as the remaining fields will be derived from the IDL during the normalization process. It is an error to specify an API interface here which cannot be resolved against the associated IDL files.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Api](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Api.html)` |   
  
### Authentication
    
    
    public Authentication Authentication { get; set; }

Auth configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Authentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Authentication)` |   
  
### Backend
    
    
    public Backend Backend { get; set; }

API backend configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Backend)` |   
  
### Billing
    
    
    public Billing Billing { get; set; }

Billing configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Billing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Billing)` |   
  
### ConfigVersion
    
    
    public uint? ConfigVersion { get; set; }

Obsolete. Do not use.

This field has no semantic meaning. The service config compiler always sets this field to `3`.

**Property Value**  
---  
**Type** | **Description**  
`System.UInt32` |   
  
### Context
    
    
    public Context Context { get; set; }

Context configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Context)` |   
  
### Control
    
    
    public Control Control { get; set; }

Configuration for the service control plane.

**Property Value**  
---  
**Type** | **Description**  
`[Control](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Control)` |   
  
### Descriptor
    
    
    public static MessageDescriptor Descriptor { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageDescriptor](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.MessageDescriptor.html)` |   
  
### Documentation
    
    
    public Documentation Documentation { get; set; }

Additional API documentation.

**Property Value**  
---  
**Type** | **Description**  
`[Documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Documentation)` |   
  
### Endpoints
    
    
    public RepeatedField<Endpoint> Endpoints { get; }

Configuration for network endpoints. If this is empty, then an endpoint with the same name as the service is automatically generated to service all defined APIs.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Endpoint)` |   
  
### Enums
    
    
    public RepeatedField<Enum> Enums { get; }

A list of all enum types included in this API service. Enums referenced directly or indirectly by the `apis` are automatically included. Enums which are not referenced but shall be included should be listed here by name by the configuration author. Example:
    
    
    enums:
    - name: google.someapi.v1.SomeEnum
    

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Enum](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Enum.html)` |   
  
### Http
    
    
    public Http Http { get; set; }

HTTP configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Http](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Http)` |   
  
### Id
    
    
    public string Id { get; set; }

A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed. If empty, the server may choose to generate one instead.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Logging
    
    
    public Logging Logging { get; set; }

Logging configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Logging](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Logging)` |   
  
### Logs
    
    
    public RepeatedField<LogDescriptor> Logs { get; }

Defines the logs used by this service.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[LogDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.LogDescriptor)` |   
  
### Metrics
    
    
    public RepeatedField<MetricDescriptor> Metrics { get; }

Defines the metrics used by this service.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MetricDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MetricDescriptor)` |   
  
### MonitoredResources
    
    
    public RepeatedField<MonitoredResourceDescriptor> MonitoredResources { get; }

Defines the monitored resources used by this service. This is required by the [Service.monitoring][google.api.Service.monitoring] and [Service.logging][google.api.Service.logging] configurations.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MonitoredResourceDescriptor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResourceDescriptor)` |   
  
### Monitoring
    
    
    public Monitoring Monitoring { get; set; }

Monitoring configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Monitoring](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Monitoring)` |   
  
### Name
    
    
    public string Name { get; set; }

The service name, which is a DNS-like logical identifier for the service, such as `calendar.googleapis.com`. The service name typically goes through DNS verification to make sure the owner of the service also owns the DNS name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parser
    
    
    public static MessageParser<Service> Parser { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MessageParser](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.MessageParser-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)` |   
  
### ProducerProjectId
    
    
    public string ProducerProjectId { get; set; }

The Google project that owns this service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Publishing
    
    
    public Publishing Publishing { get; set; }

Settings for [Google Cloud Client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) generated from APIs defined as protocol buffers.

**Property Value**  
---  
**Type** | **Description**  
`[Publishing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Publishing)` |   
  
### Quota
    
    
    public Quota Quota { get; set; }

Quota configuration.

**Property Value**  
---  
**Type** | **Description**  
`[Quota](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Quota)` |   
  
### SourceInfo
    
    
    public SourceInfo SourceInfo { get; set; }

Output only. The source information for this configuration if available.

**Property Value**  
---  
**Type** | **Description**  
`[SourceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SourceInfo)` |   
  
### SystemParameters
    
    
    public SystemParameters SystemParameters { get; set; }

System parameter configuration.

**Property Value**  
---  
**Type** | **Description**  
`[SystemParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.SystemParameters)` |   
  
### Title
    
    
    public string Title { get; set; }

The product title for this service, it is the name displayed in Google Cloud Console.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Types_
    
    
    public RepeatedField<Type> Types_ { get; }

A list of all proto message types included in this API service. Types referenced directly or indirectly by the `apis` are automatically included. Messages which are not referenced but shall be included, such as types used by the `google.protobuf.Any` type, should be listed here by name by the configuration author. Example:
    
    
    types:
    - name: google.protobuf.Int32
    

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Type](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Type.html)` |   
  
### Usage
    
    
    public Usage Usage { get; set; }

Configuration controlling usage of this service.

**Property Value**  
---  
**Type** | **Description**  
`[Usage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Usage)` |   
  
## Methods 

### CalculateSize()
    
    
    public int CalculateSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Clone()
    
    
    public Service Clone()

**Returns**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)` |   
  
### Equals(Service)
    
    
    public bool Equals(Service other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)`  
  
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

### MergeFrom(Service)
    
    
    public void MergeFrom(Service other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Service)`  
  
  
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
