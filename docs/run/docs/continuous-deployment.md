---
url: https://docs.cloud.google.com/run/docs/continuous-deployment/
title: Continuously deploy from a repository \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:51.375724+00:00
---

# Continuously deploy from a repository  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/continuous-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Continuously deploy from a repository Stay organized with collections  Save and categorize content based on your preferences. 

If you have source code or functions in a Git repository and want to automate builds and set up continuous deployments from a repository, you can use either [Cloud Build](https://docs.cloud.google.com/build/docs/overview) or [Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview) in the Cloud Run console.

When you set this up, Cloud Run uses a [Cloud Build trigger](https://docs.cloud.google.com/build/docs/running-builds/automate-builds), to automatically build and deploy your code whenever new commits are pushed to a given branch of a Git repository. The [source repository information is displayed](https://docs.cloud.google.com/run/docs/managing/revisions#build-source) in the Google Cloud console for your service after you deploy to Cloud Run.

In the Cloud Run console:

  * If you select Cloud Build, you can set up continuous deployments from GitHub. For an example, see the quickstart for [creating a template repository and deploying continuously from git](https://docs.cloud.google.com/run/docs/quickstarts/deploy-continuously).

  * If you select Developer Connect, you can set up continuous deployments from GitHub, GitLab, and Bitbucket repositories.




Alternatively, you can use [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/deploy-app-run) to set up a continuous-delivery pipeline to deploy Cloud Run services to multiple environments.

## Before you begin

  * You either have a git repository with a `Dockerfile` or your codebase is written in one of the languages supported by [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/builders). 
  * Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  * If you select the Developer Connect option, enable the Developer Connect API:

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=developerconnect.googleapis.com)




### Required roles

To get the permissions that you need to deploy Cloud Run services from Git using Cloud Build or Developer Connect, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



The service account running the build must have the following roles:

  * [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)
  * [Cloud Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * If you select the Developer Connect option: 
    * [Developer Connect Read Token Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/developerconnect#developerconnect.readTokenAccessor) (`roles/developerconnect.readTokenAccessor`)
    * If you are connecting to GitLab or Bitbucket repositories: [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`)



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set up continuous deployment from the Cloud Run console

The setup procedure varies slightly depending on whether you are setting up continuous deployment on a new service or on an existing service. Click the appropriate tab to learn more.

###  New service 

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click **Connect repository** to display the **Create service** form.

  3. Select **Cloud Build** or **Developer Connect**.

     1. If you selected **Cloud Build** , see Set up with Cloud Build.

     2. If you selected **Developer Connect** , see Set up with Developer Connect.




### Existing service

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Locate the service in the services list, and click it.

  3. Click the **Source** tab.

  4. Click **Connect to repo** and follow the instructions in Set up with Cloud Build.




### Set up with Cloud Build

In the **Set up with Cloud Build** pane:

  1. Select a repository from the list. Note that it takes a few moments to load the list of repositories. Follow the prompt and click **Next**.

GitHub is the default repository provider. If you are not yet authenticated, click **Authenticate** and follow the instructions. Connecting a repository is done using the Cloud Build GitHub app. If you see an error such as `The redirect_uri is not associated with this application`, see Troubleshoot GitHub connection.

If you can't find your repository, click the **Manage connected repositories** link. Follow the instructions to grant your repository access to Cloud Build.

  2. In the **Build Configuration** step, fill in the options:

     * _Branch_

       * Indicates what source should be used when running the trigger. You can put the [regex](https://github.com/google/re2/wiki/Syntax) here. Matched branches are automatically verified: you can see them below the input. Note that if exactly one branch is matched, the trigger will be automatically executed after the creation.
     * _Build Type_

       * **Dockerfile** : If your repository should be built using Docker and it contains a Dockerfile, select this option.

         * In **Source location** , specify the location and name of the Dockerfile. This directory will be used as the Docker build context. All paths should be relative to the current directory.
       * **Go, Node.js, Python, Java, .NET Core, Ruby or PHP via Google Cloud's buildpacks** : If your repository should be built using buildpacks, select this option.

         * In the **Build context directory** , specify the directory.
         * In **Entrypoint** (optional), provide the command to start the server. For example, `gunicorn -p :8080 main:app` for Python, and `java -jar target/myjar.jar` for Java. Leave this field blank to use [default behavior](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs#google_entrypoint).
         * In **Function target** (for function deployments only), enter the function to be invoked. Otherwise, leave this field blank.
  3. Click **Save**.

  4. The page reloads and brings you back to the _Create service_ form.

  5. Verify the selected settings in the **Source repository** section.

  6. Fill out the rest of form under **Configure**.

  7. Click **Create**.

You are redirected to the _Service Details_ page, where you can track the progress of your Building and deploying from repository setup.




After all steps are completed, you can:

  * Click **Edit repo settings** in the Cloud Run console to edit the Cloud Build trigger in the Cloud Build console.
  * View the Build History by clicking the _logs_ link in the **Building and deploying from repository** step.
  * View Source details in the [_Revision Details_ section](https://docs.cloud.google.com/run/docs/managing/revisions#view_revision_details).



#### Troubleshoot GitHub connection

If you receive the error `The redirect_uri is not associated with this application. The application might be misconfigured or could be trying to redirect you to a website you weren't expecting` when authenticating with GitHub, GitHub rejected the redirection URL provided during the OAuth handshake.

To resolve this issue, complete the following troubleshooting steps:

  1. Verify or reset the repository connection in Cloud Build:

     1. In the Google Cloud console, go to the **Repositories** page:

[Go to Repositories](https://console.cloud.google.com/cloud-build/repositories)

     2. Locate the connection to your GitHub account or organization.

     3. If the repository is connected or in an error state, disconnect the repository or the entire GitHub connection.

     4. Return to the Cloud Run console and re-initiate the continuous deployment setup to refresh the OAuth authorization.

  2. Check your Cloud Build GitHub App permissions in GitHub:

     1. In GitHub, go to your account or organization settings.
     2. In the left navigation, click **Applications** , and then select the **Installed GitHub Apps** tab.
     3. Locate the **Google Cloud Build** app and click **Configure**.
     4. Under **Repository access** , verify that the target repository is selected.
     5. If permissions appear correct but authentication fails, revoke access for the app and re-grant access during the Cloud Run setup flow.
  3. Test the connection in a private browser window:

     1. Open a new incognito or private browser window.
     2. Sign in to the Google Cloud console and your GitHub account.
     3. Retry the continuous deployment connection flow to rule out interference from cached cookies, browser extensions, or multiple signed-in accounts.
  4. Check GitHub organization third-party application restrictions:

     * If you are connecting a repository owned by a GitHub organization, verify whether your organization enforces restrictions on third-party application access.
     * If restrictions are enabled, an organization owner must approve the **Google Cloud Build** app. For more information, see the GitHub documentation on [OAuth app access restrictions](https://docs.github.com/en/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions).
  5. If the error persists after completing these steps, contact [support](https://docs.cloud.google.com/run/docs/getting-support) and provide the following details:

     * Your Google Cloud project ID
     * The GitHub repository URL
     * The exact step where the error occurred



#### Set up continuous deployment manually

Refer to [Setting up continuous deployment manually](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-cloud-run) if you need to use a manual procedure and not the UI.

#### Attach existing Cloud Build trigger to Cloud Run service

If you already have an existing Cloud Build trigger, you can attach it to the service by adding a label to your Cloud Run service.

To add a label in the Cloud Run console:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Select the checkbox next to your service.

  3. Click **Labels** at the top of the page to open the **Labels** pane.

  4. Add a label with gcb-trigger-id as the key and the the unique identifier of the Cloud Build trigger as the value (not the trigger name). If the gcb-trigger-id key already exists, modify the value. See [Set or modify labels](https://docs.cloud.google.com/run/docs/configuring/services/labels#set-labels) for setting up the label.




### Set up with Developer Connect

In the **Set up with Developer Connect** pane:

  1. Select a repository and click **Next**.

If you don't see the repository you want to select, click **Link new repository** to open the **Link new repositories via Developer Connect** pane. Click the appropriate tab to learn more about connecting to one of the source code management providers.

### GitHub

For the **GitHub** , **GitHub Enterprise Cloud** , and **GitHub Enterprise** options, click **Connect**.

If you don't see a dialog, turn off any pop-up blocking browser plug-ins and makes sure that your browser settings allow pop-ups. For example, in Chrome, follow the instructions to [allow pop-ups](https://support.google.com/chrome/answer/95472).

Grant permissions on your GitHub account and link to repositories using the following instructions. The prompts you see in your web browser depend on whether the GitHub account already has the Cloud Run GitHub app installed.

In the Cloud Run dialog, complete the following steps:

**If you see a list of GitHub accounts, install the app and link repositories by completing these steps:**

     1. Choose the GitHub account you want to use.

     2. Select one or more repositories you want to grant access to.

**If you see a prompt to re-use an existing app installation, choose where to configure the app by completing these steps:**

     1. Click **GitHub Account** to see accounts that have the Google Cloud Run app installed. If you see the account you want to use, choose it by clicking **Confirm**.

     2. If you don't see the account that you want to use, do the following:

        1. Choose **Install the GitHub App on another GitHub account** and click **Confirm**.

        2. Follow the GitHub steps to permit app installation.

        3. Select one or more repositories you want to grant access to.

When the dialog closes, the app installation is complete.

### GitLab

For the **GitLab** option:

     1. In the **Personal Access Tokens** section, enter the [tokens](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab#tokens) for your account:

        * **API access token** : Enter the personal access token with `api` scope.
        * **Read API access token** : Enter the personal access token with `read_api` scope.

You are responsible for ensuring your GitLab tokens remain valid. GitLab tokens have a maximum lifetime of 365 days, unless otherwise specified by the token creator or an administrator. To learn how to manage token expiration settings and notifications, see the GitLab documentation on [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

For more information, see GitLab's documentation on [personal access token expiration](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#access-token-expiration).

     2. Click **Show more** to see optional configuration settings.

     3. Optional: In the **Encryption** section, select a [ CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Cloud Run creates.

### GitLab Enterprise Edition

For the **GitLab Enterprise Edition** option:

     1. For **Host URL** , enter the URL of the host you want to connect to.

     2. In the **Personal Access Tokens** section, enter the [tokens](https://docs.cloud.google.com/developer-connect/docs/connect-gitlab#tokens) for your account:

        * **API access token** : Enter the personal access token with `api` scope.
        * **Read API access token** : Enter the personal access token with `read_api` scope.

You are responsible for ensuring your GitLab tokens remain valid. GitLab tokens have a maximum lifetime of 365 days, unless otherwise specified by the token creator or an administrator. To learn how to manage token expiration settings and notifications, see the GitLab documentation on [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

For more information, see GitLab's documentation on [personal access token expiration](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#access-token-expiration).

     3. Click **Show more** to see optional configuration settings.

     4. Optional: In the **Encryption** section, select a [ CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Cloud Run creates.

### Bitbucket

For the **Bitbucket Cloud** option:

     1. For **Workspace** , enter your [Bitbucket Cloud workspace ID](https://support.atlassian.com/bitbucket-cloud/docs/what-is-a-workspace/).

     2. In the **Access Tokens** section, enter your Bitbucket access tokens:

        * **Authorizer access token** : Enter your [authorizer access token](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-cloud#tokens).
        * **Read access token** : Enter your [read access token](https://docs.cloud.google.com/developer-connect/docs/connect-bitbucket-cloud#tokens).
     3. Click **Show more** to see optional configuration settings.

     4. Optional: In the **Encryption** section, select a [ CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Cloud Run creates.

### Bitbucket Data Center

For the **Bitbucket Data Center** option:

     1. For **Host URL** , enter the URL for the Bitbucket Data Center host you want to connect to.

     2. In the **Access Tokens** section, enter your Bitbucket Cloud access tokens:

        * **Admin access token** : Enter the token with the repository admin scope access.

        * **Read access token** : Enter the token with the repository read scope access.

     3. Click **Show more** to see optional configuration settings.

     4. Optional: In the **Encryption** section, select a [ CMEK key](https://docs.cloud.google.com/kms/docs/key-management-service) to encrypt Secret Manager secrets that Cloud Run creates.

  2. Click **Connect**. This process can take a few seconds.

  3. In the **Build Configuration** step, fill in the options:

     * _Branch_

       * Indicates what source should be used when running the trigger. You can put the [regex](https://github.com/google/re2/wiki/Syntax) here. Matched branches are automatically verified: you can see them below the input. Note that if exactly one branch is matched, the trigger will be automatically executed after the creation.
     * _Build Type_

       * **Dockerfile** : If your repository should be built using Docker and it contains a Dockerfile, select this option.

         * In **Source location** , specify the location and name of the Dockerfile. This directory will be used as the Docker build context. All paths should be relative to the current directory.
       * **Go, Node.js, Python, Java, .NET Core, Ruby or PHP via Google Cloud's buildpacks** : If your repository should be built using buildpacks, select this option.

         * In the **Build context directory** , specify the directory.
         * In **Entrypoint** (optional), provide the command to start the server. For example, `gunicorn -p :8080 main:app` for Python, and `java -jar target/myjar.jar` for Java. Leave this field blank to use [default behavior](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs#google_entrypoint).
         * In **Function target** (for function deployments only), enter the function to be invoked. Otherwise, leave this field blank.
  4. Click **Save**.

  5. Fill out the rest of form under **Configure**.

  6. When you are finished configuring your service, click **Create** to deploy the image to Cloud Run and wait for the deployment to finish.

  7. Click the displayed URL link to open the unique and stable endpoint of your deployed service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
