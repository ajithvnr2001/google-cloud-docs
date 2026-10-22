---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster/
title: Create a cluster \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:29.381428+00:00
---

# Create a cluster  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a cluster

This page explains how to create a cluster and node pool in GKE on Azure on Kubernetes version 1.35.3-gke.300.

## Before you begin

To complete the steps on this page, do the following:

  1. Follow the steps in [Configure prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/prerequisites).

  2. Choose if you will run the control plane in multiple zones or a single zone.

  3. Select classless inter-domain routing (CIDR) ranges to provide to your cluster.




### Control plane zonal placement

By default, GKE on Azure places separate control plane replicas in the same subnet across three zones in your selected region. You can choose these zones and subnets.

If you want to use the default control plane replica placement, skip to Select CIDR ranges for your cluster.

#### Azure NAT gateway and cluster control planes

Each control plane replica also requires connectivity to the Google-hosted management service to operate in a normal state.

If you use Azure NAT gateway to provide outbound connectivity, you must consider how a zonal failure impacts the cluster's control plane. One NAT gateway endpoint is isolated to a single zone or is regional/non-zonal, and this presents a single point of failure.

If you want to place control plane replicas in a single zone, use a single subnet and zone. If you use NAT Gateway for outbound connectivity, make sure that the endpoint is placed in the same zone.

If you want to place replicas in two or three zones, you can pass a list of subnets and zones when you create a cluster. When you pass two subnets and zones, GKE on Azure places two replicas in the first zone provided. When you pass in three subnets and zones, GKE on Azure places replicas in each subnet. For more information, see Place replicas in a specific subnet.

For more information on configuring Azure subnets and zones for high availability, see [Zone isolation with zonal stacks](https://docs.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-gateway-resource#zone-isolation-with-zonal-stacks) in the Azure documentation.

#### Place replicas in a specific subnet

This section is optional.

To control which zones control plane replicas are placed in, you use the [`--replica-placements`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--replica-placements) flag and pass a list of subnet IDs and zones when you create your cluster. You can use up to three subnets and zones where to place the control plane replicas.

To format the list of subnets, perform the following steps.

  1. Retrieve your Azure subnet IDs with the `az` command-line tool:
         
         az network vnet subnet show \
           --resource-group=VNET_RESOURCE_GROUP_NAME --vnet-name=VNET_NAME \
           --name SUBNET_NAME --query "id" -otsv
         

Replace the following:

     * `CLUSTER_RESOURCE_GROUP_NAME`: an existing resource group name where you want to run your cluster
     * `VNET_RESOURCE_GROUP_NAME`: the resource group name that holds your VNet
     * `VNET_NAME`: your VNet name
     * `SUBNET_NAME`: your subnet name

The output is the ID of the subnet. Azure subnet IDs look like the following:
    
    /subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.Network/virtualNetworks/VNET_NAME/subnets/SUBNET_NAME
    

Repeat this command for each subnet where you would like to create a control plane replica in. Copy the subnet IDs into a text editor for the following step.

  2. Create a comma-separated list of subnet IDs and Azure availability zones, with a colon separating the subnet and zone. For example, to create control plane replicas in `subnet1` in zone 1, `subnet2` in zone 2, and `subnet3` in zone 3, you use the following string:
         
         /subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.Network/virtualNetworks/VNET_NAME/subnets/subnet1:1,/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.Network/virtualNetworks/VNET_NAME/subnets/subnet2:2,/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.Network/virtualNetworks/VNET_NAME/subnets/subnet3:3
         

Copy this string and use it as the value for the `--replica-placements` flag when you create a cluster.




### Select CIDR ranges for your cluster

When you create a cluster in GKE on Azure, you need to provide IPv4 address ranges to use for Pods and Services.

These IP ranges are specified using Classless Inter-Domain Routing ([CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing)) notation—for example, `100.64.0.0/16`.

**Note:** After you create a cluster, you can't change these ranges.

### Recommended ranges

We recommend the following CIDR ranges for Services and Pods:

  * Services: 100.64.0.0/16
  * Pods: 100.96.0.0/11



These ranges are large enough for you to grow your cluster without any issues.

The following sections provide more details.

#### Details about selecting ranges

GKE on Azure uses an overlay network for Pods and Services, so the IP ranges for these networks don't need to be routable within the VNet. Any IP ranges that you use must be guaranteed available. For more information, see [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/dataplane-v2).

  * The Pod and Service IP ranges can overlap with the VNet network, provided either doesn't include the control plane or node pool subnet IP ranges.

  * The Pod and Service IP range must fall within one of the following private IP ranges:

    * `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` — Private IP addresses (RFC 1918)
    * `100.64.0.0/10` — Shared address space (RFC 6598)
    * `192.0.0.0/24` — IETF protocol assignments (RFC 6890)
    * `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` — Documentation (RFC 5737)
    * `192.88.99.0/24` — IPv6 to IPv4 relay (deprecated) (RFC 7526)
    * `198.18.0.0/15` — Benchmark testing (RFC 2544)



We recommend IP ranges within `100.64.0.0/10` (RFC 6598). This range is reserved for carrier-grade NAT, which is likely not used in your VNet.

For example, the following is a valid configuration where the Pod, Service, and Node networks don't overlap (the VNet is using RFC 1918 private IP addresses, whereas the Pod and Service networks are overlaid onto RFC 6598 private IPs).

  * VNet network: `10.0.0.0/16`, `172.16.1.0/24`, `172.16.2.0/24`
  * Pod network: `100.65.0.0/16`
  * Service network: `100.66.0.0/16`



The following is also a valid configuration despite the Pod and Service networks overlap with the VNet network since there is no overlap with the control plane replicas.

  * VNet network: `10.0.0.0/16`
  * Pod network: `10.0.1.0/24`
  * Service network: `10.0.2.0/24`
  * Control Plane Replica subnets: `10.0.3.0/24`, `10.0.4.0/24`, `10.0.5.0/24`



The following configuration is _invalid_ , because the Pod IP range overlaps with the control plane network. This overlap might prevent workloads from communicating with the control plane replica in the VNet network:

  * VNet network: `10.0.0.0/16`
  * Pod network: `10.0.1.0/24`
  * Service network: `10.1.0.0/24`
  * Control Plane Replica subnets: `10.0.1.0/24`, `10.0.2.0/24`, `10.0.3.0/24`



#### Details about the Pod address range

Kubernetes allocates addresses to [Pod](https://kubernetes.io/docs/concepts/workloads/pods) objects from the Pod address range. A cluster's Pod range is split into smaller ranges for each node. When a Pod is scheduled on a particular node, Kubernetes assigns a Pod IP address from the node's range.

To calculate the size of the Pod address range, you need to estimate the number of nodes that you want in your cluster and the number of Pods that you want to run on each node.

The following table provides size recommendations for Pod CIDR ranges based on the number of nodes and Pods that you intend to run.

**Pod address ranges table**

Pod address range | Maximum Pod IP addresses | Maximum nodes | Maximum Pods  
---|---|---|---  
/24  
Smallest possible Pod address range | 256 addresses | 1 node | 110 Pods  
/23 | 512 addresses | 2 nodes | 220 Pods  
/22 | 1,024 addresses | 4 nodes | 440 Pods  
/21 | 2,048 addresses | 8 nodes | 880 Pods  
/20 | 4,096 addresses | 16 nodes | 1,760 Pods  
/19 | 8,192 addresses | 32 nodes | 3,520 Pods  
/18 | 16,384 addresses | 64 nodes | 7,040 Pods  
/17 | 32,768 addresses | 128 nodes | 14,080 Pods  
/16  | 65,536 addresses | 256 nodes | 28,160 Pods  
/15 | 131,072 addresses | 512 nodes | 56,320 Pods  
/14 | 262,144 addresses | 1,024 nodes | 112,640 Pods  
  
#### Details about the service address range

Kubernetes allocates virtual IP addresses for [Service objects](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service)— for example, load balancers from this address range.

To calculate the size of the Service address range, you need to estimate the number of services that you want in your cluster.

The following table provides size recommendations for Service CIDR ranges based on the number of Services that you intend to run.

**Service address ranges table**

Service address range | Maximum number of Services  
---|---  
/27  
Smallest possible Service address range | 32 Services  
/26 | 64 Services  
/25 | 128 Services  
/24 | 256 Services  
/23 | 512 Services  
/22 | 1,024 Services  
/21 | 2,048 Services  
/20 | 4,096 Services  
/19 | 8,192 Services  
/18 | 16,384 Services  
/17 | 32,768 Services  
/16  
Largest possible Service address range | 65,536 Services  
  
### Authenticate to Azure

GKE on Azure provides two methods of authenticating to Azure: [workload identity federation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application#workload-identity-federation) and [creating a client certificate](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client). Workload identity federation authentication is the recommended method, because it's simpler and more secure.

#### Workload identity federation

Workload identify federation allows GKE on Azure to authenticate to Azure using a Google service account, in order to subsequently manage resources in the Azure AD application. Compared to AzureClient, you don't need to manage certificates and upload to Azure AD manually.

To configure a federated identity credential on your Azure AD application, run the following commands. Note that you can add up to twenty credentials to each Azure AD application.

  1. Save your Azure application ID to environment variables:
         
         APPLICATION_ID=$(az ad app list --all \
           --query "[?displayName=='APPLICATION_NAME'].appId" --output tsv)
         PROJECT_ID="$(gcloud config get-value project)"
         PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" \
         --format "value(projectNumber)")
         

     * `APPLICATION_NAME`: the Azure AD application name that you used when you [Create an Azure Active Directory Application](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application).
  2. Create a JSON file named `credential.json`.
         
         {
           "name": "CREDENTIAL_NAME",
           "issuer": "https://accounts.google.com",
           "subject": "service-PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com",
           "audiences": ["api://AzureADTokenExchange"],
           "description": "Allow GKE on Azure to authenticate to the Azure AD application using a Google service account."
         }
         

     * `CREDENTIAL_NAME`: the credential name.
     * `PROJECT_NUMBER`: the number of the Google Cloud project that hosts the cluster.
  3. Create a federated identity credential on the Azure AD application:
         
         az ad app federated-credential create --id "${APPLICATION_ID}" --parameters credential.json
         




For more details, see the Azure documentation [Azure AD workload identity federation with Google Cloud](https://blog.identitydigest.com/azuread-federate-gcp/).

You can also provision the Azure federated identity credential using Terraform. For details, see [azuread_application_federated_identity_credential](https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application_federated_identity_credential).

After you configure the credentials, create or select an SSH key pair for your cluster.

### Create an ssh key pair

When you create a cluster, you need to provide an SSH key pair. If you already have a key pair to use, skip this step.

  1. To create a new key pair, use the `ssh-keygen` command-line tool:
         
         ssh-keygen -m PEM -t rsa -b 4096 -f KEY_PATH
         

Replace `KEY_PATH` with the path to your new private key.

  2. Store the key in an environment variable:
         
         SSH_PUBLIC_KEY=$(cat KEY_PATH.pub)
         

For example, to create a new key pair at `~/.ssh/anthos-multicloud-key.pub` and store the public key in an environment variable, run the following command:
         
         ssh-keygen -m PEM -t rsa -b 4096 -f ~/.ssh/anthos-multicloud-key
         SSH_PUBLIC_KEY=$(cat ~/.ssh/anthos-multicloud-key.pub)
         




After you save the public key to an environment variable, you are ready to create a cluster.

### Select your Fleet host project

[Fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets) are a Google Cloud concept to organize clusters into larger groups. With fleets, you can manage multiple clusters across several clouds and apply consistent policies across them. The GKE Multi-Cloud API automatically registers your clusters with a Fleet when the cluster is created.

When you create a cluster, you specify a [Fleet host project](https://docs.cloud.google.com/anthos/multicluster-management/fleets#fleet-host-project) where the cluster will be managed from. Because GKE on Azure uses the cluster name as the Fleet membership name, you must ensure that your cluster names are unique across your Fleet.

**Note:** Once a cluster has been created, you cannot change its Fleet host project.

#### Cross-project registration

If you want to use a Fleet Host project other than the Google Cloud project where the cluster is located, you must apply an additional IAM policy binding to the Multi-Cloud Service Agent service account. This allows the service account to manage Fleets with the Fleet Host Project.

  1. To add the Service Agent to your project, run this command:
         
         gcloud beta services identity create --service=gkemulticloud.googleapis.com \
           --project=CLUSTER_PROJECT_NUMBER
         

Replace `CLUSTER_PROJECT_NUMBER` with your Google Cloud project number.

  2. Assign this binding with the following command:
         
         gcloud projects add-iam-policy-binding FLEET_PROJECT_ID \
           --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com" \
           --role="roles/gkemulticloud.serviceAgent"
         

Replace the following:

     * `FLEET_PROJECT_ID`: your Fleet host project's Google Cloud project
     * `CLUSTER_PROJECT_NUMBER`: your Google Cloud project number



The Multi-Cloud Service Agent account name has the following format: `service-CLUSTER_PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com`.

You can find your service accounts on the Google Cloud console [Service account](https://console.cloud.google.com/iam-admin/serviceaccounts) page. For more information on how to find your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## Create a cluster

To create a cluster, run the following commands:

  1. Save your Azure resource group, VNet, and subnet IDs to environment variables:
         
         SUBSCRIPTION_ID=$(az account show --query "id" --output tsv)
         TENANT_ID=$(az account list \
           --query "[?id=='${SUBSCRIPTION_ID}'].{tenantId:tenantId}" --output tsv)
         CLUSTER_RG_ID=$(az group show --resource-group=CLUSTER_RESOURCE_GROUP_NAME \
           --query "id" -otsv)
         VNET_ID=$(az network vnet show --resource-group=VNET_RESOURCE_GROUP_NAME \
           --name=VNET_NAME --query "id" -otsv)
         SUBNET_ID=$(az network vnet subnet show \
           --resource-group=VNET_RESOURCE_GROUP_NAME --vnet-name=VNET_NAME \
           --name default --query "id" -otsv)
         

Replace the following:

     * `CLUSTER_RESOURCE_GROUP_NAME`: an existing resource group name where you want to run your cluster
     * `VNET_RESOURCE_GROUP_NAME`: the resource group name that holds your VNet
     * `VNET_NAME`: the name of your VNet
  2. Create a cluster with the Google Cloud CLI:

### Workload identity federation
         
         gcloud container azure clusters create CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION \
             --fleet-project FLEET_PROJECT \
             --azure-tenant-id "${TENANT_ID}" \
             --azure-application-id "${APPLICATION_ID}" \
             --azure-region AZURE_REGION \
             --pod-address-cidr-blocks POD_CIDR \
             --service-address-cidr-blocks SERVICE_CIDR \
             --vm-size VM_SIZE \
             --cluster-version 1.35.3-gke.300 \
             --ssh-public-key "$SSH_PUBLIC_KEY" \
             --resource-group-id "$CLUSTER_RG_ID" \
             --vnet-id "$VNET_ID" \
             --subnet-id "$SUBNET_ID" # Optional, see following note \
             --tags "control-plane=CLUSTER_NAME" \
             --admin-users ADMIN_USERS_LIST
         

### Azure client
         
         gcloud container azure clusters create CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION \
             --fleet-project FLEET_PROJECT \
             --client CLIENT_NAME \
             --azure-region AZURE_REGION \
             --pod-address-cidr-blocks POD_CIDR \
             --service-address-cidr-blocks SERVICE_CIDR \
             --vm-size VM_SIZE \
             --cluster-version 1.35.3-gke.300 \
             --ssh-public-key "$SSH_PUBLIC_KEY" \
             --resource-group-id "$CLUSTER_RG_ID" \
             --vnet-id "$VNET_ID" \
             --subnet-id "$SUBNET_ID" # Optional, see following note \
             --tags "control-plane=CLUSTER_NAME" \
             --admin-users ADMIN_USERS_LIST
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster
     * `GOOGLE_CLOUD_LOCATION`: the Google Cloud location that manages your cluster
     * `FLEET_PROJECT` with the [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) host project where the cluster will be registered. If you want to manage this cluster from another Google Cloud project, see Cross-project registration.
     * `AZURE_REGION`: a [supported Azure region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) associated to your Google Cloud region
     * `POD_CIDR`: your cluster's Pod address range— for example, `10.0.1.0/18`
     * `SERVICE_CIDR`: your cluster's Service address range
     * `VM_SIZE`: a [supported Azure VM size](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-vms)
     * `ADMIN_USERS_LIST` (optional): a comma-separated list of email addresses of the users to grant administrative privileges to - for example, "kai@example.com,hao@example.com,kalani@example.com". Defaults to the user creating the cluster
     * `CLIENT_NAME`: your [AzureClient](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client) name
**Note:** When you create a cluster, you can pass the following three optional fields instead of the `--subnet-id` field:  

     * `--endpoint-subnet-id`: the subnet where GKE on Azure deploys the control plane load balancer endpoint. If you don't specify a value, the default is `subnet-id`.
     * `--service-load-balancer-subnet-id`: the subnet where Kubernetes private Service-type load balancers are deployed. If you don't specify a value, the default is `subnet-id`.
     * `--replica-placements`
  3. Check the status of your cluster:
         
         gcloud container azure clusters describe CLUSTER_NAME  --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`
     * `GOOGLE_CLOUD_LOCATION`

The output includes information about the status and configuration of your cluster.




## Authorize Cloud Logging / Cloud Monitoring

**Note:** Starting with Kubernetes version 1.28, manual policy binding to authorize the `gke-system/gke-telemetry-agent` service account for log and metric collection is no longer necessary. The required permissions are now automatically granted to this service account. You can therefore disregard this section.

In order for GKE on Azure to create and upload system logs and metrics to Google Cloud, it must be authorized.

To authorize the Kubernetes workload identity `gke-system/gke-telemetry-agent` to write logs to Google Cloud Logging, and metrics to Google Cloud Monitoring, run this command:
    
    
    gcloud projects add-iam-policy-binding GOOGLE_PROJECT_ID \
      --member="serviceAccount:GOOGLE_PROJECT_ID.svc.id.goog[gke-system/gke-telemetry-agent]" \
      --role=roles/gkemulticloud.telemetryWriter
    

Replace `GOOGLE_PROJECT_ID` with the cluster's Google Cloud project ID.

This IAM binding grants access for all clusters in the Google Cloud project project to upload logs and metrics. You only need to run it after creating your first cluster for the project.

Adding this IAM binding will fail unless at least one cluster has been created in your Google Cloud project. This is because the workload identity pool it refers to (`GOOGLE_PROJECT_ID.svc.id.goog`) is not provisioned until cluster creation.

## Create a node pool

Before you create a node pool, you need the following:

  * Permissions to use the `az` command-line tool to retrieve an Azure subnet ID.
  * Access to the cluster's SSH public key.



To create a node pool, run the following commands:

  1. Save your Azure VNet subnet ID and SSH public key to environment variables:
         
         SUBNET_ID=$(az network vnet subnet show \
           --resource-group=VNET_RESOURCE_GROUP_NAME --vnet-name=VNET_NAME \
           --name default --query "id" -otsv)
         SSH_PUBLIC_KEY=$(cat KEY_PATH.pub)
         

Replace the following:

     * `VNET_RESOURCE_GROUP_NAME`: the resource group name that holds VNet
     * `VNET_NAME`: the name of your VNet
     * `KEY_PATH`: the path to your key pair
  2. Create a node pool with the Google Cloud CLI:
         
         gcloud container azure node-pools create NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION \
             --node-version 1.35.3-gke.300 \
             --vm-size VM_SIZE \
             --max-pods-per-node 110 \
             --min-nodes MIN_NODES \
             --max-nodes MAX_NODES \
             --ssh-public-key "${SSH_PUBLIC_KEY}" \
             --subnet-id "${SUBNET_ID}"
         

Replace the following:

     * `NODE_POOL_NAME`: a unique name for your node pool—for example, `node-pool-1`
     * `CLUSTER_NAME`: the name of your GKE on Azure cluster
     * `GOOGLE_CLOUD_LOCATION`: the [Google Cloud location](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster
     * `VM_SIZE`: a [supported Azure VM size](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-vms)
     * `MIN_NODES`: the minimum number of nodes in the node pool—for more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler)
     * `MAX_NODES`: the maximum number of nodes in the node pool
  3. Check the status of your node pool:
         
         gcloud container azure node-pools describe NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `NODE_POOL_NAME`: a unique name for your node pool—for example, `node-pool-1`
     * `CLUSTER_NAME`: the name of your GKE on Azure cluster
     * `GOOGLE_CLOUD_LOCATION`: the [Google Cloud location](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster

The output includes the status of your node pool, including if it is `PROVISIONING` or `RUNNING`.




## What's next

  * [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-cluster-access-for-kubectl).
  * [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool).
  * Try the [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/quickstart) to launch your first workload.
  * Read the reference documentation for [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create).
  * Had a problem creating a cluster? See [Troubleshooting](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshooting) for more information.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
