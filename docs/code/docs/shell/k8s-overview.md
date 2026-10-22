---
url: https://docs.cloud.google.com/code/docs/shell/k8s-overview/
title: Cloud Code for Cloud Shell Kubernetes overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:53.436399+00:00
---

# Cloud Code for Cloud Shell Kubernetes overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/k8s-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Cloud Code for Cloud Shell Kubernetes overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Kubernetes development in Cloud Code.

## Use the Kubernetes Explorer in Cloud Code

The **Kubernetes** Explorer lets you access information about your clusters, nodes, workloads, and more, right from your IDE. You can also set a current context, stream and view logs, open an interactive terminal, and look up resource descriptions with the Kubernetes Explorer.

![Cloud Code Kubernetes explorer](https://docs.cloud.google.com/static/code/docs/shell/images/shell-dev-cluster-k8s-sections.png)

Cloud Code uses the default kubeconfig file, located under the `$HOME/.kube` directory on MacOS/Linux or `%USERPROFILE%\.kube` on Windows, for retrieving Kubernetes resources. You can switch or add new Kubeconfig files from within the Kubernetes Explorer. Kubeconfig files are YAML files containing your Kubernetes cluster details, certificate, and secret token for authenticating to the cluster.

To use a kubeconfig file other than the default kubeconfig, refer to the [Work with kubeconfig files](https://docs.cloud.google.com/code/docs/intellij/kubeconfigs) guide.

## Access the Kubernetes Explorer

To view and manage your Kubernetes resources, access the **Kubernetes** Explorer by clicking ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and expanding the **Kubernetes** section. To view debugging sessions or create a sample app, expand the **Development sessions** section. 

## Access the Development sessions section

Use the Development sessions to run or debug your Kubernetes application or create a sample application using a template. 

When you start a development or debugging session, the **Development sessions** section displays the structured logging view.

![Development sessions pane](https://docs.cloud.google.com/static/code/docs/vscode/images/development-sessions.png)

To access the Development sessions, click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and expand the **Development sessions** section. 

## Basic actions

The **Kubernetes** Explorer is powered by `kubectl`. As long as you've configured your `kubectl` config file to access your clusters, you can use the **Kubernetes** Explorer to add clusters, browse all your available namespaces, resources, and nodes for your clusters, regardless of them being in the active or inactive context.

### Clusters section

The available general Kubernetes actions, accessible through their icons in the Kubernetes Explorer **Clusters** section, are:

  * add Add a cluster to the KubeConfig
  * refresh Refresh the **Kubernetes** Explorer
  * question_mark Open the Cloud Code Kubernetes documentation in a web browser



### Development sessions section

The available Kubernetes actions, accessible through their icons in the Kubernetes **Development sessions** section, are:

  * ![Open Kubernetes sample icon](https://docs.cloud.google.com/static/code/docs/vscode/images/open-k8s-sample.png) Open a Kubernetes sample application
  * play_arrow Run your application
  * ![Debug icon](https://docs.cloud.google.com/static/code/docs/vscode/images/debug-icon-new.png) Debug your application



### Copy a resource name

You can copy any Kubernetes resource name to the clipboard (including container and cluster names). To copy a resource name, right-click on the resource and choose **Copy resource name**.

![Copy resource name using right-click menu](https://docs.cloud.google.com/static/code/docs/shell/images/shell-copy-resource-name.png)

### Refresh resources

The **Kubernetes** Explorer watches for changes and automatically refreshes to reflect updates. To force a refresh of any Kubernetes resource to fetch its latest information, right-click the resource and choose **Refresh**.

![Refresh pods using right-click menu](https://docs.cloud.google.com/static/code/docs/shell/images/shell-refresh-resource.png) You can also force a refresh of the entire **Kubernetes** Explorer **Clusters** section using the **Clusters** section's refresh button. 

![Clusters section refresh button](https://docs.cloud.google.com/static/code/docs/shell/images/shell-clusters-refresh-section.png)

### Describe resources

To display the details of any non-cluster resource, right-click the resource, then select **Describe**. A terminal opens and displays the resource information. ![Describe resource details in right-click menu](https://docs.cloud.google.com/static/code/docs/shell/images/shell-describe-resource.png)

## Customize your launch configuration

To configure how your application is run, you can customize your [`skaffold.yaml`](https://skaffold.dev/docs/references/yaml) file.

### View remote YAML

To view the YAML of a resource in your cluster, select or hover over the resource to show the ![](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-edit-yaml-icon.png)**Edit YAML** and ![](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-view-yaml-icon.png)**View YAML** icons. Select the **View YAML** button to open the YAML file corresponding to your specified resource in a new editor tab. ![Kubernetes service YAML opened using the View YAML icon](https://docs.cloud.google.com/static/code/docs/shell/images/shell-view-yaml.png)

### View logs

You can stream and view logs from Kubernetes resources into the Kubernetes Explorer console to monitor their progress.

To open the **logs viewer** , open the command palette by pressing `Ctrl/Cmd+Shift+P` or clicking **View > Command Palette** then select **Cloud Code: View Logs**. 

![View logs dialog in the command palette](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-command-palette-view-logs.png)

The **logs viewer** opens in a new editor tab.

![Logs viewer](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-logs-viewer.png) To view logs for a pod or container, right click on the resource and select **View logs**.

![Viewing logs for a pod](https://docs.cloud.google.com/static/code/docs/shell/images/shell-view-logs.png)

### Launch a terminal

For pods and containers, you can open an interactive terminal by right-clicking the pod or container and selecting **Get terminal**.

![Opening an interactive terminal](https://docs.cloud.google.com/static/code/docs/shell/images/shell-get-terminal.png)

## Resource-specific actions

The Kubernetes Explorer displays clusters, namespaces, nodes, workloads (such as deployments, replicasets, pods and containers), services and ingresses, configurations (such as secrets and config maps) and storage (such as volumes). Using the Kubernetes Explorer, you can perform unique actions on some of these resources.

### Clusters

  * **Add a cluster to the Kubeconfig:** Add an existing GKE or minikube cluster or create a new one.



The Add Cluster dialog appears and you can choose the project and cluster you'd like to use or create a new cluster.

![Choosing cluster platform](https://docs.cloud.google.com/static/code/docs/shell/images/shell-cluster-choose-platform.png)

![Create or choose a GKE cluster](https://docs.cloud.google.com/static/code/docs/shell/images/shell-create-or-choose-cluster.png)

  * **Set as active cluster:** Set the specified cluster as active such that your configured `kubectl` context accesses this cluster by default.

![Set cluster as active using right-click menu](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-set-active-cluster.png)




The Kubernetes Explorer refreshes automatically and you'll see the Kubernetes symbol next to the appropriate cluster.

If a cluster has multiple contexts configured, you'll be able to choose one of the available contexts to set as the current context.

### Namespaces

  * **Set as active namespace:** Set a namespace as active such that your configured `kubectl` context accesses this namespace by default.

Right-click the namespace you want to set as active.

![Set namespace as the current context using the right-click menu](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-set-active-namespace.png)


If this action is successful, the Kubernetes Explorer refreshes automatically and you'll see an asterisk next to the namespace to signify that it's part of the current context. 

Note that a Kubernetes context is a shortcut which gives you quick access to a namespace in your cluster. Contexts are normally created automatically when you start a minikube or GKE cluster. If you don't see the **Set as current context** option for a given namespace and you'd like to create a context for it, use the [`kubectl config set-context` command](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-set-context-em-) in your terminal to set a context with your preferred cluster, user, and namespace.

### Pods

  * **View Logs:** View logs from a pod into the Kubernetes Explorer Console.
  * **Get Terminal:** Get terminal for a pod in the Kubernetes Explorer Console.

Additionally, running pods have colored status marks next to their labels:

    * **Red** : Pod is in a failed state
    * **Yellow** : Pod is starting or terminating
    * **Green** : Pod is healthy and running

![Green check mark next to pod indicating healthy status](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-pod-status-green.png)

### Containers

  * **View logs:** View logs from a container into the Kubernetes Explorer console.
  * **Get Terminal:** Get terminal for a container in the Kubernetes Explorer console.



### Deployments

  * **View logs:** View logs from a deployment into the Kubernetes Explorer console.

Live deployments have colored status marks next to their labels and counts of current/total replicas:

    * **Yellow** : Deployment does not have minimum availability or have image problems.
    * **Green** : Deployment is healthy and had minimum availability.

![Green deployment icons indicating healthy status](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-deploy-status-green.png)

### Nodes

Nodes of your cluster have colored status marks next to their names:

  * **Yellow** : Node has a resource problem such as memory or disk availability.
  * **Green** : Node is healthy.



### Custom Resource Definitions (CRDs)

The Kubernetes Explorer lists all Custom Resource Definitions (CRDs) installed and available on your cluster:

![List of custom resource definitions in the Explorer](https://docs.cloud.google.com/static/code/docs/vscode/images/vscode-crd-list.png)

## What's next

  * [Get started with Cloud Code for Cloud Shell for Kubernetes](https://docs.cloud.google.com/code/docs/shell/get-started-k8s) by creating and deploying a Kubernetes application from a code sample.
  * Use [file sync and hot reloading](https://docs.cloud.google.com/code/docs/shell/speed-up-k8s-development#enable-skaffold-file-sync-and-hot-reloading) to speed up development.
  * [Debug your application in Cloud Code](https://docs.cloud.google.com/code/docs/shell/debug)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
