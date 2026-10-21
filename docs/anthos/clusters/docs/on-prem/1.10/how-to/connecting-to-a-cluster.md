---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/connecting-to-a-cluster/
title: Connecting to a cluster from the Google Cloud console \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:26:51.169359+00:00
---

# Connecting to a cluster from the Google Cloud console  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/connecting-to-a-cluster/

**Version 1.10**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.10 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/overview)



Send feedback 

#  Connecting to a cluster from the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.10 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/connecting-to-a-cluster)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/connecting-to-a-cluster)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



With Connect, you can use the Google Cloud console to manage your admin cluster and user clusters for Google Distributed Cloud.

## Cluster registration

When you create a cluster, you provide registration information in the `gkeConnect` section of the cluster configuration file. Google Distributed Cloud uses that information to register your cluster to a fleet—a unified way to view and manage multiple clusters and their workloads as part of GKE Enterprise. You can find out more about fleets and the functionality that they enable in the [Fleets guide](https://docs.cloud.google.com/anthos/multicluster-management/fleets).

Registered clusters are visible in your [fleet host project](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/how-to/multiple-gcp-projects#fleet_host_project) on the [GKE Enterprise Clusters page](https://console.cloud.google.com/anthos/clusters/) in the Google Cloud console.

As of version 1.9, user cluster registration is required at the time of creation. For user clusters that are upgraded to version 1.9 or later, registration is required during the upgrade.

To register a cluster after it has been created, fill in the `gkeConnect` section of its configuration file, and then run `gkectl update cluster` for a user cluster, or `gkectl update admin` for an admin cluster.

**Note:** Registering an admin cluster by updating it after creation is a preview feature.

Google Distributed Cloud does not support using `gcloud` to manually change the registration of a cluster.

## Logging into your cluster

To manage a registered Google Distributed Cloud cluster from the Google Cloud console, you need to log in to the cluster from the Google Cloud console.

Follow the instructions in [logging into clusters](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) to create the necessary roles and accounts and log in to your cluster.

## What's next

  * Learn about multi-cluster management with [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview).

  * Learn about cluster authentication with [OpenID Connect (OIDC)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.10/concepts/authentication).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
