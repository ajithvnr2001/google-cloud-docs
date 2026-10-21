---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/periodic-maintenance/
title: Required periodic maintenance \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:33.102505+00:00
---

# Required periodic maintenance  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/periodic-maintenance/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Required periodic maintenance Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/periodic-maintenance)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/periodic-maintenance)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This document describes periodic maintenance that is required for your Google Distributed Cloud clusters.

## Rotate certificate authorities

The certificate authorities (CAs) in a cluster are valid for five years, so you must [rotate your CAs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/ca-rotation) at least once every five years.

## Certificates for cluster components

Cluster components use certificates for authentication. These components include `kube-apiserver`, `kube-controller-manager`, `kube-scheduler`, `etcd` and `kubelet`. The certificates are valid for one year and are renewed during cluster [upgrade](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade). To prevent the certificates from expiring, you must upgrade your cluster at least once a year.

If the cluster certificates have expired, they must be [renewed manually](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/expired-certs). For more information, see [Certificate expiration](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/failure-mode-analysis#certificate_expiration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
