---
url: https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings/
title: Investigate identity and access findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:43.599196+00:00
---

# Investigate identity and access findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Investigate identity and access findings Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to work with findings for security issues that are related to identity and access (_identity and access findings_) in the Google Cloud console to investigate and identify potential misconfigurations.

You can view identity and access findings using the following Security Command Center pages:

  * **Identity** view on the **Findings** page
  * **Identity** view on the **Risk overview** page



## Before you begin

Make sure you completed the following tasks before continuing:

  * Learn about [Security Command Center's CIEM capabilities](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).
  * [Enable CIEM detection service](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service).



## View identity and access findings on the Findings page

The **Identity** view on the Security Command Center **Findings** page displays identity and access findings across all cloud environments.

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud organization.

  3. Select the **Identity** view.




The **Identity** view adds a filter condition to display only findings where the `domains.category` field contains the value `IDENTITY_AND_ACCESS`.

Use the **Quick Filters** panel and the **Query Editor** to filter results further.

  * To view only identity and access findings detected by a specific service, select the following **Source display name** values:

    * **CIEM** : Identify and access findings related to Microsoft Azure and AWS.

    * **IAM recommender** : Identify and access findings related to Google Cloud.

  * To filter the findings further, use the following attributes:

    * **Category** : Filters query the results for specific finding categories that you want to learn more about.
    * **Project ID** : Filters query the results for findings that relate to a specific project.
    * **Resource type** : Filters to query the results for findings that relate to a specific resource type.
    * **Severity** : Filters to query the results for findings of a specific severity.



The **Findings query results** panel consists of several columns that provide details about the finding. Among them, the following columns are of interest for CIEM purposes:

  * **Severity** : Displays the severity of a given finding to help you prioritize remediation.
  * **Resource display name** : Displays the resource where the finding was detected.
  * **Source display name** : Displays the service that detected the finding. Sources that produce identity-related findings include CIEM, IAM recommender, Security Health Analytics, and Event Threat Detection.
  * **Cloud provider** : Displays the cloud environment where the finding was detected, such as Google Cloud, AWS, and Microsoft Azure.
  * **Offending access grants** : Displays a link to review the principals who were potentially granted inappropriate roles.
  * **Case ID** : Displays the ID number of the case that is related to the finding. (Enterprise (Deprecated) service tier)



For more information about working with findings, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

## Inspect an identity and access finding in detail

To learn more about an identity and access finding, open the detailed view of the finding by clicking the finding name in the **Category** column in the **Findings** panel. For more information about the finding detail view, see [View the details of a finding](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings#finding-details).

The following sections on the **Summary** tab of the finding detail view are helpful when investigating identity and access findings.

### Offending access grants

On the **Summary** tab of the details pane of a finding, the **Offending access grants** row provides a way to quickly inspect principals, including [federated identities](https://docs.cloud.google.com/iam/docs/principals-overview#workforce), and their access to your resources. This information only appears for findings when IAM recommender detects principals on Google Cloud resources with highly permissive, basic, and unused roles.

Click **Review offending access grants** to open the **Review offending access grants** pane, which contains the following information:

  * The name of the principal. The principals displayed in this column can be a mix of Google Cloud user accounts, groups, federated identities, and service accounts.
  * The name of the role granted to the principal.
  * The recommended action you can take to remediate the offending access.



### Case information

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

On the **Summary** tab of the details page of a finding, the **Case information** section displays when there is a case or ticket that corresponds with a particular finding.

The **Cases information** section provides a way to track the remediation efforts for a particular finding. It provides details about the corresponding case, such as links to any corresponding case and ticketing system (Jira or ServiceNow) ticket, the assignee, case status, and case priority.

  * To access the case corresponding with the finding, click the case ID number in the **Case ID** row.

  * To access the Jira or ServiceNow ticket corresponding with the finding, click the ticket ID number in the **Ticket ID** row.




To connect your ticketing systems with Security Command Center Enterprise, see [Integrate Security Command Center Enterprise with ticketing systems](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems).

For more information on reviewing corresponding cases, see [Review identity and access finding cases](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases).

### Next steps

On the **Summary** tab of the details page of a finding, the **Next steps** section provides step-by-step guidance on how to immediately remediate the issue detected. These recommendations are tailored to the specific finding you are viewing.

## Identity and access findings generated for each cloud platform

Multiple Security Command Center services, such as CIEM, IAM recommender, Security Health Analytics, and Event Threat Detection generate CIEM-specific finding categories that detect potential identity and access security issues for your cloud platforms.

The CIEM detection service generates specific findings for your AWS and Microsoft Azure environments. The IAM recommender, Security Health Analytics, and Event Threat Detection services generate specific findings for your Google Cloud environment.

The following table describes all the findings that part of Security Command Center's CIEM capabilities.

Cloud platform | Finding category | Description | Source  
---|---|---|---  
AWS | `Assumed identity has excessive permissions` (`ASSUMED_IDENTITY_HAS_EXCESSIVE_PERMISSIONS`) | Assumed IAM roles detected in your AWS environment with highly permissive policies. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `Group has excessive permissions` (`GROUP_HAS_EXCESSIVE_PERMISSIONS`) | AWS IAM or AWS IAM Identity Center groups detected in your AWS environment with highly permissive policies. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `User has excessive permissions` (`USER_HAS_EXCESSIVE_PERMISSIONS`) | AWS IAM or AWS IAM Identity Center users detected in your AWS environment with highly permissive policies. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `User is inactive` (`INACTIVE_USER`) | Inactive AWS IAM or AWS IAM Identity Center users are detected in your AWS environment. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `Group is inactive` (`INACTIVE_GROUP`) | AWS IAM or AWS IAM Identity Center groups detected in your AWS environment are not active. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `Assumed identity is inactive` (`INACTIVE_ASSUMED_IDENTITY`) | Assumed IAM roles detected in your AWS environment are inactive. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `Overly permissive trust policy enforced on assumed identity` (`OVERLY_PERMISSIVE_TRUST_POLICY_ENFORCED_ON_ASSUMED_IDENTITY`) | The trust policy enforced on an assumed IAM role is highly permissive. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
AWS | `Assumed identity has lateral movement risk` (`ASSUMED_IDENTITY_HAS_LATERAL_MOVEMENT_RISK`) | One or more identities can move laterally in your AWS environment through role impersonation. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
Microsoft Azure | `Assumed identity has excessive permissions` (`ASSUMED_IDENTITY_HAS_EXCESSIVE_PERMISSIONS`) | Service principals or managed identities detected in your Azure environment with highly permissive role assignments. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
Microsoft Azure | `Group has excessive permissions` (`GROUP_HAS_EXCESSIVE_PERMISSIONS`) | Groups detected in your Azure environment with highly permissive role assignments. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
Microsoft Azure | `User has excessive permissions` (`USER_HAS_EXCESSIVE_PERMISSIONS`) | Users detected in your Azure environment with highly permissive role assignments. For more information, see [CIEM findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings). | CIEM  
Google Cloud | `MFA not enforced` (`MFA_NOT_ENFORCED`) | There are users who aren't using 2-Step Verification. For more information, see [Multi-factor authentication findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#mfa-findings). | Security Health Analytics  
Google Cloud | `Custom role not monitored` (`CUSTOM_ROLE_NOT_MONITORED`) | Log metrics and alerts aren't configured to monitor Custom Role changes. For more information, see [Monitoring vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#monitoring-findings). | Security Health Analytics  
Google Cloud | `KMS role separation` (`KMS_ROLE_SEPARATION`) | Separation of duties is not enforced, and a user exists who has any of the following Cloud Key Management Service roles at the same time: **CryptoKey Encrypter/Decrypter** , **Encrypter** , or **Decrypter**. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Primitive roles used` (`PRIMITIVE_ROLES_USED`) | A user has one of the following basic roles: **Owner** (`roles/owner`), **Editor** (`roles/editor`), or **Viewer** (`roles/viewer`). For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Redis role used on org` (`REDIS_ROLE_USED_ON_ORG`) | A Redis IAM role is assigned at the organization or folder level. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Service account role separation` (`SERVICE_ACCOUNT_ROLE_SEPARATION`) | A user has been assigned the **Service Account Admin** and **Service Account User** roles. This violates the "Separation of Duties" principle. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Non org IAM member` (`NON_ORG_IAM_MEMBER`) | There is a user who isn't using organizational credentials. Per CIS Google Cloud Foundations 1.0, only identities with @gmail.com email addresses trigger this detector. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Open group IAM member` (`OPEN_GROUP_IAM_MEMBER`) | A Google Groups account that can be joined without approval is used as an IAM allow policy principal. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Unused IAM role` (`UNUSED_IAM_ROLE`) | IAM recommender detected a user account that has an IAM role that has not been used in the last 90 days. For more information, see [IAM recommender findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iamrec-findings). | IAM recommender  
Google Cloud | `IAM role has excessive permissions` (`IAM_ROLE_HAS_EXCESSIVE_PERMISSIONS`) | IAM recommender detected a service account that has one or more IAM roles that give excessive permissions to the user account. For more information, see [IAM recommender findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iamrec-findings). | IAM recommender  
Google Cloud | `Service agent role replaced with basic role` (`SERVICE_AGENT_ROLE_REPLACED_WITH_BASIC_ROLE`) | IAM recommender detected that the original default IAM role granted to a service agent was replaced with one of the basic IAM roles: **Owner** , **Editor** , or **Viewer**. Basic roles are excessively permissive legacy roles and shouldn't be granted to service agents. For more information, see [IAM recommender findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iamrec-findings). | IAM recommender  
Google Cloud | `Service agent granted basic role` (`SERVICE_AGENT_GRANTED_BASIC_ROLE`) | IAM recommender detected that a service agent was granted one of the basic IAM roles: **Owner** , **Editor** , or **Viewer**. Basic roles are excessively permissive legacy roles and shouldn't be granted to service agents. For more information, see [IAM recommender findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iamrec-findings). | IAM recommender  
Google Cloud | `Admin service account` (`ADMIN_SERVICE_ACCOUNT`) | A service account has **Admin** , **Owner** , or **Editor** privileges. These roles shouldn't be assigned to user-created service accounts. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Default service account used` (`DEFAULT_SERVICE_ACCOUNT_USED`) | An instance is configured to use the default service account. For more information, see [Compute instance vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#compute-instance-findings). | Security Health Analytics  
Google Cloud | `Over privileged account` (`OVER_PRIVILEGED_ACCOUNT`) | A service account has overly broad project access in a cluster. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings). | Security Health Analytics  
Google Cloud | `Over privileged service account user` (`OVER_PRIVILEGED_SERVICE_ACCOUNT_USER`) | A user has the **Service Account User** or **Service Account Token Creator** role at the project level, instead of for a specific service account. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Service account key not rotated` (`SERVICE_ACCOUNT_KEY_NOT_ROTATED`) | A service account key hasn't been rotated for more than 90 days. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Over privileged scopes` (`OVER_PRIVILEGED_SCOPES`) | A node service account has broad access scopes. For more information, see [Container vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#container-findings). | Security Health Analytics  
Google Cloud | `KMS public key` (`KMS_PUBLIC_KEY`) | A Cloud KMS cryptographic key is publicly accessible. For more information, see [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings). | Security Health Analytics  
Google Cloud | `Public bucket ACL` (`PUBLIC_BUCKET_ACL`) | A Cloud Storage bucket is publicly accessible. For more information, see [Storage vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#storage-findings). | Security Health Analytics  
Google Cloud | `Public log bucket` (`PUBLIC_LOG_BUCKET`) | A storage bucket used as a log sink is publicly accessible. For more information, see [Storage vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#storage-findings). | Security Health Analytics  
Google Cloud | `User managed service account key` (`USER_MANAGED_SERVICE_ACCOUNT_KEY`) | A user manages a service account key. For more information, see [IAM vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iam-findings). | Security Health Analytics  
Google Cloud | `Too many KMS users` (`TOO_MANY_KMS_USERS`) | There are more than three users of cryptographic keys. For more information, see [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings). | Security Health Analytics  
Google Cloud | `KMS project has owner` (`KMS_PROJECT_HAS_OWNER`) | A user has **Owner** permissions on a project that has cryptographic keys. For more information, see [KMS vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#kms-findings). | Security Health Analytics  
Google Cloud | `Owner not monitored` (`OWNER_NOT_MONITORED`) | Log metrics and alerts aren't configured to monitor Project Ownership assignments or changes. For more information, see [Monitoring vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#monitoring-findings). | Security Health Analytics  
  
## What's next

  * Learn how to [review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).
  * Learn how to [review identity and access finding cases](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases).
  * Learn how to [review and manage identity risks in Policy Intelligence](https://docs.cloud.google.com/policy-intelligence/docs/manage-identity-risks).
  * Learn about the [CIEM detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#ciem-findings) that generate findings.
  * Learn about the [IAM recommender detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#iamrec-findings) that generate findings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
