---
url: https://docs.cloud.google.com/shell/docs/workspaces/
title: Workspace management in the Cloud Shell Editor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:12.300623+00:00
---

# Workspace management in the Cloud Shell Editor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/workspaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Workspace management in the Cloud Shell Editor Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Shell Editor lets you manage your projects as workspaces. A workspace usually represents the root folder of your project and includes your project-specific configuration files. A Home workspace (based on your Home directory) is created for you automatically.

With workspaces, you can specify persistent settings, run and debug configurations, and UI states (like open files) for all the folders in your workspace.

This page explains how to create, open, save, and close a workspace, and configure Cloud Shell Editor and workspace settings.

## Create a new workspace

To create a new workspace:

  1. Using the Cloud Shell terminal, create a new directory to use as your workspace: 
     * Use `mkdir` to manually create a new directory
     * Use `git clone` to copy in an existing repository
  2. After your directory is ready, open it as a new workspace by clicking **File** > **Open Workspace**.



## Open a workspace

You can open a workspace in one of the following ways:

  * Click **File** > **Open Folder**.

  * If no workspaces are open, click the **Open Folder** button in the Cloud Shell Editor Explorer view.

![Open Workspace button accessible in Explorer when no workspaces are open](https://docs.cloud.google.com/static/shell/docs/images/open-workspace.png)

  * Select a recently opened workspace from the Recent section in the Welcome to Cloud Shell window.

Alternatively, click **File** > **Open Recent Workspace**.

![Recently opened workspaces like hello-world-1 and appengine-guestbook-python available under Recent. Clicking their linked names opens the workspace in the Explorer](https://docs.cloud.google.com/static/shell/docs/images/open-recent-workspace.png)




## Open a Home workspace

To operate using a Home workspace, open your Home directory as your workspace by clicking **File** > **Open Folder** and then choose your Home directory.

### Save a workspace

After you've added project folders to your workspace and configured it, you can save your workspace under a new name by clicking **File** > **Save Workspace As**.

### Close a workspace

To close your workspace, click **File** > **Close Folder** and then click **OK** when prompted.

### Delete a workspace

**Warning:** These actions will delete your folder and can't be undone.

To delete the folder, run the following command:
    
    
    rm -rf FOLDER_NAME
    

## Configure settings

The Cloud Shell Editor's behavior and interface are easily configured with the Settings menu. You can define your preferences for debugging configurations, YAML editing support, and Command Palette history limits, among a variety of settings using this Settings editor. Settings are accessible through the Settings Gear ![Settings Gear icon](https://docs.cloud.google.com/static/shell/docs/images/settings-gear-icon.png), in the bottom left corner of the editor.

There are three scopes for settings:

  * **User settings** : Globally-applicable settings, applied to all your instances of the Cloud Shell Editor. This configuration is stored in the browser.
  * **Remote settings** : Globally-applicable settings, applied to all your instances of the Cloud Shell Editor. These settings are stored in your Cloud Shell home directory under $HOME/.codeoss/data/Machine/settings.json.
  * **Workspace settings** : Workspace-specific settings, applied to only the active workspace. These settings are saved in the .codeoss/settings.json file in your workspace folder and can be shared using [version control](https://docs.cloud.google.com/shell/docs/version-control) or by [downloading](https://docs.cloud.google.com/shell/docs/uploading-and-downloading-files) the workspace folder.

**Note:** When a setting is set in more than one scope remote settings override user settings, and workspace settings override both remote and user settings.

To search for a setting, you can use the **Search Settings** search bar that returns a set of settings that match your query, filtering out those that don't relate to your criteria. The settings themselves can be set either by filling in the input field, choosing an option from a dropdown menu, or toggling a checkbox.

![Settings interface with tabs for User and Workspace with Debug settings being viewed](https://docs.cloud.google.com/static/shell/docs/images/settings-view.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
