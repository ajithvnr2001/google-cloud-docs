---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/component-rbac/
title: RBAC permissions for system components \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:51.044924+00:00
---

# RBAC permissions for system components  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/component-rbac/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  RBAC permissions for system components Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/reference/component-rbac)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/component-rbac)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Google Distributed Cloud deploys Pods to your nodes that have elevated [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) permissions such as the ability to modify all Deployments and to read all cluster Secrets. These permissions are required for Google Distributed Cloud to function correctly.

The following table lists all Google Distributed Cloud components with elevated permissions:

**Note:** Select features like VM Runtime on GDC or multi-NIC for pods require some of these system components. These features are disabled by default and the related components aren't active unless the feature is enabled.

  * `ais`
  * `anet-operator`
  * `anthos-cluster-operator`
  * `anthos-multinet-controller`
  * `cap-controller-manager`
  * `capi-controller-manager`
  * `capi-kubeadm-bootstrap-controller-manager`
  * `cdi-operator`
  * `cert-manager-cainjector`
  * `cert-manager-webhook`
  * `cert-manager`
  * `cluster-metrics-webhook`
  * `csi-snapshot-controller`
  * `istio-ingress`
  * `istiod`
  * `kube-state-metrics`
  * `localpv`
  * `metallb-controller`
  * `metrics-server-operator`
  * `metrics-server`
  * `network-controller-manager`
  * `sp-anthos-static-provisioner`
  * `stackdriver-operator`
  * `virt-api`
  * `virt-controller`
  * `virt-handler`
  * `virt-operator`
  * `vm-controller-controller-manager`
  * `vmruntime-controller-manager`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
