---
url: https://docs.cloud.google.com/iam/docs/principal-identifiers/
title: Principal identifiers \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:17.394557+00:00
---

# Principal identifiers  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/principal-identifiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Principal identifiers Stay organized with collections  Save and categorize content based on your preferences. 

When you refer to a principal in an Identity and Access Management (IAM) policy, you need to use the correct identifier for the principal. The format of the identifier depends on the [type of principal](https://docs.cloud.google.com/iam/docs/principals-overview#principal-types) that you want to refer to and the type of policy that you're writing.

This page lists the identifier formats for each policy type's supported principal types.

## Principal identifiers for allow policies

The following table describes the principal identifiers for [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies), which use the IAM `v1` API.

These identifiers are also used for [Privileged Access Manager entitlements](https://docs.cloud.google.com/iam/docs/pam-overview).

Principal type | Identifier  
---|---  
Google Account |  `user:USER_EMAIL_ADDRESS` **Example:** `user:alex@example.com` **Note** : When granting access to a new Google Account in the Google Cloud console, omit the `user:` prefix.   
Service account |  `serviceAccount:SA_EMAIL_ADDRESS` **Example:** `serviceAccount:my-service-account@my-project.iam.gserviceaccount.com` When granting access to a new service account in the Google Cloud console, omit the `serviceAccount:` prefix.   
All service accounts in a project, folder, or organization |  `principalSet://cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_NUMBER/type/ServiceAccount` **Example for all service accounts in a project:** `principalSet://cloudresourcemanager.googleapis.com/projects/123456789012/type/ServiceAccount` **Example for all service accounts in all projects in a folder:** `principalSet://cloudresourcemanager.googleapis.com/folders/123456789012/type/ServiceAccount` **Example for all service accounts in all projects in an organization:** `principalSet://cloudresourcemanager.googleapis.com/organizations/123456789012/type/ServiceAccount` **Note** : Moving projects into or out of a folder or organization changes the service accounts included in this principal set. For example, if you move a project out of a folder or organization, then this principal set no longer includes that project's service accounts.   
Google group |  `group:GROUP_EMAIL_ADDRESS` **Example:** `group:my-group@example.com` When granting access to a new Google group in the Google Cloud console, omit the `group:` prefix.   
Google domain |  `domain:DOMAIN` **Example:** `domain:example.com` When granting access to a new domain in the Google Cloud console, omit the `domain:` prefix.   
[All users](https://docs.cloud.google.com/iam/docs/principals-overview#all-users) | `allUsers`  
[All authenticated users](https://docs.cloud.google.com/iam/docs/principals-overview#all-authenticated-users) | `allAuthenticatedUsers`  
Built-in resource identities |  Only available for supported resources. The format varies depending on the resource. See [Resources with built-in identities](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities) for details.   
Single identity in a workforce identity pool |  ` principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE ` **Example:** `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`  
All workforce identities in a group |  ` principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_ID ` **Example using a group email:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/group/administrators-group@altostrat.com` **Example using a group UUID:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/group/abcdefgh-0123-0123-abcdef`  
All workforce identities with a specific attribute value |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE` **Example:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/attribute.department/administration`  
All identities in a workforce identity pool |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*` **Example:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/*`  
Single identity in a workload identity pool | `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
Workload identity pool group | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP_ID`  
All identities in a workload identity pool with a certain attribute | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workload identity pool | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*`  
Agent identity |  `principal://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH` **Example (Vertex AI Agent Engine in an organization):** `principal://agents.global.org-123456789012.system.id.goog/resources/aiplatform/projects/9876543210/locations/us-central1/reasoningEngines/my-test-agent` **Example (Vertex AI Agent Engine in a project without an organization):** `principal://agents.global.proj-9876543210.system.id.goog/resources/aiplatform/projects/9876543210/locations/us-central1/reasoningEngines/my-test-agent` **Example (Gemini Enterprise):** `principal://agents.global.org-123456789012.system.id.goog/resources/discoveryengine/projects/9876543210/locations/global/collections/default_collection/engines/my-test-agent`  
All agent identities in a trust domain  |  `principalSet://TRUST_DOMAIN/*` **Example:** `principalSet://agents.global.org-123456789012.system.id.goog/*`  
All agent identities in a project  |  `principalSet://TRUST_DOMAIN/attribute.platformContainer/aiplatform/projects/PROJECT_NUMBER` **Example:** `principalSet://agents.global.org-123456789012.system.id.goog/attribute.platformContainer/aiplatform/projects/9876543210`  
All GKE Pods that use a specific Kubernetes service account |  By service account name: `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICE_ACCOUNT` By service account ID: `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/kubernetes.serviceaccount.uid/SERVICEACCOUNT_ID` Legacy format: `serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/KUBERNETES_SERVICE_ACCOUNT]`  
All GKE Pods in a Kubernetes namespace, regardless of service account or cluster | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/namespace/NAMESPACE`  
All GKE Pods in a specific cluster | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/kubernetes.cluster/https://container.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/clusters/CLUSTER_NAME`  
Deleted Google Account1 |  `deleted:user:USER_EMAIL_ADDRESS?uid=UNIQUE_ID` **Example:** `deleted:user:alex@example.com?uid=123456789012345678901`  
Deleted service account1 |  `deleted:serviceAccount:SA_EMAIL_ADDRESS?uid=UNIQUE_ID` **Example:** `deleted:serviceAccount:my-service-account@my-project.iam.gserviceaccount.com?uid=123456789012345678901`  
Deleted Google group1 |  `deleted:group:GROUP_EMAIL_ADDRESS?uid=UNIQUE_ID` **Example:** `deleted:group:my-group@example.com?uid=123456789012345678901`  
Deleted single identity in a workforce identity pool1 |  `deleted:principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE` **Example:** `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-pool-id/subject/my-subject-attribute-value`  
  
1 Don't add deleted principals when creating or modifying policies.

## Principal identifiers for deny policies

The following table describes the principal identifiers for [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview), which use the IAM `v2` API.

Principal type | Identifier  
---|---  
Google Account |  `principal://goog/subject/USER_EMAIL_ADDRESS` **Example:** `principal://goog/subject/alex@example.com`  
Service account |  `principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS` **Example:** `principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com`  
All service accounts in a project, folder, or organization |  `principalSet://cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_NUMBER/type/ServiceAccount` **Example for all service accounts in a project:** `principalSet://cloudresourcemanager.googleapis.com/projects/123456789012/type/ServiceAccount` **Example for all service accounts in all projects in a folder:** `principalSet://cloudresourcemanager.googleapis.com/folders/123456789012/type/ServiceAccount` **Example for all service accounts in all projects in an organization:** `principalSet://cloudresourcemanager.googleapis.com/organizations/123456789012/type/ServiceAccount` **Note** : Moving projects into or out of a folder or organization changes the service accounts included in this principal set. For example, if you move a project out of a folder or organization, then this principal set no longer includes that project's service accounts.   
All [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with a project, folder, or organization |  `principalSet://cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_NUMBER/type/ServiceAgent` **Example for all service agents associated with a project or its descendants:** `principalSet://cloudresourcemanager.googleapis.com/projects/123456789012/type/ServiceAgent` **Example for all service agents associated with a folder or its descendants:** `principalSet://cloudresourcemanager.googleapis.com/folders/123456789012/type/ServiceAgent` **Example for all service agents associated with an organization or its descendants:** `principalSet://cloudresourcemanager.googleapis.com/organizations/123456789012/type/ServiceAgent` **Warning:** Don't deny permissions for service agents—doing so might cause some Google Cloud services to stop working properly. Instead, use these principal sets to exempt service agents from deny rules. **Note** : Moving projects into or out of a folder or organization changes the service agents included in this principal set. For example, if you move a project out of a folder or organization, then this principal set no longer includes that project's service agents.   
Google group |  `principalSet://goog/group/GROUP_EMAIL_ADDRESS` **Example:** `principalSet://goog/group/my-group@example.com`  
All principals | `principalSet://goog/public:all`  
All principals in a Cloud Identity account (domain) |  `principalSet://goog/cloudIdentityCustomerId/CLOUD_IDENTITY_CUSTOMER_ID1` **Example:** `principalSet://goog/cloudIdentityCustomerId/C01Abc35`  
Single identity in a workforce identity pool |  ` principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE ` **Example:** `principal://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/subject/raha@altostrat.com`  
All workforce identities in a group |  ` principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/group/GROUP_ID ` **Example using a group email:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/group/administrators-group@altostrat.com` **Example using a group UUID:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/group/abcdefgh-0123-0123-abcdef`  
All workforce identities with a specific attribute value |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE` **Example:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/attribute.department/administration`  
All identities in a workforce identity pool |  `principalSet://iam.googleapis.com/locations/global/workforcePools/POOL_ID/*` **Example:** `principalSet://iam.googleapis.com/locations/global/workforcePools/altostrat-contractors/*`  
Single identity in a workload identity pool | `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE`  
Workload identity pool group | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/group/GROUP_ID`  
All identities in a workload identity pool with a certain attribute | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/attribute.ATTRIBUTE_NAME/ATTRIBUTE_VALUE`  
All identities in a workload identity pool | `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/*`  
Agent identity  |  `principal://TRUST_DOMAIN/resources/SERVICE/RESOURCE_PATH` **Example (Vertex AI Agent Engine in an organization):** `principal://agents.global.org-123456789012.system.id.goog/resources/aiplatform/projects/9876543210/locations/us-central1/reasoningEngines/my-test-agent` **Example (Vertex AI Agent Engine in a project without an organization):** `principal://agents.global.proj-9876543210.system.id.goog/resources/aiplatform/projects/9876543210/locations/us-central1/reasoningEngines/my-test-agent` **Example (Gemini Enterprise):** `principal://agents.global.org-123456789012.system.id.goog/resources/discoveryengine/projects/9876543210/locations/global/collections/default_collection/engines/my-test-agent`  
All agent identities in a trust domain  |  `principalSet://TRUST_DOMAIN/*` **Example:** `principalSet://agents.global.org-123456789012.system.id.goog/*`  
All agent identities in a project  |  `principalSet://TRUST_DOMAIN/attribute.platformContainer/aiplatform/projects/PROJECT_NUMBER` **Example:** `principalSet://agents.global.org-123456789012.system.id.goog/attribute.platformContainer/aiplatform/projects/9876543210`  
Deleted Google Account2 |  `deleted:principal://goog/subject/USER_EMAIL_ADDRESS?uid=UNIQUE_ID` **Example:** `deleted:principal://goog/subject/alex@example.com?uid=123456789012345678901`  
Deleted service account2 |  `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS?uid=UNIQUE_ID` **Example:** `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com?uid=123456789012345678901`  
Deleted Google group2 |  `deleted:principalSet://goog/group/GROUP_EMAIL_ADDRESS?uid=UNIQUE_ID` **Example:** `deleted:principalSet://goog/group/my-group@example.com?uid=123456789012345678901`  
Deleted single identity in a workforce identity pool2 |  `deleted:principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/SUBJECT_ATTRIBUTE_VALUE` **Example:** `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-pool-id/subject/my-subject-attribute-value`  
  
1[Learn how to find your Cloud Identity customer ID](https://support.google.com/cloudidentity/answer/10070793).

2 Don't add deleted principals when creating or modifying policies.

## Principal identifiers for Principal Access Boundary policy bindings

The following table describes the identifiers for the principal sets that you can use in [Principal Access Boundary (PAB) policy bindings](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies). Principal Access Boundary policy bindings use the IAM `v3` API.

To learn which principals are included in each of these principal sets, see [Supported principal sets](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets).

Principal type | Identifier  
---|---  
Workforce identity pool |  `//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID` **Example:** `//iam.googleapis.com/locations/global/workforcePools/example-workforce-pool`  
Workload identity pool |  `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/WORKLOAD_POOL_ID` **Example:** `//iam.googleapis.com/projects/123456789012/locations/global/workloadIdentityPools/example-workload-pool`  
All [agent identities](https://docs.cloud.google.com/iam/docs/principals-overview#agent-identity) in a project's trust domain |  `PROJECT_TRUST_DOMAIN/attribute.container/projects/PROJECT_NUMBER` **Example:** `//agents.global.proj-9876543210.system.id.goog/attribute.container/projects/9876543210`  
Google Workspace domain |  `//iam.googleapis.com/locations/global/workspace/CUSTOMER_ID1` **Example:** `//iam.googleapis.com/locations/global/workspace/C01Abc35`  
Project's principal set |  `//cloudresourcemanager.googleapis.com/projects/PROJECT_ID` **Example:** `//cloudresourcemanager.googleapis.com/projects/example-project`  
Folder's principal set |  `//cloudresourcemanager.googleapis.com/folders/FOLDER_ID` **Example:** `//cloudresourcemanager.googleapis.com/folders/0123456789012`  
Organization's principal set |  `//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID` **Example:** `//cloudresourcemanager.googleapis.com/organizations/0123456789012`  
  
1[Learn how to find your Cloud Identity customer ID](https://support.google.com/cloudidentity/answer/10070793).

## Principal types for access policies

The following table describes the principal identifiers that you can use in access policies. You can use access policies to control access to Eventarc resources. For more information, see the [Eventarc documentation](https://docs.cloud.google.com/eventarc/advanced/docs/control-publishing-access).

Principal type | Identifier  
---|---  
User |  `principal://goog/subject/USER_EMAIL_ADDRESS` **Example:** `principal://goog/subject/alex@example.com`  
Service account |  `principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS` **Example:** `principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com`  
All service accounts in a project, folder, or organization |  `principalSet://cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_NUMBER/type/ServiceAccount` **Example for all service accounts in a project:** `principalSet://cloudresourcemanager.googleapis.com/projects/123456789012/type/ServiceAccount` **Example for all service accounts in all projects in a folder:** `principalSet://cloudresourcemanager.googleapis.com/folders/123456789012/type/ServiceAccount` **Example for all service accounts in all projects in an organization:** `principalSet://cloudresourcemanager.googleapis.com/organizations/123456789012/type/ServiceAccount` **Note** : Moving projects into or out of a folder or organization changes the service accounts included in this principal set. For example, if you move a project out of a folder or organization, then this principal set no longer includes that project's service accounts.   
Group |  `principalSet://goog/group/GROUP_EMAIL_ADDRESS` **Example:** `principalSet://goog/group/my-group@example.com`  
All principals1 | `principalSet://goog/public:all`  
All principals in a Cloud Identity account (domain) |  `principalSet://goog/cloudIdentityCustomerId/CLOUD_IDENTITY_CUSTOMER_ID1` **Example:** `principalSet://goog/cloudIdentityCustomerId/C01Abc35`  
  
1 This value can only be used in access policies with the `DENY` action.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
