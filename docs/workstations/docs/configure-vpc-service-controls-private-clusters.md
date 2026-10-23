---
url: https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters/
title: Configure VPC Service Controls and private clusters \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:42.719842+00:00
---

# Configure VPC Service Controls and private clusters  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Configure VPC Service Controls and private clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how VPC Service Controls and private clusters work and how to set them up in Cloud Workstations.

## VPC Service Controls

VPC Service Controls provides additional security for your workstations to help mitigate the risk of data exfiltration. Using VPC Service Controls, you can add projects to service perimeters that can help protect resources and services from requests that originate outside the perimeter.

These are the requirements for using Cloud Workstations in a VPC service perimeter:

  * To help protect Cloud Workstations, you must restrict the Compute Engine API in your service perimeter whenever you restrict the Cloud Workstations API.
  * Make sure that Google Cloud Storage API and Artifact Registry API are [ VPC accessible](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) in your service perimeter. This is needed to pull images onto your workstation. We also recommend that you allow Cloud Logging API and Cloud Error Reporting API to be VPC accessible in your service perimeter, although this is not required to use Cloud Workstations. 

  * Make sure that your workstation cluster is [private](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters#create_a_private_cluster). Configuring a private cluster prevents connections to your workstations from outside your VPC service perimeter. The Cloud Workstations service prevents the creation of public clusters in a VPC service perimeter. 
  * Make sure that you turn off public IP addresses in your workstation configuration. Failing to do so results in VMs with public IP addresses in your project. We strongly recommend that you use the `constraints/compute.vmExternalIpAccess` organization policy constraint to turn off public IP addresses for all VMs in your VPC service perimeter. For details, see [Restricting external IP addresses to specific VMs](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip). 

**Note:** Access control is only based on whether the private network you're connecting from belongs to the security perimeter. Access control based on device, external IP address, or location is not supported.

To learn more about service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

## Architecture

When you configure a workstation cluster as private, the control plane of the workstation cluster only has an internal IP address. This means that clients from the public internet cannot connect to the workstations belonging to the workstation cluster. To use a private cluster, you must manually connect the private cluster to your Virtual Private Cloud (VPC) network through a [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint.

Configurations with private clusters require _two_ PSC endpoints:

  * By default, Cloud Workstations creates a separate PSC endpoint to connect the control plane to the workstation VMs.

  * You must create an additional PSC endpoint for private clusters. To connect from your local machine to a workstation in a private cluster, your local machine must be connected to your VPC network. Use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to connect the external network in which you run your machine to the VPC network. This additional PSC endpoint must be created in the same network that your external network connects to with Cloud VPN or Cloud Interconnect.




The following diagram illustrates an example architecture of a private cluster:

![](https://docs.cloud.google.com/static/workstations/images/architecture-private-clusters.svg)Figure 1. Private clusters

## Before you begin

Before you begin, make sure that you complete these required setup steps:

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

  6. Enable the Cloud Workstations API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workstations.googleapis.com)

  7. Make sure that you have a Cloud Workstations Admin IAM role on the project so that you can create workstation configurations. To check your IAM roles in the Google Cloud console, go to the **IAM** page:

[ Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  8. Cloud Workstations are hosted on VMs booted from Compute Engine's preconfigured public [Container-Optimized OS (COS)](https://docs.cloud.google.com/compute/docs/images/os-details#container-optimized_os_cos) images. If the `constraints/compute.trustedimageProjects` organization policy constraint is enforced, you must [set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images) to allow users to create boot disks from `projects/cos-cloud` or all public images. 
  9. Cloud Workstations uses Private Service Connect to connect to Google-managed services. If the `constraints/compute.restrictPrivateServiceConnectProducer` organization policy constraint is enforced in your organization, you must [add Google as an allowed producer](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#add-org-policy) (`under:organizations/433637338589`). 
  10. If the `constraints/compute.disablePrivateServiceConnectCreationForConsumers` organization policy constraint is enforced in your organization, you must ensure that Private Service Connect endpoints connecting to Google APIs (`GOOGLE_APIS`) are [allowed](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers#connection-type). If you configure private clusters, endpoints connecting to published services (`SERVICE_PRODUCERS`) must also be allowed. 
  11. **Optional:** Enable the Container File System API to allow faster workstation startup. 

[Enable the Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com?q=container%20file%20system)

For more information, see [Reduce workstation startup time with Image streaming](https://docs.cloud.google.com/workstations/docs/architecture#image-streaming). 




## Create a private cluster

Follow these steps to create a private cluster:

  1. In the Google Cloud console, go to the **Cloud Workstations** page. 

[Go to Cloud Workstations](https://console.cloud.google.com/workstations/)

  2. Navigate to the workstation **Cluster management** page.

  3. Click **Create**.

  4. Enter the **Name** and select a **Region** for your workstation cluster.

  5. In the Networking section, select **Networks in this project**.

  6. Select a **Network** and a **Subnetwork**.

  7. For **Gateway type** , select **Private gateway**. 

  8. Optional: Specify one or more additional projects that host the Private Service Connect endpoint that enables HTTP access to your private cluster. By default, this endpoint can only be created in the workstation cluster project and VPC network host project (if different). If needed, these projects can also be specified after cluster creation.

  9. Click **Create**. While the cluster is being created, the status appears as **Updating**.

Creating a cluster takes several minutes to complete. When cluster creation has finished, the cluster's status might appear as **Degraded**. After you complete the steps in the Create a PSC endpoint section, the cluster's status will change to **Ready** within several minutes.




## Enable private cluster connectivity

Clients cannot connect to workstations in private workstation clusters from the public internet. Clients must be on a network that connects to the workstation cluster using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) (PSC). Follow the steps in this section to connect to a workstation:

  1. Create a PSC endpoint that targets your workstation service attachment.

  2. Create a private DNS zone.

  3. Use Cloud DNS to create a DNS record that maps your cluster's hostname to the PSC endpoint.




### Create a Private Service Connect endpoint

**Note:** By default, the PSC endpoint and DNS zone can only be created in the workstation cluster project and VPC network host project (if different). If you want to create these resources in a different project, update the [privateClusterConfig.allowedProjects](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters#PrivateClusterConfig) field on your workstation cluster using the workstation API or UI to include the project.

Follow these steps to create a PSC endpoint:

  1. In the Google Cloud console, go to Private Service Connect. 

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc/list)

  2. Click the **Connected endpoints** tab and then click add**Connect endpoint**.

  3. For **Target** , select **Published service**.

  4. In the **Target service** field, enter the service attachment URI created for the workstation cluster. Find this by navigating to your workstation cluster on the console and looking for the **Service attachment URI** field under **Network settings**.

  5. In the **Endpoint** field, enter an endpoint name.

  6. Select a **Network** for the endpoint and then select a **Subnetwork**. This network should be the network that you want to use to connect to your workstations, and must be the same network that your external network connects to with Cloud VPN or Cloud Interconnect.

  7. Select an **IP address** for the endpoint.

If you need a new IP address, select **Create IP address** :

     1. Enter a **Name** and optional **Description** for the IP address.
     2. For a **Static IP address** , select **Assign automatically**. For a **Custom IP address** , select **Let me choose** and enter the IP address that you want to use.
     3. For **Purpose** , select **Non-shared**.
     4. Click **Reserve**.
  8. Select a **Namespace** from the drop-down list or create a new namespace. The **Region** populates based on the selected subnetwork.

  9. Click **Add endpoint**.

  10. Copy the IP address of the endpoint so that you can use it in the next section to [Create a private DNS zone and DNS record](https://docs.cloud.google.com/workstations/docs/configure-private-clusters#create_a_private_dns_zone_and_dns_record).




### Create a private DNS zone

Follow these steps to create a private DNS zone for this workstation cluster with the DNS Name set to your `clusterHostname`, which you can find by navigating to your workstation cluster on the console.

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/networking/dns/zones/~new)

  2. For the **Zone type** , select **Private**.

  3. Enter a **Zone name** such as `private-workstations-cluster-zone`.

  4. Enter a **DNS name** suffix for the private zone. All records in the zone share this suffix. Set this name to your `clusterHostname`.

To find your `clusterHostname`, navigate to the **Cloud Workstations** > **Cluster management** page in the Google Cloud console, and then click your workstation cluster to view the hostname.

  5. Optional: Add a description.

  6. Under **Options** , select **Default (private)**.

  7. Select the network that you created the PSC endpoint on in the [previous section](https://docs.cloud.google.com/workstations/docs/configure-private-clusters#create_a_endpoint) because the IP address is only valid on that network.

  8. Click **Create**.




For more information about private DNS zones, see the Cloud DNS documentation on how to [Create a private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone) and [Best practices for Cloud DNS private zones](https://docs.cloud.google.com/dns/docs/best-practices#best_practices_for_private_zones).

### Create a DNS record

To add a record that maps `*.<clusterHostname>` to the IP address reserved when you created the Private Service Connect endpoint, follow these steps:

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/)

  2. Click the name of the managed zone that you want to add the record to.

  3. On the **Zone details** page, click **Add Standard**.

  4. On the **Create record set** page, in the **DNS name** field, enter `*.<clusterHostname>`. 

  5. In the **IP Address** field, enter the IP address you reserved for your Private Service Connect endpoint in the previous section.

  6. Click **Create**.

  7. Your VPC network should now be connected to the workstation cluster and you can connect to workstations using this network.




### Enable DNS resolution on-premises

To use the default browser based editor on your workstation, use a browser from a machine connected to the VPC network. You can use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to connect from the external network in which you run your browser to the VPC network.

To connect from an external network, you need to configure DNS in the external network. Similar to the preceding steps, you can create a DNS zone for `clusterHostname` and add a record that maps `*.<clusterHostname>` to the IP address reserved when you created the Private Service Connect endpoint. Alternatively, you can set up [DNS forwarding zones or DNS server policies](https://docs.cloud.google.com/dns/docs/best-practices#best_practices_for_dns_forwarding_zones_and_server_policies) to allow lookups of DNS names between your on-premises and Google Cloud environments.

You might also need to add `*cloudworkstations.dev` to your on-premises infrastructure's allowlist.

## Configure VPC Service Controls for image streaming

If you optionally enable [image streaming](https://docs.cloud.google.com/workstations/docs/architecture#image-streaming) to reduce workstation startup times, and your workstation cluster is inside a VPC Service Controls perimeter, you must configure the following in your perimeter policy:

  * Include the Container File System API (`containerfilesystem.googleapis.com`) in the restricted services of your service perimeter.
  * Add an egress rule in the service perimeter that allows the service account specified in the workstation config to access the Container File System API on the project hosting your container images.
  * If you are using a [preconfigured IDE](https://docs.cloud.google.com/workstations/docs/preconfigured-ides), you must also configure the egress rule to allow access to the `cloud-workstations-images` project (project number `662288601415`).



## What's next

  * [Set up Shared VPC access ](https://docs.cloud.google.com/workstations/docs/set-up-shared-vpc-access)
  * [Troubleshoot common VPC issues ](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
