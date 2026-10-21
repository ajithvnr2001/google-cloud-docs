---
url: https://docs.cloud.google.com/vpc/docs/make-service-accessible-other-vpc-networks/
title: Make the service accessible from other VPC networks \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:57.322242+00:00
---

# Make the service accessible from other VPC networks  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/make-service-accessible-other-vpc-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback 

#  Make the service accessible from other VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to make a load-balanced service available from other VPC networks by using Private Service Connect.

By default, the internal passthrough Network Load Balancer that you created in the previous tutorial is available only within its own VPC network. With Private Service Connect, you can publish the service to make it available to resources in other VPC networks.

This tutorial is intended for cloud architects, network architects, network administrators, and IT administrators.

## Objectives

  * Create the published service
  * Create a firewall rule for published service traffic
  * Get the service attachment URI



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Virtual Private Cloud](https://cloud.google.com/vpc/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Complete the steps in the previous tutorial, [Create a load-balanced service](https://docs.cloud.google.com/vpc/docs/create-load-balanced-service). 
  2. Select the service producer project (`PRODUCER_PROJECT`) that you selected or created in the previous tutorial. Use this project for the steps in this tutorial.



## Create the published service

To make the service available from other VPC networks, you publish the service. To publish a service, create the following resources in the same network and region as the load balancer:

  * A Private Service Connect subnet that provides IP addresses for network address translation (NAT) between the producer and consumer networks.
  * A service attachment.



These instructions create a published service that is accessible from any project. In a production environment, you might instead choose to limit which networks or projects can access the service.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click **Publish service**.

  4. In the **Target details** section, select **Load balancer**.

  5. Select **Internal passthrough Network Load Balancer**

  6. Select the internal load balancer that you created, `service-lb`.

  7. For **Service name** , enter `published-service`.

  8. Create a Private Service Connect subnet for NAT:

     1. Click **Subnets** , and then click **Reserve new subnet**.
     2. For **Name** , enter `nat-subnet`.
     3. For **Region** , select `REGION`.
     4. For **IPv4 range** , enter `10.10.20.0/22`.
     5. Click **Add**.
  9. For **Connection preference** , select **Automatically accept all connections**.

  10. Click **Add service**.




###  gcloud 

  1. Create a Private Service Connect subnet by using the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create nat-subnet \
           --network=service-network \
           --region=REGION \
           --range=10.10.20.0/22 \
           --purpose=PRIVATE_SERVICE_CONNECT
         

  2. To publish the service, use the [`gcloud compute service-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/create).
         
         gcloud compute service-attachments create published-service \
           --region=REGION \
           --target-service=projects/PRODUCER_PROJECT/regions/REGION/forwardingRules/service-rule \
           --connection-preference=ACCEPT_AUTOMATIC \
           --nat-subnets=nat-subnet
         

Replace the following:

     * `PRODUCER_PROJECT`: the ID of the producer project.
     * `REGION`: the region for the service attachment. This must be the same region as the IP address of the target forwarding rule.



## Create a firewall rule for published service traffic

Create a firewall rule to let traffic from the Private Service Connect NAT subnet reach the load balancer's backend VMs.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To let traffic from the Private Service Connect NAT subnet reach the load balancer's backend VMs, click **Create firewall rule** and use the following settings:

     * For **Name** , enter `fw-allow-nat`.
     * For **Network** , select `service-network`.
     * For **Priority** , enter `1000`.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Targets** , select **Specified target tags**.
     * For **Target tags** , enter `allow-nat`.
     * For **Source filter** , select **IPv4 ranges**.
     * For **Source IPv4 ranges** , enter `10.10.20.0/22`.
     * For **Protocols and ports** , select **Allow all**.
  3. Click **Create**. 




###  gcloud 

  1. Create the `fw-allow-nat` firewall rule to allow communication from the Private Service Connect NAT subnet to the VM backends:
         
         gcloud compute firewall-rules create fw-allow-nat \
             --network=service-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.10.20.0/22 \
             --rules=tcp,udp,icmp
         




## Get the service attachment URI

You use the service attachment URI to configure the endpoint in the next tutorial, [Access the service from another VPC network](https://docs.cloud.google.com/vpc/docs/access-service-other-vpc-network).

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to view.

The **Service attachment** field contains the service attachment URI.




###  gcloud 

  1. View details for the published service by using the [`gcloud compute service-attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe).

The `selfLink` field contains the service attachment URI.
         
         gcloud compute service-attachments describe \
             published-service --region=REGION
         

Replace `REGION` with the region that contains the service attachment.




## What's next

  * [Access the service from another VPC network](https://docs.cloud.google.com/vpc/docs/access-service-other-vpc-network)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
