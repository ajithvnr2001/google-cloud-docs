---
url: https://docs.cloud.google.com/access-context-manager/docs/troubleshooting/
title: Troubleshoot Context-Aware Access \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:23:16.522125+00:00
---

# Troubleshoot Context-Aware Access  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Troubleshoot Context-Aware Access Stay organized with collections  Save and categorize content based on your preferences. 

This page helps security and cloud administrators diagnose and resolve issues with Access Context Manager access levels, Context-Aware Access service account bindings, certificate-based access, and managed mobile devices.

## Access level management issues

This section lists issues that you might encounter when managing access levels in Access Context Manager and provides suggestions for how to fix each of them.

### Cannot delete an access level used in Google Workspace Context-Aware Access policies

The following issue occurs when you attempt to delete an access level in Access Context Manager that is assigned to a Google Workspace Context-Aware Access policy.

Depending on the interface that you use, you receive one of the following error messages:

  * **Google Cloud console** :
        
        Cannot delete Access Level 'ACCESS_LEVEL_TITLE'. It's currently
        used in Google Workspace Context-Aware Access policies. To delete this
        Access Level, first remove it from all app assignments and default rules in
        the Google Workspace Admin Console.
        

  * **Google Cloud CLI** :
        
        ERROR: (gcloud.access-context-manager.levels.delete) FAILED_PRECONDITION:
        Cannot delete Access Level: ACCESS_LEVEL_NAME. This Access Level
        is currently being used by Google Workspace Context-Aware Access policies.
        Please remove the Access Level from all assignments in the Google Workspace
        Admin Console before attempting deletion.
        

  * **Access Context Manager API** :
        
        FAILED_PRECONDITION: WORKSPACE_CAA_LIEN_PROTECTED
        




Google Workspace Context-Aware Access policies and Access Context Manager share underlying access levels. To prevent accidental service disruptions for Google Workspace users, the system places a deletion lock (lien) on any access level that is assigned to a Google Workspace Context-Aware Access policy, whether the policy is in active, monitor, or warn mode.

To resolve this issue, remove the access level assignment in the Google Admin console before you delete the access level:

  1. Sign in to the [Admin console](https://admin.google.com).
  2. Go to **Security > Access and data control > Context-Aware Access**.
  3. Identify any core Google Workspace apps, SAML apps, or default API rules that have the access level assigned.
  4. Unassign the access level from those policies. For more information, see [Assign Context-Aware Access levels to apps](https://support.google.com/a/answer/9275380).
  5. After you remove the access level from all Google Workspace Context-Aware Access assignments, the system automatically removes the deletion lock. Retry [deleting the access level](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels#delete-an-individual-access-level) in the Google Cloud console or by using the gcloud CLI.



### Can't delete an access level referenced by another access level

You can receive this error when you attempt to delete an access level that is referenced as a condition in another basic or custom access level.

To resolve this issue, [check your access level dependencies](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels#check-access-level-dependencies) and [update any referencing access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels#update_an_access_level) to remove the dependency before you delete the access level.

### Locked out of the Google Cloud console after deleting or modifying an access level

The following issue occurs when administrators or users in a Google group are blocked from accessing the Google Cloud console or Google Cloud APIs after you delete or modify an access level that is referenced in a [Google Cloud access binding](https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings). Because Google Cloud access bindings don't place a deletion lock on referenced access levels, deleting an in-use access level causes access evaluations for the bound group to fail closed.

To resolve this issue and regain access, remove the affected users from the Google group in the Admin console:

  1. Sign in to the [Admin console](https://admin.google.com) using an administrator account that can manage Google groups.
  2. Go to **Directory > Groups** and select the Google group used in the [access binding](https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings).
  3. Remove the affected administrator or user accounts from the group to bypass the access binding and restore access to the Google Cloud console and Google Cloud APIs.
  4. After you regain access, [update or delete the access binding](https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings#modify-bindings) so that it references a valid access level, and then add the users back to the Google group.



## Service account issues

This section lists issues that you might encounter when configuring Context-Aware Access for service accounts and provides suggestions for how to fix each of them.

### Access is denied for a service account

The following issue occurs when Context-Aware Access denies a service account access to Google Cloud resources after you bind a Context-Aware Access policy.

This issue typically occurs for one of the following reasons:

  * You bound the Context-Aware Access policy in enforcement mode rather than dry-run mode.
  * The access level doesn't include all required sources, such as an IP address that you didn't include when you created the access level.
  * Your user identity is a member of a Google group that has a bound Context-Aware Access policy restricting user access, which prevents call flow to the service account.



To resolve this issue, complete the following steps:

  1. Use [dry-run mode](https://docs.cloud.google.com/access-context-manager/docs/set-up-caa-service-accounts#dry-run) instead of enforcement mode to let service accounts access resources and log enforcement events without denying access.
  2. Review Cloud Audit Logs entries by running the following log query:
         
         protoPayload.serviceName="contextawareaccess.googleapis.com"
         

  3. Check the access level resource name that Context-Aware Access reports in the Cloud Audit Logs entries.

  4. Confirm that the access level is an organization-level resource and only uses [attributes that are supported for service accounts](https://docs.cloud.google.com/access-context-manager/docs/set-up-caa-service-accounts#access-level-attributes-for-service-accounts).

  5. Verify that the Context-Aware Access policy is bound to the intended service account and that the access level includes all required IP addresses or source networks.

  6. Verify that your user identity isn't restricted by a group-level Context-Aware Access policy.




## Certificate-based access issues

This section lists issues that you might encounter when using certificate-based access for workloads or enterprise certificates and provides suggestions for how to fix each of them.

### 403 Forbidden error when authorizing workloads

The following issue occurs when a workload attempts to access a Google Cloud resource by using certificate-based access for Workload Identity Federation:
    
    
    403 Forbidden, user does not have permission.
    

To resolve this issue, check your Identity and Access Management (IAM) policy to verify that the workload identity pool has access to your Google Cloud resource. For more information, see [Configure certificate-based access for Workload Identity Federation](https://docs.cloud.google.com/access-context-manager/docs/configure-cba-for-workloads).

### Unauthorized client error for the `google.subject` attribute

The following issue occurs when the backend can't extract a value for the `google.subject` attribute from a client certificate based on your attribute mapping:
    
    
    Unauthorized_client: Could not obtain a value for google.subject from the given
    credential.
    

To resolve this issue, inspect your client certificate and verify that the certificate field referenced in your attribute mapping contains a valid value.

### Unexpected access denials after enabling Context-Aware Access bindings

The following issue occurs when Context-Aware Access unexpectedly denies valid workload requests after you enable a Context-Aware Access binding.

To resolve this issue, unblock traffic while continuing to evaluate access and generate audit logs by moving the Context-Aware Access binding to dry-run mode:
    
    
    gcloud alpha access-context-manager cloud-bindings update \
        --binding=BINDING_ID \
        --organization=ORG_ID \
        --level= \
        --dry-run-level=DRY_RUN_ACCESS_LEVEL_ID
    

Replace the following:

  * `BINDING_ID`: the ID of the Context-Aware Access binding.
  * `ORG_ID`: the ID of your organization.
  * `DRY_RUN_ACCESS_LEVEL_ID`: the full resource name of the dry-run access level—for example, `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.



Alternatively, you can delete the Context-Aware Access binding to immediately unblock traffic:

**Caution:** Deleting a Context-Aware Access binding removes access policy enforcement and stops generating audit logs for access evaluations. Prefer dry-run mode so you can diagnose the cause of the access denials.
    
    
    gcloud alpha access-context-manager cloud-bindings delete \
        --binding=BINDING_ID \
        --organization=ORG_ID
    

After you restore access, review [Context-Aware Access audit logs](https://docs.cloud.google.com/access-context-manager/docs/audit-logs) to determine why Context-Aware Access denied the requests.

### Enterprise certificate condition fails validation

The following issue occurs when an access level denies access to a device with an enterprise certificate even though you configured [enterprise certificate conditions](https://docs.cloud.google.com/access-context-manager/docs/enterprise-certificates).

To resolve this issue, verify the certificate attributes and collect Endpoint Verification logs for debugging:

  1. In the [Admin console](https://admin.google.com), review the certificate attributes on the device details page to verify that they match the issuer and attributes in your custom access level.
  2. In the Google Chrome browser, enter `chrome://policy` in the address bar and verify that `AutoSelectCertificateForUrls` is set to **Machine** (or **Current User** on ChromeOS) and doesn't show a **Conflict** status.
  3. Download the Endpoint Verification extension logs to inspect certificate selection errors: 
     1. Right-click the Endpoint Verification extension and select **Options**.
     2. Select **Log level > All > Download Logs**.
     3. If the issue persists, open a support case with [Cloud Customer Care](https://docs.cloud.google.com/support) and share the logs for further debugging.



## Mobile device issues

This section lists issues that you might encounter when using mobile devices with access levels and provides suggestions for how to fix each of them.

### Access level denies requests from a compliant mobile device

The following issue occurs when an access level denies a user request from an Android or iOS mobile device even though the access level and [mobile device management settings](https://docs.cloud.google.com/access-context-manager/docs/use-mobile-devices) are configured properly.

This issue occurs when the server-side device state hasn't refreshed or when the request doesn't originate from Safari or Chrome while signed in to an organization user account.

To resolve this issue, verify that the request originates from Safari or Chrome using an organization user account, and then force a refresh of the server-side device state:

  * **Android devices** :

    1. If you're signed in to `accounts.google.com` in your device's browser, sign out of the account.
    2. Open your device's **Settings** app and go to **Accounts**.
    3. Remove the corporate Google Account from the device.
    4. Add the corporate Google Account back to the device.
  * **iOS devices** :

    1. If you're signed in to `accounts.google.com` in your device's browser, sign out of the account.
    2. Open a Google app on the device, such as Gmail.
    3. Remove the corporate Google Account from the device.
    4. Add the corporate Google Account back to the device.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
