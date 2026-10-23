---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/troubleshooting/troubleshoot-with-feature-state-condition/
title: Understanding Feature State Conditions \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:25.373126+00:00
---

# Understanding Feature State Conditions  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/troubleshooting/troubleshoot-with-feature-state-condition/

You are viewing archived v1.25 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understanding Feature State Conditions

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

This page describes how to interpret and act upon Conditions reported on your Cloud Service Mesh cluster or fleet.

To check for conditions, run this command:
    
    
      gcloud container fleet mesh describe --project FLEET_PROJECT
    

The output may include `conditions` in `membershipStates` for a cluster, like:
    
    
      ...
      membershipStates:
        projects/test-project/locations/us-central1/memberships/my-membership:
          servicemesh:
            conditions:
              - code: <CONDITION_CODE>
                details: ...
                documentationLink: ....
                severity: ...
    

Values of `code` are described in more detail on this page.

## NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED

You may see the `NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED` error code in the `Conditions` field of your membership:
    
    
        membershipStates:
          projects/test-project/locations/us-central1/memberships/my-membership:
            servicemesh:
              conditions:
              - code: NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED
                details: One or more node pools have workload identity federation disabled.
                documentationLink: https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
                severity: ERROR
              controlPlaneManagement:
                details:
                - code: REVISION_FAILED_PRECONDITION
                  details: Required in-cluster components are not ready. This will be retried
                    within 15 minutes.
                implementation: TRAFFIC_DIRECTOR
                state: FAILED_PRECONDITION
    

This error is shown if the GKE cluster does not have [Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) enabled on all node pools of that cluster, since this is a prerequisites for the installation of Cloud Service Mesh.

To resolve this error message, you must follow instructions to [Enable Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools) on all node pools. Note that enablement may vary depending on your specific cluster case.

After enablement, the error message should be automatically removed and your cluster should go back to `ACTIVE` state. If the issue persists and you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.25/docs/getting-support).

## MESH_IAM_PERMISSION_DENIED

This error indicates that the service account does not have enough permission to access your fleet project. Follow the steps for troubleshooting:

  1. Verify if your service account has granted `Anthos Service Mesh Service Agent` role. For details on how to verify IAM permission and add it, go to [Revision(s) reporting as unhealthy error](https://docs.cloud.google.com/service-mesh/v1.25/docs/managed/troubleshoot-managed-anthos-service-mesh#revisions_reporting_as_unhealthy_error) and use the same steps there.

  2. If permission is verified while issue persists, contact Google customer support for further assistance.




## MESH_IAM_CROSS_PROJECT_PERMISSION_DENIED

This error indicates that the fleet project service account does not have enough permission to access a different project (the cluster project or the network project).

For [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks), make sure to grant all the fleet projects service account `Anthos Service Mesh Service Agent` role in the Shared VPC network project.

For the GKE fleet project and cluster project scenarios, make sure to grant the fleet project service account `Anthos Service Mesh Service Agent` role in the cluster project.

Example troubleshooting command:

  1. Verify if your network project or cluster project service account has granted `Anthos Service Mesh Service Agent` role to the fleet project service account. If not, run:
         
         gcloud projects add-iam-policy-binding NETWORK_OR_CLUSTER_PROJECT_ID  \
             --member "serviceAccount:service-FLEET_PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com" \
             --role roles/anthosservicemesh.serviceAgent
         

In addition, confirm that you don't have automation that would remove this binding.

  2. If permission is verified while issue persists, contact Google customer support for further assistance.




## CONFIG_VALIDATION_ERROR

This error indicates that some mesh related configuration applied on one or more memberships in the fleet cannot be successfully applied. The error details describe how best the user can address this.
    
    
      membershipStates:
        projects/test-project/locations/us-central1/memberships/my-membership:
          servicemesh:
            conditions:
            - code: CONFIG_VALIDATION_ERROR
              details: 'Unsupported ProxyConfig fields: [proxyconfig.statNameLength]'
              severity: ERROR
            controlPlaneManagement:
    

Config validation errors for a specific configuration mandate user action. For example, errors regarding usage of unsupported api fields are best addressed by removing the offending configuration from the Mesh API.

In the Cloud Console, navigate to Kubernetes Engine > Secrets & ConfigMaps > istio-asm-managed (the name of the ConfigMap depends upon which release channel you are using; e.g. istio-asm-managed-stable or istio-asm-managed-rapid) then select the YAML tab.

For example, meshConfig.configSources is no longer supported:
    
    
    apiVersion: v1
    data:
      mesh: |
        enablePrometheusMerge: true
        trustDomain: "foobar.svc.id.goog"
        trustDomainAliases:
          - cluster.local
    
        configSources:
          - address: k8s://
          - address: fs:///var/lib/istio/config/data
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
