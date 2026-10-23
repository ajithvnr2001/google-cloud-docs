---
url: https://docs.cloud.google.com/kms/docs/grpc/
title: Using gRPC with Cloud KMS \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:38.078451+00:00
---

# Using gRPC with Cloud KMS  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Using gRPC with Cloud KMS Stay organized with collections  Save and categorize content based on your preferences. 

If you are using manually created [gRPC](https://grpc.io/) libraries to make calls to Cloud Key Management Service, you must specify a `x-google-request-params` value in the metadata, or header, of the call. The proper use of `x-google-request-params` will route the call to the appropriate region for your Cloud KMS resources.

Set the `x-google-request-params` value to a field in the method's request as shown in the following table.

Method | Request field  
---|---  
[AsymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt) | [AsymmetricDecryptRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.AsymmetricDecryptRequest.FIELDS.string.google.cloud.kms.v1.AsymmetricDecryptRequest.name)  
[AsymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.AsymmetricSign) | [AsymmetricSignRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.AsymmetricSignRequest.FIELDS.string.google.cloud.kms.v1.AsymmetricSignRequest.name)  
[CreateCryptoKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.CreateCryptoKey) | [CreateCryptoKeyRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.CreateCryptoKeyRequest.FIELDS.string.google.cloud.kms.v1.CreateCryptoKeyRequest.parent)  
[CreateCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion) | [CreateCryptoKeyVersionRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.CreateCryptoKeyVersionRequest.FIELDS.string.google.cloud.kms.v1.CreateCryptoKeyVersionRequest.parent)  
[CreateImportJob](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.CreateImportJob) | [CreateImportJobRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.CreateImportJobRequest.FIELDS.string.google.cloud.kms.v1.CreateImportJobRequest.parent)  
[CreateKeyRing](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.CreateKeyRing) | [CreateKeyRingRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.CreateKeyRingRequest.FIELDS.string.google.cloud.kms.v1.CreateKeyRingRequest.parent)  
[Decrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.Decrypt) | [DecryptRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.DecryptRequest.FIELDS.string.google.cloud.kms.v1.DecryptRequest.name)  
[DestroyCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion) | [DestroyCryptoKeyVersionRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.DestroyCryptoKeyVersionRequest.FIELDS.string.google.cloud.kms.v1.DestroyCryptoKeyVersionRequest.name)  
[Encrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.Encrypt) | [EncryptRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.EncryptRequest.FIELDS.string.google.cloud.kms.v1.EncryptRequest.name)  
[GenerateRandomBytes](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes) | [GenerateRandomBytesRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.GenerateRandomBytesRequest.FIELDS.string.google.cloud.kms.v1.GenerateRandomBytesRequest.location)  
[GetCryptoKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.GetCryptoKey) | [GetCryptoKeyRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.GetCryptoKeyRequest.FIELDS.string.google.cloud.kms.v1.GetCryptoKeyRequest.name)  
[GetCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.GetCryptoKeyVersion) | [GetCryptoKeyVersionRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.GetCryptoKeyVersionRequest.FIELDS.string.google.cloud.kms.v1.GetCryptoKeyVersionRequest.name)  
[GetImportJob](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.GetImportJob) | [GetImportJobRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.GetImportJobRequest.FIELDS.string.google.cloud.kms.v1.GetImportJobRequest.name)  
[GetKeyRing](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.GetKeyRing) | [GetKeyRingRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.GetKeyRingRequest.FIELDS.string.google.cloud.kms.v1.GetKeyRingRequest.name)  
[GetPublicKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.GetPublicKey) | [GetPublicKeyRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.GetPublicKeyRequest.FIELDS.string.google.cloud.kms.v1.GetPublicKeyRequest.name)  
[ImportCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion) | [ImportCryptoKeyVersionRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.ImportCryptoKeyVersionRequest.FIELDS.string.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.parent)  
[ListCryptoKeyVersions](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions) | [ListCryptoKeyVersionsRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.ListCryptoKeyVersionsRequest.FIELDS.string.google.cloud.kms.v1.ListCryptoKeyVersionsRequest.parent)  
[ListCryptoKeys](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.ListCryptoKeys) | [ListCryptoKeysRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.ListCryptoKeysRequest.FIELDS.string.google.cloud.kms.v1.ListCryptoKeysRequest.parent)  
[ListImportJobs](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.ListImportJobs) | [ListImportJobsRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.ListImportJobsRequest.FIELDS.string.google.cloud.kms.v1.ListImportJobsRequest.parent)  
[ListKeyRings](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.ListKeyRings) | [ListKeyRingsRequest.parent](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.ListKeyRingsRequest.FIELDS.string.google.cloud.kms.v1.ListKeyRingsRequest.parent)  
[MacSign](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.MacSign) | [MacSignRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.MacSignRequest.FIELDS.string.google.cloud.kms.v1.MacSignRequest.name)  
[MacVerify](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.MacVerify) | [MacVerifyRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.MacVerifyRequest.FIELDS.string.google.cloud.kms.v1.MacVerifyRequest.name)  
[RawDecrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.RawDecrypt) | [RawDecryptRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.RawDecryptRequest.FIELDS.string.google.cloud.kms.v1.RawDecryptRequest.name)  
[RawEncrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.RawEncrypt) | [RawEncryptRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.RawEncryptRequest.FIELDS.string.google.cloud.kms.v1.RawEncryptRequest.name)  
[RestoreCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion) | [RestoreCryptoKeyVersionRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.RestoreCryptoKeyVersionRequest.FIELDS.string.google.cloud.kms.v1.RestoreCryptoKeyVersionRequest.name)  
[UpdateCryptoKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.UpdateCryptoKey) | [UpdateCryptoKeyRequest.crypto_key.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.CryptoKey.FIELDS.string.google.cloud.kms.v1.CryptoKey.name)  
[UpdateCryptoKeyPrimaryVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion) | [UpdateCryptoKeyPrimaryVersionRequest.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.UpdateCryptoKeyPrimaryVersionRequest.FIELDS.string.google.cloud.kms.v1.UpdateCryptoKeyPrimaryVersionRequest.name)  
[UpdateCryptoKeyVersion](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyVersion) | [UpdateCryptoKeyVersionRequest.crypto_key_version.name](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.CryptoKeyVersion.FIELDS.string.google.cloud.kms.v1.CryptoKeyVersion.name)  
  
## Setting the request field

The following examples show where to specify the resource name in various methods. Replace the text styled as place-holder with the actual values used in your Cloud KMS resource IDs.

### Decrypt example

If you are making a call to [Decrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.Decrypt), you need to populate the following fields in your request:
    
    
    name: 'projects/project-id/locations/location/keyRings/key-ring/cryptoKeys/key-name/'
    ciphertext: 'iQALWM/r6alAxQm0VQe3...'
    

The value assigned to the `name` field is the resource name of your CryptoKey. To properly route the call, you must also include this resource name in the call metadata, in the following form:
    
    
    x-goog-request-params: 'name=projects/project-id/locations/location/keyRings/key-ring/cryptoKeys/key-name/'
    

### CreateKeyRing example

If you are making a call to [CreateKeyRing](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.CreateKeyRing), you need to populate the following fields in your request:
    
    
    parent: 'projects/project-id/locations/location/'
    key_ring_id: 'myKeyRing'
    ...
    

The call metadata also needs to contain the `parent` resource name:
    
    
    x-goog-request-params: 'parent=projects/project-id/locations/location/'
    

### UpdateCryptoKey example

If you are making a call to [UpdateCryptoKey](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.UpdateCryptoKey), you need to populate the following fields in your request:
    
    
    name: 'projects/project-id/locations/location/keyRings/key-ring/cryptoKeys/key-name/'
    field_mask: ...
    

The metadata also needs to contain the `name` resource name. Note the format uses `crypto_key.name=`, not `name=`:
    
    
    x-goog-request-params: 'crypto_key.name=projects/project-id/locations/location/keyRings/key-ring/cryptoKeys/key-name/'
    

## Adding metadata using C++

If you are using C++, call `ClientContext::AddMetadata` before making your RPC call to add the appropriate information to the call metadata.

For example, if you are adding metadata for a call to [Decrypt](https://docs.cloud.google.com/kms/docs/reference/rpc/google.cloud.kms.v1#google.cloud.kms.v1.KeyManagementService.Decrypt):
    
    
    context.AddMetadata("x-goog-request-params",
                        "name=projects/project-id/locations/location/keyRings/key-ring-name/cryptoKeys/key-name/");
    

You can then pass the context to your method call as usual, along with your request and response protocol buffers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
