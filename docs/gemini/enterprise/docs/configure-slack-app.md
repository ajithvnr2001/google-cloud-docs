---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app/
title: Configure the Gemini Enterprise app for Slack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:10.010399+00:00
---

# Configure the Gemini Enterprise app for Slack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure the Gemini Enterprise app for Slack Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise can integrate with Slack to deliver AI-powered answers and search to your Slack users, directly in their Slack workspace. After you configure the Gemini Enterprise app for Slack, your users can send prompts to Gemini Enterprise and receive answers that incorporate data from all connected Gemini Enterprise data stores.

**Note:** The Gemini Enterprise app for Slack is configured separately from the [Slack data connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack), which allows Gemini Enterprise to search data from a Slack workspace.

## Supported regions

The Gemini Enterprise app for Slack is supported in the global, US, and EU multi-regions.

## Limitations

The Gemini Enterprise app for Slack has the following limitations:

  * **Supports only Gemini Enterprise search.** Data store actions are not supported.
  * **Does not support Workforce Identity Federation.** An administrator must set up the Gemini Enterprise app for Slack using Google Identity. For more information, see Before you begin.
  * **Supports one-to-one workspace mapping:** You can link each Gemini Enterprise app to only one Slack workspace. For Slack Enterprise Grid, link each workspace to a separate Gemini Enterprise app.



## Before you begin

Ensure that you have the following before configuring the Gemini Enterprise app for Slack:

  * Access to the Slack AI add-on. For information about Slack AI, see the [Slack website](https://slack.com/features/ai).
  * A Gemini Enterprise app. If you haven't created an app yet, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).
  * A configured Gemini Enterprise app that uses Google Identity as the identity provider. For information about setting up Google Identity, see [Configure identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider).
  * Configured data stores for any services that you want users to be able to search. For information about connecting Google and third-party data sources with Gemini Enterprise, see [Introduction to connectors and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores).
  * The [Project IAM Admin](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectIamAdmin) role (`roles/resourcemanager.projectIamAdmin`) for your Google Cloud project.
  * Google Cloud OAuth 2.0 credentials for your Slack instance. To get the credentials, do the following:

    1. In the Google Cloud console, navigate to **APIs & Services > Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

    2. Click **add Create credentials**, then select **OAuth client ID**.

    3. In the **Application type** drop-down, select **Web application**.

    4. For **Name** , enter a name for the OAuth 2.0 client.

    5. In the **Authorized redirect URIs** section, click **add Add URI**.

    6. Enter the URL `https://vertexaisearch.cloud.google.com/slack/oauth_callback`.

    7. Click **Create**.

    8. When the **OAuth client created** dialog appears, copy the values of **Client ID** and **Client secret**.

  * The ID of your Slack workspace. For more information, see Find your Slack workspace ID.




### Find your Slack workspace ID

You need your Slack workspace ID to connect your workspace to your Gemini Enterprise app.

**Note:** If your organization uses Slack Enterprise Grid, don't use your Organization Grid ID (which begins with `E`). If you use the Grid ID, the integration fails and the app doesn't respond to user messages. Use the individual workspace ID (which begins with `T`).

#### Standard Slack workspaces

To find the workspace ID for a standard Slack workspace:

  1. Open your Slack workspace in a web browser.
  2. In the URL, your workspace ID is the string beginning with T. For example, in the URL `https://app.slack.com/client/T0123456789/...`, the workspace ID is `T0123456789`.
  3. Copy and store the workspace ID.



#### Slack Enterprise Grid

To find the workspace ID for a specific workspace in your Enterprise Grid:

  1. Open the [Slack Admin Center](https://admin.slack.com/).
  2. In the sidebar, click **Workspaces**.
  3. Select the workspace you want to integrate.
  4. In the URL, your workspace ID is the string beginning with `T`. For example, in the URL `https://admin.slack.com/workspaces/T0123456789`, the workspace ID is `T0123456789`.
  5. Copy and store the workspace ID.



## Connect your Slack workspace with Gemini Enterprise

Register your Slack workspace in the settings of your Gemini Enterprise app.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the **Apps** list, select the Gemini Enterprise app to which you want to connect Slack.

  3. Click **Integration > Slack**.

  4. Fill out the required fields:

     * Enter your Slack workspace ID.
     * Enter your Google Cloud OAuth 2.0 client ID.
     * Enter your Google Cloud OAuth 2.0 client secret.
  5. Click **Save**.




## Install the Gemini Enterprise app for Slack in your Slack workspace

After registering your workspace, install the Gemini Enterprise app for Slack in your Slack workspace.

  1. Click the following link:

[Install Gemini Enterprise app for Slack](https://slack.com/oauth/v2/authorize?client_id=8599736726022.9330833439668&scope=app_mentions:read,assistant:write,chat:write,commands,im:history,reactions:write)

  2. Click **Allow**.

  3. In your Slack workspace settings, verify that the app installed successfully. If you have a Workspace Owner or Workspace Admin role, you can check to see if the Gemini Enterprise app for Slack has been successfully installed by clicking **Manage > Installed Apps**.




After installing the app, each user must grant one-time access to the Gemini Enterprise app for Slack if they want Gemini Enterprise to search their data. This authorization is done separately by each user. For instructions, see [User authorization](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store#user_authorization).

## Use the app in Slack

**Note:** To enable the channel mentions and multi-turn support features, your Slack administrator must reinstall the Gemini Enterprise app. For more information, see Install the Gemini Enterprise app for Slack in your Slack workspace. After the administrator reinstalls the app, end users must authorize the Slack connector. For more information, see [User authorization](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store#user_authorization).

After you authorize the Gemini Enterprise app for Slack, you can interact with it in the following ways:

### Direct messages with multi-turn support

You can message the Gemini Enterprise app for Slack directly to ask questions. These direct messages support multi-turn conversations. The Gemini Enterprise app remembers the context of your current session. You can ask follow-up questions or refine previous responses. To clear the current context and start a new session, click **New chat**.

### Channel mentions

You can collaborate with the Gemini Enterprise app directly in your Slack channels and threads. Mention the app in a channel or thread with a prompt. For example: `@Gemini Enterprise summarize this thread`. The app adds an 👀 (eyes) reaction to your message to confirm receipt of the prompt. The app returns the response privately, and the message is marked as **Only visible to you**. You can review the response before sharing it in the channel or thread.

**Note:** Chat history is platform-specific. Conversations in the Gemini Enterprise app for Slack remain in Slack, and conversations in the Gemini Enterprise web app remain in the web app. Chat histories are not synced across platforms.

## What's next

  * To connect your data sources to Gemini Enterprise, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).
  * To integrate Gemini Enterprise with Chrome Enterprise cloud-managed browsers, see [Configure Chrome Enterprise cloud-managed browsers](https://docs.cloud.google.com/gemini/enterprise/docs/configure-chrome).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
