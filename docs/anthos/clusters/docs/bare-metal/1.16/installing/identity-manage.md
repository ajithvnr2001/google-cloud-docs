---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/identity-manage/
title: Manage identity with GKE Identity Service \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:50.748602+00:00
---

# Manage identity with GKE Identity Service  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/identity-manage/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Manage identity with GKE Identity Service Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/identity-manage)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/identity-manage)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Google Distributed Cloud supports [OpenID Connect (OIDC)](https://openid.net/connect/) and [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/) as authentication mechanisms for interacting with a cluster's Kubernetes API server, using GKE Identity Service. GKE Identity Service is an authentication service that lets you bring your existing identity solutions for authentication to multiple GKE Enterprise environments. Users can log in to and use your GKE clusters from the command line (all providers) or from the Google Cloud console (OIDC only), all using your existing identity provider.

GKE Identity Service works with any kind of bare metal cluster: admin, user, hybrid, or standalone. You can use both on-premises and publicly reachable identity providers. For example, if your enterprise runs an [Active Directory Federation Services (ADFS)](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) server, the ADFS server could serve as your OpenID provider. You might also use publicly-reachable identity provider services such as Okta. Identity provider certificates may be issued by either a well-known public certificate authority (CA), or by a private CA.

For an overview of how GKE Identity Service works, see [Introducing GKE Identity Service](https://docs.cloud.google.com/anthos/identity).

If you already use or want to use Google IDs to sign in to your GKE clusters instead of an OIDC or LDAP provider, we recommend using the Connect gateway for authentication. Find out more in [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

## Before you begin

  * Note that headless systems are unsupported. A browser-based authentication flow is used to prompt users for consent and authorize their user account.

  * To authenticate through the Google Cloud console, each cluster that you want to configure must be [registered with your project fleet](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).




## Setup process and options

GKE Identity Service supports identity providers using the following protocols:

  * [OpenID Connect (OIDC)](https://openid.net/connect/). We provide specific instructions for setup for some popular OpenID providers, including Microsoft, but you can use any provider that implements OIDC.

  * [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/). You can use GKE Identity Service to authenticate using LDAP with Active Directory or an LDAP server.




### OIDC

  1. Register GKE Identity Service as a client with your OIDC provider following the instructions in [Configuring providers for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/provider).

  2. Choose from the following cluster configuration options:

     * Configure your clusters at fleet level following the instructions in [Configuring clusters for fleet-level GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/fleet-cluster) (preview, Distributed Cloud version 1.8 and higher). With this option, your authentication configuration is centrally managed by Google Cloud.

     * Configure your clusters individually following the instructions in [Configuring clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster). Because fleet-level setup is a preview feature, you may want to use this option in production environments, if you are using an earlier version of Google Distributed Cloud, or if you require GKE Identity Service features that aren't yet supported with fleet-level lifecycle management.

  3. Set up user access to your clusters, including role-based access control (RBAC), following the instructions in [Setting up user access for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/user-access).




### LDAP

  * Follow the instructions in [Set up GKE Identity Service with LDAP](https://docs.cloud.google.com/anthos/identity/setup/ldap).



## Access clusters

After GKE Identity Service has been set up, users can sign in to configured clusters using either the command line or the Google Cloud console.

  * Learn how to sign in to registered clusters with your OIDC or LDAP ID in [Accessing clusters using GKE Identity Service](https://docs.cloud.google.com/anthos/identity/accessing).

  * Learn how to sign in to clusters from the Google Cloud console in [Work with clusters from the Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) (OIDC only).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
