---
url: https://docs.cloud.google.com/code/docs/intellij/kubeconfigs/
title: Work with kubeconfig files in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:04.281084+00:00
---

# Work with kubeconfig files in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/kubeconfigs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Work with kubeconfig files in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

kubeconfig files are Kubernetes configuration files that organize cluster access, users, and contexts. This page shows you how to add, delete and switch between different kubeconfigs in Cloud Code.

For more information about kubeconfig files, see the Kubernetes documentation on [organizing cluster access using kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).

## Manage kubeconfigs

By default, the Cloud Code plugin uses the default kubeconfig file (located under the `$HOME/.kube` directory) for retrieving Kubernetes resources and running commands. However, additional kubeconfig files may be configured.

### Add additional kubeconfig files

To add additional kubeconfig files:

  1. Navigate to Cloud Code settings within your IDE (**File** > **Settings** > **Tools** > **Cloud Code** > **Kubernetes** or for Mac OS X, **IntelliJ IDEA** > **Preferences** > **Tools** > **Cloud Code** > **Kubernetes**).
  2. In the **kubeconfigs** section, click the **\+ Add kubeconfig** icon or press `Alt`+`insert` to bring up the selection dialog.
  3. In the **Select kubeconfig file** dialog, navigate to the location of the kubeconfig file you want to add.
  4. Select the kubeconfig file you want to use, and then click **Ok**.
  5. In the **Settings** dialog, click **OK** to save your changes.



### Remove kubeconfig files

To remove kubeconfig files:

  1. Navigate to Cloud Code settings within your IDE (**File** > **Settings** > **Tools** > **Cloud Code** > **Kubernetes** or for Mac OS X, **IntelliJ IDEA** > **Preferences** > **Tools** > **Cloud Code** > **Kubernetes**).
  2. In the **kubeconfigs** section, click the kubeconfig you want to remove, and then click the **\- Remove** icon or press `Alt`+`Delete`.
  3. Click **Ok** to save your changes.



### Switch kubeconfigs

You can toggle the resource browser's current kubeconfig by clicking on the kubeconfigs drop-down menu and selecting the kubeconfig you want to use. Upon selecting a kubeconfig, the tool window updates to use the chosen kubeconfig.

**Tip** : New kubeconfigs can be added directly using the kubeconfigs drop-down menu.

![Expanding the kubeconfig dropdown menu.](https://docs.cloud.google.com/static/code/docs/intellij/images/kubernetes-explorer-configs.png)

### Using Cloud Code Run Configurations

Cloud Code Run Configurations can be modified to use alternate kubeconfig files. To change kubeconfigs, open the Run Configuration to modify and under **Run** > **Advanced settings** , select the kubeconfig you want to use from the kubeconfig drop-down menu. Upon selecting a kubeconfig, available contexts update to reflect those found in the selected kubeconfig.

**Tip** : New kubeconfigs can be added directly from run configurations by clicking **\+ Add** to the right of the drop-down.

![Editing kubeconfig settings in Run Configurations. Provides a drop-down to
select an already added kubeconfig, and a button to add a new kubeconfig.](https://docs.cloud.google.com/static/code/docs/intellij/images/run-config-kubeconfigs.png)

## What's next

  * [Organize your cluster access using kubeconfig files](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/).
  * [Develop and debug parts of a microservice application](https://docs.cloud.google.com/code/docs/intellij/speed-up-k8s-development#develop-microservices).
  * Learn more about Cloud Code's [YAML editing](https://docs.cloud.google.com/code/docs/intellij/yaml-editing) assistance.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
