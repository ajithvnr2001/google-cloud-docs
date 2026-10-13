---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector
title: Managed Service for Apache Kafka API v1 API - Class Connector (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:39.646462+00:00
---

# Managed Service for Apache Kafka API v1 API - Class Connector (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class Connector (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.Connector)


    
    
    public sealed class Connector : IMessage<Connector>, IEquatable<Connector>, IDeepCloneable<Connector>, IBufferMessage, IMessage

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class Connector.

A Kafka Connect connector in a given ConnectCluster.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Connector

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### Connector()
    
    
    public Connector()

### Connector(Connector)
    
    
    public Connector(Connector other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)`  
  
  
## Properties 

### Configs
    
    
    public MapField<string, string> Configs { get; }

Optional. Connector config as keys/values. The keys of the map are connector property names, for example: `connector.class`, `tasks.max`, `key.converter`.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConnectorName
    
    
    public ConnectorName ConnectorName { get; set; }

[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector#Google_Cloud_ManagedKafka_V1_Connector_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectorName)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The name of the connector. Structured like: projects/{project}/locations/{location}/connectClusters/{connect_cluster}/connectors/{connector}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RestartPolicyCase
    
    
    public Connector.RestartPolicyOneofCase RestartPolicyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)[RestartPolicyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector.RestartPolicyOneofCase)` |   
  
### State
    
    
    public Connector.Types.State State { get; set; }

Output only. The current state of the connector.

**Property Value**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector.Types.State)` |   
  
### TaskRestartPolicy
    
    
    public TaskRetryPolicy TaskRestartPolicy { get; set; }

Optional. Restarts the individual tasks of a Connector.

**Property Value**  
---  
**Type** | **Description**  
`[TaskRetryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TaskRetryPolicy)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
