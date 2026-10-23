---
url: https://docs.cloud.google.com/shell/docs/debugging/
title: Debug with Cloud Shell Editor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:43.379024+00:00
---

# Debug with Cloud Shell Editor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/debugging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback 

#  Debug with Cloud Shell Editor Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Debugging support is available for Go, Node.js, Python, Java, and Ruby applications.

The Cloud Shell Editor allows you to easily debug your application. With the editor's debugging support, you skip manual setup like setting up port forwarding or injecting language-specific debug arguments. You can create launch configurations, set breakpoints, and inspect variables, all in the editor.

## Debug actions

To access the Cloud Shell Editor's debugging support, click ![Debug View icon](https://docs.cloud.google.com/static/shell/docs/images/debug-icon-cs.png)**Debug** in the Activity bar. Sample applications come with a `launch.json` file needed to run and debug your application. If your application doesn't have one, you're prompted in the Debug View to create one.

In the Debug View, start a debugging session by clicking ![Start Debugging icon](https://docs.cloud.google.com/static/code/docs/vscode/images/debugdropdown.png)**Start**. When prompted, choose the context to run your app in and, if applicable, the image registry to use.

After your debugging session starts, you can manage it with the Debugging action icons: Pause, Step over, Step in, Step out, Restart, Stop.

![Debugging start icon along with pause, step over, step in, step out, restart, and stop icons](https://docs.cloud.google.com/static/shell/docs/images/debug-actions.png)

## Set breakpoints

To set or toggle breakpoints, click in the editor margin next to the line you want to break at. Red circles are active breakpoints and gray circles are inactive breakpoints. If a breakpoint can't be registered with the debugger when a session starts, it changes to a gray-outlined hollow circle.

![Setting a breakpoint at line 45](https://docs.cloud.google.com/static/shell/docs/images/setting-breakpoints.png)

When running a debugging session, the app stops at the breakpoint and you can inspect the Variables panel in the Debug View to inspect variable values as the app is paused.

![Debugging session showing app paused at breakpoint and variable values in scope](https://docs.cloud.google.com/static/code/docs/vscode/images/quickstart-debug-breakpoints.png)

## Additional Kubernetes debugging support

With the Cloud Shell Editor, you can debug Kubernetes applications on a local cluster (like minikube or Docker Desktop) or a remote cluster on GKE or any other Cloud provider. You can also attach a debugger to a Kubernetes pod.

Refer to the [Debugging Kubernetes applications](https://docs.cloud.google.com/code/docs/shell/debug) using the Cloud Shell Editor guide for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
