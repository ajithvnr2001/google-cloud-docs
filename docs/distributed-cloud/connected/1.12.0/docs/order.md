---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/order/
title: Order hardware \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:58.849820+00:00
---

# Order hardware  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/order/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Order hardware Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to order Google Distributed Cloud connected hardware. Distributed Cloud connected is available in the following countries:

  * Australia
  * Austria
  * Belgium
  * Brazil
  * Canada
  * Chile
  * Denmark
  * Finland
  * France
  * Germany
  * Hong Kong
  * Japan
  * India
  * Indonesia
  * Italy
  * Malaysia
  * Mexico
  * Netherlands
  * Norway
  * Poland
  * Saudi Arabia
  * Singapore
  * South Korea
  * Spain
  * Sweden
  * Switzerland
  * United Kingdom
  * United States
  * Uruguay



Before you order the hardware, you must meet the [Distributed Cloud connected installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements).

## Distributed Cloud connected procurement models

You can order the Distributed Cloud connected hardware in one of the following ways, based on your business requirements:

  * **Google-owned hardware.** You can order the Distributed Cloud connected hardware directly from Google. In this scenario, Google sources, maintains, repairs, and decommissions the Distributed Cloud connected hardware. When your contract concludes, Google collects the Distributed Cloud hardware and destroys all data stored on it.

  * **Customer-sourced hardware.** You can order Distributed Cloud connected from a Google-certified system integrator (SI) after consulting with Google on a deployment configuration that fits your business requirements. In this scenario, you own the Distributed Cloud connected hardware. The SI works with you and Google to deploy, repair, and decommission the hardware. When your contract concludes, the SI wipes all Google software and your data from the Distributed Cloud connected hardware. You are then free to reuse or dispose of the hardware. This type of procurement is only available for Distributed Cloud connected servers.




## Distributed Cloud connected hardware variants

Distributed Cloud connected servers hardware is available in the following form factors:

  * **Distributed Cloud connected servers G1.** A group of three Dell XR11 1U rackmount machines. For more information, see [Distributed Cloud connected servers G1 hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements#g1-hardware).

  * **Distributed Cloud connected servers G2.** A Dell XR8000r chassis populated with three XR8610t machine sleds. For more information, see [Distributed Cloud connected servers G2 hardware](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements#g2-hardware).




For a list of Distributed Cloud connected servers SKUs, see [Distributed Cloud connected pricing](https://docs.cloud.google.com/distributed-cloud/connected/pricing).

## Prerequisites

This section describes the Google Cloud setup requirements and the information that you need to gather before ordering hardware.

### Google Cloud setup

Before you begin, ensure that you have the necessary permissions and that the API is enabled in your Google Cloud project. You need to complete these steps whether you place orders directly through the Google Cloud console or through an integrated API.

  * **Google Cloud project** : You must have a Google Cloud project with an administrator authorized to enable the Distributed Cloud Hardware Management API. For more information about creating a Google Cloud project, see [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project). The project that you use to manage your clusters must be the same project that you use when ordering the hardware.

  * **Distributed Cloud Hardware Management API** : You need to enable the Distributed Cloud Hardware Management API. In the Google Cloud console, go to the **GDC Hardware Management API** page. If needed, click **Enable** to enable the API.

[Go to GDC Hardware Management API](https://console.cloud.google.com/apis/library/gdchardwaremanagement.googleapis.com?project=_)

  * **IAM roles** : To order hardware, you need to be granted the **GDC Hardware Management Admin** (`gdchardwaremanagement.admin`) IAM role. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * **Contractual requirement** : Before Google can process a fulfillment request, you need a valid, signed contract on file and a billing ID. For more information, see [Find a Cloud Billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id).




### Contacts

To place an order, you need to provide the following contacts:

  * **Order contact** : A person responsible for managing the deployment of Distributed Cloud connected hardware at your organization. Provide a company representative who we can contact to complete sales and contracting processes.

  * **Site contact** : A person responsible for the selected deployment site. Google contacts this person to schedule and complete the delivery of your Distributed Cloud connected hardware. This person also coordinates hardware repairs and decommissioning with Google or with a Google-certified SI.

  * **Zone and network contact** : A person responsible for integrating the Distributed Cloud connected hardware into the existing networking and power infrastructure at the deployment site. This person also assists with joint troubleshooting if required.




### Site information

Before placing an order, gather the following information:

  * **Order identifier** : A meaningful identifier for this Distributed Cloud connected hardware order.

  * **Site identifier** : A meaningful identifier for the deployment site for this Distributed Cloud connected hardware order.

  * **Zone identifier** : A meaningful identifier for the target Distributed Cloud connected zone. If you're only deploying one zone per site, use the site identifier as the zone identifier.

  * **Deployment country** : The country where your hardware will be deployed. The country impacts the billing currency and the hardware availability. To order hardware in multiple locations, create separate orders for each country.

  * **Region** : The geographic location where your order and customer data is stored. This selection ensures that your data remains within the selected region, helping you meet compliance requirements.

  * **Company information** : When you place your order, you need to provide a company name, email address, phone number, and billing address.




## Network configuration information

When you place your order, you need to make selections for your network configuration. Use the information in the following table to understand the network configuration you need to provide during order placement.

Network type | IP configuration name | Description  
---|---|---  
Machine management network | IPv4 machine management addresses in CIDR notation | Each server has an IP address for Distributed Cloud management traffic. This block configures IP addresses from the machine management subnet that are used for this task.  
IPv4 machine management subnet in CIDR notation | The subnet allocated for Distributed Cloud management traffic. Traffic includes Distributed Cloud infrastructure software updates and infrastructure logs and metrics. This subnet must be large enough to contain the IPv4 address block for machine management as well as the default gateway of the machine management subnet.  
Default gateway of the machine management subnet | The gateway IP address within the machine management subnet  
Kubernetes node traffic | IPv4 Kubernetes node addresses in CIDR notation | Each server has an IP address for Kubernetes-related traffic. This block configures the IP addresses from the Kubernetes subnet used for Kubernetes-related traffic.  
IPv4 address block for Kubernetes control plane VIPs in CIDR notation | Each Kubernetes cluster created in the edge zone has one control plane VIP assigned from this address block. If you expect to create only one cluster in your edge zone, you can use a `/32` address block. Otherwise, the address block must be larger.  
IPv4 Kubernetes subnet in CIDR notation | The subnet allocated for Kubernetes traffic. Traffic includes container downloads, Kubernetes primary networking, Kubernetes logs and metrics, and Kubernetes control plane traffic. When empty, this subnet defaults to **IPv4 machine management subnet**. You can also specify a separate subnet in this field. This subnet must be large enough to contain the IPv4 address block for Kubernetes node traffic, the IPv4 address block for Kubernetes control plane VIPs, the default gateway of the Kubernetes subnet, and any primary network load balancer VIPs planned. If unspecified, this value is the same as the management network value.  
Default gateway of the Kubernetes subnet | The gateway IP address within the Kubernetes subnet. When empty, this field defaults to **Default gateway of the machine management subnet**.  
Kubernetes primary VLAN ID | By default, the Kubernetes node, including the primary Kubernetes network, are in the same VLAN as the machine management network. For network segmentation purposes, you can separate these networks.  
DNS name servers | DNS name server 1 | The DNS name server IPs. The Distributed Cloud infrastructure resolves DNS queries through these IPs. If unspecified, Google DNS is used.  
DNS name server 2 | The DNS name server IPs. The Distributed Cloud infrastructure resolves DNS queries through these IPs. If unspecified, Google DNS is used.  
  
## Order Distributed Cloud connected hardware using the Google Cloud console

  1. In the Google Cloud console, go to the **Orders** page. 

[Go to Orders](https://console.cloud.google.com/distributed-cloud/edgezones/order-management/orders?project=_)

  2. Select the target Google Cloud project.

  3. Click **Create single order**.

  4. In the **Order details** form, enter the order details that you gathered in the Prerequisites section of this document. Click **Continue**.

**Note:** After you enter the information on the **Order details** page, you can save a draft of your order by clicking **Save as draft**. This option is available for every step of the order process.
  5. In the **Select hardware** form, select the server configuration, number of nodes, and subscription months.

     * For standard clusters, the default value for the **Number of nodes** is **3**. Single-node options are only available for customers on an allowlist.

     * To avoid order rejection or fulfillment delays, the details that you provide must match your signed Google contract.

     * When the form is complete, click **Continue**.

  6. In the **Add site info** form, add the information about the site where the Distributed Cloud connected hardware will be shipped and installed. You can add a new site or choose an existing site. When complete, click **Continue**.

  7. In the **Add zone info** form, add a new zone or select an existing zone.

     * For **Cluster provisioning** , if you plan to configure clusters yourself, select **I will configure clusters at my site**. If you want Google to configure clusters for you, you must provide cluster intent so that Google can deliver your order with a preconfigured cluster.

     * The information in the **Network configuration** section is required to connect the hardware in your zone to the Google Cloud network. For more information about the options, see the Network configuration information section in this document.

       * You can save the order as a draft, and let your zone and network representative input the information. Otherwise, provide the necessary IP network information.

       * For **Select the preferred template for IP addresses** , select a template that matches your requirements. The templates help to ensure that the correct IP details are provided. To manually enter IP addresses, select **Custom IP**.

     * When the form is complete, click **Continue**.

  8. In the **Installation requirements** form, enter your physical site requirements, and then click **Continue**.

  9. In **Review details and submit** , verify that the order details are correct, and then click **Create**. After you click **Create** , the order is in review. A Google Cloud sales representative reviews your submission and contacts you to complete the order. The representative does the following:

     * Reviews your business requirements to help you finalize your hardware configuration.
     * Collects further information about your local network, Google Cloud project, installation site, and other requirements listed in the [installation requirements](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/requirements).
     * Uses this information to configure your Distributed Cloud hardware before delivery.



Your requested installation date is automatically set to the first available date, typically 45 days after Google accepts the order.

## Order Distributed Cloud connected hardware using the GDC Hardware Management API

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The GDC Hardware Management API lets you programmatically place an order for Distributed Cloud hardware. An order constitutes your intent to deploy Distributed Cloud connected. An order must include the following information, which is used throughout the lifetime of your Distributed Cloud connected deployment:

  * Point of contact for order management and delivery
  * Delivery site address and any information relevant to delivery
  * Hardware configuration
  * Network configuration



You must work with your Google sales representative to complete the Customer Information Questionnaire (CIQ) and finalize the scope and configuration of your Distributed Cloud connected deployment.

### Enable the GDC Hardware Management API

Before you can use the GDC Hardware Management API, you must enable it on the target Google Cloud project. To do so, complete the steps in this section.

###  Console 

  1. In the Google Cloud console, go to the **GDC Hardware Management API** page.

[Enable the API](https://console.cloud.google.com/apis/api/gdchardwaremanagement.googleapis.com)

  2. Click **Enable**.




###  gcloud 

Use the following command:
    
    
    gcloud services enable gdchardwaremanagement.googleapis.com
    

### Structure of an order

To place an order using the GDC Hardware Management API, you must create an `Order` resource, plus the accompanying `Site`, `Zone`, and `Hardware` resources that the `Order` resource references. You then submit the `Order` resource to Google. These resources support standard CRUD operations. The name of each resource is a path that includes the target Google Cloud project ID and Google Cloud region.

These resources have the following functions. For more information about using the GDC Hardware Management API, see the [Google Distributed Cloud CLI and API reference](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/apis).

  * **`Order`**. This resource requests the creation of one or more Distributed Cloud zones. When you create this resource, it receives a name accessible in the `create_order_response.name` field. The `Order` resource name has the following format:
        
        `projects/`PROJECT_ID`/locations/`REGION`/orders/`ORDER_ID

where:

    * `PROJECT_ID`: the ID of the target Google Cloud project.
    * `REGION`: the Google Cloud region in which you want to deploy your Distributed Cloud zones.
    * `ORDER_ID`: a unique ID that identifies this order. We recommend that you provide a unique order ID value consisting of [lowercase letters, numbers, and dashes](https://google.aip.dev/122#resource-id-segments). Otherwise, failed order creation calls can generate duplicate orders.
  * **`Site`**. This resource represents the physical location where you want to deploy your Distributed Cloud hardware. This resource includes the contact information of a responsible party who coordinates access for initial delivery and future maintenance. This contact might be different from the one you provided on the order.

  * **`Hardware`**. This resource instantiates a Distributed Cloud connected SKU and represents a Distributed Cloud server or rack. Each `Hardware` resource references the associated `Order`,`Site`, and `Zone` resources. To see the available SKUs, use the [ListSkus](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rpc/google.cloud.gdchardwaremanagement.v1alpha#google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement.ListSkus) API call.

  * **`Zone`**. This resource specifies the network configuration of your Distributed Cloud connected machines and associated clusters. A Distributed Cloud zone covers one or more Distributed Cloud connected racks or all of the Distributed Cloud connected server machines deployed at your location.




When you submit an `Order` resource to Google and its [status](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders#state) changes from `DRAFT` to `SUBMITTED` or `INFO_COMPLETE`, most of the field values become read-only.

### Lifecycle of an order

An `Order` resource can have one of the states listed in [`State`](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rpc/google.cloud.gdchardwaremanagement.v1alpha#google.cloud.gdchardwaremanagement.v1alpha.Order.State). Involved parties can leave comments on the order, which are stored as `Comment` resources nested under the corresponding `Order` resource. You can read and submit comments through both the GDC Hardware Management API and the Google Cloud console.

The GDC Hardware Management API supports the following order lifecycle operations:

  * **Create and submit an order.** You can create and immediately submit an order, or build it gradually and save it in a `DRAFT` state until you're ready to submit it. This process is described in the remainder of this guide.

  * **Check order status.** If the order is submitted with [type](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/submit#type) `INFO_COMPLETE` and you have signed a contract with Google, the order proceeds through the following state succession: `ACCEPTED,` `BUILDING,` `SHIPPING`, `INSTALLING` and `COMPLETED.` The states of the associated `Zone` and `Hardware` resources are updated in lockstep with the `Order` resource.

  * **Resolve order issues.** If we need more information from you or you have not signed a contract with Google, the order enters the `ADDITIONAL_INFO_NEEDED` state and awaits resolution through [comments](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments). Look for further instructions in a comment, and contact Google if the next steps are at any point unclear.

  * **Delete an unsubmitted order**. You can delete an unsubmitted order with a [`DELETE`](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/delete) call.

  * **Modify a submitted order**. You can modify the submitted [order](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/patch), [site](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.sites/patch), and [zone](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.zones/patch) using the respective `PATCH` call. The following fields are editable post-submission:

    * All resources: `display_name`, `labels`
    * Order: `organization_contact`
    * Site: `access_times`, most fields of `organization_contact` but **not** the site address
    * Hardware: `requested_installation_date` if _at least one_ of the following are true: 
      * New date is >45 days from now
      * New `requested_installation_date` is later than current `requested_installation_date` _and_ `estimated_installation_date` is empty
      * New `requested_installation_date` is later than current `requested_installation_date` _and_ `estimated_installation_date` is at least 7 days from now

No other information can be modified once an order has been submitted, but you can ask Google to do so by placing a [comment](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments).

  * **Cancel a submitted order**. You can cancel a submitted order by adding a [comment](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments) to it requesting the cancellation.




### Select the target Google Cloud project

A Google Cloud project is a construct that encapsulates a set of Google Cloud resources, makes them available for you to use, and establishes rules for access control and billing for those resources.

We recommend that you create a separate Google Cloud project per administrative domain, such as a country or corporate department, and high-level use case, such as edge versus core, and manage your Distributed Cloud connected deployment for the domain through that Google Cloud project.

The Google Cloud project lets you perform the following management tasks:

  * Order Distributed Cloud connected hardware.
  * Configure Distributed Cloud connected clusters and register them in a fleet.
  * Manage software rollouts.
  * Manage Distributed Cloud connected data in Cloud Storage.
  * Manage Distributed Cloud connected credentials in Secret Manager.
  * Manage Distributed Cloud connected logs and metrics in Cloud Monitoring.



Your exact Google Cloud project topology depends on your business requirements. We recommend that you avoid cross-project dependencies and always create and use resources inside each Google Cloud project.

Hardware ordered within a specific Google Cloud project is always managed in that Google Cloud project.

### Select the target Google Cloud region

The specific choice of Google Cloud regions for your Distributed Cloud connected deployment depends on your business requirements and legal ramifications of your target geographical locations.

If you're integrating your Distributed Cloud connected deployment into an existing multi-region Google Cloud footprint, we recommend that you map each Distributed Cloud connected zone to the Google Cloud region hosting that zone's dependencies.

If you're not integrating Distributed Cloud connected deployment with an existing Google Cloud footprint, we recommend that you diversify your Google Cloud region selection for increased reliability. For example:

  * Map each Distributed Cloud connected zone to its nearest supported Google Cloud region. This limits the impact of a management plane fault to a single geographic region.
  * Stripe your Distributed Cloud connected across several Google Cloud regions. This limits the number of Distributed Cloud connected zones that can be affected by a management plane fault; however, the impacted zones are spread over a larger geographical region.

Distributed Cloud connected supports the following Google Cloud regions:

  * **Asia** : `asia-east1`, `asia-east2`, `asia-northeast1`, `asia-northeast3`, `asia-south1`, `asia-south2`, `asia-southeast1`, `asia-southeast2`

  * **Europe** : `europe-central2`, `europe-north1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `europe-west6`, `europe-west8`, `europe-west9`

  * **Middle East** : `me-central1`, `me-west1`

  * **Oceania** : `australia-southeast1`

  * **North America** : `northamerica-northeast1`, `northamerica-northeast2`, `us-central1`, `us-central2`, `us-east1`, `us-east4`, `us-east5`, `us-east7`, `us-south1`, `us-west1`, `us-west2`, `us-west3`, `us-west4`, `us-west8`

  * **South America** : `southamerica-east1`, `southamerica-west1`




### Set up your environment

Before you begin, complete the following prerequisites:

  1. [Set up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

  2. Install the GDC Hardware Management API client library using the following command:
         
         python3 -m pip install google-cloud-gdchardwaremanagement
         

  3. Enable the [GDC Hardware Management API](https://console.cloud.google.com/apis/api/gdchardwaremanagement.googleapis.com) on the target Google Cloud project.




### Create and submit a Distributed Cloud connected hardware order using the GDC Hardware Management API

The steps in this section are examples that illustrate how to create and submit an `Order` resource to Google using the GDC Hardware Management API. To complete the steps in this section, you must have the [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`) role in your Google Cloud project. For details on the available types and methods, see the [Python client library reference](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).

  1. Create an `Order` resource. For example:
         
         import datetime
         from google.cloud import [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest)
         from google.protobuf.timestamp_pb2 import Timestamp
         from google.type import postal_address_pb2
         
         client = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[GDCHardwareManagementClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.html)()
         
         contact = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Contact](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Contact.html)(
             given_name="John",
             family_name="Customer",
             email="jcustomer@example.com",
             phone="+1 123 456 7890",
         )
         
         organization_contact = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[OrganizationContact](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact.html)(
             address=postal_address_pb2.PostalAddress(
                 organization="Example Organization",
                 address_lines=["1800 Amphibious Blvd."],
                 locality="Mountain View",
                 administrative_area="CA",
                 postal_code="94045",
                 region_code="US",
             ),
             contacts=[contact],
         )
         
         order = [gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[Order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order.html)(
             organization_contact=organization_contact,
             customer_motivation="I like Google Distributed Cloud!",
             fulfillment_time=Timestamp(
                 seconds=int(datetime.datetime(2024, 11, 22, 9, 0).timestamp()),
             ),
             region_code="US",
         )
         
         create_order_response = client.[create_order](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.html#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_order)(
             request=[gdchardwaremanagement_v1alpha](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest).[CreateOrderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.CreateOrderRequest.html)(
                 parent="projects/myProject/locations/us-east1",
                 order_id="myOrderID",
                 order=order,
             ),
         ).result()

Your order is now in `DRAFT` state and has been assigned a resource name stored in the `create_order_response.name` field. Use this resource name when modifying or tracking the status of this order.

  2. Create a `Site` resource. For example:
         
         site = gdchardwaremanagement_v1alpha.Site(
             organization_contact=organization_contact,
             google_maps_pin_uri="https://maps.app.goo.gl/z7bE8z8fffg6Sri46",
         )
         
         create_site_response = client.create_site(
             request=gdchardwaremanagement_v1alpha.CreateSiteRequest(
                 parent="projects/myProject/locations/us-east1",
                 site_id="mySite",
                 site=site,
             ),
         ).result()

  3. Create a `Zone` resource. For example:
         
         zone = gdchardwaremanagement_v1alpha.Zone(
             contacts=[contact],
             network_config=gdchardwaremanagement_v1alpha.ZoneNetworkConfig(
                 management_ipv4_subnet=gdchardwaremanagement_v1alpha.Subnet(
                     address_range="192.0.2.0/24",
                     default_gateway_ip_address="192.0.2.1",
                 ),
                 machine_mgmt_ipv4_range="192.0.2.8/29",
                 kubernetes_ipv4_subnet=gdchardwaremanagement_v1alpha.Subnet(
                     address_range="203.0.113.0/24",
                     default_gateway_ip_address="203.0.113.1",
                 ),
                 kubernetes_node_ipv4_range="203.0.113.8/29",
                 kubernetes_control_plane_ipv4_range="203.0.113.16/29",
             ),
         )
         
         create_zone_response = client.create_zone(
             request=gdchardwaremanagement_v1alpha.CreateZoneRequest(
                 parent="projects/myProject/locations/us-east1",
                 zone_id="myZone",
                 zone=zone,
             ),
         ).result()

  4. Create the `Hardware` resources. You must specify a unique `hardware_id` value for each machine in your Distributed Cloud connected deployment. For example:
         
         from google.type import date_pb2
         
         hardware = gdchardwaremanagement_v1alpha.Hardware(
             order=create_order_response.name,
             site=create_site_response.name,
             zone=create_zone_response.name,
             config=gdchardwaremanagement_v1alpha.HardwareConfig(
                 sku="projects/myProject/locations/us-east1/skus/gdce-server-l",
                 power_supply=gdchardwaremanagement_v1alpha.types.PowerSupply.POWER_SUPPLY_AC,
             ),
             physical_info=gdchardwaremanagement_v1alpha.HardwarePhysicalInfo(
                 power_receptacle=gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.PowerReceptacleType.NEMA_5_15,
                 network_uplink=gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.NetworkUplinkType.RJ_45,
                 voltage=gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Voltage.VOLTAGE_110,
                 amperes=gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Amperes.AMPERES_15,
             ),
             installation_info=gdchardwaremanagement_v1alpha.HardwareInstallationInfo(
                 rack_location="Floor 2, Room 201, Row 7, Rack 3",
                 power_distance_meters=2,
                 switch_distance_meters=2,
                 rack_unit_dimensions=gdchardwaremanagement_v1alpha.Dimensions(
                     width_inches=19,
                     height_inches=1.75,
                     depth_inches=30,
                 ),
                 rack_space=gdchardwaremanagement_v1alpha.RackSpace(
                     start_rack_unit=12,
                     end_rack_unit=12,
                 ),
                 rack_type=gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo.RackType.FOUR_POST,
             ),
             requested_installation_date=date_pb2.Date(year=2024, month=11, day=22),
         )
         
         create_hardware_response = client.create_hardware(
             request=gdchardwaremanagement_v1alpha.CreateHardwareRequest(
                 parent="projects/myProject/locations/us-east1",
                 hardware_id="machineHardwareID",
                 hardware=hardware,
             ),
         ).result()

  5. Submit the `Order` resource to Google:
         
         submit_order_response = client.submit_order(
             request=gdchardwaremanagement_v1alpha.SubmitOrderRequest(
                 name=create_order_response.name,
                 type_=gdchardwaremanagement_v1alpha.types.SubmitOrderRequest.Type.INFO_COMPLETE,
             ),
         ).result()

The [submission type](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders/submit#type) of `INFO_COMPLETE` indicates that you have provided all of the required information in the `Zone` and `Hardware` resources. If any field values are missing, the submission fails with an error message describing the problem. If you want to initiate a conversation with Google without fully populating the order, submit it with an `INFO_PENDING` status to skip these validations.




### Testing

If you would like to submit a test order, contact Google to get access to a sandbox environment. After your project or organization has been granted access, you can use a test SKU identifiable by the `fake-` prefix. Test orders progress through the stages described earlier but don't trigger monetary charges or a hardware shipment.

### Troubleshooting

This section describes the most commonly encountered errors, their causes, and available remedies.

#### Error: `400 FAILED_PRECONDITION`

If you receive a `400` error code with a `FAILED_PRECONDITION` status in response to your API call, check that your request is valid for the operation you are attempting to complete. Examples of invalid requests include submitting an `Order` resource with missing fields or values, or attempting to delete a `Hardware` resource associated with a previously submitted `Order` resource.

#### Error: `400 INVALID_ARGUMENT`

If you receive a `400` error code with an `INVALID_ARGUMENT` status in response to your API call, check for incorrect field names and values that don't match their expected types, or missing values. You might also receive this error if you use an `updateMask` in a `PATCH` request and one or more fields specified in the `updateMask` is invalid.

To remedy this issue, see [GDC Hardware Management API](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest) to verify that all field names and values are correct, including formatting. If using a JSON payload, confirm that all required information is included in the payload.

#### Error: `401 UNAUTHENTICATED`

If you receive a `401` error code with an `UNAUTHENTICATED` status in response to your API call, check your authentication configuration. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

#### Error: `403 PERMISSION_DENIED`

If you receive a `403` error code with a `PERMISSION_DENIED` status in response to your API call, check whether the service account used to make the API call has sufficient privileges to access the target objects and resources. Also verify that the credentials are correct and not expired.

#### Error: `404 NOT_FOUND`

If you receive a `404` error code with a `NOT_FOUND` status in response to your API call, check that the resource names and path specified in your API call are valid. See [GDC Hardware Management API](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest) to verify that your request URL is structured correctly and that all fields included in the URL are valid.

## Track your order status

You can track the status of your order in the Google Cloud console on the **Orders** page. The following table lists the possible statuses and their meaning.

UI Status | Meaning  
---|---  
**Draft** | The order is saved as draft.  
**In review** | The order is submitted and is being reviewed by Google.  
**Accepted** | Google accepted the order for fulfillment.  
**Building Hardware** | The hardware is being built and provisioned at Google or at its partner facility.  
**Shipping Hardware** | The hardware is being shipped to the provided site address.  
**Installing** | The hardware is being installed at the provided site address.  
**In progress** | Order is partially complete. For example, some hardware has been delivered and installed.  
**Completed** | The order is complete.  
**Missing info** | Additional information is needed from you.  
**Action required** | Immediate attention is required due to a critical underlying issue.  
**Cancelled** | The order was rejected.  
  
## What's next

  * [Deploy workloads on Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
