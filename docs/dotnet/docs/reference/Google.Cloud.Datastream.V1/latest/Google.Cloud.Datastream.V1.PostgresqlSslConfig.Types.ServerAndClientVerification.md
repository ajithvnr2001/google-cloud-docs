---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification
title: DataStream v1 API - Class PostgresqlSslConfig.Types.ServerAndClientVerification (2.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:42.017530+00:00
---

# DataStream v1 API - Class PostgresqlSslConfig.Types.ServerAndClientVerification (2.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1 API - Class PostgresqlSslConfig.Types.ServerAndClientVerification (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.12.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.11.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.10.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.9.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.8.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.7.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.6.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.5.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.4.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.3.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.2.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.1.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/2.0.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/1.0.0/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)


    
    
    public sealed class PostgresqlSslConfig.Types.ServerAndClientVerification : IMessage<PostgresqlSslConfig.Types.ServerAndClientVerification>, IEquatable<PostgresqlSslConfig.Types.ServerAndClientVerification>, IDeepCloneable<PostgresqlSslConfig.Types.ServerAndClientVerification>, IBufferMessage, IMessage

Reference documentation and code samples for the DataStream v1 API class PostgresqlSslConfig.Types.ServerAndClientVerification.

Message represents the option where Datastream will enforce the encryption and authenticate the server identity as well as the client identity. ca_certificate, client_certificate and client_key must be set if user selects this option.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PostgresqlSslConfig.Types.ServerAndClientVerification

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PostgresqlSslConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types)[ServerAndClientVerification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PostgresqlSslConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types)[ServerAndClientVerification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PostgresqlSslConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types)[ServerAndClientVerification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1)

## Assembly

Google.Cloud.Datastream.V1.dll

## Constructors 

### ServerAndClientVerification()
    
    
    public ServerAndClientVerification()

### ServerAndClientVerification(ServerAndClientVerification)
    
    
    public ServerAndClientVerification(PostgresqlSslConfig.Types.ServerAndClientVerification other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PostgresqlSslConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types)[ServerAndClientVerification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1/latest/Google.Cloud.Datastream.V1.PostgresqlSslConfig.Types.ServerAndClientVerification)`  
  
  
## Properties 

### CaCertificate
    
    
    public string CaCertificate { get; set; }

Required. Input only. PEM-encoded server root CA certificate.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ClientCertificate
    
    
    public string ClientCertificate { get; set; }

Required. Input only. PEM-encoded certificate used by the source database to authenticate the client identity (i.e., the Datastream's identity). This certificate is signed by either a root certificate trusted by the server or one or more intermediate certificates (which is stored with the leaf certificate) to link the this certificate to the trusted root certificate.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ClientKey
    
    
    public string ClientKey { get; set; }

Optional. Input only. PEM-encoded private key associated with the client certificate. This value will be used during the SSL/TLS handshake, allowing the PostgreSQL server to authenticate the client's identity, i.e. identity of the Datastream.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServerCertificateHostname
    
    
    public string ServerCertificateHostname { get; set; }

Optional. The hostname mentioned in the Subject or SAN extension of the server certificate. If this field is not provided, the hostname in the server certificate is not validated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
