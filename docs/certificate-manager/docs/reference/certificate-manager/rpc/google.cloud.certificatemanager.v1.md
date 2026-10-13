---
url: https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1
title: Package google.cloud.certificatemanager.v1 \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:42.133412+00:00
---

# Package google.cloud.certificatemanager.v1  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/certificate-manager/docs/apis)



Send feedback 

#  Package google.cloud.certificatemanager.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[CertificateManager](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateManager)` (interface)
  * `[Certificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate)` (message)
  * `[Certificate.ManagedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate)` (message)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo)` (message)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason)` (enum)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo.State](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.State)` (enum)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting)` (message)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.CNAME](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.CNAME)` (message)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.IPs](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.IPs)` (message)
  * `[Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.Issue](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.Issue)` (enum)
  * `[Certificate.ManagedCertificate.ProvisioningIssue](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue)` (message)
  * `[Certificate.ManagedCertificate.ProvisioningIssue.Reason](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue.Reason)` (enum)
  * `[Certificate.ManagedCertificate.State](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State)` (enum)
  * `[Certificate.ManagedIdentityCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedIdentityCertificate)` (message)
  * `[Certificate.Scope](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.Scope)` (enum)
  * `[Certificate.SelfManagedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.SelfManagedCertificate)` (message)
  * `[Certificate.UsedBy](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.UsedBy)` (message)
  * `[CertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig)` (message)
  * `[CertificateIssuanceConfig.CertificateAuthorityConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig.CertificateAuthorityConfig)` (message)
  * `[CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig)` (message)
  * `[CertificateIssuanceConfig.KeyAlgorithm](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig.KeyAlgorithm)` (enum)
  * `[CertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap)` (message)
  * `[CertificateMap.GclbTarget](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap.GclbTarget)` (message)
  * `[CertificateMap.GclbTarget.IpConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig)` (message)
  * `[CertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry)` (message)
  * `[CertificateMapEntry.Matcher](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry.Matcher)` (enum)
  * `[CreateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateIssuanceConfigRequest)` (message)
  * `[CreateCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateMapEntryRequest)` (message)
  * `[CreateCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateMapRequest)` (message)
  * `[CreateCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateRequest)` (message)
  * `[CreateDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateDnsAuthorizationRequest)` (message)
  * `[CreateTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateTrustConfigRequest)` (message)
  * `[DeleteCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateIssuanceConfigRequest)` (message)
  * `[DeleteCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateMapEntryRequest)` (message)
  * `[DeleteCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateMapRequest)` (message)
  * `[DeleteCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateRequest)` (message)
  * `[DeleteDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteDnsAuthorizationRequest)` (message)
  * `[DeleteTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteTrustConfigRequest)` (message)
  * `[DnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization)` (message)
  * `[DnsAuthorization.DnsResourceRecord](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization.DnsResourceRecord)` (message)
  * `[DnsAuthorization.Type](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization.Type)` (enum)
  * `[GetCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateIssuanceConfigRequest)` (message)
  * `[GetCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateMapEntryRequest)` (message)
  * `[GetCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateMapRequest)` (message)
  * `[GetCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateRequest)` (message)
  * `[GetDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetDnsAuthorizationRequest)` (message)
  * `[GetTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetTrustConfigRequest)` (message)
  * `[ListCertificateIssuanceConfigsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsRequest)` (message)
  * `[ListCertificateIssuanceConfigsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsResponse)` (message)
  * `[ListCertificateMapEntriesRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapEntriesRequest)` (message)
  * `[ListCertificateMapEntriesResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapEntriesResponse)` (message)
  * `[ListCertificateMapsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapsRequest)` (message)
  * `[ListCertificateMapsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapsResponse)` (message)
  * `[ListCertificatesRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificatesRequest)` (message)
  * `[ListCertificatesResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificatesResponse)` (message)
  * `[ListDnsAuthorizationsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListDnsAuthorizationsRequest)` (message)
  * `[ListDnsAuthorizationsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListDnsAuthorizationsResponse)` (message)
  * `[ListTrustConfigsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListTrustConfigsRequest)` (message)
  * `[ListTrustConfigsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListTrustConfigsResponse)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.OperationMetadata)` (message)
  * `[ServingState](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ServingState)` (enum)
  * `[TrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig)` (message)
  * `[TrustConfig.AllowlistedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.AllowlistedCertificate)` (message)
  * `[TrustConfig.IntermediateCA](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA)` (message)
  * `[TrustConfig.TrustAnchor](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor)` (message)
  * `[TrustConfig.TrustStore](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.TrustStore)` (message)
  * `[UpdateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateIssuanceConfigRequest)` (message)
  * `[UpdateCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateMapEntryRequest)` (message)
  * `[UpdateCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateMapRequest)` (message)
  * `[UpdateCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateRequest)` (message)
  * `[UpdateDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateDnsAuthorizationRequest)` (message)
  * `[UpdateTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateTrustConfigRequest)` (message)



## CertificateManager

API Overview

Certificates Manager API allows customers to see and manage all their TLS certificates.

Certificates Manager API service provides methods to manage certificates, group them into collections, and create serving configuration that can be easily applied to other Cloud resources e.g. Target Proxies.

Data Model

The Certificates Manager service exposes the following resources:

  * `Certificate` that describes a single TLS certificate.
  * `CertificateMap` that describes a collection of certificates that can be attached to a target resource.
  * `CertificateMapEntry` that describes a single configuration entry that consists of a SNI and a group of certificates. It's a subresource of CertificateMap.



Certificate, CertificateMap and CertificateMapEntry IDs have to fully match the regexp `[a-z0-9-]{1,63}`. In other words, - only lower case letters, digits, and hyphen are allowed - length of the resource ID has to be in [1,63] range.

Provides methods to manage Cloud Certificate Manager entities.

CreateCertificate  
---  
` rpc CreateCertificate(`[CreateCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new Certificate in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateCertificateIssuanceConfig  
---  
` rpc CreateCertificateIssuanceConfig(`[CreateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateIssuanceConfigRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new CertificateIssuanceConfig in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateCertificateMap  
---  
` rpc CreateCertificateMap(`[CreateCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateMapRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new CertificateMap in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateCertificateMapEntry  
---  
` rpc CreateCertificateMapEntry(`[CreateCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateCertificateMapEntryRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new CertificateMapEntry in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateDnsAuthorization  
---  
` rpc CreateDnsAuthorization(`[CreateDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateDnsAuthorizationRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new DnsAuthorization in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateTrustConfig  
---  
` rpc CreateTrustConfig(`[CreateTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CreateTrustConfigRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new TrustConfig in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteCertificate  
---  
` rpc DeleteCertificate(`[DeleteCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single Certificate.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteCertificateIssuanceConfig  
---  
` rpc DeleteCertificateIssuanceConfig(`[DeleteCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateIssuanceConfigRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single CertificateIssuanceConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteCertificateMap  
---  
` rpc DeleteCertificateMap(`[DeleteCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateMapRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteCertificateMapEntry  
---  
` rpc DeleteCertificateMapEntry(`[DeleteCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteCertificateMapEntryRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single CertificateMapEntry.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteDnsAuthorization  
---  
` rpc DeleteDnsAuthorization(`[DeleteDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteDnsAuthorizationRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single DnsAuthorization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteTrustConfig  
---  
` rpc DeleteTrustConfig(`[DeleteTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DeleteTrustConfigRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a single TrustConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetCertificate  
---  
` rpc GetCertificate(`[GetCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateRequest)`) returns (`[Certificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate)`) ` Gets details of a single Certificate.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetCertificateIssuanceConfig  
---  
` rpc GetCertificateIssuanceConfig(`[GetCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateIssuanceConfigRequest)`) returns (`[CertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig)`) ` Gets details of a single CertificateIssuanceConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetCertificateMap  
---  
` rpc GetCertificateMap(`[GetCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateMapRequest)`) returns (`[CertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap)`) ` Gets details of a single CertificateMap.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetCertificateMapEntry  
---  
` rpc GetCertificateMapEntry(`[GetCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetCertificateMapEntryRequest)`) returns (`[CertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry)`) ` Gets details of a single CertificateMapEntry.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDnsAuthorization  
---  
` rpc GetDnsAuthorization(`[GetDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetDnsAuthorizationRequest)`) returns (`[DnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization)`) ` Gets details of a single DnsAuthorization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetTrustConfig  
---  
` rpc GetTrustConfig(`[GetTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.GetTrustConfigRequest)`) returns (`[TrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig)`) ` Gets details of a single TrustConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListCertificateIssuanceConfigs  
---  
` rpc ListCertificateIssuanceConfigs(`[ListCertificateIssuanceConfigsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsRequest)`) returns (`[ListCertificateIssuanceConfigsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateIssuanceConfigsResponse)`) ` Lists CertificateIssuanceConfigs in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListCertificateMapEntries  
---  
` rpc ListCertificateMapEntries(`[ListCertificateMapEntriesRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapEntriesRequest)`) returns (`[ListCertificateMapEntriesResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapEntriesResponse)`) ` Lists CertificateMapEntries in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListCertificateMaps  
---  
` rpc ListCertificateMaps(`[ListCertificateMapsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapsRequest)`) returns (`[ListCertificateMapsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificateMapsResponse)`) ` Lists CertificateMaps in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListCertificates  
---  
` rpc ListCertificates(`[ListCertificatesRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificatesRequest)`) returns (`[ListCertificatesResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListCertificatesResponse)`) ` Lists Certificates in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDnsAuthorizations  
---  
` rpc ListDnsAuthorizations(`[ListDnsAuthorizationsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListDnsAuthorizationsRequest)`) returns (`[ListDnsAuthorizationsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListDnsAuthorizationsResponse)`) ` Lists DnsAuthorizations in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListTrustConfigs  
---  
` rpc ListTrustConfigs(`[ListTrustConfigsRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListTrustConfigsRequest)`) returns (`[ListTrustConfigsResponse](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ListTrustConfigsResponse)`) ` Lists TrustConfigs in a given project and location.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateCertificate  
---  
` rpc UpdateCertificate(`[UpdateCertificateRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a Certificate.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateCertificateIssuanceConfig  
---  
` rpc UpdateCertificateIssuanceConfig(`[UpdateCertificateIssuanceConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateIssuanceConfigRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a CertificateIssuanceConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateCertificateMap  
---  
` rpc UpdateCertificateMap(`[UpdateCertificateMapRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateMapRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a CertificateMap.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateCertificateMapEntry  
---  
` rpc UpdateCertificateMapEntry(`[UpdateCertificateMapEntryRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateCertificateMapEntryRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a CertificateMapEntry.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDnsAuthorization  
---  
` rpc UpdateDnsAuthorization(`[UpdateDnsAuthorizationRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateDnsAuthorizationRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a DnsAuthorization.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateTrustConfig  
---  
` rpc UpdateTrustConfig(`[UpdateTrustConfigRequest](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.UpdateTrustConfigRequest)`) returns (`[Operation](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a TrustConfig.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Certificate

Defines TLS certificate.

Fields  
---  
`name` |  `string` Identifier. A user-defined name of the certificate. Certificate names must be unique globally and match pattern `projects/*/locations/*/certificates/*`.  
`description` |  `string` Optional. One or more paragraphs of text description of a certificate.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a Certificate.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a Certificate.  
`labels` |  `map<string, string>` Optional. Set of labels associated with a Certificate.  
`san_dnsnames[]` |  `string` Output only. The list of Subject Alternative Names of dnsName type defined in the certificate (see RFC 5280 4.2.1.6). Managed certificates that haven't been provisioned yet have this field populated with a value of the managed.domains field.  
`pem_certificate` |  `string` Output only. The PEM-encoded certificate chain.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The expiry timestamp of a Certificate.  
`scope` |  `[Scope](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.Scope)` Optional. Immutable. The scope of the certificate.  
`used_by[]` |  `[UsedBy](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.UsedBy)` Output only. The list of resources that use this Certificate.  
`tags` |  `map<string, string>` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"  
Union field `type`. Type of the certificate. Required. `type` can be only one of the following:  
`self_managed` |  `[SelfManagedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.SelfManagedCertificate)` If set, defines data of a self-managed certificate.  
`managed` |  `[ManagedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate)` If set, contains configuration and state of a managed certificate.  
`managed_identity` |  `[ManagedIdentityCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedIdentityCertificate)` If set, contains configuration and state of a managed identity certificate.  
  
## ManagedCertificate

Configuration and state of a Managed Certificate. Certificate Manager provisions and renews Managed Certificates automatically, for as long as it's authorized to do so.

Fields  
---  
`domains[]` |  `string` Optional. Immutable. The domains for which a managed SSL certificate will be generated. Wildcard domains are only supported with DNS challenge resolution.  
`dns_authorizations[]` |  `string` Optional. Immutable. Authorizations that will be used for performing domain authorization. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `dnsAuthorizations`:

  * `certificatemanager.dnsauthorizations.use`

  
`issuance_config` |  `string` Optional. Immutable. The resource name for a `[CertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig)` used to configure private PKI certificates in the format `projects/*/locations/*/certificateIssuanceConfigs/*`. If this field is not set, the certificates will instead be publicly signed as documented at <https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#caa>. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `issuanceConfig`:

  * `certificatemanager.certissuanceconfigs.use`

  
`state` |  `[State](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State)` Output only. State of the managed certificate resource.  
`provisioning_issue` |  `[ProvisioningIssue](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue)` Output only. Information about issues with provisioning a Managed Certificate.  
`authorization_attempt_info[]` |  `[AuthorizationAttemptInfo](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo)` Output only. Detailed state of the latest authorization attempt for each domain specified for managed certificate resource.  
  
## AuthorizationAttemptInfo

State of the latest attempt to authorize a domain for certificate issuance.

Fields  
---  
`domain` |  `string` Output only. Domain name of the authorization attempt.  
`state` |  `[State](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.State)` Output only. State of the domain for managed certificate issuance.  
`failure_reason` |  `[FailureReason](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.FailureReason)` Output only. Reason for failure of the authorization attempt for the domain.  
`details` |  `string` Output only. Human readable explanation for reaching the state. Provided to help address the configuration issues. Not guaranteed to be stable. For programmatic access use FailureReason enum.  
`attempt_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp, when the authorization attempt was made.  
`troubleshooting` |  `[Troubleshooting](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting)` Output only. Troubleshooting information for the authorization attempt. This field is only populated if the authorization attempt failed.  
  
## FailureReason

Reason for failure of the authorization attempt for the domain.

Enums  
---  
`FAILURE_REASON_UNSPECIFIED` | FailureReason is unspecified.  
`CONFIG` | There was a problem with the user's DNS or load balancer configuration for this domain.  
`CAA` | Certificate issuance forbidden by an explicit CAA record for the domain or a failure to check CAA records for the domain.  
`RATE_LIMITED` | Reached a CA or internal rate-limit for the domain, e.g. for certificates per top-level private domain.  
  
## State

State of the domain for managed certificate issuance.

Enums  
---  
`STATE_UNSPECIFIED` | State is unspecified.  
`AUTHORIZING` | Certificate provisioning for this domain is under way. Google Cloud will attempt to authorize the domain.  
`AUTHORIZED` | A managed certificate can be provisioned, no issues for this domain.  
`FAILED` | Attempt to authorize the domain failed. This prevents the Managed Certificate from being issued. See `failure_reason` and `details` fields for more information.  
  
## Troubleshooting

Troubleshooting information for the authorization attempt.

Fields  
---  
`issues[]` |  `[Issue](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.Issue)` Output only. The list of issues discovered during the authorization attempt.  
`cname` |  `[CNAME](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.CNAME)` Output only. CNAME troubleshooting information.  
`ips` |  `[IPs](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.AuthorizationAttemptInfo.Troubleshooting.IPs)` Output only. IPs troubleshooting information.  
  
## CNAME

CNAME troubleshooting information.

Fields  
---  
`name` |  `string` Output only. The name of the CNAME record for the domain, equals to `dns_resource_record.name` in the corresponding `DnsAuthorization`.  
`expected_data` |  `string` Output only. The expected value of the CNAME record for the domain, equals to `dns_resource_record.data` in the corresponding `DnsAuthorization`.  
`resolved_data[]` |  `string` Output only. The resolved CNAME chain. Empty list if the CNAME record for `CNAME.name` is not found. Otherwise the first item is the value of the CNAME record for `CNAME.name`. If the CNAME chain is longer, the second item is the value of the CNAME record for the first item, and so on.  
  
## IPs

IPs troubleshooting information.

Fields  
---  
`serving[]` |  `string` Output only. The list of IP addresses, where the certificate is attached and port 443 is open.  
`serving_on_alt_ports[]` |  `string` Output only. The list of IP addresses, where the certificate is attached, but port 443 is not open.  
`resolved[]` |  `string` Output only. The list of IP addresses resolved from the domain's A/AAAA records. Can contain both ipv4 and ipv6 addresses.  
  
## Issue

The issue discovered during the authorization attempt.

Enums  
---  
`ISSUE_UNSPECIFIED` | Issue is unspecified.  
`CNAME_MISMATCH` | The resolved CNAME value doesn't match the expected CNAME.  
`RESOLVED_TO_NOT_SERVING` | Domain has A/AAAA records that point to IPs, where the certificate is not attached.  
`RESOLVED_TO_SERVING_ON_ALT_PORTS` | Domain has A/AAAA records that point to IPs, where the certificate is attached, but port 443 is not open.  
`NO_RESOLVED_IPS` | Domain doesn't have any A/AAAA records.  
`CERTIFICATE_NOT_ATTACHED` | Certificate is not configured to be served from any IPs (e.g. Certificate is not attached to any load balancer).  
  
## ProvisioningIssue

Information about issues with provisioning a Managed Certificate.

Fields  
---  
`reason` |  `[Reason](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue.Reason)` Output only. Reason for provisioning failures.  
`details` |  `string` Output only. Human readable explanation about the issue. Provided to help address the configuration issues. Not guaranteed to be stable. For programmatic access use Reason enum.  
  
## Reason

Reason for provisioning failures.

Enums  
---  
`REASON_UNSPECIFIED` | Reason is unspecified.  
`AUTHORIZATION_ISSUE` | Certificate provisioning failed due to an issue with one or more of the domains on the certificate. For details of which domains failed, consult the `authorization_attempt_info` field.  
`RATE_LIMITED` | Exceeded Certificate Authority quotas or internal rate limits of the system. Provisioning may take longer to complete.  
  
## State

State of the managed certificate resource.

Enums  
---  
`STATE_UNSPECIFIED` | State is unspecified.  
`PROVISIONING` | Certificate Manager attempts to provision or renew the certificate. If the process takes longer than expected, consult the `provisioning_issue` field.  
`FAILED` | Multiple certificate provisioning attempts failed and Certificate Manager gave up. To try again, delete and create a new managed Certificate resource. For details see the `provisioning_issue` field.  
`ACTIVE` | The certificate management is working, and a certificate has been provisioned.  
  
## ManagedIdentityCertificate

Configuration and state of a Managed Identity Certificate. Certificate Manager provisions and renews Managed Identity Certificates automatically, for as long as it's authorized to do so.

Fields  
---  
`identity` |  `string` Required. Immutable. SPIFFE ID of the Managed Identity used for this certificate.  
`state` |  `[State](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.State)` Output only. State of the managed certificate resource.  
`provisioning_issue` |  `[ProvisioningIssue](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate.ManagedCertificate.ProvisioningIssue)` Output only. Information about issues with provisioning a managed certificate.  
  
## Scope

Certificate scope.

Enums  
---  
`DEFAULT` | Use the DEFAULT scope if you plan to use the certificate with global external Application Load Balancer, global external proxy Network Load Balancer, or any of the regional Google Cloud services.  
`EDGE_CACHE` | Use the EDGE_CACHE scope if you plan to use the certificate with Media CDN. The certificates are served from Edge Points of Presence. See <https://cloud.google.com/vpc/docs/edge-locations>.  
`ALL_REGIONS` | Use the ALL_REGIONS scope if you plan to use the certificate with cross-region internal Application Load Balancer. The certificates are served from all Google Cloud regions. See <https://cloud.google.com/compute/docs/regions-zones>.  
`CLIENT_AUTH` | Associated with certificates used as client certificates in Backend mTLS.  
  
## SelfManagedCertificate

Certificate data for a SelfManaged Certificate. SelfManaged Certificates are uploaded by the user. Updating such certificates before they expire remains the user's responsibility.

Fields  
---  
`pem_certificate` |  `string` Optional. Input only. The PEM-encoded certificate chain. Leaf certificate comes first, followed by intermediate ones if any.  
`pem_private_key` |  `string` Optional. Input only. The PEM-encoded private key of the leaf certificate.  
  
## UsedBy

Defines a resource that uses the certificate.

Fields  
---  
`name` |  `string` Output only. Full name of the resource <https://google.aip.dev/122#full-resource-names>, e.g. `//certificatemanager.googleapis.com/projects/*/locations/*/certificateMaps/*/certificateMapEntries/*` or `//compute.googleapis.com/projects/*/locations/*/targetHttpsProxies/*`.  
  
## CertificateIssuanceConfig

CertificateIssuanceConfig specifies how to issue and manage a certificate.

Fields  
---  
`name` |  `string` Identifier. A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern `projects/*/locations/*/certificateIssuanceConfigs/*`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a CertificateIssuanceConfig.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a CertificateIssuanceConfig.  
`labels` |  `map<string, string>` Optional. Set of labels associated with a CertificateIssuanceConfig.  
`description` |  `string` Optional. One or more paragraphs of text description of a CertificateIssuanceConfig.  
`certificate_authority_config` |  `[CertificateAuthorityConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig.CertificateAuthorityConfig)` Required. The CA that issues the workload certificate. It includes the CA address, type, authentication to CA service, etc.  
`lifetime` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Required. Workload certificate lifetime requested.  
`rotation_window_percentage` |  `int32` Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive.  
`key_algorithm` |  `[KeyAlgorithm](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig.KeyAlgorithm)` Required. The key algorithm to use when generating the private key.  
`tags` |  `map<string, string>` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"  
  
## CertificateAuthorityConfig

The CA that issues the workload certificate. It includes CA address, type, authentication to CA service, etc.

Fields  
---  
Union field `kind`. The kind of CA config. `kind` can be only one of the following:  
`certificate_authority_service_config` |  `[CertificateAuthorityServiceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig.CertificateAuthorityConfig.CertificateAuthorityServiceConfig)` Defines a CertificateAuthorityServiceConfig.  
  
## CertificateAuthorityServiceConfig

Contains information required to contact CA service.

Fields  
---  
`ca_pool` |  `string` Required. A CA pool resource used to issue a certificate. The CA pool string has a relative resource path following the form "projects/{project}/locations/{location}/caPools/{ca_pool}". Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `caPool`:

  * `privateca.caPools.use`

  
  
## KeyAlgorithm

The type of keypair to generate.

Enums  
---  
`KEY_ALGORITHM_UNSPECIFIED` | Unspecified key algorithm.  
`RSA_2048` | Specifies RSA with a 2048-bit modulus.  
`ECDSA_P256` | Specifies ECDSA with curve P256.  
  
## CertificateMap

Defines a collection of certificate configurations.

Fields  
---  
`name` |  `string` Identifier. A user-defined name of the Certificate Map. Certificate Map names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*`.  
`description` |  `string` Optional. One or more paragraphs of text description of a certificate map.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a Certificate Map.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The update timestamp of a Certificate Map.  
`labels` |  `map<string, string>` Optional. Set of labels associated with a Certificate Map.  
`gclb_targets[]` |  `[GclbTarget](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap.GclbTarget)` Output only. A list of GCLB targets that use this Certificate Map. A Target Proxy is only present on this list if it's attached to a Forwarding Rule.  
`tags` |  `map<string, string>` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"  
  
## GclbTarget

Describes a Target Proxy that uses this Certificate Map.

Fields  
---  
`ip_configs[]` |  `[IpConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap.GclbTarget.IpConfig)` Output only. IP configurations for this Target Proxy where the Certificate Map is serving.  
Union field `target_proxy`. A Target Proxy to which this map is attached to. `target_proxy` can be only one of the following:  
`target_https_proxy` |  `string` Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetHttpsProxies/*`.  
`target_ssl_proxy` |  `string` Output only. This field returns the resource name in the following format: `//compute.googleapis.com/projects/*/global/targetSslProxies/*`.  
  
## IpConfig

Defines IP configuration where this Certificate Map is serving.

Fields  
---  
`ip_address` |  `string` Output only. An external IP address.  
`ports[]` |  `uint32` Output only. Ports.  
  
## CertificateMapEntry

Defines a certificate map entry.

Fields  
---  
`name` |  `string` Identifier. A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*/certificateMapEntries/*`.  
`description` |  `string` Optional. One or more paragraphs of text description of a certificate map entry.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a Certificate Map Entry.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The update timestamp of a Certificate Map Entry.  
`labels` |  `map<string, string>` Optional. Set of labels associated with a Certificate Map Entry.  
`certificates[]` |  `string` Optional. A set of Certificates defines for the given `hostname`. There can be defined up to four certificates in each Certificate Map Entry. Each certificate must match pattern `projects/*/locations/*/certificates/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `certificates`:

  * `certificatemanager.certs.use`

  
`state` |  `[ServingState](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.ServingState)` Output only. A serving state of this Certificate Map Entry.  
Union field `match`. The matcher for this certificate map entry. Required. `match` can be only one of the following:  
`hostname` |  `string` A Hostname (FQDN, e.g. `example.com`) or a wildcard hostname expression (`*.example.com`) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate.  
`matcher` |  `[Matcher](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry.Matcher)` A predefined matcher for particular cases, other than SNI selection.  
  
## Matcher

Defines predefined cases other than SNI-hostname match when this configuration should be applied.

Enums  
---  
`MATCHER_UNSPECIFIED` | A matcher has't been recognized.  
`PRIMARY` | A primary certificate that is served when SNI wasn't specified in the request or SNI couldn't be found in the map.  
  
## CreateCertificateIssuanceConfigRequest

Request for the `CreateCertificateIssuanceConfig` method.

Fields  
---  
`parent` |  `string` Required. The parent resource of the certificate issuance config. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certissuanceconfigs.create`

  
`certificate_issuance_config_id` |  `string` Required. A user-provided name of the certificate config.  
`certificate_issuance_config` |  `[CertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig)` Required. A definition of the certificate issuance config to create.  
  
## CreateCertificateMapEntryRequest

Request for the `CreateCertificateMapEntry` method.

Fields  
---  
`parent` |  `string` Required. The parent resource of the certificate map entry. Must be in the format `projects/*/locations/*/certificateMaps/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certmapentries.create`

  
`certificate_map_entry_id` |  `string` Required. A user-provided name of the certificate map entry.  
`certificate_map_entry` |  `[CertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry)` Required. A definition of the certificate map entry to create.  
  
## CreateCertificateMapRequest

Request for the `CreateCertificateMap` method.

Fields  
---  
`parent` |  `string` Required. The parent resource of the certificate map. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certmaps.create`

  
`certificate_map_id` |  `string` Required. A user-provided name of the certificate map.  
`certificate_map` |  `[CertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap)` Required. A definition of the certificate map to create.  
  
## CreateCertificateRequest

Request for the `CreateCertificate` method.

Fields  
---  
`parent` |  `string` Required. The parent resource of the certificate. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certs.create`

  
`certificate_id` |  `string` Required. A user-provided name of the certificate.  
`certificate` |  `[Certificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate)` Required. A definition of the certificate to create.  
  
## CreateDnsAuthorizationRequest

Request for the `CreateDnsAuthorization` method.

Fields  
---  
`parent` |  `string` Required. The parent resource of the dns authorization. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.dnsauthorizations.create`

  
`dns_authorization_id` |  `string` Required. A user-provided name of the dns authorization.  
`dns_authorization` |  `[DnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization)` Required. A definition of the dns authorization to create.  
  
## CreateTrustConfigRequest

Request for the `CreateTrustConfig` method.

Fields  
---  
`parent` |  `string` Required. The parent resource of the TrustConfig. Must be in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.trustconfigs.create`

  
`trust_config_id` |  `string` Required. A user-provided name of the TrustConfig. Must match the regexp `[a-z0-9-]{1,63}`.  
`trust_config` |  `[TrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig)` Required. A definition of the TrustConfig to create.  
  
## DeleteCertificateIssuanceConfigRequest

Request for the `DeleteCertificateIssuanceConfig` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate issuance config to delete. Must be in the format `projects/*/locations/*/certificateIssuanceConfigs/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certissuanceconfigs.delete`

  
  
## DeleteCertificateMapEntryRequest

Request for the `DeleteCertificateMapEntry` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate map entry to delete. Must be in the format `projects/*/locations/*/certificateMaps/*/certificateMapEntries/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certmapentries.delete`

  
  
## DeleteCertificateMapRequest

Request for the `DeleteCertificateMap` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate map to delete. Must be in the format `projects/*/locations/*/certificateMaps/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certmaps.delete`

  
  
## DeleteCertificateRequest

Request for the `DeleteCertificate` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate to delete. Must be in the format `projects/*/locations/*/certificates/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certs.delete`

  
  
## DeleteDnsAuthorizationRequest

Request for the `DeleteDnsAuthorization` method.

Fields  
---  
`name` |  `string` Required. A name of the dns authorization to delete. Must be in the format `projects/*/locations/*/dnsAuthorizations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.dnsauthorizations.delete`

  
  
## DeleteTrustConfigRequest

Request for the `DeleteTrustConfig` method.

Fields  
---  
`name` |  `string` Required. A name of the TrustConfig to delete. Must be in the format `projects/*/locations/*/trustConfigs/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.trustconfigs.delete`

  
`etag` |  `string` Optional. The current etag of the TrustConfig. If an etag is provided and does not match the current etag of the resource, deletion will be blocked and an ABORTED error will be returned.  
  
## DnsAuthorization

A DnsAuthorization resource describes a way to perform domain authorization for certificate issuance.

Fields  
---  
`name` |  `string` Identifier. A user-defined name of the dns authorization. DnsAuthorization names must be unique globally and match pattern `projects/*/locations/*/dnsAuthorizations/*`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a DnsAuthorization.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a DnsAuthorization.  
`labels` |  `map<string, string>` Optional. Set of labels associated with a DnsAuthorization.  
`description` |  `string` Optional. One or more paragraphs of text description of a DnsAuthorization.  
`domain` |  `string` Required. Immutable. A domain that is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for `example.com` can be used to issue certificates for `example.com` and `*.example.com`.  
`dns_resource_record` |  `[DnsResourceRecord](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization.DnsResourceRecord)` Output only. DNS Resource Record that needs to be added to DNS configuration.  
`type` |  `[Type](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization.Type)` Optional. Immutable. Type of DnsAuthorization. If unset during resource creation the following default will be used: - in location `global`: FIXED_RECORD, - in other locations: PER_PROJECT_RECORD.  
`tags` |  `map<string, string>` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"  
  
## DnsResourceRecord

The structure describing the DNS Resource Record that needs to be added to DNS configuration for the authorization to be usable by certificate.

Fields  
---  
`name` |  `string` Output only. Fully qualified name of the DNS Resource Record. e.g. `_acme-challenge.example.com`  
`type` |  `string` Output only. Type of the DNS Resource Record. Currently always set to "CNAME".  
`data` |  `string` Output only. Data of the DNS Resource Record.  
  
## Type

DnsAuthorization type.

Enums  
---  
`TYPE_UNSPECIFIED` | Type is unspecified.  
`FIXED_RECORD` | FIXED_RECORD DNS authorization uses DNS-01 validation method.  
`PER_PROJECT_RECORD` | PER_PROJECT_RECORD DNS authorization allows for independent management of Google-managed certificates with DNS authorization across multiple projects.  
  
## GetCertificateIssuanceConfigRequest

Request for the `GetCertificateIssuanceConfig` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate issuance config to describe. Must be in the format `projects/*/locations/*/certificateIssuanceConfigs/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certissuanceconfigs.get`

  
  
## GetCertificateMapEntryRequest

Request for the `GetCertificateMapEntry` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate map entry to describe. Must be in the format `projects/*/locations/*/certificateMaps/*/certificateMapEntries/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certmapentries.get`

  
  
## GetCertificateMapRequest

Request for the `GetCertificateMap` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate map to describe. Must be in the format `projects/*/locations/*/certificateMaps/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certmaps.get`

  
  
## GetCertificateRequest

Request for the `GetCertificate` method.

Fields  
---  
`name` |  `string` Required. A name of the certificate to describe. Must be in the format `projects/*/locations/*/certificates/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.certs.get`

  
  
## GetDnsAuthorizationRequest

Request for the `GetDnsAuthorization` method.

Fields  
---  
`name` |  `string` Required. A name of the dns authorization to describe. Must be in the format `projects/*/locations/*/dnsAuthorizations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.dnsauthorizations.get`

  
  
## GetTrustConfigRequest

Request for the `GetTrustConfig` method.

Fields  
---  
`name` |  `string` Required. A name of the TrustConfig to describe. Must be in the format `projects/*/locations/*/trustConfigs/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `certificatemanager.trustconfigs.get`

  
  
## ListCertificateIssuanceConfigsRequest

Request for the `ListCertificateIssuanceConfigs` method.

Fields  
---  
`parent` |  `string` Required. The project and location from which the certificate should be listed, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certissuanceconfigs.list`

  
`page_size` |  `int32` Optional. Maximum number of certificate configs to return per call.  
`page_token` |  `string` Optional. The value returned by the last `ListCertificateIssuanceConfigsResponse`. Indicates that this is a continuation of a prior `ListCertificateIssuanceConfigs` call, and that the system should return the next page of data.  
`filter` |  `string` Optional. Filter expression to restrict the Certificates Configs returned.  
`order_by` |  `string` Optional. A list of Certificate Config field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`.  
  
## ListCertificateIssuanceConfigsResponse

Response for the `ListCertificateIssuanceConfigs` method.

Fields  
---  
`certificate_issuance_configs[]` |  `[CertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig)` A list of certificate configs for the parent resource.  
`next_page_token` |  `string` If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListCertificateMapEntriesRequest

Request for the `ListCertificateMapEntries` method.

Fields  
---  
`parent` |  `string` Required. The project, location and certificate map from which the certificate map entries should be listed, specified in the format `projects/*/locations/*/certificateMaps/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certmapentries.list`

  
`page_size` |  `int32` Optional. Maximum number of certificate map entries to return. The service may return fewer than this value. If unspecified, at most 50 certificate map entries will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. The value returned by the last `ListCertificateMapEntriesResponse`. Indicates that this is a continuation of a prior `ListCertificateMapEntries` call, and that the system should return the next page of data.  
`filter` |  `string` Optional. Filter expression to restrict the returned Certificate Map Entries.  
`order_by` |  `string` Optional. A list of Certificate Map Entry field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`.  
  
## ListCertificateMapEntriesResponse

Response for the `ListCertificateMapEntries` method.

Fields  
---  
`certificate_map_entries[]` |  `[CertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry)` A list of certificate map entries for the parent resource.  
`next_page_token` |  `string` If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListCertificateMapsRequest

Request for the `ListCertificateMaps` method.

Fields  
---  
`parent` |  `string` Required. The project and location from which the certificate maps should be listed, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certmaps.list`

  
`page_size` |  `int32` Optional. Maximum number of certificate maps to return per call.  
`page_token` |  `string` Optional. The value returned by the last `ListCertificateMapsResponse`. Indicates that this is a continuation of a prior `ListCertificateMaps` call, and that the system should return the next page of data.  
`filter` |  `string` Optional. Filter expression to restrict the Certificates Maps returned.  
`order_by` |  `string` Optional. A list of Certificate Map field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`.  
  
## ListCertificateMapsResponse

Response for the `ListCertificateMaps` method.

Fields  
---  
`certificate_maps[]` |  `[CertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap)` A list of certificate maps for the parent resource.  
`next_page_token` |  `string` If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListCertificatesRequest

Request for the `ListCertificates` method.

Fields  
---  
`parent` |  `string` Required. The project and location from which the certificate should be listed, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.certs.list`

  
`page_size` |  `int32` Optional. Maximum number of certificates to return per call.  
`page_token` |  `string` Optional. The value returned by the last `ListCertificatesResponse`. Indicates that this is a continuation of a prior `ListCertificates` call, and that the system should return the next page of data.  
`filter` |  `string` Optional. Filter expression to restrict the Certificates returned.  
`order_by` |  `string` Optional. A list of Certificate field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`.  
  
## ListCertificatesResponse

Response for the `ListCertificates` method.

Fields  
---  
`certificates[]` |  `[Certificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate)` A list of certificates for the parent resource.  
`next_page_token` |  `string` If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
`unreachable[]` |  `string` A list of locations that could not be reached.  
  
## ListDnsAuthorizationsRequest

Request for the `ListDnsAuthorizations` method.

Fields  
---  
`parent` |  `string` Required. The project and location from which the dns authorizations should be listed, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.dnsauthorizations.list`

  
`page_size` |  `int32` Optional. Maximum number of dns authorizations to return per call.  
`page_token` |  `string` Optional. The value returned by the last `ListDnsAuthorizationsResponse`. Indicates that this is a continuation of a prior `ListDnsAuthorizations` call, and that the system should return the next page of data.  
`filter` |  `string` Optional. Filter expression to restrict the Dns Authorizations returned.  
`order_by` |  `string` Optional. A list of Dns Authorization field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`.  
  
## ListDnsAuthorizationsResponse

Response for the `ListDnsAuthorizations` method.

Fields  
---  
`dns_authorizations[]` |  `[DnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization)` A list of dns authorizations for the parent resource.  
`next_page_token` |  `string` If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## ListTrustConfigsRequest

Request for the `ListTrustConfigs` method.

Fields  
---  
`parent` |  `string` Required. The project and location from which the TrustConfigs should be listed, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `certificatemanager.trustconfigs.list`

  
`page_size` |  `int32` Optional. Maximum number of TrustConfigs to return per call.  
`page_token` |  `string` Optional. The value returned by the last `ListTrustConfigsResponse`. Indicates that this is a continuation of a prior `ListTrustConfigs` call, and that the system should return the next page of data.  
`filter` |  `string` Optional. Filter expression to restrict the TrustConfigs returned.  
`order_by` |  `string` Optional. A list of TrustConfig field names used to specify the order of the returned results. The default sorting order is ascending. To specify descending order for a field, add a suffix `" desc"`.  
  
## ListTrustConfigsResponse

Response for the `ListTrustConfigs` method.

Fields  
---  
`trust_configs[]` |  `[TrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig)` A list of TrustConfigs for the parent resource.  
`next_page_token` |  `string` If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
## OperationMetadata

Represents the metadata of the long-running operation. Output only.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the operation finished running.  
`target` |  `string` Server-defined resource path for the target of the operation.  
`verb` |  `string` Name of the verb executed by the operation.  
`status_message` |  `string` Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have `[google.longrunning.Operation.error](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of `1`, corresponding to `Code.CANCELLED`.  
`api_version` |  `string` API version used to start the operation.  
  
## ServingState

Defines set of serving states associated with a resource.

Enums  
---  
`SERVING_STATE_UNSPECIFIED` | The status is undefined.  
`ACTIVE` | The configuration is serving.  
`PENDING` | Update is in progress. Some frontends may serve this configuration.  
  
## TrustConfig

Defines a trust config.

Fields  
---  
`name` |  `string` Identifier. A user-defined name of the trust config. TrustConfig names must be unique globally and match pattern `projects/*/locations/*/trustConfigs/*`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The creation timestamp of a TrustConfig.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The last update timestamp of a TrustConfig.  
`labels` |  `map<string, string>` Optional. Set of labels associated with a TrustConfig.  
`description` |  `string` Optional. One or more paragraphs of text description of a TrustConfig.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`spiffe_trust_stores` |  `map<string, `[TrustStore](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.TrustStore)`>` Optional. Defines a mapping from a trust domain to a TrustStore. This is used for SPIFFE certificate validation.  
`trust_stores[]` |  `[TrustStore](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.TrustStore)` Optional. Set of trust stores to perform validation against.This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation.Only one TrustStore specified is currently allowed.  
`allowlisted_certificates[]` |  `[AllowlistedCertificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.AllowlistedCertificate)` Optional. A certificate matching an allowlisted certificate is always considered valid as long as the certificate is parseable, proof of private key possession is established, and constraints on the certificate's SAN field are met.  
`tags` |  `map<string, string>` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"  
  
## AllowlistedCertificate

Defines an allowlisted certificate.

Fields  
---  
`pem_certificate` |  `string` Required. PEM certificate that is allowlisted. The certificate can be up to 5k bytes, and must be a parseable X.509 certificate.  
  
## IntermediateCA

Defines an intermediate CA.

Fields  
---  
Union field `kind`. Kind of the intermediate CA. Required. `kind` can be only one of the following:  
`pem_certificate` |  `string` PEM intermediate certificate used for building up paths for validation.Each certificate provided in PEM format may occupy up to 5kB.  
  
## TrustAnchor

Defines a trust anchor.

Fields  
---  
Union field `kind`. Kind of the trust anchor. Required. `kind` can be only one of the following:  
`pem_certificate` |  `string` PEM root certificate of the PKI used for validation.Each certificate provided in PEM format may occupy up to 5kB.  
  
## TrustStore

Defines a trust store.

Fields  
---  
`trust_anchors[]` |  `[TrustAnchor](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.TrustAnchor)` Optional. List of Trust Anchors to be used while performing validation against a given TrustStore.  
`intermediate_cas[]` |  `[IntermediateCA](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig.IntermediateCA)` Optional. Set of intermediate CA certificates used for the path building phase of chain validation.The field is currently not supported if TrustConfig is used for the workload certificate feature.  
  
## UpdateCertificateIssuanceConfigRequest

Request for the `UpdateCertificateIssuanceConfig` method.

Fields  
---  
`certificate_issuance_config` |  `[CertificateIssuanceConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateIssuanceConfig)` Required. A definition of the certificate issuance config to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `certificateIssuanceConfig`:

  * `certificatemanager.certissuanceconfigs.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>.  
  
## UpdateCertificateMapEntryRequest

Request for the `UpdateCertificateMapEntry` method.

Fields  
---  
`certificate_map_entry` |  `[CertificateMapEntry](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMapEntry)` Required. A definition of the certificate map entry to create map entry. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `certificateMapEntry`:

  * `certificatemanager.certmapentries.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>.  
  
## UpdateCertificateMapRequest

Request for the `UpdateCertificateMap` method.

Fields  
---  
`certificate_map` |  `[CertificateMap](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.CertificateMap)` Required. A definition of the certificate map to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `certificateMap`:

  * `certificatemanager.certmaps.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>.  
  
## UpdateCertificateRequest

Request for the `UpdateCertificate` method.

Fields  
---  
`certificate` |  `[Certificate](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.Certificate)` Required. A definition of the certificate to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `certificate`:

  * `certificatemanager.certs.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>.  
  
## UpdateDnsAuthorizationRequest

Request for the `UpdateDnsAuthorization` method.

Fields  
---  
`dns_authorization` |  `[DnsAuthorization](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.DnsAuthorization)` Required. A definition of the dns authorization to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `dnsAuthorization`:

  * `certificatemanager.dnsauthorizations.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>.  
  
## UpdateTrustConfigRequest

Request for the `UpdateTrustConfig` method.

Fields  
---  
`trust_config` |  `[TrustConfig](https://docs.cloud.google.com/certificate-manager/docs/reference/certificate-manager/rpc/google.cloud.certificatemanager.v1#google.cloud.certificatemanager.v1.TrustConfig)` Required. A definition of the TrustConfig to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `trustConfig`:

  * `certificatemanager.trustconfigs.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-16 UTC."],[],[]] 
