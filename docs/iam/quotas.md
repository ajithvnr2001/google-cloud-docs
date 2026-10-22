---
url: https://docs.cloud.google.com/iam/quotas/
title: Quotas and limits \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:16.931204+00:00
---

# Quotas and limits  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Resources ](https://docs.cloud.google.com/iam/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the quotas and limits that apply to Identity and Access Management (IAM). Both quotas and limits can restrict the number of requests that you can send or the number of resources that you can create. Limits can also restrict a resource's attributes, such as the length of the resource's identifier.

If a quota is too low to meet your needs, you can use the Google Cloud console to [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) for your project. If the Google Cloud console does not let you request a change for a specific quota, [contact Google Cloud support](https://docs.cloud.google.com/support/docs).

Limits cannot be changed.

## Quotas

By default, the following IAM quotas apply to every Google Cloud project, with the exception of Workforce Identity Federation and Privileged Access Manager quotas. Workforce Identity Federation quotas apply to [organizations](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). 

Privileged Access Manager quotas are applicable on both projects and organizations, and are charged as follows depending on the target of the call: 

  * For projects that don't belong to an organization, one unit of project quota is charged for a call.
  * For projects belonging to an organization, one unit each of project and organization quotas are charged for a call. A call is denied if either of the two quotas has been exhausted.
  * For calls to folders or organizations, one unit of organization quota is charged.

Default quotas  
---  
IAM v1 API  
Read requests (for example, listing custom roles) | 6,000 per project per minute  
Write requests (for example, creating a new custom role) | 600 per project per minute  
IAM v2 API  
Read requests (for example, getting a deny policy) | 5 per project per minute  
Write requests (for example, updating a deny policy) | 5 per project per minute  
IAM v3 API  
Read requests (for example, getting a Principal Access Boundary policy) | 5 per project per minute  
Write requests (for example, updating a Principal Access Boundary policy) | 5 per project per minute  
Workload Identity Federation  
Read requests (for example, getting a workload identity pool) | 600 per project per minute  
6,000 per client per minute  
Write requests (for example, updating a workload identity pool) | 60 per project per minute  
600 per client per minute  
Workforce Identity Federation  
Create/delete/undelete requests | 60 per organization per minute  
Read requests (for example, getting a workforce identity pool) | 120 per organization per minute  
Update requests (for example, updating a workforce identity pool) | 120 per organization per minute  
Subject delete/undelete requests (for example, deleting a workforce identity pool subject) | 60 per organization per minute  
Number of workforce identity pools | 100 per organization  
Workforce OAuth applications  
Create/read/update/delete/undelete requests | 60 per project per minute  
Cloud OAuth API  
Token exchange requests (`cloudoauth.googleapis.com/exchange_token_requests`) | 1,000 per organization per minute  
User info requests (`cloudoauth.googleapis.com/fetch_user_info_requests`) | 1,000 per organization per minute  
Enterprise groups requests (`cloudoauth.googleapis.com/fetch_groups_requests`) | 1,000 per organization per minute  
IAM SCIM API  
Create/read/update/delete/patch requests to SCIM endpoints |  3,000 per SCIM tenant per organization per minute   
Service Account Credentials API  
Requests to generate credentials | 60,000 per project per minute  
Requests to sign a JSON Web Token (JWT) or blob | 60,000 per project per minute  
Security Token Service API  
Exchange token global requests (not Workforce Identity Federation) | 6,000 per project per minute  
Exchange token regional requests (not Workforce Identity Federation) | 6,000 per project per region per minute  
Exchange token requests (Workforce Identity Federation) | 1,000 per organization per minute  
Intermediary token exchange global requests | 3,000 per project per minute  
Intermediary token exchange regional requests | 3,000 per project per region per minute  
Token introspection global requests | 6,000 per project per minute  
Token introspection regional requests | 6,000 per project per region per minute  
Service accounts  
Number of service accounts |  Varies depending on the project. To view the quota for a project, [enable the IAM API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com), then [view your project's quotas in the Google Cloud console](https://docs.cloud.google.com/docs/quotas/view-manage#viewing_your_quota_console) and search for **Service Account Count**.  
`CreateServiceAccount` requests |  Varies depending on the project. To view the quota for a project, [enable the IAM API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com), then [view your project's quotas in the Google Cloud console](https://docs.cloud.google.com/docs/quotas/view-manage#viewing_your_quota_console) and search for **Create Service Account requests by credential per minute**.   
Privileged Access Manager API  
Entitlement write requests (for example, creating, updating, or deleting an entitlement) | 100 per project per minute  
100 per organization per minute   
`CheckOnboardingStatus` requests | 300 per project per minute  
900 per organization per minute   
`ListEntitlements` requests | 600 per project per minute  
1800 per organization per minute   
`SearchEntitlements` requests | 600 per project per minute  
1800 per organization per minute   
`GetEntitlement` requests | 3000 per project per minute  
9000 per organization per minute   
`ListGrants` requests | 600 per project per minute  
1800 per organization per minute   
`SearchGrants` requests | 600 per project per minute  
1800 per organization per minute   
`GetGrant` requests | 3000 per project per minute  
9000 per organization per minute   
`CreateGrant` requests | 200 per project per minute  
600 per organization per minute   
`ApproveGrant` requests | 200 per project per minute  
600 per organization per minute   
`DenyGrant` requests | 200 per project per minute  
600 per organization per minute   
`RevokeGrant` requests | 300 per project per minute  
900 per organization per minute   
`GetOperation` requests | 600 per project per minute  
1800 per organization per minute   
`ListOperations` requests | 300 per project per minute  
900 per organization per minute   
  
## Limits

IAM enforces the following limits on resources. These limits cannot be changed.

Limits  
---  
Custom roles  
Custom roles for an organization1 | 300  
Custom roles for a project1 | 300  
ID of a custom role | 64 bytes  
Title of a custom role | 100 bytes  
Description of a custom role | 300 bytes  
Permissions in a custom role | 3,000  
Total size of the title, description, and permission names for a custom role  | 64 KB  
Allow policies and role bindings  
Allow policies per resource | 1  
Total number of principals (including domains and Google groups) in all role bindings and [audit-logging exemptions](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-exempt) within a single policy2 | 1,500  
Domains and Google groups in all role bindings within a single allow policy3 | 250  
Logic operators in a role binding's condition expression | 12  
Role bindings in an allow policy that include the same role and the same principal, but different condition expressions  | 20  
Deny policies and deny rules  
Deny policies per resource | 500  
Deny rules per resource | 500  
Domains and Google groups in all of a resource's deny policies 4 | 500  
Total number of principals (including domains and Google groups) in all of a resource's deny policies 4 | 2500  
Deny rules in a single deny policy | 500  
Logic operators in a deny rule's condition expression | 12  
Principal Access Boundary policies  
Rules in a single Principal Access Boundary policy | 500  
Resources in all rules in a single Principal Access Boundary policy | 500  
Number of Principal Access Boundary policies that can be bound to a resource  | 10  
Principal Access Boundary policies per organization | 1000  
Logic operators in a policy binding's condition expression | 10  
Access policies  
Number of access policies that can be bound to a resource  | 5  
Number of resources that you can bind a single access policy to  | 5  
Service accounts  
Service account ID | 30 bytes  
Service account display name | 100 bytes  
Service account keys for a service account | 10  
Workforce Identity Federation  
Workforce identity pool providers per pool | 200  
Deleted workforce identity pool subjects per pool | 100,000  
Workforce OAuth applications  
Workforce OAuth clients per project | 100  
Workforce OAuth client credentials per client | 10  
Workload Identity Federation and Workforce Identity Federation attribute mapping  
Mapped subject | 127 bytes  
Mapped workforce identity pool user display name | 100 bytes  
Mapped attributes total size | 8,192 bytes  
Number of custom attribute mappings | 50  
Short-lived credentials  
Access boundary rules in a [Credential Access Boundary](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials) |  10   
Maximum lifetime of an access token 5 |  3,600 seconds (1 hour)   
  
1 If you create custom roles at the project level, those custom roles don't count towards the limit at the organization level.

2 For the purposes of this limit, IAM counts _all_ appearances of each principal in the allow policy's role bindings, as well as the principals that the allow policy [exempts from Data Access audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-exempt). It does _not_ deduplicate principals that appear in more than one role binding. For example, if an allow policy contains only role bindings for the principal `user:my-user@example.com`, and this principal appears in 50 role bindings, then you can add another 1,450 principals to the role bindings in the allow policy. 

Also, for the purposes of this limit, each appearance of a domain or Google group is counted as a single principal, regardless of the number of individual members in the domain or group. 

If you use IAM Conditions, or if you grant roles to many principals with unusually long identifiers, then IAM might allow fewer principals in the allow policy. 

3 For the purposes of this limit, Cloud Identity domains, Google Workspace accounts, and Google groups are counted as follows: 

  * For Google groups, each unique group is counted only once, regardless of how many times the group appears in the allow policy. This is different from how groups are counted for the limit on the total number of principals in an allow policy—for that limit, each appearance of a group counts towards the limit. 
  * For Cloud Identity domains or Google Workspace accounts, IAM counts _all_ appearances of each domain or account in the allow policy's role bindings. It does _not_ deduplicate domains or accounts that appear in more than one role binding. 



For example, if your allow policy contains only one group, `group:my-group@example.com`, and the group appears in the allow policy 10 times, then you can add another 249 Cloud Identity domains, Google Workspace accounts, or unique groups before you reach the limit. 

Alternatively, if your allow policy contains only one domain, `domain:example.com`, and the domain appears in the allow policy 10 times, then you can add another 240 Cloud Identity domains, Google Workspace accounts, or unique groups before you reach the limit. 

4 IAM counts _all_ appearances of each principal in all of the deny policies attached to a resource. It does _not_ deduplicate principals that appear in more than one deny rule or deny policy. For example, if the deny policies attached to a resource contain only deny rules for the principal `user:my-user@example.com`, and this principal appears in 20 deny rules, then you could add another 2,480 principals to the resource's deny policies. 

5 For OAuth 2.0 access tokens, you can extend the maximum lifetime to 12 hours (43,200 seconds). To extend the maximum lifetime, identify the service accounts that need an extended lifetime for tokens, then [add these service accounts to an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#setting_a_list_constraint) that includes the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` list constraint.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
