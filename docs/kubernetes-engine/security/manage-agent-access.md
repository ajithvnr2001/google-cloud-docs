---
url: https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access/
title: Manage access to Google Cloud APIs for agents \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:45.289687+00:00
---

# Manage access to Google Cloud APIs for agents  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/manage-agent-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Manage access to Google Cloud APIs for agents Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Agent Identity for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Application developers can [request an _agent identity_](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity) for AI agents that run on Google Kubernetes Engine (GKE). The agent identity is a per-Pod identity that can be cryptographically bound to each Pod in the workload. Agents can then authenticate to Google Cloud APIs by using the agent identity. You can control which resources an agent can access by including the agent as a principal in Identity and Access Management (IAM) policies. This document describes how to manage access to Google Cloud APIs and services for agents that use an agent identity.

This document is intended for security administrators and platform administrators who manage authorization for agents that developers deploy to GKE clusters. You should already be familiar with the following topics:

  * [About Agent Identity for GKE](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity)
  * [IAM policies](https://docs.cloud.google.com/iam/docs/policy-types)



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you have an existing Autopilot cluster or a Standard cluster that has [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled and runs GKE version 1.37.0-gke.3503000 or later.



### Required roles

To get the permissions that you need to manage access to Google Cloud APIs for agents, ask your administrator to grant you the following IAM roles on the Google Cloud project: 

  * Create IAM policies: [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) 
  * Create a Cloud Storage bucket, upload objects, and set IAM policies: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * Deploy workloads in GKE clusters: [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Find the principal identifier of an agent

This section describes how to construct the principal identifier for an agent. You can use this identifier in IAM policies to control which resources the agent can access.

Any agent workload that [requests an agent identity](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity) gets a SPIFFE identity string that's unique to that workload. When the application calls Google Cloud APIs, the calls are authenticated by using an agent identity access token that validates that the workload has an agent identity. This access token includes an IAM principal identifier for the agent workload, which you can include in IAM policies to control which resources that agent has access to.

When you design your IAM policies, you can construct the principal identifiers for agents by using the following information:

  * The resource hierarchy of the project.
  * The cluster name.
  * The Kubernetes namespace and the Kubernetes ServiceAccount in that namespace.



When developers deploy agents that get an agent identity that matches the principal identifier, the agent inherits the access that you specified in your policy.

To find the principal identifier to use in your policies, follow these steps:

  1. Identify the trust domain for the identity. The trust domain depends on whether the project is in an organization, as follows:

     * **Projects that are in an organization** :
           
           agents.global.org-ORGANIZATION_ID.system.id.goog
           

Replace `ORGANIZATION_ID` with the organization ID.

     * **Projects that aren't in an organization** :
           
           agents.global.proj-PROJECT_NUMBER.system.id.goog
           

Replace `PROJECT_NUMBER` with the project number of the cluster project.

  2. Identify the following information about the cluster:

     * The name of the GKE cluster.
     * The location of the cluster control plane, such as `us-central1`.
     * The Kubernetes namespace that developers deploy the workloads to.
     * The name of the Kubernetes ServiceAccount that developers must use for the agent workload.

If you don't know this information, then ask your platform team. The platform team should set up the namespaces, ServiceAccounts, and RBAC policies in the cluster so that agents that have different access requirements get different identities.

  3. Construct the principal identifier:
         
         principal://TRUST_DOMAIN/resources/container/projects/PROJECT_NUMBER/locations/CONTROL_PLANE_LOCATION/clusters/CLUSTER_NAME/ns/KUBERNETES_NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT
         

Replace the following:

     * `TRUST_DOMAIN`: the trust domain for the agent identity.
     * `PROJECT_NUMBER`: the project number of the cluster project.
     * `CONTROL_PLANE_LOCATION`: the region or zone of the cluster control plane.
     * `CLUSTER_NAME`: the name of the cluster.
     * `KUBERNETES_NAMESPACE`: the name of the Kubernetes namespace.
     * `KUBERNETES_SERVICEACCOUNT`: the name of the Kubernetes ServiceAccount.



## Use policies to control access

This section describes how to use an agent's principal identifier to control which Google Cloud APIs and services the agent can access. To control access, include the principal identifier in any of the following IAM policies:

  * [Principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-create)
  * [Deny policies](https://docs.cloud.google.com/iam/docs/deny-access)
  * [Allow policies](https://docs.cloud.google.com/iam/docs/manage-access-other-resources)



After you create or update a policy, any agent that requests an agent identity and runs in that namespace and uses that ServiceAccount has the access that you specify in your policies.

### Authorize agents to access the auth manager

The Agent Identity auth manager is an authentication broker and credential vault that agents might use to get credentials to access external tools and services, either as the agent's own identity or on behalf of an end user. The auth manager can have one or more auth providers, each of which handles a specific authentication and credential acquisition flow for a specific service. To give GKE agents access to specific auth providers, follow these steps:

  1. Find the principal identifier for the agent.
  2. Get the name of the auth provider that the agent needs to access.
  3. Grant the Agent Identity User (`roles/agentidentity.user`) role on the auth provider to the agent principal:
         
         gcloud agent-identity auth-providers add-iam-policy-binding AUTH_PROVIDER_NAME \
             --location=AUTH_PROVIDER_LOCATION \
             --member=PRINCIPAL_IDENTIFIER \
             --role=roles/agentidentity.user
         

Replace the following:

     * `AUTH_PROVIDER_NAME`: the name of the auth provider.
     * `AUTH_PROVIDER_LOCATION`: the region of the auth provider.
     * `PRINCIPAL_IDENTIFIER`: the principal identifier of the agent.

Alternatively, for agents that are registered in Agent Registry, you can manage access to auth providers by [creating an auth provider binding](https://docs.cloud.google.com/agent-registry/manage-bindings#auth-provider).




## What's next

  * [Request an identity for a GKE agent](https://docs.cloud.google.com/kubernetes-engine/security/request-agent-identity)
  * [Authenticate by using an agent identity in GKE](https://docs.cloud.google.com/kubernetes-engine/security/authenticate-agent-identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
