---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview/
title: Config Controller overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:36.057303+00:00
---

# Config Controller overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Config Controller overview Stay organized with collections  Save and categorize content based on your preferences. 

This page explains what Config Controller is and how it relates to Config Connector, Config Sync and Policy Controller.

Config Controller creates and manages Google Cloud resources with a declarative, Kubernetes model. Config Controller is a hosted version of Config Connector that simplifies installation and maintenance. Config Controller also includes Policy Controller and Config Sync.

With Config Controller, you can create configurations for any Google Cloud resource. The configurations for these resources are stored in a source of truth like a Git repository. Config Sync continuously monitors your resources to ensure the current states of resources matches the state that you define in your source of truth. Policy Controller can catch and enforce policy violations on those resources before they are deployed. This flow is illustrated in the following diagram:

![Config Controller resource management flow](https://docs.cloud.google.com/static/kubernetes-engine/config-controller/images/config-controller-architecture.svg)

Config Controller's declarative configuration approach gives you many benefits:

  * **Manage with Kubernetes** : Use familiar Kubernetes tools and workflows to manage Google Cloud resources and [custom workloads](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/deploy-workloads).
  * **Declare desired state** : Focus on what your resources look like rather than the specifics of how you create them.
  * **Automate drift detection and repair** : Continuously monitor your infrastructure for drift from the defined state and enable automatic repairs.
  * **Use GitOps for consistency** : Collaborate with your colleagues on potential changes and preview changes before they are made.
  * **Enforce policy guardrails** : Enforce policies earlier in the development cycle and detect violations before deploying resources.
  * **Audit infrastructure continuously** : Maintain an audit trail of all changes to help understand the history of your infrastructure.
  * **Increase developer velocity** : Improve the safety and velocity of your cloud adoption journey by using best practices.



For a guided example showing you how to install and use a Config Controller instance, see [Manage resources with Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/manage-resources). For the full installation instructions, see [Set up Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/setup).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
