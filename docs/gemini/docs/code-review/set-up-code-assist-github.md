---
url: https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github/
title: Set up Gemini Code Assist on GitHub \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:13.672194+00:00
---

# Set up Gemini Code Assist on GitHub  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Set up Gemini Code Assist on GitHub Stay organized with collections  Save and categorize content based on your preferences. 

[Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code) lets you automatically summarize pull requests and generate in-depth code reviews. In this guide, you set up Gemini Code Assist on GitHub for your repositories.

## Before you begin

To set up Gemini Code Assist on GitHub, make sure you do the following:

  1. Have a GitHub organization or personal account.

  2. Have one or more GitHub repositories that you want to enable Gemini Code Assist on GitHub on.

If you don't have such a repository, you can create a fork of [our sample repository](https://github.com/GoogleCloudPlatform/microservices-demo) to use.

  3. Ask your administrator to [grant](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) you the [**Service Usage Admin** role](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) and the `geminicodeassistmanagement.scmConnectionAdmin` role.

**Important:** The `geminicodeassistmanagement.scmConnectionAdmin` role can't be granted using the Google Cloud console. Use the Google Cloud CLI instead.
     * Alternatively, if you have the [**Admin** or **Owner** basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic), you have the necessary IAM permissions to complete the setup.
  4. Ensure that the Google Cloud project you use during setup is connected to a valid billing account.




## Install Gemini Code Assist on GitHub

The following steps show you how to set up Gemini Code Assist on GitHub.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms for Google Cloud](https://cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [Google Cloud launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the Gemini Code Assist **Agents & Tools** page.

[Go to Agents & Tools](https://console.cloud.google.com/gemini-code-assist/agents-tools)

     1. If you haven't previously enabled the Developer Connect API, you see a caution banner that prompts you to enable the API. If this happens, click the **Enable** button associated with the banner, and click the **Enable** button in the dialog window that appears.
  2. In the **Agents** section, locate the **Code Assist Source Code Management** card, and click **Enable**.

The **Enable Code Assist Source Code Management** pane opens.

  3. In the **Gemini Code Assist Management API** section, click **Enable**.

  4. In the **Select a connection** section, click the **Connection** drop-down.

  5. In the drop-down, click **Create new connection**.

The **Link Git repositories via Developer Connect** pane opens.

**Note:** Gemini Code Assist on GitHub creates the Developer Connect connection in `us-east1` and doesn't support using existing connections you might have for other features, such as [code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview).
  6. In the **Provider** drop-down, select the GitHub provider you are using.

  7. In the **Name** field, enter a name for your connection.

  8. Click **Continue**.

The **Request GitHub OAuth token** dialog window open.

  9. After reading the disclaimer, click **I understand and continue**.

  10. In the **Install Gemini Code Assist** page, click the account you want to install the app in.

  11. Choose whether to install the app for **All repositories** or **Only select repositories**.

  12. Click **Install**.

  13. Follow the GitHub steps to authenticate to GitHub.

Once access is confirmed, the dialog window closes and you return to the **Link Git repositories via Developer Connect** pane.

  14. In the **Link repositories** section, click the **Repositories** drop-down, select the repositories you want to link, and click **Ok**.

**Note:** If you want to add a GitHub repository to this Developer Connect connection in the future, you must [use Developer Connect](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo#link-repos) to do so.
  15. Click **Link**.

  16. In the **Select a connection** drop-down, select the connection you created.

  17. Click **Done**.




Gemini Code Assist is now active for all the pull requests within your selected repositories.

## What's next

  * Learn more about [Gemini Code Assist in GitHub](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code).
  * [Use Gemini Code Assist in GitHub](https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github).
  * Learn how to [customize Gemini Code Assist on GitHub behavior](https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
