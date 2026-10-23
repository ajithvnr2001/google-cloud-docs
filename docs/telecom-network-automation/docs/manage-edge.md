---
url: https://docs.cloud.google.com/telecom-network-automation/docs/manage-edge/
title: Manage GDC Edge infrastructure \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:21.536875+00:00
---

# Manage GDC Edge infrastructure  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/manage-edge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Manage GDC Edge infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

This page covers managing GDC blueprints and deployments, and creating and deleting a GDC cluster.

## GDC Workload cluster blueprint

The GDC Workload cluster blueprint contains custom resources you can combine to specify the intent to deploy a GDC cluster. For an example Workload cluster custom resource definition, see [Example `WorkloadCluster` CRD](https://docs.cloud.google.com/telecom-network-automation/docs/example-crds#example-workload-cluster-crd).

The following list defines the role of each custom resource:

  * **WorkloadCluster** : creates a local control plane based GDC cluster with one node pool and VPN Connection between the created GDC cluster and Telecom Network Automation Orchestration cluster's VPC.

  * **ClusterInit** : initializes the cluster's lifecycle that Telecom Network Automation manages. This lifecycle includes installing Telecom Network Automation components on the GDC cluster required for the lifecycle management.

  * **SourceRepoRepository and Repository** : sets up the GitOps pipeline for the created GDC cluster using Cloud Source Repository and Porch along with ConfigSync, installed from the previous resource.

  * **ComputeFirewall** : creates a firewall rule in the Telecom Network Automation Orchestration cluster's VPC to allow for TCP ingress traffic on port 3000 that comes from the same IP address range used as the GDC Cluster's pod address range.

  * **ImagePull** : sets up the required credentials on the GDC cluster for `kubelet` to pull images from the artifact registry.




When creating a deployment you can customize the blueprint using following parameters in the `setters.yaml` file:

Parameter | Description  
---|---  
`project-id` | The ID of the target Google Cloud project where the  
| Telecom Network Automation. orchestration cluster is created.  
`cluster-name` | A unique name that identifies a given cluster. This name must be unique across all deployments.  
`username` | The name of the user account within the target Google Cloud project authorized to modify cluster resources.  
`cluster-ipv4-cidr-blocks` | The IPv4 CIDR block for Kubernetes Pods that run on the cluster.  
`services-ipv4-cidr-blocks` | The IPv4 CIDR block for Kubernetes Services that run on the cluster  
`cluster-location` | The Google Cloud region where you want to create the cluster.  
`nodepool-name` | A unique name that identifies the node pool. This name must be unique across all deployments.  
`node-count` | The number of nodes you want the node pool to hold.  
`scale-down-grace-period-seconds` | Specifies the time period in seconds to wait for the NF workloads to migrate from the nodes being removed during scale down. For example, `node-count` is reduced during an update. This process is to ensure a non-disruptive scale down of the cluster. **Note** : This profcessis only applicable when the NF workloads are using the required pod label, `infra.tna.cloud.google.com/nf-workload`, for Telecom Network Automation to identify the critical NF workloads.  
`edge-zone-name` | The name of the target GDC zone. This zone must be in the region specified in `cluster-location`.  
`vpn-connection-name` | A unique name that identifies the VPN connection. This name must be unique across all deployments.  
`vpc-name` | The VPC network name of the  
| Telecom Network Automation Orchestration cluster. If you opted for **Enable management config** during the Orchestration cluster creation, this must be the VPC network name. Otherwise, the default VPC network that Telecom Network Automation creates is `tnavpc-01`.  
`nat-gateway-ip` | The NAT gateway IP address for the target cluster  
`image-registry-server` | The image registry server where GDC workload images are stored. The images are stored in `us-central1-docker.pkg.dev`.  
`control-plane-node-count` | The number of nodes to run the local control plane workloads. Valid values are `3` for high availability and `1` for standard operation.  
`control-plane-shared-deployment-policy` | Specifies whether application workloads can run on the nodes that run the local control plane workloads. Valid values are `DISALLOWED` and `ALLOWED`.  
`external-lb-ipv4-address-pools` | A comma-delimited list of IPv4 addresses, address ranges, or subnetworks for ingress traffic on services that run behind the GDC load balancer. The range must belong to the load balancer IP subnet pool mentioned during the rack turnup.  
`targetVersion` | Specifies the GDC software version that you want this cluster to run in the format 1.X.Y where X is the minor version, and Y is the patch version. For example 1.5.0.  
  
## GDC blueprints

### Create a blueprint

  1. From the navigation menu, click **Blueprints**.
  2. In the drop-down menu, select your preferred Orchestration cluster.
  3. Click **Import from Library**.
  4. Select the blueprint, **GDCE Workload cluster blueprint**.
  5. Click **Add Blueprint**.
  6. On the next screen, specify an appropriate name. For example, `workloadcluster1` for the GDC cluster blueprint.
  7. Optionally, add any labels.
  8. Afterwards, click **Create**.
  9. The blueprint appears in the **Draft Blueprints** list.



### Edit a blueprint

  1. From the navigation menu, click **Blueprints** **> Drafts Blueprint**.
  2. Select your preferred blueprint. A blueprint editor appears.
  3. Edit the blueprint. Any changes to the particular blueprint at the current stage are discouraged.



### Propose a blueprint

  1. From the navigation menu, click **Blueprints >** **Drafts Blueprint**.
  2. Select your preferred blueprint. A blueprint editor appears.
  3. Click **Propose**. The status of the blueprint updates to **Proposed**.



### Approve a blueprint

  1. From the navigation menu, click **Blueprints**.
  2. In your preferred blueprint, click **Action**.
  3. Select **Approve**. The blueprint appears in **Approved Blueprints**.



## GDC deployment

### Create a blueprint deployment

  1. From the navigation menu, click **Blueprints > **Approved Blueprints**.
  2. Select the name of your preferred blueprint.
  3. Click **Create Deployment**.
  4. Provide a name for the deployment. For example, `workloadcluster1-deploy1`.
  5. Click **Create Deployment**. The deployment appears in **Draft Deployment**.



### Edit a blueprint deployment

  1. From the navigation menu, click **Blueprints**.
  2. Select the name of your preferred deployment. A deployment editor appears.
  3. Edit the `setters.yaml` file. 
     1. Note: Ensure you carefully edit the fields and make the necessary changes to the values. For a description of these fields, see GDC Workload cluster blueprints.
  4. Click "Save File".



### Apply a blueprint deployment

  1. From the navigation menu, click **Blueprints**.
  2. Select the name of your preferred deployment. A deployment editor appears.
  3. Click **Deploy**. A dialog appears.
  4. In the dialog, click **Deploy**. The deployment appears in **Applied Deployment**.

**Note:** The GDC cluster name must be less than 15 characters, and have a unique cluster name for each blueprint deployment. Deleting a GDC blueprint deployment does not make the cluster name reusable.

### Scale up and down GDC cluster

  1. From the navigation menu, click **Blueprints > Applied Deployments**.
  2. Select your preferred deployment.
  3. Click **View**.
  4. Click **Edit Deployment**.
  5. Increase or decrease the `node-count` value from the `setters.yaml` file. When decreasing `node-count` set the `scale-down-grace-period-seconds` field to let NF workloads to migrate from the node being removed before scaling down.
  6. Click **Save File**. The deployment appears in **Draft Deployment**.
  7. Navigate to **Deployments**.
  8. In **Draft Deployment** , select the name of your preferred deployment. A deployment editor appears.
  9. Click **Deploy**.
  10. Confirm the deployment. The deployment appears in **Applied Deployment**.



### Delete GDC cluster

  1. From the navigation menu, click **Blueprints.**
  2. From the drop-down menu, Select your preferred Orchestration cluster.
  3. Click **Applied Deployment**.
  4. Click the **Action** icon for the deployment.
  5. Click **Delete**. A confirmation dialog appears.
  6. Confirm the deletion by clicking **Delete**.



The deletion process might complete in up to 30 minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
