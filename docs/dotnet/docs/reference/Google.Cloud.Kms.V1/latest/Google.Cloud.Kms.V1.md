---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1
title: Google Cloud Key Management Service v1 API - Namespace Google.Cloud.Kms.V1 (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:51.573760+00:00
---

# Google Cloud Key Management Service v1 API - Namespace Google.Cloud.Kms.V1 (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Namespace Google.Cloud.Kms.V1 (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 

## Classes 

### [ApproveSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ApproveSingleTenantHsmInstanceProposalRequest)

Request message for [HsmManagement.ApproveSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal].

### [ApproveSingleTenantHsmInstanceProposalRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ApproveSingleTenantHsmInstanceProposalRequest.Types)

Container for nested types declared in the ApproveSingleTenantHsmInstanceProposalRequest message type.

### [ApproveSingleTenantHsmInstanceProposalRequest.Types.QuorumReply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ApproveSingleTenantHsmInstanceProposalRequest.Types.QuorumReply)

The reply to [QuorumParameters][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.QuorumParameters] for approving the proposal.

### [ApproveSingleTenantHsmInstanceProposalRequest.Types.RequiredActionQuorumReply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ApproveSingleTenantHsmInstanceProposalRequest.Types.RequiredActionQuorumReply)

The reply to [RequiredActionQuorumParameters][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.RequiredActionQuorumParameters] for approving the proposal.

### [ApproveSingleTenantHsmInstanceProposalResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ApproveSingleTenantHsmInstanceProposalResponse)

Response message for [HsmManagement.ApproveSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal].

### [AsymmetricDecryptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricDecryptRequest)

Request message for [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].

### [AsymmetricDecryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricDecryptResponse)

Response message for [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].

### [AsymmetricSignRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest)

Request message for [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

### [AsymmetricSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse)

Response message for [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

### [Autokey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Autokey)

Provides interfaces for using [Cloud KMS Autokey](https://cloud.google.com/kms/help/autokey) to provision new [CryptoKeys][google.cloud.kms.v1.CryptoKey], ready for Customer Managed Encryption Key (CMEK) use, on-demand. To support certain client tooling, this feature is modeled around a [KeyHandle][google.cloud.kms.v1.KeyHandle] resource: creating a [KeyHandle][google.cloud.kms.v1.KeyHandle] in a resource project and given location triggers Cloud KMS Autokey to provision a [CryptoKey][google.cloud.kms.v1.CryptoKey] in the configured key project and the same location.

Prior to use in a given resource project, [UpdateAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig] should have been called on an ancestor folder, setting the key project where Cloud KMS Autokey should create new [CryptoKeys][google.cloud.kms.v1.CryptoKey]. See documentation for additional prerequisites. To check what key project, if any, is currently configured on a resource project's ancestor folder, see [ShowEffectiveAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig].

### [Autokey.AutokeyBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Autokey.AutokeyBase)

Base class for server-side implementations of Autokey

### [Autokey.AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Autokey.AutokeyClient)

Client for Autokey

### [AutokeyAdmin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin)

Provides interfaces for managing [Cloud KMS Autokey](https://cloud.google.com/kms/help/autokey) folder-level or project-level configurations. A configuration is inherited by all descendent folders and projects. A configuration at a folder or project overrides any other configurations in its ancestry. Setting a configuration on a folder is a prerequisite for Cloud KMS Autokey, so that users working in a descendant project can request provisioned [CryptoKeys][google.cloud.kms.v1.CryptoKey], ready for Customer Managed Encryption Key (CMEK) use, on-demand when using the dedicated key project mode. This is not required when using the delegated key management mode for same-project keys.

### [AutokeyAdmin.AutokeyAdminBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminBase)

Base class for server-side implementations of AutokeyAdmin

### [AutokeyAdmin.AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdmin.AutokeyAdminClient)

Client for AutokeyAdmin

### [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient)

AutokeyAdmin client wrapper, for convenient use.

### [AutokeyAdminClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClientBuilder)

Builder class for [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient) to provide simple configuration of credentials, endpoint etc.

### [AutokeyAdminClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClientImpl)

AutokeyAdmin client wrapper implementation, for convenient use.

### [AutokeyAdminSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminSettings)

Settings for [AutokeyAdminClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyAdminClient) instances.

### [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient)

Autokey client wrapper, for convenient use.

### [AutokeyClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClientBuilder)

Builder class for [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient) to provide simple configuration of credentials, endpoint etc.

### [AutokeyClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClientImpl)

Autokey client wrapper implementation, for convenient use.

### [AutokeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig)

Cloud KMS Autokey configuration for a folder.

### [AutokeyConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig.Types)

Container for nested types declared in the AutokeyConfig message type.

### [AutokeyConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfigName)

Resource name for the `AutokeyConfig` resource.

### [AutokeySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeySettings)

Settings for [AutokeyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyClient) instances.

### [Certificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Certificate)

A [Certificate][google.cloud.kms.v1.Certificate] represents an X.509 certificate used to authenticate HTTPS connections to EKM replicas.

### [Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Challenge)

A challenge to be signed by a 2FA key.

### [ChallengeReply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ChallengeReply)

A reply to a challenge signed by a 2FA key.

### [ChecksummedData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ChecksummedData)

Data with integrity verification field.

### [CreateCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest)

Request message for [KeyManagementService.CreateCryptoKey][google.cloud.kms.v1.KeyManagementService.CreateCryptoKey].

### [CreateCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyVersionRequest)

Request message for [KeyManagementService.CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion].

### [CreateEkmConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateEkmConnectionRequest)

Request message for [EkmService.CreateEkmConnection][google.cloud.kms.v1.EkmService.CreateEkmConnection].

### [CreateImportJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateImportJobRequest)

Request message for [KeyManagementService.CreateImportJob][google.cloud.kms.v1.KeyManagementService.CreateImportJob].

### [CreateKeyHandleMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleMetadata)

Metadata message for [CreateKeyHandle][google.cloud.kms.v1.Autokey.CreateKeyHandle] long-running operation response.

### [CreateKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyHandleRequest)

Request message for [Autokey.CreateKeyHandle][google.cloud.kms.v1.Autokey.CreateKeyHandle].

### [CreateKeyRingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateKeyRingRequest)

Request message for [KeyManagementService.CreateKeyRing][google.cloud.kms.v1.KeyManagementService.CreateKeyRing].

### [CreateSingleTenantHsmInstanceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceMetadata)

Metadata message for [CreateSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance] long-running operation response.

### [CreateSingleTenantHsmInstanceProposalMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalMetadata)

Metadata message for [CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal] long-running operation response.

### [CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceProposalRequest)

Request message for [HsmManagement.CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal].

### [CreateSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateSingleTenantHsmInstanceRequest)

Request message for [HsmManagement.CreateSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance].

### [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey)

A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents a logical key that can be used for cryptographic operations.

A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made up of zero or more [versions][google.cloud.kms.v1.CryptoKeyVersion], which represent the actual key material used in cryptographic operations.

### [CryptoKey.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types)

Container for nested types declared in the CryptoKey message type.

### [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName)

Resource name for the `CryptoKey` resource.

### [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion)

A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an individual cryptographic key, and the associated key material.

An [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED] version can be used for cryptographic operations.

For security reasons, the raw cryptographic key material represented by a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] can never be viewed or exported. It can only be used to encrypt, decrypt, or sign data when an authorized user or application invokes Cloud KMS.

### [CryptoKeyVersion.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types)

Container for nested types declared in the CryptoKeyVersion message type.

### [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName)

Resource name for the `CryptoKeyVersion` resource.

### [CryptoKeyVersionTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate)

A [CryptoKeyVersionTemplate][google.cloud.kms.v1.CryptoKeyVersionTemplate] specifies the properties to use when creating a new [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion], either manually with [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] or automatically as a result of auto-rotation.

### [DecapsulateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateRequest)

Request message for [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].

### [DecapsulateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse)

Response message for [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].

### [DecryptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecryptRequest)

Request message for [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].

### [DecryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecryptResponse)

Response message for [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].

### [DeleteCryptoKeyMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata)

Represents the metadata of the [KeyManagementService.DeleteCryptoKey][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKey] long-running operation.

### [DeleteCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyRequest)

Request message for [KeyManagementService.DeleteCryptoKey][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKey].

### [DeleteCryptoKeyVersionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyVersionMetadata)

Represents the metadata of the [KeyManagementService.DeleteCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyVersion] long-running operation.

### [DeleteCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyVersionRequest)

Request message for [KeyManagementService.DeleteCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyVersion].

### [DeleteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteSingleTenantHsmInstanceProposalRequest)

Request message for [HsmManagement.DeleteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposal].

### [DestroyCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DestroyCryptoKeyVersionRequest)

Request message for [KeyManagementService.DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion].

### [Digest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Digest)

A [Digest][google.cloud.kms.v1.Digest] holds a cryptographic message digest.

### [EkmConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConfig)

An [EkmConfig][google.cloud.kms.v1.EkmConfig] is a singleton resource that represents configuration parameters that apply to all [CryptoKeys][google.cloud.kms.v1.CryptoKey] and [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] with a [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC] in a given project and location.

### [EkmConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConfigName)

Resource name for the `EkmConfig` resource.

### [EkmConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection)

An [EkmConnection][google.cloud.kms.v1.EkmConnection] represents an individual EKM connection. It can be used for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey] and [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] with a [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC], as well as performing cryptographic operations using keys created within the [EkmConnection][google.cloud.kms.v1.EkmConnection].

### [EkmConnection.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types)

Container for nested types declared in the EkmConnection message type.

### [EkmConnection.Types.ServiceResolver](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types.ServiceResolver)

A [ServiceResolver][google.cloud.kms.v1.EkmConnection.ServiceResolver] represents an EKM replica that can be reached within an [EkmConnection][google.cloud.kms.v1.EkmConnection].

### [EkmConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnectionName)

Resource name for the `EkmConnection` resource.

### [EkmService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmService)

Google Cloud Key Management EKM Service

Manages external cryptographic keys and operations using those keys. Implements a REST model with the following objects:

  * [EkmConnection][google.cloud.kms.v1.EkmConnection]



### [EkmService.EkmServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmService.EkmServiceBase)

Base class for server-side implementations of EkmService

### [EkmService.EkmServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmService.EkmServiceClient)

Client for EkmService

### [EkmServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmServiceClient)

EkmService client wrapper, for convenient use.

### [EkmServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmServiceClientBuilder)

Builder class for [EkmServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmServiceClient) to provide simple configuration of credentials, endpoint etc.

### [EkmServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmServiceClientImpl)

EkmService client wrapper implementation, for convenient use.

### [EkmServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmServiceSettings)

Settings for [EkmServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmServiceClient) instances.

### [EncryptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EncryptRequest)

Request message for [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

### [EncryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EncryptResponse)

Response message for [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

### [ExecuteSingleTenantHsmInstanceProposalMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExecuteSingleTenantHsmInstanceProposalMetadata)

Metadata message for [ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal] long-running operation response.

### [ExecuteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExecuteSingleTenantHsmInstanceProposalRequest)

Request message for [HsmManagement.ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal].

### [ExecuteSingleTenantHsmInstanceProposalResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExecuteSingleTenantHsmInstanceProposalResponse)

Response message for [HsmManagement.ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal].

### [ExportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExportTrustedKeyWrappedCryptoKeyVersionRequest)

Request message for [KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion].

### [ExportTrustedKeyWrappedCryptoKeyVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExportTrustedKeyWrappedCryptoKeyVersionResponse)

Response message for [KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion].

### [ExternalProtectionLevelOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExternalProtectionLevelOptions)

ExternalProtectionLevelOptions stores a group of additional fields for configuring a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] that are specific to the [EXTERNAL][google.cloud.kms.v1.ProtectionLevel.EXTERNAL] protection level and [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC] protection levels.

### [GenerateRandomBytesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GenerateRandomBytesRequest)

Request message for [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].

### [GenerateRandomBytesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GenerateRandomBytesResponse)

Response message for [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].

### [GetAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetAutokeyConfigRequest)

Request message for [GetAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.GetAutokeyConfig].

### [GetCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetCryptoKeyRequest)

Request message for [KeyManagementService.GetCryptoKey][google.cloud.kms.v1.KeyManagementService.GetCryptoKey].

### [GetCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetCryptoKeyVersionRequest)

Request message for [KeyManagementService.GetCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.GetCryptoKeyVersion].

### [GetEkmConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetEkmConfigRequest)

Request message for [EkmService.GetEkmConfig][google.cloud.kms.v1.EkmService.GetEkmConfig].

### [GetEkmConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetEkmConnectionRequest)

Request message for [EkmService.GetEkmConnection][google.cloud.kms.v1.EkmService.GetEkmConnection].

### [GetImportJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetImportJobRequest)

Request message for [KeyManagementService.GetImportJob][google.cloud.kms.v1.KeyManagementService.GetImportJob].

### [GetKeyHandleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetKeyHandleRequest)

Request message for [GetKeyHandle][google.cloud.kms.v1.Autokey.GetKeyHandle].

### [GetKeyRingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetKeyRingRequest)

Request message for [KeyManagementService.GetKeyRing][google.cloud.kms.v1.KeyManagementService.GetKeyRing].

### [GetPublicKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetPublicKeyRequest)

Request message for [KeyManagementService.GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].

### [GetRetiredResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetRetiredResourceRequest)

Request message for [KeyManagementService.GetRetiredResource][google.cloud.kms.v1.KeyManagementService.GetRetiredResource].

### [GetSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetSingleTenantHsmInstanceProposalRequest)

Request message for [HsmManagement.GetSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposal].

### [GetSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GetSingleTenantHsmInstanceRequest)

Request message for [HsmManagement.GetSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstance].

### [HsmManagement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagement)

Google Cloud HSM Management Service

Provides interfaces for managing HSM instances.

Implements a REST model with the following objects:

  * [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
  * [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]



### [HsmManagement.HsmManagementBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagement.HsmManagementBase)

Base class for server-side implementations of HsmManagement

### [HsmManagement.HsmManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagement.HsmManagementClient)

Client for HsmManagement

### [HsmManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagementClient)

HsmManagement client wrapper, for convenient use.

### [HsmManagementClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagementClientBuilder)

Builder class for [HsmManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagementClient) to provide simple configuration of credentials, endpoint etc.

### [HsmManagementClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagementClientImpl)

HsmManagement client wrapper implementation, for convenient use.

### [HsmManagementSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagementSettings)

Settings for [HsmManagementClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.HsmManagementClient) instances.

### [ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportCryptoKeyVersionRequest)

Request message for [KeyManagementService.ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].

### [ImportJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJob)

An [ImportJob][google.cloud.kms.v1.ImportJob] can be used to create [CryptoKeys][google.cloud.kms.v1.CryptoKey] and [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] using pre-existing key material, generated outside of Cloud KMS.

When an [ImportJob][google.cloud.kms.v1.ImportJob] is created, Cloud KMS will generate a "wrapping key", which is a public/private key pair. You use the wrapping key to encrypt (also known as wrap) the pre-existing key material to protect it during the import process. The nature of the wrapping key depends on the choice of [import_method][google.cloud.kms.v1.ImportJob.import_method]. When the wrapping key generation is complete, the [state][google.cloud.kms.v1.ImportJob.state] will be set to [ACTIVE][google.cloud.kms.v1.ImportJob.ImportJobState.ACTIVE] and the [public_key][google.cloud.kms.v1.ImportJob.public_key] can be fetched. The fetched public key can then be used to wrap your pre-existing key material.

Once the key material is wrapped, it can be imported into a new [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in an existing [CryptoKey][google.cloud.kms.v1.CryptoKey] by calling [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion]. Multiple [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] can be imported with a single [ImportJob][google.cloud.kms.v1.ImportJob]. Cloud KMS uses the private key portion of the wrapping key to unwrap the key material. Only Cloud KMS has access to the private key.

An [ImportJob][google.cloud.kms.v1.ImportJob] expires 3 days after it is created. Once expired, Cloud KMS will no longer be able to import or unwrap any key material that was wrapped with the [ImportJob][google.cloud.kms.v1.ImportJob]'s public key.

For more information, see [Importing a key](https://cloud.google.com/kms/docs/importing-a-key).

### [ImportJob.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJob.Types)

Container for nested types declared in the ImportJob message type.

### [ImportJob.Types.WrappingPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJob.Types.WrappingPublicKey)

The public key component of the wrapping key. For details of the type of key this public key corresponds to, see the [ImportMethod][google.cloud.kms.v1.ImportJob.ImportMethod].

### [ImportJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJobName)

Resource name for the `ImportJob` resource.

### [ImportTrustedKeyWrappedCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportTrustedKeyWrappedCryptoKeyVersionRequest)

Request message for [KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion].

### [KeyAccessJustificationsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyAccessJustificationsPolicy)

A [KeyAccessJustificationsPolicy][google.cloud.kms.v1.KeyAccessJustificationsPolicy] specifies zero or more allowed [AccessReason][google.cloud.kms.v1.AccessReason] values for encrypt, decrypt, and sign operations on a [CryptoKey][google.cloud.kms.v1.CryptoKey] or [KeyAccessJustificationsPolicyConfig][google.cloud.kms.v1.KeyAccessJustificationsPolicyConfig] (the default Key Access Justifications policy).

### [KeyHandle](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandle)

Resource-oriented representation of a request to Cloud KMS Autokey and the resulting provisioning of a [CryptoKey][google.cloud.kms.v1.CryptoKey].

### [KeyHandleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandleName)

Resource name for the `KeyHandle` resource.

### [KeyManagementService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementService)

Google Cloud Key Management Service

Manages cryptographic keys and operations using those keys. Implements a REST model with the following objects:

  * [KeyRing][google.cloud.kms.v1.KeyRing]
  * [CryptoKey][google.cloud.kms.v1.CryptoKey]
  * [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
  * [ImportJob][google.cloud.kms.v1.ImportJob]



If you are using manual gRPC libraries, see [Using gRPC with Cloud KMS](https://cloud.google.com/kms/docs/grpc).

### [KeyManagementService.KeyManagementServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementService.KeyManagementServiceBase)

Base class for server-side implementations of KeyManagementService

### [KeyManagementService.KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementService.KeyManagementServiceClient)

Client for KeyManagementService

### [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient)

KeyManagementService client wrapper, for convenient use.

### [KeyManagementServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClientBuilder)

Builder class for [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient) to provide simple configuration of credentials, endpoint etc.

### [KeyManagementServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClientImpl)

KeyManagementService client wrapper implementation, for convenient use.

### [KeyManagementServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceSettings)

Settings for [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient) instances.

### [KeyOperationAttestation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation)

Contains an HSM-generated attestation about a key operation. For more information, see [Verifying attestations](https://cloud.google.com/kms/docs/attest-key).

### [KeyOperationAttestation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation.Types)

Container for nested types declared in the KeyOperationAttestation message type.

### [KeyOperationAttestation.Types.CertificateChains](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation.Types.CertificateChains)

Certificate chains needed to verify the attestation. Certificates in chains are PEM-encoded and are ordered based on <https://tools.ietf.org/html/rfc5246#section-7.4.2>.

### [KeyRing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRing)

A [KeyRing][google.cloud.kms.v1.KeyRing] is a toplevel logical grouping of [CryptoKeys][google.cloud.kms.v1.CryptoKey].

### [KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName)

Resource name for the `KeyRing` resource.

### [ListCryptoKeyVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListCryptoKeyVersionsRequest)

Request message for [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].

### [ListCryptoKeyVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListCryptoKeyVersionsResponse)

Response message for [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].

### [ListCryptoKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListCryptoKeysRequest)

Request message for [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

### [ListCryptoKeysResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListCryptoKeysResponse)

Response message for [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

### [ListEkmConnectionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListEkmConnectionsRequest)

Request message for [EkmService.ListEkmConnections][google.cloud.kms.v1.EkmService.ListEkmConnections].

### [ListEkmConnectionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListEkmConnectionsResponse)

Response message for [EkmService.ListEkmConnections][google.cloud.kms.v1.EkmService.ListEkmConnections].

### [ListImportJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListImportJobsRequest)

Request message for [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].

### [ListImportJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListImportJobsResponse)

Response message for [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].

### [ListKeyHandlesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesRequest)

Request message for [Autokey.ListKeyHandles][google.cloud.kms.v1.Autokey.ListKeyHandles].

### [ListKeyHandlesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyHandlesResponse)

Response message for [Autokey.ListKeyHandles][google.cloud.kms.v1.Autokey.ListKeyHandles].

### [ListKeyRingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyRingsRequest)

Request message for [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].

### [ListKeyRingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListKeyRingsResponse)

Response message for [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].

### [ListRetiredResourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListRetiredResourcesRequest)

Request message for [KeyManagementService.ListRetiredResources][google.cloud.kms.v1.KeyManagementService.ListRetiredResources].

### [ListRetiredResourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListRetiredResourcesResponse)

Response message for [KeyManagementService.ListRetiredResources][google.cloud.kms.v1.KeyManagementService.ListRetiredResources].

### [ListSingleTenantHsmInstanceProposalsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstanceProposalsRequest)

Request message for [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals].

### [ListSingleTenantHsmInstanceProposalsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstanceProposalsResponse)

Response message for [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals].

### [ListSingleTenantHsmInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesRequest)

Request message for [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].

### [ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse)

Response message for [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].

### [LocationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.LocationMetadata)

Cloud KMS metadata for the given [google.cloud.location.Location][google.cloud.location.Location].

### [MacSignRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.MacSignRequest)

Request message for [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].

### [MacSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.MacSignResponse)

Response message for [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].

### [MacVerifyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.MacVerifyRequest)

Request message for [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].

### [MacVerifyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.MacVerifyResponse)

Response message for [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].

### [PublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey)

The public keys for a given [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. Obtained via [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].

### [PublicKey.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.Types)

Container for nested types declared in the PublicKey message type.

### [PublicKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKeyName)

Resource name for the `PublicKey` resource.

### [RawDecryptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RawDecryptRequest)

Request message for [KeyManagementService.RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt].

### [RawDecryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RawDecryptResponse)

Response message for [KeyManagementService.RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt].

### [RawEncryptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RawEncryptRequest)

Request message for [KeyManagementService.RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt].

### [RawEncryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RawEncryptResponse)

Response message for [KeyManagementService.RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt].

### [RestoreCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RestoreCryptoKeyVersionRequest)

Request message for [KeyManagementService.RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion].

### [RetiredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RetiredResource)

A RetiredResource resource represents the record of a deleted [CryptoKey][google.cloud.kms.v1.CryptoKey]. Its purpose is to provide visibility into retained user data and to prevent reuse of these names for new [CryptoKeys][google.cloud.kms.v1.CryptoKey].

### [RetiredResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RetiredResourceName)

Resource name for the `RetiredResource` resource.

### [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ServiceName)

Resource name for the `Service` resource.

### [ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigRequest)

Request message for [ShowEffectiveAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig].

### [ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ShowEffectiveAutokeyConfigResponse)

Response message for [ShowEffectiveAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.ShowEffectiveAutokeyConfig].

### [SingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance)

A [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] represents a single-tenant HSM instance. It can be used for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey] with a [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of [HSM_SINGLE_TENANT][CryptoKeyVersion.ProtectionLevel.HSM_SINGLE_TENANT], as well as performing cryptographic operations using keys created within the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

### [SingleTenantHsmInstance.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance.Types)

Container for nested types declared in the SingleTenantHsmInstance message type.

### [SingleTenantHsmInstance.Types.QuorumAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance.Types.QuorumAuth)

Configuration for M of N quorum auth.

### [SingleTenantHsmInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceName)

Resource name for the `SingleTenantHsmInstance` resource.

### [SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal)

A [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal] represents a proposal to perform an operation on a [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

### [SingleTenantHsmInstanceProposal.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types)

Container for nested types declared in the SingleTenantHsmInstanceProposal message type.

### [SingleTenantHsmInstanceProposal.Types.AddQuorumMember](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.AddQuorumMember)

Add a quorum member to the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. This will increase the [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count] by 1. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must be in the [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.DeleteSingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.DeleteSingleTenantHsmInstance)

Delete the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. Deleting a [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] will make all [CryptoKeys][google.cloud.kms.v1.CryptoKey] attached to the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] unusable. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must not be in the [DELETING][google.cloud.kms.v1.SingleTenantHsmInstance.State.DELETING] or [DELETED][google.cloud.kms.v1.SingleTenantHsmInstance.State.DELETED] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.DisableSingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.DisableSingleTenantHsmInstance)

Disable the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must be in the [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.EnableSingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.EnableSingleTenantHsmInstance)

Enable the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must be in the [DISABLED][google.cloud.kms.v1.SingleTenantHsmInstance.State.DISABLED] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.QuorumParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.QuorumParameters)

Parameters of quorum approval for the [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

### [SingleTenantHsmInstanceProposal.Types.RefreshSingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.RefreshSingleTenantHsmInstance)

Refreshes the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. This operation must be performed periodically to keep the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] active. This operation must be performed before [unrefreshed_duration_until_disable][google.cloud.kms.v1.SingleTenantHsmInstance.unrefreshed_duration_until_disable] has passed. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must be in the [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.RegisterTwoFactorAuthKeys](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.RegisterTwoFactorAuthKeys)

Register 2FA keys for the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. This operation requires all Challenges to be signed by 2FA keys. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must be in the [PENDING_TWO_FACTOR_AUTH_REGISTRATION][google.cloud.kms.v1.SingleTenantHsmInstance.State.PENDING_TWO_FACTOR_AUTH_REGISTRATION] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.RemoveQuorumMember](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.RemoveQuorumMember)

Remove a quorum member from the [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]. This will reduce [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count] by 1. The [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance] must be in the [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE] state to perform this operation.

### [SingleTenantHsmInstanceProposal.Types.RequiredActionQuorumParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.RequiredActionQuorumParameters)

Parameters for an approval that has both required challenges and a quorum.

### [SingleTenantHsmInstanceProposal.Types.UpgradeKeyTrust](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.UpgradeKeyTrust)

Promotes a key with the AES_WRAPPING purpose to a trusted wrapping key. The key must be in the [ACTIVE][CryptoKeyVersion.CryptoKeyVersionState.ACTIVE] state to perform this operation.

### [SingleTenantHsmInstanceProposalName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposalName)

Resource name for the `SingleTenantHsmInstanceProposal` resource.

### [UpdateAutokeyConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateAutokeyConfigRequest)

Request message for [UpdateAutokeyConfig][google.cloud.kms.v1.AutokeyAdmin.UpdateAutokeyConfig].

### [UpdateCryptoKeyPrimaryVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateCryptoKeyPrimaryVersionRequest)

Request message for [KeyManagementService.UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion].

### [UpdateCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateCryptoKeyRequest)

Request message for [KeyManagementService.UpdateCryptoKey][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKey].

### [UpdateCryptoKeyVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateCryptoKeyVersionRequest)

Request message for [KeyManagementService.UpdateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyVersion].

### [UpdateEkmConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateEkmConfigRequest)

Request message for [EkmService.UpdateEkmConfig][google.cloud.kms.v1.EkmService.UpdateEkmConfig].

### [UpdateEkmConnectionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.UpdateEkmConnectionRequest)

Request message for [EkmService.UpdateEkmConnection][google.cloud.kms.v1.EkmService.UpdateEkmConnection].

### [VerifyConnectivityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.VerifyConnectivityRequest)

Request message for [EkmService.VerifyConnectivity][google.cloud.kms.v1.EkmService.VerifyConnectivity].

### [VerifyConnectivityResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.VerifyConnectivityResponse)

Response message for [EkmService.VerifyConnectivity][google.cloud.kms.v1.EkmService.VerifyConnectivity].

## Enums 

### [AccessReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AccessReason)

Describes the reason for a data access. Please refer to <https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes> for the detailed semantic meaning of justification reason codes.

### [ApproveSingleTenantHsmInstanceProposalRequest.ApprovalPayloadOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ApproveSingleTenantHsmInstanceProposalRequest.ApprovalPayloadOneofCase)

Enum of possible cases for the "approval_payload" oneof.

### [AutokeyConfig.Types.KeyProjectResolutionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig.Types.KeyProjectResolutionMode)

Defines the resolution mode enum for the key project. The [KeyProjectResolutionMode][google.cloud.kms.v1.AutokeyConfig.KeyProjectResolutionMode] determines the mechanism by which [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] identifies a [key_project][google.cloud.kms.v1.AutokeyConfig.key_project] at its specific configuration node. This parameter also determines if Autokey can be used within this project or folder.

### [AutokeyConfig.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig.Types.State)

The states AutokeyConfig can be in.

### [AutokeyConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfigName.ResourceNameType)

The possible contents of [AutokeyConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfigName).

### [CryptoKey.RotationScheduleOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.RotationScheduleOneofCase)

Enum of possible cases for the "rotation_schedule" oneof.

### [CryptoKey.Types.CryptoKeyPurpose](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose)

[CryptoKeyPurpose][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose] describes the cryptographic capabilities of a [CryptoKey][google.cloud.kms.v1.CryptoKey]. A given key can only be used for the operations allowed by its purpose. For more information, see [Key purposes](https://cloud.google.com/kms/docs/algorithms#key_purposes).

### [CryptoKeyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.ResourceNameType)

The possible contents of [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName).

### [CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm)

The algorithm of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion], indicating what parameters must be used for each cryptographic operation.

The [GOOGLE_SYMMETRIC_ENCRYPTION][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.GOOGLE_SYMMETRIC_ENCRYPTION] algorithm is usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].

Algorithms beginning with `RSA_SIGN_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ASYMMETRIC_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN].

The fields in the name after `RSA_SIGN_` correspond to the following parameters: padding algorithm, modulus bit length, and digest algorithm.

For PSS, the salt length used is equal to the length of digest algorithm. For example, [RSA_SIGN_PSS_2048_SHA256][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_2048_SHA256] will use PSS with a salt length of 256 bits or 32 bytes.

Algorithms beginning with `RSA_DECRYPT_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ASYMMETRIC_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_DECRYPT].

The fields in the name after `RSA_DECRYPT_` correspond to the following parameters: padding algorithm, modulus bit length, and digest algorithm.

Algorithms beginning with `EC_SIGN_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [ASYMMETRIC_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN].

The fields in the name after `EC_SIGN_` correspond to the following parameters: elliptic curve, digest algorithm.

Algorithms beginning with `HMAC_` are usable with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] [MAC][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.MAC].

The suffix following `HMAC_` corresponds to the hash algorithm being used (eg. SHA256).

Algorithms beginning with `PQ_` are post-quantum.

For more information, see [Key purposes and algorithms](https://cloud.google.com/kms/docs/algorithms).

### [CryptoKeyVersion.Types.CryptoKeyVersionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState)

The state of a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion], indicating if it can be used.

### [CryptoKeyVersion.Types.CryptoKeyVersionView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionView)

A view for [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]s. Controls the level of detail returned for [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] in [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions] and [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

### [CryptoKeyVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.ResourceNameType)

The possible contents of [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName).

### [Digest.DigestOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Digest.DigestOneofCase)

Enum of possible cases for the "digest" oneof.

### [EkmConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConfigName.ResourceNameType)

The possible contents of [EkmConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConfigName).

### [EkmConnection.Types.KeyManagementMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types.KeyManagementMode)

[KeyManagementMode][google.cloud.kms.v1.EkmConnection.KeyManagementMode] describes who can perform control plane cryptographic operations using this [EkmConnection][google.cloud.kms.v1.EkmConnection].

### [EkmConnectionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnectionName.ResourceNameType)

The possible contents of [EkmConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnectionName).

### [ImportCryptoKeyVersionRequest.WrappedKeyMaterialOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportCryptoKeyVersionRequest.WrappedKeyMaterialOneofCase)

Enum of possible cases for the "wrapped_key_material" oneof.

### [ImportJob.Types.ImportJobState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJob.Types.ImportJobState)

The state of the [ImportJob][google.cloud.kms.v1.ImportJob], indicating if it can be used.

### [ImportJob.Types.ImportMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJob.Types.ImportMethod)

[ImportMethod][google.cloud.kms.v1.ImportJob.ImportMethod] describes the key wrapping method chosen for this [ImportJob][google.cloud.kms.v1.ImportJob].

### [ImportJobName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJobName.ResourceNameType)

The possible contents of [ImportJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ImportJobName).

### [KeyHandleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandleName.ResourceNameType)

The possible contents of [KeyHandleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyHandleName).

### [KeyOperationAttestation.Types.AttestationFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation.Types.AttestationFormat)

Attestation formats provided by the HSM.

### [KeyRingName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.ResourceNameType)

The possible contents of [KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName).

### [ProtectionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel)

[ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] specifies how cryptographic operations are performed. For more information, see [Protection levels](https://cloud.google.com/kms/docs/algorithms#protection_levels).

### [PublicKey.Types.PublicKeyFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.Types.PublicKeyFormat)

The supported [PublicKey][google.cloud.kms.v1.PublicKey] formats.

### [PublicKeyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKeyName.ResourceNameType)

The possible contents of [PublicKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKeyName).

### [RetiredResourceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RetiredResourceName.ResourceNameType)

The possible contents of [RetiredResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RetiredResourceName).

### [ServiceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ServiceName.ResourceNameType)

The possible contents of [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ServiceName).

### [SingleTenantHsmInstance.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance.Types.State)

The set of states of a [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

### [SingleTenantHsmInstanceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceName.ResourceNameType)

The possible contents of [SingleTenantHsmInstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceName).

### [SingleTenantHsmInstanceProposal.ApprovalParametersOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.ApprovalParametersOneofCase)

Enum of possible cases for the "approval_parameters" oneof.

### [SingleTenantHsmInstanceProposal.ExpirationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.ExpirationOneofCase)

Enum of possible cases for the "expiration" oneof.

### [SingleTenantHsmInstanceProposal.OperationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.OperationOneofCase)

Enum of possible cases for the "operation" oneof.

### [SingleTenantHsmInstanceProposal.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposal.Types.State)

The set of states of a [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

### [SingleTenantHsmInstanceProposalName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposalName.ResourceNameType)

The possible contents of [SingleTenantHsmInstanceProposalName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstanceProposalName).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
