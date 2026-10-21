---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/modify-network/
title: Modify a cross-site network \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:13.921780+00:00
---

# Modify a cross-site network  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/modify-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Modify a cross-site network Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to modify a cross-site network by updating or adding wire groups.

## Before you begin

Consider the following before you modify a cross-site network:

  * **Bandwidth quotas and limits**

    * Increasing bandwidth usage between two metros by updating an existing wire group or adding a new wire group requires that you have enough bandwidth quota between the two metros. You can't add bandwidth if doing so exceeds your quota for the _Wire groups unmetered bandwidth per Cloud Interconnect metro pair_.

    * The bandwidth that you specify when updating or adding a wire group must not exceed the limit for the _Maximum bandwidth per wire_.

Review [Check bandwidth quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota) and request an increase if necessary.

  * **Connection capacity and support for multiple wire groups**

    * Increasing bandwidth usage by updating an existing wire group or adding a new wire group requires that you have Cross-Site Interconnect connections with sufficient capacity. If you plan to use existing connections, you must ensure that their capacity isn't already fully used by existing wire groups.

To view both the provisioned and effective capacity of a connection, see [View connection details](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-connections). If necessary, [order new connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections).

    * You can create multiple wire groups that use the same Cross-Site Interconnect connections if the wire groups are in VLAN mode. In port mode, you can't use the same Cross-Site Interconnect connection for more than one wire group. For more information, see [Traffic modes](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#modes).

  * **Duration of operations that add or remove wires**

    * When you initiate an operation that adds or removes a wire, the operation can take several minutes to complete. For example, if you are adding a wire group to your cross-site network, then running the Google Cloud CLI commands to add connections B1 and B2 can take several minutes to complete because Google Cloud provisions the wires A1-B1 and A2-B2.



## Add a wire group

This section describes how to add a wire group to an existing cross-site network.

###  Console 

To add a wire group to an existing cross-site network, do the following:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the cross-site network to which you want to add a wire group.

  3. Click **Add wire group**.

  4. Specify the basic details of the wire group to add to the cross-site network.

     * **Name** : a name for the wire group
     * **Description** : an optional description of the wire group
  5. Select either **VLAN mode** or **Port mode** for your wire group. If necessary, review [Traffic modes](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#modes). 

  6. If you configured **Port mode** , review the **Failure detection** field. To enable failure detection, select the **Disable port** checkbox.

When you enable failure detection, Google Cloud continuously monitors each wire and disables a wire if it loses connectivity so that you can fail over to an alternate path, such as another healthy wire in the group.

  7. In the **Unmetered bandwidth** field, enter the unmetered bandwidth, in Gbps, for the wire group.

You can't configure bandwidth that exceeds the following:

     * Your quota between a given pair of metros or the limit for a given wire. If you haven't already, follow the instructions to [check quotas and limits for bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota).
     * The Cross-Site Interconnect connection capacity.

For additional considerations for configuring this field, see [Wire bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#bandwidth).

  8. Choose whether to allocate the wire group's bandwidth setting to each wire or to share the bandwidth between all wires in the group.

     * **Allocate per wire**. The unmetered bandwidth is allocated to each wire in the group.
     * **Shared with wire group**. The unmetered bandwidth is divided equally between each wire in the group. However, dynamic throttling allocates unused unmetered bandwidth to other wires in the group.
  9. Click **Next**.

  10. Specify the Cross-Site Interconnect connections over which to create your cross-site network.

     1. Select the connections that you created for your first site, **Site A**.
     2. Select the connections that you created for your second site, **Site B**.
  11. Click **Next**.

  12. If you configured **VLAN mode** , specify **VLAN tags** for each wire in your wire group by entering an integer from `2` to `4093`.

You can't enter a VLAN tag value that is already in use on the same Cross-Site Interconnect connection.

  13. Review the configuration of your wire group, and then click **Create wire group**.




###  gcloud 

#### Google Cloud CLI procedure overview

To complete the procedure for adding a wire group to an existing cross-site network by using the Google Cloud CLI, do the following:

  1. Add a wire group to your cross-site network
  2. Add an endpoint and connections for site A to the wire group: 
     1. Add an endpoint that represents site A
     2. Add connection A1
     3. Add connection A2
  3. Add an endpoint and connections for site B to the wire group: 
     1. Add an endpoint that represents site B
     2. Add connection B1
     3. Add connection B2



#### 1\. Add a wire group

To add a wire group, use the [`gcloud compute interconnects wire-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/create).
    
    
      gcloud compute interconnects wire-groups create WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --bandwidth-unmetered=UNMETERED_BANDWIDTH \
          --bandwidth-allocation=BANDWIDTH_ALLOCATION \
          --fault-response=FAILURE_DETECTION \
          [--description=DESCRIPTION]
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group.
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to add the wire group to. 


* `UNMETERED_BANDWIDTH`: the unmetered bandwidth for the wire group in Gbps. The bandwidth that you specify is allocated to each wire in the group.

You can't configure bandwidth that exceeds the following:

  * Your quota between a given pair of metros or the limit for a given wire. If you haven't already, follow the instructions to [check quotas and limits for bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota).
  * The Cross-Site Interconnect connection capacity.



For additional considerations for configuring this field, see [Wire bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#bandwidth).

* `BANDWIDTH_ALLOCATION`: use this flag to set the bandwidth allocation scope, which can have either of the following values:

  * `ALLOCATE_PER_WIRE`, which provides a separate unmetered bandwidth allocation for each wire in the group.
  * `SHARED_WITH_WIRE_GROUP`, which has one unmetered bandwidth allocation that is divided across each wire in the group. Dynamic throttling reallocates unused bandwidth from unutilized or underutilized wires to other wires in the group.


* `FAILURE_DETECTION`: use this flag for port mode configurations only. To enable failure detection, enter `DISABLE_PORT`. Otherwise, enter `NONE`.

When you enable failure detection, Google Cloud continuously monitors each wire and disables a wire if it loses connectivity so that you can fail over to an alternate path, such as another healthy wire in the group.

* `DESCRIPTION`: an optional description of the wire group.

#### 2a. Add an endpoint for site A

To add an endpoint to the wire group that represents your first site, or _site A_ , use the [`gcloud compute interconnects wire-groups add-endpoint` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-endpoint).
    
    
      gcloud compute interconnects wire-groups add-endpoint WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_A_LABEL
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_A_LABEL`: a label for the endpoint, such as `ashburn`



#### 2b. Add connection A1

To add the first Cross-Site Interconnect connection to the wire group for site A, or _connection A1_ , use the [`gcloud compute interconnects wire-groups add-interconnect` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-interconnect).
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_A_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_A1_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_A1 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously.
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group.
  * `ENDPOINT_A_LABEL`: the existing label that you specified when you created the endpoint for site A.
  * `INTERCONNECT_CONNECTION_A1_LABEL`: a new label for the first Cross-Site Interconnect connection that you created for site A.
  * `INTERCONNECT_CONNECTION_A1`: the connection that you created for site A. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cross-Site Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify VLAN tag values manually, enter one tag value, such as `1000`. This VLAN tag is used for the wire between connections A1 and B1 (wire A1-B1). A VLAN tag value must be an integer from `2` to `4093`. VLAN tags must be the same for both endpoints of a wire. You can't enter a VLAN tag value that is already in use on the Cloud Interconnect connection.




#### 2c. Add connection A2
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_A_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_A2_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_A2 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously.
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group.
  * `ENDPOINT_A_LABEL`: the existing label that you specified when you created the endpoint for site A.
  * `INTERCONNECT_CONNECTION_A2_LABEL`: a new label for the redundant Cross-Site Interconnect connection that you created for site A.
  * `INTERCONNECT_CONNECTION_A2`: the redundant connection that you created for site A. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cloud Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`. To specify VLAN tag values manually, enter one tag value, such as `1000`. This VLAN tag is used for the wire between connections A1 and B1 (wire A1-B1). A VLAN tag value must be an integer from `2` to `4093`. VLAN tags must be the same for both endpoints of a wire. You can't enter a VLAN tag value that is already in use on the Cloud Interconnect connection.




#### 3a. Add an endpoint for site B

To add an endpoint to the wire group that represents your second site, or _site B_ , use the [`gcloud compute interconnects wire-groups add-endpoint` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-endpoint).
    
    
      gcloud compute interconnects wire-groups add-endpoint WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_B_LABEL
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_B_LABEL`: a label for the endpoint, such as `chicago`



#### 3b. Add connection B1

To add a Cross-Site Interconnect connection to the wire group for site B, or _connection B1_ , use the [`gcloud compute interconnects wire-groups add-interconnect` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/add-interconnect).

**Note:** Adding connections to site B can take several minutes to complete.
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_B_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_B1_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_B1 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_B_LABEL`: the existing label that you specified when you created the endpoint for site B
  * `INTERCONNECT_CONNECTION_B1_LABEL`: a new label for the Cross-Site Interconnect connection that you created for site B
  * `INTERCONNECT_CONNECTION_B1`: the connection that you created for site B. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cloud Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify VLAN tag values manually, enter the same tag value that you specified previously for wire A1-B1.




#### 3c. Add connection B2

**Note:** Adding connections to site B can take several minutes to complete.
    
    
      gcloud compute interconnects wire-groups add-interconnect WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          --endpoint-label=ENDPOINT_B_LABEL \
          --interconnect-label=INTERCONNECT_CONNECTION_B2_LABEL \
          --interconnect=INTERCONNECT_CONNECTION_B2 \
          --vlan-tags=TRAFFIC_MODE
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group that you created previously
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network to which you are adding a wire group
  * `ENDPOINT_B_LABEL`: the existing label that you specified when you created the endpoint for site A
  * `INTERCONNECT_CONNECTION_B2_LABEL`: a new label for the redundant Cross-Site Interconnect connection that you created for site B.
  * `INTERCONNECT_CONNECTION_B2`: the redundant connection that you created for site B. You can specify the connection by its name, partial URI, or full URI. See the following examples: 
    * `my-connection`
    * `projects/my-project/global/interconnects/my-connection`
    * `https://compute.googleapis.com/compute/v1/projects/my-project/global/interconnects/my-connection`
  * `TRAFFIC_MODE`: the traffic mode configuration for the wires that use this Cloud Interconnect connection:

    * To configure port mode, enter `-1`.
    * To configure VLAN mode, choose one of the following:

      * To auto-allocate VLAN tag values, enter `0`.
      * To specify VLAN tag values manually, enter the same tag value that you specified previously for wire A1-B1.




## Update a wire group

This section describes how to update the following properties of an existing wire group:

  * The description
  * Whether the wire group is enabled or disabled
  * The unmetered bandwidth
  * The unmetered bandwidth allocation method
  * Whether failure detection is enabled or disabled (applies to port mode only)



To change the wire group traffic mode, see Change the traffic mode of a wire group.

###  Console 

To update a wire group in a cross-site network, do the following:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the wire group that you want to update.

  3. On the **Wire group details** page, click **Edit** , and update the following fields as needed:

     * **Description** : The description of the wire group.

     * **Admin enabled state** : Whether the wire group is enabled or disabled. Disabling a wire group stops all traffic through the wire group.

     * **Unmetered bandwidth** : The unmetered bandwidth, in Gbps, for the wire group.

You can't configure bandwidth that exceeds the following:

       * Your quota between a given pair of metros or the limit for a given wire. If you haven't already, follow the instructions to [check quotas and limits for bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota).
       * The Cross-Site Interconnect connection capacity.

For additional considerations for configuring this field, see [Wire bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#bandwidth).

     * **Allocation method** : whether to allocate the wire group's bandwidth setting to each wire or to share the bandwidth between all wires in the group.

       * **Allocate per wire**. The unmetered bandwidth is allocated to each wire in the group.
       * **Shared with wire group**. The unmetered bandwidth is divided equally between each wire in the group. However, dynamic throttling allocates unused unmetered bandwidth to other wires in the group.
     * **Failure detection** : Whether failure detection is enabled or disabled. If your wire group is in port mode, you can enable failure detection by selecting the **Disable port** checkbox.

When you enable failure detection, Google Cloud continuously monitors each wire and disables a wire if it loses connectivity so that you can fail over to an alternate path, such as another healthy wire in the group.

  4. After you make your changes, click **Save**.




###  gcloud 

To update a wire group, use the [`gcloud compute interconnects wire-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/update).
    
    
      gcloud compute interconnects wire-groups update WIRE_GROUP_NAME \
          --cross-site-network=CROSS_SITE_NETWORK_NAME \
          [--bandwidth-unmetered=UNMETERED_BANDWIDTH] \
          [--bandwidth-allocation=BANDWIDTH_ALLOCATION] \
          [--fault-response=FAILURE_DETECTION] \
          [--description=DESCRIPTION] \
          [--admin-enabled | --no-admin-enabled]
    

Replace the following:

  * `WIRE_GROUP_NAME`: the name of the wire group
  * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network that contains the wire group
  * Depending on which properties you want to update, use the following flags:

    * `UNMETERED_BANDWIDTH`: the unmetered bandwidth for the wire group in Gbps. The bandwidth that you specify is allocated to each wire in the group.

You can't configure bandwidth that exceeds the following:

      * Your quota between a given pair of metros or the limit for a given wire. If you haven't already, follow the instructions to [check quotas and limits for bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota).
      * The Cross-Site Interconnect connection capacity.

For additional considerations for configuring this field, see [Wire bandwidth](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview#bandwidth).

    * `BANDWIDTH_ALLOCATION`: use this flag to set the bandwidth allocation scope, which can have either of the following values:

    * `ALLOCATE_PER_WIRE`, which provides a separate unmetered bandwidth allocation for each wire in the group.

    * `SHARED_WITH_WIRE_GROUP`, which has one unmetered bandwidth allocation that is divided across each wire in the group. Dynamic throttling reallocates unused bandwidth from unutilized or underutilized wires to other wires in the group.

    * `FAILURE_DETECTION`: Use this flag for port mode configurations only. To enable failure detection, enter `DISABLE_PORT`. Otherwise, enter `NONE`.

When you enable failure detection, Google Cloud continuously monitors each wire and disables a wire if it loses connectivity so that you can fail over to an alternate path, such as another healthy wire in the group.

    * `DESCRIPTION`: the description of the wire group

    * `--admin-enabled | --no-admin-enabled`: whether the wire group is enabled or disabled.

To enable the wire group, use `--admin-enabled`. To disable a wire group, use `--no-admin-enabled`. Disabling a wire group stops all traffic through the wire group.




## Change the traffic mode of a wire group

This section describes how to change the traffic mode of a wire group. In the following procedure, you delete your existing wires and re-create them with the mode that you want by removing and re-adding your Cross-Site Interconnect connections from and to the wire group.

If you need to get the details of your existing wire groups, such as their endpoint and connection labels, follow the instructions for listing and describing wire groups in [View cross-site networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-networks).

###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Cross-site networks** tab, click the name of the wire group whose mode you want to change.

  3. On the **Wire group details page** , click **Edit**.

  4. Click **Advanced settings** , and then select an option in the **Wire group mode** field.

  5. If you selected **VLAN mode** , specify **VLAN tags** for each wire in your wire group by entering an integer from `2` to `4093`.

You can't enter a VLAN tag value that is already in use on the same Cross-Site Interconnect connection.

  6. Click **Save**.




###  gcloud 

  1. Remove the existing connections from your wire group by using the [`gcloud compute interconnects wire-groups remove-interconnect` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/wire-groups/remove-interconnect).

Run the command four times to remove `INTERCONNECT_CONNECTION_A1`, `INTERCONNECT_CONNECTION_A2`, `INTERCONNECT_CONNECTION_B1`, and `INTERCONNECT_CONNECTION_B2`.
         
         gcloud compute interconnects wire-groups remove-interconnect WIRE_GROUP_NAME \
             --cross-site-network=CROSS_SITE_NETWORK_NAME \
             --endpoint-label=ENDPOINT_LABEL \
             --interconnect-label=INTERCONNECT_CONNECTION_LABEL
         

Replace the following:

     * `WIRE_GROUP_NAME`: the name of the wire group
     * `CROSS_SITE_NETWORK_NAME`: the name of the cross-site network
     * `ENDPOINT_LABEL`: the label that you specified when you created the endpoint for the site
     * `INTERCONNECT_CONNECTION_LABEL`: the label that you specified when you added the connection to the wire group
  2. Add the connections to your wire group again.

Complete the following steps and configure the `--vlan-tags` flag according to the traffic mode that you want to use:

     1. Add connection A1
     2. Add connection A2
     3. Add connection B1
     4. Add connection B2



## What's next

  * To learn more about Cross-Site Interconnect, see the [Cross-Site Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
