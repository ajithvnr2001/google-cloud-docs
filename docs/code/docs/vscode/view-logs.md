---
url: https://docs.cloud.google.com/code/docs/vscode/view-logs/
title: View Kubernetes logs in Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:52.773864+00:00
---

# View Kubernetes logs in Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/view-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback 

#  View Kubernetes logs in Cloud Code for VS Code Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the streaming logs of your application and to check the status of resources from within Cloud Code.

The Development sessions view provides a structured view of the logging output that surfaces tasks, artifacts, and deployed resources. This view lets you see the status of each task in your deployment and locate more information in the full logging output.

The Log Viewer provides tools for searching and filtering logs.

## View the status of tasks and resources

When you start a development or debugging session, the [**Development sessions** section](https://docs.cloud.google.com/code/docs/vscode/k8s-overview#development-section) displays the structured logging view.

  * To view the **Development sessions** section, open the Command Palette (press `Ctrl`/`Cmd`+`Shift`+`P`) and then run the **Cloud Code: Focus on development sessions explorer** command.

  * As a task begins, a progress_activity spinning semi-circle progress indicator appears.

  * If a task succeeds, a check_circle checkmark appears next to the step.

  * If a task fails, an error error mark appears next to the step.

  * To see details of a step, click the step in the **Development sessions** section. The **Output** tab displays the step in the logging output.

  * To view the full [Skaffold](https://skaffold.dev/) logs, click the **Status** node.

  * To view the logs for a container, expand **Status** , expand **Stream Application Logs** , and then click the container name. The logs for the container are displayed in the **Output** tab.




## Launch the Log Viewer

To launch the [Log Viewer](https://docs.cloud.google.com/code/docs/vscode/k8s-overview#view_logs), open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: View Logs**.

## Stream logs from a pod

To stream logs from a pod:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** section.
  2. Expand your minikube cluster and then expand **Pods**.
  3. Right-click a pod and then click **Stream Logs**.
  4. If there are multiple containers in the pod, select a container when prompted.



## View logs from a pod

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** section.
  2. Expand your minikube cluster and then expand **Pods**.
  3. Right-click a pod and then click **View Logs**
  4. If there are multiple containers in the pod, select a container when prompted.



## View logs for a specific resource

To view the logs for a specific resource, follow these steps:

  1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Kubernetes** section.
  2. In the **Kubernetes** section, expand the following:

     * The cluster whose logs you want to view
     * **Namespaces**
     * The namespace whose logs you want to view
     * **Deployments**
  3. Right-click the deployment and select **View logs**.




## View streaming logs

To have the Log Viewer display updated logs as the logs are generated, in the Log Viewer, turn the **Streaming** slider on.

## View Kubernetes logs using Cloud Logging

To display logs from GKE clusters with [Cloud Logging](https://docs.cloud.google.com/logging/docs) enabled, follow these steps:

  1. To open the Log Viewer, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: View Logs**.
  2. Select **Kubernetes Application Logs** from the **Log Type** list.
  3. To stream logs from multiple pods, turn on the **Streaming** slider and select **all** in the **Pod** list.
  4. Logs are displayed for the active cluster by default. To switch to a different cluster, select the cluster name from the **Cluster** list.



## View Kubernetes logs using kubectl

To display logs from a non-GKE cluster or a GKE cluster without Cloud Logging enabled, follow these steps:

  1. To open the Log Viewer, open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**) and then run **Cloud Code: View Logs**.
  2. Select **Kubectl Logs** from the **Log Type** list.
  3. In the **Deployment** or **Pod** list, select a deployment or pod to view logs from.
  4. To refine your search results, click **Search Logs** and then type search terms. This search includes the namespace, deployment, pod, container, and time. For clusters with Cloud Logging enabled, you can also filter by severity level.



## Change the display time

To change the display time to a different time zone, click more_vert**More** next to the **Time** column header and then choose a time zone.

## What's next

  * [Debug a Kubernetes application in Cloud Code](https://docs.cloud.google.com/code/docs/vscode/debug).
  * Explore the Kubernetes documentation on [troubleshooting containerized applications](https://kubernetes.io/docs/tasks/debug/debug-application/).



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
