---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-Authority/
title: GKE Hub V1beta1 API - Class Google::Cloud::GkeHub::V1beta1::Authority (v0.21.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:39.662448+00:00
---

# GKE Hub V1beta1 API - Class Google::Cloud::GkeHub::V1beta1::Authority (v0.21.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1beta1/latest/Google-Cloud-GkeHub-V1beta1-Authority/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GKE Hub V1beta1 API - Class Google::Cloud::GkeHub::V1beta1::Authority (v0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.20.1  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the GKE Hub V1beta1 API class Google::Cloud::GkeHub::V1beta1::Authority.

Authority encodes how Google will recognize identities from this Membership. See the workload identity documentation for more details: <https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity>

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #identity_provider
    
    
    def identity_provider() -> ::String

**Returns**

  * (::String) — Output only. An identity provider that reflects the `issuer` in the workload identity pool. 



### #issuer
    
    
    def issuer() -> ::String

**Returns**

  * (::String) — Optional. A JSON Web Token (JWT) issuer URI. `issuer` must start with `https://` and be a valid URL with length <2000 characters.

If set, then Google will allow valid OIDC tokens from this issuer to authenticate within the workload_identity_pool. OIDC discovery will be performed on this URI to validate tokens from the issuer.

Clearing `issuer` disables Workload Identity. `issuer` cannot be directly modified; it must be cleared (and Workload Identity disabled) before using a new issuer (and re-enabling Workload Identity). 




### #issuer=
    
    
    def issuer=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A JSON Web Token (JWT) issuer URI. `issuer` must start with `https://` and be a valid URL with length <2000 characters.

If set, then Google will allow valid OIDC tokens from this issuer to authenticate within the workload_identity_pool. OIDC discovery will be performed on this URI to validate tokens from the issuer.

Clearing `issuer` disables Workload Identity. `issuer` cannot be directly modified; it must be cleared (and Workload Identity disabled) before using a new issuer (and re-enabling Workload Identity). 




**Returns**

  * (::String) — Optional. A JSON Web Token (JWT) issuer URI. `issuer` must start with `https://` and be a valid URL with length <2000 characters.

If set, then Google will allow valid OIDC tokens from this issuer to authenticate within the workload_identity_pool. OIDC discovery will be performed on this URI to validate tokens from the issuer.

Clearing `issuer` disables Workload Identity. `issuer` cannot be directly modified; it must be cleared (and Workload Identity disabled) before using a new issuer (and re-enabling Workload Identity). 




### #oidc_jwks
    
    
    def oidc_jwks() -> ::String

**Returns**

  * (::String) — Optional. OIDC verification keys for this Membership in JWKS format (RFC 7517).

When this field is set, OIDC discovery will NOT be performed on `issuer`, and instead OIDC tokens will be validated using this field. 




### #oidc_jwks=
    
    
    def oidc_jwks=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. OIDC verification keys for this Membership in JWKS format (RFC 7517).

When this field is set, OIDC discovery will NOT be performed on `issuer`, and instead OIDC tokens will be validated using this field. 




**Returns**

  * (::String) — Optional. OIDC verification keys for this Membership in JWKS format (RFC 7517).

When this field is set, OIDC discovery will NOT be performed on `issuer`, and instead OIDC tokens will be validated using this field. 




### #workload_identity_pool
    
    
    def workload_identity_pool() -> ::String

**Returns**

  * (::String) — Output only. The name of the workload identity pool in which `issuer` will be recognized.

There is a single Workload Identity Pool per Hub that is shared between all Memberships that belong to that Hub. For a Hub hosted in {PROJECT_ID}, the workload pool format is `{PROJECT_ID}.hub.id.goog`, although this is subject to change in newer versions of this API. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
