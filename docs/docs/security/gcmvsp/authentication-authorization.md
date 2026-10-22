---
url: https://docs.cloud.google.com/docs/security/gcmvsp/authentication-authorization/
title: Authentication and authorization guidelines \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:53.287402+00:00
---

# Authentication and authorization guidelines  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/gcmvsp/authentication-authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Authentication and authorization guidelines Stay organized with collections  Save and categorize content based on your preferences. 

The following guidelines for the minimum viable security platform align with the authentication and authorization security pillar.

## Basic level guidelines

Implement the following authentication and authorization guidelines first.

Item | 

### Define the identity source of truth  
  
---|---  
Description | Decide on your source of truth for provisioning managed user identities. Patterns include creating user identities in Cloud Identity, syncing identities from an existing identity provider, or using Workforce Identity Federation.  
Related information | 

  * [Decide how to onboard identities to Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities)

  
Item ID | MVSP-CO-1.4  
Mapping |  Related NIST-800-53 controls:

  * AC-2

Related CRI profile controls:

  * PR.AC-1.1

  
Item | 

### Create redundant administrator accounts  
  
---|---  
Description | Don't have a single super admin or Organization Administrator. Create one or more (up to 20) backup administrator accounts. A single super admin or Organization Administrator can result in lockout scenarios. This situation also carries a higher risk as one person can make platform-altering changes, potentially with no oversight.  
Related information | 

  * [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373)
  * [Setting up your organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#setting-up)

  
Item ID | MVSP-CO-1.7  
Mapping |  Related NIST-800-53 controls:

  * IA-2
  * IA-4
  * IA-5

Related CRI profile controls:

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-1.3
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

Compliance Manager control:

  * [Limit Super Admin Accounts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#enable-cloud-logging-on-super-admin-accounts)

  
Item | 

### Enforce strong password policies  
  
---|---  
Description | Enforce strong and unique passwords for all user accounts. Consider using a password manager. Weak or no credentials are a common pattern that malicious users can easily exploit.  
Related information | 

  * [Enforce and monitor password requirements for users](https://support.google.com/a/answer/139399)
  * [Enable, disable, and use password policies](https://docs.cloud.google.com/identity-platform/docs/password-policy)

  
Item ID | MVSP-CO-1.9  
Mapping |  Related NIST-800-53 controls:

  * IA-5

Related CRI profile controls:

  * PR.AC-1.1

  
Item | 

### Use roles based on job functions  
  
---|---  
Description | Use Identity and Access Management (IAM) roles that are based on job functions to assign permissions to users. Job functions are predefined roles that allow admins to provide a set of permissions that is limited to a job function, thus improving productivity and reducing the back-and-forth of asking for permissions. To better align with your organization's requirements, you can create custom roles based on predefined roles.  
Related information | 

  * [Predefined roles for job functions](https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions)

  
Item ID | MVSP-CO-1.20  
Mapping |  Related NIST-800-53 controls:

  * AC-6

Related CRI profile controls:

  * PR.AC-4.1

  
Item | 

### Block the creation of external service account keys  
  
---|---  
Description | Use the `iam.disableServiceAccountKeyCreation` boolean constraint to disable external service account keys from being created. This constraint lets you control the use of unmanaged long-term credentials for service accounts. When this constraint is set, you can't create user-managed credentials for service accounts in projects that are affected by the constraint.  
Related information | 

  * [Disable service account key creation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation)

  
Item ID | MVSP-CO-1.17  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

Compliance Manager control:

  * [Block Service Account Key Creation](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-service-account-key-creation)

  
  
## Intermediate level guidelines

After you implemented the basic guidelines, implement the following authentication and authorization guidelines.

Item | 

### Restrict external members in groups  
  
---|---  
Description | Set organization-wide policies to prevent adding external members to Google Groups. By default, external user accounts can be added to groups in Cloud Identity. We recommend that you configure sharing settings so that group owners can't add external members. Note that this restriction doesn't apply to the super admin account or to other delegated administrators with Google Groups admin permissions. Because federation from your identity provider runs with administrator privileges, the group sharing settings don't apply to this group synchronization. We recommend that you review controls in the identity provider and synchronization mechanism to ensure that non-domain members aren't added to groups, or that you apply group restrictions.  
Related information | 

  * [Set organization-wide policies for using groups](https://support.google.com/a/answer/167097#zippy=%2Ckeep-your-organizations-groups-completely-private)
  * [Restrict group membership](https://support.google.com/a/answer/11192679)

  
Item ID | MVSP-CO-1.3  
Mapping |  Related NIST-800-53 controls:

  * AC-2
  * AC-3
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-5.1

  
Item | 

### Set daily session length  
  
---|---  
Description | Set the session length for Google Cloud services to expire at least once a day. Leaving an account signed in for an extended period is a security risk. Enforcing a maximum session duration automatically ends the session after a set time, forcing a new, secure sign-in.This practice reduces the opportunity for a malicious user to use a stolen password and ensures access is regularly reverified.  
Related information | 

  * [Set session length for Google Cloud services](https://support.google.com/a/answer/9368756)
  * [Set session length for Google services](https://support.google.com/a/answer/7576830)

  
Item ID | MVSP-CO-1.11  
Mapping |  Related NIST-800-53 controls:

  * AC-12

Related CRI profile controls:

  * PR.AC-7.1

  
Item | 

### Remediate unmanaged consumer accounts  
  
---|---  
Description | Don't permit unmanaged consumer accounts. Consolidate any unmanaged consumer accounts, and consider a solution to prevent the creation of further unmanaged consumer accounts with your domain. Unmanaged consumer accounts are not governed by your joiner-mover-leaver (JML) processes, so they introduce the risk that an employee still has access to your resources after they leave their job. These accounts are also treated as external with regard to controls like domain restricted sharing.  
Related information | 

  * [Overview of consolidating accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts)
  * [Use the transfer tool to migrate unmanaged users](https://support.google.com/a/answer/6178640)

  
Item ID | MVSP-CO-1.5  
Mapping |  Related NIST-800-53 controls:

  * AC-2

Related CRI profile controls:

  * PR.AC-1.1

  
Item | 

### Enforce dedicated admins and multiparty approval  
  
---|---  
Description | Ensure that super admin accounts are separate from day-to-day user accounts. Super admin accounts must be dedicated accounts that are used only when making critical changes. For increased security, turn on multiparty approval for admin actions. Turning on multiparty approval means sensitive actions are approved by two administrators, which helps prevent attackers from compromising an admin account and lock out other admin users.  
Related information | 

  * [Multi-party approval for sensitive actions](https://support.google.com/a/answer/13790448)
  * [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373)
  * [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices)

  
Item ID | MVSP-CO-1.8  
Mapping |  Related NIST-800-53 controls:

  * AC-6

Related CRI profile controls:

  * PR.AC-4.1

  
Item | 

### Enable multi-factor authentication for all Google Accounts and Cloud Identity users  
  
---|---  
Description | Enable multi-factor authentication (MFA), also known as 2-step authentication (2SV) for all Google Accounts and Cloud Identity users, not just super admins. MFA for super admins is enabled by default. MFA adds another layer of defense because passwords alone often aren't a strong enough security measure.To help prevent phishing attacks that can lead to cryptocurrency mining attacks, use Titan Security Keys.  
Related information | 

  * [Protect your business with 2-Step Verification](https://support.google.com/a/answer/175197)
  * [Multi-factor authentication requirement for Google Cloud](https://docs.cloud.google.com/docs/authentication/mfa-requirement)
  * [Titan Security Keys](https://cloud.google.com/security/products/titan-security-key)

  
Item ID | MVSP-CO-1.10  
Mapping |  Related NIST-800-53 controls:

  * IA-2

Related CRI profile controls:

  * PR.AC-1.1

  
Item | 

### Revoke default creator roles  
  
---|---  
Description | Remove the domain-wide Project Creator and Billing Account Creator roles that are granted by default to all members in a new organization. New organizations grant the Project Creator and Billing Account Creator roles to all managed user identities in the domain. While these roles are useful for getting started, this configuration isn't intended for production environments. Letting billing accounts proliferate leads to increased administrative overhead and has technical consequences when splitting services across multiple Billing Accounts. Allowing free-form project creation can lead to projects that don't adhere to your governance conventions. Instead, remove these roles and establish a project creation process to request new projects and associate them with billing.  
Related information | 

  * [Managing default organization roles](https://docs.cloud.google.com/resource-manager/docs/default-access-control)

  
Item ID | MVSP-CO-1.6  
Mapping |  Related NIST-800-53 controls:

  * AC-6

Related CRI profile controls:

  * PR.AC-4.1

  
Item | 

### Use Privileged Access Manager  
  
---|---  
Description | Use Privileged Access Manager for managing privileged access. For all other access, use access groups, let group memberships expire automatically, and implement an approval workflow for group memberships.Using the least privilege model lets you only provide access when needed, for the resources that are needed. Using pre-built roles simplifies use and reduces sprawl caused by custom roles so that you don't have to worry about managing the role lifecycle.  
Related information | 

  * [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview)

  
Item ID | MVSP-CO-1.18  
Mapping |  Related NIST-800-53 controls:

  * AC-2
  * AC-3
  * AC-6

Related CRI profile controls:

  * PR.AC-4.1

  
Item | 

### Disable automatic IAM grants for default service accounts  
  
---|---  
Description | Use the `automaticIamGrantsForDefaultServiceAccounts` boolean constraint to disable automatic role grants when Google Cloud services automatically create default service accounts with overly permissive roles.By default, some systems grant overly broad permissions to automated accounts, which is a potential security risk. For example, if you don't enforce this constraint and you create a default service account, the service account is automatically granted the Editor role (`roles/editor`) on your project. If an attacker compromises a single part of the system, they could gain control over the entire project. This constraint disables those automatic, high-level permissions, forcing a more secure, deliberate approach where only the minimal necessary permissions are granted.  
Related information | 

  * [Types of service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default)

  
Item ID | MVSP-CO-1.14  
Mapping |  Related NIST-800-53 controls:

  * AC-3
  * AC-17
  * AC-20

Related CRI profile controls:

  * PR.AC-3.1
  * PR.AC-3.2
  * PR.AC-4.1
  * PR.AC-4.2
  * PR.AC-4.3
  * PR.AC-6.1
  * PR.PT-3.1
  * PR.PT-4.1

Compliance Manager control:

  * [Block Automatic IAM Grants to Default Service Accounts](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#block-automatic-iam-grants-to-default-service-accounts)

  
Item | 

### Rotate service account keys  
  
---|---  
Description | If you must use service account keys, rotate the keys at least once every 90 days.A rotation interval limits how long an attacker can have access to the system. Without a rotation interval, the attacker has access forever. Where possible, consider using Workload Identity Federation instead of service account keys.  
Related information | 

  * [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)
  * [Choose the right authentication method for your use case](https://docs.cloud.google.com/docs/authentication#auth-decision-tree)

  
Item ID | MVSP-CO-1.15  
Mapping |  Related NIST-800-53 controls:

  * SC-12

Related CRI profile controls:

  * PR.DS-1.1

Compliance Manager control:

  * [Require Service Account Key Rotation](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-service-account-key-rotation)

  
Item | 

### Use Workload Identity Federation  
  
---|---  
Description | Use Workload Identity Federation to let CI/CD systems and workloads running on other clouds authenticate to Google Cloud. Workload Identity Federation lets workloads that run outside of Google Cloud authenticate without requiring a service account key. By avoiding service account keys and other long-lived credentials, Workload Identity Federation can help you reduce the risk of credential leakage.  
Related information | 

  * [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)

  
Item ID | MVSP-CO-1.16  
Mapping |  Related NIST-800-53 controls:

  * IA-2

Related CRI profile controls:

  * PR.AC-1.1

  
  
## Advanced level guidelines

After you implemented the intermediate guidelines, implement the following authentication and authorization guidelines.

Item | 

### Block account self-recovery for super admin accounts  
  
---|---  
Description | By default, super admin account self-recovery is off for new customers. However, existing customers might have this setting on. Turning this setting off helps to mitigate the risk that a compromised phone, a compromised email, or a social engineering attack might let an attacker gain super admin privileges over your environment. Plan an internal process for a super admin to contact another super admin in your organization if they have lost access to their account, and ensure that all super admins are familiar with the process for support-assisted recovery. To turn off the feature, go to the account recovery settings in the Google Admin console.  
Related information | 

  * [Manage a user's security settings](https://support.google.com/cloudidentity/answer/2537800)
  * [Recovering administrator access to your account](https://support.google.com/a/answer/33561)

  
Item ID | MVSP-CO-1.2  
Mapping |  Related NIST-800-53 controls:

  * AC-2
  * AC-3

Related CRI profile controls:

  * PR.AC-1.1
  * PR.AC-4.1

  
Item | 

### Set idle session timeout for sensitive use cases  
  
---|---  
Description | Set the idle session timeout to 15 minutes for sensitive use cases. Idle sessions might be used by attackers for credential theft.  
Related information | 

  * [Set session length for Google services](https://support.google.com/a/answer/7576830)

  
Item ID | MVSP-CO-1.12  
Mapping |  Related NIST-800-53 controls:

  * AC-12

Related CRI profile controls:

  * PR.AC-7.1

  
Item | 

### Enforce hardware security keys for administrators  
  
---|---  
Description | Provide hardware security keys, if possible, to super admins or Organization Administrators as a second factor. Super admin accounts are the highest-value targets for sophisticated attacks. Hardware security keys provide a high level of protection because they are phishing-resistant. Hardware security keys are the strongest possible defense against account takeover for your most critical administrators and build on your standard MFA policy.  
Related information | 

  * [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373)
  * [Use a security key for 2-Step Verification](https://support.google.com/accounts/answer/6103523)

  
Item ID | MVSP-CO-1.13  
Mapping |  Related NIST-800-53 controls:

  * IA-2

Related CRI profile controls:

  * PR.AC-1.1

  
Item | 

### Enable post-SSO verification  
  
---|---  
Description | If you're using an external identity provider, set up post-SSO verification. Enable an additional layer of control based on Google's sign-in risk analysis. After you apply this setting, users might see additional risk-based login challenges at sign-in if Google determines that a user sign-in is suspicious.  
Related information | 

  * [Enable login challenges with SSO](https://support.google.com/a/answer/6002699#ssochallenges&zippy=%2Cset-up-post-sso-verification)

  
Item ID | MVSP-CO-1.1  
Mapping |  Related NIST-800-53 controls:

  * IA-2
  * IA-5
  * IA-8

Related CRI profile controls:

  * PR.AC-1.1
  * PR.AC-1.2
  * PR.AC-3.1
  * PR.AC-6.1
  * PR.AC-7.1
  * PR.AC-7.2

  
Item | 

### Enable principal access boundary policies  
  
---|---  
Description | Enable principal access boundary (PAB) policies to limit principal access and help protect against phishing and data exfiltration. Enable a PAB policy for the organization to avoid external phishing attacks. PABs improve security by reducing the extent of an attack with a compromised identity, and they also help prevent any external phishing attacks and other exfiltration attacks.  
Related information | 

  * [Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)

  
Item ID | MVSP-CO-1.19  
Mapping |  Related NIST-800-53 controls:

  * AC-3

Related CRI profile controls:

  * PR.AC-3.1

  
  
## What's next

  * [Organization guidelines](https://docs.cloud.google.com/docs/security/gcmvsp/organization)
  * [Overview of minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
