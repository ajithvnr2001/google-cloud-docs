---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections/
title: Order Cross-Site Interconnect connections \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:07:38.985933+00:00
---

# Order Cross-Site Interconnect connections  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order Cross-Site Interconnect connections Stay organized with collections  Save and categorize content based on your preferences. 

Ordering Cross-Site Interconnect connections starts the creation [process](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview) of your Cross-Site Interconnect connections. When you order Cross-Site Interconnect connections, you specify details such as the capacity and the locations of your connections.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Cross-Site Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

You can request the following capacities:

  * 1 x 10-Gbps (10 Gbps) circuit
  * 1 x 100-Gbps (100 Gbps) circuit

**Caution:** The link type that you select when you create a Cross-Site Interconnect connection cannot be changed later. For example, if you select a 10-Gbps link type and need a 100-Gbps link type later, you must create a new Cross-Site Interconnect connection with the higher capacity.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.create`



**Roles**

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Compute Network Admin (`roles/compute.networkAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list)

  2. On the **Physical connections** page, click add**Set up physical connection**.

  3. Select **Cross-Site Interconnect connection** , and then click **Continue**.

  4. If you haven't already, [check your bandwidth quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota) to ensure that you can successfully create a cross-site network with your required bandwidth.

After you have confirmed that you have sufficient quota, click **Next: I acknowledge**.

  5. Specify the details of the Cross-Site Interconnect connection:

     * **Name** : A name for the connection. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect`.
     * **Colocation facility** : The physical [location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations) where the connection is created. Your on-premises network must meet Google Cloud's network in this location.
     * **Capacity** : The total capacity of your connection, which is determined by the number and size of the circuits that you order.

Select _one_ of the following options:

       * 1 x 10-Gbps circuit
       * 1 x 100-Gbps circuit
  6. Click **Next**.

  7. Specify details for your duplicate connection, and then click **Next**.

  8. Specify your contact information:

     * **Company name** : The name of your organization to put in the LOA as the party authorized to request a connection.
     * **Technical contact** : An email address where notifications about this connection are sent. You don't need to enter your own address; you are included in all notifications. You can specify only one address.

If you are creating a connection through [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), specifying a **Technical contact** is required.

  9. Review your order. Check that your connection details and contact information are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.

  10. On the order confirmation page, view your order details, your quota requirements acknowledgement, and next steps.

     1. Submit a [Letter of Authorization and Connecting Facility Assignment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#loa) (LOA-CFA) forms to your colocation facility. You can wait for an email, or you can [download the form from the Google Cloud console](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/retrieving-loas).
     2. Configure your peer router to establish the connection.
     3. Complete your site-to-site connection by adding another interconnect in a different location.

If you need to order a connection for your second site, click **Order interconnect** , and repeat the steps in this section.

  11. Click **Done**.




###  gcloud 

  1. Create a Cross-Site Interconnect connection that is a connection type of `DEDICATED` and specifies the `CROSS_SITE_NETWORK` feature. If you plan to use [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview), include `MACSEC` in the list of requested features.
         
         gcloud compute interconnects create INTERCONNECT_NAME \
             --customer-name=NAME \
             --interconnect-type=DEDICATED \
             --requested-features=CROSS_SITE_NETWORK[,MACSEC] \
             --link-type=LINK_TYPE \
             --location=LOCATION_NAME \
             [--noc-contact-email=EMAIL_ADDRESS] \
             [--description=STRING]
         

Replace the following values:

     * `INTERCONNECT_NAME`: a name for the Cross-Site Interconnect connection; this name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the connection, such as `my-interconnect`
     * `NAME`: the name of your organization to put in the LOA as the party authorized to request a connection
     * `LINK_TYPE`: 
       * If you want your Cross-Site Interconnect connection to be made up of a 10-Gbps circuit, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_10G_LR`.
       * If you want your connection to be made up of a 100-Gbps circuit, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_100G_LR`.
     * `LOCATION_NAME`: specifies the location where the Cross-Site Interconnect connection is created; to list the names of locations, see [List locations for Cross-Site Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/list-locations)
     * `EMAIL_ADDRESS` and `STRING`: optional; for the NOC contact, you can specify only one email address—you don't need to enter your own address because you are included in all notifications. If you are creating a connection through [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), providing an email address with the `‑‑noc-contact-email` flag is required.
  2. Create a duplicate Cross-Site Interconnect connection that is in the same [metro](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations) but in a different edge availability domain (metro availability zone).
         
         gcloud compute interconnects create REDUNDANT_INTERCONNECT_NAME \
              --customer-name=NAME \
              --interconnect-type=DEDICATED \
              --requested-features=CROSS_SITE_NETWORK[,MACSEC] \
              --link-type=LINK_TYPE \
              --location=LOCATION_NAME \
              [--noc-contact-email=EMAIL_ADDRESS] \
              [--description=STRING]
         

Replace the following:

     * `REDUNDANT_INTERCONNECT_NAME`: a name for the redundant Cross-Site Interconnect connection
     * `NAME`: the name of your organization to put in the LOA as the party authorized to request a connection
     * `LINK_TYPE`: the per-circuit capacity of your Cross-Site Interconnect connection; use the same value as the existing connection: 
       * If your existing connection is made up of 10-Gbps circuits, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_10G_LR`.
       * If your existing connection is made up of 100-Gbps circuits, replace `LINK_TYPE` with `LINK_TYPE_ETHERNET_100G_LR`.
     * `LOCATION_NAME`: the location where the redundant Cross-Site Interconnect connection is created

From the list of [locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cross-site-locations#locations-table), select one that's in the same metro but in a different edge availability domain from the existing connection.

For example, if the existing connection is in `iad-zone2-1`, select a location that's in Ashburn but in zone 1, such as `iad-zone1-1`.

     * `EMAIL_ADDRESS` and `STRING`: optional; for the NOC contact, you can specify only one email address—you don't need to enter your own address because you are included in all notifications

  3. To order connections for your second site, repeat the steps in this section.




After you order a Cross-Site Interconnect connection, Google emails you a confirmation and allocates ports for you. When the allocation is complete, Google generates LOA-CFAs for your connections and emails them to you.

All the automated emails are sent to the NOC contact and the email address of the Google Account used when ordering the Cross-Site Interconnect connection. You can also get your LOA-CFAs by using the Google Cloud console.

You can use the Cross-Site Interconnect connection only after your connections have been provisioned and tested for light levels and IP connectivity.

**Note:** [Billing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/pricing) for your Cross-Site Interconnect connection starts after it's ready to use (all [tests](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections) have passed) or 30 days after your order is received. You aren't charged before then. You can cancel your order by [deleting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/delete-connections) the Cross-Site Interconnect connection.

[ Previous arrow_back  Check bandwidth quotas and limits  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota)

[ Next Retrieve LOA-CFAs  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/retrieve-loas)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
