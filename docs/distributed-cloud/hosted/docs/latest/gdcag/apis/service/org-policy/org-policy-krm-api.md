---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/org-policy/org-policy-krm-api/
title: KRM API constraints.gatekeeper.sh/v1beta1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:02.784076+00:00
---

# KRM API constraints.gatekeeper.sh/v1beta1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/org-policy/org-policy-krm-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API constraints.gatekeeper.sh/v1beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## constraints.gatekeeper.sh/v1beta1

### GDCHRestrictedService

GDCHRestrictedService lets you restrict which service can be used on Distributed Cloud. When applied, the policy prevents the use of the APIs that it references.

Field | Description  
---|---  
`apiVersion` _string_ | `constraints.gatekeeper.sh/v1beta1`  
`kind` _string_ | `GDCHRestrictedService`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _GDCHRestrictedServiceSpec_ |   
`status` _GDCHRestrictedServiceStatus_ |   
  
### GDCHRestrictedServiceSpec

GDCHRestrictedServiceSpec defines the desired state for a GDCHRestrictedService.

_Appears in:_ \- GDCHRestrictedService

Field | Description  
---|---  
`match` _[Match](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/org-policy/policy-match-section)_ | Refer to the dedicated page for fields of `match`.  
`parameters` _Parameters_ | The parameters of the policy.  
  
### Parameters

Parameters define the parameters of a GDCHRestrictedService.

_Appears in:_ \- GDCHRestrictedServiceSpec

Field | Description  
---|---  
`disabledOperations` _string array_ | The API operations that are disabled by the GDCHRestrictedService policy. Supported values: `CREATE` and `UPDATE`.  
  
### GDCHRestrictedServiceStatus

GDCHRestrictedServiceStatus defines the observed state of the GDCHRestrictedService policy.

_Appears in:_ \- GDCHRestrictedService

Field | Description  
---|---  
`auditTimestamp` _Timestamp_ | The last time an audit item was generated.  
`enforced` _boolean_ | Whether the policy is currently enforced or not.  
`violations` _Violation array_ | List of recent observed policy violations.  
  
### Violation

Violation represents an event where an attempted violation of the policy happened.

_Appears in:_ \- GDCHRestrictedServiceStatus

Field | Description  
---|---  
`enforcementAction` _string_ | The enforcement action that was taken against this violation. This is often `deny`.  
`message` _string_ | The message that was given to the client who performed the action that triggered the violation.  
`group` _string_ | The API group to which the resource that triggered the violation belongs.  
`version` _string_ | The API version to which the resource that triggered the violation belongs.  
`kind` _string_ | The API kind of the resource that triggered the violation.  
`name` _string_ | The name of the resource that triggered the violation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
