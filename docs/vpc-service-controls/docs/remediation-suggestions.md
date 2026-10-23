---
url: https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions/
title: Resolve access denials with remediation suggestions \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:12.713323+00:00
---

# Resolve access denials with remediation suggestions  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/remediation-suggestions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Resolve access denials with remediation suggestions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use VPC Service Controls remediation suggestions to diagnose and resolve access denials caused by service perimeters.

When VPC Service Controls denies an access request, the remediation engine analyzes the violation event and generates actionable, narrowly scoped recommendations. These suggestions let you grant required access and adhere to the principle of least privilege.

## How remediation suggestions work

Remediation suggestions are integrated directly into the [violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer) in the Google Cloud console. When you diagnose an access denial using a unique ID or troubleshooting token, the remediation engine evaluates the violation context and proposes configuration changes based on the violation type:

  * **Ingress violations** : The engine proposes a scoped ingress rule and, if applicable, lets you select an existing access level that satisfies the request context (recommended) or create a new context-aware access level (such as IP subnetworks, geographic regions, and device policy requirements) to authorize the caller.
  * **Egress violations** : The engine proposes a scoped egress rule specifying the source identity and target resources or operations outside the perimeter.
  * **VPC accessible services violations** : The engine suggests adding the requested service to the allowlist or updating perimeter restrictions.



A single access denial can involve multiple violation types, such as a combination of ingress, egress, and VPC accessible services violations. In these cases, the remediation engine generates suggestions that address all applicable violations. You can review the generated configuration changes and apply them directly to your service perimeter with one single click.

## Before you begin

  * Verify that you have the permissions required to view and apply remediation suggestions.
  * Ensure that you have the unique ID or troubleshooting token for the access denial that you want to resolve. You can retrieve this identifier from the denial error response, Cloud Audit Logs, or the [violation dashboard](https://docs.cloud.google.com/vpc-service-controls/docs/violation-dashboard). For more information, see [Retrieve errors from audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors).



### Required roles

To get the permissions that you need to view and apply remediation suggestions, ask your administrator to grant you the following IAM roles: 

  * Diagnose an access denial event and view remediation suggestions: [Access Context Manager Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`) on your access policy 
  * Fetch troubleshooting tokens from Cloud Audit Logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the projects containing VPC Service Controls audit logs 
  * Apply remediation suggestions and update service perimeters: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.editor) (`roles/accesscontextmanager.editor`) on your access policy 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view and apply remediation suggestions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and apply remediation suggestions:

  * Diagnose an access denial event and view remediation suggestions: 
    * `accesscontextmanager.accessLevels.list` on your access policy
    * `accesscontextmanager.policies.get` on your access policy
    * `accesscontextmanager.servicePerimeters.list` on your access policy
  * Fetch troubleshooting tokens from Cloud Audit Logs: `logging.logEntries.list` on the projects containing VPC Service Controls audit logs 
  * Apply remediation suggestions and update service perimeters: 
    * `accesscontextmanager.accessLevels.create` on your access policy
    * `accesscontextmanager.accessLevels.get` on your access policy
    * `accesscontextmanager.accessLevels.list` on your access policy
    * `accesscontextmanager.policies.get` on your access policy
    * `accesscontextmanager.servicePerimeters.get` on your access policy
    * `accesscontextmanager.servicePerimeters.update` on your access policy



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View and apply remediation suggestions

To view and apply remediation suggestions for an access denial, follow these steps:

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

If prompted, select your organization.

  2. On the **VPC Service Controls** page, click **Violation analyzer**.

  3. In the **Troubleshooting token (or unique ID)** field, enter the troubleshooting token or unique ID of the access denial.

  4. Click **Continue**.

  5. On the troubleshooting result page, in the **Protected resources accessed** , select the perimeter that denied access.

  6. Click **Review recommendation**. The **Remediation details** pane opens.

  7. Review the proposed remediation actions:

     * If the remediation requires an access level, configure the access level: 
       * **Select an existing access level (recommended)** : Click the **Existing access level** tab, and then select an access level that satisfies the request context in the **Select an existing access level** list.
       * **Create a new access level** : On the **New access level** tab, review the suggested access level name, IP subnetworks, geographic regions, and device constraints.
     * Review the proposed ingress rule, egress rule, or VPC accessible services changes for the service perimeter.
  8. To apply the suggested changes, click **Apply remediation**.




VPC Service Controls automatically provisions the new access level (if you chose to create one) and updates the service perimeter configuration.

## Remediation actions by violation type

The following table describes the actions that the remediation engine proposes based on the violation type:

Violation type | Suggested remediation action  
---|---  
Ingress violation | 

  * Lets you select an existing access level that matches the request context (recommended), or provisions a new context-aware access level matching the caller's IP subnetworks, geographic regions, or device policy.
  * Appends an ingress rule scoped to the caller identity, source access level or network, target service, method selectors, and resource.

  
Egress violation |  Appends an egress rule scoped to the source identity or project and the target service, method selectors, and external resource.   
VPC accessible services |  Adds the restricted service to the perimeter's VPC accessible services allowlist, or suggests updating restrictions if the service is unsupported.   
**Note:** Remediation suggestions use the request context that your account has permission to view. Users or administrators with broader permissions might receive more fine-grained recommendations.

## Example: Ingress remediation with an access level

Consider an access denial where an analyst (`analyst@example.com`) attempts to read an object from a Cloud Storage bucket in project `803311519563` from an external workstation (`198.51.100.42`).

To remediate this denial according to least privilege, the remediation engine proposes two chained actions:

### Action 1: Select an existing access level or create a scoped access level

To authorize the caller's workstation, you can either reuse an existing access level or create a new one:

  * **Select an existing access level (recommended)** : on the **Existing access level** tab, choose an existing access level that already matches the request context (for example, `corp_trusted_workstations`). We recommend reusing an existing access level to avoid creating duplicate access levels and to simplify policy management.
  * **Create a new access level** : alternatively, on the **New access level** tab, you can let the engine create a new access level scoped to the caller's workstation: 
    * **Name** : `accessPolicies/POLICY_ID/accessLevels/analyst_secure_workstation`
    * **IP subnetworks** : `198.51.100.0/24`
    * **Regions** : `US`
    * **Device policy** : requires screen lock, disk encryption, corporate-owned status, and administrator approval.



### Action 2: Append a scoped ingress rule to the perimeter

The engine appends a narrowly scoped ingress rule to the service perimeter that references either your selected existing access level or the newly created access level:

  * **Identities** : `user:analyst@example.com`
  * **Sources** : your selected existing access level (for example, `corp_trusted_workstations`) or the new `analyst_secure_workstation` access level
  * **Service** : `storage.googleapis.com`
  * **Method selectors** : `google.storage.objects.get`
  * **Resources** : `projects/803311519563`



When you click **Apply remediation** , VPC Service Controls applies the selected access level (or creates the new access level) and updates the service perimeter in sequence.

## Limitations

  * Sensitive data redaction: 
    * Redacted internal IP addresses cannot be used to generate specific access levels.
    * If caller identities are redacted or unavailable in audit logs, suggestions might use generic identities such as `ANY_USER_ACCOUNT`.
    * If service methods are not granularly supported, suggestions might use a wildcard (`*`).
    * If network names are inaccessible, suggestions fall back to project numbers.
  * Remediation suggestions require access denial details from Cloud Audit Logs. Events older than the log retention period (30 days by default) cannot be analyzed.
  * Remediation suggestions are available only at the organization level in the Google Cloud console.
  * Service patterns and certain third-party workforce identity pool configurations are not supported by the remediation engine.



## What's next

  * Learn more about [diagnosing access denials in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).
  * Monitor access denials using the [violation dashboard](https://docs.cloud.google.com/vpc-service-controls/docs/violation-dashboard).
  * Learn about [configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).
  * Read the [VPC Service Controls troubleshooting guide](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
