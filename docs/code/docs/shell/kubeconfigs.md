---
url: https://docs.cloud.google.com/code/docs/shell/kubeconfigs/
title: Work with kubeconfigs in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:09.330914+00:00
---

# Work with kubeconfigs in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/kubeconfigs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Work with kubeconfigs in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

kubeconfig files are Kubernetes configuration files that organize cluster access, users, and contexts. This page shows you how to add, delete and switch between different kubeconfigs in Cloud Code.

For more information about kubeconfig files, see the Kubernetes documentation on [organizing cluster access using kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).

## Manage kubeconfigs

By default, the Cloud Code plugin uses the default kubeconfig file (located under the `$HOME/.kube` directory) for retrieving Kubernetes resources and running commands. However, additional kubeconfig files may be configured.

### Add additional kubeconfig files

To add additional kubeconfig files:

  1. Open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**), and then run **Cloud Code: Switch kubeconfig**.
  2. Click **\+ Load kubeconfig** , and then navigate to the location of the kubeconfig file you want to add.
  3. Select the kubeconfig file you want to add, and then click **Add KubeConfig Path**.
  4. Provide a name for the new kubeconfig when prompted.
  5. Press `Enter` to confirm.



### Remove kubeconfig files

To remove kubeconfig files:

  1. Open the command palette (press `Ctrl`/`Cmd`+`Shift`+`P` or click **View** > **Command Palette**), and then run **Cloud Code: Remove KubeConfig from Kubernetes Explorer**.
  2. Select the checkbox next to the kubeconfig you want to remove, and then click **Ok**.



### Switch kubeconfigs

You can switch kubeconfigs using the **Command palette**. To switch kubeconfigs:

  1. Open the **Command palette** , and then run **Cloud Code: Switch KubeConfig**.
  2. Click on the kubeconfig you want to use.



## What's next

  * [Organize your cluster access using kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).
  * [Develop and debug parts of a microservice application](https://docs.cloud.google.com/code/docs/shell/speed-up-k8s-development#develop-microservices).
  * Learn more about Cloud Code's [YAML editing](https://docs.cloud.google.com/code/docs/shell/yaml-editing) assistance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
