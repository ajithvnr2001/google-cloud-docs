---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configuring-privately-used-public-ips-for-gke/
title: Configuring privately used public IP addresses for GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:16.023751+00:00
---

# Configuring privately used public IP addresses for GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configuring-privately-used-public-ips-for-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configuring privately used public IP addresses for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows how to apply privately used public IP (PUPI) addresses to Google Kubernetes Engine (GKE) Pod address blocks.

Privately Used Public IP (PUPIs) addresses are addresses that you can use privately within your Google Cloud Virtual Private Cloud (VPC) network. These IP addresses are not owned by Google. You don't need to own these public IP addresses to use them privately.

## Overview

GKE clusters require dedicated IP address ranges for nodes, Pods, and Services. As your infrastructure grows, you might face exhaustion of the standard internal IP address space (RFC 1918). One way to mitigate private RFC 1918 address exhaustion is to use privately used public IP (PUPI) addresses for the [GKE Pod CIDR block](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#internal_ip_addresses). PUPIs provide an alternative for your GKE Pod network, reserving private IP addresses for other cluster components.

**Single Cluster** : If you're only creating one GKE cluster, you can enable PUPIs by [enabling privately used external IP address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_pupis).

**Multiple Clusters** : If you're working with multiple GKE clusters connected through VPC peering (a common scenario for service providers), you'll need a more complex configuration. The following diagram shows an example of how a company (producer) offers a managed service using PUPI with VPC-peering to a customer (consumer).

![PUPI addresses for the GKE Pod CIDR
block.](https://docs.cloud.google.com/static/kubernetes-engine/images/configuring-privately-used-public-ips-for-GKE-pupi-addresses.png)

The preceding diagram involves the following considerations:

  * **Primary CIDR block** : A non-PUPI CIDR block that is used for nodes and internal load balancer (ILB) and must be non-overlapping across VPCs.
  * **Producer secondary CIDR block** : A PUPI CIDR block that is used for Pods (for example, `45.45.0.0/16`).
  * **Consumer secondary CIDR block** : Any other PUPI CIDR block on the customer side (for example, `5.5.0.0/16`).



**How PUPIs are used in a Service provider scenario**

The service provider (producer) runs their managed service on a GKE cluster (gke-2) within their VPC (`vpc-producer`). This cluster uses the PUPI range `45.0.0.0/8` for its Pod IP addresses.

The customer (consumer) also has a GKE cluster (gke-1) in their own VPC (`vpc-consumer`), using a different PUPI range, `5.0.0.0/8`, for its Pod IP addresses.

These two VPCs are connected using VPC peering, but each continues to use standard private IP addresses (RFC 1918) for nodes, services, and internal load balancers.

**Ensure communication between VPCs**

  * **Consumer to Producer** : By default, the consumer's VPC automatically shares its RFC 1918 routes (but not PUPIs) with the producer. This allows resources in the consumer's VPC to access services in the producer's VPC (typically through internal load balancers).
  * **Producer to Consumer** : For the producer's Pods to reach resources in the consumer's VPC, explicit configuration is needed.
  * **No Overlap** : The producer and consumer must ensure that the consumer's PUPI range doesn't conflict with any IP addresses used in the producer's VPC.
  * **Export/Import** : The producer must enable export of its PUPI routes, and the consumer must enable import of those routes over the peering connection.



**Enable communication when PUPI ranges overlap**

If the consumer's VPC already uses the same PUPI range as the producer, direct communication from producer Pods isn't possible. Instead, the producer can enable IP address masquerading, where the Pod IP addresses are hidden behind the producer's node IP addresses.

**Note:** PUPIs don't support Service networking.

The following table shows the default import and export settings for each VPC. You can modify default VPC peering settings by using the `gcloud compute networks peerings update` command.

VPC Network | Import settings | Export settings | Notes  
---|---|---|---  
Producer | Default behavior (turned off): Does not import subnet routes with public IP addresses  
To turn on: --import-subnet-routes-with-public-ip (through peering) | Default behavior (turned on): Exports subnet routes with public IP addresses  
To turn off: --no-export-subnet-routes-with-public-ip (through peering) | Flags controlled through service networking.  
Consumer | Turned off (default) | Turned on (default) | Typically managed by the customer, not required to be modified through service networking  
  
These settings result in the following:

  * The producer VPC sees all the customer routes.
  * The consumer VPC doesn't see the PUPI routes configured on the Pod subnet in the producer VPC.
  * Traffic originating from the producer Pods to the `vpc-consumer` network must be translated behind the node addresses in the producer cluster.



## Prerequisites

To establish successful communication between VPC Pods and another VPC, ensure the following prerequisites and configurations are met:

  * Your GKE cluster must meet the following minimum version requirements: 
    * Autopilot clusters: GKE version 1.22 or later
    * Standard clusters: GKE version 1.14 or later
  * Select a PUPI range that is not publicly routable or owned by Google.
  * Ensure that the node IP addresses and the primary IP address range of both VPCs don't overlap.
  * If you require direct Pod-to-Pod communication between the customer VPC and the managed service, follow these steps: 
    * Autopilot clusters: Configure SNAT for PUPI to ensure Pod-to-Pod communication. You don't require additional configuration.
    * Standard clusters: Translate Pod IP addresses to their corresponding node IP addresses using SNAT. Enable SNAT for PUPI traffic. For more information, see [Enable privately used external IP address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_pupis).



## Configure privately used public IP addresses for GKE clusters

To configure PUPI addresses for GKE clusters:

  1. Configure two Virtual Private Cloud networks.
  2. Configure one subnet inside each Virtual Private Cloud network.
  3. Configure a PUPI address range on a secondary address range in each subnet.
  4. Establish a Virtual Private Cloud peering relationship between the two Virtual Private Cloud networks with proper import and export settings.
  5. Inspect the routes within each Virtual Private Cloud.



## Costs

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/kubernetes-engine/pricing#pricing_calculator).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Use VPC-native clusters only.

  * Setup the required IPAM specifications for [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering#specifications).




## Set up Networks and clusters

  1. Create VPC networks:

Create the following two VPC networks with RFC-1918 as primary ranges for nodes and PUPI ranges for Pods. Assign primary IP address ranges from the RFC 1918 private address space (for example, `10.x.x.x`, `172.16.x.x`, or `192.168.x.x`) to both VPCs. These ranges are typically used for the worker nodes within your GKE clusters. In addition to the internal IP address ranges, designate separate ranges of Privately Used Public IP addresses (PUPIs) for each VPC. These PUPI ranges are used exclusively for the Pod IP addresses within their corresponding GKE clusters.

     * **Consumer VPC network** : This VPC hosts the GKE cluster where the consumer's applications or workloads run. You can use configuration similar to the following:
           
           Network: consumer
           Subnetwork: consumer-subnet
           Primary range: 10.129.0.0/24
           Service range name and cidr: consumer-services, 172.16.5.0/24
           Pod range name and cidr: consumer-pods, 5.5.5.0/24
           Cluster name: consumer-cluster
           

     * **Producer VPC network** : This VPC hosts the GKE cluster responsible for providing the service that the consumer uses. You can use configuration similar to the following:
           
           Network: producer
           Subnetwork: producer-subnet
           Primary range: 10.128.0.0/24
           Service range name and cidr: producer-services, 172.16.45.0/24
           Pod range name and cidr: producer-pods, 45.45.45.0/24
           Cluster name: producer-cluster
           

For more information on creating VPC networks, see [Create VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).

  2. With the VPC networks and subnets created with PUPI ranges in the preceding step, you can create two GKE clusters (`producer` and `consumer`). 

**Note:** PUPI ranges are only supported as secondary IP address ranges for the Pod network in GKE and cannot be used for the primary IP address range (used by nodes and Services).
     1. Create `producer` clusters with the producer network and subnet as follows:
            
            gcloud container clusters create PRODUCER_CLUSTER_NAME \
                --location=PRODUCER_CONTROL_PLANE_LOCATION \
                --enable-ip-alias \
                --network=PRODUCER_NETWORK_NAME \
                --subnetwork=PRODUCER_SUBNETWORK_NAME \
                --cluster-secondary-range-name=PRODUCER_PODS \
                --services-secondary-range-name=PRODUCER_SERVICES \
                --num-nodes=1 \
                --project=PRODUCER_PROJECT_ID
            

Replace the following:

        * `PRODUCER_CLUSTER_NAME`: the name of the GKE producer cluster.
        * `PRODUCER_CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your producer cluster. Provide a region for regional clusters, or a zone for zonal clusters.
        * `PRODUCER_NETWORK_NAME`: the name of an existing producer VPC network.
        * `PRODUCER_SUBNETWORK_NAME`: the name of an existing subnet. The subnet's primary IP address range is used for nodes. The subnet must exist in the same region as the one used by the cluster. If omitted, GKE attempts to use a subnet in the `default` VPC network in the cluster's region.
        * `PRODUCER_PODS`: the name of an existing secondary IP address range in `PRODUCER_SUBNETWORK_NAME` that GKE uses for the cluster's Pods.
        * `PRODUCER_SERVICES`: the name of an existing secondary IP address range in `PRODUCER_SUBNETWORK_NAME` that GKE uses for the cluster's Services.
        * `PRODUCER_PROJECT_ID`: the ID of the producer project.
     2. Create `consumer` clusters with the consumer network and subnet as follows:
            
            gcloud container clusters create CONSUMER_CLUSTER_NAME \
                --location=CONSUMER_CONTROL_PLANE_LOCATION \
                --enable-ip-alias \
                --network=CONSUMER_NETWORK_NAME \
                --subnetwork=CONSUMER_SUBNETWORK_NAME \
                --cluster-secondary-range-name=CONSUMER_PODS \
                --services-secondary-range-name=CONSUMER_SERVICES \
                --num-nodes=1 \
                --project=CONSUMER_PROJECT_ID
            

Replace the following:

        * `CONSUMER_CLUSTER_NAME`: the name of the GKE consumer cluster.
        * `CONSUMER_CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your consumer cluster. Provide a region for regional clusters, or a zone for zonal clusters.
        * `CONSUMER_NETWORK_NAME`: the name of an existing consumer VPC network.
        * `CONSUMER_SUBNETWORK_NAME`: the name of an existing subnet. The subnet's primary IP address range is used for nodes. The subnet must exist in the same region as the one used by the cluster. If omitted, GKE attempts to use a subnet in the `default` VPC network in the cluster's region.
        * `CONSUMER_PODS`: The name of an existing secondary IP address range in `CONSUMER_SUBNETWORK_NAME` that GKE uses for the cluster's Pods.
        * `CONSUMER_SERVICES`: The name of an existing secondary IP address range in `CONSUMER_SUBNETWORK_NAME` that GKE uses for the cluster's Services.
        * `CONSUMER_PROJECT_ID`: the ID of the consumer project.

For more information on creating clusters, see [Creating clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#creating_a_cluster_in_your_first_service_project).

  3. Establish the [VPC peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#gcloud) relationship between the consumer-vpc network and the producer-vpc network as follows:

     * To connect `consumer` network to producer, run the following command:
           
           gcloud compute networks peerings create CONSUMER_PEERING_NAME \
               --project=CONSUMER_PROJECT_ID \
               --network=CONSUMER_NETWORK_NAME \
               --peer-network=PRODUCER_NETWORK_NAME
           

Replace `CONSUMER_PEERING_NAME` with name of the peering to be added to the consumer network.

     * To connect `producer` network to consumer, run the following command:
           
           gcloud compute networks peerings create PRODUCER_PEERING_NAME \
               --project=PRODUCER_PROJECT_ID \
               --network=PRODUCER_NETWORK_NAME \
               --peer-network=CONSUMER_NETWORK_NAME \
               --no-export-subnet-routes-with-public-ip \
               --import-subnet-routes-with-public-ip
           

Replace `PRODUCER_PEERING_NAME` with the name of the peering to be added to the producer network.

By default, the consumer VPC exports the PUPI addresses. When you create the producer VPC, you use the following arguments to configure the VPC to import PUPI addresses but not export them:
    
    --no-export-subnet-routes-with-public-ip
    --import-subnet-routes-with-public-ip
    




### Verify the networks and subnetworks

  1. Verify the producer network:
         
         gcloud compute networks describe PRODUCER_NETWORK_NAME \
             --project=PRODUCER_PROJECT_ID
         

The output is similar to the following:
         
         ...
         kind: compute#network
         name: producer
         peerings:
         - autoCreateRoutes: true
           exchangeSubnetRoutes: true
           exportCustomRoutes: false
           exportSubnetRoutesWithPublicIp: false
           importCustomRoutes: false
           importSubnetRoutesWithPublicIp: true
           name: producer-peer-consumer
         …
         

  2. Verify the producer subnetwork:
         
         gcloud compute networks subnets describe PRODUCER_SUBNETWORK_NAME \
             --project=PRODUCER_PROJECT_ID\
             --region=PRODUCER_CONTROL_PLANE_LOCATION
         

The output is similar to the following:
         
         ...
         ipCidrRange: 10.128.0.0/24
         kind: compute#subnetwork
         name: producer-subnet
         …
         secondaryIpRanges:
         - ipCidrRange: 172.16.45.0/24
           rangeName: producer-services
         - ipCidrRange: 45.45.45.0/24
           rangeName: producer-pods
         …
         

  3. Verify the consumer network:
         
         gcloud compute networks describe CONSUMER_NETWORK_NAME \
             --project=CONSUMER_PROJECT_ID
         

The output is similar to the following:
         
         ...
         kind: compute#network
         name: consumer
         peerings:
         - autoCreateRoutes: true
           exchangeSubnetRoutes: true
           exportCustomRoutes: false
           exportSubnetRoutesWithPublicIp: true
           importCustomRoutes: false
           importSubnetRoutesWithPublicIp: false
           name: consumer-peer-producer
         ...
         

  4. Verify the consumer subnetwork:
         
         gcloud compute networks subnets describe CONSUMER_SUBNETWORK_NAME \
             --project=CONSUMER_PROJECT_ID\
             --region=CONSUMER_CONTROL_PLANE_LOCATION
         

The output is similar to the following:
         
         ...
         ipCidrRange: 10.129.0.0/24
         kind: compute#subnetwork
         name: consumer-subnet
         ...
         secondaryIpRanges:
         - ipCidrRange: 172.16.5.0/24
           rangeName: consumer-services
         - ipCidrRange: 5.5.5.0/24
           rangeName: consumer-pods
         ...
         




### Verify GKE cluster and its resources

  1. Get the consumer cluster credentials:
         
         gcloud container clusters get-credentials CONSUMER_CLUSTER_NAME \
             --project=CONSUMER_PROJECT_ID \
             --location=CONSUMER_CONTROL_PLANE_LOCATION
         

The output is similar to the following:
         
         ...
         Fetching cluster endpoint and auth data.
         kubeconfig entry generated for consumer-cluster.
         ...
         

  2. [Install and verify the helloapp](https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-helloapp-deployment).

Alternately, you can save the following manifest as `deployment.yaml`:
         
         kubectl apply -f - <<'EOF'
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: helloweb
           labels:
             app: hello
         spec:
           selector:
             matchLabels:
               app: hello
               tier: web
           template:
             metadata:
               labels:
                 app: hello
                 tier: web
             spec:
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 ports:
                 - containerPort: 8080
                 resources:
                   requests:
                     cpu: 200m
         EOF
         

  3. Apply the manifest to your cluster:
         
         kubectl apply -f deployment.yaml
         

  4. Verify the `helloweb` deployment:
         
         kubectl get deployment helloweb
         

The output is similar to the following:
         
         ...
         NAME       READY   UP-TO-DATE   AVAILABLE   AGE
         helloweb   1/1     1            1           10s
         ...
         




## Verifying the solution

  1. Validate that you successfully created VPC peering:
         
         gcloud compute networks peerings list
         

The output is similar to the following, which shows peerings that are named consumer and producer:
         
         NAME                                     NETWORK    PEER_PROJECT                PEER_NETWORK                            STACK_TYPE  PEER_MTU  IMPORT_CUSTOM_ROUTES  EXPORT_CUSTOM_ROUTES  STATE   STATE_DETAILS
         consumer-peer-producer                   consumer   <project_name>             producer                                IPV4_ONLY   1460      False                 False                 ACTIVE  [2023-08-07T13:14:57.178-07:00]: Connected.
         producer-peer-consumer                   producer   <project_name>             consumer                                IPV4_ONLY   1460      False                 False                 ACTIVE  [2023-08-07T13:14:57.178-07:00]: Connected.
         

  2. Validate that the consumer VPC exports PUPI routes:
         
         gcloud compute networks peerings list-routes CONSUMER_PEERING_NAME \
             --direction=OUTGOING \
             --network=CONSUMER_NETWORK_NAME \
             --region=CONSUMER_CONTROL_PLANE_LOCATION
         

The output is similar to the following, which shows all three consumer CIDR blocks:
         
         DEST_RANGE     TYPE                  NEXT_HOP_REGION  PRIORITY  STATUS
         10.129.0.0/24  SUBNET_PEERING_ROUTE  us-central1      0         accepted by peer
         172.16.5.0/24  SUBNET_PEERING_ROUTE  us-central1      0         accepted by peer
         5.5.5.0/24     SUBNET_PEERING_ROUTE  us-central1      0         accepted by peer
         

  3. Validate the PUPI routes that the producer VPC imported:
         
         gcloud compute networks peerings list-routes PRODUCER_PEERING_NAME \
             --direction=INCOMING \
             --network=PRODUCER_NETWORK_NAME \
             --region=PRODUCER_CONTROL_PLANE_LOCATION
         

The output is similar to the following, which shows all three consumer CIDR blocks:
         
         DEST_RANGE     TYPE                  NEXT_HOP_REGION  PRIORITY  STATUS
         10.129.0.0/24  SUBNET_PEERING_ROUTE  us-central1      0         accepted
         172.16.5.0/24  SUBNET_PEERING_ROUTE  us-central1      0         accepted
         5.5.5.0/24     SUBNET_PEERING_ROUTE  us-central1      0         accepted
         

  4. Validate that the GKE Pods have a PUPI address:
         
         kubectl get pod -o wide
         

The output is similar to the following, which shows that the IP addresses of the Pods fall within the 5.5.5/24 range.
         
         NAME                        READY   STATUS    RESTARTS   AGE   IP         NODE                                              NOMINATED NODE   READINESS GATES
         helloweb-575d78464d-xfklj   1/1     Running   0          28m   5.5.5.16   gke-consumer-cluster-default-pool-e62b6542-dp5f   <none>           <none>
         




## What's next

  * Read the [Configuring private service access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) guide.
  * Read the [Getting started with the Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) guide.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://cloud.google.com/architecture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
