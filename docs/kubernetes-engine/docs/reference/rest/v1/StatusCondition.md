---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/StatusCondition/
title: StatusCondition \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:43.551943+00:00
---

# StatusCondition  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/StatusCondition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  StatusCondition Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Code



StatusCondition describes why a cluster or a node pool has a certain status (e.g., ERROR or DEGRADED).

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/StatusCondition#Code)),
      "message": string,
      "canonicalCode": enum ([Code](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/Shared.Types/Code))
    }  
  
Fields  
---  
`code  
**(deprecated)**` |  `enum (`[Code](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/StatusCondition#Code)`)` This item is deprecated!Machine-friendly representation of the condition Deprecated. Use canonicalCode instead.  
`message` |  `string` Human-friendly representation of the condition  
`canonicalCode` |  `enum (`[Code](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/Shared.Types/Code)`)` Canonical code of the condition.  
  
## Code

Code for each condition

Enums  
---  
`UNKNOWN` | UNKNOWN indicates a generic condition.  
`GCE_STOCKOUT` | GCE_STOCKOUT indicates that Google Compute Engine resources are temporarily unavailable.  
`GKE_SERVICE_ACCOUNT_DELETED` | GKE_SERVICE_ACCOUNT_DELETED indicates that the user deleted their robot service account.  
`GCE_QUOTA_EXCEEDED` | Google Compute Engine quota was exceeded.  
`SET_BY_OPERATOR` | Cluster state was manually changed by an SRE due to a system logic error.  
`CLOUD_KMS_KEY_ERROR` | Unable to perform an encrypt operation against the CloudKMS key used for etcd level encryption.  
`CA_EXPIRING` | Cluster CA is expiring soon.  
`NODE_SERVICE_ACCOUNT_MISSING_PERMISSIONS` | Node service account is missing permissions.  
`CLOUD_KMS_KEY_DESTROYED` | Cloud KMS key version used for etcd level encryption has been destroyed. This is a permanent error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-15 UTC."],[],[]] 
