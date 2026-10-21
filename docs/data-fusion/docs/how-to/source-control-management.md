---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management/
title: Manage pipelines using Source Control Management \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:33.409537+00:00
---

# Manage pipelines using Source Control Management  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage pipelines using Source Control Management Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage pipelines using source control in Cloud Data Fusion through Git repositories.

## About Source Control Management

Cloud Data Fusion provides the capability to visually design pipelines for ETL and ELT integrations. For better management of pipelines between development and production, Cloud Data Fusion allows Source Control Management of the pipelines using [GitHub](http://www.github.com) and other version control systems.

The Source Control Management in Cloud Data Fusion lets you do the following:

  * Integrate each Cloud Data Fusion namespace with a version control system.
  * Manage your pipelines in a central Git repository.
  * Review and audit pipeline changes.
  * Revert pipeline changes.
  * Effectively collaborate with the team while ensuring central control.

**Important:** The functionality of syncing a single pipeline is supported in Cloud Data Fusion version 6.9.0 and later. The functionality of syncing multiple pipelines is supported in Cloud Data Fusion version 6.10.0 and later.

## Before you begin

  * Source Control Management supports integration with GitHub, Bitbucket Server, Bitbucket Cloud, and Gitlab repositories.
  * GitHub OAuth isn't supported.
  * Source Control Management only supports batch pipelines.
  * Source Control Management only supports pipeline design JSONs for push and pull operations. Execution configurations are not supported.
  * The size limit of the linked repository is 5 GB.

**Warning:** Make sure that the pipelines being pushed to Git repositories don't include secrets, such as service account JSON in plain text. To store secrets, we strongly recommend using [secure keys](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+Microservices#Create-a-Secure-Key).**Important:** To connect to a version control system server from a private Cloud Data Fusion instance, you must configure the network settings for public source access. For more information, see [Create a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip) and [Connect to a public source from a private instance](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-public-source).

### Required roles and permissions

**Note:** The predefined Cloud Data Fusion roles and current permissions don't necessarily cover the `read`, `write`, and `update_repo_metadata` permissions in Source Control Management Git repositories.

Source Control Management in Cloud Data Fusion consists of two key operations:

  * Configuring source control repositories
  * Syncing pipelines with Git repositories using push and pull operations



To get the permissions that you need to use the Source Control Management feature, ask your administrator to grant you any of the following predefined roles on your project:

  * Configure source control repository:

    * [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)
    * [Cloud Data Fusion Editor](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac#predefined-roles) (`roles/datafusion.editor`)
    * [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)
  * Sync pipelines using push or pull operation from a namespace:

    * [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) (`roles/datafusion.operator`)
    * [Cloud Data Fusion Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.developer) (`roles/datafusion.developer`)
    * [Cloud Data Fusion Editor](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac#predefined-roles) (`roles/datafusion.editor`)
    * [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

### Set up a Git repository

To create a Git repository in GitHub, follow the instructions described in [Create a repository](https://docs.github.com/en/get-started/quickstart/create-a-repo).

**Note:** If you're using a Private Service Connect enabled instance, make sure that the Git server is not hosted in the IP range `240.0.0.0/16` or `240.1.0.0/16` to avoid connection issues between the Cloud Data Fusion instance and the Git server.

For more information about personal access tokens in GitHub and other version control systems, see the following pages:

  * [Bitbucket Cloud access token documentation](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/)

  * [Bitbucket Server access token documentation](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html)

  * GitHub: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) and [Creating a fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)

  * [GitLab access token documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)


**Note:** We recommend using the [GitHub fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token), as roles like [Cloud Data Fusion Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.operator) and Cloud Data Fusion Editor can access the saved tokens.

## Connect a Git repository with Cloud Data Fusion

Cloud Data Fusion lets you configure and connect your Git repository in the Source Control Management tab for each namespace. To link a namespace with your Git repository, follow these steps:

### Console

  1. In the Cloud Data Fusion Studio, click menu **Menu**.
  2. Click **Namespace admin**.
  3. On the **Namespace admin** page, click the **Source Control Management** tab.
  4. Click **Link repository**.
  5. Enter the following details:

     * **Provider** : Choose a Git service provider, such as **GitHub** or **GitLab**.
     * **Repository URL** : Enter the URL where your repository can be accessed. For GitHub, the repository URL is `https://github.com/HOST/REPO`.
     * **Default branch** (optional): Enter the initial branch of the Git. This branch can be different from the default branch configured on GitHub. This branch is used to sync pipelines, regardless of the default branch on GitHub.
     * **Path prefix** (optional): Enter a prefix for your pipeline name that's saved in the Git repository. For example, if your pipeline name is `DataFusionQuickStart` and if you specify the prefix as `namespaceName`, then the pipeline is saved as `namespaceName/DataFusionQuickStart` in the Git repository.
     * **Authentication type** : Cloud Data Fusion lets you use the personalized access token as the authentication type. This is auto-selected.
     * **Token name** : Enter a name that can be associated with the token.
     * **Token** : Enter the token provided by the GitHub repository.
     * Optional: **User name** : Enter a username or an owner for the token.
  6. Click **Validate**. Wait for the connection to be verified.

  7. When the configuration is complete, click **Save and close** to confirm the configuration.




![Connect a Git repository with Cloud Data Fusion.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/source-control-management/connect-git-data-fusion.png)

### REST API

  1. [Create a secret key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+Microservices?focusedCommentId=798621721#comment-798621721) in Cloud Data Fusion containing the personal access token.

  2. Run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" 
         ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/securekeys/PASSWORD_SECRET_KEY -X PUT -d '{ "description": "Example Secure Key","data": "PERSONAL_ACCESS_TOKEN"}'
         

Replace the following:

     * `NAMESPACE_ID`: the ID of the namespace.
     * `PASSWORD_SECRET_KEY`: the name of the secret key containing personal access token.
     * `PERSONAL_ACCESS_TOKEN`: personal access token of GitHub.
  3. Run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" 
         ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/repository -X PUT -d '{"test": "TEST_ONLY", "config": {"provider": "PROVIDER_TYPE", "link": "REPO_URL", "defaultBranch": "DEFAULT_BRANCH", "pathPrefix": "PATH_TO_DIRECTORY", "auth": {"type": "AUTH_TYPE", "patConfig": {"passwordName": "PASSWORD_SECRET_KEY", "username": "USER_NAME"}}}}'
         

Replace the following:

     * `NAMESPACE_ID`: the ID of the namespace.
     * `TEST_ONLY`: set to `true` if you want to only validate the configuration and not add to it.
     * `PROVIDER_TYPE`: the Git provider name, that is, `GITHUB`.
     * `REPO_URL`: Repository URL to be linked. Use an `https` URl—for example, `https://github.com/user/repo.git`.
     * `DEFAULT_BRANCH`: Branch used for push and pull operations. If omitted, the default configured branch in the repository is used—for example, the main branch.
     * `PATH_TO_DIRECTORY`: path to the directory in the repository where configuration files are stored.
     * `AUTH_TYPE`: the authentication type. Only `PAT` is supported. See [Fine-grained personal access token in GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token).
     * `PASSWORD_SECRET_KEY`: the name of the secret key containing the personal access token for authentication type `PAT`.
     * `USER_NAME`: you can omit this value for authentication type `PAT`.



## Sync Cloud Data Fusion pipelines with a remote repository

After you configure a Git repository with a namespace, you can push and pull pipelines, and sync them, with the Git repository.

### Push pipelines from Cloud Data Fusion to Git repository

To sync multiple deployed pipelines from a namespace to a Git repository, follow these steps:

### Console

  1. In the Cloud Data Fusion Studio, click menu **Menu**.
  2. Click **Namespace admin**.
  3. On the **Namespace admin** page, click the **Source Control Management** tab.
  4. Find the Git repository that you want to sync with, and click **Sync pipelines**.
  5. Click the **Namespace pipelines** tab.
  6. Search for and select the pipelines that you want to push to the Git repository.

If the latest version of the pipeline is pushed to or pulled from the Git repository, the **Connected to Git** status shows `Connected`. If the pipeline has never been pushed to GitHub, the **Connected to Git** status shows blank (`-`).

If you deploy a newer version of a pipeline that is already synced with the Git repository, the **Connected to Git** status changes from `Connected` to blank (`-`).

  7. Click **Push to repository**.

  8. Enter a **Commit message** , and click **OK**.

The push operation starts and a message is displayed indicating that the selected pipelines are being pushed to the remote repository.




![Push pipelines from Cloud Data Fusion to Git repository.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/source-control-management/push-multiple-pipelines.png)

When the push operation is completed successfully, a success message is displayed indicating the number of pipelines that were pushed to the remote repository.

If the push operation fails, check the pipeline in GitHub to see if it's the latest version. For every failed push operation, an error message is displayed. To view the details of the error, expand the error message.

**Note:** If a push operation for multiple pipelines is in running state, you cannot concurrently start another push or pull operation in the namespace until the current operation completes. The list of pipelines in the **Namespace pipelines** and **Repository pipelines** tabs remain disabled until the current push operation completes.

You can also push individual pipelines to a Git repository from the pipeline design studio:

  1. In the Cloud Data Fusion Studio, click menu **Menu**.
  2. Click **List**.
  3. Click the pipeline you want to push to the Git repository.
  4. On the pipeline page, click **Actions** > **Push to repository**.
  5. Enter a **Commit message** and click **OK**.



![Push pipelines from the pipeline design studio.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/source-control-management/sync-from-design-studio.png)

### REST API

  1. Push a set of pipelines from Cloud Data Fusion to the Git repository:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"
         ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/repository/apps/push -X POST
         -d '{"apps": ["PIPELINE_NAME_1", "PIPELINE_NAME_2"]}, "commitMessage": "COMMIT_MESSAGE"'
         

Replace the following:

     * `NAMESPACE_ID`: the ID of the namespace.
     * `PIPELINE_NAME_1`, `PIPELINE_NAME_2`: names of the pipelines to be pushed.
     * `COMMIT_MESSAGE`: commit message for the Git commit.

The response contains the ID of the push operation. For example:
    
    RESPONSE
    {
    "id": OPERATION_ID
    }
    

  2. To poll the status of the push operation, run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" 
         ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/operations/OPERATION_ID
         

Replace the following:

     * `NAMESPACE_ID`: the ID of the namespace.
     * `OPERATION_ID`: the operation ID received from the push operation.

The response contains the status of the push operation. For example:
    
    RESPONSE
    {
    "id": OPERATION_ID
    "done": True/False
    "status": STARTING/RUNNING/SUCCEEDED/FAILED
    "error": {"message": ERROR_MESSAGE, "details":[{"resourceUri": RESOURCE, "message": ERROR_MESSAGE}]}
    }
    

To verify if the push operation is completed, check the `done` property in the response. If the operation failed, check the `error` property for more details.




### Pull pipelines from Git repository into Cloud Data Fusion

To sync multiple pipelines from a Git repository to your namespace, follow these steps:

### Console

  1. In the Cloud Data Fusion Studio, click menu **Menu**.
  2. Click **Namespace admin**.
  3. On the **Namespace admin** page, click the **Source Control Management** tab.
  4. Find the Git repository that you want to sync with, and click **Sync pipelines**.
  5. Click the **Repository pipelines** tab. All of the pipelines stored in the Git repository are displayed.
  6. Search for and select the pipelines that you want to pull from the Git repository into your Cloud Data Fusion namespace.
  7. Click **Pull from repository**.

The pull operation starts and a message is displayed indicating that the selected pipelines are being pulled from the remote repository. Cloud Data Fusion looks for JSON files under the configured path, and pulls and deploys them as pipelines to Cloud Data Fusion.




![Pull pipelines from Git repository into Cloud Data Fusion.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/source-control-management/pull-multiple-pipelines.png)

When the pull operation is completed successfully, a success message is displayed indicating the number of pipelines that were pulled from the remote repository.

If the pull operation fails, an error message is displayed. To view the details of the error, expand the error message.

**Note:** If a pull operation for multiple pipelines is in running state, you cannot concurrently start another push or pull operation in the namespace until the current operation completes. The list of pipelines in the **Namespace pipelines** and **Repository pipelines** tabs remain disabled until the current pull operation completes.

You can also pull individual pipelines from a Git repository to a namespace from the pipeline design studio:

  1. In the Cloud Data Fusion Studio, click menu **Menu**.
  2. Click **List**.
  3. Click the pipeline that you want to pull from the Git repository.
  4. On the pipeline page, click **Actions** > **Pull from repository**.



![Pull pipelines from the pipeline design studio.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/source-control-management/sync-from-design-studio.png)

### REST API

  1. Pull a set of pipelines from the Git repository into Cloud Data Fusion:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" 
         ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/repository/apps/pull -X POST -d '{"apps": ["PIPELINE_NAME_1", "PIPELINE_NAME_2"]}'
         

Replace the following:

     * `NAMESPACE_ID`: the ID of the namespace.
     * `PIPELINE_NAME_1`, `PIPELINE_NAME_2`: names of the pipelines to be pulled.

The response contains the ID of the pull operation. For example:
    
    RESPONSE
    {
    "id": OPERATION_ID
    }
    

  2. To poll the status of the pull operation, run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" 
         ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/operations/OPERATION_ID
         

Replace the following:

     * `NAMESPACE_ID`: the ID of the namespace.
     * `OPERATION_ID`: the operation ID received from the pull operation.

The response contains the status of the pull operation. For example:
    
    RESPONSE
    {
    "id": OPERATION_ID
    "done": True/False
    "status": STARTING/RUNNING/SUCCEEDED/FAILED
    "error": {"message": ERROR_MESSAGE, "details":[{"resourceUri": RESOURCE, "message": ERROR_MESSAGE}]}
    }
    

To verify if the pull operation is completed, check the `done` property in the response. If the operation failed, check the `error` property for more details.




## Delete the Git repository configuration

To delete the Git repository configuration from a namespace, follow these steps:

### Console

  1. In the Cloud Data Fusion Studio, click menu **Menu**.
  2. Click **Namespace admin**.
  3. On the **Namespace admin** page, click the **Source Control Management** tab.
  4. For the Git repository configuration you want to delete, click more_vert > **Delete**.



### REST API

Delete the Git repository configuration:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/repository -X DELETE
    

Replace NAMESPACE_ID with the ID of the namespace.

## What's next

  * Read more about [Using a GitHub repository to manage pipelines](https://cloud.google.com/blog/products/data-analytics/link-a-github-repository-with-a-namespace).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
