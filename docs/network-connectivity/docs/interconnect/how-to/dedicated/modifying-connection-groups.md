---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups/
title: Modify connection groups \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:47.331116+00:00
---

# Modify connection groups  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Modify connection groups Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for creating Cloud Interconnect connection groups; creating and adding Cloud Interconnect connections to a connection group; removing connections from a connection group; and deleting connection groups. For more information about Cloud Interconnect connection groups, see [Resiliency and SLA options](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#sla-options) in the Cloud Interconnect overview.

## Create Cloud Interconnect connection groups

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.groups.create`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Create group**.

  3. Specify the details of the Dedicated Interconnect connection group:

     * **Name** : A name for the connection group. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect-group`.
     * **Description** : An optional description of the connection group.
  4. In the **Production SLA** field, select the SLA option that you need for your deployment.

  5. Optional: In the **Group members** field, select **Add interconnects**.

  6. Optional: In the box, select the Cloud Interconnect connections that you want to add to the connection group. Repeat this step for each Cloud Interconnect connection that you want to add to the connection group.

  7. Click **Save**.




###  gcloud 

When you create a new connection group, you specify an intended SLA by using the `--intended-topology-capability` flag with a value of `PRODUCTION_CRITICAL`, `PRODUCTION_NON_CRITICAL`, or `NO_SLA`. In the following example command, you create a connection group called `GROUP_NAME` with an intended SLA of `PRODUCTION_NON_CRITICAL`:
    
    
    gcloud compute interconnects groups create GROUP_NAME \
        --intended-topology-capability PRODUCTION_NON_CRITICAL
    

Note that this new group doesn't yet satisfy your intended SLA because it doesn't have any Cloud Interconnect connections.

## Create Cloud Interconnect connections within a connection group

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectGroups.get`
  * `compute.interconnects.create`
  * `compute.interconnectGroups.update`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Set up physical connection**.

  3. In the **Interconnect type** field, select **Dedicated interconnect connection**.

  4. Click **Continue**.

  5. Select **Order a new Dedicated Interconnect connection**.

  6. Click **Continue**.

  7. In the **Intended SLA** field, select the SLA option that you need for your deployment.

  8. Select **Add this interconnect to an existing group**.

  9. In the **Interconnect group** box, select the Cloud Interconnect connection group to which you want to add the new connection.

  10. Click **Next**.

  11. Specify the details of the Dedicated Interconnect connection:

     * **Name** : A name for the connection. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect`.
     * **Location** : The physical [location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities) where the connection is created. When you create a connection group, you only choose the facility. The location is chosen automatically.
     * **Capacity** : The total capacity of your connection, which is determined by the number and size of the circuits that you order.

**Note:** You can view the estimated cost of your choice in the Google Cloud console page.

Select _one_ of the following options:

       * 1 x 10-Gbps circuit in 10-Gbps increments up to 8 x 10-Gbps (80 Gbps) circuits
       * 1 x 100-Gbps (100 Gbps) circuit
       * 2 x 100-Gbps (200 Gbps) circuits
  12. Click **Next**.

  13. If you require redundancy, specify details for your duplicate connection, and then click **Next**.

  14. Specify your contact information:

     * **Company name** : The name of your organization to put in the LOA as the party authorized to request a connection.
     * **Technical contact** : An email address where notifications about this connection are sent. You don't need to enter your own address; you are included in all notifications. You can specify only one address.

If you are creating a connection through [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), specifying a **Technical contact** is required. Workforce Identity Federation is in [Preview](https://cloud.google.com/products#product-launch-stages).

  15. Review your order. Check that your connection details and contact information are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.

  16. On the order confirmation page, review the next steps, and then click **Done**.




###  gcloud 

In the following example, you create Cloud Interconnect connections called `CONNECTION_1` and `CONNECTION_2` in the connection group called `GROUP_NAME`. You provide the `--interconnect` flag, with a unique Cloud Interconnect name and any other fields that you want to be different for each new Cloud Interconnect connection that you want to create in the group.

In the following example, each Cloud Interconnect connection has a different name and description, but share the same values for all other fields.
    
    
    gcloud compute interconnects groups create-members GROUP_NAME \
        --interconnect-type dedicated \
        --link-type LINK_TYPE \
        --facility FACILITY_NAME \
        --customer-name NAME \
        --noc-contact-email EMAIL_ADDRESS \
        --interconnect "name=CONNECTION_1,description='The first interconnect connection'" \
        --interconnect "name=CONNECTION_2,description='The second interconnect connection'"
    

Replace the following values:

  * `GROUP_NAME`: the name of your connection group
  * `LINK_TYPE`: 
    * If you want your Dedicated Interconnect connection to be made up of 10-Gbps circuits, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_10G_LR`.
    * If you want your connection to be made up of 100-Gbps circuits, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_100G_LR`.
  * `FACILITY_NAME`: the name of the facility in which you want to create the Dedicated Interconnect connections, without `-zone1` or `zone2`. The Dedicated Interconnectconnection group automatically selects the best zones for each Interconnect to maximize your resiliency. You can find facility names in the [colocation facility table](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities#locations-table).
  * `NAME`: the name of your organization to put in the LOA as the party authorized to request a connection
  * `EMAIL_ADDRESS`: an optional email address for the NOC contact. You can specify only one email address—you don't need to enter your own address because you are included in all notifications. If you are creating a connection through [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), providing an email address with the `‑‑noc-contact-email` flag is required. Workforce Identity Federation is in [Preview](https://cloud.google.com/products#product-launch-stages).
  * `CONNECTION_1`: the name of the first Cloud Interconnect connection.
  * `CONNECTION_2`: the name of the second Cloud Interconnect connection.



In the following alternative example the Cloud Interconnect connections have the same description, but different facilities:
    
    
    gcloud compute interconnects groups create-members GROUP_NAME \
        --interconnect-type dedicated \
        --description "Both will have this same description" \
        --link-type LINK_TYPE \
        --customer-name NAME \
        --noc-contact-email EMAIL_ADDRESS \
        --interconnect "name=CONNECTION_1,facility=FACILITY_NAME_1" \
        --interconnect "name=CONNECTION_2,facility=FACILITY_NAME_2" \
    

Replace the following values:

  * `GROUP_NAME`: the name of your connection group
  * `LINK_TYPE`: 
    * If you want your Dedicated Interconnect connection to be made up of 10-Gbps circuits, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_10G_LR`.
    * If you want your connection to be made up of 100-Gbps circuits, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_100G_LR`.
  * `NAME`: the name of your organization to put in the LOA as the party authorized to request a connection
  * `EMAIL_ADDRESS`: an optional email address for the NOC contact. You can specify only one email address—you don't need to enter your own address because you are included in all notifications. If you are creating a connection through [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), providing an email address with the `‑‑noc-contact-email` flag is required. Workforce Identity Federation is in [Preview](https://cloud.google.com/products#product-launch-stages).
  * `CONNECTION_1`: the name of the first Cloud Interconnect connection.
  * `CONNECTION_2`: the name of the second Cloud Interconnect connection.
  * `FACILITY_NAME_1`: the name of the first facility as described in the previous example.
  * `FACILITY_NAME_2`: the name of the second facility as described in the previous example.



## Add existing Cloud Interconnect connections to a group

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



You can add Cloud Interconnect connections to a connection group by editing the group.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. In the **Interconnect groups** field, select the connection group that you want to edit.

  3. Click **Edit**.

  4. In the **Group members** field, select **Add interconnect** , then select the Cloud Interconnect connection that you want to add to the connection group. Repeat this step for each Cloud Interconnect connection that you want to add to the group.

  5. Click **Save**.




###  gcloud 

In the following example command, you add existing connections `CONNECTION_1` and `CONNECTION_2` to the connection group called `GROUP_NAME`:
    
    
    gcloud compute interconnects groups add-members GROUP_NAME \
        --interconnects=CONNECTION_1,CONNECTION_2
    

## Remove Cloud Interconnect connections from a group

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectGroups.get`
  * `compute.interconnectGroups.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



You can remove Cloud Interconnect connections from a connection group by editing the group.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. In the **Interconnect groups** field, select the connection group that you want to edit.

  3. Click **Edit**.

  4. In the **Group members** field, click the box with the Cloud Interconnect connection that you want to remove from the connection group, and either replace the selected connection with another connection or click delete**Delete**.

  5. Click **Save**.




###  gcloud 

In the following example command, you remove connections `CONNECTION_1` and `CONNECTION_2` from the connection group called `GROUP_NAME`:
    
    
    gcloud compute interconnects groups remove-members GROUP_NAME \
        --interconnects=CONNECTION_1,CONNECTION_2
    

## Delete Cloud Interconnect connection groups

Use the instructions in this section to delete a Cloud Interconnect connection group. Note that when you delete a connection group, the Cloud Interconnect connections that are members of the group aren't deleted. To delete Cloud Interconnect connections, see [Delete connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/deleting-interconnects).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectGroups.delete`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. In the **Interconnect groups** field, find the row of the connection group that you want to delete and then click the checkbox next to the group.

  3. Click **Delete** , then click **Delete** again in the confirmation box.

  4. Click **Save**.




###  gcloud 

In the following example command, you delete the connection group named `GROUP_NAME`.
    
    
    gcloud compute interconnects groups delete GROUP_NAME
    

## What's next

  * [View VLAN attachment groups and their details](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-vlans#view_vlan_attachment_groups_and_their_details)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
