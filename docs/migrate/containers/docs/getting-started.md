---
url: https://docs.cloud.google.com/migrate/containers/docs/getting-started/
title: Migrate to Containers overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:04.002946+00:00
---

# Migrate to Containers overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to Containers overview

Use Migrate to Containers to modernize traditional applications away from virtual machine (VM) instances and into native containers that run on Google Kubernetes Engine (GKE) or Cloud Run platform. You can migrate workloads from VMs that run on VMware or Compute Engine, giving you the flexibility to containerize your existing workloads with ease. Migrate to Containers supports modernization of IBM WebSphere, JBoss, Apache, Tomcat, WordPress, Windows IIS applications, as well as containerisation of Linux-based applications.

The Migrate to Containers CLI is a lightweight tool that you can use on your local machine for migrating your workloads to modernize application components that run on VMs. It generates artifacts that you can deploy to GKE or Cloud Run. The offline mode lets you perform migrations of your Linux-based workloads locally and can work on your local network without pulling resources from the internet during runtime.

You can migrate applications from supported source platforms to the following:

  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs) and [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
  * [Cloud Run](https://docs.cloud.google.com/run/docs)



## About Migrate to Containers integration with Cloud Code

The Migrate to Containers integration with the Cloud Code gives you the ability to migrate applications from VMs to containers running on GKE, directly in Visual Studio, using a Linux machine.

  * The extension is integrated with the Migration Center discovery client CLI and Migrate to Containers CLI.
  * It provides a guided replatforming journey, technical fit assessment, and automated artifact generation, which let you run existing applications on GKE.



To learn more about the Migrate to Containers extension, see [Replatform Linux applications to containers](https://docs.cloud.google.com/code/docs/vscode/replatform-apps-to-containers).

## About GKE and GKE Enterprise clusters

Google Kubernetes Engine (GKE) clusters provide secured and managed Kubernetes services with autoscaling and multi-cluster support. GKE lets you deploy, manage, and scale containerized applications on Kubernetes, powered by Google Cloud.

  * [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview): this mode of operation in GKE provisions and manages the cluster's underlying infrastructure, including nodes and node pools, giving you an optimized cluster experience. For the benefits of using the simplified Linux service manager, see [Migrating to Autopilot clusters and Cloud Run](https://docs.cloud.google.com/migrate/containers/docs/autopilot-overview).



GKE Enterprise is an application management platform that provides a consistent development and operations experience for cloud and on-premises environments. GKE Enterprise includes a set of core components, including the following:

  * [GKE clusters](https://docs.cloud.google.com/anthos/clusters/docs): container orchestration and management service for running Kubernetes clusters in both cloud and on-premises environments. GKE Enterprise relies on GKE clusters on Google Cloud or Google Distributed Cloud to manage Kubernetes installations in the environments where you intend to deploy your applications.

  * [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview): continuously reconciles your clusters to a central set of configurations that are stored in a source of truth, like one or more Git repositories.

  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller): defines, automates, and enforces policies across environments to meet your organization's security and compliance requirements.

  * [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview): a hosted service to provision and orchestrate Google Cloud resources.

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs): manages and secures traffic between services while monitoring, troubleshooting, and improving application performance.

  * [GKE Enterprise security](https://docs.cloud.google.com/anthos/docs): secures your hybrid and multi-cloud deployments by providing consistent controls across your environments.




## About Cloud Run

Cloud Run is a managed compute platform that lets you run stateless containers using web requests or Pub/Sub events. The simplified Linux service manager lets you deploy your migrated container workloads on Cloud Run.

  * For the benefits of using the simplified Linux service manager, see [Migrating to Autopilot clusters and Cloud Run](https://docs.cloud.google.com/migrate/containers/docs/services-manager).



## What's next

  * Learn about the [benefits of migrating to containers](https://docs.cloud.google.com/migrate/containers/docs/anthos-migrate-benefits). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
