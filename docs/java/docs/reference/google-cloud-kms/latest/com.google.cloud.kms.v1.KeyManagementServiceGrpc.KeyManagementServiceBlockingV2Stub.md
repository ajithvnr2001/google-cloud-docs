---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub
title: Class KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:47.961757+00:00
---

# Class KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.8  2.5.3  2.4.4  2.3.1 
    
    
    public static final class KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub extends AbstractBlockingStub<KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service KeyManagementService.

Google Cloud Key Management Service Manages cryptographic keys and operations using those keys. Implements a REST model with the following objects:

  * KeyRing
  * CryptoKey
  * CryptoKeyVersion
  * ImportJob If you are using manual gRPC libraries, see [Using gRPC with Cloud KMS](https://cloud.google.com/kms/docs/grpc).



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub

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

### asymmetricDecrypt(AsymmetricDecryptRequest request)
    
    
    public AsymmetricDecryptResponse asymmetricDecrypt(AsymmetricDecryptRequest request)

Decrypts data that was encrypted with a public key retrieved from GetPublicKey corresponding to a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AsymmetricDecryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricDecryptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AsymmetricDecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricDecryptResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### asymmetricSign(AsymmetricSignRequest request)
    
    
    public AsymmetricSignResponse asymmetricSign(AsymmetricSignRequest request)

Signs data using a CryptoKeyVersion with CryptoKey.purpose ASYMMETRIC_SIGN, producing a signature that can be verified with the public key retrieved from GetPublicKey.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AsymmetricSignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricSignRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AsymmetricSignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricSignResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceGrpc.KeyManagementServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createCryptoKey(CreateCryptoKeyRequest request)
    
    
    public CryptoKey createCryptoKey(CreateCryptoKeyRequest request)

Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCryptoKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createCryptoKeyVersion(CreateCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion createCryptoKeyVersion(CreateCryptoKeyVersionRequest request)

Create a new CryptoKeyVersion in a CryptoKey. The server will assign the next sequential id. If unset, state will be set to ENABLED.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createImportJob(CreateImportJobRequest request)
    
    
    public ImportJob createImportJob(CreateImportJobRequest request)

Create a new ImportJob within a KeyRing. ImportJob.import_method is required.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateImportJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createKeyRing(CreateKeyRingRequest request)
    
    
    public KeyRing createKeyRing(CreateKeyRingRequest request)

Create a new KeyRing in a given Project and Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateKeyRingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateKeyRingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[KeyRing](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### decapsulate(DecapsulateRequest request)
    
    
    public DecapsulateResponse decapsulate(DecapsulateRequest request)

Decapsulates data that was encapsulated with a public key retrieved from GetPublicKey corresponding to a CryptoKeyVersion with CryptoKey.purpose KEY_ENCAPSULATION.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DecapsulateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecapsulateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DecapsulateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecapsulateResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### decrypt(DecryptRequest request)
    
    
    public DecryptResponse decrypt(DecryptRequest request)

Decrypts data that was protected by Encrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DecryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecryptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecryptResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCryptoKey(DeleteCryptoKeyRequest request)
    
    
    public Operation deleteCryptoKey(DeleteCryptoKeyRequest request)

Permanently deletes the given CryptoKey. All child CryptoKeyVersions must have been previously deleted using KeyManagementService.DeleteCryptoKeyVersion. The specified crypto key will be immediately and permanently deleted upon calling this method. This action cannot be undone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCryptoKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DeleteCryptoKeyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCryptoKeyVersion(DeleteCryptoKeyVersionRequest request)
    
    
    public Operation deleteCryptoKeyVersion(DeleteCryptoKeyVersionRequest request)

Permanently deletes the given CryptoKeyVersion. Only possible if the version has not been previously imported and if its state is one of DESTROYED, IMPORT_FAILED, or GENERATION_FAILED. Successfully imported CryptoKeyVersions cannot be deleted at this time. The specified version will be immediately and permanently deleted upon calling this method. This action cannot be undone.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DeleteCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### destroyCryptoKeyVersion(DestroyCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion destroyCryptoKeyVersion(DestroyCryptoKeyVersionRequest request)

Schedule a CryptoKeyVersion for destruction. Upon calling this method, CryptoKeyVersion.state will be set to DESTROY_SCHEDULED, and destroy_time will be set to the time destroy_scheduled_duration in the future. At that time, the state will automatically change to DESTROYED, and the key material will be irrevocably destroyed. Before the destroy_time is reached, RestoreCryptoKeyVersion may be called to reverse the process.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DestroyCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DestroyCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### encrypt(EncryptRequest request)
    
    
    public EncryptResponse encrypt(EncryptRequest request)

Encrypts data, so that it can only be recovered by a call to Decrypt. The CryptoKey.purpose must be ENCRYPT_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EncryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EncryptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EncryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EncryptResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### exportTrustedKeyWrappedCryptoKeyVersion(ExportTrustedKeyWrappedCryptoKeyVersionRequest request)
    
    
    public ExportTrustedKeyWrappedCryptoKeyVersionResponse exportTrustedKeyWrappedCryptoKeyVersion(ExportTrustedKeyWrappedCryptoKeyVersionRequest request)

Exports a CryptoKeyVersion with a trusted key. The CryptoKeyVersion must have trusted_wrapping_enabled set to true. The CryptoKeyVersion of the [wrapping_key] must have the AES_WRAPPING purpose. The [wrapping_key] must have the AES_256_KWP algorithm.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExportTrustedKeyWrappedCryptoKeyVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExportTrustedKeyWrappedCryptoKeyVersionResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### generateRandomBytes(GenerateRandomBytesRequest request)
    
    
    public GenerateRandomBytesResponse generateRandomBytes(GenerateRandomBytesRequest request)

Generate random bytes using the Cloud KMS randomness source in the provided location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateRandomBytesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GenerateRandomBytesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateRandomBytesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GenerateRandomBytesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCryptoKey(GetCryptoKeyRequest request)
    
    
    public CryptoKey getCryptoKey(GetCryptoKeyRequest request)

Returns metadata for a given CryptoKey, as well as its primary CryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCryptoKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetCryptoKeyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCryptoKeyVersion(GetCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion getCryptoKeyVersion(GetCryptoKeyVersionRequest request)

Returns metadata for a given CryptoKeyVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getImportJob(GetImportJobRequest request)
    
    
    public ImportJob getImportJob(GetImportJobRequest request)

Returns metadata for a given ImportJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetImportJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getKeyRing(GetKeyRingRequest request)
    
    
    public KeyRing getKeyRing(GetKeyRingRequest request)

Returns metadata for a given KeyRing.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetKeyRingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetKeyRingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[KeyRing](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getPublicKey(GetPublicKeyRequest request)
    
    
    public PublicKey getPublicKey(GetPublicKeyRequest request)

Returns the public key for the given CryptoKeyVersion. The CryptoKey.purpose must be ASYMMETRIC_SIGN or ASYMMETRIC_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPublicKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetPublicKeyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getRetiredResource(GetRetiredResourceRequest request)
    
    
    public RetiredResource getRetiredResource(GetRetiredResourceRequest request)

Retrieves a specific RetiredResource resource, which represents the record of a deleted CryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRetiredResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetRetiredResourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetiredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.RetiredResource)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importCryptoKeyVersion(ImportCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion importCryptoKeyVersion(ImportCryptoKeyVersionRequest request)

Import wrapped key material into a CryptoKeyVersion. All requests must specify a CryptoKey. If a CryptoKeyVersion is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the CryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importTrustedKeyWrappedCryptoKeyVersion(ImportTrustedKeyWrappedCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion importTrustedKeyWrappedCryptoKeyVersion(ImportTrustedKeyWrappedCryptoKeyVersionRequest request)

Import wrapped key material into a CryptoKeyVersion with a trusted key. All requests must specify a CryptoKey. If a CryptoKeyVersion is additionally specified in the request, key material will be reimported into that version. Otherwise, a new version will be created, and will be assigned the next sequential id within the CryptoKey. The CryptoKeyVersion will have trusted_wrapping_enabled set to true.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportTrustedKeyWrappedCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCryptoKeyVersions(ListCryptoKeyVersionsRequest request)
    
    
    public ListCryptoKeyVersionsResponse listCryptoKeyVersions(ListCryptoKeyVersionsRequest request)

Lists CryptoKeyVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCryptoKeyVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListCryptoKeyVersionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCryptoKeyVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListCryptoKeyVersionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCryptoKeys(ListCryptoKeysRequest request)
    
    
    public ListCryptoKeysResponse listCryptoKeys(ListCryptoKeysRequest request)

Lists CryptoKeys.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCryptoKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListCryptoKeysRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCryptoKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListCryptoKeysResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listImportJobs(ListImportJobsRequest request)
    
    
    public ListImportJobsResponse listImportJobs(ListImportJobsRequest request)

Lists ImportJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListImportJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListImportJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListImportJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListImportJobsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listKeyRings(ListKeyRingsRequest request)
    
    
    public ListKeyRingsResponse listKeyRings(ListKeyRingsRequest request)

Lists KeyRings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListKeyRingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListKeyRingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListKeyRingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListKeyRingsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listRetiredResources(ListRetiredResourcesRequest request)
    
    
    public ListRetiredResourcesResponse listRetiredResources(ListRetiredResourcesRequest request)

Lists the RetiredResources which are the records of deleted CryptoKeys. RetiredResources prevent the reuse of these resource names after deletion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRetiredResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListRetiredResourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListRetiredResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListRetiredResourcesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### macSign(MacSignRequest request)
    
    
    public MacSignResponse macSign(MacSignRequest request)

Signs data using a CryptoKeyVersion with CryptoKey.purpose MAC, producing a tag that can be verified by another source with the same key.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MacSignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.MacSignRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MacSignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.MacSignResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### macVerify(MacVerifyRequest request)
    
    
    public MacVerifyResponse macVerify(MacVerifyRequest request)

Verifies MAC tag using a CryptoKeyVersion with CryptoKey.purpose MAC, and returns a response that indicates whether or not the verification was successful.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MacVerifyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.MacVerifyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MacVerifyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.MacVerifyResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### rawDecrypt(RawDecryptRequest request)
    
    
    public RawDecryptResponse rawDecrypt(RawDecryptRequest request)

Decrypts data that was originally encrypted using a raw cryptographic mechanism. The CryptoKey.purpose must be RAW_ENCRYPT_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RawDecryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.RawDecryptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RawDecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.RawDecryptResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### rawEncrypt(RawEncryptRequest request)
    
    
    public RawEncryptResponse rawEncrypt(RawEncryptRequest request)

Encrypts data using portable cryptographic primitives. Most users should choose Encrypt and Decrypt rather than their raw counterparts. The CryptoKey.purpose must be RAW_ENCRYPT_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RawEncryptRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.RawEncryptRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RawEncryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.RawEncryptResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### restoreCryptoKeyVersion(RestoreCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion restoreCryptoKeyVersion(RestoreCryptoKeyVersionRequest request)

Restore a CryptoKeyVersion in the DESTROY_SCHEDULED state. Upon restoration of the CryptoKeyVersion, state will be set to DISABLED, and destroy_time will be cleared.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.RestoreCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCryptoKey(UpdateCryptoKeyRequest request)
    
    
    public CryptoKey updateCryptoKey(UpdateCryptoKeyRequest request)

Update a CryptoKey.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCryptoKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.UpdateCryptoKeyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCryptoKeyPrimaryVersion(UpdateCryptoKeyPrimaryVersionRequest request)
    
    
    public CryptoKey updateCryptoKeyPrimaryVersion(UpdateCryptoKeyPrimaryVersionRequest request)

Update the version of a CryptoKey that will be used in Encrypt. Returns an error if called on a key whose purpose is not ENCRYPT_DECRYPT.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCryptoKeyPrimaryVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.UpdateCryptoKeyPrimaryVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCryptoKeyVersion(UpdateCryptoKeyVersionRequest request)
    
    
    public CryptoKeyVersion updateCryptoKeyVersion(UpdateCryptoKeyVersionRequest request)

Update a CryptoKeyVersion's metadata. state may be changed between ENABLED and DISABLED using this method. See DestroyCryptoKeyVersion and RestoreCryptoKeyVersion to move between other states.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.UpdateCryptoKeyVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
