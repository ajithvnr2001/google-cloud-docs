---
url: https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities/
title: Supported identities for ingress and egress rules \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:35.746624+00:00
---

# Supported identities for ingress and egress rules  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Supported identities for ingress and egress rules Stay organized with collections  Save and categorize content based on your preferences. 

VPC Service Controls uses [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to control access to and from resources and clients within service perimeters. To refine access further, you can specify supported identities in ingress and egress rules.

This page lists the identities supported by VPC Service Controls and their identifier formats.

**Note:** You can specify workforce identity pools, workload identity pools, Workload Identity Federation for GKE ([Preview](https://cloud.google.com/products#product-launch-stages)), agentic identities, and service agents only in service perimeter ingress and egress rules. These identity types are not supported in Access Context Manager access levels.

## Supported identities

VPC Service Controls supports the following identities from [Principal identifiers for allow policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1), which use the IAM `v1` API:

Identity type | Principal type | Identifier  
---|---|---  
Single principals | User accounts | `user:USER_EMAIL_ADDRESS`  
Service accounts | `serviceAccount:SA_EMAIL_ADDRESS`  
Identity groups and third-party identities | Group | `group:GROUP_EMAIL_ADDRESS`  
Single identity in a workforce identity pool | `principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
All workforce identities in a group | `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_ID`  
All workforce identities with a specific attribute value | `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workforce identity pool | `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*`  
Single identity in a workload identity pool | `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
Workload identity pool group | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP_ID`  
All identities in a workload identity pool with a certain attribute | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workload identity pool | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*`  
[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)  
([Preview](https://cloud.google.com/products#product-launch-stages))  | All GKE Pods that use a Kubernetes service account by name | `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT`  
All GKE Pods that use a Kubernetes service account by ID | `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/kubernetes.serviceaccount.uid/SERVICEACCOUNT_ID`  
All GKE Pods in a Kubernetes namespace, regardless of service account or cluster | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/namespace/NAMESPACE`  
All GKE Pods in a cluster | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/kubernetes.cluster/https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME`  
[Agent identities](https://docs.cloud.google.com/agent-builder/agent-engine/agent-identity#overview) | Agent identity | `principal://TRUST_DOMAIN/AGENT_UNIQUE_IDENTIFIER`  
All agent identities in a trust domain with a certain attribute | `principalSet://TRUST_DOMAIN/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All agent identities in a trust domain | `principalSet://TRUST_DOMAIN/*`  
  
For more information about these identities, see [Principal identifiers for allow policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#allow).

VPC Service Controls also supports the following [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/) formats for third-party workforce and workload identities:

Identity type | Principal type | Identifier  
---|---|---  
Workforce identities in SPIFFE format | Single identity in a workforce identity pool | `principal://POOL_ID.global.workforce.id.goog/SUBJECT_ATTRIBUTE_VALUE`  
All identities in a workforce identity pool as a trust domain with a certain attribute | `principalSet://POOL_ID.global.workforce.id.goog/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workforce identity pool as a trust domain | `principalSet://POOL_ID.global.workforce.id.goog/*`  
Workload identities in SPIFFE format | Single identity in a workload identity pool | `principal://POOL_ID.global.ORGANIZATION_ID.workload.id.goog/SUBJECT_ATTRIBUTE_VALUE`  
All identities in a workload identity pool as a trust domain with a certain attribute | `principalSet://POOL_ID.global.ORGANIZATION_ID.workload.id.goog/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workload identity pool as a trust domain | `principalSet://POOL_ID.global.ORGANIZATION_ID.workload.id.goog/*`  
  
### Workload Identity Federation for GKE considerations

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  * A limit of 1,000 Workload Identity Federation for GKE principals per access policy applies. For more information, see [Quotas and limits](https://docs.cloud.google.com/vpc-service-controls/quotas).
  * Workload Identity Federation for GKE principals don't support deleted principal syntax.
  * You can specify Workload Identity Federation for GKE principals by using either the full IAM principal identifier format (for example, `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT`) or the equivalent SPIFFE format (for example, `principal://PROJECT_ID.svc.id.goog/ns/NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT`). When you [describe or retrieve a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#list-and-describe) that contains rules created with SPIFFE syntax, VPC Service Controls returns the identity in SPIFFE format.



## Deleted IAM principals

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To help you manage service perimeters that reference deleted accounts, VPC Service Controls lets you enable support for deleted IAM principal identifiers. By default, attempting to update or list perimeters that contain deleted principals fails with a `The email address is invalid or non-existent` error. For more information, see [Troubleshooting common issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#invalid-email-address).

To retrieve or update perimeters that contain deleted principals, use the Access Context Manager API. Set the `deletedPrincipalSyntax` parameter (REST) or the `deleted_principal_syntax` field (gRPC) to `DELETED_PRINCIPAL_SYNTAX_SUPPORT_ENABLED` in a request, such as the [get](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/get), [list](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/list), or [patch](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/patch) methods.

For more information, see the [REST](https://docs.cloud.google.com/access-context-manager/docs/reference/rest) or [gRPC](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1) reference pages.

For example, you can use the following `curl` command to get a perimeter:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://accesscontextmanager.googleapis.com/v1/accessPolicies/\
    POLICY_NAME/servicePerimeters/PERIMETER_NAME?\
    deletedPrincipalSyntax=DELETED_PRINCIPAL_SYNTAX_SUPPORT_ENABLED"
    

**Note:** You can't use the Google Cloud console or the `gcloud` command-line tool to manage perimeters that contain deleted principals. Attempting to do so fails with a `The email address is invalid or non-existent` error.

For a list of IAM principal types that support the deleted syntax, see [Principal identifiers for allow policies](https://docs.cloud.google.com/iam/docs/principal-identifiers).

### Limitations

The following limitations apply to deleted IAM principals in VPC Service Controls perimeters:

  * VPC Service Controls supports only the deleted IAM principals that use the IAM `v1` API. It doesn't support deleted principals that use the IAM `v2` or `v3` APIs.
  * Deleted IAM principals in access levels are not supported.
  * Principals that don't support the `deleted:` prefix syntax in IAM are also not supported in VPC Service Controls service perimeter rules.
  * You can specify a maximum of 500 deleted identities in an access policy.



## What's next

  * [Configure identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
