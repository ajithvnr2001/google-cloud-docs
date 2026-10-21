---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam/
title: Authorize access with IAM (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:41.511908+00:00
---

# Authorize access with IAM (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authorize access with IAM (1st gen)

You use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) to authorize identities to perform administrative actions on your functions, like creating, updating, and deleting them. You add **principals** (the identities you wish to enable, usually a user or service account email) to the function and then grant those principals the appropriate IAM [roles](https://docs.cloud.google.com/iam/docs/understanding-roles). These roles include **permissions** that define the actions they are allowed to do.

**Note:** By default, entities that need to **invoke** an HTTP function must explicitly present authentication credentials (proof of identity) as well as having the required permissions. The authentication requirement, however, can be turned off. For more information on how to acquire and present the appropriate authentication credential, see [Authenticate for invocation](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating).

## Enabling access to a function

You can control actions on a function by granting or restricting roles to individual identities through IAM.

### Adding principals and granting roles

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/)

  2. Click the checkbox next to the function in which you are interested.

  3. Click **Permissions** at the top of the screen. The **Permissions** panel opens.

  4. Click **Add principal**.

  5. In the **New principals** field, enter one or more identities that need access to your function. This is usually a user or service account email.

  6. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

**Note:** for a list of the available roles and the permissions they grant, see Cloud Run functions IAM [Roles reference page](https://docs.cloud.google.com/functions/docs/reference/iam/roles)
  7. Click **Save**.




###  gcloud 

Use the `gcloud functions add-iam-policy-binding` command:
    
    
    gcloud functions add-iam-policy-binding FUNCTION_NAME \
      --member=PRINCIPAL_ID \
      --role=ROLE

where `FUNCTION_NAME` is the function name, `PRINCIPAL_ID` is the principal's identifier, usually an email, and `ROLE` is the role.

For a list of sources that can provide a `PRINCIPAL_ID`, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). For a list of acceptable values for `ROLE`, see the [Cloud Run functions IAM Roles reference page](https://docs.cloud.google.com/functions/docs/reference/iam/roles).

### Removing roles from principals

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/)

  2. Click the checkbox next to the function in which you are interested.

  3. Click **Permissions** at the top of the screen. The **Permissions** panel opens.

  4. Search for the principal you want to remove. Look in every role the principal has been granted.

  5. When you find the principal in the role you wish to delete, click the trash can icon next to it. If you wish to completely remove the principal's access, do this for every role the principal has been granted.


**Note:** You can also **change** a principal's role here.

###  gcloud 

Use the `gcloud functions remove-iam-policy-binding` command:
    
    
      gcloud functions remove-iam-policy-binding FUNCTION_NAME \
        --member=PRINCIPAL_ID \
        --role=ROLE

where `FUNCTION_NAME` is the function name, `PRINCIPAL_ID` is the email address that identifies the service account, prefaced with `serviceAccount:`, and `ROLE` is the role.

For a list of acceptable sources for `PRINCIPAL_ID`, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). For a list of possible values for `ROLE`, see the [Cloud Run functions IAM Roles reference page](https://docs.cloud.google.com/functions/docs/reference/iam/roles).

If the principal has been granted multiple roles, make sure you specify the one you wish to remove.

### Bulk addition of principals

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/)

  2. Click the checkboxes next to the functions on which you want to grant or restrict access.

  3. Click **Permissions** at the top of the screen. The **Permissions** panel opens.




To add principals:

  1. Click **Add principal**.

  2. In the **New principals** field, enter multiple identities that need access to your function.

  3. Select a role (or roles) from the **Select a role** drop-down menu. The roles you select appear in the pane with a short description of the permissions they grant.

  4. Click **Save**.




###  gcloud 

Create an IAM policy named, for example, `policy.json`:
    
    
    {
      "bindings": [
        {
          "role": ROLE,
          "members": [
            PRINCIPAL_ID
          ]
        }
      ]
    }

Use the `gcloud functions set-iam-policy` command:
    
    
    gcloud functions set-iam-policy FUNCTION_NAME policy.json

For a list of acceptable sources for `PRINCIPAL_ID`, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). For a list of acceptable values for `ROLE`, see the [Cloud Run functions IAM Roles reference page](https://docs.cloud.google.com/functions/docs/reference/iam/roles).

### Viewing principals

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/)

  2. Click the name of the function you are interested in.

  3. Select the **Permissions** tab. The **Permissions** panel opens.

  4. Select the **View by principals** tab to view a list of all principals with permissions on the selected function.




###  gcloud 

Use the `gcloud functions get-iam-policy` command:
    
    
    gcloud functions get-iam-policy FUNCTION_NAME

## Allowing unauthenticated HTTP function invocation

As of January 15, 2020, HTTP functions without **Allow unauthenticated invocations** enabled restrict access to end users and service accounts that don't have appropriate permissions.

To allow unauthenticated invocations you must specify this at or after deployment.

You use a special variant of the approach described earlier to grant unauthenticated invokers the ability to invoke an [HTTP function](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions).

**Note:** [Event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions) can only be invoked by the event source to which they are subscribed.

### At deployment

### Console

Select **Allow unauthenticated invocations** in the **Authentication** section in the **Trigger** panel.

###  gcloud 

The `gcloud functions deploy` command includes a prompt to help you configure invocation permissions during function creation. It can also include the [`--allow-unauthenticated`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--allow-unauthenticated) flag:
    
    
    gcloud functions deploy FUNCTION_NAME \
      --no-gen2 \
      --trigger-http \
    **--allow-unauthenticated** \
    ...

Subsequent deployments of the same function do not change its status, even if you do not use this flag.

**Note:** Use of the `--allow-unauthenticated` flag modifies IAM permissions. To ensure that unauthorized developers cannot modify function permissions, the user or service that is deploying the function must have the `cloudfunctions.functions.setIamPolicy` permission. This permission is included in both the Owner and functions Admin roles. See [Cloud Run functions IAM Roles](https://docs.cloud.google.com/functions/docs/reference/iam/roles) for the full list of roles and their associated permissions.

### After deployment

To allow unauthenticated invocation of a function, grant the Cloud Functions Invoker role to the special `allUsers` principal on the function:

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/)

  2. Click the checkbox next to the receiving function. (Don't click on the function itself.)

  3. Click **Permissions** at the top of the screen. The **Permissions** panel opens.

  4. Click **Add principal**.

  5. In the **New principals** field, type `allUsers`.

  6. Select the role **Cloud Functions > Cloud Functions Invoker** from the **Select a role** drop-down menu.

  7. In response to the dialog, click **Allow public access**.




###  gcloud 

Use the `gcloud functions add-iam-policy-binding` command to grant the `roles/cloudfunctions.invoker` role to the special `allUsers` principal on the function:
    
    
    gcloud functions add-iam-policy-binding FUNCTION_NAME \
     --member=**"allUsers"** \
     --role=**"roles/cloudfunctions.invoker"**

See the [`gcloud functions add-iam-policy-binding` reference](https://docs.cloud.google.com/sdk/gcloud/reference/functions/add-iam-policy-binding) for more information about these fields.

## Domain Restricted Sharing

If you are developing functions in a project that is subject to the [Domain Restricted Sharing organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) you will be unable to allow unauthenticated invocation of a function. This policy restricts [public data sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#public_data_sharing) to reduce the risk of data exfiltration.

If you wish to deploy functions that permit unauthenticated invocation, we recommend that you remove the Domain Restricted Sharing organization policy on the project. Organization policies can be set at the organization, folder or project level.

Once you have created your function(s) that allow unauthenticated invocation, the organization policy can be re-enabled:

  * Functions deployed before the organization policy has been re-enabled will continue to allow unauthenticated invocation.
  * New versions of these existing functions can be deployed without requiring authenticated invocation.
  * New functions that permit unauthenticated invocations cannot be deployed.



## Controlling access on all functions in a project

If you want to grant roles on all functions in a project, you can [grant these roles on the project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** You can't grant roles to `allUsers` and `allAuthenticatedUsers` at the project level.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
