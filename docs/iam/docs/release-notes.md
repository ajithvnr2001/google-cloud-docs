---
url: https://docs.cloud.google.com/iam/docs/release-notes/
title: IAM release notes \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:07.144047+00:00
---

# IAM release notes  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Resources ](https://docs.cloud.google.com/iam/docs/resources)



Send feedback 

#  IAM release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Identity and Access Management. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

**Note:** To learn about changes to the IAM permissions for each Google Cloud service, see the [permissions change log](https://docs.cloud.google.com/iam/docs/permissions-change-log).

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/iam-release-notes.xml) directly. 

## October 06, 2026

Feature

Revoking active sessions and short-lived credentials for Workforce Identity Federation users (principals) across all clients is [generally available](https://cloud.google.com/products#product-launch-stages). You can revoke workforce user sessions by using the gcloud CLI or the REST API.

For more information, see [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions).

## September 21, 2026

Feature

You can use System for Cross-domain Identity Management (SCIM) data as the source for both user and group claims in the OAuth sign-in workflows for Looker. You can also use Extended Session Length (ESL) when using SCIM.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see the following:

  * [SCIM provisioning for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim)
  * [Configure SCIM with Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra)
  * [Configure SCIM with Okta](https://docs.cloud.google.com/iam/docs/configure-scim-okta)
  * [Troubleshoot SCIM provisioning and synchronization](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#scim-signin-users-groups-fail)



## September 16, 2026

Feature

The Cloud OAuth API (`cloudoauth.googleapis.com`) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

The Cloud OAuth API provides dedicated OAuth 2.0 and OpenID Connect (OIDC) token exchange and authentication endpoints for Workforce Identity Federation integrations. Applications can use the Cloud OAuth API to exchange external credentials, authorization codes, or refresh tokens for Google Cloud access tokens, or to retrieve authenticated user profile claims and enterprise group memberships.

For more information, see the following documentation:

  * [Cloud OAuth API overview](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview)
  * [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens)
  * [Retrieve user info with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-userinfo)
  * [Retrieve enterprise groups with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-groups)



## September 10, 2026

Feature

The Identity and Access Management (IAM) Model Context Protocol (MCP) server is [generally available](https://cloud.google.com/products#product-launch-stages). You can connect to the IAM remote MCP server from AI applications to inspect and manage custom roles and deny policies across your resources.

For more information, see the following documentation:

  * [Use the IAM remote MCP server](https://docs.cloud.google.com/iam/docs/use-iam-mcp)
  * [IAM MCP reference](https://docs.cloud.google.com/iam/docs/reference/mcp)



## September 09, 2026

Feature

You can get IAM role suggestions from Gemini programmatically by using the Policy Assist API ([Preview](https://cloud.google.com/products#product-launch-stages)).

For more information, see the following documentation:

  * [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini)
  * [Policy Assist REST reference](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyassist/rest)



## August 22, 2026

Feature

The Agent Identity auth manager and the Agent Identity APIs (`agentidentity.googleapis.com` and `agentidentitycredentials.googleapis.com`) are [generally available](https://cloud.google.com/products#product-launch-stages).

Agent Identity auth manager provides a centralized credentials vault and authentication broker that simplifies outbound tool authentication for 3-legged OAuth, 2-legged OAuth, and API keys. The Agent Identity APIs replace the legacy IAM Connectors API (`iamconnectors.googleapis.com`) for managing auth providers and agent identities.

For more information, see the following documentation:

  * [Agent Identity auth manager overview](https://docs.cloud.google.com/iam/docs/auth-manager-overview)
  * [Manage Agent Identity auth providers](https://docs.cloud.google.com/iam/docs/manage-auth-providers-v2)
  * [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview)
  * [Agent Identity locations](https://docs.cloud.google.com/iam/docs/agent-identity-locations)



## August 14, 2026

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for Agent Identity resources, such as `agentidentity.googleapis.com/AuthProvider`. For more information, see [Use custom organization policies for Agent Identity](https://docs.cloud.google.com/iam/docs/agent-identity-custom-constraints). This feature is in [GA](https://cloud.google.com/products#product-launch-stages).

Feature

Agent Identity VPC Service Controls (VPC Service Controls) integration is [generally available](https://cloud.google.com/products#product-launch-stages). You can add the Agent Identity API (`agentidentity.googleapis.com`) and Agent Identity Credentials API (`agentidentitycredentials.googleapis.com`) to a service perimeter and specify agent identities in ingress and egress rules.

For more information, see [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

## August 12, 2026

Change

The workflow for creating workforce identity pool providers in the Google Cloud console changed. After submitting the initial provider configuration, the console directs you to a centralized page to configure provider attributes, including attribute mappings, attribute conditions, and extra attributes.

For more information, see [Manage workforce identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers).

## August 03, 2026

Feature

Organization Policy Service custom constraints are available for Privileged Access Manager (PAM). You can use custom constraints to restrict how users create and modify entitlements and grants. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Use custom organization policies for Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-custom-constraints).

## July 27, 2026

Feature

Managed workload identities for Compute Engine are [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Configure managed workload identity authentication for Compute Engine](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities).

## June 18, 2026

Feature

The Agent Identity API (`agentidentity.googleapis.com`) is available in [Preview](https://cloud.google.com/products#product-launch-stages). This new API replaces the legacy IAM Connectors API (`iamconnectors.googleapis.com`) for managing auth providers and agent identities.

During the preview migration period, both APIs operate side-by-side. Existing auth providers are automatically mirrored to the new V2 resource hierarchy (`authProviders/`), allowing you to migrate your IAM policies, agent code, and client applications without downtime.

## June 15, 2026

Feature

You can use the error ID provided in permission error messages to help troubleshoot access. Error IDs provide context for the error, including the principal, resource, permission, and supported IAM conditions. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Permission error messages](https://docs.cloud.google.com/iam/docs/permission-error-messages).

## May 08, 2026

Feature

You can use the IAM recommender to remediate excessive permissions for Google groups by transitioning from permanent role bindings to temporary, on-demand entitlements in Privileged Access Manager (PAM). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

To learn how to remediate excessive permissions, see [Remediate excessive permissions with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations).

## April 22, 2026

Feature

Privileged Access Manager supports [agent identities](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1) as grant requesters and approvers.

This feature is available in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview#supported-identities).

Feature

**Agent Identity auth manager** is available in [preview](https://cloud.google.com/products#product-launch-stages). You can use Agent Identity auth manager to help securely authenticate your agents to third-party services using 3-legged OAuth, 2-legged OAuth, or API keys.

For more information, see [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager).

Feature

**Agent Identity** is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Agent Identity provides a strongly attested, cryptographic identity for each agent that is tied to the lifecycle of the resource hosting the agent.

For more information, see [Agent Identity overview](https://docs.cloud.google.com/iam/docs/agent-identity-overview).

## April 13, 2026

Feature

Requesters can schedule grant requests in Privileged Access Manager up to seven days in advance. This lets requesters align access with scheduled maintenance or on-call shifts.

This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview#grant-scheduling).

## April 07, 2026

Feature

Organization Policy Service custom constraints are available for managed workload identity and Workload Identity Federation. You can use custom constraints to control how managed workload identity and Workload Identity Federation are used in your organization. For more information, see [Custom organization policy constraints for managed workload identity](https://docs.cloud.google.com/iam/docs/managed-workload-identity-custom-constraints) and [Custom organization policy constraints for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints).

## March 31, 2026

Feature

Gemini assistance in the IAM role picker is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini).

## March 18, 2026

Feature

Managed workload identities are [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Managed workload identities overview](https://docs.cloud.google.com/iam/docs/managed-workload-identity).

## March 03, 2026

Feature

[Service account principal sets](https://docs.cloud.google.com/iam/docs/principals-overview#service-account) are [generally available](https://cloud.google.com/products#product-launch-stages). You can use service account principal sets to reference all service accounts or service agents in a project, folder, or organization when writing allow policies, deny policies, and access policies.

## February 27, 2026

Feature

The ability to self-grant missing permissions from permission error messages is [generally available](https://cloud.google.com/products#product-launch-stages).

To learn how to request missing permissions, see [Request missing permissions](https://docs.cloud.google.com/iam/docs/request-missing-permissions).

Feature

You can disable the option to send auto-generated access requests from permission error messages. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

To learn how to disable these requests, see [Disable auto-generated access request emails](https://docs.cloud.google.com/iam/docs/resolve-permission-errors#disable-autogenerated-requests).

## December 15, 2025

Change

You can ask Gemini for predefined role suggestions ([preview](https://cloud.google.com/products#product-launch-stages)) without enabling any APIs.

In addition, you can get custom role suggestions from Gemini using the Cloud Assist panel in the Google Cloud console.

For more information, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini).

Feature

A new infinite-scrolling UI for audit logs is available on the **Privileged Access Manager > Audit logs** page in the Google Cloud console. This interface update replaces pagination with clear data loading indicators and time boundaries to help facilitate event investigations.

This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## September 26, 2025

Feature

[Privileged Access Manager (PAM)](https://docs.cloud.google.com/iam/docs/pam-overview) offers the following features in [preview](https://cloud.google.com/products#product-launch-stages):

  * [Multi-level and multi-party approvals](https://docs.cloud.google.com/iam/docs/pam-overview#mp-approvals)
  * [Scope customization](https://docs.cloud.google.com/iam/docs/pam-overview#customize-scope)
  * [Service account approvals](https://docs.cloud.google.com/iam/docs/pam-overview#ser-acc-approvals)
  * [Inheritance support](https://docs.cloud.google.com/iam/docs/pam-overview#inheritance-support)
  * [Notification preferences customization](https://docs.cloud.google.com/iam/docs/pam-overview#customize-settings)
  * [Grant withdrawal](https://docs.cloud.google.com/iam/docs/pam-overview#grant-withdrawal)



Change

For Privileged Access Manager, notification emails for grant activation, activation failure, or denial no longer include approver details.

To learn how to view the approver details, see [Check grant status](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#check-status).

## September 12, 2025

Feature

IAM offers predefined roles that are tailored to specific job functions. These roles cover all of the permissions that a user might need to perform their job. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Predefined roles for job functions](https://docs.cloud.google.com/iam/docs/job-functions/roles-for-job-functions).

Feature

Permission errors in the Google Cloud console contain actionable steps for remediation. For more information, see [Troubleshoot permission error messages](https://docs.cloud.google.com/iam/docs/permission-error-messages).

## July 21, 2025

Feature

You can ask Gemini for predefined role suggestions using the IAM role picker in the Google Cloud console. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini).

## June 13, 2025

Change

Conditions that check the tags for a resource can also check other attributes, such as the resource name of the timestamp of the request. This feature is available in Preview. For more information, see [Resource tags](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags).

## May 28, 2025

Feature

Workforce Identity Federation supports [detailed audit logging](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#detailed-audit-logging), which you can use to troubleshoot attribute mapping issues. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

## May 15, 2025

Change

The predefined role reference and the permissions reference have been reorganized to improve performance and searchability. To see the new experience, visit the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## May 07, 2025

Feature

[Workload Identity Federation support for X.509 certificates](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates) is [generally available](https://cloud.google.com/products#product-launch-stages).

## May 05, 2025

Change

A new enforcement version, enforcement version 3, is available for principal access boundary policies. To learn more about enforcement versions and see the permissions that enforcement version 3 can block, see [Permissions that principal access boundary policies can block](https://docs.cloud.google.com/iam/docs/pab-blocked-permissions).

## February 24, 2025

Feature

Workforce Identity Federation can map up to 400 groups from Microsoft Entra ID. The feature is generally available. To learn more, see [Configure Workforce Identity Federation with Microsoft Entra ID and a large number of groups](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups).

Change

Workforce Identity Federation supports an [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) of up to 400 groups and a maximum size of 16 KB.

## December 16, 2024

Change

[Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) are generally available. You can use principal access boundary policies to limit the resources that a principal is eligible to access.

## December 09, 2024

Change

Using IAM attributes in custom organization policies is generally available. For more information, see [Use custom organization policies](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints).

Feature

You can use the `iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` managed organization policy constraint to prevent default service accounts from being granted the Editor (`roles/editor`) or Owner (`roles/owner`) roles. For more information, see [Prevent the Owner and Editor role from being granted to default service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#prevent-service-account-grants).

## September 16, 2024

Feature

[Privileged Access Manager (PAM)](https://docs.cloud.google.com/iam/docs/pam-overview) is now released to General Availability. The following features have been added:

  * [Alerting on any external modifications](https://docs.cloud.google.com/iam/docs/pam-view-grants#modified-through-iam) to access grants outside of PAM.
  * [VPC Service Controls integration for PAM](https://docs.cloud.google.com/iam/docs/secure-iam-vpc-sc#pam), which allows customers to enforce authorized network access or require specific access context while using PAM.
  * [Pub/Sub integration](https://docs.cloud.google.com/iam/docs/pam-overview#pubsub-notifications) for custom alerting and monitoring.



## September 12, 2024

Change

You can manage IAM deny policies using the Google Cloud console. For more information, see [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access).

## August 12, 2024

Feature

You can attach tags to Identity and Access Management (IAM) service accounts to conditionally grant or deny access to specific service accounts. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Creating and managing tags for service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-tags).

## July 30, 2024

Feature

You can use IAM attributes in custom organization policies to control how your allow policies can be modified. For more information, see [Use custom organization policies](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints).

## June 10, 2024

Feature

You can use [principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) to limit the resources that a principal is eligible to access. This feature is available in Preview.

## May 08, 2024

Feature

[Privileged Access Manager (PAM)](https://docs.cloud.google.com/iam/docs/pam-overview) lets you manage just-in-time temporary privilege elevation for select principals, and to view audit logs afterwards to find out who had access to what and when. This feature is in Preview.

## May 03, 2024

Change

As of May 3, 2024, when you create a new organization, it enforces the following organization policy constraints by default:

  * `iam.disableServiceAccountKeyCreation`
  * `iam.disableServiceAccountKeyUpload`
  * `iam.automaticGrantsForDefaultServiceAccounts`
  * `iam.allowedPolicyMemberDomains`



For more information, see [Restricting service account usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts) and [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).

## March 15, 2024

Change

You can use the [`iam.serviceAccountKeyExposureResponse` organization policy constraint](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable-exposed-keys) to help manage leaked service account credentials.

## March 05, 2024

Change

To improve performance, we've removed the ability to expand abbreviated permissions in the [predefined roles table](https://docs.cloud.google.com/iam/docs/roles-permissions). You can still filter the predefined roles table based on the full list of permissions included in a role.

## February 15, 2024

Feature

Managed workload identities let you bind strongly attested identities to your Compute Engine workloads. The feature is in Preview. Google Cloud provisions X.509 credentials, issued from Certificate Authority Service, that can be used to reliably authenticate your workload with other workloads over mutual TLS (mTLS) authentication. For more information, see [Managed workload identities overview](https://docs.cloud.google.com/iam/docs/managed-workload-identity).

## January 17, 2024

Change

IAM deny policies let you deny groups of permissions for certain services. For more information, see [Permission groups](https://docs.cloud.google.com/iam/docs/deny-overview#permission-groups).

## December 11, 2023

Change

You can use identities from workforce and workload identity pools in [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). For more information, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

## September 27, 2023

Feature

You can now configure [IAM workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) using the Google Cloud console. To learn more, see the configuration guides for [Azure AD](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad), [Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta), or other [OIDC and SAML 2.0 providers](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation). The feature is in General Availability (GA).

## September 13, 2023

Feature

You can now configure [IAM workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) using the Google Cloud console. To learn more, see the configuration guides for [Azure AD](https://docs.cloud.google.com/iam/docs/workforce-sign-in-azure-ad), [Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta), or other [OIDC and SAML 2.0 providers](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation). The feature is in Preview.

## August 14, 2023

Change

For [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials), removed the requirement to enable [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) for your Cloud Storage bucket.

## July 11, 2023

Change

[Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) now supports browser-based sign-in with the Google Cloud CLI. The feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). To use it, see [Browser-based sign-in in Obtain short-lived tokens for workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#browser-based-sign-in), or locate the _Browser-based sign-in_ section in the configuration guide for your identity provider.

## June 22, 2023

Feature

You can trigger service agent creation instead of waiting for service agents to be created automatically. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 05, 2023

Feature

[Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) and [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) can now accept encrypted SAML assertions. The feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). To use the feature, locate the _Create the workload identity pool and provider_ section in the configuration guide for your identity provider and follow the gcloud CLI instructions for the SAML workflow.

## March 13, 2023

Feature

[Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) now supports browser-based sign-in with the Google Cloud CLI. The feature is in [Preview](https://cloud.google.com/products#product-launch-stages). To use it, see [Browser-based sign-in in Obtain short-lived tokens for workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#browser-based-sign-in), or locate the _Browser-based sign-in_ section in the configuration guide for your identity provider.

## March 07, 2023

Feature

You can now [set an expiry time](https://docs.cloud.google.com/iam/docs/service-account-creds#key-expiry) for all newly created service account keys in your project, folder, or organization. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 03, 2023

Change

The IAM documentation has been reorganized. We made the following changes:

  * Reorganized the left-hand navigation for the **Guides** tab. 
  * Removed the **Support** tab and relocated its documents to the **Resources** and **Guides** tabs.



## February 10, 2023

Announcement

[Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). The feature lets you use an external identity provider to authenticate and authorize users to access [supported Google Cloud products](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

## December 14, 2022

Issue

For information about issues with workforce identity federation, see [Troubleshoot workforce identity federation](https://cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation)

## December 01, 2022

Issue

For some users, the [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles) is crashing or is very slow to load. We are working to mitigate this issue.

## November 09, 2022

Feature

You can use the Google Cloud console to [view authentication activities](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication), which indicate when your service accounts and keys were last used to call a Google API.

## October 25, 2022

Change

[Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) are generally available (GA). Use deny policies to prevent principals from using certain permissions, regardless of the roles they're granted.

## September 20, 2022

Change

[Conceptual](https://docs.cloud.google.com/iam/docs/roles-overview) and [reference](https://docs.cloud.google.com/iam/docs/understanding-roles) information for IAM basic and predefined roles has been improved. You can now filter the predefined roles table, expand abbreviated permissions to see all included permissions, and quickly identify [owner permissions](https://docs.cloud.google.com/iam/docs/roles-permissions).

## August 18, 2022

Feature

Workforce identity federation now lets users from external identity providers sign in to the [Google Cloud workforce identity federation console, also known as the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso). The console (federated) provides UI access to [supported Google Cloud products](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services). This feature is available in Preview.

## July 07, 2022

Feature

[Workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) lets you authenticate and authorize users from external identity providers to access supported Google Cloud products. This feature is available in Preview.

## June 30, 2022

Fixed

In June 2022, IAM had an issue that resulted in excess [usage metrics for service accounts and service account keys](https://docs.cloud.google.com/iam/docs/service-account-monitoring) when any of the following actions were performed:

  * [Listing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#list-keys)
  * [Getting a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#get-key)
  * [Disabling a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#disabling)
  * [Enabling a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#enabling)



Each time you took any of these actions, Cloud Monitoring recorded an authentication usage metric for the parent service account, and for each of its service account keys, regardless of whether you used the service account or its keys to authenticate. These excess metrics were visible in [Cloud Monitoring](https://docs.cloud.google.com/iam/docs/service-account-monitoring#view-metrics-all), and in the [metrics for individual service accounts and keys](https://docs.cloud.google.com/iam/docs/service-account-monitoring#view-metrics-single-sa), from June 7, 2022, through June 17, 2022.

In addition, these excess metrics were visible in other systems that use data from Cloud Monitoring, including [Activity Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication), which shows when service accounts and keys were used to authenticate, and [service account insights](https://docs.cloud.google.com/policy-intelligence/docs/service-account-insights), which provide findings about unused service accounts. Excess metrics were visible in these systems from June 7, 2022, through June 22, 2022. 

This issue has been corrected, and Cloud Monitoring is no longer recording these excess metrics. However, the [last authentication time](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication#view-recent-multiple-accounts-or-keys) for each service account and key will continue to reflect the excess metrics indefinitely, until you authenticate with the service account or key again.

## May 05, 2022

Change

Documentation for Activity Analyzer, IAM insights, IAM Policy Troubleshooter, IAM role recommendations, and IAM Policy Simulator has moved to the [Policy Intelligence documentation](https://docs.cloud.google.com/policy-intelligence/docs).

## April 29, 2022

Change

Support for using [workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) with any SAML 2.0-compatible identity provider is now generally available.

## April 25, 2022

Change

The IAM documentation now refers to "IAM policies" as "allow policies." You might continue to see references to "IAM policies" in other documentation.

This change does not affect REST APIs, client libraries, or flags for the `gcloud` CLI.

## April 22, 2022

Feature

IAM Conditions now provides [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes) for Cloud SQL backup sets. You can use these resource attributes to grant access to a subset of your Cloud SQL resources.

## March 25, 2022

Feature

IAM Conditions now provides [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes) for Apigee X. You can use these resource attributes to grant access to a subset of your Apigee X resources.

## March 03, 2022

Feature

You can now use [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) to prevent principals from using certain permissions, regardless of the roles they're granted. This feature is in Preview.

## January 27, 2022

Feature

You can now [set an expiry time](https://docs.cloud.google.com/iam/docs/service-accounts#key-expiry) for all newly created service account keys in your project, folder, or organization. This feature is in Preview. To use this feature, [request access to the Preview release](https://forms.gle/P8NZpgAjAJvtYbqa8).

## December 03, 2021

Change

The IAM documentation now explains how to [choose the most appropriate predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

## October 26, 2021

Feature

For [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials), you can now use updated authentication libraries for Go, Java, Node.js, and Python to automatically exchange OAuth 2.0 access tokens for downscoped tokens.

For details, see [Exchange and refresh the access token automatically](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#exchange-credential-auto).

## October 19, 2021

Change

The IAM page of the Cloud Console now lists [lateral movement insights](https://docs.cloud.google.com/iam/docs/manage-lateral-movement-insights) in addition to policy insights. Lateral movement insights are in Preview.

## October 13, 2021

Feature

You can now use [workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) with any SAML 2.0-compatible identity provider. This feature is in Preview.

## September 30, 2021

Change

[IAM role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) for folder- and organization-level roles are now generally available.

## September 20, 2021

Change

The IAM documentation now refers to the identities that can be granted access to a resource as _principals_. Previously, these identities were known as _members_.

This change does not affect the REST API, the client libraries, or the flags for the `gcloud` command-line tool.

Change

The [reference documentation for predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) now uses a new format that is easier to browse.

## September 16, 2021

Feature

You can now [disable and enable service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#disabling).

## August 27, 2021

Change

[Managing Google Groups from the Cloud Console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) is now generally available.

## August 02, 2021

Feature

You can now use [Activity Analyzer](https://docs.cloud.google.com/iam/docs/service-account-recent-usage) to see when your service accounts and keys were last used to call a Google API. This feature is in Preview.

## July 27, 2021

Feature

Recommender now generates [lateral movement insights](https://docs.cloud.google.com/iam/docs/recommender-overview#lateral-movement-insights), which identify roles that allow a service account in one project to impersonate a service account in another project. You can [manage lateral movement insights](https://docs.cloud.google.com/iam/docs/manage-lateral-movement-insights) using the `gcloud` command-line tool or the Recommender REST API. This feature is available in Preview.

## July 22, 2021

Feature

A C++ [client library](https://docs.cloud.google.com/iam/docs/reference/libraries) for IAM is now available. The client library supports the [IAM API](https://docs.cloud.google.com/iam/docs/reference/rest) and the [Service Account Credentials API](https://docs.cloud.google.com/iam/docs/reference/credentials/rest).

## July 21, 2021

Change

You can now [set limits on the Cloud Storage roles that a member can grant and revoke](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles). This is possible because Cloud Storage now recognizes the [`modifiedGrantsByRole`](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#api-attributes-iam) API attribute in conditions.

## June 10, 2021

Change

The documentation for [IAM role recommendations](http://cloud.google.com/iam/docs/recommender-overview) now has more detail about how insights are used to generate recommendations.

## May 14, 2021

Feature

You can now use the Google Cloud Console to manage [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). For details, see the documentation for your identity provider:

  * [Access resources from AWS](https://docs.cloud.google.com/iam/docs/access-resources-aws)
  * [Access resources from Microsoft Azure](https://docs.cloud.google.com/iam/docs/access-resources-azure)
  * [Access resources from an OIDC identity provider](https://docs.cloud.google.com/iam/docs/access-resources-oidc)



## May 10, 2021

Change

The ability to [attach service accounts to resources in other projects](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#attaching-different-project) is now generally available.

## April 09, 2021

Change

[Workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) is now generally available. You can use workload identity federation to grant access to Google Cloud resources from on-premises and multi-cloud workloads.

## April 07, 2021

Feature

You can now get [recommendations for folder- and organization-level role bindings](https://docs.cloud.google.com/iam/docs/recommender-managing) using the `gcloud` command-line tool and REST API. This feature is available in Preview.

## April 01, 2021

Change

[Policy Simulator](https://docs.cloud.google.com/iam/docs/understanding-simulator) is now generally available. You can use Policy Simulator to [simulate policy changes](https://docs.cloud.google.com/iam/docs/simulating-access) before you apply them.

## March 16, 2021

Change

Tags are now generally available. You can attach tags to resources, then [use the tags to manage access to your resources](https://docs.cloud.google.com/iam/docs/tags-access-control).

## March 04, 2021

Feature

For [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), available in beta, you can now use updated client libraries for C++, Go, Java, Node.js, and Python to automatically obtain Google credentials.

For details, see the documentation for your identity provider:

  * [Generating Google credentials on AWS](https://docs.cloud.google.com/iam/docs/access-resources-aws#generate)
  * [Generating Google credentials on Azure](https://docs.cloud.google.com/iam/docs/access-resources-azure#generate)
  * [Generating Google credentials with other providers](https://docs.cloud.google.com/iam/docs/access-resources-oidc#generate)



## February 24, 2021

Feature

You can now use [Policy Simulator](https://docs.cloud.google.com/iam/docs/understanding-simulator) to [simulate policy changes](https://docs.cloud.google.com/iam/docs/simulating-access) before you apply them. This feature is available in Preview.

## February 16, 2021

Feature

You can now use IAM conditions to [set limits on the roles that a member can grant and revoke](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles). This feature is generally available.

## February 09, 2021

Feature

You can now attach tags to resources, then [use the tags to manage access to your resources](https://docs.cloud.google.com/iam/docs/tags-access-control). This feature is available in Preview.

Issue

If you run one of the `gcloud` tool's `add-iam-policy-binding` commands, and the IAM policy contains conditional role bindings for that role, the `gcloud` tool prompts you to choose one of the condition expressions that exists in the policy. If you choose a condition expression that contains a comma, the command fails.

To work around this issue, use the `--condition` flag to specify a condition expression on the command line.

## January 20, 2021

Feature

You can now [troubleshoot conditional role bindings](https://docs.cloud.google.com/iam/docs/troubleshooting-access#troubleshoot-with-cond) by troubleshooting directly from audit log entries. This feature is available in Preview.

## December 17, 2020

Feature

You can now [attach service accounts to resources in other projects](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts#binding-different-project). This feature is available in Preview.

## December 14, 2020

Change

You can now use Cloud Monitoring to [check when your service accounts and service account keys were used](https://docs.cloud.google.com/iam/docs/service-account-monitoring). This feature is generally available.

## November 24, 2020

Change

IAM Conditions: Starting on February 26, 2021, if a permission check encounters an unsupported attribute in a conditional role binding, it will never interpret that part of the condition as granting access.

To prevent access issues, [limit the scope of conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#inherited-support) when necessary, especially if a condition checks the `resource.name` attribute.

## November 12, 2020

Feature

IAM Conditions now provides [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes) for Pub/Sub Lite. You can use these resource attributes to grant access to a subset of your Pub/Sub Lite subscriptions and topics.

## October 16, 2020

Feature

You can now [manage service account insights](https://docs.cloud.google.com/iam/docs/manage-service-account-insights) generated by the IAM recommender. This feature is available in beta.

Change

[Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials) are now [generally available](https://cloud.google.com/products/#product-launch-stages). Use Credential Access Boundaries to downscope the permissions that a short-lived credential can use to access a Cloud Storage bucket.

## October 15, 2020

Change

If a role binding in an IAM policy refers to a deleted member (for example, `deleted:user:tamika@example.com?uid=123456789012345678901`), you can now add role bindings for a newly created member with the same name (in this case, `user:tamika@example.com`). The role bindings always apply to the newly created member.

For details, see the documentation for [policies with deleted members](https://docs.cloud.google.com/iam/docs/policies#handle-deleted-members).

## October 09, 2020

Change

The documentation now provides [details about service agents](https://docs.cloud.google.com/iam/docs/service-agents) for all publicly available services. A service agent is a special type of service account that is created and managed by Google, and is used by Google Cloud services to access your resources.

## September 21, 2020

Feature

You can now use [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), available in beta, to grant access to Google Cloud resources from on-premises and multi-cloud workloads.

## September 17, 2020

Fixed

The issue with undeleting service accounts has been resolved. You can now undelete most service accounts that meet the [criteria for undeletion](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#undeleting).

## September 16, 2020

Change

The documentation now includes a [quickstart](https://docs.cloud.google.com/iam/docs/quickstart-client-libraries) demonstrating how to modify IAM policies using client libraries.

## September 09, 2020

Issue

You cannot [undelete most service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#undeleting) at this time. Our engineering team is working to resolve this issue.

## August 28, 2020

Feature

New features are available for [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials), currently in beta:

  * You can now manage permissions for Cloud Storage objects, in addition to buckets.
  * You can now use IAM Conditions to control which permissions are available in a short-lived OAuth 2.0 access token. For an example, see [Limit permissions for specific objects](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#example-object-startswith).
  * You can now use Credential Access Boundaries with a Cloud Storage bucket that does not use [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).



Change

For [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials), currently in beta, you must migrate to a new API endpoint, `sts.googleapis.com`. To learn how to use the new API endpoint, see [Exchanging the OAuth 2.0 access token](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#exchange-credential).

## August 25, 2020

Change

[Uploading public keys for service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#uploading) is now generally available.

## August 18, 2020

Change

The documentation now provides a [list of the resource types that accept IAM policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies).

## August 14, 2020

Feature

You can now use Cloud Monitoring to [check when your service accounts and service account keys were used](https://docs.cloud.google.com/iam/docs/service-account-monitoring). This feature is available in beta.

Feature

You can now use an organization policy to [extend the maximum lifetime for OAuth 2.0 access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) that you create for a service account.

## August 05, 2020

Feature

You can now [manage policy insights](https://docs.cloud.google.com/iam/docs/managing-insights) generated by the IAM recommender. This feature is generally available.

## July 31, 2020

Change

We are delaying the upcoming changes for [deleted members that are bound to a role](https://docs.cloud.google.com/iam/docs/release-notes#July_01_2020). These changes will take effect starting on September 14, 2020.

Change

The documentation now describes [best practices for using the IAM recommender](https://docs.cloud.google.com/iam/docs/recommender-best-practices).

## July 20, 2020

Change

We are delaying the upcoming changes for [deleted members that are bound to a role](https://docs.cloud.google.com/iam/docs/release-notes#July_01_2020). These changes will take effect starting on August 31, 2020.

## July 01, 2020

Change

The organization policy constraint to [prevent automatic role grants to IAM service accounts](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) is now [generally available](https://cloud.google.com/products/#product-launch-stages). To improve security, we strongly recommend that you enable this constraint.

Issue

Starting on July 27, 2020, if a binding in a policy refers to a deleted member (for example, `deleted:user:tamika@example.com?uid=123456789012345678901`), you cannot add a binding for a newly created member with the same name (in this case, `user:tamika@example.com`). If you try to add a binding for the newly created member, IAM will apply the binding to the deleted member instead.

To resolve this issue, see our guidance on [updating policies that contain deleted members](https://docs.cloud.google.com/iam/docs/policies#handle-deleted-members).

Change

Starting on July 27, 2020, IAM policies will identify deleted members that are bound to a role. Deleted members have the prefix `deleted:` and the suffix `?uid=numeric-id`.

For example, if you delete the account for the user `tamika@example.com`, and a policy binds that user to a role, the policy shows an identifier similar to `deleted:user:tamika@example.com?uid=123456789012345678901`.

For `SetIamPolicy` requests, you can use this new syntax starting on July 27. For `GetIamPolicy` and `SetIamPolicy` responses, you might see the new prefix and suffix in some, but not all, responses until we finish rolling out the change. We expect to complete the rollout by July 31, 2020.

See the documentation for a [detailed example](https://docs.cloud.google.com/iam/docs/policies#example-deleted-member), as well as guidance on [updating policies that contain deleted members](https://docs.cloud.google.com/iam/docs/policies#handle-deleted-members).

## June 22, 2020

Deprecated

Using the IAM API to sign JSON Web Tokens (JWTs) or binary blobs is now deprecated.

  * If you use the IAM API or its client libraries to sign JWTs or binary blobs, you must [migrate to the Service Account Credentials API](https://docs.cloud.google.com/iam/docs/migrating-to-credentials-api) before July 1, 2021.
  * If you use the `gcloud` command-line tool to sign JWTs, you must [prepare for changes to the `gcloud` tool](https://docs.cloud.google.com/iam/docs/migrating-to-credentials-api#gcloud) before July 1, 2021.



## May 19, 2020

Feature

You can now [manage Google Groups from the Cloud Console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console). This feature is available in beta.

## May 18, 2020

Change

Recommendations from the [IAM recommender](https://docs.cloud.google.com/iam/docs/recommender-overview) can now include [suggestions to create custom roles](https://docs.cloud.google.com/iam/docs/recommender-overview#custom-roles).

## April 01, 2020

Feature

When you [use a service account key to access Google Cloud](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts#auth-service-account-key), your audit logs now identify the key that was used.

## March 17, 2020

Change

[Forwarding rule attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#forwarding-rule) for IAM Conditions are now [generally available](https://cloud.google.com/products/#product-launch-stages). You can use these attributes to specify the types of [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) that a member can create.

## March 05, 2020

Feature

For Cloud Storage buckets, you can now use [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials), currently in beta, to downscope the permissions that a short-lived credential can use.

## February 28, 2020

Change

[IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) are now [generally available](https://cloud.google.com/products/#product-launch-stages). You can use IAM Conditions to define and enforce conditional, attribute-based access control for Google Cloud resources.

Feature

For IAM Conditions, you can now use the `extract()` function to [extract a value from a resource name](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#extract). This function enables condition expressions to refer to an arbitrary part of the resource name.

## February 21, 2020

Change

A version 1 [IAM policy](https://docs.cloud.google.com/iam/docs/policies) can now include [conditional role bindings](https://docs.cloud.google.com/iam/docs/conditions-overview). The role name in these bindings includes the string `withcond`, followed by a hash value. For example: `roles/iam.serviceAccountAdmin_withcond_2b17cc25d2cd9e2c54d8`

If you see the string `withcond` in an IAM policy, follow the steps in the [troubleshooting guide](https://docs.cloud.google.com/iam/docs/troubleshooting-withcond).

## February 18, 2020

Change

You can now learn about [IAM audit logging for service accounts](https://docs.cloud.google.com/iam/docs/audit-logging) and see [examples of audit logs for service accounts](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts).

## February 13, 2020

Change

The [IAM recommender](https://docs.cloud.google.com/iam/docs/recommender-overview) is now [generally available](https://cloud.google.com/products/#product-launch-stages). The IAM recommender helps you enforce the principle of least privilege by ensuring that members have only the permissions that they actually use.

## February 04, 2020

Feature

IAM Conditions now supports [forwarding rule attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#forwarding-rule), currently in beta. You can use these attributes to specify the types of [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) that a member can create.

## December 17, 2019

Change

[Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access) is now [generally available](https://cloud.google.com/products/#product-launch-stages). Use Policy Troubleshooter to determine why a user has access to a resource or doesn't have permission to call an API.

## December 13, 2019

Change

On December 9, we [announced](https://docs.cloud.google.com/iam/docs/release-notes#December_09_2019) that IAM policies would now identify deleted members. We have temporarily reverted this change. IAM policies no longer identify deleted members.

## December 12, 2019

Feature

[IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) are now available in public beta. You can use IAM Conditions to define and enforce conditional, attribute-based access control for Google Cloud resources.

## December 09, 2019

Change

IAM policies now identify deleted members that are bound to a role. Deleted members have the prefix `deleted:` and the suffix `?uid=[NUMERIC_ID]`.

For example, if you delete the account for the user `bob@example.com`, and a policy binds that user to a role, the policy shows an identifier similar to `deleted:user:bob@example.com?uid=123456789012345678901`.

For `SetIamPolicy` requests, you can use this new syntax starting today. For `GetIamPolicy` and `SetIamPolicy` responses, because we are still rolling out this change, you might see the new prefix and suffix in some, but not all, responses. We expect to complete the rollout by December 13, 2019.

Issue

If a binding in a policy refers to a deleted member (for example, `deleted:user:bob@example.com?uid=123456789012345678901`), you cannot add a binding for a newly created member with the same name (in this case, `user:bob@example.com`). If you try to add a binding for the newly created member, IAM will apply the binding to the deleted member instead.

## September 23, 2019

Feature

The [IAM recommender](https://docs.cloud.google.com/iam/docs/recommender-overview) is now available in beta. The IAM recommender helps you enforce the principle of least privilege by ensuring that members have only the permissions that they actually use.

## September 18, 2019

Feature

You can now [upload a public key for a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#uploading), which causes service account keys to be signed with that public key. This feature is available in beta.

## August 20, 2019

Change

The Service Account Credentials API is now [generally available](https://cloud.google.com/products/#product-launch-stages). Use this API to [create short-lived service account credentials](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials).

## March 28, 2019

Feature

When you [create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) or [update](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#updating) a service account, you can now provide a description of the service account.

## June 29, 2018

Feature

You can now [create short-lived service account credentials](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with the Service Account Credentials API, available in beta.

## February 27, 2018

Change

You can now learn how to [configure IAM roles to facilitate audit logging](https://docs.cloud.google.com/iam/docs/roles-audit-logging).

## January 31, 2018

Change

[Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) are now [generally available](https://cloud.google.com/products/#product-launch-stages). You can create a custom IAM role with one or more permissions, then grant that custom role to users in your organization.

For more information, see the following topics:

  * [Understanding custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles)
  * [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)
  * [Maintaining custom roles with Deployment Manager](https://docs.cloud.google.com/iam/docs/maintain-custom-roles-deployment-manager)
  * [Support level for permissions in custom roles](https://docs.cloud.google.com/iam/docs/custom-roles-permissions-support)



## September 27, 2017

Change

[Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) are now available in beta. You can create a custom IAM role with one or more permissions, then grant that custom role to users in your organization.

## September 14, 2017

Change

You can now refer to the [IAM permissions change log](https://docs.cloud.google.com/iam/docs/permissions-change-log) to determine what permissions have changed recently. Use this change log to help you maintain and troubleshoot your custom roles.

## July 06, 2017

Change

You can now learn how to configure [IAM roles for networking-related job functions](https://docs.cloud.google.com/iam/docs/job-functions/networking).

## June 28, 2017

Change

[Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) are now available in a public alpha. You can create a custom IAM role with one or more permissions, then grant that custom role to users in your organization.

## May 24, 2017

Change

You can now learn how to configure [IAM roles for billing-related job functions](https://docs.cloud.google.com/iam/docs/job-functions/billing).

## March 08, 2017

Feature

[Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) are now available in a private alpha. You can create a custom IAM role with one or more permissions, then grant that custom role to users in your organization.

## May 10, 2016

Change

IAM is now [generally available](https://cloud.google.com/products/#product-launch-stages).

## March 28, 2016

Change

Documentation is now available to help you [understand service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) and [use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely).

## March 08, 2016

Feature

IAM is now available in beta.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
