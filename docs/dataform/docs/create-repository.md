---
url: https://docs.cloud.google.com/dataform/docs/create-repository/
title: Create a repository \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:37.738226+00:00
---

# Create a repository  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/create-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Create a repository Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand the concept of repositories in Dataform and how to create a new repository.

## About Dataform repositories

Each Dataform repository houses a collection of SQLX and JavaScript files that make up your workflow, as well as Dataform configuration files and packages. You interact with the contents of your repository in a [development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

Dataform displays your repositories on the Dataform page in the alphabetical order of repository IDs. You can sort and filter them.

  * To view your repositories, in the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)




Each Dataform repository must be connected to a custom service account. You select a custom service account when you create a repository. You can edit the service account later.

Dataform uses Git to record changes and manage file versions. Each Dataform repository corresponds with a Git repository. After you create a Dataform repository, you can connect it to a remote GitHub, GitLab, or Bitbucket repository.

In a Dataform repository, Dataform stores the repository code. In a connected repository, the third-party repository stores the repository code. Dataform interacts with the third-party repository to allow you to edit and execute its contents in a Dataform development workspace.

The Dataform repository page consists of the following components:

Development Workspaces tab
    Displays development workspaces created in the repository.
Workflow Execution Logs tab
    Displays [Dataform workflow execution logs](https://docs.cloud.google.com/dataform/docs/monitor-runs#monitor-execution-logs).
Releases & scheduling tab
    Lets you inspect, create, edit, and delete [release configurations](https://docs.cloud.google.com/dataform/docs/configure-compilation#create-release-configuration) and [workflow configurations](https://docs.cloud.google.com/dataform/docs/schedule-runs#workflow-configurations).
Settings tab
    Displays the name and location of the repository. For a repository connected to a third-party Git repository, displays the third-party repository source, default branch name, and secret token. Displays the buttons to [connect the repository](https://docs.cloud.google.com/dataform/docs/connect-repository) to a third-party Git repository and to [edit the Git connection](https://docs.cloud.google.com/dataform/docs/connect-repository#edit-connection).
Create development workspace button
    Lets you [create a development workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

After you create and initialize a development workspace, you can [edit your workflow settings file](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings) to configure the following Dataform settings of your repository:

  * The default database (Google Cloud project ID).
  * The default schema (BigQuery dataset ID).
  * The default BigQuery location.
  * The default schema (BigQuery dataset ID) for assertions.
  * The warehouse, which must be set to `bigquery`.
  * User-defined variables that are made available to project code during compilation.

**Important:** Repositories created in Dataform are not visible in BigQuery repositories.

For more information about Dataform repository settings, see [IProjectConfig in the Dataform core reference](https://docs.cloud.google.com/dataform/docs/reference/dataform-core-reference#iprojectconfig).

### Repository settings

When you create a Dataform repository, you need to set the following repository settings:

Repository ID
    A unique ID of the repository. IDs can only include numbers, letters, hyphens, and underscores.
Region
    

Dataform region for storing the repository and its contents.

This storage region can be different than the processing region where Dataform processes your code and stores the output of executions. By default, the processing region is set to your default BigQuery dataset region. You can edit the processing region in the workflow settings file after creating the repository. For more information, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

Service account
    

The custom service account associated with the repository. You can select a service account associated with your Google Cloud project or manually enter a different service account.

You must use a custom service account to run workflows in your repository. All other repository operations are performed by the default Dataform service agent.

Strict act-as mode
    

Enables an additional security check that requires the `iam.serviceAccounts.actAs` permission on the service account. Strict act-as mode is enforced for all repositories.

Encryption
    

Encryption method for the repository. You can use the [default encryption](https://docs.cloud.google.com/kms/docs/cmek#default-encryption), a unique customer-managed Cloud KMS encryption key, or a default Dataform CMEK key. For more information about using customer-managed encryption keys (CMEK) in Dataform, see [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek).

After you create a repository, you can [connect it to GitHub or GitLab](https://docs.cloud.google.com/dataform/docs/connect-repository).

**Important:** To create a Dataform repository connected to a remote Git repository that is not allow-listed in the `dataform.restrictGitRemotes` policy, first add the remote Git repository to the `allowedValues` list in the policy, and then create a new Dataform repository and connect it to the remote repository. For more information, see [Restrict remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery and Dataform APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery and Dataform APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,dataform.googleapis.com)

  8. To use CMEK encryption for the repository, [enable CMEK encryption of Dataform repositories](https://docs.cloud.google.com/dataform/docs/cmek).

**Important:** Before you create a Dataform repository that you want to [connect to a remote Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository), check if your organization or project restricts remote Git repositories with the `dataform.restrictGitRemotes` Organization Policy. If the policy is in place, ensure that the remote repository is allow-listed before you create the Dataform repository and connect it to the remote repository. For more information, see [Restrict remote repositories](https://docs.cloud.google.com/dataform/docs/restrict-git-remotes)

### Required roles

To get the permissions that you need to create and delete a repository, ask your administrator to grant you the following IAM roles on repositories: 

  * Dataform Admin (`roles/dataform.admin`) - the project 
  * Service Account User (`roles/iam.serviceAccountUser`) - the custom service account 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant required roles

To run workflows in your Dataform repository and in BigQuery, you can use a custom service account or your Google Account.

Your custom service account must have the following required roles:

  * [BigQuery Data Editor](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor) (`roles/bigquery.dataEditor`) on projects or specific BigQuery datasets to which Dataform needs both read and write access. This usually includes the project hosting your Dataform repository.
  * [BigQuery Data Viewer](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataViewer) (`roles/bigquery.dataViewer`) on projects or specific BigQuery datasets to which Dataform needs read-only access.
  * [BigQuery Job User](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser) (`roles/bigquery.jobUser`) on the project hosting your Dataform repository.



To let Dataform use your custom service account, the default Dataform service agent must have the following roles on the custom service account resource:

  * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`)
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



To grant these roles, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin)

  2. Click **Grant access**.

  3. In the **New principals** field, enter your custom service account ID.

  4. In the **Select a role** menu, select the following roles one by one, using **Add another role** for each additional role:

     * **BigQuery Data Editor**
     * **BigQuery Data Viewer**
     * **BigQuery Job User**
  5. Click **Save**.

  6. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  7. Select your custom service account.

  8. Go to **Principals with access** , and then click **Grant access**.

  9. In the **New principals** field, enter your default Dataform service agent ID.

Your default Dataform service agent ID is in the following format:
         
         service-PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with the numeral ID of your Google Cloud project. You can find your Google Cloud project ID in the Google Cloud console dashboard. For more information, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

  10. In the **Select a role** list, add the following roles:

     * **Service Account User**
     * **Service Account Token Creator**
  11. Click **Save**.




For more information on granting roles, see [Grant Dataform the required access](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access).

## Create a repository

To create a Dataform repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Click **Create repository**.

  3. On the **Create repository** page, in the **Repository ID** field, enter a unique ID.

IDs can only include numbers, letters, hyphens, and underscores.

  4. In the **Region** drop-down list, select a Dataform region for storing the repository and its contents. Select the Dataform region nearest to your location.

For a list of available Dataform regions, see [Locations](https://docs.cloud.google.com/dataform/docs/locations). The repository region does not have to match the location of your BigQuery datasets.

In the `workflow_settings.yaml` file, you can set the processing region where Dataform processes your code and stores the output of executions. The processing region has to match the location of your BigQuery datasets, but does not need to match the repository region. For more information, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).

  5. In the **Service account** menu, select a custom service account for the repository.

**Important:** You can't select the default Dataform service agent when creating a repository. You must use a custom service account for the repository.

In the menu, you can select a custom service account associated with your Google Cloud project that you have access to. Custom service accounts are used only for workflow execution. All other repository operations are performed by the default Dataform service agent.

     1. Optional: To select a service account that's not displayed in the menu—for example, if you lack the `iam.serviceAccounts.list` permission required to view the list of roles—click **Enter manually** and enter the service account ID.
**Note:** The `iam.serviceAccounts.list` permission is available in the [View Service Accounts role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`).
  6. In the **actAs permission checks** section, enforce the permission checks on user actions on the repository. For details on these checks, see [Use strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode).

  7. Configure your selected encryption mechanism for the repository:

**Caution:** You can't change the encryption mechanism of a Dataform repository after the repository is created. For more information, see [Dataform CMEK restrictions](https://docs.cloud.google.com/dataform/docs/cmek#restrictions)

###  Default CMEK key 

Dataform displays the **Use the default KMS key** checkbox and selects it by default.

     * To encrypt the repository with the default Dataform CMEK key, leave the **Use the default KMS key** checkbox selected.
**Caution:** If you select the **Use the default KMS key** checkbox but no default Dataform CMEK key is set for your project, Dataform applies [encryption at rest](https://docs.cloud.google.com/kms/docs/cmek#default-encryption) to the repository. [Use customer-managed encryption keys](https://docs.cloud.google.com/dataform/docs/cmek).

###  Unique CMEK key 

To encrypt the repository with a unique CMEK key, do the following:

     1. If the **Use the default KMS key** checkbox is selected by default, deselect the checkbox.
     2. In the **Encryption** section, select the **Customer-managed encryption keys (CMEK)** option.
     3. In the **Select a customer-managed key** drop-down, select a unique CMEK key.

###  Encryption at rest 

     * To use the [default encryption](https://docs.cloud.google.com/kms/docs/cmek#default-encryption), in the **Encryption** section, select the **Google-managed encryption key** option.
**Caution:** If a default Dataform CMEK key is set for the region of your repository, you must use CMEK encryption. Don't select the **Google-managed encryption key** option. For more information, see [Dataform CMEK restrictions](https://docs.cloud.google.com/dataform/docs/cmek#restrictions).

  8. Click **Create** , and then click **Go to repositories**.




## Edit the service account

You must use a custom service account to run workflows in your repository. All other repository operations are performed by the default Dataform service agent.

To edit the service account for a Dataform repository, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. Select a repository, and then click **Settings**.

**Note:** The Dataform repositories list includes only repositories created for Dataform workflow development. Repositories for BigQuery Studio assets, such as notebooks or saved queries, are managed separately and don't appear in this list.
  3. By the **Service account** field, click edit **Edit Service account**.

  4. In the **Service account** menu, select a service account for the repository.

In the menu, you can select a custom service account associated with your Google Cloud project that you have access to.

     1. Optional: To select a service account that is not displayed in the menu, click **Enter manually** and enter a service account ID.
  5. Click **Save**.




## Delete a repository

To delete a repository and all its contents, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to Dataform](https://console.cloud.google.com/bigquery/dataform)

  2. By the repository that you want to delete, click the more_vert **More** menu, and then select **Delete**.

  3. In the **Delete repository** window, enter the name of the repository to confirm deletion.

  4. Click **Delete**.




## What's next

  * To learn how to connect a Dataform repository to a third-party Git repository, see [Connect to a third-party Git repository](https://docs.cloud.google.com/dataform/docs/connect-repository).
  * To learn more about how repository size affects development in Dataform, see [Overview of repository size](https://docs.cloud.google.com/dataform/docs/best-practices-repositories#overview-repo-size).
  * To learn more about splitting a repository in Dataform, see [Introduction to splitting repositories](https://docs.cloud.google.com/dataform/docs/best-practices-repositories#splitting-repos).
  * To learn how to configure Dataform processing settings, see [Configure Dataform workflow settings](https://docs.cloud.google.com/dataform/docs/manage-repository#configure-workflow-settings).
  * To learn how to create and initialize a workspace, see [Create a workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
