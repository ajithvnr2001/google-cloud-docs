---
url: https://docs.cloud.google.com/access-context-manager/docs/create-access-policy/
title: Create an access policy \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:51:08.697134+00:00
---

# Create an access policy  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/create-access-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Create an access policy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an organization-level access policy for your organization and scoped policies for the folders and projects in your organization.

**Note:** An organization can only have one organization-level access policy and can contain multiple scoped policies for the folders and projects in the organization.

## Before you begin

  * Ensure you have the [correct permissions](https://docs.cloud.google.com/access-context-manager/docs/access-control) to use Access Context Manager.



## Create an organization-level access policy

For an organization, you cannot create an organization-level access policy if an organization-level access policy exists for that organization.

###  Console 

When you [create an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level), a default access policy is created automatically. No additional manual steps are required.

###  gcloud 

To create an organization-level access policy, use the [`create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create) command.
    
    
    gcloud access-context-manager policies create \
    --organization ORGANIZATION_ID --title POLICY_TITLE

Where:

  * ORGANIZATION_ID is the numeric ID of your organization.

  * POLICY_TITLE is a human-readable title for your policy.




You should see output similar to the following (where POLICY_NAME is a unique [numeric identifier for the policy](https://cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy) assigned by Google Cloud):
    
    
    Create request issued
    Waiting for operation [accessPolicies/POLICY_NAME/create/1521580097614100] to complete...done.
    Created.
    

Next, [set your default policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).

###  API 

To create an organization-level access policy:

  1. Create a request body.
         
         {
          "parent": "ORGANIZATION_ID",
          "title": "POLICY_TITLE"
         }

Where:

     * ORGANIZATION_ID is the numeric ID of your organization.

     * POLICY_TITLE is a human-readable title for your policy.

  2. Create the access policy by calling [`accessPolicies.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/create).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies
         

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `POST` operation.




## Create a scoped access policy and delegate the policy

Only VPC Service Controls supports creating a scoped access policy. You must continue to use organization-level policies for Google Cloud services, such as Identity-Aware Proxy (IAP).

**Warning:** If an organization-level access policy doesn't exist for your organization, scoped policies that you create at the folder or project-level will not operate.

###  Console 

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, select the access policy that is the parent of the scoped policy. For example, you can select the `default policy` organization policy.

  4. Click **Manage policies**.

  5. On the **Manage VPC Service Controls** page, click **Create**.

  6. On the **Create access policy** page, in the **Access policy name** box, type a name for the scoped access policy.

The scoped access policy name can have a maximum length of 50 characters, must start with a letter, and can contain only ASCII Latin letters (a-z, A-Z), numbers (0-9), or underscores (`_`). The scoped access policy name is case sensitive and must be unique within an organization's access policy.

  7. To specify a scope for the access policy, click **Scopes**.

  8. Specify either a project or a folder as the scope of the access policy.

     * To select a project that you want to add to the scope of the access policy, do the following:

       1. In the **Scopes** pane, click **Add project**.

       2. In the **Add project** dialog, select that project's checkbox.

       3. Click **Done**. The added project appears in the **Scopes** section.

     * To select a folder that you want to add to the scope of the access policy, do the following:

       1. In the **Scopes** pane, click **Add folder**.

       2. In the **Add folders** dialog, select that folders's checkbox.

       3. Click **Done**. The added folder appears in the **Scopes** section.

  9. To delegate administration of the scoped access policy, click **Principals**.

  10. To specify the [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) and the role that you want to bind to the access policy, do the following:

     1. In the **Principals** pane, click **Add principals**.

     2. In the **Add principals** dialog, select a principal, such as a user name or service account.

     3. Select the role that you want to associate with the principal, such as editor and read roles.

     4. Click **Save**. The added principal and role appear in the **Principals** section.

  11. On the **Create access policy** page, click **Create access policy**.




###  gcloud 

To create a scoped access policy, use the [`gcloud access-context-manager policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/create) command.
    
    
    gcloud access-context-manager policies create \
    --organization ORGANIZATION_ID [--scopes=SCOPE] --title POLICY_TITLE

Where:

  * ORGANIZATION_ID is the numeric ID of your organization.

  * POLICY_TITLE is a human-readable title for your policy. The policy title can have a maximum length of 50 characters, must start with a letter, and can contain only ASCII Latin letters (a-z, A-Z), numbers (0-9), or underscores (`_`). The policy title is case sensitive and must be unique within an organization's access policy.

  * SCOPE is the folder or project on which this policy is applicable. You can specify only one folder or project as the scope, and the scope must exist within the specified organization. If you don't specify a scope, the policy applies to the entire organization.




The following output appears (where POLICY_NAME is a unique [numeric identifier for the policy](https://cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy) assigned by Google Cloud):
    
    
    Create request issued
    Waiting for operation [accessPolicies/POLICY_NAME/create/1521580097614100] to complete...done.
    Created.
    

To delegate administration by binding a principal and role with a scoped access policy, use the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/add-iam-policy-binding) command.
    
    
    gcloud access-context-manager policies add-iam-policy-binding \
    [POLICY] --member=PRINCIPAL --role=ROLE

Where:

  * POLICY is ID of the policy or fully qualified identifier for the policy.

  * PRINCIPAL is the principal to add the binding for. Specify in the following format: `user|group|serviceAccount:email` or `domain:domain`.

  * ROLE is the role name to assign to the principal. The role name is the complete path of a predefined role, such as `roles/accesscontextmanager.policyReader`, or the role ID for a custom role, such as `organizations/{ORGANIZATION_ID}/roles/accesscontextmanager.policyReader`.




###  API 

To create a scoped access policy, do the following:

  1. Create a request body.
         
         {
          "parent": "ORGANIZATION_ID",
          "scope": "SCOPE",
          "title": "POLICY_TITLE"
         }

Where:

     * ORGANIZATION_ID is the numeric ID of your organization.

     * SCOPE is the folder or project on which this policy is applicable.

     * POLICY_TITLE is a human-readable title for your policy. The policy title can have a maximum length of 50 characters, must start with a letter, and can contain only ASCII Latin letters (a-z, A-Z), numbers (0-9), or underscores (`_`). The policy title is case sensitive and must be unique within an organization's access policy.

  2. Create the access policy by calling [`accessPolicies.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/create).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies
         

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `POST` operation.




To delegate administration of the scoped access policy, do the following:

  1. Create a request body.
         
         {
          "policy": "IAM_POLICY",
         }

Where:

     * IAM_POLICY is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains. A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role.
  2. Create the access policy by calling [`accessPolicies.setIamPolicy`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/setIamPolicy).

When the operation completes, the response body contains the [`accessPolicy`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies). The `name` field contains the resource name: `accessPolicy`/`POLICY_ID`

     1. To set the IAM policy, use the following endpoint:
    
    POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_ID:setIamPolicy
    

Replace `POLICY_ID` with the policy ID from that was returned from `accessPolicies.create`.

The request body must contain the IAM policy to set.

If successful, the response body contains an instance of [`policy`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Policy).




**Note:** After you create a scoped policy, you cannot change the scope of the policy. To change the scope of an existing policy, delete the policy and recreate the policy with the new scope.

## What's next

  * [Manage an access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
