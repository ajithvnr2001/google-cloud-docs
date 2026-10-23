---
url: https://docs.cloud.google.com/iam/docs/permission-error-messages/
title: Permission error messages \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:01.305571+00:00
---

# Permission error messages  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/permission-error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Permission error messages Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the error messages that you might encounter if you don't have the required access permissions for a resource.

## Issues that cause permission error messages

The Google Cloud console, Google Cloud CLI, and REST API all display error messages when you try to access a resource that you don't have permission to access.

These error messages can be caused by any of the following:

  * **You don't have the required permissions.** You must have either an [allow policy role binding](https://docs.cloud.google.com/iam/docs/allow-policies) or an active [Privileged Access Manager entitlement](https://docs.cloud.google.com/iam/docs/pam-overview) for a role with the required permissions. If you don't have the required permissions, then Google Cloud displays an error message.


  * **There's a deny policy blocking access.** If a [deny policy](https://docs.cloud.google.com/iam/docs/deny-access) prevents you from using any of the required permissions, then Google Cloud displays an error message.


  * **You aren't eligible to access the resource.** If you're subject to any [Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies), then the resource that you're trying to access must be included in the policies' Principal Access Boundary rules. If it isn't, then Google Cloud displays an error message.


  * **The resource doesn't exist.** If the resource doesn't exist, then Google Cloud displays an error message.



The following sections show what these error messages look like for the Google Cloud console, gcloud CLI, and REST API.

### Google Cloud console error messages

In the Google Cloud console, error messages look similar to the following:

![](https://docs.cloud.google.com/static/iam/img/iam-error-message-2x.png)

These error messages contain the following information:

  * **The resource that you tried to access:** The resource name appears in the title of the error page and indicates the resource that you were trying to access when you encountered the permission error.
  * **The missing required permissions:** A list of the permissions that you need to have to access the resource.


  * **A list of[Privileged Access Manager entitlements](https://docs.cloud.google.com/iam/docs/pam-overview) with roles that contain the required permissions:** This list is non-exhaustive—it contains only the top entitlements that Google Cloud suggests to resolve the access issue.

This list is only available for permission errors that can be resolved by granting additional IAM roles.

You can click an entitlement to learn more about the entitlement and to request a grant against the entitlement. To learn more, see [Request a Privileged Access Manager access grant](https://docs.cloud.google.com/iam/docs/resolve-permission-errors#allow-pam).

If no entitlements contain the required permissions, then the error message page doesn't include the list of entitlements.



  * **A list of IAM roles that contain the required permissions:** This list is non-exhaustive—it contains a curated list of roles that Google Cloud suggests to resolve the access issue. Ordering is based on the type of actions permitted by the role, service relevance, and the number of permissions.

If you have the [permissions required to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions), then this section is titled **Select a role to grant**. If you don't have the required permissions, then this section is titled **Request a specific role**.

You can click a role to learn more about the role and request that the role be granted to you. If you have the permissions required to grant roles, then you can grant yourself the role instead of requesting it.

  * **A Policy Troubleshooter URL:** You can use this link to navigate to the Policy Troubleshooter summary for this access request.




### Google Cloud CLI and REST API error messages

The exact wording of the error message depends on the command that you run. However, it typically contains the following information:

  * The required permission
  * The resource you tried to perform an action on
  * The authenticating account
  * A unique identifier for the error
  * A link to a Policy Troubleshooter summary for this error



For example, if you don't have permission to list buckets in a project, you see an error message like the following:

### gcloud
    
    
    ERROR: (gcloud.storage.buckets.list) PERMISSION_DENIED:
    EMAIL_ADDRESS does not have
    storage.buckets.list access to the Google Cloud project. Permission
    'storage.buckets.list' denied on resource (or it may not exist). This command
    is authenticated as EMAIL_ADDRESS which
    is the active account specified by the [core/account] property.
    - '@type': type.googleapis.com/google.rpc.ErrorInfo
      domain: storage.googleapis.com
      metadata:
        permission: storage.buckets.list
        error_info_id: ERROR_ID
      reason: IAM_PERMISSION_DENIED
    

### REST
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'storage.buckets.list' denied on resource (or it may not exist). Remediate access with this Troubleshooter URL or share it with your administrator - https://console.cloud.google.com/iam-admin/troubleshooter;errorId=ERROR_ID .",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "forbidden",
            "domain": "global",
            "metadata": {
              "error_info_id": "ERROR_ID",
              "permission": "storage.buckets.list"
            }
          }
        ]
      }
    }
    

## What's next

  * If you don't have administrative permissions and you encounter a permission error message, see [Request missing permissions](https://docs.cloud.google.com/iam/docs/request-missing-permissions).
  * If you have administrative permissions and need to resolve a user access request, see [Resolve permission errors](https://docs.cloud.google.com/iam/docs/resolve-permission-errors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
