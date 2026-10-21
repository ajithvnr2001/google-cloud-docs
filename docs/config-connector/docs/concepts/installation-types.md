---
url: https://docs.cloud.google.com/config-connector/docs/concepts/installation-types/
title: Choosing an installation type \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:46:18.121996+00:00
---

# Choosing an installation type  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/installation-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Choosing an installation type

The page provides you with an overview of the different installations options you can use when installing Config Connector.

You can install Config Connector in one of three ways:

  * **[Manual installation](https://docs.cloud.google.com/config-connector/docs/how-to/install-manually)** (Recommended): Manually installing with the [Kubernetes operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) gives you the most flexibility. You can install Config Connector in **namespaced mode** (recommended for most use cases) or **cluster mode**. Manual installation lets you control the exact version of Config Connector you install and when you upgrade.

  * **[Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)** : Config Controller is a hosted service that includes Config Connector. The Config Connector version in Config Controller is managed by Google and automatically updated regularly as versions qualify. Config Controller is a centralized and designated control plane which provides a more secure way to manage Google Cloud resources. For more information, see [Quickstart: Manage resources with Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/manage-resources) or [Set up Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/setup).

  * **[GKE Config Connector add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall)** : The Config Connector add-on lets you install Config Connector during cluster creation. The Config Connector add-on is available on only GKE Standard clusters, and not [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#add-ons). The version of Config Connector installed through the Config Connector add-on is often behind by up to 12 months or more. For more information, see [Config Connector add-on upgrades](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#how-gcp-upgrades-add-on).




There are many factors to consider when selecting an installation method. The following table outlines some high-level considerations:

Installation methods | Advantages | Disadvantages  
---|---|---  
Manual installation  |  • Allows more customization, such as installing in either namespaced mode (recommended) or cluster mode.  
• Flexible version update schedule.   
• Can run with any custom workload in the same cluster. |  • Operational cost.   
Config Controller  |  • No installation required.   
• Automatic version upgrades.   
• Includes [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).   
• Managed and supported by Google Cloud.  |  • Restriction on custom workloads.   
• Managed by Google and may not be the absolute latest version available compared to manual installation.   
GKE Config Connector add-on |  |  • Significant lag behind the latest Config Connector version.   
  
## Authentication

If you want to install Config Connector on GKE clusters, use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). Workload Identity Federation for GKE lets you configure a Kubernetes ServiceAccount to impersonate Identity and Access Management (IAM) service accounts to access Google Cloud services. Config Connector uses that Kubernetes ServiceAccount within your cluster to create new resources. Config Connector can only create resources with the roles that you grant the IAM service account.

If you want to install Config Connector on other [deployment options](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options), such as on-premises or multi-cloud options, use [Cloud Identity](https://docs.cloud.google.com/identity/docs/overview) to create an account and then use IAM to [create a service account key and import the key's credentials as a Secret to your clusters](https://docs.cloud.google.com/iam/docs/keys-create-delete).

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

## Managing resources with service accounts

When installing Config Connector manually, you can choose between a single, cluster-wide service account (**cluster mode**) or multiple service accounts, one for each namespace (**namespaced mode**). Namespaced mode is the recommended approach for most use cases, as it provides better permission isolation. For more information about using IAM service accounts with Config Connector, see [Access control with IAM](https://docs.cloud.google.com/config-connector/docs/how-to/configure-iam-permissions).

## What's next

  * Learn how to [manage Google Cloud resources with Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/manage-resources).
  * Learn how to [manually install Config Connector](https://docs.cloud.google.com/config-connector/docs/how-to/install-manually).
  * Learn how to [install Config Connector as a GKE add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
