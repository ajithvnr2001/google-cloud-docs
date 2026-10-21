---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/using-interconnects-other-projects/
title: Use connections in other projects \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:10.172187+00:00
---

# Use connections in other projects  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/using-interconnects-other-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Use connections in other projects Stay organized with collections  Save and categorize content based on your preferences. 

Cross-Cloud Interconnect lets you connect your remote cloud network to multiple Virtual Private Cloud (VPC) networks. You extend reachability by adding multiple VLAN attachments to the connection.

As part of this functionality, you can create a VLAN attachment that uses a Cross-Cloud Interconnect connection that's in a different project. You can use this approach as long as both resources are in the same [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

If appropriate, you can share connectivity between even more VPC networks by using Shared VPC or VPC Network Peering. For more information about these approaches, see [Options for connecting to multiple VPC networks](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment).

**Note:** If you have VLAN attachments associated with multiple VPC networks that have overlapping IP address ranges, the conflicting IP ranges might cause traffic to be routed incorrectly by external routers. To avoid this issue, we recommend that you use a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) to assign unique IP address ranges to all of your VPC subnets.

## Required permissions

_In the project where you create the attachment_ , you need the [Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) .

_In the project that contains the connection_ , you need one of the following:

  * The [Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) or the `compute.interconnects.get` permission
  * Minimally, the `compute.interconnects.use` permission



### compute.interconnects.get

If the user has the `compute.interconnects.get` permission, then the process of creating the attachment is the same as it is for a network administrator.

### compute.interconnects.use

If the user has the `compute.interconnects.use` permission and does not have the `compute.interconnects.get` permission, then the user does not have visibility into what type of remote cloud the connection uses. In this case, the Google Cloud console can't detect requirements related to the remote location.

For example, attachments to Azure require using an IPv4 subnet length of `/30`. For an administrative user, the Google Cloud console removes the option to request a `/29` IPv4 subnet. However, it does not do so for users who have only the `compute.interconnects.use` permission.

Some constraints are enforced by the API, and in such cases, the Google Cloud console returns an error if an invalid parameter is specified.

Other constraints are merely advisory, to guide users toward known valid configurations. For such constraints, the absence of Google Cloud console advice can result in incompatible configuration choices that are not discovered until further along in the configuration sequence.

The following are sample requirements:

  * Microsoft Azure attachments require using an IPv4 subnet length of `/30`.
  * Azure attachments require using the same VLAN ID on both ports of a pair.
  * Amazon Web Services (AWS) attachments require using MD5 authentication for Border Gateway Protocol (BGP) sessions.
  * Oracle Cloud Infrastructure (OCI) attachments require using a VLAN ID >= `100`. Auto-allocated VLAN IDs meet this requirement.



To learn about constraints, consult the following pages:

  * [Create VLAN attachments (AWS)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#create-attachments)
  * [Create VLAN attachments (Azure)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources#create-attachments)
  * [Create VLAN attachments (OCI)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources#create-attachments)



When you grant a user the `compute.interconnects.use` permission, inform them of any constraints.

## Create a VLAN attachment

To create a VLAN attachment that uses a Cross-Cloud Interconnect connection from another project, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the project in which you need to create a VLAN attachment by using the project picker.

  3. Click **Create VLAN attachments** , and then select **Cross-Cloud Interconnect connection**.

  4. In the **Encrypt interconnect** section, select **Set up unencrypted Interconnect** , and then click **Continue**.

  5. On the **Choose an Interconnect** page, select **In another project**. Enter the following information:

     * **Project ID** : Enter the ID of the project that contains the Cross-Cloud Interconnect connection.
     * **Interconnect name** : Enter the name of the connection.
  6. Click **Continue**.

  7. For **VLAN attachments** , click **Add VLAN attachment**. Provide the following information:

     * **Name** : Specify a name for the VLAN attachment.
     * **Cloud Router** : Choose an existing Cloud Router or create a new one. The Cloud Router that you choose defines the region and VPC network to which your VLAN attachment is available. The Google Cloud ASN is also defined by the Cloud Router that you choose.
  8. Click **Done** , and then click **Create**. The attachment takes a few minutes to create.

  9. After the attachment is created, click **Configure** to create a BGP session on the chosen Cloud Router. The Google and Peer BGP IP addresses are selected for you automatically.

  10. After you add the BGP session, click **Save configuration**. The BGP session is not active until you configure resources in your remote cloud.




###  gcloud 

  1. If you have not already created a Cloud Router, create one by running the following command:
         
         gcloud compute routers create ROUTER_NAME \
             --region=REGION \
             --asn=GOOGLE_ASN \
             --network=NETWORK \
             --project=PROJECT_ID
         

Replace the following:

     * `ROUTER_NAME`: a name that you specify for your Cloud Router
     * `REGION`: the Google Cloud region in which your Cloud Router is created; this region must match the region used by the VLAN attachment
     * `GOOGLE_ASN`: the [private ASN](https://tools.ietf.org/html/rfc6996) (`16550`, `64512 - 65534`, `4200000000 - 4294967294`); it is used for all BGP sessions on the same Cloud Router, and it cannot be changed later
     * `NETWORK`: the name of the network to which the Cloud Router manages routes; this is the same network that your VLAN attachment uses
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and VLAN attachment exist; this project ID is different from the project where the connection is located
  2. In the project that contains your connections, list all the Cloud Interconnect connections:
         
         gcloud compute interconnects list \
             --project=INTERCONNECT_PROJECT_ID
         

Replace `INTERCONNECT_PROJECT_ID` with that project's ID. Determine the name of the connection that you need to use.

  3. Determine the self link for the connection that you need to use:
         
         gcloud compute interconnects describe INTERCONNECT_NAME \
             --project=INTERCONNECT_PROJECT_ID \
             --format="get(selfLink)"
         

Replace `INTERCONNECT_NAME` with its name, and replace `INTERCONNECT_PROJECT_ID` with the ID of the project that contains it.

  4. Create the VLAN attachment:
         
         gcloud compute interconnects attachments dedicated create VLAN_ATTACHMENT_NAME \
             --region=REGION \
             --router=ROUTER_NAME \
             --project=PROJECT_ID \
             --interconnect=INTERCONNECT_SELF_LINK \
             --candidate-subnets=CANDIDATE_SUBNETS \
             --vlan=VLAN_ID
         

Replace the following:

     * `VLAN_ATTACHMENT_NAME`: a name that you specify for your VLAN attachment
     * `REGION`: must match the same region as the associated Cloud Router
     * `ROUTER_NAME`: the name of the Cloud Router from the first step
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and the VLAN attachment exist; this project ID is different from the project where the connection is located
     * `INTERCONNECT_SELF_LINK`: the self link for the connection that the VLAN attachment uses; the self link includes the ID of the project that contains the connection itself
     * `CANDIDATE_SUBNETS`: an optional flag that lets you specify comma-delimited ranges of link-local IP addresses (as `CANDIDATE_SUBNETS`) to be used for the BGP session that manages routes for the VLAN attachment; for more information, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/create#--candidate-subnets)
     * `VLAN_ID`: an optional flag that lets you specify a VLAN ID; for more information, see the [Google Cloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/create#--vlan)
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
     * `customerRouterIpAddress` is the BGP IP address that you use to configure the BGP session in your remote cloud.
     * `tag8021q` is the VLAN ID, which you might have specified manually in the previous step.
  6. Create an interface on the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
             --interconnect-attachment=VLAN_ATTACHMENT_NAME \
             --region=REGION \
             --interface-name=INTERFACE_NAME \
             --project=PROJECT_ID \
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router from the first step
     * `VLAN_ATTACHMENT_NAME`: the name of the VLAN attachment that you created and described in these steps
     * `REGION`: the region used by the Cloud Router and the VLAN attachment
     * `INTERFACE_NAME`: a name that you specify for the new interface on the Cloud Router
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and VLAN attachment exist; this project ID is different from the project where the connection is located
     * `CLOUD_ROUTER_IP`: the `cloudRouterIpAddress` that you determined in the previous step
  7. Add a BGP peer to the new interface on the Cloud Router:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
             --region=REGION \
             --interface-name=INTERFACE_NAME \
             --peer-name=BGP_PEER_NAME \
             --project=PROJECT_ID \
             --peer-asn=PEER_ASN \
             --advertised-route-priority=PRIORITY \
             --advertisement-mode=ADVERTISEMENT_MODE
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router from the first step
     * `REGION`: the region used by the Cloud Router and the VLAN attachment
     * `INTERFACE_NAME`: the name of the interface that you created in the previous step
     * `BGP_PEER_NAME`: a name that you specify for the BGP peer
     * `PROJECT_ID`: the ID for the project in which both the Cloud Router and the VLAN attachment exist; this project ID is different from the project where the connection is located
     * `CUSTOMER_ROUTER_IP`: the BGP IP address for your remote cloud; this is the `customerRouterIpAddress` that you noted when you described your VLAN attachment
     * `PEER_ASN`: the ASN for your remote cloud
     * `PRIORITY`: an optional flag that you can use to set the base priority for the routes that the Cloud Router advertises to the remote cloud; for more details about this option and the base metric, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority)
     * `ADVERTISEMENT_MODE`: an optional flag that you can use if you want to customize the routes that the Cloud Router advertises to the remote cloud; for information about default and custom advertisements, see [route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am)



## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
