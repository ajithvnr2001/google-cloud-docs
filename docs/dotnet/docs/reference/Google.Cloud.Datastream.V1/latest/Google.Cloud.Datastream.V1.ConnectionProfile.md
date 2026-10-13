---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile
title: DataStream v1 API - Class ConnectionProfile (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:21.273105+00:00
---

# DataStream v1 API - Class ConnectionProfile (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class ConnectionProfile (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.ConnectionProfile)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.ConnectionProfile)


    
    
    public sealed class ConnectionProfile : IMessage<ConnectionProfile>, IEquatable<ConnectionProfile>, IDeepCloneable<ConnectionProfile>, IBufferMessage, IMessage

Reference documentation and code samples for the DataStream v1 API class ConnectionProfile.

A set of reusable connection configurations to be used as a source or destination for a stream.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConnectionProfile

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Constructors 

### ConnectionProfile()
    
    
    public ConnectionProfile()

### ConnectionProfile(ConnectionProfile)
    
    
    public ConnectionProfile(ConnectionProfile other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)`  
  
  
## Properties 

### BigqueryProfile
    
    
    public BigQueryProfile BigqueryProfile { get; set; }

BigQuery Connection Profile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.BigQueryProfile)` |   
  
### ConnectionProfileName
    
    
    public ConnectionProfileName ConnectionProfileName { get; set; }

[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile#Google_Cloud_Datastream_V1_ConnectionProfile_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfileName)` |   
  
### ConnectivityCase
    
    
    public ConnectionProfile.ConnectivityOneofCase ConnectivityCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[ConnectivityOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile.ConnectivityOneofCase)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The create time of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. Display name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ForwardSshConnectivity
    
    
    public ForwardSshTunnelConnectivity ForwardSshConnectivity { get; set; }

Forward SSH tunnel connectivity.

**Property Value**  
---  
**Type** | **Description**  
`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ForwardSshTunnelConnectivity)` |   
  
### GcsProfile
    
    
    public GcsProfile GcsProfile { get; set; }

Cloud Storage ConnectionProfile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[GcsProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.GcsProfile)` |   
  
### HasSatisfiesPzi
    
    
    public bool HasSatisfiesPzi { get; }

Gets whether the "satisfies_pzi" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSatisfiesPzs
    
    
    public bool HasSatisfiesPzs { get; }

Gets whether the "satisfies_pzs" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MongodbProfile
    
    
    public MongodbProfile MongodbProfile { get; set; }

MongoDB Connection Profile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[MongodbProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.MongodbProfile)` |   
  
### MysqlProfile
    
    
    public MysqlProfile MysqlProfile { get; set; }

MySQL ConnectionProfile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[MysqlProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.MysqlProfile)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. Identifier. The resource's name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OracleProfile
    
    
    public OracleProfile OracleProfile { get; set; }

Oracle ConnectionProfile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[OracleProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.OracleProfile)` |   
  
### PostgresqlProfile
    
    
    public PostgresqlProfile PostgresqlProfile { get; set; }

PostgreSQL Connection Profile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[PostgresqlProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlProfile)` |   
  
### PrivateConnectivity
    
    
    public PrivateConnectivity PrivateConnectivity { get; set; }

Private connectivity.

**Property Value**  
---  
**Type** | **Description**  
`[PrivateConnectivity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PrivateConnectivity)` |   
  
### ProfileCase
    
    
    public ConnectionProfile.ProfileOneofCase ProfileCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile)[ProfileOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.ConnectionProfile.ProfileOneofCase)` |   
  
### SalesforceProfile
    
    
    public SalesforceProfile SalesforceProfile { get; set; }

Salesforce Connection Profile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[SalesforceProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.SalesforceProfile)` |   
  
### SatisfiesPzi
    
    
    public bool SatisfiesPzi { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SqlServerProfile
    
    
    public SqlServerProfile SqlServerProfile { get; set; }

SQLServer Connection Profile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[SqlServerProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.SqlServerProfile)` |   
  
### StaticServiceIpConnectivity
    
    
    public StaticServiceIpConnectivity StaticServiceIpConnectivity { get; set; }

Static Service IP connectivity.

**Property Value**  
---  
**Type** | **Description**  
`[StaticServiceIpConnectivity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.StaticServiceIpConnectivity)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The update time of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
