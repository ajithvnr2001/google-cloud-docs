---
url: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-user-groups/
title: Enforce certificate-based access for a user group \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:17.797074+00:00
---

# Enforce certificate-based access for a user group  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/enable-cba-user-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Enforce certificate-based access for a user group Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enforce certificate-based access (CBA) using Context-Aware Access policies that are based on a user group.

You can restrict access to all Google Cloud services by binding a CBA access level to a user group. This restriction applies to all client applications that call Google Cloud APIs.

Optionally, you can apply the restrictions to specific client applications or exempt specific applications. The applications include both third-party applications and first-party applications built by Google, such as `Cloud Console` for the Google Cloud console and `Google Cloud SDK` for the [`Google Cloud CLI`](https://cloud.google.com/sdk/gcloud/reference).

## Before you begin

[Create a CBA access level](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels) that requires certificates when determining access to resources.

### Create a user group

[Create a user group](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console#creating) containing the members that should be granted access based on the CBA access level.

**Note:** Exclude at least one Organization Admin or Organization Owner from this group to reduce the risk of an accidental lockout.

### Assign the Cloud Access Binding Admin role

Assign the [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) role to the user group.

You must have sufficient privileges to add IAM permissions at the organization level. You need at least the [Organization Admin](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#setting-up) and the [Cloud Access Binding Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.gcpAccessAdmin) roles.

###  Console 

  1. In the console, go to **IAM**. 

[ Go to IAM](https://console.cloud.google.com/iam-admin)

  2. On the **Permissions** tab, click **Grant access** , then configure the following:

     1. **New principals** : Specify the group to which you want to grant the role.
     2. For **Select a role** option, select **Access Context Manager > Cloud Access Binding Admin**.
     3. Click **Save**.



###  gcloud 

  1. Sign in:
         
         gcloud auth login
         

  2. Assign the `GcpAccessAdmin` role by running the following command:
         
         gcloud organizations add-iam-policy-binding ORG_ID \
           --member=user:EMAIL \
           --role=roles/accesscontextmanager.gcpAccessAdmin
         

     * `ORG_ID` is the ID for your organization. If you don't already have your organization ID, you can use the following command to find it:
           
           gcloud organizations list
           

     * `EMAIL` is the email address of the person or group you want to grant the role to.

**Note:** For read-only access to the bindings, you can assign the `accesscontextmanager.gcpAccessReader` role.



### Bind a CBA access level to a user group

In this binding option, the CBA access level applies to all client applications for the user group that you specify.

  1. In the console, go to the Console & APIs Access Policy page:

[ Go to Console & APIs Access Policy](https://console.cloud.google.com/security/caa)

  2. Choose an organization, then click **Select**.

  3. Click **Manage access** to choose the user groups that should have access.

  4. Click **Add** , then configure the following:

     1. **Member groups** : Specify the group to which you want to grant access. You can only select groups that are not already bound to an access level.
     2. **Select access levels** : Select the CBA access level to apply to the group.
     3. Click **Save**.



### Bind a CBA access level to a user group and specific applications

In some use cases, such as applications that support client certificates, binding a CBA access level to a user group might be too broad. You can use this option to apply CBA access levels to applications that support client certificates.

The following example binds a CBA access level to the Google Cloud console, the gcloud CLI, and a user's OAuth application.

  1. Sign in to the gcloud CLI.
         
         gcloud auth application-default login
         

  2. Create a `policy_file.yaml` file.

You can specify applications using their OAuth client ID. To specify Google applications, use the application name, such as `Cloud Console` for the Google Cloud console. Only the Google Cloud console and Google Cloud SDK Google applications are supported.
         
         scopedAccessSettings:
         - scope:
             clientScope:
               restrictedClientApplication:
                 name: Cloud Console
           activeSettings:
             accessLevels:
             - CBA_ACCESS_LEVEL
         - scope:
             clientScope:
               restrictedClientApplication:
                 name: Google Cloud SDK
           activeSettings:
             accessLevels:
             - CBA_ACCESS_LEVEL
         - scope:
             clientScope:
               restrictedClientApplication:
                 clientId: CLIENT_ID_1
           activeSettings:
             accessLevels:
             - CBA_ACCESS_LEVEL
         

Replace the following:

     * CLIENT_ID_1: the OAuth client ID.
     * CBA_ACCESS_LEVEL: a CBA access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  3. Create the CBA access level binding.
         
         gcloud access-context-manager cloud-bindings create \
            --group-key='GROUP_KEY' \
            --organization='ORG_ID' \
            --binding-file=policy_file.yaml
         

Replace the following:

     * `GROUP_KEY`: the unique group ID
     * `ORG_ID`: the organization ID

### gcloud

You can use the unique group ID as GROUP_KEY. To obtain the unique group ID, use the following command:
    
    gcloud identity groups describe EMAIL
    

Replace EMAIL with your group's email address. The unique group ID is the value returned after `/` in the group name. For example, the unique group ID in `groups/01gf8i8311xalqg` is `01gf8i8311xalqg`.

### REST

You can use the unique group ID as GROUP_KEY. To obtain the unique group ID using the REST API, you can retrieve it by calling the [`get`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/get) method on the group resource. The unique group ID is returned in the `id` field of the group resource.

  4. Optional: Update an existing access level binding.
         
         gcloud access-context-manager cloud-bindings update \
            --binding='BINDING_NAME' \
            --binding-file=policy_file.yaml
         

Replace BINDING_NAME with the binding name that was automatically generated when the binding was created.




### Exempt an application from a binding

Another way to apply a CBA access level without blocking client applications that don't support client certificates is to exempt those applications from the policy.

The following steps assume that you have previously [created a CBA access level](https://docs.cloud.google.com/access-context-manager/docs/create-cba-access-levels) that requires certificates when determining access to resources.

  1. Create an exemption access level using one of the following methods.

     * [Custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level): Provide `true` as the value in the CEL expression condition.
     * [Basic access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level): Create an [IP range-based access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#gcloud_1) by providing IP subnetworks `0.0.0.0/0` and `::/0`, which correspond to IPv4 and IPv6 respectively.
  2. Create an `exemption_file.yaml` file.
         
         scopedAccessSettings:
         - scope:
             clientScope:
               restrictedClientApplication:
                 clientId: CLIENT_ID_2
           activeSettings:
             accessLevels:
             - EXEMPT_ACCESS_LEVEL
         - scope:
             clientScope:
               restrictedClientApplication:
                 name: APPLICATION_NAME_2
           activeSettings:
             accessLevels:
             - EXEMPT_ACCESS_LEVEL
         

Replace the following:

     * CLIENT_ID_2: the OAuth client ID
     * APPLICATION_NAME_2: the application name
     * EXEMPT_ACCESS_LEVEL: an exemption access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
  3. Create the exemption binding policy.
         
         gcloud access-context-manager cloud-bindings create \
            --group-key='GROUP_KEY' \
            --organization='ORG_ID' \
            --binding-file=exemption_file.yaml
         

Replace the following:

     * GROUP_KEY: the unique group ID
     * ORG_ID: the organization ID



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
