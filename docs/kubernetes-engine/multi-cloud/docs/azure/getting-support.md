---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support/
title: Get support \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:52.329050+00:00
---

# Get support  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get support

This page shows you how to get support for GKE on Azure.

## Before contacting support

Before contacting support, you can try and resolve issues yourself. For tips on resolving common problems, see [Troubleshoot common issues](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/troubleshooting).

## Get a Google support package

Google Cloud offers different support packages to meet different needs, such as 24/7 coverage, phone support, and access to a technical support manager. For more information, see [Cloud Customer Care](https://docs.cloud.google.com/support).

## File bugs or feature requests

You can submit a product or documentation issue by using one of the following procedures:

  * **GKE on Azure issues and feature requests** : If you experience an issue with the product that you can't resolve, or you'd like to make a feature request, open a support case. The support team can then open a bug or feature request if required.
  * **Documentation issues** : From the GKE on Azure documentation, click **Send feedback > Documentation feedback**. This button opens a feedback form. The comments that you submit are reviewed by the GKE on Azure documentation team.



## Billing questions

Use the following resources to get help with billing questions:

  * To learn more about billing, read the [Google Cloud billing documentation](https://docs.cloud.google.com/billing/docs).
  * Resolve billing concerns by using the [billing concerns troubleshooter](https://support.google.com/cloud/troubleshooter/7279311?ref_topic=6288636).
  * Request help with billing questions by using the [billing support form](https://support.google.com/cloud/contact/cloud_platform_billing?visit_id=1-636564925221770723-4170709031&rd=1).



## Version Support Policy

Google supports each GKE on Azure minor version for the later of:

  * 12 months after the initial release of the minor version.
  * The release of the third subsequent minor version.



For the list of the Kubernetes versions that GKE on Azure supports, see [Kubernetes version notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions).

## Shared responsibility model

Running a business-critical production application on GKE on Azure requires multiple parties to carry different responsponsibilities. Although they aren't an exhaustive list, the following sections list the roles and responsibilities of different parties.

### Google's responsibilities

  * Maintain and distribute the GKE on Azure software package including Kubernetes, base images, Azure integrations, the Ingress controller, the Connect agent, and the Google Cloud CLI.

  * Continually scan components with the [Artifact Analysis API](https://docs.cloud.google.com/container-registry/docs/container-analysis) and patch known vulnerabilities.

  * Maintain and distribute the management service, control plane, and node pool machine images, including regular patching and security fixes.

  * Notify users of available upgrades for GKE on Azure, and produce upgrade instructions for the previous version. GKE on Azure supports sequential upgrades only (1.2 → 1.3 → 1.4 only and not 1.2 → 1.4).

  * Provide Google Cloud integrations for Connect and Google Cloud Observability.

  * Troubleshoot, provide workarounds, and correct the root cause of any issues related to Google-provided components.




### Customer's responsibilities

  * Provide overall system administration for GKE on Azure clusters. For example, configuring them to work within the corporate VPC environment.

  * Maintain your workloads, including your application code, build files, container images, data, RBAC/IAM allow policy, and containers and pods that you are running.

  * Operate and maintain the Azure environment, including networking configuration, and connectivity to Google Cloud.

  * Maintain support contracts with Azure.

  * Upgrade GKE on Azure to a supported version on a regular basis. For the list of the Kubernetes versions that GKE on Azure supports, see [Kubernetes version notes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-versions).

  * Monitor clusters and applications and respond to any incidents.

  * Ensure Logging and Monitoring agents are deployed to clusters. _Without logs, support is available on a best-effort basis_.

  * Provide Google with environmental details (for example, Azure VNet configuration) when requested for troubleshooting purposes.




## What's next

  * Review the [compatibility between GKE components and cluster product families](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support#gke_multi_cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
