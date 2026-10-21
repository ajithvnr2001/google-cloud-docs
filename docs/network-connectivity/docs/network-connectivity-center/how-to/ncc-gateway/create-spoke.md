---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke/
title: Create an NCC Gateway spoke \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:36:00.709377+00:00
---

# Create an NCC Gateway spoke  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Create an NCC Gateway spoke Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create an NCC Gateway spoke resource in a specified region connected to the Network Connectivity Center (NCC) hub.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, select the hub location as follows:

     * To attach the new spoke to a hub in the same project, select **In project` PROJECT_NAME`** and select the hub name from the list.
     * Choose a **Topology** :
     * For a greenfield deployment of NCC Gateway, choose **Hybrid inspection topology**
     * For a [brownfield deployment](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-to-ncc-gw-spoke), you can use the existing **Star** or **Mesh** topology.
  6. Enter a **Spoke name** and optionally, a **Description**.

  7. Select **NCC Gateway** as the **Spoke type**.

If you're using hybrid inspection topology, an NCC Gateway spoke can only be in the gateways group. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).

  8. Choose the **Region** that you want the gateway spoke to be deployed in.

  9. Choose the **Aggregated capacity** of the gateway spoke, in Gbps.

Supported capacity values are 1, 10, or 100.

  10. In the **Reserved IP range** field, enter a block of IP address ranges used to allocate supporting infrastructure for this gateway—for example, `10.1.2.0/23`.

The IP address block must be a `/23` range. This IP address block must not overlap with subnets in any spoke or peer network that the gateway can communicate with.

IP address ranges can't be within the `100.64.0.0/10` block as it is a space reserved for use by the internet service provider (ISP) infrastructure.

You can't change assigned IP address ranges. Some IP address ranges are reserved for SSE partners.

**Note:** When deploying multiple NCC Gateway in different regions on the same hub, you must ensure that the reserved IP range is unique for each regional gateway instance.
  11. Optional: to add routes advertised from NCC Gateway to the hub, in the **Routes advertised from NCC Gateway to hub** section, do the following:

     * Enter the **Route name**.
     * Enter an **IP range** for the route.
     * Enter the **Priority** for the route.

To add additional routes, click **Add route** and repeat the process starting with entering a **Route name**.

  12. Click **Done**.

  13. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.

  14. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.




After the spoke is created, you can associate the spoke with a Cloud Router. To do so, click the spoke that you just created. On the **Spoke details** page, click **Add Cloud Router**. Then, follow the instructions to [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments#create-cloud-router).

You can also attach it to Secure Access Connect by clicking **Secure Access Connect attachments** and following the instructions to [Create a Secure Access Connect attachment](https://docs.cloud.google.com/secure-access-connect/docs/create-attachments).

###  gcloud 

Use the [`gcloud network-connectivity spokes gateways create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/gateways/create):
    
    
    gcloud network-connectivity spokes gateways create SPOKE_NAME \
        --region=REGION \
        --hub=HUB \
        --capacity=CAPACITY \
        --ip-range-reservations=IP_RANGE \
        --group=SPOKE_GROUP
    

Replace the following values:

  * `SPOKE_NAME`: the name of the spoke
  * `REGION`: the region that you want theNCC Gateway to be deployed in
  * `HUB`: the name of the hub for the spoke
  * `CAPACITY`: the capacity of the gateway spoke, in Gbps

Supported capacity values are 1, 10, or 100.

  * `IP_RANGE`: a block of IP address ranges used to allocate supporting infrastructure for this gateway—for example, `10.1.2.0/23`

The IP address block must be a /23 range. This IP address block must not overlap with subnets in any spoke or peer network that the gateway can communicate with.

IP address ranges can't be within the `100.64.0.0/10` block as it is a space reserved for use by the internet service provider (ISP) infrastructure.

You can't change assigned IP address ranges. Some IP address ranges are reserved for SSE partners.

**Note:** When deploying multiple NCC Gateway in different regions on the same hub, you must ensure that the reserved IP range is unique for each regional gateway instance.
  * `SPOKE_GROUP`: the spoke group for your spoke. This can vary based on the topology that you're using for your hub.

    * For a greenfield deployment of NCC Gateway, use hybrid inspection topology
    * For a [brownfield deployment](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-to-ncc-gw-spoke), you can use the existing Star or Mesh topology. For details, about connectivity topologies, see [Connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).



###  API 

To create an NCC Gateway spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
      {
        "hub":"HUB_NAME",
        "location" : LOCATION,
        "gateway": {
           "ip_range_reservation": IP_RANGE,
           "capacity": CAPACITY
           "group": SPOKE_GROUP
        },
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke
  * `SPOKE_NAME`: the name of the spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `LOCATION`: the region that you want the NCC Gateway to be deployed in
  * `IP_RANGE`: a block of IP address ranges used to allocate supporting infrastructure for this gateway—for example, `10.1.2.0/23`

The IP address block must be a /23 range. This IP address block must not overlap with subnets in any spoke or peer network that the gateway can communicate with.

IP address ranges can't be within the `100.64.0.0/10` block as it is a space reserved for use by the internet service provider (ISP) infrastructure.

You can't change assigned IP address ranges. Some IP address ranges are reserved for SSE partners.

**Note:** When deploying multiple NCC Gateway in different regions on the same hub, you must ensure that the reserved IP range is unique for each regional gateway instance.
  * `CAPACITY`: the capacity of the gateway spoke, in Gbps

Supported capacity values are 1, 10, or 100.

  * `SPOKE_GROUP`: the spoke group for your spoke. This group can vary based on the topology that you're using for your hub. For details, see [Connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).




[ Previous arrow_back  Set up NCC and create a hub  ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-hub)

[ Next Connect the Secure Access Connect attachment  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/connect-sac)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
