---
url: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/understand-health-checks/
title: Understand health checks \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:48.533296+00:00
---

# Understand health checks  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/understand-health-checks/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand health checks

Cloud Service Mesh uses health checks to determine the health of your workloads and route traffic accordingly. This page describes how health checking works in Cloud Service Mesh and how to manage the required firewall rules.

## About Health Checks

In a service mesh, the control plane needs to know the health status of workloads (Pods) to ensure traffic is only routed to healthy endpoints.

  * **Managed Cloud Service Mesh (`TRAFFIC_DIRECTOR` control plane implementation)**: Cloud Service Mesh uses Google Cloud's [centralized health-checking infrastructure](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) to perform health checks. This infrastructure resides outside your cluster and sends health check probes to your cluster nodes. In addition we install a DaemonSet named `snk` in the `kube-system` namespace that intercepts all traffic on port 7877 and exposes health status for all workloads.

  * **Istiod control plane ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations))**: Health checking is done within the cluster using Kubernetes mechanisms.




## Firewall Rules for Managed Health Checks

To allow Managed Cloud Service Mesh's external health check probes to reach your GKE nodes, appropriate firewall rules must be present.

### Firewall rule specification

Cloud Service Mesh requires a firewall rule in the VPC network project, for each managed Cloud Service Mesh cluster in your fleet. These rules allow ingress traffic from Google's health check probes to the dedicated health check port on the nodes of your GKE clusters:

  * **Source Ranges** : `35.191.0.0/16`, `130.211.0.0/22`
  * **Allowed Protocols/Ports** : `tcp:7877`



### Do I need to take action?

Whether you need to manually configure permissions or firewall rules depends on where your VPC network is located relative to your fleet and GKE cluster projects:

  * The VPC network is located in the fleet project => **No action required**. The Cloud Service Mesh service agent is automatically granted `roles/anthosservicemesh.serviceAgent`, which includes these permissions.

  * The VPC network is located in the GKE cluster project => **No action required**. You granted `roles/anthosservicemesh.serviceAgent` to the Cloud Service Mesh service agent during onboarding.

  * The VPC network is in a separate host project (such as a Shared VPC host project) that is neither the fleet project nor the cluster project => **Action required**. You must grant the service agent permission to manage the firewall rules in that project.




To help identify these projects in the following instructions, note the following roles:

  * **Fleet Project** : The project where your GKE clusters are registered. The Cloud Service Mesh service agent resides here.
  * **VPC Network Project** : The project that contains the VPC network connected to your GKE clusters (this is the host project if you use Shared VPC).
  * **Cluster Project** : The project where your GKE clusters are located.



### System-Managed Firewall Rules

By default, Cloud Service Mesh automatically creates and manages the firewall rules required for health checks on your behalf. The system will create one rule per cluster during onboarding, and delete that rule when uninstalling.

#### Required permissions

To manage system-managed firewall rules, the Cloud Service Mesh service agent requires the following permissions in the VPC network project:

  * `compute.firewalls.get` (to check if the firewall rule already exists)
  * `compute.firewalls.create` (to create the firewall rule if it doesn't exist)
  * `compute.firewalls.update` (to reconcile the firewall rule back to the intended configuration if it has been modified)
  * `compute.firewalls.delete` (to delete the firewall rule when offboarding)
  * `compute.networks.updatePolicy` (part of the two-level authorization check to attach, modify, or remove firewall rules on a VPC network)



#### VPC network in the fleet or cluster project (Automatic)

If your VPC network is in the fleet project or the GKE cluster project, no action is required. The Cloud Service Mesh service agent automatically has the required permissions to manage the firewall rules.

#### VPC network in a separate project (for example Shared VPC)

If your VPC network is in a separate project, the service agent in the fleet project does not have permission to manage resources in that project by default. You must grant the service agent permission to manage the firewall rules in the VPC network project.

You have two options for granting these permissions:

##### Option 1: Grant narrow firewall permissions (Best practice)

If you want Google to manage the firewall rules but want to restrict the permissions granted to the service agent on the VPC network project, you can create a custom IAM role with only the necessary firewall permissions.

  1. Create a custom IAM role with the required firewall permissions in the VPC network project:
         
         gcloud iam roles create LIMITED_IAM_ROLE_NAME \
             --project=NETWORK_PROJECT_ID \
             --title="Service Mesh Firewall Role" \
             --permissions="compute.firewalls.get,compute.firewalls.create,compute.firewalls.update,compute.firewalls.delete,compute.networks.updatePolicy" \
             --stage="GA"
         

  2. Grant the role in the VPC network project to the fleet project's Cloud Service Mesh service account:
         
         gcloud projects add-iam-policy-binding NETWORK_PROJECT_ID \
             --member "serviceAccount:service-FLEET_PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com" \
             --role "projects/NETWORK_PROJECT_ID/roles/LIMITED_IAM_ROLE_NAME"
         

Replace the placeholders:

     * `NETWORK_PROJECT_ID`: The ID of your VPC network project.
     * `FLEET_PROJECT_NUMBER`: The project number of your fleet project.
     * `LIMITED_IAM_ROLE_NAME`: The name you want to give to the custom role.



##### Option 2: Grant Service Mesh Service Agent role (Simplest)

The simplest approach is to grant the fleet project's service account the existing Service Mesh Service Agent role (`roles/anthosservicemesh.serviceAgent`) on the VPC network project.

  1. Grant the role in the VPC network project to the fleet project's Cloud Service Mesh service account:
         
         gcloud projects add-iam-policy-binding NETWORK_PROJECT_ID \
             --member "serviceAccount:service-FLEET_PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com" \
             --role roles/anthosservicemesh.serviceAgent
         

Replace the placeholders:

     * `NETWORK_PROJECT_ID`: The ID of your VPC network project.
     * `FLEET_PROJECT_NUMBER`: The project number of your fleet project.



### User-Managed Firewall Rules

If you prefer not to grant any write permissions (`create`, `update`, `delete`) to the Cloud Service Mesh service agent in the VPC network project, you can pre-create the firewall rules yourself and grant Google only the read (`get`) permission.

If the firewall rule already exists and matches the required specification, Cloud Service Mesh will use it without attempting to modify it.

#### Step 1: Create the firewall rule

Find your `SHORT_CLUSTER_ID`:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --project=CLUSTER_PROJECT_ID \
        --format="value(id)" | cut -c1-8
    

Create a firewall rule using the following template:
    
    
    gcloud compute firewall-rules create gke-csm-thc-SHORT_CLUSTER_ID \
        --project=NETWORK_PROJECT_ID \
        --network=NETWORK_NAME \
        --description="Firewall rule for service mesh health checks" \
        --direction=INGRESS \
        --action=ALLOW \
        --rules=tcp:7877 \
        --source-ranges="35.191.0.0/16,130.211.0.0/22" \
        --target-tags=gke-CLUSTER_NAME-SHORT_CLUSTER_ID-node
    

Replace the placeholders:

  * `SHORT_CLUSTER_ID`: The first 8 characters of the GKE cluster ID that you found in the previous step.
  * `NETWORK_PROJECT_ID` and `NETWORK_NAME`: The project (VPC network project) and name of the VPC network.
  * `CLUSTER_NAME`: The name of the GKE cluster.



Repeat Step 1 for each managed Cloud Service Mesh cluster in your fleet.

#### Step 2: Grant read-only permission to Google

Grant the `compute.firewalls.get` permission to the Cloud Service Mesh service agent.

  1. Create a custom role with only the `get` permission in the VPC network project:
         
         gcloud iam roles create READONLY_IAM_ROLE_NAME \
             --project=NETWORK_PROJECT_ID \
             --title="Service Mesh Firewall Read-Only Role" \
             --permissions="compute.firewalls.get" \
             --stage="GA"
         

  2. Grant the role to the Cloud Service Mesh service agent:
         
         gcloud projects add-iam-policy-binding NETWORK_PROJECT_ID \
             --member "serviceAccount:service-FLEET_PROJECT_NUMBER@gcp-sa-servicemesh.iam.gserviceaccount.com" \
             --role "projects/NETWORK_PROJECT_ID/roles/READONLY_IAM_ROLE_NAME"
         




#### Delete the firewall rule on cluster deletion, or on offboarding from Cloud Service Mesh

If you created the firewall rules manually (User-Managed Firewall Rules), Cloud Service Mesh cannot automatically delete them when you delete the cluster or offboard from the service mesh. You must manually delete the firewall rules to avoid leaving unused resources.

To delete the firewall rule:
    
    
    gcloud compute firewall-rules delete gke-csm-thc-SHORT_CLUSTER_ID \
        --project=NETWORK_PROJECT_ID
    

**Note:** Remember to get the `SHORT_CLUSTER_ID` before you delete the cluster, as you will need it to identify the firewall rule for deletion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
