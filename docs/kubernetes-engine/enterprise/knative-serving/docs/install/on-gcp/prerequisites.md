---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/prerequisites/
title: Prerequisites for clusters on Google Cloud \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:31.322100+00:00
---

# Prerequisites for clusters on Google Cloud  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Prerequisites for clusters on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Before you install Knative serving in your cluster on Google Cloud, you must first ensure that you meet the following requirements:

  * Review and understand the [access permissions of components in Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/permissions).

  * You must ensure that you have adequate permissions in your Google Cloud project to meet the installation requirements for your cluster, fleet, and Cloud Service Mesh:

    * If you have the [_Owner_](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role for the Google Cloud project, then you have more than the necessary permissions to create clusters, install, and then configure Knative serving. 
    * Note that the [Cloud Service Mesh permissions requirements](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane#roles-required) also meet all the permission requirements for installing and configuring Knative serving.

    * Using other roles and the minimum requirements:

Depending on your organization, you can also meet the permission requirements through a combination of the following predefined roles:

      * Google Cloud project permissions: [Basic _Editor_ role](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

      * Fleet permissions: [_GKE Hub Admin_](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) or a role that includes the following permissions:

        * `gkehub.features.create`
        * `gkehub.features.update`
      * Cluster permissions: [A Kubernetes Engine Admin Role](https://docs.cloud.google.com/iam/docs/roles-permissions/container):

        * _Kubernetes Engine Admin_
        * _Kubernetes Engine Cluster Admin_
  * A cluster with the following configuration is required:

    * A supported [Google Kubernetes Engine cluster](https://docs.cloud.google.com/anthos/docs/setup/set-up-google-cloud). Note that GKE clusters that have Windows Server node pools are unsupported. 

    * Registered to a fleet:

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

**Tip:** Workload Identity Federation for GKE allows you to authenticate to Google Cloud services and it's also required by Cloud Service Mesh. Enabling fleet Workload Identity Federation in your cluster during fleet registration can reduce the configuration and deployment time.

To learn how to register your cluster and enable Workload Identity Federation for GKE in your fleet, see [Registering a cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke). Supported cluster types outside Google Cloud are registered by default.

    * In-cluster [Cloud Service Mesh is installed](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh). Additionally, note the following prerequisites:

      * The [Google-managed Cloud Service Mesh control plane](https://docs.cloud.google.com/service-mesh/docs/supported-features-mcp) is currently not fully supported by Knative serving. Use the in-cluster control plane instead.
      * Cloud Service Mesh requires that your cluster use a machine type with at least 4 vCPUs, such as `e2-standard-4`. See the Cloud Service Mesh installation guide for details about requirements. If you need to change your existing cluster's machine type, see [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).
      * In order to benefit from the automated provisioning of test domains - Cloud Service Mesh uses an ingress gateway and a service named `istio-ingress` in namespace `istio-system`. To enable creation of the gateway during the feature installation use `--option legacy-default-ingressgateway` of `asmcli` installation script.
  * [The command-line environment must be set up](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools).

  * The following APIs must be enabled in your Google Cloud project:

    * Kubernetes Engine API: Build and manage container-based applications.
    * Cloud Build API: Create and manage builds.
    * Container Registry API: Push and pull images in Container Registry.

[Enable the APIs in the Google Cloud console](https://console.cloud.google.com/start/api?id=container.googleapis.com,containerregistry.googleapis.com,cloudbuild.googleapis.com)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
