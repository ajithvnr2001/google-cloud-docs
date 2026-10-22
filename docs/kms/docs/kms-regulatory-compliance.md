---
url: https://docs.cloud.google.com/kms/docs/kms-regulatory-compliance/
title: Regulatory support in Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:16.275947+00:00
---

# Regulatory support in Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/kms-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Resources ](https://docs.cloud.google.com/kms/docs/resources)



Send feedback 

#  Regulatory support in Cloud Key Management Service Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Cloud Key Management Service that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllIndia Data BoundaryAustralia Data Boundary and SupportCanada Data Boundary and SupportEU Data Boundary and SupportIsrael Data Boundary and SupportJapan Data BoundaryUS Data Boundary and SupportData Boundary for CJISData Boundary for Canada Protected BData Boundary for FedRAMP HighData Boundary for FedRAMP ModerateData Boundary for IRS Publication 1075Data Boundary for ITARData Boundary for Impact Level 2 (IL2)Data Boundary for Impact Level 4 (IL4)Data Boundary for Impact Level 5 (IL5)EU Data Boundary with Access JustificationsKingdom of Saudi Arabia (KSA) Data Boundary with Access JustificationsSovereign Controls Advanced KSA CNTXTSovereign Controls Foundation KSA CNTXTSovereign Controls by Indra / MinsaitSovereign Controls by PSN (TIM)Sovereign Controls by S3NS / ThalesSovereign Controls by T-SystemsUS Data Boundary for Healthcare and Life Sciences  
  
---  
  
## India Data Boundary

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of India Data Boundary. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under India Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under India Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under India Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under India Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under India Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under India Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key access controls | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `keyAccessJustificationsPolicyConfig.name`

  
Key configuration | 

  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`
  * `cryptoKey.cryptoKeyBackend`
  * `ekmConnection.cryptoSpacePath`
  * `wrappingKey`

  
Key handle management | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key material import | 

  * `autokeyConfig.etag`
  * `cryptoKeyVersion`
  * `ekmConnection.etag`
  * `importJob`
  * `importingKey`

  
Labeling | 

  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Project and location | 

  * `project`

  
Quorum and access proposals | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `name`
  * `parent`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Australia Data Boundary and Support

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Australia Data Boundary and Support. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Australia Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Australia Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Australia Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Australia Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Australia Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Australia Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
External key management | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
HSM instance proposals | 

  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposalId`

  
Import job configuration | 

  * `importJob`
  * `importJob.cryptoKeyBackend`

  
Key access control | 

  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `keyAccessJustificationsPolicyConfig.name`

  
Key handle management | 

  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`
  * `ekmConfig.defaultEkmConnection`

  
Key version management | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersionId`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
  
  
  
## Canada Data Boundary and Support

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Canada Data Boundary and Support. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Canada Data Boundary and Support in the following Google Cloud regions:

  * northamerica-northeast1
  * northamerica-northeast2



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Canada Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Canada Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Canada Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Canada Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Canada Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Canada Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Cryptographic key details | 

  * `cryptoKey`
  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
EKM configuration | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Import job configuration | 

  * `importJob`
  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key access control | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key handle management | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key version configuration | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `cryptoKeyVersionId`

  
List and filter options | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Resource identification | 

  * `name`
  * `project`

  
Resource management | 

  * `parent`
  * `updateMask.paths`

  
  
  
  
## EU Data Boundary and Support

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of EU Data Boundary and Support. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for EU Data Boundary and Support in the following Google Cloud regions:

  * europe-west8
  * europe-west9
  * europe-west3



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Autokey configuration | 

  * `autokeyConfig.etag`
  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`

  
Context and quorum | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`

  
Crypto key version specifics | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Ekm connection details | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.etag`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Import job details | 

  * `importJob`
  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key handle configuration | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`

  
Pagination | 

  * `pageToken`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `keyHandleId`
  * `name`
  * `parent`
  * `project`

  
Wrapping key information | 

  * `wrappingKey`

  
  
  
  
## Israel Data Boundary and Support

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Israel Data Boundary and Support. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Israel Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Israel Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Israel Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Israel Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Israel Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Israel Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual data | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
External key management | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConfig.defaultEkmConnection`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
HSM proposal details | 

  * `singleTenantHsmInstance.name`
  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Import job configuration | 

  * `importJob`
  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key access control | 

  * `autokeyConfig.name`
  * `ekmConnectionId`
  * `keyAccessJustificationsPolicyConfig.name`
  * `keyHandle.name`
  * `keyHandleId`
  * `wrappingKey`

  
Key configuration | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Key version information | 

  * `cryptoKey`
  * `cryptoKeyVersion`
  * `cryptoKeyVersionId`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
Update mask | 

  * `updateMask.paths`

  
  
  
  
## Japan Data Boundary

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Japan Data Boundary. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Japan Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Japan Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Japan Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Japan Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Japan Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Japan Data Boundary.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control and permissions | 

  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `keyAccessJustificationsPolicyConfig.name`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
HSM instance management | 

  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Key management | 

  * `autokeyConfig.etag`
  * `autokeyConfig.keyProject`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.etag`
  * `ekmConnectionId`

  
Key version configuration | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `cryptoKeyVersionId`
  * `importJob.cryptoKeyBackend`

  
Key wrapping | 

  * `cryptoKey`
  * `importingKey`
  * `wrappingKey`

  
List and filtering options | 

  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`
  * `filter`
  * `orderBy`
  * `pageToken`

  
Project and backend configuration | 

  * `cryptoKey.cryptoKeyBackend`
  * `project`

  
Resource identification | 

  * `keyHandle.name`
  * `keyHandleId`
  * `name`
  * `parent`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
Update mask | 

  * `updateMask.paths`

  
  
  
  
## US Data Boundary and Support

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of US Data Boundary and Support. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for US Data Boundary and Support in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary and Support.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Configuration updates | 

  * `updateMask.paths`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
EKM configuration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Import job details | 

  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key access justification | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key handle details | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`

  
Key management parameters | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `wrappingKey`

  
Pagination | 

  * `pageToken`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `keyHandleId`
  * `name`
  * `parent`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Data Boundary for CJIS

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for CJIS. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for CJIS in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for CJIS.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for CJIS.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for CJIS.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for CJIS.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for CJIS.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for CJIS.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
External key configuration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
HSM instance proposals | 

  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`
  * `singleTenantHsmInstanceProposalId`

  
Import job configuration | 

  * `importJob`
  * `importJob.cryptoKeyBackend`

  
Key creation and update | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`
  * `updateMask.paths`

  
Key handle details | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnectionId`

  
Pagination | 

  * `pageToken`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
  
  
  
## Data Boundary for Canada Protected B

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for Canada Protected B. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for Canada Protected B in the following Google Cloud regions:

  * northamerica-northeast1
  * northamerica-northeast2



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Canada Protected B.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Canada Protected B.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Canada Protected B.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Canada Protected B.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Canada Protected B.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Canada Protected B.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Import job configuration | 

  * `importJob`
  * `importJob.cryptoKeyBackend`

  
Key configuration - autokey | 

  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`

  
Key configuration - ekm | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Key configuration - external protection | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Key handle configuration | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`

  
Key metadata | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Quorum and trust configuration | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Data Boundary for FedRAMP High

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for FedRAMP High. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for FedRAMP High in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP High.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Context and authentication | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`

  
Crypto key attributes | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
External key integration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
HSM instance proposals | 

  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Import job details | 

  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key handle management | 

  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key management configuration | 

  * `autokeyConfig.name`
  * `ekmConfig.defaultEkmConnection`
  * `keyAccessJustificationsPolicyConfig.name`
  * `wrappingKey`

  
Pagination | 

  * `pageToken`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`

  
  
  
  
## Data Boundary for FedRAMP Moderate

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for FedRAMP Moderate. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP Moderate.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP Moderate.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP Moderate.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP Moderate.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP Moderate.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for FedRAMP Moderate.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control and policies | 

  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `keyAccessJustificationsPolicyConfig.name`

  
EKM connection details | 

  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.etag`
  * `ekmConnectionId`

  
Import and export operations | 

  * `importJob`
  * `importingKey`
  * `wrappingKey`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `ekmConfig.defaultEkmConnection`

  
Key version management | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Labeling and metadata | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Pagination and filtering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Quorum and multi-factor authentication | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
Resource specific ids | 

  * `cryptoKeyVersionId`
  * `keyHandleId`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Data Boundary for IRS Publication 1075

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for IRS Publication 1075. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for IRS Publication 1075 in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for IRS Publication 1075.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for IRS Publication 1075.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for IRS Publication 1075.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for IRS Publication 1075.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for IRS Publication 1075.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for IRS Publication 1075.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
EKM connection details | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key access control | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `keyAccessJustificationsPolicyConfig.name`
  * `wrappingKey`

  
Key handle details | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key management configuration | 

  * `autokeyConfig.etag`
  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `ekmConnection.etag`
  * `importJob.cryptoKeyBackend`

  
Key version management | 

  * `cryptoKey`
  * `cryptoKeyVersion`
  * `importJob`

  
Labels and metadata | 

  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Quorum and trust management | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
External key management (ekm) configuration | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.etag`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Filtering and pagination | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key access control | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key attributes | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Key handle management | 

  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key import and wrapping | 

  * `importJob`
  * `importJob.cryptoKeyBackend`
  * `wrappingKey`

  
Key version management | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `cryptoKeyVersionId`

  
Quorum and security proposals | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
  
  
  
## Data Boundary for Impact Level 2 (IL2)

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for Impact Level 2 (IL2). | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for Impact Level 2 (IL2) in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 2 (IL2).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 2 (IL2).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 2 (IL2).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 2 (IL2).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 2 (IL2).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 2 (IL2).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control and permissions | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`
  * `keyAccessJustificationsPolicyConfig.name`
  * `wrappingKey`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Import job configuration | 

  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Key version configuration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Pagination | 

  * `pageToken`

  
Quorum and security proposals | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
Update masking | 

  * `updateMask.paths`

  
  
  
  
## Data Boundary for Impact Level 4 (IL4)

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for Impact Level 4 (IL4). | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for Impact Level 4 (IL4) in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Data Boundary for Impact Level 4 (IL4). By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: SOFTWARE`
  * `Allowed: HSM`
  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 4 (IL4).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 4 (IL4).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 4 (IL4).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 4 (IL4).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 4 (IL4).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 4 (IL4).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control & permissions | 

  * `keyHandle.resourceTypeSelector`
  * `wrappingKey`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Key identifiers | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `keyHandleId`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `importJob.cryptoKeyBackend`

  
Key version configuration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Pagination | 

  * `pageToken`

  
Quorum and trust management | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
Update control | 

  * `autokeyConfig.etag`
  * `ekmConnection.etag`
  * `updateMask.paths`

  
  
  
  
## Data Boundary for Impact Level 5 (IL5)

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Data Boundary for Impact Level 5 (IL5). | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Data Boundary for Impact Level 5 (IL5) in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Data Boundary for Impact Level 5 (IL5). By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: SOFTWARE`
  * `Allowed: HSM`
  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 5 (IL5).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 5 (IL5).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 5 (IL5).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 5 (IL5).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 5 (IL5).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for Impact Level 5 (IL5).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control and policy | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`
  * `ekmConnection.etag`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `keyAccessJustificationsPolicyConfig.name`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Key configuration | 

  * `autokeyConfig.keyProject`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `importJob.cryptoKeyBackend`

  
Key version configuration | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `wrappingKey`

  
Object identification | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `keyHandleId`

  
Paging | 

  * `pageToken`

  
Quorum and multi-factor authentication | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
Update mask | 

  * `updateMask.paths`

  
  
  
  
## EU Data Boundary with Access Justifications

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of EU Data Boundary with Access Justifications. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for EU Data Boundary with Access Justifications in the following Google Cloud regions:

  * europe-west8
  * europe-west9
  * europe-west3



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to EU Data Boundary with Access Justifications. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under EU Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Autokey configuration | 

  * `autokeyConfig.etag`
  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Ekm connection service resolution | 

  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
External key integration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key access justifications | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key labels | 

  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Key version specifics | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersionId`
  * `importJob`
  * `importingKey`
  * `wrappingKey`

  
Quorum and trust management | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `ekmConnectionId`
  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications in the following Google Cloud regions:

  * me-central2



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`
  * `Allowed: SOFTWARE`
  * `Allowed: HSM`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Kingdom of Saudi Arabia (KSA) Data Boundary with Access Justifications.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.quorumChallengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`

  
Crypto key version | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersionId`

  
External key management | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
HSM instance proposals | 

  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Import job configuration | 

  * `importJob`
  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key access controls | 

  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `keyAccessJustificationsPolicyConfig.name`

  
Key handle and wrapping | 

  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`
  * `wrappingKey`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`

  
Labels | 

  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
  
  
  
## Sovereign Controls Advanced KSA CNTXT

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Sovereign Controls Advanced KSA CNTXT. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Sovereign Controls Advanced KSA CNTXT in the following Google Cloud regions:

  * me-central2



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Sovereign Controls Advanced KSA CNTXT. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Advanced KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Advanced KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Advanced KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Advanced KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Advanced KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Advanced KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control and permissions | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `keyHandle.resourceTypeSelector`

  
Autokey configuration specifics | 

  * `autokeyConfig.etag`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Ekm connection specifics | 

  * `ekmConnection.etag`
  * `ekmConnection.serviceResolvers.hostname`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key configuration | 

  * `autokeyConfig.name`
  * `keyAccessJustificationsPolicyConfig.name`
  * `singleTenantHsmInstance.name`
  * `singleTenantHsmInstanceProposal.name`

  
Key material and protection | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `importingKey`
  * `wrappingKey`

  
Quorum management | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `keyHandleId`
  * `name`
  * `parent`
  * `project`

  
Update mask | 

  * `updateMask.paths`

  
  
  
  
## Sovereign Controls Foundation KSA CNTXT

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Sovereign Controls Foundation KSA CNTXT. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Sovereign Controls Foundation KSA CNTXT in the following Google Cloud regions:

  * me-central2



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Sovereign Controls Foundation KSA CNTXT. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`
  * `Allowed: SOFTWARE`
  * `Allowed: HSM`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Foundation KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Foundation KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Foundation KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Foundation KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Foundation KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls Foundation KSA CNTXT.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
EKM connection details | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Import job details | 

  * `importJob`
  * `importJob.cryptoKeyBackend`
  * `importingKey`

  
Key access justifications | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key handle configuration | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key protection configuration | 

  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`
  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Quorum and trust management | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `name`
  * `parent`
  * `project`

  
Update masks | 

  * `updateMask.paths`

  
  
  
  
## Sovereign Controls by Indra / Minsait

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Sovereign Controls by Indra / Minsait. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Sovereign Controls by Indra / Minsait. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by Indra / Minsait.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by Indra / Minsait.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by Indra / Minsait.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by Indra / Minsait.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by Indra / Minsait.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by Indra / Minsait.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual data | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Cryptography key attributes | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key access justifications policy | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key configuration - autokey | 

  * `autokeyConfig.keyProject`
  * `autokeyConfig.name`

  
Key configuration - ekm | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Key handle configuration | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`

  
Key import and wrapping | 

  * `importJob.cryptoKeyBackend`
  * `importingKey`
  * `wrappingKey`

  
Key version configuration - external protection | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
  
  
  
## Sovereign Controls by PSN (TIM)

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Sovereign Controls by PSN (TIM). | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Sovereign Controls by PSN (TIM) in the following Google Cloud regions:

  * europe-west8



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Sovereign Controls by PSN (TIM). By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by PSN (TIM).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by PSN (TIM).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by PSN (TIM).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by PSN (TIM).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by PSN (TIM).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by PSN (TIM).

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access justification configuration | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
External key integration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Key attributes | 

  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Key configuration | 

  * `autokeyConfig.keyProject`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Key import parameters | 

  * `importJob.cryptoKeyBackend`
  * `wrappingKey`

  
Quorum and security proposals | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `cryptoKeyVersionId`
  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
Update masking | 

  * `updateMask.paths`

  
  
  
  
## Sovereign Controls by S3NS / Thales

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Sovereign Controls by S3NS / Thales. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Sovereign Controls by S3NS / Thales in the following Google Cloud regions:

  * europe-west9



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Sovereign Controls by S3NS / Thales. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by S3NS / Thales.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by S3NS / Thales.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by S3NS / Thales.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by S3NS / Thales.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by S3NS / Thales.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by S3NS / Thales.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Access control and permissions | 

  * `importJob.cryptoKeyBackend`
  * `importingKey`
  * `keyAccessJustificationsPolicyConfig.name`
  * `wrappingKey`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`

  
HSM instance proposals | 

  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`

  
Key access justification | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`

  
Key labels | 

  * `cryptoKey.labels.key`
  * `cryptoKey.labels.value`

  
Key management configuration | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`

  
Key version configuration | 

  * `cryptoKeyVersion`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `cryptoKeyVersionId`

  
Pagination | 

  * `pageToken`

  
Quorum and security controls | 

  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`

  
  
  
  
## Sovereign Controls by T-Systems

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of Sovereign Controls by T-Systems. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for Sovereign Controls by T-Systems in the following Google Cloud regions:

  * europe-west3



### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Sovereign Controls by T-Systems. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[cloudkms.allowedProtectionLevels](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `Allowed: EXTERNAL`
  * `Allowed: EXTERNAL_VPC`

  
  
### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by T-Systems.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by T-Systems.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by T-Systems.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by T-Systems.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by T-Systems.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under Sovereign Controls by T-Systems.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
AccessControlAndContext | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `keyAccessJustificationsPolicyConfig.name`
  * `quorumReply.challengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.quorumChallengeReplies.publicKeyPem`
  * `requiredActionQuorumReply.requiredChallengeReplies.publicKeyPem`

  
ConfigurationDetails | 

  * `cryptoKey.labels.key`
  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `importingKey`
  * `wrappingKey`

  
ExternalKeyIntegration | 

  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `ekmConnection.etag`

  
FilteringAndSorting | 

  * `filter`
  * `orderBy`
  * `updateMask.paths`

  
HSMSpecificParameters | 

  * `singleTenantHsmInstance.name`
  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Identification | 

  * `cryptoKeyVersionId`
  * `ekmConnectionId`
  * `keyHandleId`
  * `name`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
KeyManagement | 

  * `autokeyConfig.keyProject`
  * `cryptoKey.cryptoKeyBackend`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `importJob.cryptoKeyBackend`

  
KeyMaterialHandling | 

  * `cryptoKey`
  * `cryptoKeyVersion`
  * `keyHandle.resourceTypeSelector`

  
Pagination | 

  * `pageToken`

  
ResourceHierarchy | 

  * `parent`
  * `project`

  
  
  
  
## US Data Boundary for Healthcare and Life Sciences

### Supported services

The following table lists the Cloud Key Management Service APIs and versions that meet the requirements of US Data Boundary for Healthcare and Life Sciences. | Service | Version | Status  
---|---|---  
cloudkms.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Cloud Key Management Service is available for US Data Boundary for Healthcare and Life Sciences in the following Google Cloud regions:

  * us-east1
  * us-east4
  * us-west2
  * us-west1
  * us-central1
  * us-west3
  * us-central2
  * us-west4
  * us-east5
  * us-south1



### API fields for sensitive data

#### Resource: cloudkms.googleapis.com/CryptoKey

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary for Healthcare and Life Sciences.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeys`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/**}:encrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Encrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataChecksum.crc32c.value`
  * `additionalAuthenticatedDataCrc32c.value`
  * `plaintext`
  * `plaintextChecksum.crc32c.value`
  * `plaintextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*}:decrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/cryptoKeys` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateCryptoKey`

| 

  * `cryptoKeyId`

  
  
#### Resource: cloudkms.googleapis.com/CryptoKeyVersion

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary for Healthcare and Life Sciences.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*/cryptoKeys/*}/cryptoKeyVersions` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:asymmetricSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.AsymmetricSign`

| 

  * `data`
  * `dataCrc32c.value`
  * `digest.externalMu`
  * `digest.sha256`
  * `digest.sha384`
  * `digest.sha512`
  * `digestCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:decapsulate` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.Decapsulate`

| 

  * `ciphertext`
  * `ciphertextCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macSign` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacSign`

| 

  * `data`
  * `dataCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:macVerify` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.MacVerify`

| 

  * `data`
  * `dataCrc32c.value`
  * `mac`
  * `macCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawDecrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawDecrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `ciphertext`
  * `ciphertextCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}:rawEncrypt` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.RawEncrypt`

| 

  * `additionalAuthenticatedData`
  * `additionalAuthenticatedDataCrc32c.value`
  * `initializationVector`
  * `initializationVectorCrc32c.value`
  * `plaintext`
  * `plaintextCrc32c.value`

  
  
#### Resource: cloudkms.googleapis.com/ImportJob

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary for Healthcare and Life Sciences.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/importJobs/*}` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetImportJob`

| 

  * `publicKeyFormat`

  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListImportJobs`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*/keyRings/*}/importJobs` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateImportJob`

| 

  * `importJobId`

  
  
#### Resource: cloudkms.googleapis.com/KeyRing

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary for Healthcare and Life Sciences.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.ListKeyRings`

| 

  * `filter`
  * `orderBy`

  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/keyRings` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.CreateKeyRing`

| 

  * `keyRingId`

  
  
#### Resource: cloudkms.googleapis.com/Location

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary for Healthcare and Life Sciences.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `POST` `/v1/{location=projects/*/locations/*}:generateRandomBytes` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes`

| 

  * `lengthBytes`
  * `location`
  * `protectionLevel`

  
  
#### Resource: cloudkms.googleapis.com/PublicKey

The following table specifies the API resources and fields that are designed to handle data that is protected under US Data Boundary for Healthcare and Life Sciences.

API Method | Protected fields  
---|---  
Service: `cloudkms.googleapis.com` REST API: `GET` `/v1/{name=projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*}/publicKey` RPC methods:

  * `google.cloud.kms.v1.KeyManagementService.GetPublicKey`

| 

  * `publicKeyFormat`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Contextual information | 

  * `callerProvidedContext.fields.key`
  * `callerProvidedContext.fields.value.stringValue`
  * `quorumReply.challengeReplies.publicKeyPem`

  
EKM connection details | 

  * `ekmConfig.defaultEkmConnection`
  * `ekmConnection.etag`
  * `ekmConnectionId`

  
Filtering and ordering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
HSM instance proposals | 

  * `singleTenantHsmInstanceProposal.addQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.name`
  * `singleTenantHsmInstanceProposal.registerTwoFactorAuthKeys.twoFactorPublicKeyPems`
  * `singleTenantHsmInstanceProposal.removeQuorumMember.twoFactorPublicKeyPem`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.name`
  * `singleTenantHsmInstanceProposal.upgradeKeyTrust.twoFactorPublicKeyPem`

  
Key access control | 

  * `keyAccessJustificationsPolicyConfig.name`

  
Key configuration | 

  * `autokeyConfig.keyProject`
  * `ekmConnection.cryptoSpacePath`
  * `ekmConnection.serviceResolvers.endpointFilter`
  * `ekmConnection.serviceResolvers.hostname`
  * `ekmConnection.serviceResolvers.serviceDirectoryService`
  * `importJob.cryptoKeyBackend`

  
Key handle details | 

  * `keyHandle.name`
  * `keyHandle.resourceTypeSelector`
  * `keyHandleId`

  
Key version configuration | 

  * `cryptoKey`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionBackendOverride`
  * `cryptoKeyVersion.externalProtectionLevelOptions.ekmConnectionKeyPath`
  * `cryptoKeyVersion.externalProtectionLevelOptions.externalKeyUri`
  * `importingKey`
  * `wrappingKey`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`
  * `singleTenantHsmInstanceId`
  * `singleTenantHsmInstanceProposalId`

  
Update mask | 

  * `updateMask.paths`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
