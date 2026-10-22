---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/overview/
title: About GDC Sandbox \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:09.931367+00:00
---

# About GDC Sandbox  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  About GDC Sandbox Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) Sandbox (GDC Sandbox) is a managed environment that lets you build and test services designed for Google Distributed Cloud (GDC) air-gapped in a Google Cloud environment, without navigating the air gap and physical hardware. With GDC Sandbox, you can train, perform, and test familiar Distributed Cloud operations using the GDC console user interface (UI), gdcloud CLI, and API services before investments in hardware and deployments. You can develop for the Google Distributed Cloud environment without the cost and logistics of working on air-gapped hardware, and without waiting for a data center installation.

![GDC Sandbox Console user interface showing landing page](https://docs.cloud.google.com/static/distributed-cloud/sandbox/latest/images/sandbox-console-ui.png)

With GDC Sandbox, you can:

  * **Develop applications** : Build and test apps without infrastructure overhead, from writing scripts to managing large-scale systems.
  * **Build methodologies** : Experiment with technologies or solutions in an isolated environment.
  * **Demonstrate capabilities** : Show your solution's capabilities by testing and training on familiar GDC Sandbox services.
  * **Train developers** : Provide self-paced or guided learning in a simulated GDC Sandbox environment.
  * **Manage development** : Create virtual environments automatically and avoid hardware purchases and maintenance.



## What is a Sandbox?

A GDC Sandbox instance is a non-persistent simulation of a Google Distributed Cloud environment. Instances are subject to being refreshed on a monthly basis. These refreshes give you access to the latest features of the GDC Sandbox and the underlying Google Distributed Cloud environment itself.

When instances are refreshed, they're returned to a default state, meaning all data is removed and you'll need to redeploy your configurations. It's recommended to save your configurations, code, and containers in a code repository. This practice is also a good fit for a low-high development model where you develop and test in GDC Sandbox and deploy to a secure environment. Configuration tasks such as project creation and user management can be scripted for repeatability.

## Technical features

The current release of GDC Sandbox includes the following features:

  * **Managed developer experience** emulating the Google Distributed Cloud air-gapped environment, supporting a web-based console UI and the `gdcloud` CLI
  * **Remote access** to a private instance from Linux, macOS, and Windows
  * **Flexible workload options** including virtual machines (VM) and containers
  * **Storage** including block storage, PostgreSQL, and AlloyDB



## Included resources

GDC Sandbox includes the following pre-configured resources:

  * An organization called **org-1**. An organization is the top-level resource in the Google Distributed Cloud air-gapped resource hierarchy.
  * An org infrastructure cluster called **org-1-admin**. For details on clusters, see [Cluster architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/clusters#cluster-architecture).
  * Two Kubernetes clusters called **user-vm-1** and **user-vm-2** for running container workloads.
  * A fake OIDC identity provider. This identity provider contains a default user account you adopt for operations such as assigning yourself required roles and permissions.
  * Four available personas. For your testing purposes, we recommend you follow the **Platform Admin** user.
  * The following default projects in the org-1 organization: 
    * e2e-test-user
    * user-project



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
