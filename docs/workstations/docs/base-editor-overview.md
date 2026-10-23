---
url: https://docs.cloud.google.com/workstations/docs/base-editor-overview/
title: Base editor overview \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:04.492953+00:00
---

# Base editor overview  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/base-editor-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Base editor overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations comes with a default base editor that lets you write, build, test, debug, and run your applications. The base editor is based on the [Code-OSS](https://github.com/microsoft/vscode) open source project, supports IDE extensions provided with the [Open VSX Registry](https://open-vsx.org/), and comes with the [Cloud Code](https://docs.cloud.google.com/code/docs/vscode/how-to) IDE extension pre-installed.

To get started using the Cloud Workstations base editor:

  1. Follow the quickstart instructions to [Create a workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration). When prompted to select **Environment customization** , select **Code OSS (default)** as your code editor.
  2. Follow the quickstart instructions to [Create a workstation](https://docs.cloud.google.com/workstations/docs/create-workstation) using the configuration that you just created.

  3. In the Google Cloud console, go to the **Cloud Workstations** page to launch your workstation from the browser. 

[Go to Cloud Workstations](https://console.cloud.google.com/workstations/)




## Activity bar

The Activity bar appears to the side and you can access the views available in the Cloud Workstations base editor. These Activity bar views are as follows:

  * ![](https://docs.cloud.google.com/static/workstations/images/file-explorer-icon.svg)**Explorer** : view the folders and files in your current workspace

  * ![](https://docs.cloud.google.com/static/workstations/images/search-icon.svg)**Search** : search your files for a string or regular expression

  * ![](https://docs.cloud.google.com/static/workstations/images/source-control-icon.svg)**Source Control** : manage application files with the Cloud Workstations base editor's Git support

  * ![](https://docs.cloud.google.com/static/workstations/images/debug-icon.svg)**Debug** : debug your application by setting breakpoints and inspecting variables

  * ![](https://docs.cloud.google.com/static/workstations/images/extensions-icon.svg)**Extensions** : search through a catalog of extensions that add additional features to your IDE

  * ![](https://docs.cloud.google.com/static/workstations/images/cloud-code-icon.svg)**Cloud Code** : create and deploy Google Cloud applications directly from the IDE

  * ![](https://docs.cloud.google.com/static/workstations/images/settings-gear.svg)**Settings** : customize the Cloud Workstations base editor to suit your workflow




## View and edit files

The built-in code editor that lets you browse file directories and view and edit files inside your workstation.

To work with the base editor, follow these steps:

  1. Use the **Activity Bar** to switch between views.

  2. Use the **Editor** to view and edit your files.

  3. Use the **Explorer view** to browse through the file directories, upload and download files, preview web applications on a Cloud Workstations virtual machine instance, and view usage statistics. ![](https://docs.cloud.google.com/static/workstations/images/code-editor-with-callouts.png)Figure 1. Cloud Workstations base editor




## Upload and download files and directories

To upload or download files and directories in the Code-OSS Explorer view, use any of the following methods:

  * Drag files over the Explorer view to add it to the workspace.

  * Navigate to the files and directories you would like to use, right-click, and then choose **Upload** or **Download**.

![](https://docs.cloud.google.com/static/workstations/images/code-editor-upload-download.png)Figure 2. Right-click in Explorer view to upload and download files



## Language support

The Cloud Workstations base editor supports languages such as Go, Python, Java, .NET Core, and Node.js through extensions, providing language features such as:

  * Smart highlighting, code suggestions and context-based completions
  * Linting and providing descriptive errors
  * Code navigation (go to definitions, declarations, references, and implementations)
  * Intuitive debugging support



## Cloud Code integration

[Cloud Code](https://docs.cloud.google.com/code/docs/vscode/how-to) provides IDE support for the full development cycle of Kubernetes and Cloud Run applications, from creating and customizing a new application from sample applications to running your finished application. Cloud Code also supports you along the way with run-ready samples, configuration snippets, and a tailored debugging experience.

Cloud Code integrates with Gemini, an AI-powered collaborator, to simplify development. [Use Gemini to accomplish tasks](https://docs.cloud.google.com/workstations/docs/write-code-gemini) more effectively and efficiently.

Cloud Code supports the development of applications in Node.js, Python, Java, Go, and .NET Core.

In addition to the Cloud Code menu available in the status bar of Cloud Workstations, you can also access Cloud Code commands through the command palette. To open the command palette, press `Control+Shift+P` (or `Command+Shift+P` on macOS), or click **View** > **Command Palette**.

### Data Agent Kit integration

To manage your data science and data engineering workloads directly in base editor, you can use Google Cloud Data Agent Kit, which is integrated with Cloud Code. To use Data Agent Kit, click the **Google Cloud Data Agent Kit** icon in the base editor activity bar. For more information, see [Data Agent Kit overview](https://docs.cloud.google.com/data-agent-kit/overview).

## Version control support

The Cloud Workstations base editor comes with pre-configured version control. You can initialize repositories, diff between file states, stage, unstage, and commit changes. You can also use public, private, or even self-hosted repositories, as long as the repositories are accessible from the workstation.

## Workspace management

With Cloud Workstations, you can manage and configure your projects as workspaces. Workspaces usually represent your root project folder and with the Cloud Workstations base editor, you can create, open, and save workspaces as well as customize them with project-specific settings.

To open a folder as a workspace, use the menu at the top of the activity bar and select **File** > **Open Folder**. Alternatively, you may use the **Open File** or **Recent Workspace** options on the Welcome Page of the base editor, or use the URL parameter `folder` to specify the path of the folder you want to open—for example, `&folder=/home/user/foo`.

## Debug applications

Cloud Workstations lets you debug your application, with support for Go, Node.js, Python, and Java applications. You can create launch configurations, set breakpoints, and inspect variables, all within Cloud Workstations.

Additionally, you can debug Kubernetes applications on a local cluster such as minikube or Docker Desktop, a remote cluster on GKE, or any other Cloud provider.

## Integrated terminal

You can interact with your underlying development environment through the integrated terminal. Use any of the following methods to toggle the terminal view on and off:

  * Press ``Control+``.
  * Press `Control+Shift+P` (or `Command+Shift+P` on macOS), or click **View** > **Command Palette** , and then enter `View: Toggle Terminal`.
  * Select **Terminal** > **New Terminal**.
  * Select **View** > **Terminal**.
  * Click add**Add** in the terminal tab list.



To open multiple terminal windows, click ![](https://docs.cloud.google.com/static/workstations/images/split-icon.svg)**Split** , or press `Control+Shift+5`.

![Workstations code editor](https://docs.cloud.google.com/static/workstations/images/code-editor-with-terminal.png)Figure 4. Cloud Workstations interface with terminal open

### Manage and customize terminal tabs

If you open multiple terminals, a terminal tabs list appears on the side of the terminal view. This list contains names of open terminals.

  * When you select a terminal name in the list, ![](https://docs.cloud.google.com/static/workstations/images/split-icon.svg)**Split** and ![](https://docs.cloud.google.com/static/workstations/images/delete-icon.svg)**Delete** icons appear. Click the respective icon to split or delete a terminal window.

  * To see additional terminal options such as **Move Terminal into Editor Area** , **Rename** , **Change Color** , **Change Icon** , and more, right-click on a terminal name.

![Terminal tabs list](https://docs.cloud.google.com/static/workstations/images/terminal-tabs-list.png)Figure 5. Customize your terminal



### Scroll the display

In addition to using your mouse while browser focus is on a session tab, you can scroll by pressing `Control+Shift+PageUp` and `Control+Shift+PageDn` on Windows and Linux (or `Fn+Shift+Up` and `Fn+Shift+Down` on macOS).

## Customize settings

To customize the editor, user interface, and functional behavior, the Cloud Workstations base editor provides the following scopes for defining settings:

  * **Machine Settings** : Settings that apply globally when you connect to a Cloud Workstations virtual instance and that appear on your workstation in the `$HOME/.codeoss-cloudworkstations/data/Machine/settings.json` file.

  * **User Settings** : Settings that apply globally when you connect to a Cloud Workstations virtual instance and that persist in browser storage for each workstation instance.

  * **Workspace Settings** : Settings stored inside a workspace that only apply when opening that workspace. These settings appear with your workspace files in the `$WORKSPACE_ROOT/.vscode/settings.json` file.




The editor evaluates each settings scope respectively.

## Keyboard shortcuts

Because the default base editor runs in the browser, some keyboard shortcuts might be reserved by the browser and not captured by the editor.

To support all keyboard shortcuts, the default base editor bundles a Progressive Web App (PWA) that allows the editor to capture these shortcuts.

To use the PWA:

  1. Open the Workstation in your browser.
  2. Click the installation icon that appears in your browser's address bar.



The PWA should then be installed and the Workstation reopens in the PWA. On subsequent loads of your Workstation the browser presents an option to reopen the Workstation in the PWA in the address bar.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
