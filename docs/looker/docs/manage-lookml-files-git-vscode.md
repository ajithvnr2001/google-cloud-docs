---
url: https://docs.cloud.google.com/looker/docs/manage-lookml-files-git-vscode/
title: Managing LookML files and Git with the Looker extension for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:08:33.429799+00:00
---

# Managing LookML files and Git with the Looker extension for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/manage-lookml-files-git-vscode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Managing LookML files and Git with the Looker extension for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

The [**Looker extension for VS Code**](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension) uses a local-first development model. This model maintains a three-way relationship among your local file system, your Looker instance's [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode), and your remote Git repository.

This guide explains how the extension synchronizes files and how local Git operations impact your Looker project.

## Sync mechanism

The extension automatically manages the synchronization of file content between your local IDE and the Looker server.

### Opening files (read-on-open)

When you open a `.lkml` file in your local IDE, the extension automatically fetches the current version of that file from your checked-out branch in your Looker instance's Development Mode. This ensures that you're always working on the most up-to-date version of the code.

### Saving files (write-on-save)

When you save a file locally (**Command-S** on Mac or **Ctrl+S** on Windows/Linux), the extension immediately pushes your local changes to the Looker server. These changes are then visible in the browser-based Looker IDE when you're in Development Mode.

**Note:** This file-level synchronization is separate from Git. Saving a file does not create a Git commit on either the local or remote repository.

## Handle sync conflicts

If a file is edited in the browser-based Looker IDE while it is also open in VS Code, a conflict may occur.

By default, the extension will overwrite the version on the Looker server with your local VS Code version.

However, if you have enabled the `looker.askBeforeOverwritingRemote` setting, VS Code displays a warning when you attempt to save a file that has been modified on the server. You can choose to take one of the following actions:

  * **View Diff** : Open a diff editor to compare changes between the remote and local versions of the file. This option lets you selectively view and merge changes line by line to resolve the conflict and sync the merged local changes back to the Looker server.
  * **Overwrite Remote** : Overwrite the version on the Looker server with your local VS Code version.
  * **Overwrite Local** : Overwrite your local file with the version from the Looker server.



The `looker.askBeforeOverwritingRemote` setting is disabled by default.

## Local Git operations

The extension synchronizes file content, but you should manage your Git repository by using standard Git commands in your local terminal or the local IDE's Source Control tab.

**Note:** You can also use the browser-based Looker IDE to perform these Git actions if preferred.

### Manage branches

When you switch branches locally by using `git checkout`, the extension detects the change and automatically switches your session on the Looker server to the matching branch.

Before Looker syncs your file changes, the Looker extension for VS Code verifies that your local Git branch matches your Looker Development Mode branch, automatically pausing synchronization if the branches diverge, which prevents cross-branch overwrites. If a mismatch occurs, an interactive prompt lets you either switch your remote Looker workspace or check out the branch locally, automatically invalidating cached file hashes upon alignment to resume sync safely.

### Git state in Looker

When you save file changes, they are synced to your Looker instance and appear as uncommitted in the browser-based Looker IDE. If you commit these changes using Git in your local environment, they will continue to appear as uncommitted in the Looker IDE until you push them to your remote repository.

When you use `git push`, your Looker instance pulls the committed changes from your remote repository. After your Looker instance has pulled from remote, changes that you have committed and pushed will no longer appear as uncommitted in the Looker IDE. Only files that are saved locally but not yet committed and pushed will appear as uncommitted.

## Validate LookML

The extension automatically runs the [Looker LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation) every time you save a change. Any syntax and model errors returned by the Validator will appear inline within your files inside your local IDE. If you want, you can also run the LookML Validator manually without saving files using the **Looker: Validate LookML** Command Palette command.

## What's next

  * [AI-assisted development (vibe coding) with Looker](https://docs.cloud.google.com/looker/docs/ai-assisted-development-vscode)
  * [LookML reference overview](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
