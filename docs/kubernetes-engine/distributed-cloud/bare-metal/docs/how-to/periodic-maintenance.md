---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/periodic-maintenance/
title: Required periodic maintenance \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:24.979134+00:00
---

# Required periodic maintenance  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/periodic-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Required periodic maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes periodic maintenance that is required for your Google Distributed Cloud clusters.

## Rotate certificate authorities

The certificate authorities (CAs) in a cluster are valid for ten years. For versions before 1.36.100, the core cluster component `clientconfig-operator`, uses a certificate that is valid for five years and is only renewed when you rotate the cluster CA. To prevent this certificate from expiring, you must [rotate your CAs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation) at least once every five years, even if you don't actively use external identity providers or GKE Identity Service.

## Certificates for cluster components

Cluster components use certificates for authentication:

  * **Control plane and node components** : Certificates for components including `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `etcd`, and `kubelet` are valid for one year and are renewed during cluster [upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade). To prevent these certificates from expiring, you must upgrade your cluster at least once a year.

  * **GKE Identity Service (`clientconfig-operator`)**: The certificate for the `clientconfig-operator` component is valid for ten years and is renewed when you [rotate certificate authorities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation).




If the cluster certificates have expired, they must be [renewed manually](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/expired-certs). For more information, see [Certificate expiration](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/failure-mode-analysis#certificate_expiration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
