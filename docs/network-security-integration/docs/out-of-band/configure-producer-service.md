---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-producer-service/
title: Set up producer services \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:53:02.630988+00:00
---

# Set up producer services  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-producer-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Set up producer services Stay organized with collections  Save and categorize content based on your preferences. 

To enable producer service in your network, you must set up the producer services such as mirroring deployment groups and mirroring deployments. This document provides a high-level workflow that describes how to configure these components.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make sure that you have the following Identity and Access Management (IAM) roles on your project: 
     * [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)
     * Mirroring Deployment Admin role (`roles/networksecurity.mirroringDeploymentAdmin`)
  7. Enable the Compute Engine and Network Security APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networksecurity.googleapis.com)

  8. Make sure to install the Google Cloud CLI. For the conceptual and installation information about the tool, see [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you haven't run the Google Cloud CLI previously, initialize your gcloud CLI directory by running the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init). 




## Configure producer compute resources

To configure producer compute resources in your network, perform the following tasks:

**Note:** This section describes the commonly used configuration for setting up internal passthrough Network Load Balancer. For information about other configurations, see [Set up a regional internal proxy Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs).

  1. Create a Virtual Private Cloud (VPC) network that contains the producer deployment groups and deployments. For more information, see [Create networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).

  2. Create an instance template and specify the machine type, boot disk image, VPC network, and other properties for your third-party appliances. You can then use the instance template to create a managed instance group. For more information, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

**Note:** We recommend using a managed instance group, but you can also use the unmanaged instance group.
  3. Create [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) and deploy your third-party appliances on multiple identical VMs in a specific zone. For more information, see [Create a MIG in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).

  4. Create health checks to monitor whether [load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) backends respond to traffic. For more information, see [Create health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#create-hc).

  5. Create the backend service with the third-party appliance instance groups that you created in the previous step.

To create backend services with an internal passthrough Network Load Balancer, follow these steps:

     1. Create the backend service with the protocol set to `UDP`. For more information, see Create an internal load balancer for Packet Mirroring.

     2. Add the VM instance group to the backend service. A backend service is necessary for creating an internal passthrough Network Load Balancer. For more information, see [Add a managed instance group to a backend service](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer#add_a_managed_instance_group_to_a_backend_service).

     3. Create an internal forwarding rule for the backend service to forward mirrored traffic that originates from the consumer VPC network. For more information, see Create an internal load balancer for Packet Mirroring.

     4. Create an ingress firewall rule in your network firewall policy that allows UDP traffic on port 6081 to your VMs from the producer subnet gateway address or the local subnet range. The producer-side firewall does not require consumer IP ranges. For more information, see [Create global network firewall rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-rules).

**Note:** To get the producer subnet gateway address (`gatewayAddress`), use the [`gcloud compute networks subnets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/describe) command or the [`subnetworks.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/get) method.



### Create an internal load balancer for Packet Mirroring

To enable Packet Mirroring, you need an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) that can serve as a packet mirroring producer. The internal passthrough Network Load Balancer must meet the following requirements:

  * The internal passthrough Network Load Balancer's forwarding rule must have Packet Mirroring enabled when the rule is created. This status can't be changed after the rule is created. While the forwarding rule only accepts IPv4 traffic, the mirrored traffic that is Geneve-encapsulated can be IPv4 or IPv6.
  * The internal passthrough Network Load Balancer and the instances you're mirroring must be in the same region.
  * The internal passthrough Network Load Balancer's backend service uses a [session affinity](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity) of `NONE` (5-tuple hash).
  * The [backend subsetting](https://docs.cloud.google.com/load-balancing/docs/internal#backend_subsetting) of the internal passthrough Network Load Balancer's backend service is disabled.



If your producer instances are not set up to respond to the health check configured for your backend service, the health check might fail. However, packet mirroring continues in this scenario.

To create an internal passthrough Network Load Balancer for Packet Mirroring, follow these steps.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. On the **Create internal passthrough Network Load Balancer** page, enter the following information:

     1. For **Load balancer name** , enter a name.
     2. For **Region** , select the region of the VM instances where you want to mirror packets.
     3. For **Network** , select the network where you want to mirror packets.



#### Configure the backends

  1. Click **Backend configuration**.
  2. For **Backend type** , select **Instance group**.
  3. From the **Protocol** list, select **UDP**.
  4. In the **New Backend** section, from **Instance group** list, select the instance group to forward packets to.
  5. In the **New Backend** section, do the following:

     1. Select the **IP stack type**.
     2. From **Instance group** list, select the instance group to forward packets to.
     3. Click **Done**.

Note that when you use the Google Cloud console to create your load balancer, the health check is global. If you want to create a regional health check, use `gcloud` or the API.




#### Configure the frontend

  1. On the **Create internal passthrough Network Load Balancer** page, click **Frontend configuration**.
  2. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter a name.
     2. For **Subnetwork** , select a subnetwork in the same region as the instances to mirror.
     3. For **Ports** , select **Single** and then in **Port numbers** , enter `6081`.
     4. Click **Advanced configurations** and select the **Enable this load balancer for packet mirroring**.
     5. Click **Done**.



#### Review the configuration

  1. On the **Create internal passthrough Network Load Balancer** page, click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Click **Create**.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to an instance group:
         
         gcloud compute health-checks create http HEALTH_CHECK_NAME \
             --region REGION \
             --port PORT
         

Replace the following:

     * `HEALTH_CHECK_NAME`: the name of the health check.
     * `REGION`: the region of the VM instances for which you want to mirror packets.
     * `PORT`: The port number that the health check monitors. If none is specified, the default port of `80` is used.
  2. Create a backend service for HTTP traffic:
         
         gcloud compute backend-services create COLLECTOR_BACKEND_SERVICE \
             --region=REGION \
             --health-checks-region=REGION \
             --health-checks=HEALTH_CHECK_NAME \
             --load-balancing-scheme=internal \
             --protocol=udp
         

Replace the following:

     * `COLLECTOR_BACKEND_SERVICE`: the name of the backend service.
     * `REGION`: the region of the VM instances where you want to mirror packets.
     * `HEALTH_CHECK_NAME`: the name of the health check.
  3. Add an instance group to the backend service:
         
         gcloud compute backend-services add-backend COLLECTOR_BACKEND_SERVICE \
             --region=REGION \
             --instance-group=INSTANCE_GROUP \
             --instance-group-zone=ZONE
         

Replace the following:

     * `COLLECTOR_BACKEND_SERVICE`: the name of the backend service.
     * `REGION`: the region of the instance group.
     * `INSTANCE_GROUP`: the name of the instance group.
     * `ZONE`: the zone of the instance group.
  4. Create a forwarding rule for the backend service:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
             --region REGION \
             --load-balancing-scheme=internal \
             --network NETWORK \
             --subnet SUBNET \
             --address=ADDRESS \
             --ports=6081 \
             --ip-protocol=UDP \
             --backend-service COLLECTOR_BACKEND_SERVICE \
             --backend-service-region BACKEND_REGION \
             --is-mirroring-collector
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule.
     * `REGION`: the region for the forwarding rule.
     * `NETWORK`: the network for the forwarding rule.
     * `SUBNET`: a subnetwork in the region of the VMs where you want to mirror packets.
     * `ADDRESS`: the IP address that the forwarding rule serves. When the mirrored traffic reaches the collector VMs, this value is set as the destination IP address.
     * `COLLECTOR_BACKEND_SERVICE`: the backend service for the load balancer.
     * `BACKEND_REGION`: the region of the backend service.



## Configure producer mirroring resources

To configure producer mirroring resources, such as mirroring deployment groups and mirroring deployments in your network, do the following:

  1. Create a [mirroring deployment group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview) to represent a producer's mirroring service that the consumers can connect to. For more information, see [Create and manage mirroring deployment groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups).

  2. Create [mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployments-overview) in every zone where you want to expose the backend service through Network Security Integration. These are the same backend services that you created in the previous step. For more information, see [Create and manage mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployments).

  3. By default, a mirroring deployment group and mirroring deployment are secured against traffic from unknown consumers. To allow a consumer to attach to the mirroring deployment group, make sure that you have the Mirroring Deployment Admin role (`networksecurity.mirroringDeploymentGroups.use`) on the producer's project. The Mirroring Deployment User role (`roles/networksecurity.mirroringDeploymentUser`) is included by default when you have have the Mirroring Deployment Admin role.




## What's next

  * [Set up consumer services](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-consumer-service)
  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
