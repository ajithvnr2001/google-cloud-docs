---
url: https://docs.cloud.google.com/workstations/docs/overview/
title: Cloud Workstations overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:08.929185+00:00
---

# Cloud Workstations overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Cloud Workstations overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations provides managed development environments on Google Cloud with built-in security and preconfigured yet customizable development environments. Instead of requiring your developers to install software and run setup scripts, you can create a workstation configuration that specifies your environment in a reproducible way. Any updates to a workstation configuration automatically apply to workstations the next time they start. Developers access the workstations through a browser-based IDE, from multiple local code editors (such as VSCode or JetBrains IDEs such as IntelliJ IDEA Ultimate and PyCharm Professional), or through SSH.

Cloud Workstations uses the following Google Cloud resources to manage your development environments:

  * **Workstation clusters** define a group of workstations in a particular region and the VPC network they're attached to. Workstation clusters aren't related to [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) clusters.

  * **Workstation configurations** act as templates for workstations. The workstation configuration defines details such as the workstation virtual machine (VM) instance type, persistent storage, container image defining environment, which IDE or Code Editor to use, and more. Administrators and platform teams can also use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) rules to grant access to teams or to individual developers.

  * **Workstations** are preconfigured development environments that provide a cloud IDE, language tooling, libraries, and more. Workstations can be started or stopped on demand, and run on [Compute Engine](https://docs.cloud.google.com/compute/docs/instances) VMs in your project, with a persistent disk attached to store data between sessions.




Administrators and platform teams create _workstation configurations_ that they share with their development team. Each developer creates a _workstation_ based on a workstation configuration.

![Concepts](https://docs.cloud.google.com/static/workstations/images/overview-workstations-concepts.svg)Figure 1. Cloud Workstations Concepts

## Workstation lifecycle

Workstations run on ephemeral Compute Engine VMs, and can be started or stopped on demand to improve cost savings. Additionally, administrators and platform teams can configure an _idle timeout_ or _running timeout_ in the [workstation configuration](https://docs.cloud.google.com/workstations/docs/customize-development-environment#resource:-workstationconfig) to help make sure that workstations shut down when they are no longer used, which reduces costs. It also helps make sure that all workstations synchronize with the latest changes applied to their workstation configuration when each workstation restarts.

## Persistent storage

When a workstation stops, its ephemeral VM is deleted along with all workstation runtime data. Administrators and platform teams can optionally configure a persistent home directory on a workstation configuration, so all data saved to the home directory persists between sessions. This persistent storage is implemented as a [persistent disk](https://cloud.google.com/persistent-disk) that is attached to the workstation VM when the session starts, and detached when the session ends.

## Workstation DNS hostnames

Every workstation is given its own unique hostname. All workstations in a workstation cluster share a common, cluster-specific domain name, and the workstation cluster takes care of routing requests for this hostname to the running workstation. The workstation hostname can be used to connect to the workstation through your browser.

## Configuration updates

Updates to a workstation configuration automatically apply to workstations when each workstation restarts after the configuration update. For example, changing the machine type in a workstation configuration changes the machine type of the VMs used by the associated workstations the next time each workstation restarts. Administrators and platform teams can configure an _idle timeout_ or _running timeout_ in the [workstation configuration](https://docs.cloud.google.com/workstations/docs/customize-development-environment#resource:-workstationconfig) to help make sure that workstations synchronize with configuration updates within a bounded period of time.

## Gemini Code Assist

[Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/overview) is an AI-powered collaborator in Google Cloud. If you select the Cloud Workstations **Base Editor (Code OSS for Cloud Workstations)** when you [create your workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration#customize_environment), Gemini can help you with the following in the base editor:

  * Provide guidance to help you solve problems with your code.

  * Generate code for your project.

  * Receive inline suggestions while you're coding.




Gemini provides source citations when suggestions directly quote at length from a source to help you comply with any license requirements. For more information about using Gemini with Cloud Workstations, see [Code with Gemini Code Assist assistance](https://docs.cloud.google.com/workstations/docs/write-code-gemini).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Software supply chain security

Cloud Workstations is one of the Google Cloud components you can use to protect your software supply chain. You can use Cloud Workstations together with other Google Cloud products and features to improve the security posture of developer workflows and tools, software dependencies, CI/CD systems used to build and deploy your software, and runtime environments such as Google Kubernetes Engine and Cloud Run. To learn more, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
