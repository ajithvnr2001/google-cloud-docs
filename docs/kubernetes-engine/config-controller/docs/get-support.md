---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/get-support/
title: Get support \u00a0|\u00a0 Config Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:45.130451+00:00
---

# Get support  |  Config Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/get-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/resources)



Send feedback 

#  Get support Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to get support for Config Controller.

## Before contacting support

Before contacting support, you can try to resolve issues yourself. For troubleshooting tips, see [Troubleshoot Config Controller](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot) and [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

## Support options

Google Cloud offers a variety of support packages to accommodate your support needs.

Google manages the lifecycle of the cluster that backs your Config Controller instance including upgrading the cluster and installing the latest version of Google-managed operators.

For open source Config Connector, you can get support by checking for existing issues or opening a new issue in the [public GitHub issue tracker](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues).

### What Google doesn't support

Google doesn't support issues with customer-owned `YAML` file configurations.

### Unsupported changes to Config Controller instances

Because Config Controller is a managed offering, you shouldn't make changes to the Google Kubernetes Engine (GKE) cluster that backs your Config Controller instance. To ensure you can receive [Google Cloud Support](https://docs.cloud.google.com/support/docs) services, you should avoid the following:

  * Deleting a Config Controller instance with the GKE API or associated gcloud CLI. If you want to delete a Config Controller instance, you should use [`gcloud anthos config controller delete`](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/config/controller/delete).
  * Registering a Config Controller instance to a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs) or enabling any fleet features.
  * Changing the cluster settings of the Config Controller instance, for example `projects.locations.clusters.update`.
  * Creating or deleting the nodepool of a Config Controller instance, for example `projects.locations.clusters.nodePools.delete`.



Don't edit, update, or delete the following namespaces and resources contained within those namespaces:

  * `cnrm-system`
  * `config-management-monitoring`
  * `config-management-system` (you can edit, update, or delete `rootsync` and `secret` resources)
  * `configconnector-operator-system`
  * `gatekeeper-system`
  * `krmapihosting-monitoring`
  * `krmapihosting-system`
  * `kube-node-lease`
  * `kube-system`
  * `resource-group-system`



Don't edit, update, or delete the following cluster-scoped APIs:

  * `MutatingWebhookConfigurations`
  * `ValidatingWebhookConfigurations`



Don't edit, update, or delete the following [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) used by API groups:

  * `*.cloud.google.com`
  * `gatekeeper.sh`
  * `gke.io`



Don't delete the following Objects:

  * Kind: `ConfigConnector` (Cluster Scoped), Name: `configconnector.core.cnrm.cloud.google.com`



## File bugs or feature requests

You can submit a product issue by using one of the following procedures:

  * **Config Controller issues and feature requests** : Check for [existing issues](https://issuetracker.google.com/issues?q=componentid:1161547%2B%20status:open%20&s=vote_count:desc&d=issue_id&d=type&d=status&d=vote_count&d=title&d=priority&d=severity&d=assignee&d=blocked_by_issue_id&d=created_time&d=modified_time) or [open new issues](https://issuetracker.google.com/issues/new?component=1161547).

  * **Config Connector issues and feature requests** : Check for existing issues or open new issues in the [public issue trackers](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues).

  * **Documentation issues** : On the documentation page, select **Send feedback**. This action opens a feedback form. The Config Management team reviews and takes action on your comments.




## Billing questions

Use the following resources to get help with billing questions:

  * To learn more about billing, read the [Google Cloud billing documentation](https://docs.cloud.google.com/billing/docs).
  * Resolve billing concerns by using the [billing concerns troubleshooter](https://support.google.com/cloud/troubleshooter/7279311?ref_topic=6288636).
  * Request help with billing questions by using the [billing support form](https://support.google.com/cloud/contact/cloud_platform_billing?visit_id=1-636564925221770723-4170709031&rd=1).



## What's next

  * For support details for products related to Config Controller, see the following support pages: 
    * [Get support for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync)
    * [Get support for Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/get-support-policy-controller)
  * To review the compatibility between Google Kubernetes Engine features and cluster product families, see [Version and upgrade support](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
