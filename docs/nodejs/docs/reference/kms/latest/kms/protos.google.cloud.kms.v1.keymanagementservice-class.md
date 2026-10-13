---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.keymanagementservice-class
title: Class protos.google.cloud.kms.v1.KeyManagementService (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:08:54.544405+00:00
---

# Class protos.google.cloud.kms.v1.KeyManagementService (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.keymanagementservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.kms.v1.KeyManagementService (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Represents a KeyManagementService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.kms.v1.KeyManagementService

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new KeyManagementService service.

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

### asymmetricDecrypt(request, callback)
    
    
    public asymmetricDecrypt(request: google.cloud.kms.v1.IAsymmetricDecryptRequest, callback: google.cloud.kms.v1.KeyManagementService.AsymmetricDecryptCallback): void;

Calls AsymmetricDecrypt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAsymmetricDecryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iasymmetricdecryptrequest)`   
AsymmetricDecryptRequest message or plain object  
`callback` |  `[AsymmetricDecryptCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and AsymmetricDecryptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### asymmetricDecrypt(request)
    
    
    public asymmetricDecrypt(request: google.cloud.kms.v1.IAsymmetricDecryptRequest): Promise<google.cloud.kms.v1.AsymmetricDecryptResponse>;

Calls AsymmetricDecrypt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAsymmetricDecryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iasymmetricdecryptrequest)`   
AsymmetricDecryptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.AsymmetricDecryptResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.asymmetricdecryptresponse)>` | Promise  
  
### asymmetricSign(request, callback)
    
    
    public asymmetricSign(request: google.cloud.kms.v1.IAsymmetricSignRequest, callback: google.cloud.kms.v1.KeyManagementService.AsymmetricSignCallback): void;

Calls AsymmetricSign.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAsymmetricSignRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iasymmetricsignrequest)`   
AsymmetricSignRequest message or plain object  
`callback` |  `[AsymmetricSignCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and AsymmetricSignResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### asymmetricSign(request)
    
    
    public asymmetricSign(request: google.cloud.kms.v1.IAsymmetricSignRequest): Promise<google.cloud.kms.v1.AsymmetricSignResponse>;

Calls AsymmetricSign.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAsymmetricSignRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iasymmetricsignrequest)`   
AsymmetricSignRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.AsymmetricSignResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.asymmetricsignresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): KeyManagementService;

Creates new KeyManagementService service using the specified rpc implementation.

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
`[KeyManagementService](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.keymanagementservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCryptoKey(request, callback)
    
    
    public createCryptoKey(request: google.cloud.kms.v1.ICreateCryptoKeyRequest, callback: google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyCallback): void;

Calls CreateCryptoKey.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatecryptokeyrequest)`   
CreateCryptoKeyRequest message or plain object  
`callback` |  `[CreateCryptoKeyCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKey  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCryptoKey(request)
    
    
    public createCryptoKey(request: google.cloud.kms.v1.ICreateCryptoKeyRequest): Promise<google.cloud.kms.v1.CryptoKey>;

Calls CreateCryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatecryptokeyrequest)`   
CreateCryptoKeyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKey](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokey-class)>` | Promise  
  
### createCryptoKeyVersion(request, callback)
    
    
    public createCryptoKeyVersion(request: google.cloud.kms.v1.ICreateCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersionCallback): void;

Calls CreateCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatecryptokeyversionrequest)`   
CreateCryptoKeyVersionRequest message or plain object  
`callback` |  `[CreateCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCryptoKeyVersion(request)
    
    
    public createCryptoKeyVersion(request: google.cloud.kms.v1.ICreateCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls CreateCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatecryptokeyversionrequest)`   
CreateCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
### createImportJob(request, callback)
    
    
    public createImportJob(request: google.cloud.kms.v1.ICreateImportJobRequest, callback: google.cloud.kms.v1.KeyManagementService.CreateImportJobCallback): void;

Calls CreateImportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreateimportjobrequest)`   
CreateImportJobRequest message or plain object  
`callback` |  `[CreateImportJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ImportJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createImportJob(request)
    
    
    public createImportJob(request: google.cloud.kms.v1.ICreateImportJobRequest): Promise<google.cloud.kms.v1.ImportJob>;

Calls CreateImportJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreateimportjobrequest)`   
CreateImportJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)>` | Promise  
  
### createKeyRing(request, callback)
    
    
    public createKeyRing(request: google.cloud.kms.v1.ICreateKeyRingRequest, callback: google.cloud.kms.v1.KeyManagementService.CreateKeyRingCallback): void;

Calls CreateKeyRing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyRingRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatekeyringrequest)`   
CreateKeyRingRequest message or plain object  
`callback` |  `[CreateKeyRingCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyRing  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKeyRing(request)
    
    
    public createKeyRing(request: google.cloud.kms.v1.ICreateKeyRingRequest): Promise<google.cloud.kms.v1.KeyRing>;

Calls CreateKeyRing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyRingRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.icreatekeyringrequest)`   
CreateKeyRingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.KeyRing](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.keyring)>` | Promise  
  
### decapsulate(request, callback)
    
    
    public decapsulate(request: google.cloud.kms.v1.IDecapsulateRequest, callback: google.cloud.kms.v1.KeyManagementService.DecapsulateCallback): void;

Calls Decapsulate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDecapsulateRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.idecapsulaterequest)`   
DecapsulateRequest message or plain object  
`callback` |  `[DecapsulateCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and DecapsulateResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### decapsulate(request)
    
    
    public decapsulate(request: google.cloud.kms.v1.IDecapsulateRequest): Promise<google.cloud.kms.v1.DecapsulateResponse>;

Calls Decapsulate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDecapsulateRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.idecapsulaterequest)`   
DecapsulateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.DecapsulateResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.decapsulateresponse)>` | Promise  
  
### decrypt(request, callback)
    
    
    public decrypt(request: google.cloud.kms.v1.IDecryptRequest, callback: google.cloud.kms.v1.KeyManagementService.DecryptCallback): void;

Calls Decrypt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDecryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.idecryptrequest)`   
DecryptRequest message or plain object  
`callback` |  `[DecryptCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and DecryptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### decrypt(request)
    
    
    public decrypt(request: google.cloud.kms.v1.IDecryptRequest): Promise<google.cloud.kms.v1.DecryptResponse>;

Calls Decrypt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDecryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.idecryptrequest)`   
DecryptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.DecryptResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.decryptresponse)>` | Promise  
  
### deleteCryptoKey(request, callback)
    
    
    public deleteCryptoKey(request: google.cloud.kms.v1.IDeleteCryptoKeyRequest, callback: google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyCallback): void;

Calls DeleteCryptoKey.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ideletecryptokeyrequest)`   
DeleteCryptoKeyRequest message or plain object  
`callback` |  `[DeleteCryptoKeyCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCryptoKey(request)
    
    
    public deleteCryptoKey(request: google.cloud.kms.v1.IDeleteCryptoKeyRequest): Promise<google.longrunning.Operation>;

Calls DeleteCryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ideletecryptokeyrequest)`   
DeleteCryptoKeyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.longrunning.operation)>` | Promise  
  
### deleteCryptoKeyVersion(request, callback)
    
    
    public deleteCryptoKeyVersion(request: google.cloud.kms.v1.IDeleteCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyVersionCallback): void;

Calls DeleteCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ideletecryptokeyversionrequest)`   
DeleteCryptoKeyVersionRequest message or plain object  
`callback` |  `[DeleteCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCryptoKeyVersion(request)
    
    
    public deleteCryptoKeyVersion(request: google.cloud.kms.v1.IDeleteCryptoKeyVersionRequest): Promise<google.longrunning.Operation>;

Calls DeleteCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ideletecryptokeyversionrequest)`   
DeleteCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.longrunning.operation)>` | Promise  
  
### destroyCryptoKeyVersion(request, callback)
    
    
    public destroyCryptoKeyVersion(request: google.cloud.kms.v1.IDestroyCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersionCallback): void;

Calls DestroyCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDestroyCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.idestroycryptokeyversionrequest)`   
DestroyCryptoKeyVersionRequest message or plain object  
`callback` |  `[DestroyCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### destroyCryptoKeyVersion(request)
    
    
    public destroyCryptoKeyVersion(request: google.cloud.kms.v1.IDestroyCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls DestroyCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDestroyCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.idestroycryptokeyversionrequest)`   
DestroyCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
### encrypt(request, callback)
    
    
    public encrypt(request: google.cloud.kms.v1.IEncryptRequest, callback: google.cloud.kms.v1.KeyManagementService.EncryptCallback): void;

Calls Encrypt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEncryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iencryptrequest)`   
EncryptRequest message or plain object  
`callback` |  `[EncryptCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and EncryptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### encrypt(request)
    
    
    public encrypt(request: google.cloud.kms.v1.IEncryptRequest): Promise<google.cloud.kms.v1.EncryptResponse>;

Calls Encrypt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEncryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iencryptrequest)`   
EncryptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.EncryptResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.encryptresponse)>` | Promise  
  
### exportTrustedKeyWrappedCryptoKeyVersion(request, callback)
    
    
    public exportTrustedKeyWrappedCryptoKeyVersion(request: google.cloud.kms.v1.IExportTrustedKeyWrappedCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersionCallback): void;

Calls ExportTrustedKeyWrappedCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iexporttrustedkeywrappedcryptokeyversionrequest)`   
ExportTrustedKeyWrappedCryptoKeyVersionRequest message or plain object  
`callback` |  `[ExportTrustedKeyWrappedCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ExportTrustedKeyWrappedCryptoKeyVersionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportTrustedKeyWrappedCryptoKeyVersion(request)
    
    
    public exportTrustedKeyWrappedCryptoKeyVersion(request: google.cloud.kms.v1.IExportTrustedKeyWrappedCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse>;

Calls ExportTrustedKeyWrappedCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IExportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iexporttrustedkeywrappedcryptokeyversionrequest)`   
ExportTrustedKeyWrappedCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.exporttrustedkeywrappedcryptokeyversionresponse)>` | Promise  
  
### generateRandomBytes(request, callback)
    
    
    public generateRandomBytes(request: google.cloud.kms.v1.IGenerateRandomBytesRequest, callback: google.cloud.kms.v1.KeyManagementService.GenerateRandomBytesCallback): void;

Calls GenerateRandomBytes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateRandomBytesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igeneraterandombytesrequest)`   
GenerateRandomBytesRequest message or plain object  
`callback` |  `[GenerateRandomBytesCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateRandomBytesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateRandomBytes(request)
    
    
    public generateRandomBytes(request: google.cloud.kms.v1.IGenerateRandomBytesRequest): Promise<google.cloud.kms.v1.GenerateRandomBytesResponse>;

Calls GenerateRandomBytes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateRandomBytesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igeneraterandombytesrequest)`   
GenerateRandomBytesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.GenerateRandomBytesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.generaterandombytesresponse)>` | Promise  
  
### getCryptoKey(request, callback)
    
    
    public getCryptoKey(request: google.cloud.kms.v1.IGetCryptoKeyRequest, callback: google.cloud.kms.v1.KeyManagementService.GetCryptoKeyCallback): void;

Calls GetCryptoKey.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetcryptokeyrequest)`   
GetCryptoKeyRequest message or plain object  
`callback` |  `[GetCryptoKeyCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKey  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCryptoKey(request)
    
    
    public getCryptoKey(request: google.cloud.kms.v1.IGetCryptoKeyRequest): Promise<google.cloud.kms.v1.CryptoKey>;

Calls GetCryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetcryptokeyrequest)`   
GetCryptoKeyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKey](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokey-class)>` | Promise  
  
### getCryptoKeyVersion(request, callback)
    
    
    public getCryptoKeyVersion(request: google.cloud.kms.v1.IGetCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.GetCryptoKeyVersionCallback): void;

Calls GetCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetcryptokeyversionrequest)`   
GetCryptoKeyVersionRequest message or plain object  
`callback` |  `[GetCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCryptoKeyVersion(request)
    
    
    public getCryptoKeyVersion(request: google.cloud.kms.v1.IGetCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls GetCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetcryptokeyversionrequest)`   
GetCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
### getImportJob(request, callback)
    
    
    public getImportJob(request: google.cloud.kms.v1.IGetImportJobRequest, callback: google.cloud.kms.v1.KeyManagementService.GetImportJobCallback): void;

Calls GetImportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetimportjobrequest)`   
GetImportJobRequest message or plain object  
`callback` |  `[GetImportJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ImportJob  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getImportJob(request)
    
    
    public getImportJob(request: google.cloud.kms.v1.IGetImportJobRequest): Promise<google.cloud.kms.v1.ImportJob>;

Calls GetImportJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetImportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetimportjobrequest)`   
GetImportJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ImportJob](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.importjob-class)>` | Promise  
  
### getKeyRing(request, callback)
    
    
    public getKeyRing(request: google.cloud.kms.v1.IGetKeyRingRequest, callback: google.cloud.kms.v1.KeyManagementService.GetKeyRingCallback): void;

Calls GetKeyRing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyRingRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetkeyringrequest)`   
GetKeyRingRequest message or plain object  
`callback` |  `[GetKeyRingCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyRing  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKeyRing(request)
    
    
    public getKeyRing(request: google.cloud.kms.v1.IGetKeyRingRequest): Promise<google.cloud.kms.v1.KeyRing>;

Calls GetKeyRing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyRingRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetkeyringrequest)`   
GetKeyRingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.KeyRing](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.keyring)>` | Promise  
  
### getPublicKey(request, callback)
    
    
    public getPublicKey(request: google.cloud.kms.v1.IGetPublicKeyRequest, callback: google.cloud.kms.v1.KeyManagementService.GetPublicKeyCallback): void;

Calls GetPublicKey.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPublicKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetpublickeyrequest)`   
GetPublicKeyRequest message or plain object  
`callback` |  `[GetPublicKeyCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and PublicKey  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPublicKey(request)
    
    
    public getPublicKey(request: google.cloud.kms.v1.IGetPublicKeyRequest): Promise<google.cloud.kms.v1.PublicKey>;

Calls GetPublicKey.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPublicKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetpublickeyrequest)`   
GetPublicKeyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.PublicKey](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.publickey-class)>` | Promise  
  
### getRetiredResource(request, callback)
    
    
    public getRetiredResource(request: google.cloud.kms.v1.IGetRetiredResourceRequest, callback: google.cloud.kms.v1.KeyManagementService.GetRetiredResourceCallback): void;

Calls GetRetiredResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRetiredResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetretiredresourcerequest)`   
GetRetiredResourceRequest message or plain object  
`callback` |  `[GetRetiredResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and RetiredResource  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRetiredResource(request)
    
    
    public getRetiredResource(request: google.cloud.kms.v1.IGetRetiredResourceRequest): Promise<google.cloud.kms.v1.RetiredResource>;

Calls GetRetiredResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRetiredResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.igetretiredresourcerequest)`   
GetRetiredResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.RetiredResource](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.retiredresource)>` | Promise  
  
### importCryptoKeyVersion(request, callback)
    
    
    public importCryptoKeyVersion(request: google.cloud.kms.v1.IImportCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersionCallback): void;

Calls ImportCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)`   
ImportCryptoKeyVersionRequest message or plain object  
`callback` |  `[ImportCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importCryptoKeyVersion(request)
    
    
    public importCryptoKeyVersion(request: google.cloud.kms.v1.IImportCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls ImportCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportcryptokeyversionrequest)`   
ImportCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
### importTrustedKeyWrappedCryptoKeyVersion(request, callback)
    
    
    public importTrustedKeyWrappedCryptoKeyVersion(request: google.cloud.kms.v1.IImportTrustedKeyWrappedCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersionCallback): void;

Calls ImportTrustedKeyWrappedCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimporttrustedkeywrappedcryptokeyversionrequest)`   
ImportTrustedKeyWrappedCryptoKeyVersionRequest message or plain object  
`callback` |  `[ImportTrustedKeyWrappedCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importTrustedKeyWrappedCryptoKeyVersion(request)
    
    
    public importTrustedKeyWrappedCryptoKeyVersion(request: google.cloud.kms.v1.IImportTrustedKeyWrappedCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls ImportTrustedKeyWrappedCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimporttrustedkeywrappedcryptokeyversionrequest)`   
ImportTrustedKeyWrappedCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
### listCryptoKeys(request, callback)
    
    
    public listCryptoKeys(request: google.cloud.kms.v1.IListCryptoKeysRequest, callback: google.cloud.kms.v1.KeyManagementService.ListCryptoKeysCallback): void;

Calls ListCryptoKeys.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCryptoKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistcryptokeysrequest)`   
ListCryptoKeysRequest message or plain object  
`callback` |  `[ListCryptoKeysCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCryptoKeysResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCryptoKeys(request)
    
    
    public listCryptoKeys(request: google.cloud.kms.v1.IListCryptoKeysRequest): Promise<google.cloud.kms.v1.ListCryptoKeysResponse>;

Calls ListCryptoKeys.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCryptoKeysRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistcryptokeysrequest)`   
ListCryptoKeysRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListCryptoKeysResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listcryptokeysresponse)>` | Promise  
  
### listCryptoKeyVersions(request, callback)
    
    
    public listCryptoKeyVersions(request: google.cloud.kms.v1.IListCryptoKeyVersionsRequest, callback: google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersionsCallback): void;

Calls ListCryptoKeyVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCryptoKeyVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistcryptokeyversionsrequest)`   
ListCryptoKeyVersionsRequest message or plain object  
`callback` |  `[ListCryptoKeyVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCryptoKeyVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCryptoKeyVersions(request)
    
    
    public listCryptoKeyVersions(request: google.cloud.kms.v1.IListCryptoKeyVersionsRequest): Promise<google.cloud.kms.v1.ListCryptoKeyVersionsResponse>;

Calls ListCryptoKeyVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCryptoKeyVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistcryptokeyversionsrequest)`   
ListCryptoKeyVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListCryptoKeyVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listcryptokeyversionsresponse)>` | Promise  
  
### listImportJobs(request, callback)
    
    
    public listImportJobs(request: google.cloud.kms.v1.IListImportJobsRequest, callback: google.cloud.kms.v1.KeyManagementService.ListImportJobsCallback): void;

Calls ListImportJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListImportJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistimportjobsrequest)`   
ListImportJobsRequest message or plain object  
`callback` |  `[ListImportJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListImportJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listImportJobs(request)
    
    
    public listImportJobs(request: google.cloud.kms.v1.IListImportJobsRequest): Promise<google.cloud.kms.v1.ListImportJobsResponse>;

Calls ListImportJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListImportJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistimportjobsrequest)`   
ListImportJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListImportJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listimportjobsresponse)>` | Promise  
  
### listKeyRings(request, callback)
    
    
    public listKeyRings(request: google.cloud.kms.v1.IListKeyRingsRequest, callback: google.cloud.kms.v1.KeyManagementService.ListKeyRingsCallback): void;

Calls ListKeyRings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyRingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistkeyringsrequest)`   
ListKeyRingsRequest message or plain object  
`callback` |  `[ListKeyRingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListKeyRingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKeyRings(request)
    
    
    public listKeyRings(request: google.cloud.kms.v1.IListKeyRingsRequest): Promise<google.cloud.kms.v1.ListKeyRingsResponse>;

Calls ListKeyRings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListKeyRingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistkeyringsrequest)`   
ListKeyRingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListKeyRingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listkeyringsresponse)>` | Promise  
  
### listRetiredResources(request, callback)
    
    
    public listRetiredResources(request: google.cloud.kms.v1.IListRetiredResourcesRequest, callback: google.cloud.kms.v1.KeyManagementService.ListRetiredResourcesCallback): void;

Calls ListRetiredResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRetiredResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistretiredresourcesrequest)`   
ListRetiredResourcesRequest message or plain object  
`callback` |  `[ListRetiredResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRetiredResourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRetiredResources(request)
    
    
    public listRetiredResources(request: google.cloud.kms.v1.IListRetiredResourcesRequest): Promise<google.cloud.kms.v1.ListRetiredResourcesResponse>;

Calls ListRetiredResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRetiredResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.ilistretiredresourcesrequest)`   
ListRetiredResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.ListRetiredResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.listretiredresourcesresponse)>` | Promise  
  
### macSign(request, callback)
    
    
    public macSign(request: google.cloud.kms.v1.IMacSignRequest, callback: google.cloud.kms.v1.KeyManagementService.MacSignCallback): void;

Calls MacSign.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMacSignRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.imacsignrequest)`   
MacSignRequest message or plain object  
`callback` |  `[MacSignCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and MacSignResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### macSign(request)
    
    
    public macSign(request: google.cloud.kms.v1.IMacSignRequest): Promise<google.cloud.kms.v1.MacSignResponse>;

Calls MacSign.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMacSignRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.imacsignrequest)`   
MacSignRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.MacSignResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.macsignresponse)>` | Promise  
  
### macVerify(request, callback)
    
    
    public macVerify(request: google.cloud.kms.v1.IMacVerifyRequest, callback: google.cloud.kms.v1.KeyManagementService.MacVerifyCallback): void;

Calls MacVerify.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMacVerifyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.imacverifyrequest)`   
MacVerifyRequest message or plain object  
`callback` |  `[MacVerifyCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and MacVerifyResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### macVerify(request)
    
    
    public macVerify(request: google.cloud.kms.v1.IMacVerifyRequest): Promise<google.cloud.kms.v1.MacVerifyResponse>;

Calls MacVerify.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMacVerifyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.imacverifyrequest)`   
MacVerifyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.MacVerifyResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.macverifyresponse)>` | Promise  
  
### rawDecrypt(request, callback)
    
    
    public rawDecrypt(request: google.cloud.kms.v1.IRawDecryptRequest, callback: google.cloud.kms.v1.KeyManagementService.RawDecryptCallback): void;

Calls RawDecrypt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRawDecryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.irawdecryptrequest)`   
RawDecryptRequest message or plain object  
`callback` |  `[RawDecryptCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and RawDecryptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rawDecrypt(request)
    
    
    public rawDecrypt(request: google.cloud.kms.v1.IRawDecryptRequest): Promise<google.cloud.kms.v1.RawDecryptResponse>;

Calls RawDecrypt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRawDecryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.irawdecryptrequest)`   
RawDecryptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.RawDecryptResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.rawdecryptresponse)>` | Promise  
  
### rawEncrypt(request, callback)
    
    
    public rawEncrypt(request: google.cloud.kms.v1.IRawEncryptRequest, callback: google.cloud.kms.v1.KeyManagementService.RawEncryptCallback): void;

Calls RawEncrypt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRawEncryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.irawencryptrequest)`   
RawEncryptRequest message or plain object  
`callback` |  `[RawEncryptCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and RawEncryptResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rawEncrypt(request)
    
    
    public rawEncrypt(request: google.cloud.kms.v1.IRawEncryptRequest): Promise<google.cloud.kms.v1.RawEncryptResponse>;

Calls RawEncrypt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRawEncryptRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.irawencryptrequest)`   
RawEncryptRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.RawEncryptResponse](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.rawencryptresponse)>` | Promise  
  
### restoreCryptoKeyVersion(request, callback)
    
    
    public restoreCryptoKeyVersion(request: google.cloud.kms.v1.IRestoreCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersionCallback): void;

Calls RestoreCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.irestorecryptokeyversionrequest)`   
RestoreCryptoKeyVersionRequest message or plain object  
`callback` |  `[RestoreCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreCryptoKeyVersion(request)
    
    
    public restoreCryptoKeyVersion(request: google.cloud.kms.v1.IRestoreCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls RestoreCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestoreCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.irestorecryptokeyversionrequest)`   
RestoreCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
### updateCryptoKey(request, callback)
    
    
    public updateCryptoKey(request: google.cloud.kms.v1.IUpdateCryptoKeyRequest, callback: google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyCallback): void;

Calls UpdateCryptoKey.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdatecryptokeyrequest)`   
UpdateCryptoKeyRequest message or plain object  
`callback` |  `[UpdateCryptoKeyCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKey  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCryptoKey(request)
    
    
    public updateCryptoKey(request: google.cloud.kms.v1.IUpdateCryptoKeyRequest): Promise<google.cloud.kms.v1.CryptoKey>;

Calls UpdateCryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCryptoKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdatecryptokeyrequest)`   
UpdateCryptoKeyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKey](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokey-class)>` | Promise  
  
### updateCryptoKeyPrimaryVersion(request, callback)
    
    
    public updateCryptoKeyPrimaryVersion(request: google.cloud.kms.v1.IUpdateCryptoKeyPrimaryVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersionCallback): void;

Calls UpdateCryptoKeyPrimaryVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCryptoKeyPrimaryVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdatecryptokeyprimaryversionrequest)`   
UpdateCryptoKeyPrimaryVersionRequest message or plain object  
`callback` |  `[UpdateCryptoKeyPrimaryVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKey  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCryptoKeyPrimaryVersion(request)
    
    
    public updateCryptoKeyPrimaryVersion(request: google.cloud.kms.v1.IUpdateCryptoKeyPrimaryVersionRequest): Promise<google.cloud.kms.v1.CryptoKey>;

Calls UpdateCryptoKeyPrimaryVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCryptoKeyPrimaryVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdatecryptokeyprimaryversionrequest)`   
UpdateCryptoKeyPrimaryVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKey](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokey-class)>` | Promise  
  
### updateCryptoKeyVersion(request, callback)
    
    
    public updateCryptoKeyVersion(request: google.cloud.kms.v1.IUpdateCryptoKeyVersionRequest, callback: google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyVersionCallback): void;

Calls UpdateCryptoKeyVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdatecryptokeyversionrequest)`   
UpdateCryptoKeyVersionRequest message or plain object  
`callback` |  `[UpdateCryptoKeyVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)`   
Node-style callback called with the error, if any, and CryptoKeyVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCryptoKeyVersion(request)
    
    
    public updateCryptoKeyVersion(request: google.cloud.kms.v1.IUpdateCryptoKeyVersionRequest): Promise<google.cloud.kms.v1.CryptoKeyVersion>;

Calls UpdateCryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCryptoKeyVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iupdatecryptokeyversionrequest)`   
UpdateCryptoKeyVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.kms.v1.CryptoKeyVersion](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.cryptokeyversion-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
