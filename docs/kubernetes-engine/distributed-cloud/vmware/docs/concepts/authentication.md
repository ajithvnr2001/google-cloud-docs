---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication/
title: Manage identity with GKE Identity Service \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:36.628973+00:00
---

# Manage identity with GKE Identity Service  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Manage identity with GKE Identity Service Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud supports [OpenID Connect (OIDC)](https://openid.net/connect/) and [Lightweight Directory Access Protocol (LDAP)](https://ldap.com/) as authentication mechanisms for interacting with a cluster's Kubernetes API server, using GKE Identity Service. GKE Identity Service is an authentication service that lets you bring your existing identity solutions for authentication to multiple cluster environments. Users can log in to and use your clusters from the command line (all providers) or from the Google Cloud console (OIDC only), all using your existing identity provider.

You can use both on-premises and publicly reachable identity providers with GKE Identity Service. For example, if your enterprise runs an [Active Directory Federation Services (ADFS)](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) server, the ADFS server could serve as your OpenID provider. You might also use publicly-reachable identity provider services such as Okta. Identity provider certificates may be issued by either a well-known public certificate authority (CA), or by a private CA.

**Note:** The GKE Identity Service runs as a Pod inside the cluster control plane. During cluster lifecycle phases, the API Server is dynamically configured to use the in-cluster GKE Identity Service as the authentication webhook for all incoming requests. The API Server [isn't able to use in-cluster DNS](https://github.com/kubernetes/minikube/issues/3772). As a result, the API Server is configured to access GKE Identity Service as a REST resource access. In audit logs, this invocation is recorded as a `CREATE` request to the Services or proxy resource by a `system:anonymous` user.

For an overview of how GKE Identity Service works, see [Introducing GKE Identity Service](https://docs.cloud.google.com/anthos/identity).

If you already use or want to use Google IDs to log in to your GKE clusters instead of an OIDC or LDAP provider, we recommend using the Connect gateway for authentication. Find out more in [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).

## Setup process and options

### OIDC

  1. Register GKE Identity Service as a client with your OIDC provider following the instructions in [Configuring providers for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/provider).

  2. Choose from the following cluster configuration options:

     * Configure your clusters at fleet level following the instructions in [Configuring clusters for fleet-level GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/fleet-cluster) (preview, Google Distributed Cloud version 1.8 and higher). With this option, your authentication configuration is centrally managed by Google Cloud.
     * Configure your clusters individually following the instructions in [Configuring clusters for GKE Identity Service with OIDC](https://docs.cloud.google.com/anthos/identity/setup/per-cluster). Because fleet-level setup is a preview feature, you may want to use this option in production environments, if you are using an earlier version of Google Distributed Cloud, or if you require GKE Identity Service features that aren't yet supported with fleet-level lifecycle management.
  3. Set up user access to your clusters, including role-based access control (RBAC), following the instructions in [Setting up user access for GKE Identity Service](https://docs.cloud.google.com/anthos/identity/setup/user-access).




### LDAP

  * Follow the instructions in [Set up GKE Identity Service with LDAP](https://docs.cloud.google.com/anthos/identity/setup/ldap).



## Accessing clusters

After GKE Identity Service has been set up, users can log in to configured clusters using either the command line or the Google Cloud console.

  * Learn how to log in to registered clusters with your OIDC or LDAP ID in [Accessing clusters using GKE Identity Service](https://docs.cloud.google.com/anthos/identity/accessing).
  * Learn how to log in to clusters from the Google Cloud console in [Logging in to a cluster from the Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) (OIDC only).



## Troubleshoot the login flow

To troubleshoot [login flows that authenticate directly on the GKE Identity Service server with a fully qualified domain name (FQDN)](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-fqdn-access), you can use the GKE Identity Service diagnostic utility. The diagnostic utility simulates login flows with your OIDC provider to quickly identify configuration problems. This tool requires a version 1.32 or higher cluster and only supports OIDC. For more information, see [GKE Identity Service diagnostic utility](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/anthos-v2-diagnostic-utility).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
