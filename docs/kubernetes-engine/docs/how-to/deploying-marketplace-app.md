---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-marketplace-app/
title: Deploying an application from Cloud Marketplace \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:53:15.722174+00:00
---

# Deploying an application from Cloud Marketplace  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-marketplace-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deploying an application from Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can select and deploy container-based applications from Google Cloud Marketplace to your Google Kubernetes Engine cluster.

To see the applications that you can install, in the Google Cloud console, open the GKE Applications page, and click **Deploy from Cloud Marketplace**.

[Go to the Applications page](https://console.cloud.google.com/kubernetes/application)

To deploy an application to your cluster, follow these steps:

**Note:** Marketplace applications that require elevated privileges generate `ClusterRole` and `ClusterRoleBinding` resources upon deployment. When you use Google Cloud console to deploy or delete an application that requires elevated privileges, these resources are automatically removed. However, if you use the command line to deploy or delete an application that requires elevated privileges, you must manually delete the `ClusterRole` and `ClusterRoleBinding` resources. For instructions, see the command-line instructions that follow.

You must have the `Kubernetes Engine Admin` and `Project Viewer`, or `Project Owner` role to deploy an app to a GKE cluster.

To deploy a Kubernetes app from GKE, your project must have a network called `default`. [Learn about creating networks with Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).

###  Console 

  1. To see information about an app, including its pricing, select the app.
  2. Click **Configure**.
  3. Select the Kubernetes cluster that you want to deploy the app to. If you want to create a new cluster, click **Create cluster**.

**Note:** If a cluster is marked ineligible, verify that you have permissions to deploy workloads to that cluster.
  4. Select or create a Namespace to use for the application. [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) are a way to divide cluster resources among multiple users or teams.

**Note:** Namespaces with the `-system` suffix are reserved for GKE components. You cannot deploy applications to these namespaces.
  5. In the **App instance name** box, enter a name for the app, such as `sandbox-dev-app`. The name must be unique within the namespace.

  6. If you need to change the service account associated with the application's billing plan, expand **Advanced plan settings** , and verify the service account that is associated with the application.

For information on billing plans for Kubernetes apps, see [Understanding Billing](https://docs.cloud.google.com/marketplace/docs/understanding-billing).

  7. Enter a name for your app instance, and then click **Deploy**.

  8. To manage, edit, or delete your deployment, open the GKE Applications page.

[Go to the Applications Page](https://console.cloud.google.com/kubernetes/application)

For information on what you can customize in the app, see the documentation provided by the software vendor.

  9. If the application needs to be accessible to external traffic, follow [these steps to expose the application as a Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).




###  Command Line 

You can deploy a Kubernetes app to a Google Kubernetes Engine cluster, or to your own infrastructure, such as a local installation of [Minikube](https://kubernetes.io/docs/setup/minikube/).

To deploy the app from the command line, you download a license file from Google Cloud. When you deploy the app using the steps below, you must apply the license file to your `kubectl` config or Helm chart.

Depending on the app provider, the specific steps to deploy the app might be different. At a high level, you do the following:

  1. Connect to your Kubernetes cluster.
  2. Add the license file to your `kubectl` configuration or Helm chart, as applicable.
  3. Clone the Git repository for the app. The repository typically contains:

     * A `kubectl` configuration or Helm chart, which describes the Kubernetes resources for the app.

If you want to customize the app, such as increasing the number of replicas, or changing the update strategy for application pods, edit the `kubectl` configuration or Helm chart.

     * An [Application resource](https://github.com/kubernetes-sigs/application), which defines the application's properties, such as the type of application, the version, maintainers, and so on.

     * Specific steps to deploy the application to your Kubernetes cluster.

     * Additional scripts or tools added by the provider.

  4. Verify the app's configuration and deploy the app.

  5. Following deployment, check for `ClusterRole` or `ClusterRoleBinding` resources labeled `app.kubernetes.io/component=deployer-rbac.marketplace.cloud.google.com`. If you find them, delete them.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
