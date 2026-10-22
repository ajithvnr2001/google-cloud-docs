---
url: https://docs.cloud.google.com/alloydb/docs/connect-psql/
title: Connect from Compute Engine \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:55.503955+00:00
---

# Connect from Compute Engine  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-psql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect from Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

To run SQL queries and manage your database from a virtual machine (VM) in your Virtual Private Cloud (VPC) network, you can connect the `psql` client tool on a Compute Engine VM to an AlloyDB instance over private services access:

  1. Create a Compute Engine VM that can connect to AlloyDB instances by using private services access.
  2. Install the `psql` client on the Compute Engine VM.
  3. Get the IP address of the AlloyDB instance that you want to connect to.
  4. Run the `psql` client.



The first two tasks are one-time operations. After you create a Compute Engine VM and install the `psql` client on it, you can continue to use the VM to connect `psql` to AlloyDB instances by completing the remaining tasks.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * A VPC network in the Google Cloud project that you are using must already be [configured for private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity) to AlloyDB. 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.

  * If the client host has a firewall, it must allow egress connections to port 5432 on your AlloyDB instances' IP addresses. 



## Create a Compute Engine VM

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the project containing the AlloyDB instance you want to connect to.
  3. Click **Create instance**.
  4. Click the **Machine configuration** section.
  5. Enter a **Name** for the instance.
  6. Configure the region and zone where you want to create the instance.
  7. Select a machine series and the corresponding machine type.
  8. Retain the default values in the **OS and Storage** section.
  9. Click the **Networking** section, and set **Network interfaces** to the VPC network configured for private services access to AlloyDB.  
If **Network interfaces** is not set to the VPC network configured for private services access, expand it and then set **Network** to the VPC network.
  10. Retain the default values in the **Observability** section.
  11. Click the **Security** section.
  12. In **Identity and API access** , set **Access scopes** to **Allow full access to all Cloud APIs**.
  13. Retain the default values in the **Advanced** section.
  14. Click **Create**.



After the VM is created, connect to the Compute Engine VM you created using SSH.

## Install the psql client tool

To install the `psql` client tool on your client host, see [Install the psql client tool](https://docs.cloud.google.com/alloydb/docs/install-psql).

If you are using a Compute Engine VM as your client host, follow these steps to connect to your VM and install `psql`:

  1. Connect to the Compute Engine VM you created using SSH.  By default, SSH connections to Compute Engine VMs use Identity-Aware Proxy. Depending on your organization's networking policies, you might need to [create an ingress firewall rule](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#firewall) to allow traffic to your VMs. 

### Console

     1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. In the list of virtual machine instances, click **SSH** in the row of the instance you created. 

### gcloud

Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the instance you created.
    
    gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the instance
     * `ZONE`: the name of the zone in which the instance is located
     * `VM_NAME`: the name of the instance

  2. Install the `psql` client from the package manager: 
         
         sudo apt-get update
         sudo apt-get install postgresql-client




## Get the IP address of the AlloyDB instance

To get the IP address of the AlloyDB instance you want to connect to, [view that instance's settings](https://docs.cloud.google.com/alloydb/docs/instance-view).

## Run the psql client

  1. Connect to the VM you created using SSH. 

### Console

     1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. In the list of virtual machine instances, click **SSH** in the row of the instance you created. 

### gcloud

Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the instance you created.
    
    gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the instance.
     * `ZONE`: the name of the zone in which the instance is located.
     * `VM_NAME`: the name of the instance.

  2. Run the `psql` client tool: 
         
         psql -h IP_ADDRESS -p 5432 -U USERNAME -d postgres

You are prompted to enter the password of the USERNAME user.

If you're connecting for the first time, specify `postgres` for both the USERNAME and the database. Your command looks like the following:
         
         psql -h IP_ADDRESS -p 5432 -U postgres -d postgres

Use the password that you set when you created the cluster.




## What's next

  * Learn about other [ways to connect to AlloyDB](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
