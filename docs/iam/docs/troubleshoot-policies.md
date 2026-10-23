---
url: https://docs.cloud.google.com/iam/docs/troubleshoot-policies/
title: Troubleshoot policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:57.513990+00:00
---

# Troubleshoot policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/troubleshoot-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Troubleshoot policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot Identity and Access Management (IAM) allow, deny, and Principal Access Boundary policies.

## Use Policy Troubleshooter

If you need to troubleshoot access for a specific principal, use Policy Troubleshooter for IAM.

Policy Troubleshooter helps you understand whether a principal can access a resource. Given a principal, a resource, and a permission, Policy Troubleshooter examines the allow policies, deny policies, and Principal Access Boundary (PAB) policies that impact the principal's access. Then, it tells you whether, based on those policies, the principal can use the specified permission to access the resource. It also lists the relevant policies and explains how they affect the principal's access. 

To learn how to use Policy Troubleshooter to troubleshoot allow policies, deny policies, and Principal Access Boundary policies, see [Troubleshoot IAM permissions](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access).

## Required roles

To get the permissions that you need to view all allow and deny policies, ask your administrator to grant you the [Security Reviewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`) IAM role on the organization that contains the resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View all allow and deny policies that apply to a resource

In Google Cloud, the following allow and deny policies affect access to a resource: 

  * The resource's allow policy 
  * The resource's deny policies, if any 
  * The allow policies of the resource's parent project, folder, and organization, if any 
  * The deny policies of the resource's parent project, folder, and organization, if any 



The allow and deny policies of parent projects, folders, and organizations affect access to a resource because of [policy inheritance](https://docs.cloud.google.com/iam/docs/policies#inheritance). When you attach an allow or deny policy to a project, folder, or organization, that policy also applies for all resources inside that project, folder, or organization. 

For example, if a deny policy for an organization says that a principal can't use a specific permission, then the principal can't use that permission for any resource within the organization. This rule applies even if the folders and projects within that organization have more permissive deny policies, or allow policies that give the principal the permission. 

Similarly, if an allow policy for a project gives a principal a specific permission, then the principal has that permission for any resource within the project, provided that they aren't denied that permission. 

The union of all of these policies is called the _applicable policy_ or _effective policy_ for the resource.

In Google Cloud, you can get a list of all of the allow and deny policies that affect access to a project by using the `gcloud beta projects get-ancestors-iam-policy` command with the `--include-deny` flag. Together, these policies make up the applicable policy for the project. You can investigate each policy to see how it affects the principal's access.

### gcloud

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



Execute the [`gcloud beta projects get-ancestors-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/get-ancestors-iam-policy) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud beta projects get-ancestors-iam-policy PROJECT_ID --include-deny --format=json

#### Windows (PowerShell)
    
    
    gcloud beta projects get-ancestors-iam-policy PROJECT_ID --include-deny --format=json

#### Windows (cmd.exe)
    
    
    gcloud beta projects get-ancestors-iam-policy PROJECT_ID --include-deny --format=json

The response contains the allow and deny policies for the project; any folders that are ancestors of the project; and the organization. The following example shows allow policies for the organization `1234567890123` and the project `my-project`, as well as a deny policy for the project `my-project`: 
    
    
    [
      {
        "id": "1234567890123",
        "policy": {
          "bindings": [
            {
              "members": [
                "group:cloud-admins@example.com"
              ],
              "role": "roles/iam.denyAdmin"
            },
            **{
              "members": [
                "user:raha@example.com"
              ],
              "role": "roles/iam.serviceAccountAdmin"
            }**
          ],
          "etag": "BwXW6Eab7TI=",
          "version": 1
        },
        "type": "organization"
      },
      {
        "id": "my-project",
        "policy": {
          "bindings": [
            {
              "members": [
                "group:cloud-admins@example.com"
              ],
              "role": "roles/owner"
            }
          ],
          "etag": "BwXXjOM7L6M=",
          "type": "project"
        }
      },
      {
        "id": "my-project",
        "policy": {
          "createTime": "2022-02-14T21:46:35.865279Z",
          "displayName": "My deny policy",
          "etag": "MTgyMzg2ODcwNTEyMjMxMTM3Mjg=",
          "kind": "DenyPolicy",
          "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F123456789012/denypolicies/my-deny-policy",
          "rules": [
            **{
              "denyRule": {
                "deniedPermissions": [
                  "iam.googleapis.com/serviceAccounts.create"
                ],
                "deniedPrincipals": [
                  "user:raha@example.com"
                ]
              },
              "description": "Prevent service account creation"
            }**
          ],
          "uid": "c83e3dc3-d8a6-6f51-4018-814e9f200b05",
          "updateTime": "2022-02-14T21:46:35.865279Z"
        },
        "type": "project"
      }
    ]
    

In this example, Raha is granted the Service Account Admin role (`roles/iam.serviceAccountAdmin`) on the organization, but the project has a deny policy that prevents Raha from using the permission `iam.googleapis.com/serviceAccounts.create`. As a result, if Raha tries to create a service account in the project `my-project`, the request will be denied.

In some cases, you might only need to view the effective allow policy for a resource—for example, if your organization doesn't use deny policies. In these cases, you can use the following methods to view the effective allow policy:

  * View the resource's IAM allow policy in the Google Cloud console. The Google Cloud console automatically shows each resource's effective policy.

To learn how to view a resource's IAM allow policy in the Google Cloud console, see [View current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#view-access).

  * Use the Cloud Asset API to get the resource's effective allow policy. To learn more, see [Viewing effective IAM policies](https://docs.cloud.google.com/asset-inventory/docs/view-effective-iam-policies).




## Search allow policies

If you need to locate a specific role binding in an allow policy, you can search the allow policy.

Cloud Asset Inventory lets you search allow policies for role bindings that match the specified parameters. You can use a variety of search parameters, including the following:

  * Resource type
  * Principal type
  * Role
  * Project
  * Folder
  * Organization



For more information, see [Searching IAM allow policies](https://docs.cloud.google.com/asset-inventory/docs/searching-iam-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
