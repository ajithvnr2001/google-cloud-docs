---
url: https://docs.cloud.google.com/code/docs/intellij/watch-modes/
title: Watch modes in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:37.349923+00:00
---

# Watch modes in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/watch-modes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Watch modes in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Code allows you to quickly apply changes to your application during a development or debug session for a faster feedback loop. This lets you run your Kubernetes and emulated Cloud Run sessions in _watch mode_.

To learn more about how deployment works, please see the [Skaffold documentation.](https://skaffold.dev/docs/workflows/dev/#file-watcher-and-watch-modes)

## Settings for Kubernetes and Cloud Run configurations

You can configure watch mode in the Cloud Code Kubernetes and Cloud Run configurations at **Run** > **Edit configurations** on the **Run** tab:

Watch mode | Description  
---|---  
**On demand** | 

  * The default value for new run configurations.
  * Cloud Code only rebuilds and redeploys your application when triggered. To trigger On-demand mode, click ![On demand trigger button](https://docs.cloud.google.com/static/code/docs/intellij/images/watch-mode-on-demand-trigger.png)**Trigger Build and Deploy** or press `Option+Cmd+Comma` on Mac OS or `Ctrl+Alt+Comma` on Windows (the default key bindings).
    * If you'd like to customize these key bindings, see Customizing the Trigger Build and Deploy keymap.

  
**On file save** | 

  * Rebuilds and redeploys your application after you save any changes.
  * This option is not available in debug mode.

  
![Watch mode options](https://docs.cloud.google.com/static/code/docs/intellij/images/watch-mode-options.png)

### Customizing the Trigger Build and Deploy keymap

The default key bindings for ![On demand trigger button](https://docs.cloud.google.com/static/code/docs/intellij/images/watch-mode-on-demand-trigger.png)**Trigger Build and Deploy** are:

  * Mac OS: `Option+Cmd+Comma`
  * Windows: `Ctrl+Alt+Comma`



To change the default key bindings:

  1. Navigate to **Preferences** > **Keymap**.
  2. In the Keymap search bar, enter "trigger build and deploy".
  3. Right-click the Trigger Build and Deploy search result and select **Add Keyboard Shortcut**.
  4. Enter shortcut combination you prefer (for example, `Shift+R`) and click **OK** , then click **OK** in the Preferences window. This adds your new key binding to the Trigger Build and Deploy function, so that both the default and your new key binding will work.
  5. You can also remove the default key binding by right-clicking the Trigger Build and Deploy search result and selecting the **Remove** option.



## Applying changes while debugging

With Cloud Code, you can debug an application while making changes to, and iterating on, source code. This is available for Kubernetes development and Cloud Run local development.

**Note:** Certain runtimes support other modes of live updating; for example, Java and HotSwap over JDWP. HotSwap, while limited by the types of changes supported, maintains your debugger state. This design, which operates over [Skaffold](https://skaffold.dev/) debug, assumes the debugger will be destroyed and reattached on change. These other modes of updating code will continue to be supported independently.

To apply changes to your code while debugging, perform the following:

  1. Ensure On-demand mode is enabled in **Run** > **Edit Configurations** (the default option).
  2. Launch the run configuration in debug mode by clicking ![Debug icon](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debug-action.png)**Debug**.



### Common use case

This section outlines a common scenario of how you can debug with watch mode enabled in your IDE.

#### Debugging a Kubernetes application with watch mode enabled

You're a developer building an application that runs on Kubernetes, and use Cloud Code to iterate on your app. You discovered a bug in your code.

  1. You launch the Develop on Kubernetes run configuration, and:
     1. Select **On demand** to rebuild and redeploy the app.
     2. Launch the run configuration in debug mode by clicking ![Debug icon](https://docs.cloud.google.com/static/code/docs/intellij/images/k8s-debug-action.png)**Debug**.
  2. You set a breakpoint near the expected bug, launch the app, and use the debugger to figure out what the bug is.
  3. You fix the bug while the development session is still running (the debugger is still attached). You now want to confirm that the issue is fixed.
  4. You trigger On-demand mode which tells Cloud Code to rebuild and redeploy the application, by clicking ![On demand trigger button](https://docs.cloud.google.com/static/code/docs/intellij/images/watch-mode-on-demand-trigger.png)**Trigger Build and Deploy** or pressing `Option+Cmd+Comma` on Mac OS or `Ctrl+Alt+Comma` on Windows (the default key bindings).
  5. A notification appears and asks you to confirm: "Redeploying your changes will cause the debugger to be stopped and reattached, potentially losing your current debug state". You have the option to either cancel, continue, or to never be notified again.
  6. After clicking **continue** :
     * The debugger is terminated
     * The application is rebuilt and redeployed
     * The debugger is reattached
  7. You can now verify the changes and debug again as needed.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
