---
url: https://docs.cloud.google.com/code/docs/intellij/view-logs/
title: View Kubernetes logs in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:22.618641+00:00
---

# View Kubernetes logs in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/view-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  View Kubernetes logs in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the streaming logs of your application and to check the status of resources from within Cloud Code.

After your application builds and runs in either regular or development mode, you'll be able to monitor logs streaming from your application from within your IDE. You can also view logs from a specific resource (a pod, a deployment, etc.) by navigating to the Kubernetes Explorer. 

## View the status of tasks and resources

When you start a development or debugging session, you'll be able to monitor logs streaming from your application from [within your IDE](https://docs.cloud.google.com/code/docs/intellij/k8s-overview#view_logs). 

From the Kubernetes Explorer, you can check the status of your deployment in the following ways:

  * **Pod, deployment and node statuses** : These Kubernetes resources have colored status marks next to their labels; red for failed state, yellow for starting/terminating/warning, and green for healthy, desired state.

  * **Deployed resource descriptions** : You can run a `kubectl describe` on your deployed resources to display its details by right-clicking and choosing **Describe**.




## View logs for a specific resource

To view logs from a specific resource, follow these steps: 

  1. Navigate to the Kubernetes Explorer. It can be accessed either from the side panel on the right or using **Tools** > **Cloud Code** > **Kubernetes** > **View Cluster Explorer**.

  2. Select the resource you'd like to see logs from, such as a pod, a deployment, or a service.

  3. Right-click the resource and select **Stream Logs**. Alternatively, you can stream logs for individual containers running in pods.

This outputs logs to the Kubernetes Explorer Console.




## What's next

  * [Debug a Kubernetes application in Cloud Code](https://docs.cloud.google.com/code/docs/intellij/debug).
  * Explore the Kubernetes documentation on [troubleshooting containerized applications](https://kubernetes.io/docs/tasks/debug/debug-application/).



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
