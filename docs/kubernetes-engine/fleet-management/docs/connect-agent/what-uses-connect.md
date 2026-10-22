---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/what-uses-connect/
title: What uses Connect \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:20.726449+00:00
---

# What uses Connect  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/what-uses-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  What uses Connect Stay organized with collections  Save and categorize content based on your preferences. 

Topic last modified: June 18 2024 **Note:** The information in this topic is not exhaustive. It will change over time as new components that operate over Connect are introduced or as the scope or permissions of existing Google Cloud-side controllers evolve.

When you register your Kubernetes clusters with Google Cloud using Connect, a long-lived, [authenticated and encrypted](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/security-features) connection is established between your clusters and the Google Cloud control plane. The connection surfaces information about clusters in the Google Cloud console, and it lets you manage and deploy configurations and resources to clusters using GKE components and features, such as Config Management.

This topic describes the nature of the connection between Google Cloud and Connect and provides details about the Google Cloud-side controllers that operate on your clusters over Connect.

## About the connection between Google Cloud and Connect

As described in the [Security features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/security-features) topic, only the Google Cloud control plane makes requests over Connect to each connected cluster (for example, to a cluster's API server), and the cluster sends responses back to the control plane. (Cluster services and resources cannot initiate requests to the control plane over Connect.) The connection allows authorized users and Google-side automation to reach and authenticate against clusters.

For example, Connect lets the Google Cloud console get information about workloads and services; or allows Config Management to install or update the Connect in-cluster agent and observe the sync status. Connect also lets the metering agent observe the number of vCPUs in a connected cluster.

Connect does not provide data transport for container images, load balancing, database connections, Logging, or Monitoring. You must establish connectivity for those in parallel through their own mechanisms.

## Google Cloud console user access to clusters through Connect

After users in your organization [log in](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/console#log-in) to a cluster through the Google Cloud console, they have specific cluster permissions determined by the role-based access controls (RBAC) assigned to them. The cluster (not Connect) enforces the permissions. Standard Kubernetes logs let you audit the actions that each user took in managing a cluster.

The following table shows which parts of the Google Cloud console let users interact with clusters through Connect.

Google Cloud console section | What users can do  
---|---  
[ Kubernetes Engine](https://console.cloud.google.com/kubernetes/list) | Manage fleet-registered clusters and workloads, manage GKE components.  
[ Knative serving](https://console.cloud.google.com/kubernetes/run) | Build, deploy, and manage services and applications.  
[ Marketplace](https://console.cloud.google.com/marketplace) | Deploy and manage third-party applications.  
  
## Google Cloud-side controller access to clusters through Connect

Google Cloud-side controllers access a cluster from the Google Cloud control plane using the [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent/security-features#architecture-of-connect-for-anthos). These controllers provide management and automation for the functionality you enable on your clusters. For example, Config Management has a Google Cloud-side controller that helps direct the lifecycle of in-cluster agents and provides a UI to configure and view the status of Config Management running across multiple clusters.

Different controllers access clusters using different identities, and you can audit each controller's activities in Kubernetes [audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).

The following table summarizes how Google Cloud-side controllers operate over Connect. The table highlights key details about controllers: the permissions they need, their IDs in Kubernetes audit logs, and whether or not you can disable them.

Disabling a component in this context means turning it off completely, with no individual parts of the component able to be used in clusters.

Component Name | Can be disabled? | Cluster role / RBAC permissions | Description | ID in cluster audit logs  
---|---|---|---|---  
Feature Authorizer | No (**enabled** by default) | `cluster-admin` |  Feature Authorizer adds RBAC for [fleet-enabled components](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/fleets#fleet-enabled-components), or features, operating on Kubernetes clusters, ensuring each has only the specific permissions required to perform its functions. You cannot disable Feature Authorizer as long as there are registered Memberships in the project. See [ Feature authorization in a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features#feature_authorization) for more information. | service-project-number@gcp-sa-**gkehub**.iam.gserviceaccount.com  
Config Management | Yes (**disabled** by default) | `cluster-admin` |  The Config Management controller manages its own in-cluster agents and provides a UI that shows the status of Config Management across all clusters in a fleet. The controller installs its in-cluster components and creates a local service account with the appropriate permissions to deploy all types of Kubernetes configurations on behalf of users. When not installing or managing in-cluster components, the Config Management controller reads status information from its in-cluster agent. | service-project-number@gcp-sa-**acm**.iam.gserviceaccount.com  
Usage metering | No (**enabled** by default) | See RBAC definition | The metering controller reads basic information about connected clusters to provide billing services. This controller requires its permissions to:

  * Meter based on node vCPU capacity.
  * Watch and delete the `metering.gke.io/usagerecords` custom resource.
  * Create and update the `anthos.gke.io/entitlements` custom resource.

You cannot disable Metering, as long as there are registered Memberships in the project. | service-project-number@gcp-sa-**mcmetering**.iam.gserviceaccount.com  
  
## RBAC for specific components operating over Connect

The following API definitions show access control permissions for different component resources operating over Connect.

### Usage metering RBAC over Connect
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      labels:
        hub.gke.io/owner-feature: metering
        hub.gke.io/project: [PROJECT_ID]
      name: metering
      selfLink: /apis/rbac.authorization.k8s.io/v1/clusterroles/metering
    rules:
    - apiGroups:
      - ""
      resources:
      - nodes
      verbs:
      - get
      - watch
      - list
    - apiGroups:
      - metering.gke.io
      resources:
      - usagerecords
      verbs:
      - get
      - list
      - watch
      - delete
    - apiGroups:
      - anthos.gke.io
      resources:
      - entitlements
      verbs:
      - create
      - delete
      - get
      - list
      - update
      - watch
    - apiGroups:
      - apiextensions.k8s.io
      resources:
      - customresourcedefinitions
      verbs:
      - create
      - list
      - watch
    - apiGroups:
      - apiextensions.k8s.io
      resourceNames:
      - entitlements.anthos.gke.io
      resources:
      - customresourcedefinitions
      verbs:
      - get
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
