---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1
title: Binary Authorization v1 API - Namespace Google.Cloud.BinaryAuthorization.V1 (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:42.299944+00:00
---

# Binary Authorization v1 API - Namespace Google.Cloud.BinaryAuthorization.V1 (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1 API - Namespace Google.Cloud.BinaryAuthorization.V1 (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.0 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 

## Classes 

### [AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AdmissionRule)

An [admission rule][google.cloud.binaryauthorization.v1.AdmissionRule] specifies either that all container images used in a pod creation request must be attested to by one or more [attestors][google.cloud.binaryauthorization.v1.Attestor], that all pod creations will be allowed, or that all pod creations will be denied.

Images matching an [admission allowlist pattern][google.cloud.binaryauthorization.v1.AdmissionWhitelistPattern] are exempted from admission rules and will never block a pod creation.

### [AdmissionRule.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AdmissionRule.Types)

Container for nested types declared in the AdmissionRule message type.

### [AdmissionWhitelistPattern](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AdmissionWhitelistPattern)

An [admission allowlist pattern][google.cloud.binaryauthorization.v1.AdmissionWhitelistPattern] exempts images from checks by [admission rules][google.cloud.binaryauthorization.v1.AdmissionRule].

### [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor)

An [attestor][google.cloud.binaryauthorization.v1.Attestor] that attests to container image artifacts. An existing attestor cannot be modified except where indicated.

### [AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AttestorName)

Resource name for the `Attestor` resource.

### [AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AttestorPublicKey)

An [attestor public key][google.cloud.binaryauthorization.v1.AttestorPublicKey] that will be used to verify attestations signed by this attestor.

### [BinauthzManagementServiceV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1)

Google Cloud Management Service for Binary Authorization admission policies and attestation authorities.

This API implements a REST model with the following objects:

  * [Policy][google.cloud.binaryauthorization.v1.Policy]
  * [Attestor][google.cloud.binaryauthorization.v1.Attestor]



### [BinauthzManagementServiceV1.BinauthzManagementServiceV1Base](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1.BinauthzManagementServiceV1Base)

Base class for server-side implementations of BinauthzManagementServiceV1

### [BinauthzManagementServiceV1.BinauthzManagementServiceV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1.BinauthzManagementServiceV1Client)

Client for BinauthzManagementServiceV1

### [BinauthzManagementServiceV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1Client)

BinauthzManagementServiceV1 client wrapper, for convenient use.

### [BinauthzManagementServiceV1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1ClientBuilder)

Builder class for [BinauthzManagementServiceV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1Client) to provide simple configuration of credentials, endpoint etc.

### [BinauthzManagementServiceV1ClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1ClientImpl)

BinauthzManagementServiceV1 client wrapper implementation, for convenient use.

### [BinauthzManagementServiceV1Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1Settings)

Settings for [BinauthzManagementServiceV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.BinauthzManagementServiceV1Client) instances.

### [CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.CreateAttestorRequest)

Request message for [BinauthzManagementServiceV1.CreateAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestor].

### [DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.DeleteAttestorRequest)

Request message for [BinauthzManagementServiceV1.DeleteAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestor].

### [GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.GetAttestorRequest)

Request message for [BinauthzManagementServiceV1.GetAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestor].

### [GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.GetPolicyRequest)

Request message for [BinauthzManagementServiceV1.GetPolicy][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicy].

### [GetSystemPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.GetSystemPolicyRequest)

Request to read the current system policy.

### [ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest)

Request message for [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

### [ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse)

Response message for [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

### [PkixPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.PkixPublicKey)

A public key in the PkixPublicKey [format](https://tools.ietf.org/html/rfc5280#section-4.1.2.7). Public keys of this type are typically textually encoded using the PEM format.

### [PkixPublicKey.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.PkixPublicKey.Types)

Container for nested types declared in the PkixPublicKey message type.

### [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Policy)

A [policy][google.cloud.binaryauthorization.v1.Policy] for container image binary authorization.

### [Policy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Policy.Types)

Container for nested types declared in the Policy message type.

### [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.PolicyName)

Resource name for the `Policy` resource.

### [SystemPolicyV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1)

API for working with the system policy.

### [SystemPolicyV1.SystemPolicyV1Base](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1.SystemPolicyV1Base)

Base class for server-side implementations of SystemPolicyV1

### [SystemPolicyV1.SystemPolicyV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1.SystemPolicyV1Client)

Client for SystemPolicyV1

### [SystemPolicyV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1Client)

SystemPolicyV1 client wrapper, for convenient use.

### [SystemPolicyV1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1ClientBuilder)

Builder class for [SystemPolicyV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1Client) to provide simple configuration of credentials, endpoint etc.

### [SystemPolicyV1ClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1ClientImpl)

SystemPolicyV1 client wrapper implementation, for convenient use.

### [SystemPolicyV1Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1Settings)

Settings for [SystemPolicyV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.SystemPolicyV1Client) instances.

### [UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.UpdateAttestorRequest)

Request message for [BinauthzManagementServiceV1.UpdateAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestor].

### [UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.UpdatePolicyRequest)

Request message for [BinauthzManagementServiceV1.UpdatePolicy][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicy].

### [UserOwnedGrafeasNote](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.UserOwnedGrafeasNote)

An [user owned Grafeas note][google.cloud.binaryauthorization.v1.UserOwnedGrafeasNote] references a Grafeas Attestation.Authority Note created by the user.

### [ValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceRequest)

Request message for [ValidationHelperV1.ValidateAttestationOccurrence][google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence].

### [ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceResponse)

Response message for [ValidationHelperV1.ValidateAttestationOccurrence][google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence].

### [ValidateAttestationOccurrenceResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceResponse.Types)

Container for nested types declared in the ValidateAttestationOccurrenceResponse message type.

### [ValidationHelperV1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1)

BinAuthz Attestor verification

### [ValidationHelperV1.ValidationHelperV1Base](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1.ValidationHelperV1Base)

Base class for server-side implementations of ValidationHelperV1

### [ValidationHelperV1.ValidationHelperV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1.ValidationHelperV1Client)

Client for ValidationHelperV1

### [ValidationHelperV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1Client)

ValidationHelperV1 client wrapper, for convenient use.

### [ValidationHelperV1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1ClientBuilder)

Builder class for [ValidationHelperV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1Client) to provide simple configuration of credentials, endpoint etc.

### [ValidationHelperV1ClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1ClientImpl)

ValidationHelperV1 client wrapper implementation, for convenient use.

### [ValidationHelperV1Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1Settings)

Settings for [ValidationHelperV1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidationHelperV1Client) instances.

## Enums 

### [AdmissionRule.Types.EnforcementMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AdmissionRule.Types.EnforcementMode)

Defines the possible actions when a pod creation is denied by an admission rule.

### [AdmissionRule.Types.EvaluationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AdmissionRule.Types.EvaluationMode)

### [Attestor.AttestorTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor.AttestorTypeOneofCase)

Enum of possible cases for the "attestor_type" oneof.

### [AttestorName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AttestorName.ResourceNameType)

The possible contents of [AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AttestorName).

### [AttestorPublicKey.PublicKeyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.AttestorPublicKey.PublicKeyOneofCase)

Enum of possible cases for the "public_key" oneof.

### [PkixPublicKey.Types.SignatureAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.PkixPublicKey.Types.SignatureAlgorithm)

Represents a signature algorithm and other information necessary to verify signatures with a given public key. This is based primarily on the public key types supported by Tink's PemKeyType, which is in turn based on KMS's supported signing [algorithms](https://cloud.google.com/kms/docs/algorithms). In the future, Binary Authorization might support additional public key types independently of Tink and/or KMS.

### [Policy.Types.GlobalPolicyEvaluationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Policy.Types.GlobalPolicyEvaluationMode)

### [PolicyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.PolicyName.ResourceNameType)

The possible contents of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.PolicyName).

### [ValidateAttestationOccurrenceResponse.Types.Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ValidateAttestationOccurrenceResponse.Types.Result)

The enum returned in the `result` field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
