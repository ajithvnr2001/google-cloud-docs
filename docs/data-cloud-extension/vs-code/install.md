---
url: https://docs.cloud.google.com/data-cloud-extension/vs-code/install/
title: Install Data Agent Kit \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:58:49.072535+00:00
---

# Install Data Agent Kit  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-cloud-extension/vs-code/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Install Data Agent Kit Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Data Agent Kit lets you work with your Google Cloud data resources in your preferred IDE or agentic coding environment. Depending on your setup, you install either an IDE extension or a plugin.

Data Agent Kit comes pre-installed with the following Google Cloud services:

  * Cloud Shell
  * Cloud Workstations



## Before you begin

Before you install Data Agent Kit, do the following.

### Set up your local environment

On your local machine, install your preferred IDE or coding agent and Node.js.

  1. Install and set up your IDE, agentic CLI, or coding agent. If it's already installed, update it to the latest version.
  2. Install [Node.js](https://nodejs.org/en/download).



### Set up Google Cloud

  1. If you don't already have one, [create a Google Cloud project](https://console.cloud.google.com/cloud-resource-manager).
  2. [Enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project).



### Required roles

Data Agent Kit notifies you when you need additional permissions to accomplish a task. You only need permissions for the services that you use. For a complete list of permissions and APIs that are required for each service in Data Agent Kit, see [Permissions](https://docs.cloud.google.com/data-agent-kit/permissions).

## Install the extension or plugin

Your installation process depends on the IDE or coding agent that you use.

### VS Code

To use Data Agent Kit in VS Code, install the extension:

  1. In the IDE, click **Extensions** or press `Ctrl/Cmd+Shift+X`.
  2. Search for `Google Cloud Data Agent Kit`.
  3. Click **Install**.
  4. If prompted, restart your IDE. After the extension has installed successfully, the Google Cloud Data Agent Kit icon is added to the activity bar.



You can also install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.datacloud).

### Antigravity

Click to expand the instructions for the Antigravity tool that you are using.

#### Antigravity IDE

To use Data Agent Kit in the Antigravity IDE, install the extension.

  1. In the IDE, click **Extensions** or press `Ctrl/Cmd+Shift+X`.
  2. Search for `Google Cloud Data Agent Kit`.
  3. Click **Install**.
  4. If prompted, restart your IDE. After the extension has installed successfully, the Google Cloud Data Agent Kit icon is added to the activity bar.



#### Antigravity CLI

To use Data Agent Kit with the Antigravity CLI, install the plugin. In your terminal, run the following command:
    
    
    agy plugin install https://github.com/GoogleCloudPlatform/data-agent-kit-plugin

#### Antigravity 2.0

To use Data Agent Kit with the Antigravity CLI, install the plugin.

  1. Click **Settings**.
  2. In the **Settings** pane, click **Customizations**.
  3. Locate **Build with Google Plugins** and click **Customize**.
  4. Locate **Google Cloud Data Agent Kit** in the list and click **Download**.



#### Antigravity for VS Code extension

To use Data Agent Kit in VS Code when using the Antigravity for VS Code extension, do the following:

  1. In the VS Code status bar, click **Antigravity - Settings**.
  2. In the **Settings** pane, click **Customizations**.
  3. Locate **Build with Google Plugins** and click **Customize**.
  4. Locate **Google Cloud Data Agent Kit** in the list and click **Download**.



### Claude Code CLI

To use Data Agent Kit with the Claude Code CLI, install the plugin. Run the following command in your terminal:
    
    
    claude plugin marketplace add https://github.com/GoogleCloudPlatform/data-agent-kit-plugin
    claude plugin install dak@dak-marketplace
    

### Codex CLI

To use Data Agent Kit with the Codex CLI, install the plugin. Run the following commands in your terminal:
    
    
    codex plugin marketplace add GoogleCloudPlatform/data-agent-kit-plugin
    codex plugin add dak@dak-marketplace
    

### Cursor

To use Data Agent Kit in Cursor, install the extension.

  1. In the IDE, click **Extensions** or press `Ctrl/Cmd+Shift+X`.
  2. Search for `Google Cloud Data Agent Kit`.
  3. Click **Install**.
  4. If prompted, restart your IDE. After the extension has installed successfully, the Google Cloud Data Agent Kit icon is added to the activity bar.



### VS Code-based IDEs

To use Data Agent Kit with all other IDEs based on VS Code, install the extension.

  1. In the IDE, click **Extensions** or press `Ctrl/Cmd+Shift+X`.
  2. Search for `Google Cloud Data Agent Kit`.
  3. Click **Install**.
  4. If prompted, restart your IDE. After the extension has installed successfully, the Google Cloud Data Agent Kit icon is added to the activity bar.



## Sign in to Data Agent Kit

After installing the extension or plugin, you must sign in.

### Extension sign-in

If you installed the IDE extension, you must authenticate to Google Cloud Data Agent Kit.

  1. If the **sign-in** dialog doesn't open automatically, look for a Google Cloud Data Agent Kit sign-in link in the **status bar** near the bottom of the IDE window, and click it.

Alternatively, you can press `Ctrl/Cmd+Shift+P` to open the **command palette** , search for and select **Google Cloud Data Agent Kit: Sign in**.

  2. Follow the prompts and complete signing in.

A web page confirming that authentication is complete is displayed.

  3. Close the page and return to the IDE.




#### Select services

After you sign in to the extension, the **Select services** page opens. The services that you select determine the sections that appear in the Google Cloud Data Agent Kit menu and the MCP servers, skills, and APIs that are enabled.

  1. Select the Google Cloud services that you want to use.
  2. Click **Next**.

If you're missing any required IAM roles or APIs for the selected services, the **Missing permissions** page opens. Otherwise, the **Quick Start Guide** opens.




You can change your selection later. In the Google Cloud Data Agent Kit menu, expand **Settings** , click **Settings** , and then click **Service Integrations**. If a section in the Google Cloud Data Agent Kit menu shows **integration is not enabled** , click it to enable that service.

### Plugin sign-in

Install and sign in to the Google Cloud CLI. The Data Agent Kit plugin uses credentials from both the gcloud CLI credentials and application default credentials (ADC).

  1. Open the terminal on your local machine or in your IDE.
  2. If you haven't previously installed the gcloud CLI, follow the steps on [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) to download and install the gcloud CLI.
  3. In the terminal, run `gcloud init` to initialize the gcloud CLI: 
         
         gcloud init

  4. Run the following command and follow the prompts to authenticate and set up application default credentials: 
         
         gcloud auth login && gcloud auth application-default login

  5. Update the gcloud CLI to the latest version: 
         
         gcloud components update




## Troubleshoot

If you run into issues, try signing out and then signing in again. To find additional methods for diagnosing and resolving installation errors, see [Troubleshoot](https://docs.cloud.google.com/data-agent-kit/troubleshooting).

## What's next

  * [Set up and configure settings](https://docs.cloud.google.com/data-agent-kit/configure)
  * [Data Agent Kit GitHub repository](https://github.com/GoogleCloudPlatform/data-agent-kit-plugin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
