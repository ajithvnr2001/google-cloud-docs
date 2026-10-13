---
url: https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.KubernetesResource
title: Class KubernetesResource (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:34.984904+00:00
---

# Class KubernetesResource (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.KubernetesResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class KubernetesResource (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.1  1.24.0  1.23.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.3  1.16.0  1.15.1  1.14.2  1.13.1  1.12.1  1.11.0  1.10.2  1.9.0  1.8.1  1.7.1  1.6.0  1.5.3  1.4.3  1.3.0  1.2.0  1.1.0  1.0.0  0.2.2  0.1.2 
    
    
    KubernetesResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

KubernetesResource contains the YAML manifests and configuration for Membership Kubernetes resources in the cluster. After CreateMembership or UpdateMembership, these resources should be re-applied in the cluster.

## Attributes  
  
---  
**Name** | **Description**  
`membership_cr_manifest` |  `str`   
Input only. The YAML representation of the Membership CR. This field is ignored for GKE clusters where Hub can read the CR directly. Callers should provide the CR that is currently present in the cluster during CreateMembership or UpdateMembership, or leave this field empty if none exists. The CR manifest is used to validate the cluster has not been registered with another Membership.   
`membership_resources` |  `MutableSequence[[google.cloud.gkehub_v1beta1.types.ResourceManifest](https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.ResourceManifest)]`   
Output only. Additional Kubernetes resources that need to be applied to the cluster after Membership creation, and after every update. This field is only populated in the Membership returned from a successful long-running operation from CreateMembership or UpdateMembership. It is not populated during normal GetMembership or ListMemberships requests. To get the resource manifest after the initial registration, the caller should make a UpdateMembership call with an empty field mask.   
`connect_resources` |  `MutableSequence[[google.cloud.gkehub_v1beta1.types.ResourceManifest](https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.ResourceManifest)]`   
Output only. The Kubernetes resources for installing the GKE Connect agent This field is only populated in the Membership returned from a successful long-running operation from CreateMembership or UpdateMembership. It is not populated during normal GetMembership or ListMemberships requests. To get the resource manifest after the initial registration, the caller should make a UpdateMembership call with an empty field mask.   
`resource_options` |  `[google.cloud.gkehub_v1beta1.types.ResourceOptions](https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.ResourceOptions)`   
Optional. Options for Kubernetes resource generation.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
