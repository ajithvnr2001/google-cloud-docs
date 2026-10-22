---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect/
title: Order a Dedicated Interconnect connection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:30.476304+00:00
---

# Order a Dedicated Interconnect connection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order a Dedicated Interconnect connection Stay organized with collections  Save and categorize content based on your preferences. 

Ordering a Dedicated Interconnect connection starts the creation [process](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) of your Dedicated Interconnect connection. When you order a Dedicated Interconnect connection, you specify details such as the capacity and the location of your connection.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Dedicated Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

For more information about the capacities that you can request, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#port-capacity).

## Create a Dedicated Interconnect connection group

Cloud Interconnect connection groups provide information about the reliability of the grouped connections, compared to the requirements for your intended level of reliability. For more information about Cloud Interconnect connection groups, see [Resiliency and SLA options](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#sla-options).

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

### Create connections in a Dedicated Interconnect connection group

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



## Create a Dedicated Interconnect connection

When you create a Dedicated Interconnect connection, we recommend that you follow the steps in the previous sections.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.create`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Set up physical connection**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **Order new Dedicated Interconnect** , and then click **Continue**.

  5. In the **Intended SLA** field, select the SLA option that you need for your deployment.

  6. Optional: If you chose a **Critical production** or **Non-critical production** SLA, you can create the connection within a new Cloud Interconnect connection group:

     1. Select **Create a new group**.
     2. Specify a name and optionally add a description.
     3. Click **Next**.
  7. Specify the details of the Dedicated Interconnect connection:

     * **Name** : a name for the connection. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect`.
     * **Colocation facility** : the physical [location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities) where the connection is created. Your on-premises network must meet Google Cloud's network in this location.
     * **Capacity** : the total capacity of your connection, which is determined by the number and size of the circuits that you order.

**Note:** You can view the estimated cost of your choice on the Google Cloud console page.

Select _one_ of the available capacity options.

  8. Click **Next**.

  9. If you require redundancy, specify details for your duplicate connection, and then click **Next**.

  10. Specify your contact information:

     * **Company name** : the name of your organization to put in the LOA as the party authorized to request a connection.
     * **Technical contact** : an email address where notifications about this connection are sent. You don't need to enter your own address; you are included in all notifications. You can specify only one address.

If you are creating a connection through [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), specifying a **Technical contact** is required. Workforce identity federation is in [Preview](https://cloud.google.com/products#product-launch-stages).

  11. Review your order. Your SLA eligibility is displayed on this page. Check that your connection details and contact information are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.

  12. On the order confirmation page, review the next steps, and then click **Done**.




###  gcloud 

  1. Create a Dedicated Interconnect connection that is a connection type of `DEDICATED`:
         
         gcloud compute interconnects create INTERCONNECT_NAME \
            --customer-name=NAME \
            --interconnect-type=DEDICATED \
            --link-type=LINK_TYPE \
            --location=LOCATION_NAME \
            --requested-link-count=NUMBER_OF_LINKS \
           [--requested-features=MACSEC]
           [--noc-contact-email=EMAIL_ADDRESS] \
           [--description=STRING]
         

Replace the following values:

     * `INTERCONNECT_NAME`: a name for the Dedicated Interconnect connection; this name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect`
     * `NAME`: the name of your organization to put in the LOA as the party authorized to request a connection
     * `LINK_TYPE`: the type of circuits with which you want to configure your connection. Replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_XG_LR`, in which `X` is the capacity that you want. For example, to configure a connection made up of 100-Gbps circuits you replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_100G_LR`. For more information about capacity, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#port-capacity).
     * `LOCATION_NAME`: specifies the location where the Dedicated Interconnect connection is created; to list the names of locations, see [List locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/listing-locations)
     * `NUMBER_OF_LINKS`: number of circuits of type `link-type`; this field combined with `--link-type` determines your total connection capacity. For example, for 2 x 100-Gbps (200 Gbps) circuits, this number would be `2`.
     * `EMAIL_ADDRESS` and `STRING`: optional; for the NOC contact, you can specify only one email address—you don't need to enter your own address because you are included in all notifications. If you are creating a connection through [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), providing an email address with the `‑‑noc-contact-email` flag is required. Workforce identity federation is in [Preview](https://cloud.google.com/products#product-launch-stages).
  2. For redundancy, create a duplicate Dedicated Interconnect connection that is in the same [location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities) but in a different edge availability domain (metro availability zone). For more information, see [Duplicate a connection for redundancy](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-redundant-interconnect).




After you order a Dedicated Interconnect connection, Google sends you a confirmation through email, and allocates ports for you. When the allocation is complete, Google generates LOA-CFAs for your connections and sends them to you through email.

All the automated emails are sent to the NOC contact and the email address of the user account used when ordering the Dedicated Interconnect connection. You can also get your LOA-CFAs by using the Google Cloud console.

You can use the Dedicated Interconnect connection only after your connections have been provisioned and tested for light levels and IP connectivity.

Note: [Billing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/pricing) for your Dedicated Interconnect connection starts after the connection is ready to use (all [tests](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections) have passed) or 30 days after your order is received. You aren't charged before then. You can cancel your order by [deleting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/deleting-interconnects) the Dedicated Interconnect connection.

[ Previous arrow_back  Provisioning overview  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview)

[ Next Retrieve LOA-CFAs  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/retrieving-loas)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
