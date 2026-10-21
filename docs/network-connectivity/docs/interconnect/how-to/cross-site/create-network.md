---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/create-network/
title: Create a cross-site network \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:13.434142+00:00
---

# Create a cross-site network  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/create-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Create a cross-site network Stay organized with collections  Save and categorize content based on your preferences. 

You can create cross-site networks over connections that have [passed all tests](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections) and are ready to use.

Billing for a cross-site network starts when you create wires and stops when you delete them.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.use`
  * `compute.crossSiteNetworks.create`
  * `compute.wireGroups.create`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



To create a cross-site network, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?tab=cross-site)

  2. On the **Cross-site networks** tab, click **Create cross-site network**.

  3. Specify the details of the cross-site network:

     * **Name** : a name for the cross-site network
     * **Description** : an optional description of the cross-site network
  4. Click **Next**.

  5. Specify the basic details of the wire group to add to the cross-site network:

     * **Name** : a name for the wire group.
     * **Description** : an optional description of the wire group.
  6. Select either **VLAN mode** or **Port mode** for your wire group. If necessary, review [Traffic modes](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#modes) in the Cross-Site Interconnect overview. 

  7. In the **Unmetered bandwidth** field, enter the unmetered bandwidth, in Gbps, for the wire group.

You can't configure bandwidth that exceeds the following:

     * Your quota between a given pair of metros or the limit for a given wire. If you haven't already, follow the instructions to [check quotas and limits for bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota).
     * The Cross-Site Interconnect connection capacity.

For additional considerations for configuring this field, see [Wire bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#bandwidth).

  8. If you configured **Port mode** , review the **Failure detection** field. To enable failure detection, select the **Disable port** checkbox.

When you enable failure detection, Google Cloud continuously monitors each wire and disables a wire if it loses connectivity so that you can failover to an alternate path, such as another healthy wire in the group.

  9. Choose whether to allocate the wire group's bandwidth setting to each wire or to share the bandwidth between all wires in the group.

     * **Allocate per wire**. The unmetered bandwidth is allocated to each wire in the group. Consider the cost implications, because per-wire allocation reserves double the total bandwidth compared to shared allocation.
     * **Shared with wire group**. The unmetered bandwidth is divided equally between each wire in the group. However, dynamic throttling allocates unused unmetered bandwidth to other wires in the group.
  10. Click **Next**.

  11. Specify the Cross-Site Interconnect connections over which to create your cross-site network.

     1. Depending on your topology, select the connection or redundant connections that you created for your first site, **Site A**.
     2. Depending on your topology, select the connection or redundant connections that you created for your second site, **Site B**.
  12. Click **Next**.

  13. If you configured **VLAN mode** , specify **VLAN tags** for each wire in your wire group by entering an integer from `2` to `4093`.

You can't enter a VLAN tag value that is already in use on the same Cross-Site Interconnect connection.

  14. Review the configuration of your cross-site network, and then click **Create network**.

  15. If necessary, create additional wire groups in the cross-site network by following the instructions to [add a wire group](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/modify-network#add-wire-group). You might want to add a wire group for the following reasons:

     * To add more bandwidth between site A and site B.

     * To connect additional sites. For example, you can add wire groups that connect an additional site, site C, to site A and site B.




###  gcloud 

#### Google Cloud CLI procedure overview

To complete the procedure for creating a cross-site network by using the Google Cloud CLI, do the following:

  1. Create a cross-site network
  2. Add a wire group to the cross-site network
  3. Add an endpoint and connections for site A to the wire group: 
     1. Add an endpoint that represents site A
     2. Add connection A1
     3. Add connection A2
  4. Add an endpoint and connections for site B to the wire group: 
     1. Add an endpoint that represents site B
     2. Add connection B1
     3. Add connection B2



You can create additional wire groups in the cross-site network depending on your use case:

  * To add more bandwidth between site A and site B, repeat the steps for creating a wire group and adding endpoints and connections.

  * To connect additional sites, repeat the steps for each pair of sites that you want to connect. For example, you can create an additional wire group that connects site A to site C, and another that connects site B to site C.




You can also [add more wire groups later](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/modify-network#add-wire-group).

#### 1\. Create a cross-site network

To create a cross-site network, use the [`gcloud compute interconnects cross-site-networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/cross-site-networks/create).
    
    
      gcloud compute interconnects cross-site-networks create CROSS_SITE_NETWORK_NAME \
          [--description=DESCRIPTION]
    

Replace the following values:

  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network
  * `DESCRIPTION`: an optional description for the cross-site network



#### 2\. Add a wire group

To add a wire group, use the [`gcloud compute interconnects wire-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/create).
    
    
      gcloud compute interconnects wire-groups create WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --bandwidth-unmetered=UNMETERED_BANDWIDTH \
          --bandwidth-allocation=BANDWIDTH_ALLOCATION \
          --fault-response=FAILURE_DETECTION \
          [--description=DESCRIPTION]
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to add the wire group to



  * `UNMETERED_BANDWIDTH`: the unmetered bandwidth for the wire group in Gbps. The bandwidth that you specify is allocated to each wire in the group.

You can't configure bandwidth that exceeds the following:

    * Your quota between a given pair of metros or the limit for a given wire. If you haven't already, follow the instructions to [check quotas and limits for bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota).
    * The Cross-Site Interconnect connection capacity.

For additional considerations for configuring this field, see [Wire bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#bandwidth).

  * `BANDWIDTH_ALLOCATION`: use this flag to set the bandwidth allocation scope, which can have either of the following values:

    * `ALLOCATE_PER_WIRE`, which provides a separate unmetered bandwidth allocation for each wire in the group.
    * `SHARED_WITH_WIRE_GROUP`, which has one unmetered bandwidth allocation that is divided across each wire in the group. Dynamic throttling reallocates unused bandwidth from unutilized or underutilized wires to other wires in the group.
  * `FAILURE_DETECTION`: use this flag for port mode configurations only. To enable failure detection, enter `DISABLE_PORT`. Otherwise, enter `NONE`.

When you enable failure detection, Google Cloud continuously monitors each wire and disables a wire if it loses connectivity so that you can failover to an alternate path, such as another healthy wire in the group.

  * `DESCRIPTION`: an optional description of the wire group.




#### 3a. Add an endpoint for site A

To add an endpoint to the wire group that represents your first site, or _site A_ , use the [`gcloud compute interconnects wire-groups add-endpoint` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-endpoint).
    
    
      gcloud compute interconnects wire-groups add-endpoint WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_A_LABEL
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_A_LABEL`: a label for the endpoint, such as `ashburn`



#### 3b. Add connection A1

To add the first Cross-Site Interconnect connection to the wire group for site A, or _connection A1_ , use the [`gcloud compute interconnects wire-groups add-interconnect` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-interconnect).
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_A_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_A1_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_A1 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_A_LABEL`: the existing label that you specified when you created the endpoint for site A
  * `INTERCONNECT_CONNECTION_A1_LABEL`: a new label for the first Cross-Site Interconnect connection that you created for site A
  * `INTERCONNECT_CONNECTION_A1`: the connection that you created for site A. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cross-Site Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify your own VLAN tag values, enter an integer from `2` to `4093`. VLAN tags must be the same for both endpoints of a wire. You can't enter a VLAN tag value that is already in use on the Cloud Interconnect connection.




#### 3c. Add connection A2
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_A_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_A2_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_A2 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_A_LABEL`: the existing label that you specified when you created the endpoint for site A
  * `INTERCONNECT_CONNECTION_A2_LABEL`: a new label for the redundant Cross-Site Interconnect connection that you created for site A
  * `INTERCONNECT_CONNECTION_A2`: the redundant connection that you created for site A. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cross-Site Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify your own VLAN tag values, enter an integer from `2` to `4093`. VLAN tags must be the same for both endpoints of a wire. You can't enter a VLAN tag value that is already in use on the Cloud Interconnect connection.




#### 4a. Add an endpoint for site B

To add an endpoint to the wire group that represents your second site, or _site B_ , use the [`gcloud compute interconnects wire-groups add-endpoint` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-endpoint).
    
    
      gcloud compute interconnects wire-groups add-endpoint WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_B_LABEL
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_B_LABEL`: a label for the endpoint, such as `chicago`



#### 4b. Add connection B1

To add a Cross-Site Interconnect connection to the wire group for site B, or _Interconnect connection B1_ , use the [`gcloud compute interconnects wire-groups add-interconnect` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-interconnect).

**Note:** Adding connections to site B can take several minutes to complete.
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_B_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_B1_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_B1 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_B_LABEL`: the existing label that you specified when you created the endpoint for site B
  * `INTERCONNECT_CONNECTION_B1_LABEL`: a new label for the Cross-Site Interconnect connection that you created for site B
  * `INTERCONNECT_CONNECTION_B1`: the connection that you created for site B. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cross-Site Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify your own VLAN tag values, enter an integer from `2` to `4093`. VLAN tags must be the same for both endpoints of a wire. You can't enter a VLAN tag value that is already in use on the Cloud Interconnect connection.




#### 4c. Add connection B2

**Note:** Adding connections to site B can take several minutes to complete.
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_B_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_B2_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_B2 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following values:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously.
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to add the wire group to.
  * `ENDPOINT_B_LABEL`: the existing label that you specified when you created the endpoint for site A.
  * `INTERCONNECT_CONNECTION_B2_LABEL`: a new label for the redundant Cross-Site Interconnect connection that you created for site B.
  * `INTERCONNECT_CONNECTION_B2`: the redundant connection that you created for site B. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cross-Site Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify your own VLAN tag values, enter an integer from `2` to `4093`. VLAN tags must be the same for both endpoints of a wire. You can't enter a VLAN tag value that is already in use on the Cloud Interconnect connection.




[ Previous arrow_back  Test connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections)

[ Next Configure on-premises routers  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/configure-onprem-routers)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
