---
url: https://docs.cloud.google.com/workstations/docs/version-control/
title: Version control with Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:52.105743+00:00
---

# Version control with Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/version-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Version control with Cloud Workstations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use version control for your application files with the Cloud Workstations base editor's Git support.

Click ![](https://docs.cloud.google.com/static/workstations/images/source-control-icon.svg)**Source Control** from the Activity bar to create a new Git repository, access your existing Git repositories, view existing and staged changes, or merge changes.

From here, you can stage and unstage changes, diff between the previous state and the current version of files, and commit changes, all from within the base editor.

## Authenticate with Git

To pull or push changes to your Git repository or clone your repository, as you do when importing a custom sample, you must authenticate with Git.

When you carry out an action that requires authentication, Git prompts you for a password. Enter a personal access token (PAT), which is a more secure alternative to Git passwords. For details on setting up your PAT, see the [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) guide.

To make your workflow more efficient and avoid having to enter your PAT multiple times, turn on credential helper to allow Git to cache your PAT for 15 minutes:

  1. Launch the Cloud Workstations base editor terminal by clicking **Terminal** > **New Terminal**.
  2. Run the following command:
         
         git config --global credential.helper cache
         




For more customization options like changing timeout length and specifying a local path for credential storage, see the [Git Tools - Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) documentation.

## Toggle between multiple repositories

You can work across multiple Git repositories with the Cloud Workstations base editor. To toggle between your repositories, in the Cloud Workstations base editor status bar, click your repository name. From the menu, select the repository to switch your scope to.

This updates your Source Control: Git panel with the context of your chosen repository.

### Display working changes

As you add, modify, and delete files, these changes are reflected under the Changes section in your Source Control: Git panel. You can choose to open the selected file, stage these changes, discard changes, or see what changes are being made in this commit.

### Turn on diff view

In the Source Control: Git panel, your changed files are listed under Changes. If you've staged your changed files, they're also listed under Staged Changes. Clicking any of these files brings up their diff view, showing you what's changed between the previously committed state of the file and the current state.

### Commit changes

When you're ready to check in your changes, you can do so right from within Cloud Workstations.

  1. Run the following git commands using the Cloud Workstations terminal. Be sure to update the email and name with your data:
         
         git config --global user.email alex@example.com
         git config --global user.name Alex
         

  2. To check in your change, in the Source Control: Git panel in the base editor, write a commit message and then click  check_box**Commit** or press `Control+Enter` (or `Command+Enter` on mac OS).




## Clone a repository

To clone a remote Git repository for use in the Cloud Workstations base editor:

  1. Retrieve the repository URL: For GitHub repositories, open the main page of your repository and then open the Clone or Download dialog.
  2. To open the command palette, press `Control+Shift+P` (or `Command+Shift+P` on macOS), or click **View** > **Command Palette**.
  3. Run **Git: Clone**.
  4. When prompted, enter the Git repository location.



## Create and switching between branches

To create a new branch or switch to working on an existing branch:

  1. To open the command palette, press `Control+Shift+P` (or `Command+Shift+P` on macOS), or click **View** > **Command Palette**.
  2. Run **Git: Checkout**.
  3. Select from the list of branches or create a new local branch.



## Git status bar

The Git status bar provides a way to keep track of your current branch and switch to another with the branch indicator. It also provides the Synchronize Changes action to check for changes between your local repository and your upstream branch. Synchronizing changes pushes local changes to your upstream branch and pulls remote changes into your local repository.

If you don't have an upstream branch set up, the Publish action is available to push your local changes to a remote repository.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
