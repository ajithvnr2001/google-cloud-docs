---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/security-overview/
title: Security overview \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:30.122830+00:00
---

# Security overview  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/security-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Security overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an introduction to establishing good security practices for Google Distributed Cloud. The guidance on this page is not intended to provide you with a comprehensive list of best practices.

Using good practices for security on Google Distributed Cloud involves applying concepts from Kubernetes and Google Kubernetes Engine (GKE), as well as concepts that are unique to Google Distributed Cloud.

## Kubernetes security

We recommend that you follow general Kubernetes guidelines for security when you're using Google Distributed Cloud.

For an introduction to Kubernetes security guidelines, see the [Security Checklist](https://kubernetes.io/docs/concepts/security/security-checklist/) and [Overview of Cloud Native Security](https://kubernetes.io/docs/concepts/security/overview/) in the Kubernetes documentation.

## GKE security

Google Distributed Cloud extends GKE to let you create GKE clusters on your own Linux servers on your own premises. To learn more about GKE security, see the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview). As you're reading, keep in mind that because your control plane and nodes run on-premises, the suggestions for [control plane security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#control_plane_security) and [node security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#node_security) don't apply.

## Google Distributed Cloud security

The following sections provide guidance for establishing good security practices for Google Distributed Cloud.

### Hardware security

  * Secure your on-premises data centers with industry standard physical security and safety features.

  * Ensure that access to your [admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites) is highly restricted. The admin workstation stores sensitive data such as `kubeconfig` files, SSH keys, and service account keys.




### Node security

  * Keep your operating system up-to-date by updating software packages and installing security patches.

  * For added control over workload image pulls and related security benefits, you can [configure worker nodes to authenticate to a private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-node-private-reg). Private registry support for nodes is available for [Preview](https://cloud.google.com/products/#product-launch-stages) for version 1.29 clusters.

  * By default, Google Distributed Cloud adds the Docker `apt` repository and the needed GPG key to your cluster nodes. As an alternative to adding adding package repositories to each cluster node in your deployment, you can configure your cluster to [use a private package repository](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/package-server) for container images.




### Cluster security

  * [Harden the security of your Google Distributed Cloud clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/hardening-your-cluster).

  * Isolate your traffic and data by using an [admin and user cluster deployment](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep#admin_user_model). This deployment type helps you to achieve the following types of isolation:

    * Workload traffic is isolated from administrative, or management plane traffic.
    * Cluster access is isolated by group or role.
    * Production workloads are isolated from development workloads.
  * [Upgrade your clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade-best-practices) to a [supported version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#version-support). Using a supported version provides you with the following security benefits:

    * Fixes for security vulnerabilities.
    * New features and functions that take advantage of latest security posture and technologies.
    * Updates for bundled software and components.
  * For reduced external exposure and other security benefits, you can [configure a registry mirror](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror) to install Google Distributed Cloud components from a local copy of the public registry.

  * The etcd cluster for Distributed Cloud software only encrypts secrets within etcd using `EncryptionConfiguration` with AES-CBC. You cannot modify this configuration. Values are encrypted with static encryption and Distributed Cloud software only uses mTLS to encrypt communication between etcd and the API server and among etcd peers. For more information about etcd and encryption, see [Encrypting confidential data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/).




### Workload security

  * [Secure your containers using Security-Enhanced Linux (SELinux)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux).

  * [Secure your workloads with Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem). Binary Authorization is a service on Google Cloud that provides software supply-chain security for applications that run in the cloud. With Binary Authorization, you can ensure that internal processes that safeguard the quality and integrity of your software have successfully completed before an application is deployed to your production environment.

  * Use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to give Pods access to Google Cloud resources. Workload Identity Federation for GKE allows a Kubernetes service account to run as an IAM service account. Pods that run as the Kubernetes service account have the permissions of the IAM service account.

  * [Follow the best practices for GKE RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/rbac).




### Network security

  * [Choose a secure connection between your Google Distributed Cloud and Google Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/connect-on-prem-gcp#enhancing_your_fundamental_connection). After your fundamental connection is in place, add features that enhance the security of your connection.

  * Limit the exposure of your clusters to the public internet by [installing them behind a proxy and creating firewall rules](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/proxy). Also use the appropriate controls in your network environment to limit public access to the cluster.




### Authentication security

  * [Manage identity with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/identity-manage). GKE Identity Service is an authentication service that lets you bring your existing identity solutions for authentication to multiple Google Cloud environments. You can sign in to and use your Google Distributed Cloud clusters from the command line (all providers) or from the Google Cloud console (OIDC only), all using your existing identity provider.

  * [Connect to registered clusters with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway). The Connect gateway builds on the power of fleets to let users connect to and run commands against registered clusters in a consistent and secure way.




### Credential security

  * [Rotate certificate authorities](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation). Google Distributed Cloud uses certificates and private keys to authenticate and encrypt connections between system components in clusters. To maintain secure cluster communication, rotate your user cluster certificate authorities periodically and whenever there is a possible security breach.

  * [Rotate service account keys](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-secrets). To reduce the security risk caused by leaked keys, we recommend that you regularly rotate your service keys.




### Monitor your security

  * [Use Kubernetes audit logging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/audit-logging). Audit logging provides a way for administrators to retain, query, process, and alert on events that occur in your Google Distributed Cloud environments.



For more information about monitoring cluster security, see [Monitor fleet security posture](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure#monitor-fleets-scale).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
