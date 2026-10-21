---
url: https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy/
title: Manage an access policy \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:07.232299+00:00
---

# Manage an access policy  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Manage an access policy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage an existing access policy. You can do the following:

  * Get the name and etag of an access policy

  * Set the default access policy for the `gcloud` command-line tool

  * Delegate an access policy

  * Describe an access policy

  * Update an access policy

  * Delete an access policy




## Get the name and etag of an access policy

###  Console 

To get the numeric name of an access policy in the Google Cloud console, do the following:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, click **Manage policies**.

  4. On the **Manage VPC Service Control policies** page, click the title of the access policy that you want to inspect.

  5. On the **Edit access policy** page, find the numeric ID of the policy under **Access policy name**.


**Note:** The Google Cloud console does not display the `etag` of an access policy. To get the `etag`, use the `gcloud` command-line tool or the API.

###  gcloud 

To get the name of your access policy, use the [`list`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/list) command. The access policy name is required for all access level commands for the `gcloud` command-line tool.
    
    
    gcloud access-context-manager policies list \
        --organization ORGANIZATION_ID

Where:

  * ORGANIZATION_ID is the numeric ID of your organization.



You should see output similar to:
    
    
    NAME           ORGANIZATION  TITLE        ETAG
    1034095178592  511928527926  Corp Policy  10bc3c76ca809ab2
    

###  API 

To get the name of your access policy, call [`accessPolicies.list`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/list).
    
    
    GET https://accesscontextmanager.googleapis.com/v1/accessPolicies
    

### Request body

The request body must be empty.

### Response body

If successful, the response body will look similar to:
    
    
    {
      "accessPolicies": [
        {
          object(AccessPolicy)
        }
      ],
      "nextPageToken": string
    }

Where:

  * `accessPolicies` is a list of [`AccessPolicy` objects](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy).



## Set the default access policy for the `gcloud` command-line tool

When using the `gcloud` command-line tool, you can set a default access policy. When you set a default policy, you no longer need to specify a policy each time you use an Access Context Manager command.

To set a default access policy, use the `config` command.
    
    
    gcloud config set access_context_manager/policy POLICY_NUMBER

Where:

  * POLICY_NUMBER is the numeric name of your access policy.



## Delegate an access policy

###  Console 

To delegate administration of a scoped access policy in the Google Cloud console, do the following:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, click **Manage policies**.

  4. On the **Manage VPC Service Control policies** page, in the row for the scoped access policy that you want to delegate, click the _more_vert_ button, and then click **Edit**.

  5. On the **Edit access policy** page, under **Manage principals** , click **Add principals**.

  6. In the **Add principals** pane, select a [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity), such as a user or service account.

  7. Select the role that you want to associate with the principal, such as **Access Context Manager admin** , **Access Context Manager editor** , or **Access Context Manager reader** , and then click **Save**.

  8. On the **Edit access policy** page, click **Save**.




###  gcloud 

To delegate administration by binding a principal and role with a scoped access policy, use the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/add-iam-policy-binding) command.
    
    
    gcloud access-context-manager policies add-iam-policy-binding \
    [POLICY] --member=PRINCIPAL --role=ROLE

Where:

  * POLICY is ID of the policy or fully qualified identifier for the policy.

  * PRINCIPAL is the principal to add the binding for. Specify in the following format: `user|group|serviceAccount:email` or `domain:domain`.

  * ROLE is the role name to assign to the principal. The role name is the complete path of a predefined role, such as `roles/accesscontextmanager.policyEditor`, or the role ID for a custom role, such as `organizations/{ORGANIZATION_ID}/roles/accesscontextmanager.policyEditor`.




###  API 

To delegate administration of the scoped access policy, do the following:

  1. Create a request body.
         
         {
         "policy": "IAM_POLICY",
         }

Where:

     * IAM_POLICY is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains. A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role.
  2. Delegate the access policy by calling [`accessPolicies.setIamPolicy`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/setIamPolicy).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies
         




#### Response body

If successful, the response body contains an instance of [`policy`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Policy).

## Describe an access policy

###  Console 

To view the details of an access policy in the Google Cloud console, do the following:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, click **Manage policies**.

  4. On the **Manage VPC Service Control policies** page, click the title of the access policy that you want to view.

The **Edit access policy** page displays the policy's title, numeric **Access policy name** , scope, and delegated principals.




###  gcloud 

To describe your access policy, use the [`describe`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/describe) command.
    
    
    gcloud access-context-manager policies describe POLICY_NUMBER

Where:

  * POLICY_NUMBER is the numeric name of your policy.



The following output appears:
    
    
    name: accessPolicies/1034095178592
    parent: organizations/511928527926
    title: Corp Policy
    

###  API 

To describe your access policy, call [`accessPolicies.get`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/get)
    
    
    GET https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NUMBER
    

Where:

  * POLICY_NUMBER is the numeric name of your policy.



### Request body

The request body must be empty.

### Response body

If successful, the response body contains an [`AccessPolicy` object](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies#AccessPolicy).

## Update an access policy

###  Console 

In the Google Cloud console, you cannot change the title or scope of an existing access policy. To change the title of an access policy, use the `gcloud` command-line tool or the API.

To update the delegated principals and role bindings for a scoped access policy in the Google Cloud console, see Delegate an access policy.

###  gcloud 

To update your access policy, use the [`update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/update) command. Currently, you can change only the title of the policy.
    
    
    gcloud access-context-manager policies update POLICY_NUMBER \
        --title=POLICY_TITLE

Where:

  * POLICY_NUMBER is the numeric name of your policy.

  * POLICY_TITLE is a human-readable title for your policy.




The following output appears:
    
    
    Waiting for PATCH operation [accessPolicies/POLICY_NUMBER/update/1542234231134882]...done.
    

###  API 

Currently, you can change only the title of your access policy.

To update your policy:

  1. Create a request body.
         
         {
          "parent": "ORGANIZATION_ID",
          "title": "POLICY_TITLE"
         }

Where:

     * ORGANIZATION_ID is the numeric ID of your organization.

     * POLICY_TITLE is a human-readable title for your policy.

  2. Call [`accessPolicies.patch`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/patch).
         
         PATCH https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NUMBER/UPDATE_MASK
         

Where:

     * POLICY_NUMBER is the numeric name of your policy.

     * UPDATE_MASK is a string that represents the value you want to update. For example, `title`.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `PATCH` operation.




## Delete an access policy

**Warning:** When you delete a policy, the levels that the policy contains are also deleted and cannot be recovered.

###  Console 

To delete an access policy in the Google Cloud console, do the following:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. On the **VPC Service Controls** page, click **Manage policies**.

  4. On the **Manage VPC Service Control policies** page, in the row for the access policy that you want to delete, click the _more_vert_ button, and then click **Delete**.

  5. In the confirmation dialog, click **Delete**.




###  gcloud 

To delete an access policy:

  1. Use the [`delete`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/policies/delete) command.
         
         gcloud access-context-manager policies delete POLICY_NUMBER

Where:

     * POLICY_NUMBER is the numeric name of your policy.
  2. Confirm that you want to delete the access policy.

For example:
         
         You are about to delete policy [POLICY_NUMBER]
         
         Do you want to continue (Y/n)?
         

The following output appears:
         
         Deleted policy [1034095178592].
         




###  API 

To delete your access policy, call [`accessPolicies.delete`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies/delete).
    
    
    DELETE https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NUMBER
    

Where:

  * POLICY_NUMBER is the numeric name of your policy.



### Request body

The request body must be empty.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `DELETE` operation.

## What's next

  * [Managing access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
