---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/github/
title: Git export/restore \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:55.407067+00:00
---

# Git export/restore  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/github/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Git export/restore Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** In February 2025, a new version of this integration was released. Users of the old version can provide tokens without using secrets. The documentation below applies primarily to the new version.

Dialogflow CX integrates with multiple Git providers (GitHub, Gitlab, Bitbucket, and others). This integration makes it easy to [export your agent to JSON](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export) for a push to a Git provider, and to pull from a Git provider for an [agent restore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export). The JSON exported format pushed to a Git provider is the expanded zip file contents of the exported agent.

Using this feature allows you to take advantage of a Git provider source control features like:

  * Agent change reviews using code review tools
  * Examine agent diffs using diff tools
  * Merges



## Limitations

The following limitations apply:

  * [Old integration version only] GitHub APIs have a limitation on the number of files that can be updated in a single commit. If the number of files exceeds 500, you may not be able to push to GitHub from Dialogflow CX. In such cases, you can export the agent as a zip and use the Git CLI on your machine to push the agent files to GitHub. This limitation will be addressed in a later Dialogflow CX release.
  * GitHub private access [self-hosted](https://docs.github.com/en/enterprise-server/admin/overview/about-github-enterprise-server) repos are not supported, because Dialogflow CX cannot access these repos.
  * The Git repository cannot contain any files other than the agent files exported by agent export. Any other files in the repository will be removed on every push.



## Configuration

To configure this feature, you need to acquire an access token from your Git provider, store it in Secret Manager, and provide the secret resource to Dialogflow CX:

### Access token

To acquire an access token from your Git provider:

### GitHub

You need to acquire a [GitHub personal token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) If you use a fine-grained personal access token, you need the following [permissions](https://docs.github.com/en/rest/overview/permissions-required-for-fine-grained-personal-access-tokens) access:

  * **Repository Permissions > Contents**: Read and write
  * **Repository Permissions > Metadata**: Read-only (should be auto-selected after selecting Contents permission)



### Gitlab

You need to acquire a [Gitlab personal access token](https://docs.gitlab.com/user/profile/personal_access_tokens/).

### Bitbucket

You need to acquire a [Bitbucket access token](https://support.atlassian.com/bitbucket-cloud/docs/access-tokens/).

### Secret Manager

Now that you have an access token, you need to create a secret for your token:

  1. [Enable the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager).
  2. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).



### Dialogflow CX configuration

To configure this integration for Dialogflow CX:

  1. Provide the Dialogflow service agent permission to access the access token secret in Secret Manager. Provide the `Secret Manager Secret Accessor` role to the `gcp-sa-dialogflow.iam.gserviceaccount.com` service account in your agent project. See [Grant access to Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets#grant-access).
  2. Open the Git integration configuration: 
     * Conversational Agents console 
       1. Open the settings display by clicking the settings icon near the top right corner.
       2. Scroll down and click **Add Git integration**.
     * Dialogflow CX console 
       1. Click the **Manage** tab.
       2. Click **Git** in the **Testing & Deployment** section.
       3. Click **Create new**.
  3. Provide configuration details: 
     1. Enter the following: 
        * Display name for the GitHub connection.
        * Git repository URL (for example: `https://github.com/<path-to-repo>.git`).
        * Add Git branches your agent will be interacting with. You can designate a branch as the default branch by clicking the star icon next to it.
        * Access token secret, which is the secret version you created in the form `projects/*/secrets/*/versions/*` for a specific version or `projects/*/secrets/*/versions/latest` for the latest version.
     2. Click **Connect**.
     3. It can take a minute for the Git service to be ready. The console will display notifications.



## Push and restore

Once configured, you can push/pull your agent to/from Git.

The **Push** button is used to export your agent and make a commit to the Git branch selected in the Git branch dropdown. This commit will consist of the entire agent and not specific changes, and will delete any existing files in the repository.

Users with **Dialogflow Reader** roles have the ability to push to Git repositories. To prevent unwanted pushes, configure these agents with read-only personal access tokens.

The **Restore** button is used to pull your agent data from the Git branch selected in the Git branch drop-down and restore your Dialogflow CX agent from this data. This will overwrite your agent in the same way that any agent restore behaves.

## Example use case

The following example illustrates how this feature can be used by multiple people to propose different agent changes to a production agent.

Consider that your agent uses the following Git branches:

  * **Prod** : branch for your production agent
  * **Dev1** : branch for agent development
  * **Dev2** : another branch for agent development



User 1 wants to propose agent changes and takes the following steps:

  1. Export the production agent to a new agent.
  2. Make the desired changes to this agent copy.
  3. Test the changes.
  4. Push the altered agent to the **Dev1** branch.
  5. Create a merge request to the **Prod** branch.



User 2 wants to propose agent changes and takes the following steps:

  1. Export the production agent to a new agent.
  2. Make the desired changes to this agent copy.
  3. Test the changes.
  4. Push the altered agent to the **Dev2** branch.
  5. Create a merge request to the **Prod** branch.



User 3 reviews merge requests from both users and takes the following steps:

  1. Resolve conflicts.
  2. Commits approved changes.
  3. Restores the production Git branch to the production Dialogflow CX agent.



[ Previous arrow_back  Sessions  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/session)

[ Next Sentiment  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
