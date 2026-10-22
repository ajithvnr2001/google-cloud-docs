---
url: https://docs.cloud.google.com/iam/docs/pam-overview/
title: Privileged Access Manager overview \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:36.116290+00:00
---

# Privileged Access Manager overview  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Privileged Access Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

You can use Privileged Access Manager (PAM) to control just-in-time temporary privilege elevation for select principals, and to [view audit logs](https://docs.cloud.google.com/iam/docs/pam-audit-entitlement-events) afterwards to find out who had access to what and when.

To allow temporary elevation, you [create an _entitlement_](https://docs.cloud.google.com/iam/docs/pam-create-entitlements) in Privileged Access Manager, and add the following attributes to it:

  * A set of principals who are allowed to request a grant against the entitlement.

  * Whether a justification is required for that grant.

  * A set of [roles](https://docs.cloud.google.com/iam/docs/roles-overview) to temporarily grant. [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) can be set on the roles.

  * The maximum duration a grant can last.

  * Optional: Whether requests need [approval from a select set of principals](https://docs.cloud.google.com/iam/docs/pam-approve-deny-grants), and whether those principals need to justify their approval.

  * Optional: Additional stakeholders to be notified about important events, such as grants and pending approvals.




A principal that's been added as a requester to an entitlement can [request a grant against that entitlement](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access). If successful, they are granted the roles listed in the entitlement until the end of the grant duration, after which the roles are revoked by Privileged Access Manager.

## Use cases

To effectively use Privileged Access Manager, start by identifying specific use cases and scenarios where it can address your organization's needs. Tailor your Privileged Access Manager entitlements based on these use cases and necessary requirements and controls. This involves mapping out the users, roles, resources, and durations involved, along with any necessary justifications and approvals.

While Privileged Access Manager can be used as a general best practice to grant temporary rather than permanent privileges, here are some scenarios where it may be commonly used:

  * **Grant emergency access** : Allow select emergency responders to perform critical tasks without having to wait for approval. You can require justifications for emergency access requests for additional context.

  * **Control access to sensitive resources** : Tightly control access to sensitive resources, requiring approvals and business justifications. Privileged Access Manager can also be used to audit how this access was used—for example, when granted roles were active for a user, which resources were accessible during that time, the justification for access, and who approved it.

For example, you can use Privileged Access Manager to do the following:

    * Give developers temporary access to production environments for troubleshooting or deployments.

    * Give support engineers access to sensitive customer data for specific tasks.

    * Give database administrators elevated privileges for maintenance or configuration changes.

  * **Implement granular least privilege** : Assigning administrative roles or broad access to all users can increase the attack surface. To prevent this, administrators can assign least privilege permanent roles and use Privileged Access Manager to provide temporary, time-bound elevated access for specific tasks when needed. Administrators can create entitlements with tag-based conditions and enforce requesters to create grant requests with customized scope and withdraw grants after the task is completed. This significantly reduces opportunities for misuse and reinforces the principle of "just-in-time" access.

  * **Automate privileged access approvals** : To enhance efficiency, you can configure service accounts or agent identities as approvers within your DevOps pipelines. These accounts can automate programmatic approvals by validating tickets directly from ITSM systems, thereby eliminating slow manual checks.

  * **Help secure service accounts and agent identities** : Instead of permanently granting roles to service accounts or agent identities, allow them to self-elevate and assume roles only when needed for automated tasks.

  * **Mitigate insider threats and accidental misuse** : With multi-party approvals, you can require a second approver for grant requests. This approach reduces the risk of a single administrator or a compromised account approving malicious access.

  * **Manage access for contractors and extended workforce** : Grant contractors or members of the extended workforce temporary, time-bound access to resources, with approvals and justifications required.

  * **Transition permanent roles to temporary access** : Remediate excessive permissions identified by [IAM recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). Instead of permanently revoking a role, you can shift it to a temporary, on-demand entitlement. For more information, see [Remediate excessive permissions with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations).




## Capabilities and limitations

The following sections describe the different capabilities and limitations of Privileged Access Manager.

### Supported resources

Privileged Access Manager supports creating entitlements and requesting grants for projects, folders, and organizations.

If you want to limit access to a subset of resources within a project, folder, or organization, you can add [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to the entitlement. Privileged Access Manager supports all condition attributes that are supported in allow policy role bindings. Privileged Access Manager only supports services that support granular access through IAM because it uses IAM conditions to manage temporary access.

### Supported roles

Privileged Access Manager supports [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined), [custom roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom), and the Admin, Writer, and Reader [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic). Privileged Access Manager doesn't support [legacy basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic) (Owner, Editor, and Viewer).

### Supported identities

Privileged Access Manager supports all types of identities, including [Cloud Identity](https://docs.cloud.google.com/identity/docs), [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), and [agent identities](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1).

### Audit logging

Privileged Access Manager events, such as creation of entitlements, requisition or review of grants, are logged to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). For a complete list of events that Privileged Access Manager generates logs for, see the [Privileged Access Manager audit logging documentation](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-pam). To learn how to view these logs, see [Audit entitlement and grant events in Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-audit-entitlement-events).

### Multi-level and multi-party approvals

**Preview — Multi-level and multi-party approvals**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is available with either the [Enterprise or Premium tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) of Security Command Center. 

Privileged Access Manager administrators can set up multi-level and multi-party approvals. This is useful for use cases that involve the following:

  * High-risk operations such as modifying critical infrastructure or accessing sensitive data
  * Enforcing the separation of duties
  * Automating multi-level approval processes in dynamic workflows using service accounts or agent identities as intelligent approvers



With this feature, Privileged Access Manager administrators can mandate more than one approval level per entitlement, allowing up to two levels of sequential approvals for each entitlement. Administrators can mandate up to five approvals per level. For more information, see [Create entitlements](https://docs.cloud.google.com/iam/docs/pam-create-entitlements).

### Scope customization

**Preview — Scope customization**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is available with either the [Enterprise or Premium tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) of Security Command Center. 

Requesters can customize the scope of their grant requests to include only the specific roles and resources that they need within the scope of their entitlement. For more information, see [Request temporary elevated access](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access).

### Service account and agent identity approvals

**Preview — Service account and agent identity approvals**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Privileged Access Manager administrators can enable service accounts and agent identities as eligible approvers. This lets administrators add service accounts, agent identities, and [identities in workload identity pools](https://docs.cloud.google.com/iam/docs/workload-identity-federation) as approvers when creating or modifying entitlements. For more information, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

### Inheritance support

**Preview — Inheritance support**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Entitlements and grants that are set up at the organization- or folder-level are visible from their descendent folders and projects in the Google Cloud console. Requesters can request access to the child resources based on those entitlements directly within those child resources. For more information, see [Request temporary elevated access with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access).

### Notification preferences customization

**Preview — Notification preferences customization**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Privileged Access Manager settings administrators can customize resource-wide notification preferences for various Privileged Access Manager events. These settings let administrators selectively disable notifications for specific events and specific personas, or disable all notifications. For more information, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

### Grant scheduling

**Preview — Grant scheduling**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Requesters can schedule grant requests up to seven days in advance. This helps requesters align access with planned maintenance or on-call shifts and reduces the time they spend waiting for approvals. For more information, see [Request temporary elevated access](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access).

### Grant withdrawal

**Preview — Grant withdrawal**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Requesters can withdraw grant requests that are pending approval or scheduled for activation. Requesters can also end their active grants when their privileged task is complete or when the access is no longer required. Organizations can recommend this as a best practice to limit the duration of privileged access to only the time it's actively needed. For more information, see [Withdraw grants](https://docs.cloud.google.com/iam/docs/pam-withdraw-grants).

### Grant retention

Grants are automatically deleted from Privileged Access Manager 30 days after they are denied, revoked, withdrawn, expired, or ended. Logs for grants are kept in Cloud Audit Logs for the [log retention duration of the `_Required` bucket](https://docs.cloud.google.com/logging/quotas#logs_retention_periods). To learn how to view these logs, see [Audit entitlement and grant events in Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-audit-entitlement-events).

### Privileged Access Manager and IAM policy modifications

Privileged Access Manager manages temporary access by adding and removing [role bindings](https://docs.cloud.google.com/iam/docs/allow-policies#structure) from resources' IAM allow policies. These role bindings use time-based [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to help ensure that access is temporary. Consequently, the activation and revocation of temporary access depend on standard [access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

If these role bindings are modified by something other than Privileged Access Manager, then Privileged Access Manager might not work as expected.

To avoid this issue, we recommend doing the following:

  * Don't manually modify role bindings that are managed by Privileged Access Manager.
  * If you use [Terraform](https://www.terraform.io/) to manage your IAM policies, ensure that you're using [non-authoritative resources](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam) instead of authoritative resources. This helps ensure that Terraform won't override Privileged Access Manager role bindings, even if they aren't in the declarative IAM policy configuration.



## Notifications

Privileged Access Manager can notify you about various events happening in Privileged Access Manager as described in the following sections.

### Email notifications

Privileged Access Manager sends email notifications to the relevant stakeholders for an entitlement and grant changes. The sets of recipients are as follows:

  * **Eligible requesters of an entitlement** :

    * Email addresses of Cloud Identity users and [groups](https://docs.cloud.google.com/identity/docs/groups) specified as requesters in the entitlement.
    * Manually configured email addresses in the entitlement: When using Google Cloud console, these email addresses are listed in the **Requester email recipients** field in the **Add requesters** section. When using the gcloud CLI or the REST API, these email addresses are listed in the `requesterEmailRecipients` field.
  * **Grant approvers for an entitlement** :

    * Email addresses of Cloud Identity users and groups specified as approvers in the approval level.
    * Manually configured email addresses in the entitlement: When using the Google Cloud console, these email addresses are listed in the **Approval email recipients** field in the **Add approvers** section. When using the gcloud CLI or the REST API, these email addresses are listed in the `approverEmailRecipients` field of the approval workflow steps.
  * **Administrator of the entitlement** :

    * Manually configured email addresses in the entitlement: When using the Google Cloud console, these email addresses are listed in the **Admin email recipients** field in the **Entitlement details** section. When using the gcloud CLI or the REST API, these email addresses are listed in the `adminEmailRecipients` field.
  * **Requester of a grant** :

    * Email address of the grant requester if they are a Cloud Identity user.
    * Additional email addresses added by the requester while requesting the grant: When using Google Cloud console, these email addresses are listed in the **Additional email address(es)** field. When using gcloud CLI or the REST API, these email addresses are listed in the `additionalEmailRecipients` field.



Privileged Access Manager sends emails to these email addresses for the following events:

Recipients | Event  
---|---  
Eligible requesters of an entitlement | When the entitlement is assigned and available for use to the requester  
Grant approvers for an entitlement | When a grant is requested and it requires approval  
Requester of a grant | 

  * When the grant is successfully activated or fails to be activated
  * When the grant ends
  * When the grant is denied
  * When the grant expires (it was not approved or denied within 24 hours or by the scheduled activation time)
  * When the grant is revoked

  
Administrator of the entitlement | 

  * When the grant is successfully activated or fails to be activated
  * When the grant ends

  
  
### Pub/Sub notifications

Privileged Access Manager is integrated with [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview). You can use [Cloud Asset Inventory feeds](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes) feature to receive notifications about all grant changes through Pub/Sub. The asset type to use for grants is `privilegedaccessmanager.googleapis.com/Grant`.

## What's next

  * [Privileged Access Manager permissions and setup](https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
