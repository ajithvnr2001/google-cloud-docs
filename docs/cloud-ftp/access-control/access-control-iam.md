---
url: https://docs.cloud.google.com/cloud-ftp/access-control/access-control-iam/
title: Access control with IAM \u00a0|\u00a0 Cloud FTP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:07.461084+00:00
---

# Access control with IAM  |  Cloud FTP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/access-control/access-control-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can control access to Cloud FTP resources. 

Cloud FTP uses Identity and Access Management (IAM) to control access to resources. IAM is a tool to manage fine-grained authorization for your Google Cloud resources. In other words, IAM lets you control who can do what on which resources. 

To give users access to a resource with IAM, you grant them specific roles. IAM roles give the principals permissions to perform tasks on your Cloud FTP resources. 

For detailed information about IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/overview). 

## Manage access to Cloud FTP resources

The most common way to manage access with IAM is to use [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies). Allow policies list which principals have access to the resource and what actions they can perform on the resource. 

The following sections describe how to manage access with allow policies using the Google Cloud console and the Google Cloud CLI. This includes procedures for common tasks, such as how to grant and revoke a single role. You can also grant and revoke multiple roles at the same time. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation. 

You can also use allow policies that are attached to different Google Cloud resources to manage access at other levels of the resource hierarchy. To learn more, see [Using resource hierarchy for access control](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) in the IAM documentation. 

Not all resources support allow policies. To learn which resources you can attach allow policies to, see [Resources that support allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies#allow-policies) in the IAM documentation. 

To learn about other policies you can use to control access with IAM, such as deny policies, see [IAM policy types](https://cloud.google.com/iam/docs/policy-types) in the IAM documentation. 

### Grant a single IAM role on a project, folder, or organization

This section describes how to grant access at the project, folder, or organization level. This controls a user's access to the project, folder, or organization, and all resources within it.

To grant a single role to a principal on a project, folder, or organization, do the following:

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.
  3. Select a principal to grant a role to: 
     * To grant a principal an additional role on the resource, find a row containing the principal, click edit **Edit principal** in that row, and click add **Add another role**. 

To grant a role to a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox to see its email address.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted. 
     * To grant a role to a principal who doesn't have any existing roles on the resource, click person_add **Grant Access** , then enter a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers)—for example, `my-user@example.com` or `//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.
  4. Select a role to grant from the drop-down list. For best security practices, choose a role that includes only the permissions that your principal needs.
  5. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.
  6. Click **Save**. The principal is granted the role on the resource.



### gcloud

**Note:** To grant the Owner role (`roles/owner`) on a project to a user outside of your organization, you must use the Google Cloud console, not the gcloud CLI. If your project is not part of an organization, you must use the Google Cloud console to grant the Owner role. 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. The `[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` command lets you quickly grant a role to a principal. 

Before using any of the command data below, make the following replacements: 

     * `RESOURCE_TYPE`: The resource type that you want to manage access to. Use `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `PRINCIPAL`: An identifier for the principal, or member, which usually has the following form: `PRINCIPAL_TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. For a full list of the values that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

     * `ROLE_NAME`: The name of the role that you want to grant. Use one of the following formats: 

       * Predefined roles: `roles/SERVICE.IDENTIFIER`
       * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
       * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles). 

     * `CONDITION`: The condition to add to the role binding. If you don't want to add a condition, use the value `None`. For more information about conditions, see the [conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview).

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member=PRINCIPAL --role=ROLE_NAME \
        --condition=CONDITION

#### Windows (PowerShell)
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID `
        --member=PRINCIPAL --role=ROLE_NAME `
        --condition=CONDITION

#### Windows (cmd.exe)
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID ^
        --member=PRINCIPAL --role=ROLE_NAME ^
        --condition=CONDITION

The response contains the updated IAM allow policy. 




**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

### Revoke a single IAM role on a project, folder, or organization

This section describes how to revoke access at the project, folder, or organization level. This controls a user's access to the project, folder, or organization, and all resources within it.

To revoke a single role from a principal on a project, folder, or organization, do the following:

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.
  3. Find the row containing the principal whose access you want to revoke. Then, click  edit **Edit principal** in that row. **Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted. 
  4. Click the **Delete** delete button for the role that you want to revoke, and then click **Save**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To revoke a role from a user, run the `remove-iam-policy-binding` command:
         
         gcloud RESOURCE_TYPE remove-iam-policy-binding RESOURCE_ID \
             --member=PRINCIPAL --role=ROLE_NAME

Provide the following values:

     * `RESOURCE_TYPE`: The resource type that you want to manage access to. Use `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `PRINCIPAL`: An identifier for the principal, or member, which usually has the following form: `PRINCIPAL_TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

     * `ROLE_NAME`: The name of the role that you want to revoke. Use one of the following formats: 

       * Predefined roles: `roles/SERVICE.IDENTIFIER`
       * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
       * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles). 

For example, to revoke the Project Creator role from the service account `example-service-account@example-project.iam.gserviceaccount.com` for the project `example-project`:
    
    gcloud projects remove-iam-policy-binding example-project \
          --member=serviceAccount:example-service-account@example-project.iam.gserviceaccount.com \
          --role=roles/resourcemanager.projectCreator




To help avoid revoking any necessary roles, you can enable [change risk recommendations](https://docs.cloud.google.com/recommender/docs/change-risk-recommendations). Change risk recommendations generate warnings when you try to revoke project-level roles that Google Cloud has identified as important. 

## Conditional access

IAM Conditions let you make your policies more granular by granting access to principals only when certain specified conditions are met. Conditions are based on attributes relating to the principal, resource, and request. For example, you can grant a principal access only if they're accessing the resource from a specific location or at a specific time. 

Conditions in allow policies are based on the following types of attributes: 

  * **Resource attributes** : Includes the service, type, or name of the resource. These attributes are typically used to change the scope of an access granted by a role binding. 
  * **Request attributes** : Includes details of the request, like the time or access level of the principal who made the request. These attributes let you create conditions that evaluate details about the request, such as its access level, date and time, the destination IP address and port, or the expected URL path. 



For more information about the condition attributes supported by Cloud FTP, see the [Attribute reference for IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) in the IAM documentation. 

You can't grant conditional access directly on Cloud FTP resources. However, you can grant conditional access to Cloud FTP resource types by granting roles to principals on a container resource, such as a project, folder, or organization, and adding conditions to these role bindings. Conditions added to the allow policy of a container resource are inherited by the resources included in that container resource. For more information about inherited conditions, see [Support for inherited conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#inherited-support) in the IAM documentation. 

To learn how to add conditions to role bindings, see [Managing conditional role bindings](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings) in the IAM documentation. 

## What's next

  * To learn more about access control with IAM, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 
  * To view the available roles and permissions for Cloud FTP, see [Cloud FTP roles and permissions](https://docs.cloud.google.com/cloud-ftp/access-control/roles-permissions). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
