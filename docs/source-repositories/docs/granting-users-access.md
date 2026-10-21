---
url: https://docs.cloud.google.com/source-repositories/docs/granting-users-access/
title: Granting user access to repositories and projects \u00a0|\u00a0 Cloud Source Repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:00.317316+00:00
---

# Granting user access to repositories and projects  |  Cloud Source Repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/source-repositories/docs/granting-users-access/

Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. For alternative source hosting options, [Secure Source Manager](https://cloud.google.com/secure-source-manager/docs) is a regionally deployed, single tenant, managed source code repository hosted on Google Cloud.

If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API. Organizations that have used Cloud Source Repositories prior to June 17, 2024 are not affected by this change.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Source Repositories ](https://docs.cloud.google.com/source-repositories/docs)
  * [ Guides ](https://docs.cloud.google.com/source-repositories/docs/create-code-repository)



Send feedback 

#  Granting user access to repositories and projects Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how you can provide users access to repositories and projects, and what actions those users can take. Examples of user actions include the following:

  * Listing repositories
  * Creating new repositories
  * Updating repositories



For a complete list of actions, see [Roles and permissions matrix](https://docs.cloud.google.com/source-repositories/docs/configure-access-control#roles_and_permissions_matrix).

## Grant permissions to view repositories

Users with this level of permissions can view the contents of a repository. They can also clone and fetch the repository.

If granted this permission at the project level, users can view all repositories for that project.

### Grant viewing permissions for a repository

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click the name of a repository.

The **Files** view opens.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

The **Permissions** page opens.

  5. In the **Members** field, enter the user's email address.

  6. In the **Role** drop-down list, select **Source repository > Source Repository Reader**.

  7. Click **Add**.




###  Command line 

  1. Open a terminal window.

  2. Enter the following command:
         
         gcloud source repos set-iam-policy [REPO_NAME] [POLICY_FILE] [GCLOUD_WIDE_FLAG …]
         

Where:

     * `[REPO_NAME]` is the name of the repository.
     * `[POLICY_FILE]` is the JSON or YAML file with the Identity and Access Management policy.



For more information on this command, see [gcloud source repos set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy).

### Grant viewing permissions across a project

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click the name of a Google Cloud project ID for a specific repository.

The page displays a list of all repositories for that project.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

The **Permissions** page opens.

  5. In the **Members** field, enter the user's email address.

  6. In the **Role** drop-down list, select **Source repository > Source Repository Reader**.

  7. Click **Add**.




###  Command line 

  1. Open a terminal window.

  2. Enter the following command:
         
         gcloud projects add-iam-policy-binding [PROJECT_ID] --member=[MEMBER] \
         --role=[ROLE] [GCLOUD_WIDE_FLAG …]
         

Where:

     * `[PROJECT_ID]` is the ID for your Google Cloud project.
     * `[MEMBER]` is the user you want to add.
     * `[ROLE]` is the IAM role you want to assign.



For more information on this command, see [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

## Grant permissions to push commits

Users with this level of permissions can push changes to a repository. They can also perform all the actions described in Viewing repositories.

If granted this permission at the project level, users can push changes to all repositories in that project.

### Grant push permissions for a repository

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click the name of a repository.

The **Files** view opens.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

The **Permissions** page opens.

  5. In the **Members** field, enter the user's email address.

  6. In the **Role** drop-down list, select **Source repository > Source Repository Writer**.

  7. Click **Add**.




###  Command line 

  1. Open a terminal window.

  2. Enter the following command:
         
         gcloud source repos set-iam-policy [REPO_NAME] [POLICY_FILE] [GCLOUD_WIDE_FLAG …]
         

Where:

     * `[REPO_NAME]` is the name of the repository.
     * `[POLICY_FILE]` is the JSON or YAML file with the IAM policy.



For more information on this command, see [gcloud source repos set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/source/repos/set-iam-policy).

### Grant push permissions for a project

###  Console 

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click the name of a Google Cloud project ID for a specific repository.

The page displays a list of all repositories for that project.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

The **Permissions** page opens.

  5. In the **Members** field, enter the user's email address .

  6. In the **Role** drop-down list, select **Source Repository > Source Repository Writer**.

  7. Click **Add**.




###  Command line 

  1. Open a terminal window.

  2. Enter the following command:
         
         gcloud projects add-iam-policy-binding [PROJECT_ID] --member=[MEMBER] \
         --role=[ROLE] [GCLOUD_WIDE_FLAG …]
         

Where:

     * `[PROJECT_ID]` is the ID for your Google Cloud project.
     * `[MEMBER]` is the user you want to add.
     * `[ROLE]` is the IAM role you want to assign.



For more information on this command, see [gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

## Grant permissions to create and delete repositories

If granted this permission at the project level, users can create, update, and delete repositories for the entire project.

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click the name of a Google Cloud project ID for a specific repository.

The page displays a list of all repositories for that project.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

The **Permissions** page opens.

  5. In the **Members** field, enter the user's email address.

  6. In the **Role** drop-down list, select **Source repository > Source Repository Administrator**.

  7. Click **Add**.




## Remove a user's access

There may be cases where you need to remove a user's access to a repository or project.

### Remove access to a repository

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click on the name of a repository.

The **Files** view opens.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

  5. Locate the role you want to remove, and then click **Delete** _delete_ for that role.

A confirmation dialog opens.

  6. Click **Remove**.




### Remove access to a project

  1. In the Google Cloud console, open Cloud Source Repositories in the [My source](https://source.cloud.google.com/) view tab

  2. Click the name of a Google Cloud project ID for a specific repository.

The page displays a list of all repositories for that project.

  3. Click **Settings** _settings_.

The **General settings** page opens.

  4. Click **Permissions**.

The **Permissions** page opens.

  5. Locate the role you want to remove, and then click **Delete** _delete_ for that role.

A confirmation dialog opens.

  6. Click **Remove**.




## What's next

  * Learn more about [Cloud Source Repositories and access control](https://docs.cloud.google.com/source-repositories/docs/configure-access-control).

  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
