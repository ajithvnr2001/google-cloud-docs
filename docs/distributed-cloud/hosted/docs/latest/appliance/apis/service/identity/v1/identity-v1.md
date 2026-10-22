---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/identity/v1/identity-v1/
title: KRM API iam.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:35.911374+00:00
---

# KRM API iam.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/identity/v1/identity-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API iam.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## iam.gdc.goog/v1

Contains API Schema definitions for the identity API group.

Package v1 contains API Schema definitions for the iam.gdc.goog v1 API group

### CustomRole

Represents a template for a zonal CustomRole Custom roles provide fine-grained control over user permissions, unlike predefined roles. This allows organizations to tailor access rights to their specific needs, balancing operational efficiency with security. By adhering to the principle of least privilege, custom roles significantly enhance security and protect sensitive data.

_Appears in:_ \- CustomRoleList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `CustomRole`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _CustomRoleSpec_ |   
`status` _CustomRoleStatus_ |   
  
### CustomRoleList

Contains a list of `CustomRole` resource

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `CustomRoleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CustomRole array_ |   
  
### CustomRoleStatus

Provides a status of CustomRole

_Appears in:_ \- CustomRole

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this Custom role overall state  
`propagationInfo` _PropagationInfo_ | propagation information of converted template for zonal role template conversion  
  
### IdentityProviderConfig

Represents a configuration for an identity provider that supports OIDC or SAML.

_Appears in:_ \- IdentityProviderConfigList

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfig`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _IdentityProviderConfigSpec_ |   
`status` _IdentityProviderConfigStatus_ |   
  
### IdentityProviderConfigList

Contains a list of `IdentityProviderConfig` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `iam.gdc.goog/v1`  
`kind` _string_ | `IdentityProviderConfigList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _IdentityProviderConfig array_ |   
  
### IdentityProviderConfigSpec

Provides the specification, or desired state, of an `IdentityProviderConfig` resource. Either OIDCConfig or SAMLConfig has to be provided but not both.

_Appears in:_ \- IdentityProviderConfig

Field | Description  
---|---  
`oidc` _OIDCProviderConfig_ | OIDC specific configuration.  
`saml` _SAMLProviderConfig_ | SAML specific configuration.  
  
### IdentityProviderConfigStatus

Provides the status of an `IdentityProviderConfig` resource.

_Appears in:_ \- IdentityProviderConfig

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
