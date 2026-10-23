---
url: https://docs.cloud.google.com/looker/docs/webhook-deploy-secret/
title: Configuring the webhook deploy secret \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:38.508349+00:00
---

# Configuring the webhook deploy secret  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/webhook-deploy-secret/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Configuring the webhook deploy secret Stay organized with collections  Save and categorize content based on your preferences. 

A webhook deploy endpoint prompts your Looker instance to deploy changes from a Git branch, a commit SHA, or a tag name, and then push the changes to the production version of your project. (See the [Deploying with webhooks](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_webhooks) section for the Looker deploy webhook formats.) For most projects, Looker handles the Git integrations and [deploys updates to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production), so you don't need to set up a deploy webhook.

However, you _do_ need to use a deploy webhook to push changes to production if any of the following circumstances applies:

  * You push updates to the remote production branch outside of the Looker IDE, which is common in development workflows with staging environments.
  * You want to use a webhook to deploy with [advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode), which lets you specify the branch, the commit SHA, or the tag name that is used for your production version of the Looker project.
  * You have configured your Looker project with Git [pull requests](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project), which means that you have to trigger a deploy webhook once you merge a pull request in order to push those changes to your Looker production environment. Most Git hosting services have ways of automating this if you [add the webhook to your Git provider's interface](https://docs.cloud.google.com/looker/docs/git-options#adding_a_webhook_to_your_git_provider).



If you are a Looker admin, you can configure the deploy webhook to require a secret so that only authorized parties can trigger it. Looker developers who are not admins can view the **Project Configuration** page but cannot change the options there.

## Adding a deploy secret

Looker supports web secrets for the following Git providers: GitHub, Bitbucket Server, and GitLab.

To set a webhook deploy secret to your project:

![](https://docs.cloud.google.com/static/looker/docs/images/dev-project-add-secret-718.png)

  1. In [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode), [open your project](https://docs.cloud.google.com/looker/docs/accessing-project-files) and select the settings icon in the IDE navigation bar to open the project settings panel.
  2. Select **Configuration** in the project settings panel.
  3. Scroll to the **Webhook Deploy Secret** section, then click **Set Webhook Secret**. Looker will automatically generate a secret token. You can use this automatically generated secret, or you can type in your own secret token.
  4. Whether you are using the automatically generated secret or creating your own secret, copy the webhook deploy secret and paste it into a text file so you'll have it if you need to add the secret to the webhook for your repository. Be sure to copy it at this point. Once you leave or refresh the **Project Configuration** page, you lose access to the webhook deploy secret and will have to change or remove the webhook deploy secret to regain access to your project.
  5. Click **Save Project Configuration**.



The deploy webhook for your project now requires this secret. For projects that use a Looker staging instance, you need to include the webhook deploy secret in your HTTP header in order to deploy to production. For projects with [Git pull request integration](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project), you need to go to your Git provider's interface to add the secret to the webhook for your repository.

### Configuring the secret for your Git repository's webhook

For projects with [Git pull request integration](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project), if you have added a deploy webhook secret to your LookML project, you need to go to your Git provider's interface to add the secret to the webhook for your repository. As an example, here is how you do that using GitHub:

![](https://docs.cloud.google.com/static/looker/docs/images/dev-project-add-secret-repo-718.png)

  1. Navigate to your project's repository settings on your Git provider's website.

> **TIP** : If you've set up your project for Git integration, you can use the **View Project on Git** option from your project's Git menu in Looker.

  2. In your repository's settings, click **Webhooks**.

  3. Find the webhook for your LookML project, then click its **Edit** button.

  4. In the **Secret** field, paste the webhook deploy secret you copied from the **Webhook Deploy Secret** section in Looker.

  5. Click **Update webhook**.




The webhook secret is now required in order to deploy changes to the production version of your project. If you need, you can change the secret or remove the secret from your project.

## Changing a deploy secret

Once a webhook deploy secret has been added to your project, if you are a Looker admin, you can change the secret by doing the following:

  1. [From your project](https://docs.cloud.google.com/looker/docs/accessing-project-files), select the **Settings** icon from the navigation bar.
  2. Scroll to the **Webhook Deploy Secret** section and click **Reset Secret**. Looker will automatically generate a new secret token. You can use this automatically generated secret, or you can type in your own new secret token.
  3. Whether you are using the automatically generated secret or creating your own secret, copy the webhook deploy secret and paste it into a text file so you'll have it if you need to add the secret to the webhook for your repository. Be sure to copy it from your clipboard at this point. Once you leave or refresh the **Project Configuration** page, you will lose access to the webhook deploy secret and will have to go back and change it or remove it entirely.
  4. Click **Save Project Configuration**.



If your project is configured with [Git pull request integration](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project), you also need to go to your Git provider's interface to update the webhook secret for your repository.

## Removing a deploy secret

Once a webhook deploy secret has been added to your project, if you are a Looker admin, you can remove the secret by doing the following:

  1. [From your project](https://docs.cloud.google.com/looker/docs/accessing-project-files), select the **Settings** icon from the navigation bar.
  2. Scroll to the **Webhook Deploy Secret** section and click **Remove Secret**. At this point, you can cancel the operation and keep the deploy secret by clicking **Don't Remove**.
  3. To permanently remove the webhook deploy secret from your project, click **Save Project Configuration**.



Your project no longer requires a secret for the deploy webhook. If your project is configured with [Git pull request integration](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project), you can now go to your Git provider's interface to remove the webhook secret from your repository. Looker itself will no longer check for a secret on the Git provider's end, so it doesn't hurt if your Git repository webhook still has a secret configured. If you do want to remove the secret from your Git repository, see Configuring the Secret for Your Git Repository's Webhook for information on editing the secret on a Git provider's interface.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
