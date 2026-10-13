---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CertificateManagerGrpc.CertificateManagerBlockingV2Stub
title: Class CertificateManagerGrpc.CertificateManagerBlockingV2Stub (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:04.535047+00:00
---

# Class CertificateManagerGrpc.CertificateManagerBlockingV2Stub (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CertificateManagerGrpc.CertificateManagerBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CertificateManagerGrpc.CertificateManagerBlockingV2Stub (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.2  0.4.0  0.3.1  0.2.0  0.1.1 
    
    
    public static final class CertificateManagerGrpc.CertificateManagerBlockingV2Stub extends AbstractBlockingStub<CertificateManagerGrpc.CertificateManagerBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service CertificateManager.

API Overview Certificates Manager API allows customers to see and manage all their TLS certificates. Certificates Manager API service provides methods to manage certificates, group them into collections, and create serving configuration that can be easily applied to other Cloud resources e.g. Target Proxies. Data Model The Certificates Manager service exposes the following resources:

  * `Certificate` that describes a single TLS certificate.
  * `CertificateMap` that describes a collection of certificates that can be attached to a target resource.
  * `CertificateMapEntry` that describes a single configuration entry that consists of a SNI and a group of certificates. It's a subresource of CertificateMap. Certificate, CertificateMap and CertificateMapEntry IDs have to fully match the regexp `[a-z0-9-]{1,63}`. In other words,
  * only lower case letters, digits, and hyphen are allowed
  * length of the resource ID has to be in [1,63] range. Provides methods to manage Cloud Certificate Manager entities.



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > CertificateManagerGrpc.CertificateManagerBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected CertificateManagerGrpc.CertificateManagerBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateManagerGrpc.CertificateManagerBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CertificateManagerGrpc.CertificateManagerBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createCertificate(CreateCertificateRequest request)
    
    
    public Operation createCertificate(CreateCertificateRequest request)

Creates a new Certificate in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CreateCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createCertificateIssuanceConfig(CreateCertificateIssuanceConfigRequest request)
    
    
    public Operation createCertificateIssuanceConfig(CreateCertificateIssuanceConfigRequest request)

Creates a new CertificateIssuanceConfig in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CreateCertificateIssuanceConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createCertificateMap(CreateCertificateMapRequest request)
    
    
    public Operation createCertificateMap(CreateCertificateMapRequest request)

Creates a new CertificateMap in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCertificateMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CreateCertificateMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createCertificateMapEntry(CreateCertificateMapEntryRequest request)
    
    
    public Operation createCertificateMapEntry(CreateCertificateMapEntryRequest request)

Creates a new CertificateMapEntry in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCertificateMapEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CreateCertificateMapEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createDnsAuthorization(CreateDnsAuthorizationRequest request)
    
    
    public Operation createDnsAuthorization(CreateDnsAuthorizationRequest request)

Creates a new DnsAuthorization in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDnsAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CreateDnsAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createTrustConfig(CreateTrustConfigRequest request)
    
    
    public Operation createTrustConfig(CreateTrustConfigRequest request)

Creates a new TrustConfig in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTrustConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CreateTrustConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCertificate(DeleteCertificateRequest request)
    
    
    public Operation deleteCertificate(DeleteCertificateRequest request)

Deletes a single Certificate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DeleteCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCertificateIssuanceConfig(DeleteCertificateIssuanceConfigRequest request)
    
    
    public Operation deleteCertificateIssuanceConfig(DeleteCertificateIssuanceConfigRequest request)

Deletes a single CertificateIssuanceConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCertificateIssuanceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DeleteCertificateIssuanceConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCertificateMap(DeleteCertificateMapRequest request)
    
    
    public Operation deleteCertificateMap(DeleteCertificateMapRequest request)

Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCertificateMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DeleteCertificateMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCertificateMapEntry(DeleteCertificateMapEntryRequest request)
    
    
    public Operation deleteCertificateMapEntry(DeleteCertificateMapEntryRequest request)

Deletes a single CertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCertificateMapEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DeleteCertificateMapEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteDnsAuthorization(DeleteDnsAuthorizationRequest request)
    
    
    public Operation deleteDnsAuthorization(DeleteDnsAuthorizationRequest request)

Deletes a single DnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDnsAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DeleteDnsAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteTrustConfig(DeleteTrustConfigRequest request)
    
    
    public Operation deleteTrustConfig(DeleteTrustConfigRequest request)

Deletes a single TrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTrustConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DeleteTrustConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCertificate(GetCertificateRequest request)
    
    
    public Certificate getCertificate(GetCertificateRequest request)

Gets details of a single Certificate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.GetCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.Certificate)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCertificateIssuanceConfig(GetCertificateIssuanceConfigRequest request)
    
    
    public CertificateIssuanceConfig getCertificateIssuanceConfig(GetCertificateIssuanceConfigRequest request)

Gets details of a single CertificateIssuanceConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCertificateIssuanceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.GetCertificateIssuanceConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateIssuanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CertificateIssuanceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCertificateMap(GetCertificateMapRequest request)
    
    
    public CertificateMap getCertificateMap(GetCertificateMapRequest request)

Gets details of a single CertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCertificateMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.GetCertificateMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CertificateMap)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCertificateMapEntry(GetCertificateMapEntryRequest request)
    
    
    public CertificateMapEntry getCertificateMapEntry(GetCertificateMapEntryRequest request)

Gets details of a single CertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCertificateMapEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.GetCertificateMapEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateMapEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.CertificateMapEntry)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getDnsAuthorization(GetDnsAuthorizationRequest request)
    
    
    public DnsAuthorization getDnsAuthorization(GetDnsAuthorizationRequest request)

Gets details of a single DnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDnsAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.GetDnsAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DnsAuthorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.DnsAuthorization)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTrustConfig(GetTrustConfigRequest request)
    
    
    public TrustConfig getTrustConfig(GetTrustConfigRequest request)

Gets details of a single TrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTrustConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.GetTrustConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TrustConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.TrustConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCertificateIssuanceConfigs(ListCertificateIssuanceConfigsRequest request)
    
    
    public ListCertificateIssuanceConfigsResponse listCertificateIssuanceConfigs(ListCertificateIssuanceConfigsRequest request)

Lists CertificateIssuanceConfigs in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCertificateIssuanceConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCertificateIssuanceConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCertificateMapEntries(ListCertificateMapEntriesRequest request)
    
    
    public ListCertificateMapEntriesResponse listCertificateMapEntries(ListCertificateMapEntriesRequest request)

Lists CertificateMapEntries in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCertificateMapEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificateMapEntriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCertificateMapEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificateMapEntriesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCertificateMaps(ListCertificateMapsRequest request)
    
    
    public ListCertificateMapsResponse listCertificateMaps(ListCertificateMapsRequest request)

Lists CertificateMaps in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCertificateMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificateMapsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCertificateMapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificateMapsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCertificates(ListCertificatesRequest request)
    
    
    public ListCertificatesResponse listCertificates(ListCertificatesRequest request)

Lists Certificates in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificatesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListCertificatesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listDnsAuthorizations(ListDnsAuthorizationsRequest request)
    
    
    public ListDnsAuthorizationsResponse listDnsAuthorizations(ListDnsAuthorizationsRequest request)

Lists DnsAuthorizations in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDnsAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListDnsAuthorizationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDnsAuthorizationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListDnsAuthorizationsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTrustConfigs(ListTrustConfigsRequest request)
    
    
    public ListTrustConfigsResponse listTrustConfigs(ListTrustConfigsRequest request)

Lists TrustConfigs in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTrustConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListTrustConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTrustConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.ListTrustConfigsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCertificate(UpdateCertificateRequest request)
    
    
    public Operation updateCertificate(UpdateCertificateRequest request)

Updates a Certificate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.UpdateCertificateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCertificateMap(UpdateCertificateMapRequest request)
    
    
    public Operation updateCertificateMap(UpdateCertificateMapRequest request)

Updates a CertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCertificateMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.UpdateCertificateMapRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCertificateMapEntry(UpdateCertificateMapEntryRequest request)
    
    
    public Operation updateCertificateMapEntry(UpdateCertificateMapEntryRequest request)

Updates a CertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCertificateMapEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.UpdateCertificateMapEntryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateDnsAuthorization(UpdateDnsAuthorizationRequest request)
    
    
    public Operation updateDnsAuthorization(UpdateDnsAuthorizationRequest request)

Updates a DnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDnsAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.UpdateDnsAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTrustConfig(UpdateTrustConfigRequest request)
    
    
    public Operation updateTrustConfig(UpdateTrustConfigRequest request)

Updates a TrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTrustConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-certificate-manager/latest/com.google.cloud.certificatemanager.v1.UpdateTrustConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
