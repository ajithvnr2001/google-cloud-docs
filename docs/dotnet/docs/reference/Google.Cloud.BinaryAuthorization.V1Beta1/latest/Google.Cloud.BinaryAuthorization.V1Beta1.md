---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1
title: Binary Authorization v1beta1 API - Namespace Google.Cloud.BinaryAuthorization.V1Beta1 (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:46.846915+00:00
---

# Binary Authorization v1beta1 API - Namespace Google.Cloud.BinaryAuthorization.V1Beta1 (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Namespace Google.Cloud.BinaryAuthorization.V1Beta1 (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 

## Classes 

### [AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule)

An [admission rule][google.cloud.binaryauthorization.v1beta1.AdmissionRule] specifies either that all container images used in a pod creation request must be attested to by one or more [attestors][google.cloud.binaryauthorization.v1beta1.Attestor], that all pod creations will be allowed, or that all pod creations will be denied.

Images matching an [admission allowlist pattern][google.cloud.binaryauthorization.v1beta1.AdmissionWhitelistPattern] are exempted from admission rules and will never block a pod creation.

### [AdmissionRule.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule.Types)

Container for nested types declared in the AdmissionRule message type.

### [AdmissionWhitelistPattern](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionWhitelistPattern)

An [admission allowlist pattern][google.cloud.binaryauthorization.v1beta1.AdmissionWhitelistPattern] exempts images from checks by [admission rules][google.cloud.binaryauthorization.v1beta1.AdmissionRule].

### [Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor)

An [attestor][google.cloud.binaryauthorization.v1beta1.Attestor] that attests to container image artifacts. An existing attestor cannot be modified except where indicated.

### [AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName)

Resource name for the `Attestor` resource.

### [AttestorPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey)

An [attestor public key][google.cloud.binaryauthorization.v1beta1.AttestorPublicKey] that will be used to verify attestations signed by this attestor.

### [BinauthzManagementServiceV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1)

Google Cloud Management Service for Binary Authorization admission policies and attestation authorities.

This API implements a REST model with the following objects:

  * [Policy][google.cloud.binaryauthorization.v1beta1.Policy]
  * [Attestor][google.cloud.binaryauthorization.v1beta1.Attestor]



### [BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Base](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Base)

Base class for server-side implementations of BinauthzManagementServiceV1Beta1

### [BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1.BinauthzManagementServiceV1Beta1Client)

Client for BinauthzManagementServiceV1Beta1

### [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client)

BinauthzManagementServiceV1Beta1 client wrapper, for convenient use.

### [BinauthzManagementServiceV1Beta1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1ClientBuilder)

Builder class for [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client) to provide simple configuration of credentials, endpoint etc.

### [BinauthzManagementServiceV1Beta1ClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1ClientImpl)

BinauthzManagementServiceV1Beta1 client wrapper implementation, for convenient use.

### [BinauthzManagementServiceV1Beta1Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Settings)

Settings for [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.BinauthzManagementServiceV1Beta1Client) instances.

### [ContinuousValidationEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent)

Represents an auditing event from Continuous Validation.

### [ContinuousValidationEvent.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types)

Container for nested types declared in the ContinuousValidationEvent message type.

### [ContinuousValidationEvent.Types.ConfigErrorEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ConfigErrorEvent)

An event describing a user-actionable configuration issue that prevents CV from auditing.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent)

An auditing event for one Pod.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types)

Container for nested types declared in the ContinuousValidationPodEvent message type.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails)

Container image with auditing details.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types)

Container for nested types declared in the ImageDetails message type.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult)

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types)

Container for nested types declared in the CheckResult message type.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types.CheckSetScope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types.CheckSetScope)

A scope specifier for check sets.

### [CreateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.CreateAttestorRequest)

Request message for [BinauthzManagementService.CreateAttestor][].

### [DeleteAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.DeleteAttestorRequest)

Request message for [BinauthzManagementService.DeleteAttestor][].

### [GetAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetAttestorRequest)

Request message for [BinauthzManagementService.GetAttestor][].

### [GetPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetPolicyRequest)

Request message for [BinauthzManagementService.GetPolicy][].

### [GetSystemPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.GetSystemPolicyRequest)

Request to read the current system policy.

### [ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsRequest)

Request message for [BinauthzManagementService.ListAttestors][].

### [ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ListAttestorsResponse)

Response message for [BinauthzManagementService.ListAttestors][].

### [PkixPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PkixPublicKey)

A public key in the PkixPublicKey format (see <https://tools.ietf.org/html/rfc5280#section-4.1.2.7> for details). Public keys of this type are typically textually encoded using the PEM format.

### [PkixPublicKey.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PkixPublicKey.Types)

Container for nested types declared in the PkixPublicKey message type.

### [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] for Binary Authorization.

### [Policy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy.Types)

Container for nested types declared in the Policy message type.

### [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName)

Resource name for the `Policy` resource.

### [SystemPolicyV1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1)

API for working with the system policy.

### [SystemPolicyV1Beta1.SystemPolicyV1Beta1Base](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1.SystemPolicyV1Beta1Base)

Base class for server-side implementations of SystemPolicyV1Beta1

### [SystemPolicyV1Beta1.SystemPolicyV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1.SystemPolicyV1Beta1Client)

Client for SystemPolicyV1Beta1

### [SystemPolicyV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1Client)

SystemPolicyV1Beta1 client wrapper, for convenient use.

### [SystemPolicyV1Beta1ClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1ClientBuilder)

Builder class for [SystemPolicyV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1Client) to provide simple configuration of credentials, endpoint etc.

### [SystemPolicyV1Beta1ClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1ClientImpl)

SystemPolicyV1Beta1 client wrapper implementation, for convenient use.

### [SystemPolicyV1Beta1Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1Settings)

Settings for [SystemPolicyV1Beta1Client](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.SystemPolicyV1Beta1Client) instances.

### [UpdateAttestorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdateAttestorRequest)

Request message for [BinauthzManagementService.UpdateAttestor][].

### [UpdatePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UpdatePolicyRequest)

Request message for [BinauthzManagementService.UpdatePolicy][].

### [UserOwnedDrydockNote](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.UserOwnedDrydockNote)

An [user owned drydock note][google.cloud.binaryauthorization.v1beta1.UserOwnedDrydockNote] references a Drydock ATTESTATION_AUTHORITY Note created by the user.

## Enums 

### [AdmissionRule.Types.EnforcementMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule.Types.EnforcementMode)

TODO(wietse) re-word this text to 'per-image' instead of 'per-pod' and to allow for three-way evaluation (allow, deny, delegate). Defines the possible actions when a pod creation is denied by an admission rule.

### [AdmissionRule.Types.EvaluationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule.Types.EvaluationMode)

### [Attestor.AttestorTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Attestor.AttestorTypeOneofCase)

Enum of possible cases for the "attestor_type" oneof.

### [AttestorName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName.ResourceNameType)

The possible contents of [AttestorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorName).

### [AttestorPublicKey.PublicKeyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AttestorPublicKey.PublicKeyOneofCase)

Enum of possible cases for the "public_key" oneof.

### [ContinuousValidationEvent.EventTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.EventTypeOneofCase)

Enum of possible cases for the "event_type" oneof.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.AuditResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.AuditResult)

Result of the audit.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types.CheckSetScope.ScopeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types.CheckSetScope.ScopeOneofCase)

Enum of possible cases for the "scope" oneof.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types.CheckVerdict](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.CheckResult.Types.CheckVerdict)

Result of evaluating one check.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.ContainerType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.ImageDetails.Types.ContainerType)

The container type.

### [ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.PolicyConformanceVerdict](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.ContinuousValidationEvent.Types.ContinuousValidationPodEvent.Types.PolicyConformanceVerdict)

Audit time policy conformance verdict.

### [PkixPublicKey.Types.SignatureAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PkixPublicKey.Types.SignatureAlgorithm)

Represents a signature algorithm and other information necessary to verify signatures with a given public key. This is based primarily on the public key types supported by Tink's PemKeyType, which is in turn based on KMS's supported signing algorithms. See <https://cloud.google.com/kms/docs/algorithms>. In the future, BinAuthz might support additional public key types independently of Tink and/or KMS.

### [Policy.Types.GlobalPolicyEvaluationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy.Types.GlobalPolicyEvaluationMode)

### [PolicyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName.ResourceNameType)

The possible contents of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
