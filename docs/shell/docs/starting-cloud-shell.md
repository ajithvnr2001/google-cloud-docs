---
url: https://docs.cloud.google.com/shell/docs/starting-cloud-shell/
title: Use Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:20.630463+00:00
---

# Use Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/starting-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/quickstart)



Send feedback 

#  Use Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to start and set up a new Cloud Shell session.

## Start a new session

Click ![](https://docs.cloud.google.com/static/shell/docs/images/activate-cloud-shell-button.svg)**Activate Cloud Shell** at the top of the Google Cloud console.

A Cloud Shell session opens inside a new frame at the bottom of the Google Cloud console and displays a command-line prompt. It can take a few seconds for the session to be initialized.

### Use the terminal

Cloud Shell provides command-line access to the virtual machine instance in a terminal window that opens in the Google Cloud console.

In addition to accessing the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and other utilities from the command line, you can use the `cloudshell` command to launch tutorials, open the Cloud Shell Editor, and download files.

Refer to the guide on using the [Cloud Shell Terminal](https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal) for more details.

### Use the Cloud Shell Editor

The built-in code editor provides the convenience of viewing and editing files in the same environment where projects are built and deployed. Launch the Cloud Shell Editor by clicking ![Code Editor Button](https://docs.cloud.google.com/static/code/docs/shell/images/open-editor.png)**Open Editor** on the toolbar of the Cloud Shell window.

For more information, see [Cloud Shell Editor interface overview](https://docs.cloud.google.com/shell/docs/editor-overview).

### Choose ephemeral mode

By default, Cloud Shell provisions 5 GB of free persistent disk storage on your temporarily allocated virtual machine. This is your `$HOME` directory. When you use the default Cloud Shell experience, the files in your home directory persist between sessions.

If you do not need persistent storage, use Cloud Shell in ephemeral mode. In ephemeral mode, you can get started with Cloud Shell faster because there is less set up and there is no disk attachment or archive. However, this means that all the files you create during your ephemeral mode session are deleted with the VM when the session ends.

To choose ephemeral mode, append `ephemeral=true` to the `https://shell.cloud.google.com` URL. For example: `https://shell.cloud.google.com/?ephemeral=true`.

This does not work for `https://console.cloud.google.com` URLs.

Alternatively, you can open the Cloud Shell ![More menu icon](https://docs.cloud.google.com/static/shell/docs/images/more.svg)**More** menu, select **Ephemeral mode** , and click **Save**.

To set ephemeral mode as your Cloud Shell default, enable **Always start Cloud Shell in ephemeral mode** before you click **Save**.

### Adjust the display window

To adjust the display window:

  1. Click ![Hide Shell Button](https://docs.cloud.google.com/static/shell/docs/images/hide-button.png)**Hide** or ![Restore Shell Button](https://docs.cloud.google.com/static/shell/docs/images/restore-button.png)**Restore** to hide or restore the session display.

  2. Click ![Detach Shell Button](https://docs.cloud.google.com/static/shell/docs/images/detach-button.png)**Open Session in New Window** to detach the session as a new window.

  3. To close the detached window and re-open the session in the Google Cloud console, click ![](https://docs.cloud.google.com/static/shell/docs/images/activate-cloud-shell-button.svg)**Activate Cloud Shell** at the top of the Google Cloud console window.

  4. To toggle between themes, click ![Settings Button](https://docs.cloud.google.com/static/shell/docs/images/settings-button.png)**Settings** and then click **Switch to Light Theme** or **Switch to Dark Theme**.




## What's next

Now that you're familiar with configuring Cloud Shell, you can start to use the [pre-installed tools and commands](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works#tools) from the command line. You can also install additional tools in your [home directory](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works#persistent_disk_storage) in persistent disk storage as needed.

  * [Learn how to use web preview](https://docs.cloud.google.com/shell/docs/using-web-preview)
  * [Explore examples of things you can do in Cloud Shell](https://docs.cloud.google.com/shell/docs/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
