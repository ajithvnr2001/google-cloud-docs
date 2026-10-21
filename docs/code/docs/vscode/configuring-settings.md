---
url: https://docs.cloud.google.com/code/docs/vscode/configuring-settings/
title: Configure Cloud Code for VS Code settings \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:15.104768+00:00
---

# Configure Cloud Code for VS Code settings  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/configuring-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  Configure Cloud Code for VS Code settings Stay organized with collections  Save and categorize content based on your preferences. 

You can customize Cloud Code to enable cluster resource completion, enable YAML formatting and validation, display or hide explorers, collect telemetry, and customize your Kubeconfig path.

## Specifying preferences using VS Code Settings

To configure VS Code Settings, click settings **Manage** > **Settings** and then search for `cloudcode`.

Configuring preferences this way lets you change the defaults that Cloud Code saved when you were first prompted for preferences. These settings include preferences for YAML formatting and completion, telemetry collection, the KubeConfig file path, wrapping style, and criteria for YAML file matching. Other Cloud Code settings are configurable using your `settings.json` file.

## Working with additional KubeConfig files

A [KubeConfig file](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) is a file that Kubernetes uses to configure access to clusters. By default, Cloud Code uses the default KubeConfig file (located in the `$HOME/.kube` directory) for retrieving Kubernetes resources and running commands.

### Importing a new KubeConfig

To import an alternative KubeConfig file into Cloud Code, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** section.
  2. Hold the pointer over the default config name.
  3. Click sync_alt **Switch KubeConfig** next to the Default Config and then click **\+ Load KubeConfig**.
  4. In the file explorer, select the KubeConfig that you want to import. The file you imported becomes the active KubeConfig file.



**Tip:** If you've imported multiple KubeConfig files, you can easily switch between them by clicking sync_alt **Switch KubeConfig** and then selecting another KubeConfig file.

### Removing a KubeConfig

To remove the KubeConfig file(s) that you've imported, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**), run the **Remove KubeConfig from Kubernetes Explorer** command, and then select the configs that you want to remove.

## Configuring settings in `settings.json`

Some advanced settings, like Cloud Code debugger customizations, are configured in the `settings.json` file.

  1. In Settings, click **Edit in settings.json** under the setting that you want to change. The `settings.json` file opens at the appropriate setting.
  2. Type a quotation mark (") to open the list of properties or values for the setting. For example, typing " in `cloudcode.debug-kubernetes` gives the options of `SuppressGoWarning`, `SuppressJavaWarning`, `SuppressNETCoreWarning`, `SuppressNodeJSWarning`, and `SuppressPythonWarning`.
  3. Click the property and then click the value you want the property to have, or, if the setting takes a value directly, click the value. For example, clicking `SuppressNodeJSWarning` gives the options of `true` and `false`.



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
