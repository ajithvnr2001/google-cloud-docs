---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects/
title: Use connections in other projects \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:37.185438+00:00
---

# Use connections in other projects  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Use connections in other projects Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a VLAN attachment that uses a Dedicated Interconnect connection located in a different project than the attachment's project. Using separate projects can also help you maintain separate billing and permissions.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

Dedicated Interconnect connections enable you to connect your on-premises network to multiple Virtual Private Cloud (VPC) networks by adding multiple VLAN attachments to that connection. You can create a VLAN attachment from a connection in one project to a VPC network in another project, as long as they are both in the same [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

When using Partner Interconnect, you still create VLAN attachments to the VPC networks that you want to use. However, because the service provider manages the connection on your behalf, you don't have to be concerned about organization restrictions on the connection.

A VLAN attachment that is used with either type of connection can use Shared VPC or VPC Network Peering to share the connectivity between multiple VPC networks.

If you have VLAN attachments associated with multiple VPC networks that have overlapping IP ranges, the conflicting IP ranges might cause traffic to be routed incorrectly by one or more of your on-premises devices. To avoid this issue, we recommend that you assign unique IP ranges to all of your VPC subnets by configuring subnets in a [VPC custom mode network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges).

For more information, see [Options for connecting to multiple VPC networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment).

If you are using VLAN attachments located in different regions than your Dedicated Interconnect connection, then [change your VPC network's dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes#change-network-modes) to **Global**.

## Required permissions

**To create the VLAN attachment and Cloud Router:** Project owners, editors, or Identity and Access Management (IAM) principals with the [Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) can create new VLAN attachments and Cloud Routers.

**To use the Dedicated Interconnect connection from another project:** Project owners, editors, or IAM principals with the Network Admin role (`roles/compute.networkAdmin`) _to that other project_ have access to all of its connections. The minimal permission required to use a connection in another project is the `compute.interconnects.use` permission on the project that contains the connection.

## Create a VLAN attachment

To create a VLAN attachment that uses a Dedicated Interconnect connection from another project, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Interconnect Hybrid Connectivity** page.

[Go to Interconnect Hybrid Connectivity](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the project in which you need to create a VLAN attachment by using the project picker.

  3. Click **Create VLAN attachments** , and then select **Dedicated Interconnect connection**.

  4. In the **Encrypt interconnect** section, select **Set up unencrypted Interconnect** , and then click **Continue**.

  5. On the **Choose an Interconnect** page, select **In another project**. Enter the following information:

     * **Project ID** : Enter the project ID of the project that contains the Dedicated Interconnect connection.
     * **Interconnect name** : Enter the name of the connection.
  6. Click **Continue**.

  7. For **VLAN attachments** , click **Add VLAN attachment**. Provide the following information for the VLAN attachment:

     * **Name** : Specify a name for the VLAN attachment.
     * **Cloud Router** : Choose an existing Cloud Router or [create a new one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-on-premises-network). The Cloud Router that you choose defines the region and VPC network to which your VLAN attachment is available. The Google Cloud ASN is also defined by the Cloud Router that you choose.
  8. Click **Done** , and then click **Create**. The attachment takes a few minutes to create.

  9. After the attachment is created, click **Configure** to create a BGP session on the chosen Cloud Router. The Google and Peer BGP IP addresses are selected for you automatically.

  10. After you add the BGP session, click **Save configuration**. The BGP session is not active until you configure your on-premises router.




###  gcloud 

  1. If you have not already created a Cloud Router, create one by running the following command:
         
         gcloud compute routers create ROUTER_NAME \
             --region=REGION \
             --asn=PRIVATE_ASN \
             --network=NETWORK \
             --project=PROJECT_ID
         

Replace the following:

     * `ROUTER_NAME`: a name that you specify for your Cloud Router
     * `REGION`: the Google Cloud region in which your Cloud Router is created; this region must match the region used by the VLAN attachment
     * `PRIVATE_ASN`: the [private ASN](https://tools.ietf.org/html/rfc6996) (`64512 - 65534`, `4200000000 - 4294967294`); it is used for all BGP sessions on the same Cloud Router, and it cannot be changed later
     * `NETWORK`: the name of the network to which the Cloud Router manages routes; this is the same network that your VLAN attachment uses
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and VLAN attachment exist; this project ID is different from the project where the connection is located
  2. List Dedicated Interconnect connections in the project that contains your connections:
         
         gcloud compute interconnects list \
             --project=INTERCONNECT_PROJECT_ID
         

Replace `INTERCONNECT_PROJECT_ID` with that project's ID. Determine the name of the connection that you need to use.

  3. Determine the self link for the connection that you need to use:
         
         gcloud compute interconnects describe INTERCONNECT_NAME \
             --project=INTERCONNECT_PROJECT_ID \
             --format="get(selfLink)"
         

Replace `INTERCONNECT_NAME` with its name, and `INTERCONNECT_PROJECT_ID` with the ID of the project that contains it.

  4. Create the VLAN attachment:
         
         gcloud compute interconnects attachments dedicated create VLAN_ATTACHMENT_NAME \
             --region=REGION \
             --router=ROUTER_NAME \
             --project=PROJECT_ID \
             --interconnect=INTERCONNECT_SELF_LINK \
            [--candidate-subnets=CANDIDATE_SUBNETS] \
            [--vlan=VLAN_ID]
         

Replace the following:

     * `VLAN_ATTACHMENT_NAME`: a name that you specify for your VLAN attachment
     * `REGION`: must match the same region as the associated Cloud Router
     * `ROUTER_NAME`: the name of the Cloud Router from the first step
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and VLAN attachment exist; this project ID is different from the project where the connection is located
     * `INTERCONNECT_SELF_LINK`: the self link for the connection that the VLAN attachment uses; the self link includes the ID of the project that contains the connection itself
     * `CANDIDATE_SUBNETS`: an _optional_ flag that lets you specify comma-delimited ranges of link-local IP addresses (as `CANDIDATE_SUBNETS`) to be used for the BGP session that manages routes for the VLAN attachment; for more information, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/create#--candidate-subnets)
     * `VLAN_ID`: an _optional_ flag that lets you specify a VLAN ID; for more information, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/create#--vlan)
  5. Describe the VLAN attachment that you just created:
         
         gcloud compute interconnects attachments dedicated describe VLAN_ATTACHMENT_NAME \
             --region=REGION \
             --project=PROJECT_ID \
             --format="get(cloudRouterIpAddress,customerRouterIpAddress,tag8021q)"
         

Replace the following:

     * `VLAN_ATTACHMENT_NAME`: its name
     * `REGION`: its region
     * `PROJECT_ID`: its project ID

Note the following:

     * `cloudRouterIpAddress` is the BGP IP address that is used by the BGP session on the associated Cloud Router.
     * `customerRouterIpAddress` is the BGP IP address that you use to configure the BGP session on your on-premises router.
     * `tag8021q` is the VLAN ID, which you might have specified manually in the previous step.
  6. Create an interface on the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
             --interconnect-attachment=VLAN_ATTACHMENT_NAME \
             --region=REGION \
             --interface-name=INTERFACE_NAME \
             --project=PROJECT_ID \
             --ip-address=CLOUD_ROUTER_IP \
             --mask-length=29
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router from the first step
     * `VLAN_ATTACHMENT_NAME`: the name of the VLAN attachment that you created and described in these steps
     * `REGION`: the region used by the Cloud Router and VLAN attachment
     * `INTERFACE_NAME`: a name that you specify for the new interface on the Cloud Router
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and VLAN attachment exist; this project ID is different from the project where the connection is located
     * `CLOUD_ROUTER_IP`: the `cloudRouterIpAddress` that you determined in the previous step
  7. Add a BGP peer to the new interface on the Cloud Router:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
             --region=REGION \
             --interface-name=INTERFACE_NAME \
             --peer-name=BGP_PEER_NAME \
             --project=PROJECT_ID \
             --peer-ip-address=CUSTOMER_ROUTER_IP \
             --peer-asn=PEER_ASN \
            [--advertised-route-priority=PRIORITY] \
            [--advertisement-mode=ADVERTISEMENT_MODE]
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router from the first step
     * `REGION`: the region used by the Cloud Router and VLAN attachment
     * `INTERFACE_NAME`: the name of the interface that you created in the previous step
     * `BGP_PEER_NAME`: a name that you specify for the BGP peer
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and VLAN attachment exist; this project ID is different from the project where the connection is located
     * `CUSTOMER_ROUTER_IP`: the BGP IP address for your on-premises router; this is the `customerRouterIpAddress` that you noted when you described your VLAN attachment
     * `PEER_ASN`: the ASN for your on-premises router
     * `PRIORITY`: an _optional_ flag that you can use to set the base priority for the "to Google" routes that the Cloud Router shares with the on-premises router; for more details about this option and the base metric, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority)
     * `ADVERTISEMENT_MODE`: an _optional_ flag that you can use if you want to customize the "to Google" routes advertised by the Cloud Router; for information about default and custom advertisements, see [route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am)



## What's next

  * To configure a VLAN subinterface and a BGP peer on your on-premises router by using the values allocated by your VLAN attachment, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers).

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
