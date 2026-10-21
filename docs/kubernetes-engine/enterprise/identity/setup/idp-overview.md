---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/idp-overview/
title: Identity provider configuration overview \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:36:50.100574+00:00
---

# Identity provider configuration overview  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/idp-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Identity provider configuration overview Stay organized with collections  Save and categorize content based on your preferences. 

This document is for platform administrators who are responsible for setting up and managing identity within your organization. If you're a cluster administrator or application operator, ask your platform administrator to complete the setup described here before you configure individual clusters or use the fleet setup.

## Before you begin

If you want cluster administrators to provide authentication access using the fully qualified domain name (FQDN) of the cluster's Kubernetes API server (recommended), do the following. Otherwise, you can skip ahead to configuring your identity provider. You can learn more about user authentication methods in [Set up an authentication method for user access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access).

  * Configure your domain name service (DNS) to resolve your chosen fully qualified domain name to the cluster's control plane VIPs (virtual IP addresses). Users can access the cluster using this domain name.
  * Use a Server Name Indication (SNI) certificate issued by your trusted enterprise Certificate Authority (CA). This certificate specifically mentions your FQDN as a valid domain, eliminating potential certificate warnings for users. You can provide the SNI certificate during cluster creation. For more information on specifying SNI certificates, see [SNI certificate authentication](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/user-cluster-configuration-file#authentication-sni-section).
  * If SNI certificates are not feasible, cluster administrators need to configure all user devices to trust the cluster-CA certificate. This avoids certificate warnings but requires distributing the cluster-CA certificate to all users.



For more information on user login access using these certificates, see [Authenticate using FQDN access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#alternativeuserloginaccess).

## Configure the identity provider

How you configure your identity provider depends on the authentication protocol that you want to use. For more information, see one of the following pages:

  * [Configure OIDC providers](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider)
  * [Configure SAML providers](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/saml-provider)
  * [Configure LDAP providers](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider-ldap)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
