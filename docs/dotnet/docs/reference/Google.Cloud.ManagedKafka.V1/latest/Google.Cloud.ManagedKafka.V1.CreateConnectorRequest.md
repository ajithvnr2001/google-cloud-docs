---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest
title: Managed Service for Apache Kafka API v1 API - Class CreateConnectorRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:43.335060+00:00
---

# Managed Service for Apache Kafka API v1 API - Class CreateConnectorRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class CreateConnectorRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)


    
    
    public sealed class CreateConnectorRequest : IMessage<CreateConnectorRequest>, IEquatable<CreateConnectorRequest>, IDeepCloneable<CreateConnectorRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class CreateConnectorRequest.

Request for CreateConnector.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateConnectorRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### CreateConnectorRequest()
    
    
    public CreateConnectorRequest()

### CreateConnectorRequest(CreateConnectorRequest)
    
    
    public CreateConnectorRequest(CreateConnectorRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateConnectorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest)`  
  
  
## Properties 

### Connector
    
    
    public Connector Connector { get; set; }

Required. The connector to create.

**Property Value**  
---  
**Type** | **Description**  
`[Connector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Connector)` |   
  
### ConnectorId
    
    
    public string ConnectorId { get; set; }

Required. The ID to use for the connector, which will become the final component of the connector's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035.

This value is structured like: `my-connector-id`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent Connect cluster in which to create the connector. Structured like `projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsConnectClusterName
    
    
    public ConnectClusterName ParentAsConnectClusterName { get; set; }

[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateConnectorRequest#Google_Cloud_ManagedKafka_V1_CreateConnectorRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConnectClusterName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
