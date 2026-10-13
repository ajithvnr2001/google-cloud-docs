---
url: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificatemanager-class
title: Class protos.google.cloud.certificatemanager.v1.CertificateManager (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:11.878764+00:00
---

# Class protos.google.cloud.certificatemanager.v1.CertificateManager (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificatemanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.certificatemanager.v1.CertificateManager (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.3  0.7.2  0.6.2  0.5.0  0.1.0 

Represents a CertificateManager

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.certificatemanager.v1.CertificateManager

## Package

[@google-cloud/certificate-manager](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CertificateManager service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CertificateManager;

Creates new CertificateManager service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[CertificateManager](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificatemanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCertificate(request, callback)
    
    
    public createCertificate(request: google.cloud.certificatemanager.v1.ICreateCertificateRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateCallback): void;

Calls CreateCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificaterequest)`   
CreateCertificateRequest message or plain object  
`callback` |  `[CreateCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCertificate(request)
    
    
    public createCertificate(request: google.cloud.certificatemanager.v1.ICreateCertificateRequest): Promise<google.longrunning.Operation>;

Calls CreateCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificaterequest)`   
CreateCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### createCertificateIssuanceConfig(request, callback)
    
    
    public createCertificateIssuanceConfig(request: google.cloud.certificatemanager.v1.ICreateCertificateIssuanceConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateIssuanceConfigCallback): void;

Calls CreateCertificateIssuanceConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificateissuanceconfigrequest)`   
CreateCertificateIssuanceConfigRequest message or plain object  
`callback` |  `[CreateCertificateIssuanceConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCertificateIssuanceConfig(request)
    
    
    public createCertificateIssuanceConfig(request: google.cloud.certificatemanager.v1.ICreateCertificateIssuanceConfigRequest): Promise<google.longrunning.Operation>;

Calls CreateCertificateIssuanceConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificateissuanceconfigrequest)`   
CreateCertificateIssuanceConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### createCertificateMap(request, callback)
    
    
    public createCertificateMap(request: google.cloud.certificatemanager.v1.ICreateCertificateMapRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMapCallback): void;

Calls CreateCertificateMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificatemaprequest)`   
CreateCertificateMapRequest message or plain object  
`callback` |  `[CreateCertificateMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCertificateMap(request)
    
    
    public createCertificateMap(request: google.cloud.certificatemanager.v1.ICreateCertificateMapRequest): Promise<google.longrunning.Operation>;

Calls CreateCertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificatemaprequest)`   
CreateCertificateMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### createCertificateMapEntry(request, callback)
    
    
    public createCertificateMapEntry(request: google.cloud.certificatemanager.v1.ICreateCertificateMapEntryRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.CreateCertificateMapEntryCallback): void;

Calls CreateCertificateMapEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificatemapentryrequest)`   
CreateCertificateMapEntryRequest message or plain object  
`callback` |  `[CreateCertificateMapEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCertificateMapEntry(request)
    
    
    public createCertificateMapEntry(request: google.cloud.certificatemanager.v1.ICreateCertificateMapEntryRequest): Promise<google.longrunning.Operation>;

Calls CreateCertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatecertificatemapentryrequest)`   
CreateCertificateMapEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### createDnsAuthorization(request, callback)
    
    
    public createDnsAuthorization(request: google.cloud.certificatemanager.v1.ICreateDnsAuthorizationRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.CreateDnsAuthorizationCallback): void;

Calls CreateDnsAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatednsauthorizationrequest)`   
CreateDnsAuthorizationRequest message or plain object  
`callback` |  `[CreateDnsAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDnsAuthorization(request)
    
    
    public createDnsAuthorization(request: google.cloud.certificatemanager.v1.ICreateDnsAuthorizationRequest): Promise<google.longrunning.Operation>;

Calls CreateDnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatednsauthorizationrequest)`   
CreateDnsAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### createTrustConfig(request, callback)
    
    
    public createTrustConfig(request: google.cloud.certificatemanager.v1.ICreateTrustConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.CreateTrustConfigCallback): void;

Calls CreateTrustConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatetrustconfigrequest)`   
CreateTrustConfigRequest message or plain object  
`callback` |  `[CreateTrustConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTrustConfig(request)
    
    
    public createTrustConfig(request: google.cloud.certificatemanager.v1.ICreateTrustConfigRequest): Promise<google.longrunning.Operation>;

Calls CreateTrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.icreatetrustconfigrequest)`   
CreateTrustConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteCertificate(request, callback)
    
    
    public deleteCertificate(request: google.cloud.certificatemanager.v1.IDeleteCertificateRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateCallback): void;

Calls DeleteCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificaterequest)`   
DeleteCertificateRequest message or plain object  
`callback` |  `[DeleteCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCertificate(request)
    
    
    public deleteCertificate(request: google.cloud.certificatemanager.v1.IDeleteCertificateRequest): Promise<google.longrunning.Operation>;

Calls DeleteCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificaterequest)`   
DeleteCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteCertificateIssuanceConfig(request, callback)
    
    
    public deleteCertificateIssuanceConfig(request: google.cloud.certificatemanager.v1.IDeleteCertificateIssuanceConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateIssuanceConfigCallback): void;

Calls DeleteCertificateIssuanceConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateIssuanceConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificateissuanceconfigrequest)`   
DeleteCertificateIssuanceConfigRequest message or plain object  
`callback` |  `[DeleteCertificateIssuanceConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCertificateIssuanceConfig(request)
    
    
    public deleteCertificateIssuanceConfig(request: google.cloud.certificatemanager.v1.IDeleteCertificateIssuanceConfigRequest): Promise<google.longrunning.Operation>;

Calls DeleteCertificateIssuanceConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateIssuanceConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificateissuanceconfigrequest)`   
DeleteCertificateIssuanceConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteCertificateMap(request, callback)
    
    
    public deleteCertificateMap(request: google.cloud.certificatemanager.v1.IDeleteCertificateMapRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMapCallback): void;

Calls DeleteCertificateMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificatemaprequest)`   
DeleteCertificateMapRequest message or plain object  
`callback` |  `[DeleteCertificateMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCertificateMap(request)
    
    
    public deleteCertificateMap(request: google.cloud.certificatemanager.v1.IDeleteCertificateMapRequest): Promise<google.longrunning.Operation>;

Calls DeleteCertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificatemaprequest)`   
DeleteCertificateMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteCertificateMapEntry(request, callback)
    
    
    public deleteCertificateMapEntry(request: google.cloud.certificatemanager.v1.IDeleteCertificateMapEntryRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.DeleteCertificateMapEntryCallback): void;

Calls DeleteCertificateMapEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificatemapentryrequest)`   
DeleteCertificateMapEntryRequest message or plain object  
`callback` |  `[DeleteCertificateMapEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCertificateMapEntry(request)
    
    
    public deleteCertificateMapEntry(request: google.cloud.certificatemanager.v1.IDeleteCertificateMapEntryRequest): Promise<google.longrunning.Operation>;

Calls DeleteCertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletecertificatemapentryrequest)`   
DeleteCertificateMapEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteDnsAuthorization(request, callback)
    
    
    public deleteDnsAuthorization(request: google.cloud.certificatemanager.v1.IDeleteDnsAuthorizationRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.DeleteDnsAuthorizationCallback): void;

Calls DeleteDnsAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletednsauthorizationrequest)`   
DeleteDnsAuthorizationRequest message or plain object  
`callback` |  `[DeleteDnsAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDnsAuthorization(request)
    
    
    public deleteDnsAuthorization(request: google.cloud.certificatemanager.v1.IDeleteDnsAuthorizationRequest): Promise<google.longrunning.Operation>;

Calls DeleteDnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletednsauthorizationrequest)`   
DeleteDnsAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### deleteTrustConfig(request, callback)
    
    
    public deleteTrustConfig(request: google.cloud.certificatemanager.v1.IDeleteTrustConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.DeleteTrustConfigCallback): void;

Calls DeleteTrustConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletetrustconfigrequest)`   
DeleteTrustConfigRequest message or plain object  
`callback` |  `[DeleteTrustConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTrustConfig(request)
    
    
    public deleteTrustConfig(request: google.cloud.certificatemanager.v1.IDeleteTrustConfigRequest): Promise<google.longrunning.Operation>;

Calls DeleteTrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ideletetrustconfigrequest)`   
DeleteTrustConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### getCertificate(request, callback)
    
    
    public getCertificate(request: google.cloud.certificatemanager.v1.IGetCertificateRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.GetCertificateCallback): void;

Calls GetCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificaterequest)`   
GetCertificateRequest message or plain object  
`callback` |  `[GetCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Certificate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCertificate(request)
    
    
    public getCertificate(request: google.cloud.certificatemanager.v1.IGetCertificateRequest): Promise<google.cloud.certificatemanager.v1.Certificate>;

Calls GetCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificaterequest)`   
GetCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.Certificate](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificate-class)>` | Promise  
  
### getCertificateIssuanceConfig(request, callback)
    
    
    public getCertificateIssuanceConfig(request: google.cloud.certificatemanager.v1.IGetCertificateIssuanceConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.GetCertificateIssuanceConfigCallback): void;

Calls GetCertificateIssuanceConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateIssuanceConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificateissuanceconfigrequest)`   
GetCertificateIssuanceConfigRequest message or plain object  
`callback` |  `[GetCertificateIssuanceConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and CertificateIssuanceConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCertificateIssuanceConfig(request)
    
    
    public getCertificateIssuanceConfig(request: google.cloud.certificatemanager.v1.IGetCertificateIssuanceConfigRequest): Promise<google.cloud.certificatemanager.v1.CertificateIssuanceConfig>;

Calls GetCertificateIssuanceConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateIssuanceConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificateissuanceconfigrequest)`   
GetCertificateIssuanceConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.CertificateIssuanceConfig](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificateissuanceconfig-class)>` | Promise  
  
### getCertificateMap(request, callback)
    
    
    public getCertificateMap(request: google.cloud.certificatemanager.v1.IGetCertificateMapRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMapCallback): void;

Calls GetCertificateMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)`   
GetCertificateMapRequest message or plain object  
`callback` |  `[GetCertificateMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and CertificateMap  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCertificateMap(request)
    
    
    public getCertificateMap(request: google.cloud.certificatemanager.v1.IGetCertificateMapRequest): Promise<google.cloud.certificatemanager.v1.CertificateMap>;

Calls GetCertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemaprequest)`   
GetCertificateMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.CertificateMap](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificatemap-class)>` | Promise  
  
### getCertificateMapEntry(request, callback)
    
    
    public getCertificateMapEntry(request: google.cloud.certificatemanager.v1.IGetCertificateMapEntryRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.GetCertificateMapEntryCallback): void;

Calls GetCertificateMapEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemapentryrequest)`   
GetCertificateMapEntryRequest message or plain object  
`callback` |  `[GetCertificateMapEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and CertificateMapEntry  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCertificateMapEntry(request)
    
    
    public getCertificateMapEntry(request: google.cloud.certificatemanager.v1.IGetCertificateMapEntryRequest): Promise<google.cloud.certificatemanager.v1.CertificateMapEntry>;

Calls GetCertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetcertificatemapentryrequest)`   
GetCertificateMapEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.CertificateMapEntry](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.certificatemapentry-class)>` | Promise  
  
### getDnsAuthorization(request, callback)
    
    
    public getDnsAuthorization(request: google.cloud.certificatemanager.v1.IGetDnsAuthorizationRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.GetDnsAuthorizationCallback): void;

Calls GetDnsAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetdnsauthorizationrequest)`   
GetDnsAuthorizationRequest message or plain object  
`callback` |  `[GetDnsAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and DnsAuthorization  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDnsAuthorization(request)
    
    
    public getDnsAuthorization(request: google.cloud.certificatemanager.v1.IGetDnsAuthorizationRequest): Promise<google.cloud.certificatemanager.v1.DnsAuthorization>;

Calls GetDnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igetdnsauthorizationrequest)`   
GetDnsAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.DnsAuthorization](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.dnsauthorization-class)>` | Promise  
  
### getTrustConfig(request, callback)
    
    
    public getTrustConfig(request: google.cloud.certificatemanager.v1.IGetTrustConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.GetTrustConfigCallback): void;

Calls GetTrustConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igettrustconfigrequest)`   
GetTrustConfigRequest message or plain object  
`callback` |  `[GetTrustConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and TrustConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTrustConfig(request)
    
    
    public getTrustConfig(request: google.cloud.certificatemanager.v1.IGetTrustConfigRequest): Promise<google.cloud.certificatemanager.v1.TrustConfig>;

Calls GetTrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.igettrustconfigrequest)`   
GetTrustConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.TrustConfig](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.trustconfig-class)>` | Promise  
  
### listCertificateIssuanceConfigs(request, callback)
    
    
    public listCertificateIssuanceConfigs(request: google.cloud.certificatemanager.v1.IListCertificateIssuanceConfigsRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.ListCertificateIssuanceConfigsCallback): void;

Calls ListCertificateIssuanceConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCertificateIssuanceConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificateissuanceconfigsrequest)`   
ListCertificateIssuanceConfigsRequest message or plain object  
`callback` |  `[ListCertificateIssuanceConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCertificateIssuanceConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCertificateIssuanceConfigs(request)
    
    
    public listCertificateIssuanceConfigs(request: google.cloud.certificatemanager.v1.IListCertificateIssuanceConfigsRequest): Promise<google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsResponse>;

Calls ListCertificateIssuanceConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCertificateIssuanceConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificateissuanceconfigsrequest)`   
ListCertificateIssuanceConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listcertificateissuanceconfigsresponse)>` | Promise  
  
### listCertificateMapEntries(request, callback)
    
    
    public listCertificateMapEntries(request: google.cloud.certificatemanager.v1.IListCertificateMapEntriesRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMapEntriesCallback): void;

Calls ListCertificateMapEntries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCertificateMapEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificatemapentriesrequest)`   
ListCertificateMapEntriesRequest message or plain object  
`callback` |  `[ListCertificateMapEntriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCertificateMapEntriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCertificateMapEntries(request)
    
    
    public listCertificateMapEntries(request: google.cloud.certificatemanager.v1.IListCertificateMapEntriesRequest): Promise<google.cloud.certificatemanager.v1.ListCertificateMapEntriesResponse>;

Calls ListCertificateMapEntries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCertificateMapEntriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificatemapentriesrequest)`   
ListCertificateMapEntriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.ListCertificateMapEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listcertificatemapentriesresponse)>` | Promise  
  
### listCertificateMaps(request, callback)
    
    
    public listCertificateMaps(request: google.cloud.certificatemanager.v1.IListCertificateMapsRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.ListCertificateMapsCallback): void;

Calls ListCertificateMaps.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCertificateMapsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificatemapsrequest)`   
ListCertificateMapsRequest message or plain object  
`callback` |  `[ListCertificateMapsCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCertificateMapsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCertificateMaps(request)
    
    
    public listCertificateMaps(request: google.cloud.certificatemanager.v1.IListCertificateMapsRequest): Promise<google.cloud.certificatemanager.v1.ListCertificateMapsResponse>;

Calls ListCertificateMaps.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCertificateMapsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificatemapsrequest)`   
ListCertificateMapsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.ListCertificateMapsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listcertificatemapsresponse)>` | Promise  
  
### listCertificates(request, callback)
    
    
    public listCertificates(request: google.cloud.certificatemanager.v1.IListCertificatesRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.ListCertificatesCallback): void;

Calls ListCertificates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCertificatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificatesrequest)`   
ListCertificatesRequest message or plain object  
`callback` |  `[ListCertificatesCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCertificatesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCertificates(request)
    
    
    public listCertificates(request: google.cloud.certificatemanager.v1.IListCertificatesRequest): Promise<google.cloud.certificatemanager.v1.ListCertificatesResponse>;

Calls ListCertificates.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCertificatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistcertificatesrequest)`   
ListCertificatesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.ListCertificatesResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listcertificatesresponse)>` | Promise  
  
### listDnsAuthorizations(request, callback)
    
    
    public listDnsAuthorizations(request: google.cloud.certificatemanager.v1.IListDnsAuthorizationsRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.ListDnsAuthorizationsCallback): void;

Calls ListDnsAuthorizations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDnsAuthorizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistdnsauthorizationsrequest)`   
ListDnsAuthorizationsRequest message or plain object  
`callback` |  `[ListDnsAuthorizationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDnsAuthorizationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDnsAuthorizations(request)
    
    
    public listDnsAuthorizations(request: google.cloud.certificatemanager.v1.IListDnsAuthorizationsRequest): Promise<google.cloud.certificatemanager.v1.ListDnsAuthorizationsResponse>;

Calls ListDnsAuthorizations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDnsAuthorizationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilistdnsauthorizationsrequest)`   
ListDnsAuthorizationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.ListDnsAuthorizationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listdnsauthorizationsresponse)>` | Promise  
  
### listTrustConfigs(request, callback)
    
    
    public listTrustConfigs(request: google.cloud.certificatemanager.v1.IListTrustConfigsRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.ListTrustConfigsCallback): void;

Calls ListTrustConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTrustConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsrequest)`   
ListTrustConfigsRequest message or plain object  
`callback` |  `[ListTrustConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTrustConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTrustConfigs(request)
    
    
    public listTrustConfigs(request: google.cloud.certificatemanager.v1.IListTrustConfigsRequest): Promise<google.cloud.certificatemanager.v1.ListTrustConfigsResponse>;

Calls ListTrustConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTrustConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.ilisttrustconfigsrequest)`   
ListTrustConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.certificatemanager.v1.ListTrustConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.listtrustconfigsresponse)>` | Promise  
  
### updateCertificate(request, callback)
    
    
    public updateCertificate(request: google.cloud.certificatemanager.v1.IUpdateCertificateRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateCallback): void;

Calls UpdateCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatecertificaterequest)`   
UpdateCertificateRequest message or plain object  
`callback` |  `[UpdateCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCertificate(request)
    
    
    public updateCertificate(request: google.cloud.certificatemanager.v1.IUpdateCertificateRequest): Promise<google.longrunning.Operation>;

Calls UpdateCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatecertificaterequest)`   
UpdateCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateCertificateMap(request, callback)
    
    
    public updateCertificateMap(request: google.cloud.certificatemanager.v1.IUpdateCertificateMapRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMapCallback): void;

Calls UpdateCertificateMap.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatecertificatemaprequest)`   
UpdateCertificateMapRequest message or plain object  
`callback` |  `[UpdateCertificateMapCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCertificateMap(request)
    
    
    public updateCertificateMap(request: google.cloud.certificatemanager.v1.IUpdateCertificateMapRequest): Promise<google.longrunning.Operation>;

Calls UpdateCertificateMap.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCertificateMapRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatecertificatemaprequest)`   
UpdateCertificateMapRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateCertificateMapEntry(request, callback)
    
    
    public updateCertificateMapEntry(request: google.cloud.certificatemanager.v1.IUpdateCertificateMapEntryRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.UpdateCertificateMapEntryCallback): void;

Calls UpdateCertificateMapEntry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatecertificatemapentryrequest)`   
UpdateCertificateMapEntryRequest message or plain object  
`callback` |  `[UpdateCertificateMapEntryCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCertificateMapEntry(request)
    
    
    public updateCertificateMapEntry(request: google.cloud.certificatemanager.v1.IUpdateCertificateMapEntryRequest): Promise<google.longrunning.Operation>;

Calls UpdateCertificateMapEntry.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCertificateMapEntryRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatecertificatemapentryrequest)`   
UpdateCertificateMapEntryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateDnsAuthorization(request, callback)
    
    
    public updateDnsAuthorization(request: google.cloud.certificatemanager.v1.IUpdateDnsAuthorizationRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.UpdateDnsAuthorizationCallback): void;

Calls UpdateDnsAuthorization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatednsauthorizationrequest)`   
UpdateDnsAuthorizationRequest message or plain object  
`callback` |  `[UpdateDnsAuthorizationCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDnsAuthorization(request)
    
    
    public updateDnsAuthorization(request: google.cloud.certificatemanager.v1.IUpdateDnsAuthorizationRequest): Promise<google.longrunning.Operation>;

Calls UpdateDnsAuthorization.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDnsAuthorizationRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatednsauthorizationrequest)`   
UpdateDnsAuthorizationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
### updateTrustConfig(request, callback)
    
    
    public updateTrustConfig(request: google.cloud.certificatemanager.v1.IUpdateTrustConfigRequest, callback: google.cloud.certificatemanager.v1.CertificateManager.UpdateTrustConfigCallback): void;

Calls UpdateTrustConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatetrustconfigrequest)`   
UpdateTrustConfigRequest message or plain object  
`callback` |  `[UpdateTrustConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTrustConfig(request)
    
    
    public updateTrustConfig(request: google.cloud.certificatemanager.v1.IUpdateTrustConfigRequest): Promise<google.longrunning.Operation>;

Calls UpdateTrustConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTrustConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.cloud.certificatemanager.v1.iupdatetrustconfigrequest)`   
UpdateTrustConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/certificate-manager/latest/certificate-manager/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
