---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot/
title: Troubleshoot Config Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:42.270341+00:00
---

# Troubleshoot Config Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Troubleshoot Config Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Config Controller.

## Troubleshoot installation

### No network named default

When creating your Config Controller instance, you might receive an error about the default network not being available:
    
    
    Error 400: Project \"PROJECT_ID\" has no network named \"default\"., badRequest\n\n  on main.tf line 35, in resource \"google_container_cluster\" \"acp_cluster\"
    

This error occurs if you didn't specify an existing network with the [`--network`](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/config/controller/create#--network) flag and your [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) in Google Cloud is either deleted or disabled. By default, Config Controller creates the Google Kubernetes Engine cluster that backs your Config Controller instance in the default network.

If you want to create the instance in an existing network, add the `--network=NETWORK` flag when you create your Config Controller instance. Replace `NETWORK` with the name of an existing network.

If you want to create the Config Controller instance in the default network, re-create your default network with the following command:
    
    
    gcloud compute networks create default --subnet-mode=auto
    

For this command to work, enabling automatic subnets with the `--subnet-mode=auto` flag is required.

After you have recreated your default network, you can omit the `--network` flag when you create your Config Controller instance.

### Invalid value for MasterIpv4CidrBlock

Config Controller creation uses a default subnet of `172.16.0.128/28` for the [control plane IPv4 CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#step_1_view_control_planes_cidr_block). If there's a conflict in the IPv4 CIDR block, Config Controller creation fails with the following error:
    
    
    Cloud SSA\n\nError: Error waiting for creating GKE cluster: Invalid value for field PrivateClusterConfig.MasterIpv4CidrBlock: 172.16.0.128/28 conflicts with an existing subnet in one of the peered VPCs.
    

If you see this error, select a different private IPv4 CIDR and use it using the `--master-ipv4-cidr-block` flag in the `gcloud anthos config controller create` command.

To find IPv4 CIDR blocks that are already in use, complete the following steps:

  1. Find the name of the peering:
         
         gcloud compute networks peerings list --network=NETWORK
         

Replace `NETWORK` with the name of the network that you want to look up.

The output is similar to the following:
         
         NAME                                    NETWORK   PEER_PROJECT               PEER_NETWORK                            PEER_MTU  IMPORT_CUSTOM_ROUTES  EXPORT_CUSTOM_ROUTES  STATE   STATE_DETAILS
         gke-n210ce17a4dd120e16b6-7ebf-959a-peer  default  gke-prod-us-central1-59d2  gke-n210ce17a4dd120e16b6-7ebf-0c27-net            False                 False                 ACTIVE  [2021-06-08T13:22:07.596-07:00]: Connected.
         

  2. Show the IPv4 CIDR being used by the peering:
         
         gcloud compute networks peerings list-routes PEERING_NAME \
             --direction=INCOMING \
             --network=NETWORK \
             --region=REGION
         

Replace the following:

     * `PEERING_NAME`: the name of peering you want to look up
     * `NETWORK`: the name of network you want to look up
     * `REGION`: the name of the region your Config Controller instance is in



## Troubleshoot issues while running Config Controller

### Ran out of node pool IPs

If you see the following error message, then your node pools might not have enough IP addresses:
    
    
    Can't scale up because instances in managed instance groups hosting node pools ran out of IPs
    

This issue can happen if you omit the `--cluster-ipv4-cidr-block` flag. When you omit this flag, Config Controller defaults to the `/20` Pod CIDR range. This range gives you a maximum of 16 nodes.

If you require more nodes, delete your Config Controller instance as you can't modify the CIDR block after creation. When you recreate the Config Controller instance, use the optional parameter [`--cluster-ipv4-cidr-block`](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/config/controller/create#--cluster-ipv4-cidr-block) and specify the [`CIDR range or netmask size`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_pods).

### Config Controller-managed cluster(s) not listed in Config Sync dashboard

If you click the Config Sync Dashboard and see no instances, [create an empty fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#optional_create_an_empty_fleet) and assign the Config Controller cluster to that fleet.

### Missing dashboard information

If you don't see any details for Config Controller in the Google Cloud console dashboard, then the default service account used by Config Controller might not have the Google Cloud Observability permissions that it needs.

To grant these permissions, use the following commands:
    
    
    # Cloud Monitoring metrics permissions
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role=roles/monitoring.metricWriter \
        --condition=None \
        --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role=roles/stackdriver.resourceMetadata.writer \
        --condition=None \
        --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role=roles/opsconfigmonitoring.resourceMetadata.writer \
        --condition=None \
        --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    
    # Cloud Logging permissions
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role=roles/logging.logWriter \
        --condition=None \
        --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    
    # Cloud Trace permissions\
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --role=roles/cloudtrace.agent \
        --condition=None \
        --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that you created your Config Controller instance in
  * `PROJECT_NUMBER`: your Google Cloud project number



## Troubleshoot components

Because your Config Controller instance comes pre-installed with Policy Controller, Config Sync, and Config Connector, you might encounter problems with these components. To learn how to troubleshoot these components, see the following pages:

  * [Troubleshoot Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/troubleshoot-policy-controller)
  * [Introduction to troubleshooting Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync)
  * [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting)



The following sections provide advice on some of the more common problems that you might encounter when you use Config Controller with these components.

### Sync errors

The configurations in your source of truth (for example, a Git repository or an OCI image) are synced to your Config Controller instance with Config Sync. Check for errors in this sync process by using the [`nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command) command:
    
    
    nomos status  --contexts $(kubectl config current-context)
    

### Troubleshoot Config Connector resources

#### Immutable fields and resources

Some fields on the underlying Google Cloud resources [are immutable](https://docs.cloud.google.com/config-connector/docs/concepts/reconciliation#resources_will_not_be_recreated_when_modifying_immutable_fields), such as project IDs or the name of your VPC network. [Config Connector](https://docs.cloud.google.com/config-connector/docs) blocks edits to such fields and is unable to actuate changes. If you want to edit one of these immutable fields, you must delete the original resource (through Git) before re-adding it with your preferred values.

#### Stuck resources

Sometimes, resources might fail to delete correctly (as reported by `nomos status`). You can fix this problem by removing the [finalizers](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#finalizers) on the resource and then deleting the resource manually.

For example, to delete an IAMPolicyMember that's stuck, run the following command:
    
    
    kubectl patch IAMPolicyMember logging-sa-iam-permissions \
        -p '{"metadata":{"finalizers":[]}}' --type=merge -n config-control
    kubectl delete IAMPolicyMember logging-sa-iam-permissions -n config-control
    

## What's next

  * If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/get-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
