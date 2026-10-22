---
url: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations/
title: Secure enterprise foundation controls \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:40.162653+00:00
---

# Secure enterprise foundation controls  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Secure enterprise foundation controls Stay organized with collections  Save and categorize content based on your preferences. 

This document includes the best practices and guidelines for building a secure enterprise foundation when running workloads that use Google Cloud. A secure enterprise foundation includes controls for the following:

  * Authentication and authorization
  * Organization
  * Networking
  * Logging, monitoring, and alerting
  * Key and secret management
  * Security posture and analytics



## Authentication and authorization

This section includes the best practices and guidelines for Identity and Access Management (IAM) and Cloud Identity when running workloads on Google Cloud.

### Disable automatic IAM grants for default service accounts

Google control ID | IAM-CO-4.1  
---|---  
Implementation | Required  
Description | Use the `automaticIamGrantsForDefaultServiceAccounts` boolean constraint to disable automatic role grants when Google Cloud services automatically create default service accounts with overly permissive roles.By default, some systems grant overly broad permissions to automated accounts, which is a potential security risk. For example, if you don't enforce this constraint and you create a default service account, the service account is automatically granted the Editor role (`roles/editor`) on your project. If an attacker compromises a single part of the system, they could gain control over the entire project. This constraint disables those automatic, high-level permissions, forcing a more secure, deliberate approach where only the minimal necessary permissions are granted.  
Applicable products | 

  * IAM
  * Organization Policy Service

  
Path | `constraints/iam.automaticIamGrantsForDefaultServiceAccounts`  
Operator | Is  
Value |  `False`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Types of service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default)

  
  
### Block the creation of external service account keys

Google control ID | IAM-CO-4.2  
---|---  
Implementation | Required  
Description | Use the `iam.disableServiceAccountKeyCreation` boolean constraint to disable external service account keys from being created. This constraint lets you control the use of unmanaged long-term credentials for service accounts. When this constraint is set, you can't create user-managed credentials for service accounts in projects that are affected by the constraint.  
Applicable products | 

  * Organization Policy Service
  * IAM

  
Path | `constraints/iam.disableServiceAccountKeyCreation`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Disable service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation)

  
  
### Block service account key uploads

Google control ID | IAM-CO-4.3  
---|---  
Implementation | Required  
Description | Use the `iam.disableServiceAccountKeyUpload` boolean constraint to disable the upload of external public keys to service accounts. When this constraint is set, users can't upload public keys to service accounts in projects affected by the constraint.  
Applicable products | 

  * Organization Policy Service
  * IAM

  
Path | `constraints/iam.disableServiceAccountKeyUpload`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Disable service account key upload](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_upload_managed)

  
  
### Configure separation of duties for organization policy administrators

Google control ID | OPS-CO-6.1  
---|---  
Implementation | Required  
Description | Assign the Organization Policy Administrator (`roles/orgpolicy.policyAdmin`) role to groups that are accountable for the security posture of the Google Cloud organization. To avoid resource creation that violates security policy, don't assign this role to project owners.  
Applicable products | 

  * IAM
  * Organization Policy Service

  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-5

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.DS-5.1
  * PR.PT-3.1

  
Related information | 

  * [Creating and managing organization resources](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization)
  * [Determine which principals have certain roles or permissions](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#principal-query-all)

  
  
### Enable two-step verification for super admin accounts

Google control ID | CI-CO-6.1  
---|---  
Implementation | Required  
Description | Google recommends Titan Security Keys for 2-step verification (2SV) for super admin accounts. However, for use cases where this isn't possible, we recommend using another security key as an alternative.  
Applicable products | 

  * Cloud Identity
  * Titan Security Keys

  
Related NIST-800-53 controls | 

  * IA-2
  * IA-4
  * IA-5
  * IA-7

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Related information | 

  * [Deploy 2-Step Verification](https://support.google.com/cloudidentity/answer/9176657)

  
  
### Enforce two-step verification on the super admin organization unit

Google control ID | CI-CO-6.2  
---|---  
Implementation | Required  
Description | Enforce 2-step verification (2SV) for a specific organization unit (OU) or the entire organization. We recommend that you create an OU for super admins and enforce 2SV on that OU.  
Applicable products |  Cloud Identity  
Related NIST-800-53 controls | 

  * IA-2
  * IA-4
  * IA-5
  * IA-7

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Related information | 

  * [Add an organizational unit](https://support.google.com/cloudidentity/answer/182537)
  * [Move users to an organizational unit](https://support.google.com/cloudidentity/answer/182449)

  
  
### Create an exclusive email address for the primary super admin

Google control ID | CI-CO-6.4  
---|---  
Implementation | Required  
Description | Create an email address that's not specific to a particular user as the primary Cloud Identity super admin account.  
Applicable products |  Cloud Identity  
Related NIST-800-53 controls | 

  * IA-2
  * IA-4
  * IA-5

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Related information | 

  * [Create Cloud Identity user accounts](https://support.google.com/cloudidentity/answer/7332836)

  
  
### Create redundant administrator accounts

Google control ID | CI-CO-6.7  
---|---  
Implementation | Required  
Description | Don't have a single super admin or Organization Administrator. Create one or more (up to 20) backup administrator accounts. A single super admin or Organization Administrator can result in lockout scenarios. This situation also carries a higher risk as one person can make platform-altering changes, potentially with no oversight.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * IA-2
  * IA-4
  * IA-5

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Related information | 

  * [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373)
  * [Setting up your organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#setting-up)

  
  
### Use Privileged Access Manager

Google control ID | GCVE-CO-3.2  
---|---  
Implementation | Required  
Description | Use Privileged Access Manager for managing privileged access. For all other access, use access groups, let group memberships expire automatically, and implement an approval workflow for group memberships.Using the least privilege model lets you only provide access when needed, for the resources that are needed. Using pre-built roles simplifies use and reduces sprawl caused by custom roles so that you don't have to worry about managing the role lifecycle.  
Applicable products |  Identity and Access Management (IAM)  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1

  
Related information | 

  * [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview)

  
  
### Define the identity source of truth

Implementation | Required  
---|---  
Description | Decide on your source of truth for provisioning managed user identities. Patterns include creating user identities in Cloud Identity, syncing identities from an existing identity provider, or using Workforce Identity Federation.  
Applicable products | 

  * Cloud Identity
  * Workforce Identity Federation

  
Related NIST-800-53 controls | 

  * AC-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Decide how to onboard identities to Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities)

  
  
### Enforce strong password policies

Implementation | Required  
---|---  
Description | Enforce strong and unique passwords for all user accounts. Consider using a password manager. Weak or no credentials are a common pattern that malicious users can easily exploit.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * IA-5

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Enforce and monitor password requirements for users](https://support.google.com/a/answer/139399)
  * [Enable, disable, and use password policies](https://docs.cloud.google.com/identity-platform/docs/password-policy)

  
  
### Use roles based on job functions

Implementation | Required  
---|---  
Description | Use Identity and Access Management (IAM) roles that are based on job functions to assign permissions to users. Job functions are predefined roles that allow admins to provide a set of permissions that is limited to a job function, thus improving productivity and reducing the back-and-forth of asking for permissions. To better align with your organization's requirements, you can create custom roles based on predefined roles.  
Applicable products |  IAM  
Related NIST-800-53 controls | 

  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1

  
Related information | 

  * [Predefined roles for job functions](https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions)

  
  
### Restrict external members in groups

Implementation | Required  
---|---  
Description | Set organization-wide policies to prevent adding external members to Google Groups. By default, external user accounts can be added to groups in Cloud Identity. We recommend that you configure sharing settings so that group owners can't add external members. Note that this restriction doesn't apply to the super admin account or to other delegated administrators with Google Groups admin permissions. Because federation from your identity provider runs with administrator privileges, the group sharing settings don't apply to this group synchronization. We recommend that you review controls in the identity provider and synchronization mechanism to ensure that non-domain members aren't added to groups, or that you apply group restrictions.  
Applicable products | 

  * Cloud Identity
  * Google Workspace

  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-5.1

  
Related information | 

  * [Set organization-wide policies for using groups](https://support.google.com/a/answer/167097#zippy=%2Ckeep-your-organizations-groups-completely-private)
  * [Restrict group membership](https://support.google.com/a/answer/11192679)

  
  
### Set daily session length

Implementation | Required  
---|---  
Description | Set the session length for Google Cloud services to expire at least once a day. Leaving an account signed in for an extended period is a security risk. Enforcing a maximum session duration automatically ends the session after a set time, forcing a new, secure sign-in.This practice reduces the opportunity for a malicious user to use a stolen password and ensures access is regularly reverified. For new customers, a default session length of 16 hours is automatically enforced. Customers who created their Google Cloud organization before 2023 might have a default setting to never require reauthentication. Review this setting to ensure that you have a reauthentication policy with a session length that is between 1 and 24 hours. The reauthentication policy invalidates the refresh token and forces the user to regularly reauthenticate the gcloud CLI with their password or security key.The session length for Google Cloud services is a distinct setting from session length for Google services, which controls web sessions for sign-in across Google Workspace services but doesn't control reauthentication for the Google Cloud. If you use Google Workspace services, set the session length for both.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * AC-12

  
Related CRI profile controls | 

  * PR.AC-7.1

  
Related information | 

  * [Set session length for Google Cloud services](https://support.google.com/a/answer/9368756)
  * [Set session length for Google services](https://support.google.com/a/answer/7576830)

  
  
### Remediate unmanaged consumer accounts

Implementation | Required  
---|---  
Description | Don't permit unmanaged consumer accounts. Consolidate any unmanaged consumer accounts, and consider a solution to prevent the creation of further unmanaged consumer accounts with your domain. Unmanaged consumer accounts are not governed by your joiner-mover-leaver (JML) processes, so they introduce the risk that an employee still has access to your resources after they leave their job. These accounts are also treated as external with regard to controls like domain restricted sharing.  
Applicable products |  Cloud Identity  
Related NIST-800-53 controls | 

  * AC-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Overview of consolidating accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts)
  * [Use the transfer tool to migrate unmanaged users](https://support.google.com/a/answer/6178640)

  
  
### Enforce dedicated admins and multiparty approval

Implementation | Required  
---|---  
Description | Ensure that super admin accounts are separate from day-to-day user accounts. Super admin accounts must be dedicated accounts that are used only when making critical changes. For increased security, turn on multiparty approval for admin actions. Turning on multiparty approval means sensitive actions are approved by two administrators, which helps prevent attackers from compromising an admin account and lock out other admin users.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1

  
Related information | 

  * [Multi-party approval for sensitive actions](https://support.google.com/a/answer/13790448)
  * [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373)
  * [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices)

  
  
### Enable multi-factor authentication for all Google Accounts and Cloud Identity users

Google control ID | CI-CO-6.1  
---|---  
Implementation | Required  
Description | Enable multi-factor authentication (MFA), also known as 2-step authentication (2SV) for all Google Accounts and Cloud Identity users, not just super admins. MFA for super admins is enabled by default. MFA adds another layer of defense because passwords alone often aren't a strong enough security measure.To help prevent phishing attacks that can lead to cryptocurrency mining attacks, use Titan Security Keys.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * IA-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Protect your business with 2-Step Verification](https://support.google.com/a/answer/175197)
  * [Multi-factor authentication requirement for Google Cloud](https://docs.cloud.google.com/docs/authentication/mfa-requirement)
  * [Titan Security Keys](https://cloud.google.com/security/products/titan-security-key)

  
  
### Revoke default creator roles

Implementation | Required  
---|---  
Description | Remove the domain-wide Project Creator and Billing Account Creator roles that are granted by default to all members in a new organization. New organizations grant the Project Creator and Billing Account Creator roles to all managed user identities in the domain. While these roles are useful for getting started, this configuration isn't intended for production environments. Letting billing accounts proliferate leads to increased administrative overhead and has technical consequences when splitting services across multiple Billing Accounts. Allowing free-form project creation can lead to projects that don't adhere to your governance conventions. Instead, remove these roles and establish a project creation process to request new projects and associate them with billing.  
Applicable products |  IAM  
Path | `resourcemanager.organizations/iamPolicy.bindings`  
Operator | not_contains  
Value | 

  * `role:roles/resourcemanager.projectCreator AND member:domain:*`
  * `role:roles/billing.creator AND member:domain:*`

  
Type | String  
Related NIST-800-53 controls | 

  * AC-6

  
Related CRI profile controls | 

  * PR.AC-4.1

  
Related information | 

  * [Managing default organization roles](https://docs.cloud.google.com/resource-manager/docs/default-access-control)

  
  
### Rotate service account keys

Implementation | Required  
---|---  
Description | If you must use service account keys, rotate the keys at least once every 90 days.A rotation interval limits how long an attacker can have access to the system. Without a rotation interval, the attacker has access forever. Where possible, consider using Workload Identity Federation instead of service account keys.  
Applicable products |  IAM  
Path | `constraints/iam.serviceAccountKeyExpiryHours`  
Operator | <=  
Value |  `2160`  
Type | String  
Related NIST-800-53 controls | 

  * SC-12

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)
  * [Choose the right authentication method for your use case](https://docs.cloud.google.com/docs/authentication#auth-decision-tree)

  
  
### Use Workload Identity Federation

Implementation | Required  
---|---  
Description | Use Workload Identity Federation to let CI/CD systems and workloads running on other clouds authenticate to Google Cloud. Workload Identity Federation lets workloads that run outside of Google Cloud authenticate without requiring a service account key. By avoiding service account keys and other long-lived credentials, Workload Identity Federation can help you reduce the risk of credential leakage.  
Applicable products |  IAM  
Path | `iam.googleapis.com/WorkloadIdentityPool`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * IA-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

  
  
### Block account self-recovery for super admin accounts

Google control ID | CI-CO-6.3  
---|---  
Implementation | Required  
Description | By default, super admin account self-recovery is off for new customers. However, existing customers might have this setting on. Turning this setting off helps to mitigate the risk that a compromised phone, a compromised email, or a social engineering attack might let an attacker gain super admin privileges over your environment. Plan an internal process for a super admin to contact another super admin in your organization if they have lost access to their account, and ensure that all super admins are familiar with the process for support-assisted recovery. To turn off the feature, go to the account recovery settings in the Google Admin console.  
Applicable products | 

  * Cloud Identity
  * Google Workspace

  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-4.1

  
Related information | 

  * [Manage a user's security settings](https://support.google.com/cloudidentity/answer/2537800)
  * [Recovering administrator access to your account](https://support.google.com/a/answer/33561)

  
  
### Set idle session timeout for sensitive use cases

Implementation | Required  
---|---  
Description | Set the idle session timeout to 15 minutes for sensitive use cases. Idle sessions might be used by attackers for credential theft.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * AC-12

  
Related CRI profile controls | 

  * PR.AC-7.1

  
Related information | 

  * [Set session length for Google services](https://support.google.com/a/answer/7576830)

  
  
### Enforce hardware security keys for administrators

Implementation | Required  
---|---  
Description | Provide hardware security keys, if possible, to super admins or Organization Administrators as a second factor. Super admin accounts are the highest-value targets for sophisticated attacks. Hardware security keys provide a high level of protection because they are phishing-resistant. Hardware security keys are the strongest possible defense against account takeover for your most critical administrators and build on your standard MFA policy.  
Applicable products | 

  * Identity and Access Management (IAM)
  * Google Workspace
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * IA-2

  
Related CRI profile controls | 

  * PR.AC-1.1

  
Related information | 

  * [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373)
  * [Use a security key for 2-Step Verification](https://support.google.com/accounts/answer/6103523)

  
  
### Enable post-SSO verification

Implementation | Required  
---|---  
Description | If you're using an external identity provider, set up post-SSO verification. Enable an additional layer of control based on Google's sign-in risk analysis. After you apply this setting, users might see additional risk-based login challenges at sign-in if Google determines that a user sign-in is suspicious.  
Applicable products | 

  * Cloud Identity
  * Google Workspace

  
Related NIST-800-53 controls | 

  * IA-2
  * IA-5
  * IA-8

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-3.1
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Related information | 

  * [Enable login challenges with SSO](https://support.google.com/a/answer/6002699#ssochallenges&zippy=%2Cset-up-post-sso-verification)

  
  
### Enable principal access boundary policies

Implementation | Required  
---|---  
Description | Enable principal access boundary (PAB) policies to limit principal access and help protect against phishing and data exfiltration. Enable a PAB policy for the organization to avoid external phishing attacks. PABs improve security by reducing the extent of an attack with a compromised identity, and they also help prevent any external phishing attacks and other exfiltration attacks.  
Applicable products |  IAM  
Path | `iam.googleapis.com/PrincipalAccessBoundaryPolicy`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * AC-3

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)

  
  
### Deactivate accounts and reset permissions when offboarding

Implementation | Required  
---|---  
Description | Ensure that your offboarding procedures include processes to deactivate accounts and reset permissions when employees leave your organization or change roles.  
Applicable products |  Cloud Identity  
Related NIST-800-53 controls | 

  * AC-2
  * PS-4
  * PS-5
  * AC-6
  * IA-4

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.IP-11.1
  * PR.IP-11.2
  * PR.AC-4.1
  * PR.AC-6.1

  
Related information | 

  * [Revoking access to Google Cloud](https://docs.cloud.google.com/docs/security/data-loss-prevention/revoking-user-access)

  
  
### Implement tags to efficiently assign IAM policies and organization policies

Google control ID | IAM-CO-6.1  
---|---  
Implementation | Recommended  
Description | Tags provide a way to create annotations for resources, and in some cases conditionally allow or deny policies based on whether a resource has a specific tag. Use tags and conditional policy enforcement for fine-grained control across your resource hierarchy.  
Applicable products |  Resource Manager  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-5

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.DS-5.1
  * PR.PT-3.1

  
Related information | 

  * [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)

  
  
### Audit high-risk changes to IAM

Google control ID | IAM-CO-7.1  
---|---  
Implementation | Recommended  
Description | Use Cloud Audit Logs to monitor for high-risk activity, such as accounts being granted high-risk roles like Organization Admin and Super Admin. Set up alerts for this type of activity.  
Applicable products |  Cloud Audit Logs  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Identity and Access Management audit logging](https://docs.cloud.google.com/iam/docs/audit-logging)
  * [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit)

  
  
### Block access to Cloud Shell for Cloud Identity managed user accounts

Google control ID | CI-CO-6.8  
---|---  
Implementation | Recommended  
Description | To avoid granting excessive access to Google Cloud, block access to Cloud Shell for Cloud Identity managed user accounts.  
Applicable products | 

  * Cloud Identity
  * Cloud Shell

  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Disable Cloud Shell for managed user accounts](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell#disable-shell-for-managed-user-accounts)

  
  
### Analyze and refine IAM permissions regularly

Implementation | Recommended  
---|---  
Description | Use Policy Intelligence tools such as IAM recommender and Policy Analyzer to analyze and refine your Identity and Access Management (IAM) permissions.Use IAM recommender to remove roles that aren't needed or replace overly permissive roles with more granular, less-privileged roles. Use Policy Analyzer to understand who has what access to which Google Cloud resources based on your Identity and Access Management (IAM) allow policies.  
Applicable products |  IAM  
Related NIST-800-53 controls | 

  * AC-2
  * AC-6
  * CA-7

  
Related CRI profile controls | 

  * PR.AC-4.1
  * PR.AC-6.1
  * PR.IP-1.1

  
Related information | 

  * [Overview of role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview)
  * [Analyze allow policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies)

  
  
### Configure Context-Aware Access for Google consoles

Google control ID | IAM-CO-8.2  
---|---  
Implementation | Optional  
Description | With Context-Aware Access, you can create granular access control security policies for applications based on attributes such as user identity, location, device security status, and IP address. We recommend that you use Context-Aware Access to restrict access to the the Google Cloud console (https://console.cloud.google.com/) and the Google Admin console (https://admin.cloud.google.com).  
Applicable products | 

  * Cloud Identity
  * Context-Aware Access

  
Related NIST-800-53 controls | 

  * AC-3
  * AC-12
  * AC-17
  * AC-20
  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-5.1
  * PR.AC-5.2
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Protect your business with Context-Aware Access](https://support.google.com/a/answer/9275380)

  
  
### Block account self-recovery for super admin accounts

Google control ID | CI-CO-6.3  
---|---  
Implementation | Optional  
Description | An attacker could use the self-recovery process to reset super admin passwords. To mitigate the security risks associated with Signaling System 7 (SS7) attacks, SIM Swap attacks, or other phishing attacks, we recommend that you turn off this feature. To turn off the feature, go to the account recovery settings in the Google Admin console.  
Applicable products | 

  * Cloud Identity
  * Google Workspace

  
Related NIST-800-53 controls | 

  * IA-2
  * IA-4
  * IA-5

  
Related CRI profile controls | 

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Related information | 

  * [Manage a user's security settings](https://support.google.com/cloudidentity/answer/2537800)

  
  
### Turn off unused Google services

Google control ID | CI-CO-6.6  
---|---  
Implementation | Optional  
Description | In general, we recommend turning off the services that you won't use.  
Applicable products |  Cloud Identity  
Path | `http://admin.google.com > Apps > Additional Google Services`  
Operator | Setting  
Value |  `False`  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Turn on or off additional Google services](https://support.google.com/a/answer/181865)

  
  
## Organization

This section includes the best practices and guidelines for Organization Policy Service and Resource Manager when running workloads on Google Cloud.

### Restrict TLS versions supported by Google APIs

Google control ID | COM-CO-1.1  
---|---  
Implementation | Required  
Description | Google Cloud supports multiple TLS protocol versions. To meet compliance requirements, you might want to deny handshake requests from clients that use older TLS versions. To configure this control, use the **Restrict TLS Versions** (`gcp.restrictTLSVersion`) organization policy constraint. You can apply this constraint to organizations, folders, or projects in the resource hierarchy. The **Restrict TLS Versions** constraint uses a deny list, which denies explicit values and allows all others. An error occurs if you try to use an allow list.Due to the behavior of organization policy hierarchy evaluation, the TLS version restriction applies to the specified resource node and all of its folders and projects (children). For example, if you deny TLS version 1.0 for an organization, it is also denied for all children that descend from that organization. You can override the inherited TLS version restriction by updating the organization policy on a child resource. For example, if your organization policy denies TLS 1.0 at the organization level, you can remove the restriction for a child folder by setting a separate organization policy on that folder. If the folder has any children, the folder's policy will also be applied on each child resource due to policy inheritance.To further restrict the TLS version to TLS 1.3 only, you can set this policy to also restrict TLS version 1.2. You must implement this control on applications that you host inside of Google Cloud. For example, at the organization level, set:`["TLS_VERSION_1","TLS_VERSION_1.1","TLS_VERSION_1.2"]`  
Applicable products |  All; managed by Organization Policy Service  
Path | `gcp.restrictTLSVersion`  
Operator | ==  
Value | 

  * `TLS_VERSION_1`
  * `TLS_VERSION_1.1`

  
Type | String  
Compliance Manager control ID | `RESTRICT_LEGACY_TLS_VERSIONS`  
Related NIST-800-53 controls | 

  * SC-8
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Restrict TLS versions](https://docs.cloud.google.com/assured-workloads/docs/restrict-tls-versions)

  
  
### Restrict authorized principals

Google control ID | COM-CO-4.1  
---|---  
Implementation | Required  
Description | Ensure only identities from your organization are allowed in your Google Cloud environment. Use the **Domain restricted sharing** (`iam.allowedPolicyMemberDomains`) or the `iam.managed.allowedPolicyMembers` organization policy constraint to define one or more Cloud Identity or Google Workspace customer IDs whose principals can be added to Identity and Access Management (IAM) policies.These constraints help prevent employees from granting access to external accounts outside of your organization's control that don't follow your security policies for multifactor authentication (MFA) or password management. This control is critical for preventing unauthorized access, ensuring that only trusted, managed corporate identities can be used.  
Applicable products | 

  * Organization Policy Service
  * IAM

  
Path | `constraints/iam.allowedPolicyMemberDomains`  
Operator | Is  
Value |  `CUSTOMER_ID,ORG_ID`  
Type | List  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains)

  
  
### Restrict resource service usage

Google control ID | RM-CO-4.1  
---|---  
Implementation | Required  
Description | The `gcp.restrictServiceUsage` constraint ensures that only your approved Google Cloud services are used in the right places. For example, a production or highly sensitive folder has a small list of Google Cloud services that are approved to store data. A sandbox folder might have a larger list of services and accompanying data security controls to help prevent data exfiltration. The value is specific to your systems and matches your approved list of services and dependencies for specific folders and projects.This constraint lets your organization create an allowlist of approved services, which helps prevent employees from using unvetted services.  
Applicable products | 

  * Organization Policy Service
  * Resource Manager

  
Path | `constraints/gcp.restrictServiceUsage`  
Operator | Is  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources)

  
  
### Restrict resource locations

Google control ID | RM-CO-4.2  
---|---  
Implementation | Required  
Description | The Resource Location Restriction (`gcp.resourceLocations`) constraint ensures that only your approved Google Cloud regions are used to store data. The value is specific to your systems and matches your organization's approved list of regions for data residency.This constraint lets your organization enforce that your resources and data are only created and saved in specific, approved geographic regions.  
Applicable products | 

  * Organization Policy Service
  * Resource Manager

  
Path | `constraints/gcp.resourceLocations`  
Operator | Is  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Restricting resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations)

  
  
### Use Infrastructure as Code for secure baselines

Implementation | Required  
---|---  
Description | Use Infrastructure as Code (such as Terraform) with the enterprise foundations blueprint as a secure baseline to help ensure known good states and enable rapid, consistent deployments.  
Applicable products |  All  
Related NIST-800-53 controls | 

  * CM-2
  * CM-3
  * CM-9

  
Related CRI profile controls | 

  * PR.IP-1.1
  * PR.IP-3.1

  
Related information | 

  * [Google Cloud enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations)

  
  
## Networking

This section includes the best practices and guidelines for Virtual Private Cloud (VPC) and Cloud DNS when running workloads on Google Cloud.

### Block default network creation

Google control ID | VPC-CO-6.1  
---|---  
Implementation | Required  
Description | The `compute.skipDefaultNetworkCreation` boolean constraint skips the creation of the default network and related resources when creating Google Cloud projects.The default network is an auto-mode Virtual Private Cloud (VPC) network with pre-populated IPv4 firewall rules to allow internal communication paths. Generally, this setup isn't a recommended security posture for production environments.  
Applicable products | 

  * Organization Policy Service
  * Virtual Private Cloud (VPC)

  
Path | `constraints/compute.skipDefaultNetworkCreation`  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Organization policy constraints](https://docs.cloud.google.com/vpc/docs/vpc#org-policies)

  
  
### Enable DNS Security Extensions

Google control ID | DNS-CO-6.1  
---|---  
Implementation | Required  
Description | The Domain Name System Security Extensions (DNSSEC) is a feature of the Domain Name System (DNS) that authenticates responses to domain name lookups. It doesn't provide privacy protections for those lookups, but prevents attackers from manipulating or poisoning the responses to DNS requests.Within Cloud DNS, enable DNSSEC in the following places:

  * DNS zone
  * Top-level domain (TLD)
  * DNS resolution

  
Applicable products |  Cloud DNS  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Not applicable](https://github.com/GoogleCloudPlatform/community/blob/master/archived/dnssec-cloud-dns-domains/index.md)

  
  
### Enable Private Google Access

Google control ID | GCVE-CO-1.5  
---|---  
Implementation | Required  
Description | Enable Private Google Access on all subnets.Enabling Private Google Access lets services access Google Cloud services that don't have external IP addresses. By default, Private Google Access isn't enabled on new resources and requires additional steps to explicitly enable it.  
Applicable products |  Virtual Private Cloud (VPC)  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8
  * SC-13

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access)

  
  
### Enable private service access for service producers

Google control ID | GCVE-CO-1.6  
---|---  
Implementation | Required  
Description | Enable private service access to create a private network between Google Cloud services such as Google Cloud VMware Engine legacy networks and service producers such as Cloud SQL. Private service access helps avoid exposing workload network connections to the internet unnecessarily.  
Applicable products |  Virtual Private Cloud (VPC)  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8
  * SC-13

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Private service access](https://docs.cloud.google.com/vpc/docs/private-services-access)
  * [(Legacy) Set up private connections](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access)

  
  
### Disable IPv6 unless required

Implementation | Required  
---|---  
Description | Disable IPv6 external subnet creation unless specifically required. To reduce your attack surface, consider disabling IPv6 on systems and networks where it's not actively managed or required. Many organizations have mature security controls and monitoring for IPv4, but their tools and policies might not fully extend to IPv6, which can create a significant blind spot for threats. Running a dual-stack network also introduces operational complexity, requiring specific configurations and expertise to manage and troubleshoot effectively. Therefore, if you don't have a clear business driver for IPv6, disabling it can simplify your environment and ensure all traffic is consistently filtered through your established IPv4 security posture.  
Applicable products |  Compute Engine  
Path | `constraints/compute.disableVpcExternalIpv6`  
Operator | Is  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * CM-7

  
Related CRI profile controls | 

  * PR.PT-3.1

  
Related information | 

  * [IPv6 support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support)

  
  
### Restrict outbound traffic

Implementation | Required  
---|---  
Description | Limit access to external sources because by default, all access is allowed out. Set specific firewall rules for intended patterns of traffic needing to egress.By default, systems are often allowed to make outbound connections to the internet, which can be deemed a security risk. A deny-by-default policy blocks outbound traffic and requires specific rules to be created for only the known, necessary destinations.  
Applicable products |  Cloud Next Generation Firewall  
Path | `cloudasset.assets/assetType`  
Operator | ==  
Value |  `compute.googleapis.com/Firewall`  
Type | String  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls)

  
  
### Limit inbound access to SSH and RDP ports

Implementation | Required  
---|---  
Description | Where possible, restrict inbound access to specific resources and resource ranges only. If Identity-Aware Proxy (IAP) is configured, set inbound SSH and Remote Desktop Protocol (RDP) firewall rules to IAP IP ranges as sources.Permissive SSH and RDP firewall rules allow for brute force attacks. Instead, use Google Cloud identity-aware proxies (such as IAP) for SSH and RDP.  
Applicable products |  IAP  
Path | `cloudasset.assets/assetType`  
Operator | ==  
Value |  `compute.googleapis.com/Firewall`  
Type | String  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding)

  
  
### Enable VPC Service Controls

Implementation | Required  
---|---  
Description | Enable VPC Service Controls as an additional layer of protection to prevent potential data loss.VPC Service Controls can help prevent data exfiltration by creating isolation perimeters around your cloud resources, sensitive data, and networks. The service perimeter limits the usefulness of compromised credentials because the perimeter blocks requests to restricted services that originate from attacker-controlled endpoints that are outside of your environment.  
Applicable products |  VPC Service Controls  
Path | `accesscontextmanager.accessPolicies.servicePerimeters/perimeterType`  
Operator | ==  
Value |  `PERIMETER_TYPE_REGULAR`  
Type | String  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)
  * [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products)

  
  
### Use Cloud Armor policies

Implementation | Required  
---|---  
Description | For applications that are exposed behind Cloud Load Balancing, use Google Cloud Armor default policies or configure your own policies to add Layer 3 to Layer 7 network protection for externally-facing applications or services. Cloud Armor security policies help protect your application by providing Layer 7 filtering. These policies also review incoming requests for common web attacks or other Layer 7 attributes to potentially block traffic before the traffic reaches your load-balanced backend services or backend buckets. Each security policy is made up of a set of rules that include attributes from Layer 3 through Layer 7.  
Applicable products |  Cloud Armor  
Path | `compute.backendServices/securityPolicy`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Cloud Armor overview](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)

  
  
### Enable the service scope restriction in Access Context Manager access policies

Google control ID | COM-CO-8.1  
---|---  
Implementation | Recommended for generative AI on use cases  
Description | For every service perimeter, confirm in the Google Cloud console that the perimeter type is set to regular.  
Applicable products | 

  * Access Context Manager
  * VPC Service Controls

  
Path | `accesscontextmanager.accessPolicies.servicePerimeters/perimeterType`  
Operator | ==  
Value |  `PERIMETER_TYPE_REGULAR`  
Type | String  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [Access Context Manager overview](https://docs.cloud.google.com/access-context-manager/docs/overview)

  
  
### Restrict APIs within VPC Service Controls service perimeters

Google control ID | COM-CO-8.2  
---|---  
Implementation | Recommended for generative AI on use cases  
Description | For every service perimeter, use Access Context Manager to confirm that the perimeter is protecting the API.  
Applicable products | 

  * VPC Service Controls
  * Access Context Manager

  
Path | `accesscontextmanager.accessPolicies.servicePerimeters/status.restrictedServices`  
Operator | Anyof  
Value | 

  * `aiplatform.googleapis.com`
  * `artifactregistry.googleapis.com`
  * `bigquery.googleapis.com`
  * `cloudasset.googleapis.com`
  * `cloudbuild.googleapis.com`
  * `cloudfunctions.googleapis.com`
  * `cloudresourcemanager.googleapis.com`
  * `containeranalysis.googleapis.com`
  * `discoveryengine.googleapis.com`
  * `dns.googleapis.com`
  * `notebooks.googleapis.com`
  * `ondemandscanning.googleapis.com`
  * `orgpolicy.googleapis.com`
  * `pubsub.googleapis.com`
  * `secretmanager.googleapis.com`
  * `storage.googleapis.com`
  * `visionai.googleapis.com`

  
Type | String  
Related NIST-800-53 controls | 

  * SC-7
  * SC-8

  
Related CRI profile controls | 

  * PR.AC-5.1
  * PR.AC-5.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1
  * PR.PT-4.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4

  
Related information | 

  * [gcloud access-context-manager perimeters update](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update)

  
  
### Use Cloud VPN or Cloud Interconnect in hybrid environments

Implementation | Recommended  
---|---  
Description | To connect securely to your on-premises environment, use Cloud VPN or Cloud Interconnect.Cloud VPN is a lower-cost solution with lower bandwidth requirements. Cloud Interconnect provides an enterprise-grade connection with higher throughput.  
Applicable products | 

  * Cloud VPN
  * Cloud Interconnect

  
Path | `cloudasset.assets/assetType`  
Operator | in  
Value | 

  * `compute.googleapis.com/VpnGateway`
  * `compute.googleapis.com/VpnTunnel`
  * `compute.googleapis.com/Interconnect`
  * `compute.googleapis.com/InterconnectAttachment`

  
Type | String  
Related NIST-800-53 controls | 

  * SC-7

  
Related CRI profile controls | 

  * PR.AC-3.1

  
Related information | 

  * [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)
  * [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)
  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)

  
  
### Use zonal DNS

Google control ID | DNS-CO-4.1  
---|---  
Implementation | Optional  
Description | The `compute.setNewProjectDefaultToZonalDNSOnly` boolean constraint lets you set the internal DNS setting for new projects to use zonal DNS only. Use zonal DNS because it offers higher reliability compared to individual zones because zonal DNS isolates failures in the DNS registration .  
Applicable products |  Organization policy  
Path | `constraints/compute.setNewProjectDefaultToZonalDNSOnly`  
Operator | =  
Value |  `True`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AC-3
  * AC-17
  * AC-20

  
Related CRI profile controls | 

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

  
Related information | 

  * [Zonal and global internal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names)

  
  
### Inspect network traffic using Cloud IDS

Implementation | Optional  
---|---  
Description | To help detect cryptomining and other malware activities in outbound network traffic, configure [Cloud Intrusion Detection System](https://cloud.google.com/intrusion-detection-system). Cloud Intrusion Detection System is an intrusion detection service that provides threat detection for intrusions, malware, spyware, and command-and-control attacks on your network. To mitigate against cryptomining attacks, Cloud IDS inspects network packets for payloads that cryptomining protocols (such as Stratum) use, flags connections to known malicious mining pool domains, and detects the use of anonymization tools or proxy tunnels that try to mask outbound traffic.  
Applicable products |  Cloud IDS  
Path | `cloudasset.assets/assetType`  
Operator | ==  
Value |  `ids.googleapis.com/Endpoint`  
Type | String  
Related NIST-800-53 controls | 

  * SI-4
  * SC-7
  * SI-3
  * AU-6
  * CA-7

  
Related CRI profile controls | 

  * DE.CM-1.1
  * DE.CM-1.2
  * DE.AE-2.1
  * DE.AE-3.1
  * PR.PT-4.1
  * PR.AC-3.1

  
Related information | 

  * [Configure Cloud IDS](https://docs.cloud.google.com/intrusion-detection-system/docs/configuring-ids)

  
  
## Logging, monitoring, alerting

This section includes the best practices and guidelines for logging and auditing services in Google Cloud and configuring alerts for services such as Cloud Billing.

### Share audit logs from Cloud Identity

Google control ID | CI-CO-6.5  
---|---  
Implementation | Required  
Description | If using Cloud Identity, share audit logs from Cloud Identity to Google Cloud.Admin Activity audit logs from Google Workspace or Cloud Identity are ordinarily managed and viewed in the Google Admin console, separately from your logs in your Google Cloud environment. These logs contain information that is relevant for your Google Cloud environment, such as user login events.We recommend that you share Cloud Identity audit logs to your Google Cloud environment to centrally manage logs from all sources.  
Applicable products | 

  * Google Workspace
  * Cloud Logging
  * Cloud Identity

  
Related NIST-800-53 controls | 

  * AC-2
  * AC-3
  * AC-8
  * AC-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4

  
Related information | 

  * [Audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging)
  * [Share data with Google Cloud services](https://support.google.com/a/answer/9320190)

  
  
### Use audit logs

Google control ID | COM-CO-7.3  
---|---  
Implementation | Required  
Description | Google Cloud services write audit log entries to answer who did what, where, and when with Google Cloud resources. Enable audit logging at the organization level. You can configure logging using the pipeline that you use to set up the Google Cloud organization.  
Applicable products |  Cloud Audit Logs  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit)

  
  
### Enable VPC Flow Logs

Google control ID | COM-CO-7.4  
---|---  
Implementation | Required  
Description | VPC Flow Logs record a sample of network flows that are sent from and received by VM instances, including those used as Google Kubernetes Engine (GKE) nodes. The sample is typically 50% or less of the VPC network flows. When you enable VPC Flow Logs, you enable logging for all VMs in a subnet. However, you can reduce the amount of information written to logging. Enable VPC Flow Logs for each VPC subnet. You can configure logging using a pipeline that you use to create a project.  
Applicable products |  Virtual Private Cloud  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Log sampling and aggregation](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling)

  
  
### Enable Firewall Rules Logging

Google control ID | COM-CO-7.5  
---|---  
Implementation | Required  
Description | By default, firewall rules don't automatically write logs.Firewall Rules Logging lets you audit, verify, and analyze the effects of your firewall rules. For example, you can determine if a firewall rule designed to deny traffic is functioning as intended. Logging is also useful if you want to determine how many connections are affected by a given firewall rule.  Enable logging for each firewall rule. You can configure logging using a pipeline that you use to create a firewall.  
Applicable products |  Virtual Private Cloud  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Use Firewall Rules Logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging)

  
  
### Enable auditing of administrator activity

Google control ID | COM-CO-7.1  
---|---  
Implementation | Required  
Description | By default, Google Cloud enables and doesn't let anyone disable auditing of key administrator activity for privileged accounts.Admin Activity audit logs contain log entries for API calls or other actions that modify the configuration or metadata of resources. For example, these logs record when users create VM instances or change IAM permissions. Admin Activity audit logs contain log entries for creating, modifying, and deleting of organization policy constraints from an organization, folder, and project level.Admin Activity audit logs are always written; you can't configure, exclude, or disable them. Even if you disable the Cloud Logging API, Admin Activity audit logs are still generated. We recommend that your organization set up policies and procedures to monitor these alerts, and generate actions or alerts according to your enterprise access policies for monitoring administrator activities.Consider creating log-based alerts in Cloud Logging to flag suspicious API requests (such as unauthorized VM creations or IAM privilege escalations).  
Applicable products |  Cloud Audit Logs  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Google Cloud services with audit logs](https://docs.cloud.google.com/logging/docs/audit/services)
  * [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)

  
  
### Subscribe to security bulletins

Google control ID | GKE-CO-1.8  
---|---  
Implementation | Required  
Description | Subscribe to the security bulletin notifications for Google Cloud services to receive alerts about vulnerabilities and mitigation measures.When security bulletins are available that are relevant to your Google Cloud service (such as GKE), the service can publish notifications about those events as messages to Pub/Sub topics that you configure. You can receive these notifications on a Pub/Sub subscription, integrate with third-party services, and filter for the notification types you want to receive.  
Applicable products |  All  
Related NIST-800-53 controls | 

  * SI-5

  
Related CRI profile controls | 

  * PR.IP-1.4

  
Related information | 

  * [Security Bulletins](https://docs.cloud.google.com/support/bulletins)

  
  
### Configure Essential Contacts groups

Implementation | Required  
---|---  
Description | Configure Essential Contacts to ensure that a monitored group alias or mailing list receive important notifications.Google sends critical security alerts (like a potential account compromise) to the email addresses listed as Essential Contacts. If an individual's email is used for this purpose, the alert is missed if that person is unavailable or has left the company.Using a monitored group email address helps ensure these time-sensitive alerts are delivered to an active team that can respond quickly.  
Applicable products |  Resource Manager  
Path | `essentialcontacts.googleapis.com/Contact`  
Operator | Is set  
Type | String  
Related NIST-800-53 controls | 

  * IR-4

  
Related CRI profile controls | 

  * PR.IP-1.4

  
Related information | 

  * [Essential Contacts overview](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)

  
  
### Monitor billing anomalies

Implementation | Required  
---|---  
Description | Use the billing anomaly feature in Cloud Billing to track any spikes or deviations in expected spend. A sudden, unexpected spike in a cloud bill is a primary indicator of a security compromise. Unexpected billing spikes are sometimes caused by attackers who have gained access and are using resources for unauthorized activities.Enabling billing anomaly detection provides an essential early warning system so that you can automatically flag this suspicious activity.  
Applicable products |  Cloud Billing  
Related NIST-800-53 controls | 

  * AU-6

  
Related CRI profile controls | 

  * DE.AE-1.1

  
Related information | 

  * [View and manage cost anomalies](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies)
  * [Set up programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications)

  
  
### Export logs to a log sink for long-term storage

Implementation | Required  
---|---  
Description | Create a log sink to export logs for your security monitoring solution and set the retention period to meet your requirements.The default log retention periods are often not long enough to meet the 1-7 year requirements mandated by compliance regulations like PCI or HIPAA.Creating a log sink to export logs to a long-term storage location is essential for meeting certain legal and regulatory obligations. Log sinks also let you send logs to a centralized security monitoring system for advanced threat detection.  
Applicable products |  Cloud Logging  
Path | `logging.googleapis.com/LogSink/disabled`  
Operator | Is  
Value |  `False`  
Type | Boolean  
Related NIST-800-53 controls | 

  * AU-9

  
Related CRI profile controls | 

  * PR.DS-4.1

  
Related information | 

  * [Route log entries](https://docs.cloud.google.com/logging/docs/routing/overview)

  
  
### Maintain an inventory of your resources in Google Cloud

Implementation | Required  
---|---  
Description | Use Cloud Asset Inventory to maintain a five-week inventory of your resources in Google Cloud. To analyze changes, export your asset metadata to BigQuery or Cloud Storage.  
Applicable products |  Cloud Asset Inventory  
Related NIST-800-53 controls | 

  * CM-8
  * CM-8(1)
  * CM-8(2)
  * CM-8(3)
  * CM-8(4)
  * PM-5

  
Related CRI profile controls | 

  * ID.AM-1.1
  * ID.AM-2.1
  * ID.AM-3.1
  * ID.AM-5.1

  
Related information | 

  * [Cloud Asset Inventory overview](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)
  * [Export asset metadata to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery)

  
  
### Enable Data Access audit logs

Google control ID | COM-CO-7.2  
---|---  
Implementation | Recommended for certain use cases  
Description | To track who accessed data in your Google Cloud environment, enable Data Access audit logs. These logs record API calls that read, create, or modify user data, as well as API calls that read resource configurations. We highly recommend enabling Data Access audit logs for situations where you need to monitor who reads or exports data. For example, you have generative AI models that can access sensitive data and you want to audit who has read the information. To use Data Access audit logs, you must set up your own custom detection logic for specific activities, like super admin logins. Data Access audit logs volume can be large. Enabling Data Access logs might result in your Google Cloud project being charged for the additional logs usage.  
Applicable products |  Cloud Audit Logs  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable)

  
  
### Configure billing alerts

Google control ID | CB-CO-6.1  
---|---  
Implementation | Recommended  
Description | Avoid surprises on your bill by creating Cloud Billing budgets to monitor all of your Google Cloud charges in one place. After you've established a budget amount, set budget alert threshold rules on a per-project basis to trigger email notifications. These notifications help you track your spending against your budget. You can also use Cloud Billing budgets to automate cost-control responses.  
Applicable products |  Cloud Billing  
Related NIST-800-53 controls | 

  * SI-4
  * SI-5

  
Related CRI profile controls | 

  * PR.DS-5.1
  * PR.DS-8.1
  * ID.RA-1.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4
  * DE.CM-5.1
  * DE.CM-6.1
  * DE.CM-6.2
  * DE.CM-6.3
  * DE.CM-7.1
  * DE.CM-7.2
  * DE.CM-7.3
  * DE.CM-7.4
  * DE.DP-2.1
  * DE.DP-3.1
  * DE.DP-4.1
  * DE.DP-4.2
  * DE.DP-5.1
  * DE.AE-2.1
  * DE.AE-3.1
  * DE.AE-3.2
  * DE.AE-4.1
  * ID.RA-1.1
  * ID.RA-2.1
  * ID.RA-3.1
  * ID.RA-3.2
  * ID.RA-3.3

  
Related information | 

  * [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)

  
  
### Monitor group logs

Implementation | Recommended  
---|---  
Description | If you use groups to assign IAM policies, monitor the group logs to ensure that non-corporate accounts aren't added.  
Applicable products |  Google Workspace  
Related NIST-800-53 controls | 

  * AU-6
  * AU-2
  * AC-2
  * AU-12
  * AU-3

  
Related CRI profile controls | 

  * DE.CM-1.1
  * DE.AE-2.1
  * DE.AE-3.1
  * PR.PT-1.1
  * PR.AC-1.1
  * PR.AC-6.1

  
Related information | 

  * [Groups log events](https://support.google.com/a/answer/6270454)

  
  
### Monitor usage patterns for service accounts and service account keys

Implementation | Recommended  
---|---  
Description | Set up monitoring so that you can track how service accounts and service account keys are being used in your organization.  
Applicable products |  IAM  
Related NIST-800-53 controls | 

  * AU-6
  * AC-2
  * AU-2
  * IA-5
  * AU-12
  * AU-3

  
Related CRI profile controls | 

  * DE.CM-1.1
  * DE.CM-3.1
  * DE.AE-2.1
  * DE.AE-3.1
  * PR.PT-1.1
  * PR.AC-1.1
  * PR.AC-6.1

  
Related information | 

  * [Monitor usage patterns for service accounts and keys](https://docs.cloud.google.com/iam/docs/service-account-monitoring)
  * [Tools to understand service account usage](https://docs.cloud.google.com/policy-intelligence/docs/service-account-usage-tools)

  
  
### Enable Access Transparency logs

Google control ID | COM-CO-7.7  
---|---  
Implementation | Optional  
Description | Standard logs show you what your organization's own users are doing, but Access Transparency logs show what Google support staff do when they access the account. This access typically only happens in response to a support request. Access Transparency logs provide a complete and verifiable audit trail of all access, which is essential for meeting strict compliance and data governance requirements. You can enable Access Transparency at the organization level.  
Applicable products |  Access Transparency  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable)

  
  
### Export billing data for detailed analysis

Google control ID | CB-CO-6.2  
---|---  
Implementation | Optional  
Description | For further billing analysis, you can export Google Cloud billing data to BigQuery or a JSON file. For example, you can automatically export detailed data, such as usage, cost estimates, and pricing, throughout the day to a BigQuery dataset that you specify. You can then access your Cloud Billing data from BigQuery for detailed analysis, or use a tool like Data Studio to visualize your data.  
Applicable products | 

  * BigQuery Data Transfer Service
  * BigQuery
  * Cloud Billing

  
Related NIST-800-53 controls | 

  * SI-4
  * SI-5

  
Related CRI profile controls | 

  * PR.DS-5.1
  * PR.DS-8.1
  * ID.RA-1.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4
  * DE.CM-5.1
  * DE.CM-6.1
  * DE.CM-6.2
  * DE.CM-6.3
  * DE.CM-7.1
  * DE.CM-7.2
  * DE.CM-7.3
  * DE.CM-7.4
  * DE.DP-2.1
  * DE.DP-3.1
  * DE.DP-4.1
  * DE.DP-4.2
  * DE.DP-5.1
  * DE.AE-2.1
  * DE.AE-3.1
  * DE.AE-3.2
  * DE.AE-4.1
  * ID.RA-1.1
  * ID.RA-2.1
  * ID.RA-3.1
  * ID.RA-3.2
  * ID.RA-3.3

  
Related information | 

  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)

  
  
## Key and secret management

This section includes the best practices and guidelines for Cloud Key Management Service and Secret Manager when running workloads on Google Cloud.

### Encrypt data at rest in Google Cloud

Google control ID | COM-CO-2.1  
---|---  
Implementation | Required (default)  
Description | All data in Google Cloud is encrypted at rest by default using NIST-approved algorithms.  
Applicable products |  Google Cloud default  
Related NIST-800-53 controls | 

  * SC-28

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2

  
Related information | 

  * [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption)

  
  
### Use NIST-approved algorithms for encryption and decryption

Google control ID | COM-CO-2.4  
---|---  
Implementation | Required  
Description | Ensure that Cloud Key Management Service (Cloud KMS) only uses NIST-approved algorithms to store sensitive keys in the environment. This control ensures secure key usage by only NIST-approved algorithms and security. The `CryptoKeyVersionAlgorithm` field is a provided allowlist. Remove algorithms that don't comply with your organization's policies.  
Applicable products |  Cloud KMS  
Path | `cloudkms.projects.locations.keyRings.cryptoKeys/versionTemplate.algorithm`  
Operator | in  
Value | 

  * `RSA_SIGN_PSS_2048_SHA256`
  * `RSA_SIGN_PSS_3072_SHA256`
  * `RSA_SIGN_PSS_4096_SHA256`
  * `RSA_DECRYPT_OAEP_2048_SHA256`
  * `RSA_DECRYPT_OAEP_4096_SHA256`
  * `RSA_DECRYPT_OAEP_2048_SHA1`
  * `RSA_DECRYPT_OAEP_4096_SHA1`

  
Type | String  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms)
  * [Create a key](https://docs.cloud.google.com/kms/docs/create-key)

  
  
### Set the purpose for Cloud KMS keys

Google control ID | COM-CO-2.5  
---|---  
Implementation | Required  
Description | Set the purpose for Cloud KMS keys to `ENCRYPT_DECRYPT` so that keys are only used to encrypt and decrypt data. This control blocks other functions, such as signing, and ensures that keys are only used for their intended purpose. If you use keys for other functions, validate those use cases and consider creating additional keys.  
Applicable products |  Cloud KMS  
Path | `cloudkms.projects.locations.keyRings.cryptoKeys/purpose`  
Operator | ==  
Value |  `ENCRYPT_DECRYPT`  
Type | String  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms)
  * [Create a key](https://docs.cloud.google.com/kms/docs/create-key)

  
  
### Ensure that CMEK settings are appropriate for secure BigQuery data warehouses

Google control ID | COM-CO-2.6  
---|---  
Implementation | Required  
Description | The protection level indicates how cryptographic operations are performed. After you create a customer-managed encryption key (CMEK), you can't change the protection level. Supported protection levels are the following:

  * **SOFTWARE:** Cryptographic operations are performed in software.
  * **HSM:** Cryptographic operations are performed in a hardware security module (HSM).
  * **EXTERNAL:** Cryptographic operations are performed using a key that is stored in an external key manager that is connected to Google Cloud over the internet. Limited to symmetric encryption and asymmetric signing.
  * **EXTERNAL_VPC:** Cryptographic operations are performed using a key that is stored in an external key manager that is connected to Google Cloud over a Virtual Private Cloud (VPC) network. Limited to symmetric encryption and asymmetric signing.

  
Applicable products | 

  * Cloud KMS
  * BigQuery

  
Path | `cloudkms.projects.locations.keyRings.cryptoKeys/primary.protectionLevel`  
Operator | in  
Value |  `[]`  
Type | String  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Cloud KMS protection levels](https://docs.cloud.google.com/kms/docs/protection-levels)
  * [External key manager](https://docs.cloud.google.com/kms/docs/ekm)
  * [Import data into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint)

  
  
### Rotate encryption keys every 90 days

Google control ID | COM-CO-2.7  
---|---  
Implementation | Required  
Description | Ensure that the rotation period of your Cloud KMS keys are set to 90 days. A general best practice is to rotate your security keys on a regular interval. This control enforces key rotation for keys that are created with HSM services. When you create this rotation period, also create appropriate policies and procedures to securely handle the creation, deletion, and modification of keying material so that you can help protect your information and ensure availability. Ensure that this period adheres to your corporate policies for key rotation.  
Applicable products |  Cloud KMS  
Path | `cloudkms.projects.locations.keyRings.cryptoKeys/rotationPeriod`  
Operator | <=  
Value |  `90`  
Type | int32  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation)

  
  
### Set up automatic secret rotation

Google control ID | SM-CO-6.2  
---|---  
Implementation | Required  
Description | Automatically rotate secrets and have emergency rotation procedures available in case of a compromise.  
Applicable products |  Secret Manager  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Create rotation schedules in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/secret-rotation)

  
  
### Create a managed encryption strategy

Implementation | Required  
---|---  
Description | Create an encryption management strategy using Cloud Key Management Service (Cloud KMS) with Autokey, Cloud External Key Manager (Cloud EKM), or both. This strategy lets your organization use and manage its own encryption keys to meet your specific requirements. Using your own encryption keys provides granular, auditable control over data access, including the ability to immediately block access to data by disabling the key.  
Applicable products | 

  * Cloud KMS
  * Cloud EKM

  
Related NIST-800-53 controls | 

  * SC-12

  
Related CRI profile controls | 

  * PR.DS-1.1

  
Related information | 

  * [Cloud KMS overview](https://docs.cloud.google.com/kms/docs/key-management-service)

  
  
### Monitor key-related activities

Implementation | Required  
---|---  
Description | Monitor critical key-related activities, including the following:

  * Key destruction (`DestroyCryptoKeyVersion`)
  * Key disablement (`UpdateCryptoKeyVersion`)
  * Policy changes (`SetIamPolicy`)
  * Key import (`CreateImportJob`, `ImportCryptoKeyVersion`, `CreateCryptoKey`, and `CreateKeyRing`)
  * Abnormal cryptographic operations (such as spikes in `Decrypt` or `AsymmetricDecrypt` operations and high rates of failed cryptographic operations)

If you're using customer-supplied encryption keys (CSEK) or Cloud External Key Manager (Cloud EKM), configure robust external backup and rotation processes.  
Applicable products |  Cloud Key Management Service  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13
  * AU-2
  * AU-6
  * SI-4

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-5.1
  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4

  
Related information | 

  * [Using Cloud Monitoring with Cloud KMS](https://docs.cloud.google.com/kms/docs/monitoring)
  * [Using Cloud Audit Logs with Cloud KMS](https://docs.cloud.google.com/kms/docs/logging)
  * [Monitor state changes using Pub/Sub](https://docs.cloud.google.com/kms/docs/monitor-state-changes)
  * [Monitor your external key manager usage](https://docs.cloud.google.com/kms/docs/monitor-ekm-usage)

  
  
### Use CMEK for Pub/Sub messages

Google control ID | PS-CO-6.1  
---|---  
Implementation | Recommended  
Description | When you enable customer-managed encryption keys (CMEK) for Pub/Sub, you obtain greater control of the encryption keys that Pub/Sub uses to protect your messages. At the application layer, Pub/Sub individually encrypts incoming messages when Pub/Sub receives them. Before Pub/Sub publishes messages to a subscription, it encrypts the messages using the newest data encryption key (DEK) that was generated for the topic. Pub/Sub decrypts the messages shortly before they're delivered to subscribers. Pub/Sub uses a Google Cloud service account to access Cloud Key Management Service. The service account is maintained internally by Pub/Sub for each project, and isn't visible in your list of service accounts.  
Applicable products | 

  * Cloud KMS
  * Pub/Sub

  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Configure message encryption](https://docs.cloud.google.com/pubsub/docs/encryption)

  
  
### Restrict customer-managed encryption keys location 

Google control ID | COM-CO-2.2  
---|---  
Implementation | Recommended  
Description | Use the **Restrict which projects may supply KMS CryptoKeys for CMEK** (`gcp.restrictCmekCryptoKeyProjects`) organization policy constraint to define which projects can store customer-managed encryption keys (CMEKs). This constraint lets you to centralize the governance and management of encryption keys. When a selected key doesn't meet this constraint, resource creation fails.To modify this constraint, administrators need the **Organization Policy Administrator** (`roles/orgpolicy.policyAdmin`) IAM role. If you want to add a second layer of protection, such as bring your own key, change this constraint to represent the key names of the CMEK that is enabled. Product specifics:

  * In Gemini Enterprise Agent Platform, you store your keys in the **KEY PROJECTS** project.

  
Applicable products | 

  * Cloud KMS
  * Organization Policy

  
Path | `constraints/gcp.restrictCmekCryptoKeyProjects`  
Operator | notexists  
Value |  `KEY PROJECTS`  
Type | String  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Require CMEK protection](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek)

  
  
### Use CMEK for Google Cloud services

Google control ID | COM-CO-2.3  
---|---  
Implementation | Recommended  
Description | If you require more control over key operations than what Google-owned and Google-managed encryption keys allow, you can use customer-managed encryption keys (CMEKs). These keys are created and managed using Cloud KMS. Store the keys as software keys, in an HSM cluster, or in an external key management system. Cloud KMS encryption and decryption rates are subject to quotas. **Cloud Storage specifics** In Cloud Storage, use CMEKs on individual objects, or configure your Cloud Storage buckets to use a CMEK by default on all new objects added to a bucket. When using a CMEK, an object is encrypted with the key by Cloud Storage at the time it's stored in a bucket, and the object is automatically decrypted by Cloud Storage when the object is served to requesters. The following restrictions apply when using CMEKs with Cloud Storage:

  * You can't encrypt an object with a CMEK by updating the object's metadata. Include the key as part of a rewrite of the object instead.
  * Your Cloud Storage uses the objects update command to set encryption keys on objects, but the command rewrites the object as part of the request.
  * You must create the Cloud KMS key ring in the same location as the data you intend to encrypt. For example, if your bucket is located in `us-east1`, any key ring used for encrypting objects in that bucket must also be created in `us-east1`.
  * For most dual-regions, you must create the Cloud KMS key ring in the associated multi-region. For example, if your bucket is located in the pair `us-east1`, `us-west1`, any key ring used for encrypting objects in that bucket must be created in the US multi-region.
  * For the `asia1`, `eur4`, and `nam4` predefined dual-regions, you must create the key ring in the same predefined dual-region.
  * The CRC32C checksum and MD5 hash of objects encrypted with CMEKs aren't returned when listing objects with the JSON API.
  * Using tools like Cloud Storage to perform additional metadata `GET` requests on each encryption object to retrieve the CRC32C and MD5 information can make listing substantially shorter. Cloud Storage can't use the decryption portion of asymmetric keys stored in Cloud KMS to automatically decrypt relevant objects in the same manner that CMEKs do.

  
Applicable products | 

  * Cloud KMS
  * Organization Policy
  * Cloud Storage

  
Path | `constraints/gcp.restrictNonCmekServices`  
Operator | ==  
Value | 

  * `bigquery.googleapis.com`
  * `storage.googleapis.com`
  * `aiplatform.googleapis.com`

  
Type | String  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations)
  * [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas)
  * [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)

  
  
### Replicate secrets automatically

Google control ID | SM-CO-6.1  
---|---  
Implementation | Recommended  
Description | Choose the automatic replication policy to replicate your secrets unless your workload has specific location requirements. The automatic policy meets the availability and performance needs of most workloads. If your workload has specific location requirements, you can use the API to select the locations for the replication policy when you create the secret.  
Applicable products |  Secret Manager  
Related NIST-800-53 controls | 

  * SC-12
  * SC-13

  
Related CRI profile controls | 

  * PR.DS-1.1
  * PR.DS-1.2
  * PR.DS-2.1
  * PR.DS-2.2
  * PR.DS-5.1

  
Related information | 

  * [Choose a replication policy](https://docs.cloud.google.com/secret-manager/docs/choosing-replication)

  
  
## Security posture and analytics

This document includes the best practices and guidelines for Security Command Center when running workloads on Google Cloud.

### Enable Security Command Center at the organization level

Google control ID | SCC-CO-6.1  
---|---  
Implementation | Required  
Description | Enable Security Command Center at the organization level to detect potential attacks and analyze alerts. Security Command Center lets you scan for common vulnerabilities (CVEs) and leaked secrets across running virtual machines, containers, and serverless Cloud Run workloads without deploying OS agents. Security Command Center can detect toxic combinations of security issues when it runs attack path simulations, which let you visualize how threat actors could exploit and chain together minor vulnerabilities from the internet to reach high-value compute resources or project billing permissions. Deploy Compliance Manager frameworks to monitor your organization's compliance and alert you to any posture drift. You can use Container Threat Detection and Cloud Run Threat Detection to monitor active workloads for threats such as evasive exploits, reverse shell executions, and the launch of unauthorized cryptomining binaries within active container workloads.If you don't want to use Security Command Center, you must enable another posture management solution.  
Applicable products |  Security Command Center  
Path | `cloudasset.assets/assetType`  
Operator | ==  
Value |  `securitycenter.googleapis.com/OrganizationSettings`  
Type | String  
Related NIST-800-53 controls | 

  * SI-4
  * SI-5

  
Related CRI profile controls | 

  * PR.DS-5.1
  * PR.DS-8.1
  * ID.RA-1.1
  * DE.CM-1.1
  * DE.CM-1.2
  * DE.CM-1.3
  * DE.CM-1.4
  * DE.CM-5.1
  * DE.CM-6.1
  * DE.CM-6.2
  * DE.CM-6.3
  * DE.CM-7.1
  * DE.CM-7.2
  * DE.CM-7.3
  * DE.CM-7.4
  * DE.DP-2.1
  * DE.DP-3.1
  * DE.DP-4.1
  * DE.DP-4.2
  * DE.DP-5.1
  * DE.AE-2.1
  * DE.AE-3.1
  * DE.AE-3.2
  * DE.AE-4.1
  * ID.RA-1.1
  * ID.RA-2.1
  * ID.RA-3.1
  * ID.RA-3.2
  * ID.RA-3.3

  
Related information | 

  * [Overview of activating Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level)

  
  
### Configure alerts from Security Command Center

Google control ID | SCC-CO-7.1  
---|---  
Implementation | Recommended  
Description | Alerts from the Security Command Center provide visibility into your organization and notify you about issues with your Google Cloud services so you can take appropriate action. You can set up alerts in Cloud Logging to get notifications on errors that are related to the Security Command Center service agent (`service-org-ORGANIZATION_NUMBER@security-center-api.iam.gserviceaccount.com`).  
Applicable products | 

  * Security Command Center
  * Logging

  
Related NIST-800-53 controls | 

  * AU-2
  * AU-3
  * AU-8
  * AU-9

  
Related CRI profile controls | 

  * DM.ED-7.1
  * DM.ED-7.2
  * DM.ED-7.3
  * DM.ED-7.4
  * PR.IP-1.4

  
Related information | 

  * [Troubleshooting](https://docs.cloud.google.com/security-command-center/docs/troubleshooting)

  
  
## What's next

  * Review [infrastructure controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/infrastructure).

  * See more [Google Cloud security best practices and guidelines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
