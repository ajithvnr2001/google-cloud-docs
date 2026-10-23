---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/
title: Knative serving fleet installation overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:32.997159+00:00
---

# Knative serving fleet installation overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Knative serving fleet installation overview Stay organized with collections  Save and categorize content based on your preferences. 

Knative serving is supported on GKE Enterprise through [fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets) and in-cluster [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview). To learn more about Knative serving, see the [architectural overview](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview).

## New installations

Choose the installation method that matches the location of your GKE cluster:

On Google Cloud
    For the Google Kubernetes Engine clusters in your fleet that are running on Google Cloud. [See the on Google Cloud install prerequisites](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/prerequisites).
Outside Google Cloud
    For the GKE clusters in your fleet that are hosted and running outside Google Cloud. [See the outside Google Cloud install prerequisites](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/prerequisites).

## Upgrading "free trial" installations

Previous "free trial" installations of Knative serving were enabled in clusters as a "_GKE add-on_ ". Beginning with Anthos version 1.8, Knative serving must be installed as a fleet component with Cloud Service Mesh.

To migrate your existing Knative serving installation to use a fleet and Cloud Service Mesh, choose the corresponding guide for your cluster:

  * [Upgrading GKE on Google Cloud to fleets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/upgrade)
  * [Upgrading Knative serving on VMware to fleets](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/upgrade-vmware)



### Migrate off Knative serving

If GKE Enterprise does not meet your needs, you can migrate your existing Knative serving workloads to run on other products. [Learn how to migrate your workloads](https://docs.cloud.google.com/anthos/run/docs/migrate).

### What's new in Knative serving fleet installations

The changes to the installation of Knative serving provide the following:

  * [Fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets) enable you to manage and upgrade your Knative serving installation independently of the other enterprise components.

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) is another component of your fleet, which now decouples Knative serving from your service mesh administration and maintenance tasks. Use of Cloud Service Mesh brings your installation to parity with the rest of GKE Enterprise and also removes the dependencies and those limitations of the previously bundled Istio version.

  * Fleet-wide access and administration across your clusters:

    * Full integration with [fleet components](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-enabled-components). Like Cloud Service Mesh, your Knative serving installation gains support within and across your GKE Enterprise environment.

    * You can use Terraform to manage your configurations, for example [Setup Anthos on Google Cloud](https://docs.cloud.google.com/anthos/docs/setup/set-up-google-cloud#registering_clusters_to_the_fleet).

  * Your Knative serving installation is always up-to-date. The `appdevexperience-operator` [operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) that runs in your cluster automatically rolls out the latest version of Knative serving as [new pods are created](https://kubernetes.io/docs/concepts/workloads/pods/#pod-update-and-replacement).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
