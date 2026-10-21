---
url: https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring/
title: Secure your fleet \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:07:57.882180+00:00
---

# Secure your fleet  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/docs/concepts/security-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Secure your fleet Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides a range of features to secure your fleet and the applications that run on it. This page provides an overview of fleet security features, with links to find out more.

## Manage identity

Google Cloud provides the following options for authenticating to fleet clusters in a simple, consistent, and secured way, wherever the clusters live. After you have set up authentication, you can configure more fine-grained access control to your clusters using [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).

### Authenticate with Google Cloud

All GKE clusters on Google Cloud are configured to accept Google Cloud user and service account identities by default. If your fleet contains clusters in multiple environments, you can configure the [Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway) so that users and service accounts can also authenticate to any registered cluster using their Google Cloud ID.

Learn more about setting up and using authentication with Google Cloud in the following guides:

  * [Configuring cluster access for `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
  * [Connecting to registered clusters with the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway)
  * [Setting up the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/setup)
  * [Using the Connect gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using)



### Authenticate with third-party providers

If you want to use your existing third-party identity provider to authenticate to your fleet clusters, GKE Identity Service is an authentication service that lets you bring your existing identity solutions to multiple environments. It supports all [OpenID Connect (OIDC)](https://openid.net/connect/) providers such as Okta and Microsoft AD FS, as well as preview support for LDAP providers in some environments. You can set up GKE Identity Service on a cluster-by-cluster basis or with [a single configuration for your entire fleet](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet), where supported.

Learn more about setting up and using third-party authentication, including supported environments and providers, in the following guides:

  * [Introducing GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity)
  * [Accessing clusters with GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing)



### Authenticate with a bearer token

If the preceding Google-provided solutions aren't suitable for your organization, you can set up authentication using a Kubernetes service account and using its bearer token to log in. For details, see [Set up using a bearer token](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/bearer-token-auth).

## Manage fleet security

Google Cloud provides a range of features and products that improve the security of your fleets and workloads, such as the following:

  * Binary Authorization to ensure that only trusted images are deployed on your fleet clusters
  * Kubernetes network policies to control connections between Pods
  * Fine-grained service access control for Cloud Service Mesh
  * The GKE security posture dashboard to monitor your clusters' security posture.



### Monitor fleet security posture

The GKE security posture dashboard helps you assess and manage your fleet's GKE clusters for security concerns and get actionable recommendations to fix them. Capabilities include [configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning).

The dashboard displays discovered concerns for all of the clusters in the selected fleet and for any standalone GKE clusters in the selected project.

  * For details and a full list of capabilities, see [About the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard).
  * For pricing information, see [GKE security posture dashboard pricing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#pricing).



### Configure security posture dashboard features at fleet level

You can manage some security dashboard features at fleet level, so that all the clusters in your fleet can use the same default settings for security observability.

  * Learn how to [configure security posture dashboard features](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture) for your fleet.



### Fleet security resources

Learn more about fleet security features in the following guides:

  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)
  * [Kubernetes network policies](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy)
  * Application security in Cloud Service Mesh: 
    * [Authorization policy overview](https://docs.cloud.google.com/service-mesh/docs/security/authorization-policy-overview)
    * [Configuring transport security](https://docs.cloud.google.com/service-mesh/docs/security/configuring-mtls)
    * [Monitoring mesh security](https://docs.cloud.google.com/service-mesh/docs/observability/monitor-mesh-security)
  * [About the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)



## Manage cluster policies

Policy Controller enables the enforcement of fully programmable policies for your fleet clusters. These policies act as "guardrails" and prevent any changes to the configuration of the Kubernetes API from violating security, operational, or compliance controls.

Learn more about what you can do with Policy Controller in the [Policy Controller documentation](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
