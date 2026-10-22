---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/
title: Connect Agent overview \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:15.596067+00:00
---

# Connect Agent overview  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Connect Agent overview Stay organized with collections  Save and categorize content based on your preferences. 

When you register a cluster outside Google Cloud to your fleet, Google Cloud uses a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) called the _Connect Agent_ to establish a connection between the cluster and your Google Cloud project, and to handle Kubernetes requests. The Connect Agent is not required to establish a connection for GKE clusters running in Google Cloud.

This enables access to cluster and to workload management features in Google Cloud, including a unified user interface, [Google Cloud console](https://docs.cloud.google.com/cloud-console), to interact with your cluster.

If your network is configured to allow outbound requests, you can configure the Connect Agent to traverse NATs, egress proxies, and firewalls to establish a long-lived, encrypted connection between your cluster's Kubernetes API server and your Google Cloud project. Once this connection is enabled, you can use your own credentials to log back into your clusters and access details about their Kubernetes resources. This effectively replicates the UI experience that is otherwise only available to GKE clusters.

After the connection is established, the Connect Agent software can exchange account credentials, technical details, and metadata about connected infrastructure and workloads necessary to manage them with Google Cloud, including the details of resources, applications, and hardware.

This cluster service data is associated with your Google Cloud project and account. Google uses this data to maintain a control plane between your cluster and Google Cloud, to provide you with any Google Cloud services and features you request, including facilitating support, billing, providing updates, and to measure and improve the reliability, quality, capacity, and functionality of Connect and Google Cloud services available through Connect.

You remain in control of what data is sent through Connect: your Kubernetes API server performs [authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/), [authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/), and [audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) on all requests via Connect. Google and users can access data or APIs via Connect after they have been authorized by the cluster administrator (for example, via [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)); the cluster administrator can revoke that authorization.

## Connect IAM roles

[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) allows users, groups, and service accounts to access Google Cloud APIs and to perform tasks within Google Cloud products.

You need to provide specific IAM [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to launch the Connect Agent and interact with your cluster using the Google Cloud console or Google Cloud CLI. These roles do not allow direct access to connected clusters. You can learn more about logging in to clusters from the Google Cloud console in [Working with clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console).

Some of these roles allow you to access information about clusters, including:

  * Cluster names
  * Public keys
  * IP addresses
  * Identity providers
  * Kubernetes versions
  * Cluster size
  * Other cluster metadata



Connect uses the following IAM roles:

Role name | Role title | Description | Permissions  
---|---|---|---  
`roles/gkehub.editor` | GKE Fleet Editor | Provides edit access to GKE Hub resources. |  **Permissions for Google Cloud**

  * resourcemanager.projects.get
  * resourcemanager.projects.list

**Permissions for GKE Fleet**

  * gkehub.memberships.list
  * gkehub.memberships.get
  * gkehub.memberships.create
  * gkehub.memberships.update
  * gkehub.memberships.delete
  * gkehub.memberships.generateConnectManifest
  * gkehub.memberships.getIamPolicy
  * gkehub.locations.list
  * gkehub.locations.get
  * gkehub.operations.list
  * gkehub.operations.get
  * gkehub.operations.cancel
  * gkehub.features.list
  * gkehub.features.get
  * gkehub.features.create
  * gkehub.features.update
  * gkehub.features.delete
  * gkehub.features.getIamPolicy
  * gkehub.fleet.*
  * gkehub.membershipfeatures.list
  * gkehub.membershipfeatures.get
  * gkehub.membershipfeatures.create
  * gkehub.membershipfeatures.update
  * gkehub.membershipfeatures.delete

  
`roles/gkehub.viewer` | GKE Fleet Viewer | Provide read-only access to GKE Fleet and related resources. |  **Permissions for Google Cloud**

  * resourcemanager.projects.get
  * resourcemanager.projects.list

**Permissions for GKE Fleet**

  * gkehub.memberships.list
  * gkehub.memberships.get
  * gkehub.memberships.generateConnectManifest
  * gkehub.memberships.getIamPolicy
  * gkehub.locations.list
  * gkehub.locations.get
  * gkehub.operations.list
  * gkehub.operations.get
  * gkehub.features.list
  * gkehub.features.get
  * gkehub.features.getIamPolicy
  * gkehub.membershipfeatures.list
  * gkehub.membershipfeatures.get

  
`roles/gkehub.connect` | GKE Connect Agent | Provides ability to establish new connections between external clusters and Google. | gkehub.endpoints.connect  
  
## Resource usage and requirements

Typically the Connect agent installed at registration uses 500m of CPU and 200Mi of memory. However, this usage can vary depending on the number of requests being made to the agent per second, and the size of those requests. These can be affected by a number of factors, including the size of the cluster, the number of users accessing the cluster via the Google Cloud console (the more users and/or workloads, the more requests), and the number of [fleet-enabled features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-enabled-components) on the cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
