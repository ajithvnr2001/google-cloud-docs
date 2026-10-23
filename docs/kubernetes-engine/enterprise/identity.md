---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/
title: About authentication using third-party identities \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:32.909146+00:00
---

# About authentication using third-party identities  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  About authentication using third-party identities Stay organized with collections  Save and categorize content based on your preferences. 

You can use existing third-party identity providers to authenticate to your Kubernetes clusters that are registered to a fleet. This document describes the supported authentication protocols and the types of clusters that support each protocol. Users can access and manage your clusters from the command line or from the Google Cloud console, without requiring you to change your identity provider.

If you prefer to use Google IDs to log in to your clusters instead of using an identity provider, see [Connect to registered clusters with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway).

## Supported identity providers

If you have a third-party identity provider, you can use the following protocols to authenticate to your clusters:

  * [OpenID Connect (OIDC)](https://openid.net/connect/): OIDC is a modern, lightweight authentication protocol built on top of the OAuth 2.0 authorization framework. We provide specific instructions for setup of some popular OpenID Connect providers, including Microsoft, but you can use any provider that implements OIDC.
  * [Security Assertion Markup Language (SAML)](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html): SAML is an XML-based standard for exchanging authentication and authorization data between parties, primarily between an identity provider (IdP) and a service provider (SP).
  * [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/): LDAP is a mature, standardized protocol for accessing and managing directory information services. It's commonly used to store and retrieve user information, such as usernames, passwords, and group memberships. You can authenticate by using LDAP with Active Directory or an LDAP server.



## Supported cluster types

This authentication service can be installed only on clusters that are [registered to a fleet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-fleets). Most cluster types are always registered to a fleet. For GKE clusters on Google Cloud, you must explicitly register the clusters to your fleet to use this service.

The following table describes the cluster types that support third-party authentication and the specific protocols that you can use for each type:

Supported cluster types and protocols  
---  
GDC (VMware) |  Supports the following protocols:

  * OIDC
  * LDAP (for user clusters)
  * SAML

  
GDC (bare metal) |  Supports the following protocols:

  * OIDC
  * LDAP
  * SAML

  
GKE on Google Cloud (fleet members only) | Supports OIDC  
GKE on AWS |  **Caution** : GKE on AWS is [deprecated](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17,2027.Supports OIDC  
GKE on Azure |  **Caution** : GKE on Azure is [deprecated](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17,2027.Supports OIDC  
  
The following configurations aren't supported:

  * [GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached): any EKS, AKS, or other Kubernetes installations aren't supported. To connect to these GKE attached clusters, use the [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway#why_use_the_connect_gateway).
  * For VMware deployments of Google Distributed Cloud, you can authenticate only to _user clusters_ by using the LDAP protocol. Admin clusters on VMware don't support authentication with LDAP.
  * GKE clusters on Google Cloud: your GKE clusters must be [registered to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke). To connect to GKE clusters that aren't in a fleet, use [Workforce Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc#use-workforce-id-federation).



## Setup process

Setting up authentication from third-party identity providers involves the following users and steps:

  1. **[Configure providers](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/idp-overview)** : The _platform administrator_ registers a client application with their identity provider. This client application has the protocol-specific configuration for Kubernetes. The platform administrator gets a _client ID_ and _secret_ from the identity provider.
  2. **Set up clusters** : The _cluster administrator_ sets up clusters for your identity service. Cluster administrators can set up clusters as follows:

     * **Fleet-level setup** : the cluster administrator configures all of the clusters that are registered to a specific fleet. Use this method to set up multiple clusters at once with a similar configuration. For more information, see [Set up fleet-level authentication](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster).
     * **Individual cluster setup** : the cluster administrator configures each cluster separately. Use this method for scenarios where different cluster types need different authentication configurations. For more information, see the following documents:

       * [Set up clusters for authentication using OIDC](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster)
       * [Set up clusters for authentication using SAML](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-per-cluster)
       * [Set up clusters for authentication using LDAP](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ldap)
  3. **[Set up user access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access)** : The _cluster administrator_ sets up user login access to authenticate to the clusters using the [FQDN access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#fqdn-access) (recommended) or [file-based access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#file-access) approach, and optionally configures _Kubernetes[role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/setup-rbac)_ for users on these clusters.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
