---
url: https://docs.cloud.google.com/vpc/docs/access-service-other-vpc-network/
title: Access the service from another VPC network \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:44.485335+00:00
---

# Access the service from another VPC network  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/access-service-other-vpc-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback 

#  Access the service from another VPC network Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how you, as a _service consumer_ , can access your published service by creating a Private Service Connect _endpoint_. When you send requests to the endpoint, Private Service Connect forwards those requests to the published service.

This tutorial is intended for cloud architects, network architects, network administrators, and IT administrators.

## Objectives

  * Configure networking for the service consumer resources
  * Create an endpoint
  * Test accessing the endpoint



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Virtual Private Cloud](http://cloud.google.com/vpc/pricing)
  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Complete the previous two tutorials in this series: 
     * [Create a load-balanced service](https://docs.cloud.google.com/vpc/docs/create-load-balanced-service).
     * [Make the service accessible from other VPC networks](https://docs.cloud.google.com/vpc/docs/make-service-accessible-other-vpc-networks). You need the [ service attachment ID](https://docs.cloud.google.com/vpc/docs/make-service-accessible-other-vpc-networks#get-service-details) to complete this tutorial. 
  2. Create or select a project to use for the service consumer resources. This project is referred to as `CONSUMER_PROJECT`
     1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. Select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  3. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  4. Make sure that you have the following role or roles on the project: Compute Engine > Compute Network Admin, Compute Engine > Compute Instance Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Configure networking

The following sections explain how to create a network and a subnet to host the endpoint, and how to create a firewall rule to allow SSH access to the client VM used for testing the endpoint.

### Create a network and subnet

To create the service consumer network and subnet, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `consumer-network`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the **New subnet** section, enter the following information.

     1. For **Name** , enter `consumer-subnet`.
     2. For **Region** , select the same region as the published service that you created.
     3. For **IP stack type** , select **IPv4 (single-stack)**.
     4. For **IPv4 range** , enter `192.168.10.0/24`.
     5. Click **Done**.
  6. Click **Create**.




###  gcloud 

  1. Create a custom mode VPC network:
         
         gcloud compute networks create consumer-network --subnet-mode=custom
         

  2. In the `consumer-network` network, create a subnet.
         
         gcloud compute networks subnets create consumer-subnet \
             --network=consumer-network \
             --range=192.168.10.0/24 \
             --region=REGION
         

Replace `REGION` with the same region as the published service that you created.




### Configure firewall rules

Create a firewall rule called `fw-allow-ssh` to let SSH traffic from `0.0.0.0/0` reach VMs that have the `allow-ssh` network tag.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow incoming SSH connections, click **Create firewall rule** and use the following settings:

     * For **Name** , enter `fw-allow-ssh`.
     * For **Network** , select `consumer-network`.
     * For **Priority** , enter `1000`.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Targets** , select **Specified target tags**.
     * For **Target tags** , enter `allow-ssh`.
     * For **Source filter** , select **IPv4 ranges**.
     * For **Source IPv4 ranges** , enter `0.0.0.0/0`.
     * For **Protocols and ports** , select **Specified protocols and ports** , select the **TCP** checkbox. For **Ports** , enter `22`.
  3. Click **Create**. 




###  gcloud 

  1. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`.
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=consumer-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=0.0.0.0/0 \
             --target-tags=allow-ssh \
             --rules=tcp:22
         




## Create an endpoint

Create an endpoint that points to the published service that you created.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click **Connect endpoint**.

  4. For **Target** , select **Published service**.

  5. For **Target service** , enter `projects/PRODUCER_PROJECT/regions/REGION/serviceAttachments/published-service`.

Replace `PRODUCER_PROJECT` with the project ID of the published service. Replace `REGION` with the region of the published service.

  6. For **Endpoint name** , enter `ep-1`.

  7. For **Network** , select `consumer-network`.

  8. For **Subnetwork** , select `consumer-subnet`.

  9. Click the **IP address** drop-down menu and select **Create IP address**.

     1. For **Name** , enter `ep-ip-1`.
     2. For **Static IP address** , select **Let me choose**.
     3. For **Custom IP address** , enter `192.168.10.5`.
     4. Click **Reserve**.
  10. Click **Add endpoint**.




###  gcloud 

  1. Reserve an internal IP address to assign to the endpoint.
         
         gcloud compute addresses create ep-ip-1 \
             --region=REGION \
             --subnet=consumer-subnet \
             --addresses=192.168.10.5
         

Replace `REGION` with the same region as the published service that you created.

  2. Create a forwarding rule to connect the endpoint to the service producer's service attachment.
         
         gcloud compute forwarding-rules create ep-1 \
             --region=REGION \
             --network=consumer-network \
             --address=ep-ip-1 \
             --target-service-attachment=projects/PRODUCER_PROJECT/regions/REGION/serviceAttachments/published-service
         

Replace the following:

     * `PRODUCER_PROJECT`: the project ID of the service producer project.

     * `REGION`: the region of the service attachment.




## Test accessing the endpoint

To test that the endpoint and the published service are working, create a test VM and send a request from it to the endpoint.

### Create a client VM for testing

Create a client VM in the same region as the endpoint.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `consumer-test`.

  4. For **Region** , select the same region as the backend VMs.

  5. For **Zone** , select a zone in that region.

  6. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * For **Network** , select `consumer-network`
        * For **Subnet** , select `consumer-subnet`
  7. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create consumer-test \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=consumer-subnet
    

Replace `ZONE` with a zone that's in the same region as the backend VMs.

### Test connectivity

This test contacts the endpoint from a client VM. The expected behavior is for traffic to be distributed across the load balancer's backend VMs.

  1. Connect to the client VM instance. 
         
         gcloud compute ssh consumer-test --zone=ZONE
         

Replace `ZONE` with the zone of the client VM.
  2. Make a web request to the endpoint using `curl` to contact its IP address. Repeat the request so you can see that responses come from different backend VMs. The name of the VM generating the response is displayed in the text in the HTML response, because of the contents of `/var/www/html/index.html` on each backend VM. For example, expected responses look like `Page served from: vm-1` and `Page served from: vm-2`. 
         
         curl -s http://192.168.10.5
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the projects

Delete both the producer project (`PRODUCER_PROJECT`) and the consumer project (`CONSUMER_PROJECT`).

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Learn more about [Private Service Connect published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services)
  * Learn more about [accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
