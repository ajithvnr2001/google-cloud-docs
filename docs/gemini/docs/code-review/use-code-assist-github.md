---
url: https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github/
title: Use Gemini Code Assist on GitHub \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:51.102189+00:00
---

# Use Gemini Code Assist on GitHub  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/code-review/use-code-assist-github/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Use Gemini Code Assist on GitHub Stay organized with collections  Save and categorize content based on your preferences. 

[Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code) lets you automate code reviews and generate pull request summaries directly in your repositories. This page shows you how to use Gemini Code Assist on GitHub.

## Before you begin

To complete the tasks in this page, make sure you have [set up Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github).

## Get pull request summary and feedback

To get an initial review for a pull request from Gemini Code Assist, create a new pull request.

When you open the new pull request, Gemini Code Assist provides an initial review. After the review is ready, `gemini-code-assist[bot]` is automatically added as a reviewer to the pull request. Gemini Code Assist adds an issue comment in the **Conversation** tab of the pull request with its feedback and proceeds to add comments about modified portions of the code.

Review comments contain the following information:

  * Severity of the issue, given as Critical, High, Medium, and Low
  * Feedback on the issue
  * Code suggestion that can be committed directly from GitHub
  * References to a [user-provided style guide](https://docs.cloud.google.com/gemini/docs/code-review/style-guide)



Gemini Code Assist does not add comments that have a _severity_ less than the minimum severity threshold that is [set for the repository](https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review).

## Manually invoke Gemini Code Assist

Gemini Code Assist listens to comments from any pull request contributor, and decides whether it should respond.

To manually invoke Gemini Code Assist, you can use the following commands in the main comments page on the pull request as an issue comment.

Command | Description  
---|---  
`/gemini summary` | Posts a summary of the changes in the pull request  
`/gemini review` | Posts a code review of the changes in the pull request  
`/gemini` | Manually invokes Gemini Code Assist in comments  
`/gemini help` | Overview of the available commands  
  
## Manage the Gemini Code Assist settings

Anyone with permissions to modify GitHub App settings for the organization can manage the Gemini Code Assist app settings. You can review the permissions provided to the Gemini Code Assist app, manage repository access, and uninstall the Gemini Code Assist app.

To modify the settings, follow these steps:

  1. On GitHub, click your profile photo and then click **Settings**.
  2. In the **Integrations** section, click **Applications**. A list of GitHub Apps is displayed.
  3. Beside Gemini Code Assist, click **Configure**.



## Troubleshooting

If you're not receiving responses from Gemini Code Assist, it might be because the Google Cloud project that you used during setup isn't connected to a valid billing account. You should [verify the billing status of your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled) and, if necessary, connect your project to a valid billing account.

Note that Developer Connect has a large [free tier](https://docs.cloud.google.com/developer-connect/pricing), and there are no charges for using Gemini Code Assist on GitHub during Preview. While a valid billing account is required, it only accrues charges when usage goes over the free tier limits.

## What's next

  * Learn more about [Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code).
  * [Set up Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github).
  * Learn how to [customize Gemini Code Assist on GitHub behavior](https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
