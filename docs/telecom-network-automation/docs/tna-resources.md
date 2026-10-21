---
url: https://docs.cloud.google.com/telecom-network-automation/docs/tna-resources/
title: Resources \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:36.881317+00:00
---

# Resources  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/tna-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Resources Stay organized with collections  Save and categorize content based on your preferences. 

This section describes the Telecom Network Automation resources.

## Orchestration cluster

An Orchestration cluster is a GKE-based control plane cluster that governs workloads deployed through Telecom Network Automation. An Orchestration cluster uses [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) as the foundation.

## Blueprints

A blueprint (BP) is a collection of Kubernetes resources in the form of YAML files that contain the configurations required to automate the deployment of the required infrastructure.

Telecom Network Automation provides a Blueprint Library, which contains key blueprints. This Blueprint Library is also known as the _Public Catalog_. This guide uses the terms Blueprint Library and Public Catalog interchangeably. Blueprints in the Public Catalog are referred to as *Public Blueprints.

You can import any Public Blueprint into your Telecom Network Automation project and customize them according to your business needs. These Blueprints are referred to as the _private catalog_.

The lifecycle of a Blueprint is as follows:

  * When imported, the blueprint starts in the **DRAFT** state after creation. All edits are made to the blueprint in **DRAFT** state.

  * When the edits are ready for review, you can propose the blueprint and update the state to **PROPOSED**. You can't edit a blueprint in the **PROPOSED** state.

  * After you approve a proposed blueprint, the blueprint updates to the **APPROVED** state. A new revision is committed.

  * You can use the latest committed revision to create a deployment on the Orchestration or Workload cluster.

  * Edits to an **APPROVED** blueprint returns the state to **DRAFT**. The last committed revision of a blueprint represents the latest **APPROVED** state.


**Note:** A Blueprint Designer is responsible for making the appropriate changes to a public blueprint.

The deployment level of a blueprint specifies where to apply the blueprint. The following list describes the available blueprint levels:

  * **Hydration** : You cannot use blueprints at the hydration level to create a deployment. You cannot manually initiate deployment of these blueprints on orchestration or workload clusters. These blueprints stay in your private catalog that the Telecom Network Automation automation configures and deploys.

  * **Single-deployment** : You can modify blueprints at the single-deployment level in your private catalog and use them to create a deployment on an Orchestration cluster by the user with approval.

  * **Multi-deployment** : You can modify blueprints at the multi-deployment level in your private catalog and use them to create a deployment on an Orchestration cluster, which creates further hydration-level deployments.




## Deployments

A deployment is an actuated blueprint that you apply on an Orchestration cluster or a Workload cluster. A deployment begins in the **DRAFT** state. All edits are made in this state. A deployment opened for editing after applying is in **DRAFT** state, while the previous revision is the current applied version.

An **APPLIED** state represents the contents of the deployment applied to an Orchestration or Workload cluster. A revision is created when a deployment is **APPLIED**. This revision represents the latest view of **APPLIED** on the cluster until you modify and apply the deployment, which creates a new revision.

A deployment in the **DELETING** state is marked for deletion. You can query the deletion through the `ComputeDeploymentStatus` API. No updates are allowed to a deployment in the **DELETING** state.

The Deployment Admin works with the deployments and is responsible for making the appropriate changes. In contrast to Blueprints, Deployments only have a few select editable files and fields the user edits according to specification.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
