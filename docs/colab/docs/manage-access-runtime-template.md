---
url: https://docs.cloud.google.com/colab/docs/manage-access-runtime-template/
title: Manage access to a runtime template in Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:22.207707+00:00
---

# Manage access to a runtime template in Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/manage-access-runtime-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage access to a runtime template

This page describes how you can grant and revoke access to a runtime template in Colab Enterprise.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to manage access to a runtime template, ask your administrator to grant you the Colab Enterprise Admin ([`roles/aiplatform.colabEnterpriseAdmin`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.colabEnterpriseAdmin)) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Grant access to a runtime template

To grant a principal access to a runtime template, you can use the Google Cloud console, the Google Cloud CLI, or Terraform.

### Console

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime templates** page. 

[Go to Runtime templates](https://console.cloud.google.com/agent-platform/colab/runtime-templates)

  2. In the **Region** menu, select the region that contains your runtime template. 

  3. In the **Runtime template** menu, select a runtime template. If there aren't any runtime templates listed, [create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template). 

  4. Click ![](https://docs.cloud.google.com/static/colab/images/icon-runtime-template-permissions.png) **Permissions**. 

  5. In the **Permissions** window, click ![](https://docs.cloud.google.com/static/colab/images/icon-add-principal.png) **Add principal**. 

  6. In the **Grant access** dialog, in the **New principals** field, enter one or a comma separated list of principals. 

  7. In the **Select a role** menu, complete the dialog to assign a role. 

  8. Optional: Click add **Add another role** , and repeat the last step. 

  9. Click **Save**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `RUNTIME_TEMPLATE_ID`: the ID of your runtime template.
  * `PRINCIPAL`: the principal to add the binding for.
  * `ROLE`: the role name to assign to the principal.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your runtime template is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates add-iam-policy-binding RUNTIME_TEMPLATE_ID \
        --member=PRINCIPAL \
        --role=ROLE \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates add-iam-policy-binding RUNTIME_TEMPLATE_ID `
        --member=PRINCIPAL `
        --role=ROLE `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates add-iam-policy-binding RUNTIME_TEMPLATE_ID ^
        --member=PRINCIPAL ^
        --role=ROLE ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about managing IAM policies for runtime templates from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates). 

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

The following sample uses the [`google_colab_runtime_template_iam_policy` ](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/colab_runtime_template_iam) Terraform resource to grant access to a Colab Enterprise runtime template. 
    
    
    data "google_iam_policy" "admin" {
      binding {
        role = "roles/viewer"
        members = [
          "user:jane@example.com",
        ]
      }
    }
    
    resource "google_colab_runtime_template_iam_policy" "policy" {
      project = google_colab_runtime_template.runtime-template.project
      location = google_colab_runtime_template.runtime-template.location
      runtime_template = google_colab_runtime_template.runtime-template.name
      policy_data = data.google_iam_policy.admin.policy_data
    }

## Colab Enterprise principals are users, groups, or domains

You can grant access to users, groups, or domains. See the following table:

Principal | Example user account  
---|---  
Single user | `user@gmail.com`  
Google group | `admins@googlegroups.com`  
Google Workspace domain | `example.com`  
  
## Revoke access to a runtime template

To revoke access to a runtime template, you can use the Google Cloud console or the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Find the row containing the principal whose access you want to revoke. Then, click  edit **Edit principal** in that row.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted.
  4. Click the **Delete** delete button for the role that you want to revoke, and then click **Save**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `RUNTIME_TEMPLATE_ID`: the ID of your runtime template.
  * `PRINCIPAL`: the principal whose access you want to revoke.
  * `ROLE`: the role to remove from the principal.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your runtime template is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates remove-iam-policy-binding RUNTIME_TEMPLATE_ID \
        --member=PRINCIPAL \
        --role=ROLE \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates remove-iam-policy-binding RUNTIME_TEMPLATE_ID `
        --member=PRINCIPAL `
        --role=ROLE `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates remove-iam-policy-binding RUNTIME_TEMPLATE_ID ^
        --member=PRINCIPAL ^
        --role=ROLE ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about managing IAM policies for runtime templates from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates). 

## What's next

  * To learn how to grant access to a notebook, see [Manage access to a notebook](https://docs.cloud.google.com/colab/docs/manage-access-notebook).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
