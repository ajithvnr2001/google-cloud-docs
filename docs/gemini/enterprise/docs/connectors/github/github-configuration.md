---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration/
title: GitHub configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:36.066885+00:00
---

# GitHub configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  GitHub configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure a third-party configuration before creating the GitHub data store.

## Set permissions and obtain client ID and client secret

To register a GitHub app and obtain the client ID and client secret, do the following:

  1. Sign in to your GitHub account.
  2. Go to **Settings** > **Developer Settings**.
  3. In the **Developer Settings** page, click **GitHub apps**.
  4. Click **New GitHub app**.

![Developer settings GitHub app](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/github-images/githubapp.png)GitHub app
  5. In the app registration page, do the following:

     1. In the **GitHub app name** field, enter a label to identify the app.
     2. In the **Homepage URL** field, enter the full URL to your application homepage.
     3. In the **Callback URL** field, enter `https://vertexaisearch.cloud.google.com/oauth-redirect`.
     4. To ensure tokens expire regularly and to receive a `refresh_token` that can be used to request a new access token, select the **Expire user authorization tokens** checkbox.
     5. To prompt users to authorize your app when they install it, select the **Request user authorization (OAuth) during installation** checkbox.
     6. In the **Permissions** section, enable the following permissions:

**Permission Name** | **Permission Type** | **Reason for Access**  
---|---|---  
Repository: Actions  | Read and write  | Trigger, list, cancel, and rerun workflow runs; access job logs   
Repository: Administration  | Read-only  | List repository collaborators   
Repository: Contents  | Read and write  | Read files, commits, branches, tags, and releases; create branches, write files, push commits, and fork repositories   
Repository: Discussions  | Read and write  | Read GitHub Discussions and discussion categories; add, update, or delete discussion comments   
Repository: Issues  | Read and write  | Read issues, labels, comments, and search issues; create or update issues, post comments, triage issues, and manage labels   
Repository: Metadata  | Read-only (Mandatory)  | Search for repositories and users   
Repository: Pull requests  | Read and write  | Read pull requests, diffs, and PR comments; merge, update, and add review comments and replies   
Repository: Code scanning alerts  | Read-only  | Read code scanning alerts   
Repository: Dependabot alerts  | Read-only  | Read Dependabot security alerts   
Repository: Secret scanning alerts  | Read-only  | Read secret scanning alerts   
Organization: Members  | Read-only  | View organization teams and their members   
Organization: Issue Types  | Read-only  | View organization issue types   
Organization: Projects  | Read and write  | Read and manage organization-level Projects v2 (projects, items, fields, and status updates)   
Account: Starring  | Read and write  | Star and unstar repositories   
Account: Profile  | Read and write  | Access user profile information   
     7. In the section asking where to install the app, select **Only on this account**.

     8. Click **Create GitHub app**.

  6. In the navigation menu, select **Install app**.

  7. Select an account to install the newly created app and click **Install**.

  8. Select **All repositories** and click **Install & authorize**.

  9. In the navigation menu, select **General**.

  10. Click **Generate a new client secret**. Copy the **Client ID** and the generated **Client secret** values, and store them securely for later use.

![Client ID and client secret](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/github-images/client-id-secret.png)GitHub app General tab



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
