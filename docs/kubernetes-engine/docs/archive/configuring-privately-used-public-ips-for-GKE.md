---
url: https://docs.cloud.google.com/kubernetes-engine/docs/archive/configuring-privately-used-public-ips-for-GKE/
title: Configuring privately used public IPs for GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:52.277107+00:00
---

# Configuring privately used public IPs for GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/archive/configuring-privately-used-public-ips-for-GKE/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Configuring privately used public IPs for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2022-12-19 UTC

Standard 

**Warning:** This page is **archived** and is not actively maintained. The commands on this page might not work and could cause disruptions to your cluster.

This tutorial shows how to apply privately used public IP (PUPI) addresses to Google Kubernetes Engine (GKE) Pod address blocks. Service consumer organizations that are IPv4-address constrained can use PUPI addresses in service producer virtual private clouds (VPCs) as an address-management option.

This document is intended for network architects and GKE system administrators whose companies offer managed services over a GKE infrastructure on Google Cloud.

## Introduction

Some companies want to deliver managed services to their customers over Kubernetes or GKE clusters on Google Cloud. However, Kubernetes can require many IP addresses for its various components. For some organizations, meeting this requirement is difficult or impossible because they're unable to assign appropriately sized `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` (RFC 1918) [Classless Inter-domain Routing (CIDR) blocks](https://tools.ietf.org/html/rfc4632).

One way to mitigate address exhaustion is to use privately used public IP (PUPI) addresses for the GKE Pod CIDR block. PUPIs are any public IP addresses not owned by Google that a customer can use privately on Google Cloud. The customer doesn't necessarily own these addresses.

The following diagram shows a company (producer) that offers a managed service to a customer (consumer).

![PUPI addresses for the GKE Pod CIDR block.](https://docs.cloud.google.com/static/architecture/images/configuring-privately-used-public-ips-for-GKE-pupi-addresses.svg)

This setup involves the following considerations:

  * **Primary CIDR block:** A non-PUPI CIDR block that is used for nodes and ILB and must be non-overlapping across VPCs.
  * **Producer secondary CIDR block:** A PUPI CIDR block that is used for Pods (for example, `45.45.0.0/16`).
  * **Consumer secondary CIDR block:** Any other PUPI CIDR block on the customer side (for example, `5.5/16`).



The company's managed service is in the producer VPC (`vpc-producer`) and is built on a GKE deployment. The company's GKE cluster uses the PUPI `45.0.0.0/8` CIDR block for Pod addresses. The customer's applications are located in the consumer VPC (`vpc-consumer`). The customer also has a GKE installation. The GKE cluster in the consumer VPC uses the PUPI `5.0.0.0/8` CIDR block for Pod addresses. The two VPCs are peered with one another. Both VPCs use the RFC 1918 address space for node, service, and load balancing addresses.

By default, the consumer VPC (`vpc-consumer`) exports all RFC 1918 to the producer VPC (`vpc-producer`). Unlike RFC 1918 private addresses and extended private addresses (CGN, Class E), PUPIs aren't automatically advertised to VPC peers by default. If the `vpc-consumer` Pods must communicate with `vpc-producer`, the consumer must enable the VPC peering connection to export PUPI addresses. Likewise, the producer must configure the producer VPC to import PUPI routes over the VPC peering connection.

The `vpc-consumer` address space that is exported into `vpc-producer` must not overlap with any RFC 1918 or PUPI address used in `vpc-producer`. The producer must inform the consumer what PUPI CIDR blocks the managed service uses and ensure that the consumer isn't using these blocks. The producer and consumer must also agree and assign non-overlapping address space for internal load balancing (ILB) and node addresses in `vpc-producer`.

**Note:** PUPIs don't support service networking.

In most cases, resources in `vpc-consumer` communicate with services in `vpc-producer` through ILB addresses in the producer cluster. If the producer Pods are required to initiate communication directly with resources in `vpc-consumer`, and PUPI addressing doesn't overlap, then the producer must configure the producer VPC to export the PUPI routes over the VPC peering connection. Likewise, the consumer must configure the VPC peering connection to import routes into `vpc-consumer`. If the consumer VPC already uses the PUPI address, then the producer should instead configure the IP masquerade feature and hide the Pod IP addresses behind the producer node IP addresses.

The following table shows the default import and export settings for each VPC. You can modify default VPC peering settings by using the [`gcloud compute networks peerings update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/update) Google Cloud CLI command.

PUPI flag | Import | Export  
---|---|---  
Producer side (flags controlled through service networking) | To turn on: `--import-subnet-routes-with-public-ip` (through peering) Default behavior: Turned off | To turn off: `--no-export-subnet-routes-with-public-ip` (through peering) Default behavior: Turned on  
Consumer side (owned by customer, not required to be modified through service networking) | Turned off (default) | Turned on (default)  
  
These settings result in the following:

  * The producer VPC sees all the customer routes.
  * The consumer VPC doesn't see the PUPI routes configured on the Pod subnet in the producer VPC.
  * Traffic originating from the producer Pods to the `vpc-consumer` network must be translated behind the node addresses in the producer cluster.



## Qualifications

  * The address range that you select for a PUPI can't be reachable through the internet or be an address that Google owns.
  * The Node IPs and primary range need to be non-overlapping between the two VPCs.
  * If direct Pod-to-Pod communication is required between the customer VPC and the managed service, then the producer Pod IP addresses must be translated behind their corresponding Node IPs.



## Objectives

  * Configure two VPC networks.
  * Configure one subnet inside each VPC network.
  * Configure a PUPI address range on a secondary address range in each subnet.
  * Establish a VPC peering relationship between the two VPC networks with proper import and export settings.
  * Inspect the routes within each VPC.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

You complete most of this tutorial from the Cloud Shell terminal using HashiCorp's Terraform and the gcloud CLI.

  2. Clone the GitHub repository and change to the local working directory:
         
         git clone https://github.com/GoogleCloudPlatform/terraform-vpc-pupi $HOME/pupi
         

The repository contains all the files that you need to complete this tutorial. For a complete description of each file, see the `README.md` file in the repository.

  3. Make all shell scripts executable:
         
         sudo chmod 755 $HOME/pupi/*.sh
         




## Preparing your environment

In this section, you install and set up Terraform, and then you set environment variables.

### Set up Terraform

  1. Install Terraform by following the [steps in the HashiCorp documentation](https://learn.hashicorp.com/terraform/getting-started/install.html).
  2. In Cloud Shell, initialize Terraform:
         
         cd $HOME/pupi
         terraform init
         

The output is similar to the following:
         
         ...
         Initializing provider plugins...
         The following providers do not have any version constraints in
         configuration, so the latest version was installed.
         ...
         Terraform has been successfully initialized!
         ...
         

As Terraform initializes, it logs progress messages. At the end of the message output, you see a message that Terraform initialized successfully.




### Set environment variables

  1. In Cloud Shell, set the `TF_VAR_org_id` variable:
         
         export TF_VAR_org_id=$(gcloud organizations list | \
             awk '/YOUR_ORGANIZATION_NAME/ {print $2}')

Replace the following:

     * `YOUR_ORGANIZATION_NAME`: the Google Cloud organization name that you want to use for this tutorial
  2. Verify that you set the environment variable correctly:
         
         echo $TF_VAR_org_id
         

The output lists your numeric organization ID and looks similar to the following:
         
         ...
         123123123123
         ...
         

  3. Set the remaining environment variables:
         
         source $HOME/pupi/set_variables.sh
         

This shell script sets basic parameters such as the Google Cloud region, organization ID, and project ID as variables in the shell environment. Terraform uses these variables to configure your Google Cloud resources. You can adjust or change the parameters in the shell script to fit your environment. For a full list of variables, review the `set_variables` shell script.

  4. Verify that you set the environment variables correctly:
         
         env | grep TF_
         

The output is similar to the following:
         
         ...
         TF_VAR_billing_account=QQQQQQ-XAAAAA-E8769
         TF_VAR_org_id=406999999999
         TF_VAR_region1=us-west1
         TF_VAR_region2=us-west2
         TF_VAR_consumer_ilb_ip=10.129.0.200
         TF_VAR_user_account=user@example
         TF_VAR_pid=pupi-pid--999999999
         TF_VAR_zone2=us-west2-b
         TF_VAR_zone1=us-west1-b
         ...
         

  5. Create an environment variable file:
         
         $HOME/pupi/saveVars.sh
         

This command redirects the environment variables that you created into a file named `TF_ENV_VARS`. Each variable is prepended with the `export` command. If your Cloud Shell session is terminated, you can use this file to reset the variables. These variables are used by the Terraform scripts, Cloud Shell scripts, and the Google Cloud CLI.

If you need to reinitialize the variables later, run the following command:
         
         source $HOME/pupi/TF_ENV_VARS
         




### Deploy supporting infrastructure

  1. In Cloud Shell, deploy the Terraform supporting infrastructure:
         
         terraform apply
         

When prompted, enter `yes` to apply either configuration. Terraform can take several minutes to deploy the resources.

The `terraform apply` command instructs Terraform to deploy all the solution's components. To understand how the infrastructure is declaratively defined, see the Terraform manifests (files with a `.tf` extension).

  2. Establish the VPC peering relationship. Because the feature is in alpha and not supported by Terraform, you use `gcloud` commands to set up peering.
         
         gcloud alpha compute networks peerings create consumer \
             --project="$TF_VAR_pid" \
             --network=consumer \
             --peer-network=producer
         
         gcloud alpha compute networks peerings create producer \
             --project="$TF_VAR_pid" \
             --network=producer \
             --peer-network=consumer \
             --no-export-subnet-routes-with-public-ip \
             --import-subnet-routes-with-public-ip
         

By default, the consumer VPC exports the PUPI addresses. When you create the producer VPC, you use the following arguments to configure the VPC to import PUPI addresses but not export them:
         
         --no-export-subnet-routes-with-public-ip
         --import-subnet-routes-with-public-ip
         




## Inspecting the supporting infrastructure

You now verify that Terraform successfully created the resources by checking whether the resources respond after you send a command.

### Verify the projects

  1. In Cloud Shell, list the project:
         
         gcloud projects list | grep pupi-pid
         

The output is similar to the following:
         
         ...
         pupi-pid--1234567899            pupi-test             777999333555
         ...
         

In this output, `pupi-test` is the project name, and `pupi-pid-` is the prefix to your project ID.

  2. List the API status:
         
         gcloud services list --project=$TF_VAR_pid \
             | grep -E "compute|container"
         

The output is similar to the following:
         
         ...
         compute.googleapis.com            Compute Engine API
         container.googleapis.com          Kubernetes Engine API
         containerregistry.googleapis.com  Container Registry API
         ...
         

This output shows that the Compute Engine, GKE, and Container Registry APIs are enabled.




### Verify the networks and subnetworks

  1. In Cloud Shell, verify the producer network and subnetwork:
         
         gcloud compute networks describe producer \
             --project=$TF_VAR_pid
         
         gcloud compute networks subnets describe producer-nodes \
             --project=$TF_VAR_pid \
             --region=$TF_VAR_region1
         

The output is similar to the following:
         
         ...
         kind: compute#network
         name: producer
         ...
         ipCidrRange: 10.128.0.0/24
         kind: compute#isubnetwork
         name: producer-nodes
         ...
         secondaryIpRanges:
         - ipCidrRange: 45.45.45.0/24
           rangeName: producer-pods
         - ipCidrRange: 172.16.45.0/24
           rangeName: producer-cluster
         ...
         

This output shows the following:

     * The network was created with the `10.128.0.0/24` CIDR block.
     * The two subnets were created with the `45.45.45.0/24` and `172.16.45.0/24` CIDR blocks.
  2. Verify the consumer network and subnetwork:
         
         gcloud compute networks describe consumer \
             --project=$TF_VAR_pid
         
         gcloud compute networks subnets describe consumer-nodes \
             --project=$TF_VAR_pid \
             --region=$TF_VAR_region2
         

The output is similar to the following:
         
         ...
         kind: compute#network
         name: consumer
         ...
         ipCidrRange: 10.129.0.0/24
         kind: compute#isubnetwork
         name: consumer-nodes
         ...
         secondaryIpRanges:
         - ipCidrRange: 5.5.5.0/24
           rangeName: producer-pods
         - ipCidrRange: 172.16.5.0/24
           rangeName: consumer-cluster
         ...
         

This output shows the following:

     * The network was created using the `10.129.0.0/24` CIDR block.
     * The two subnets were created using the `5.5.5.0/24` and `172.16.5.0/24` CIDR blocks.



### Verify the GKE cluster and its resources

  1. In Cloud Shell, get the cluster credentials:
         
         gcloud container clusters get-credentials consumer-cluster \
             --project=$TF_VAR_pid \
             --zone=$TF_VAR_zone2
         

The output is similar to the following:
         
         ...
         Fetching cluster endpoint and auth data.
         kubeconfig entry generated for consumer-cluster.
         ...
         

  2. Verify the cluster:
         
         gcloud container clusters list \
             --project=$TF_VAR_pid \
             --zone=$TF_VAR_zone2
         

The output is similar to the following:
         
         NAME              LOCATION    MASTER_VERSION  MASTER_IP      MACHINE_TYPE   NODE_VERSION    NUM_NODES  STATUS
         consumer-cluster  us-west2-b  1.14.10-gke.17  35.236.104.74  n1-standard-1  1.14.10-gke.17  3          RUNNING
         

This output shows a cluster that is named `consumer-cluster`.

  3. Verify the Hello World app:
         
         kubectl get deployment my-app
         

The output is similar to the following:
         
         ...
         NAME     DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
         my-app   3         3         3            3           118m
         ...
         

This output shows a deployment that is named `my-app`.

  4. Verify the internal load balancer service:
         
         kubectl get service hello-server
         

The output is similar to the following:
         
         NAME           TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)          AGE
         hello-server   LoadBalancer   172.16.5.99   10.129.0.200   8080:31673/TCP   4d23h
         

This output shows a service that is named `hello-server`.




## Verifying the solution

  1. In Cloud Shell, validate that you successfully created VPC peering:
         
         gcloud alpha compute networks peerings list
         

The output is similar to the following:
         
         NAME      NETWORK   PEER_PROJECT          PEER_NETWORK  IMPORT_CUSTOM_ROUTES  EXPORT_CUSTOM_ROUTES  STATE   STATE_DETAILS
         consumer  consumer  pupi-pid--1324732197  producer      False                 False                 ACTIVE  [2020-02-26T11:33:16.886-08:00]: Connected.
         producer  producer  pupi-pid--1324732197  consumer      False                 False                 ACTIVE  [2020-02-26T11:33:16.886-08:00]: Connected.
         

This output shows peerings that are named `consumer` and `producer`.

  2. Validate that the consumer VPC exports PUPI routes:
         
         gcloud alpha compute networks peerings list-routes consumer \
             --direction=OUTGOING \
             --network=consumer \
             --region="$TF_VAR_region2"
         

The output is similar to the following:
         
         DEST_RANGE     TYPE                  NEXT_HOP_REGION  PRIORITY  STATUS
         10.129.0.0/24  SUBNET_PEERING_ROUTE  us-west2         1000      accepted by peer
         172.16.5.0/24  SUBNET_PEERING_ROUTE  us-west2         1000      accepted by peer
         5.5.5.0/24     SUBNET_PEERING_ROUTE  us-west2         1000      accepted by peer
         

This output shows all three consumer CIDR blocks.

  3. Validate the PUPI routes that the producer VCP imported:
         
         gcloud alpha compute networks peerings list-routes producer \
             --direction=INCOMING \
             --network=producer \
             --region="$TF_VAR_region1"
         

The output is similar to the following:
         
         DEST_RANGE     TYPE                  NEXT_HOP_REGION  PRIORITY  STATUS
         10.129.0.0/24  SUBNET_PEERING_ROUTE  us-west2         1000      accepted
         172.16.5.0/24  SUBNET_PEERING_ROUTE  us-west2         1000      accepted
         5.5.5.0/24     SUBNET_PEERING_ROUTE  us-west2         1000      accepted
         

This output shows all three consumer CIDR blocks.

  4. Validate that the GKE Pods have a PUPI address:
         
         kubectl get pod -o wide
         

The output is similar to the following:
         
         NAME                      READY   STATUS    RESTARTS   AGE     IP         NODE                                              NOMINATED NODE   READINESS GATES
         my-app-594b56d7bc-642d8   1/1     Running   0          4d23h   5.5.5.21   gke-consumer-cluster-default-pool-cd302b68-tccf   <none>           <none>
         my-app-594b56d7bc-chnw8   1/1     Running   0          4d23h   5.5.5.38   gke-consumer-cluster-default-pool-cd302b68-h8v9   <none>           <none>
         my-app-594b56d7bc-fjvbz   1/1     Running   0          4d23h   5.5.5.20   gke-consumer-cluster-default-pool-cd302b68-tccf   <none>           <none>
         

The IP addresses of the Pods fall within the `5.5.5/24` range.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial:

### Destroy the infrastructure

  1. In Cloud Shell, destroy all of the tutorial's components:
         
         terraform destroy
         

When prompted, enter `yes` to destroy the configuration.

You might see the following Terraform error:
         
         ...
         ∗ google_compute_network.ivpc (destroy): 1 error(s) occurred:
         ∗ google_compute_network.ivpc: Error waiting for Deleting Network: The network resource 'projects/pupi-pid--1324732197/global/networks/consumer-cluster' is already being used by 'projects/pupi-pid--1324732197/global/firewalls/k8s-05693142c93de80e-node-hc'
         ...
         

This error occurs when the command attempts to destroy the VPC network before destroying the GKE firewall rules. If you receive this error, do the following:

     1. Remove the non-default firewall rules from the VPC:
            
            $HOME/pupi/k8-fwr.sh
            

The output shows you the firewall rules to be removed. Review the rules and, when prompted, enter `yes`.

     2. Re-issue the following command:
            
            cd $HOME/pupi
            terraform destroy
            

When prompted, enter `yes` to destroy the configuration.

  2. Remove the Git repository:
         
         rm -rf $HOME/pupi
         




## What's next

  * Read the [Configuring private service access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) guide.
  * Read the [Getting started with the Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) guide.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2022-12-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2022-12-19 UTC."],[],[]] 
