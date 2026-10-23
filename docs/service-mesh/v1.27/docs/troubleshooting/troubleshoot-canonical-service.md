---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-canonical-service/
title: Resolving Canonical Service issues in Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:57.678900+00:00
---

# Resolving Canonical Service issues in Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-canonical-service/

You are viewing v1.27 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving Canonical Service issues in Cloud Service Mesh

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.27/docs/getting-support).

## Clusters in your mesh are running an older version of Cloud Service Mesh

If any of your clusters are running an earlier version of Cloud Service Mesh (<1.6.8) or a cluster is running Cloud Service Mesh with the Canonical Service controller disabled, then those clusters (and services running on them) will not appear in the Service Mesh UI. In order to use Canonical Services, you must upgrade each cluster to Cloud Service Mesh 1.6.8 or higher and use the default install option which includes the Canonical Service controller. For more information, see [Upgrading Cloud Service Mesh to the latest version](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade-path-old-versions-gke) if your clusters are on GKE or [Upgrading Cloud Service Mesh on premises](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade-path-old-versions-on-prem).

Alternatively, if you prefer not to install the controller in your clusters, you can enable the Managed Canonical Service Controller (currently in Preview) for your mesh.

For more information about enabling the Canonical Service controller, see [Enabling the Canonical Service controller](https://docs.cloud.google.com/service-mesh/v1.27/docs/canonical-service-controller-enable-and-disable).

## Cloud Service Mesh is not installed on the cluster

If Cloud Service Mesh is not installed on any of your clusters, those clusters will not appear in the Service Mesh UI. For more information on how to install Cloud Service Mesh, see the [Cloud Service Mesh documentation](https://docs.cloud.google.com/service-mesh/v1.27/docs).

## You are not logged into the on-premise cluster

If you have an on-premise cluster in the mesh and you are not logged in to the cluster, you will not be able to view the services corresponding to that cluster. In order to view those services in the dashboard, you must log in to the cluster. For more information on Logging into a cluster, see [Logging in to a cluster from the Cloud console](https://docs.cloud.google.com/anthos/fleet-management/docs/console).

## Your on-premise cluster is not reachable

If you have an on-premise cluster in the mesh and it is not reachable via the connect agent, you will not be able to view the services corresponding to that cluster. In order to view those services in the dashboard, make sure your cluster is running and is connected to Google Cloud. For more information on connecting your cluster to Google Cloud, see [Connect Overview](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview).

## A service with defined SLOs does not map 1:1 with a Canonical Service

Prior to the shift to [Canonical Service](https://docs.cloud.google.com/service-mesh/v1.27/docs/canonical-service), Cloud Service Mesh showed dashboards for Kubernetes Services. While Kubernetes Services and default Canonical Services often line up, it is possible that a Kubernetes Service can't automatically be matched to its corresponding Canonical Service or that the default Canonical Service boundary is not desired.

If you have Service Level Objectives (SLOs) set up on existing services which cannot be automatically matched to a default Canonical Service, they cannot be migrated. To start using Canonical Services you will need to delete the SLO(s) for the problematic service. If you'd like, you may [create new SLOs](https://docs.cloud.google.com/service-mesh/v1.27/docs/observability/create-slo) for the Canonical Service(s) that most closely match that service before deleting the old SLO.

## My dashboard doesn't have the contents I expect

The Service Mesh service dashboards are each scoped to a [Canonical Service](https://docs.cloud.google.com/service-mesh/v1.27/docs/canonical-service) in your service mesh, where a Canonical Service is a high-level logical service concept that spans all relevant workloads, regions, etc.

By default, existing labels in each workload instance (Pod or WorkloadEntry) define Canonical Services and follow these rules in decreasing priority:

  1. The `service.istio.io/canonical-name` label has already been explicitly set. No further action is taken.
  2. Otherwise, the `service.istio.io/canonical-name` label is added and its value is set to that of the `app.kubernetes.io/name` label.
  3. Otherwise, the `service.istio.io/canonical-name` label is added and its value is set to that of the `app` label.
  4. Otherwise, the `service.istio.io/canonical-name` label is added and its value is set to the `name` of the owning workload. The "owning workload" in this case if the Pod is deployed solo, or the Deployment, StatefulSet, etc. if using higher-level orchestration.



For most idiomatic users of Kubernetes and Kube Run / Knative, these rules map directly to how you already manage your services and workloads.

In some more custom or more complex use cases, however, the default heuristics do not capture your service appropriately, and in turn the Cloud Service Mesh dashboard you see does not include the contents you expect.

This can be fixed by manually defining Canonical Service scope.

## Manually defining the scope of a service

Wherever possible, we recommend that you use the automatic default grouping mechanisms. If you want to override these default groupings, however, you can do so by applying the `service.istio.io/canonical-name` Kubernetes label to your Kubernetes Pod and WorkloadEntry configurations.

For details, see [manually defining a Canonical Service](https://docs.cloud.google.com/service-mesh/v1.27/docs/define-canonical-service#manual).

## Resolve managed canonical controller issues

**1\. Check Feature State:** Execute the following command, where `FLEET_PROJECT_ID` is the ID of your Fleet Host project. Generally, the FLEET_PROJECT_ID is created by default and has the same name as the project. 
    
    
      gcloud container fleet mesh describe --project FLEET_PROJECT_ID
      

Example output:
    
    
          membershipStates:
            projects/<project-number>/locations/<location>/memberships/<membership-name>:
              state:
                code: OK
                description: 
                  Revision(s) ready for use: istiod-asm-183-2.
                  All Canonical Services have been reconciled successfully.
    

**2\. Take action based on`state.code`:**

In the feature state output, check the state of your cluster. Examine the value of `state.code`, it helps to understand the current status of the managed CSC. Based on the value of `state.code`, implement the corresponding actions:

  * **`MISSING`:**

    1. Wait for an hour to allow for potential initialization delays. 
    2. Re-run the `gcloud container fleet mesh describe --project <FLEET_PROJECT_ID>` command. If `state.code` is still missing, contact [Google Cloud Support](https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-canonical-service/) for assistance.
  * **`WARNING/ERROR`:**

    1. Check the `servicemesh.conditions` for detailed error information. 
    2. If the condition `CANONICAL_SERVICE_ERROR` is found, the managed Canonical Service Controller is encountering an issue. If not, the problem is likely external to Canonical Service Controller. 
    3. In both scenarios, contact [Google Cloud Support](https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-canonical-service/) for further troubleshooting
  * **`OK`:** Refer to the following table for actions based on the `state.description` text:


State.Description  |  Required Action   
---|---  
All Canonical Services have been reconciled successfully |  The CSC is operating as expected. No further intervention is required.   
The Managed Canonical Service Controller is yielding to the in-cluster controller  |  Follow the guide to [migrate from in-cluster controller](https://docs.cloud.google.com/service-mesh/v1.27/docs/canonical-service-migrate-from-in-cluster-controller)  
No specific information about canonical services is mentioned in `state.description`  | 

  1. If your cluster does not have any sidecar-injected pods or service entries, this situation can occur. To confirm the managed canonical controller's operational status, follow the steps outlined in the [managed controller is operational](https://docs.cloud.google.com/service-mesh/v1.27/docs/canonical-service-migrate-from-in-cluster-controller#verify-managed-controller-is-operational) section. 
  2. If required canonical services are still missing, ensure your canonical services are correctly defined. Refer: [Define canonical service ](https://docs.cloud.google.com/service-mesh/v1.27/docs/define-canonical-service).

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
