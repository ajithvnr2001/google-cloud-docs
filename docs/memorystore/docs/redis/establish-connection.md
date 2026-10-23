---
url: https://docs.cloud.google.com/memorystore/docs/redis/establish-connection/
title: Establish a private services access connection \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:36.859408+00:00
---

# Establish a private services access connection  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/establish-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Establish a private services access connection Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to establish a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection for a network. Establishing a private services access connection for a network is a prerequisite for creating a Redis instance with the private services access connection mode designated for that network. For more details, see [Networking](https://docs.cloud.google.com/memorystore/docs/redis/networking).

**Note:** We recommend that your organization's networking team / networking admin manage these steps for setting up a private services access connection.   
  
If you are an application developer, usually your networking team should manage establishing a private services access connection. For more details, see [Communicating networking requirements](https://docs.cloud.google.com/memorystore/docs/redis/networking#communicating_networking_requirements).

## Private services access setup instructions

Follow these steps to setup a private services access connection for your network:

### gcloud

  1. Enable the Service Networking API:   
[Enable the Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)

If you are using Shared VPC, enable the API in both the Service Project and the Host Project.

  2. [Check to see](https://docs.cloud.google.com/memorystore/docs/redis/verifying-connection) if a private service access connection has been established for your network.

     * If the connection has already been established, then see [Create a Redis instance that uses a centralized IP address range](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_that_uses_a_centralized_ip_address_range) for instructions on how to create a Redis instance.
  3. Open a terminal window.

  4. Set your default project by running the following command, replacing variables with appropriate values:
         
         gcloud config set core/project project-id
         

  5. Reserve an IP address range in your network by running the following command:
         
         gcloud compute addresses create reserved-range-name --global --prefix-length=24 --description=description --network=vpc-network --purpose=vpc_peering
         

     * In the command above, the CIDR prefix length is set to `24`. This value must be `24` or less. For example, `23` is an acceptable prefix. Note that smaller CIDR prefixes create larger IP address ranges.

     * For information on managing private services access, see [Configuring private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

  6. Create a [private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection) between your network and the private services access network by running the following command:
         
         gcloud services vpc-peerings connect --service=servicenetworking.googleapis.com --ranges=reserved-range-name --network=vpc-network --project=project-id
         




### Console: VPC network

  1. Enable the Service Networking API:   
[Enable the Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)

If you are using Shared VPC, enable the API in both the Service Project and the Host Project.

  2. [Check to see](https://docs.cloud.google.com/memorystore/docs/redis/verifying-connection) if a private service access connection has been established for your network.

     * If the connection has already been established, then see [Create a Redis instance that uses a centralized IP address range](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_that_uses_a_centralized_ip_address_range) for instructions on how to create a Redis instance.
  3. Go to the VPC Networks page in the Google Cloud console.   
[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  4. Click the name of your network. Usually it is named "default".

  5. Click **Private services access**.

  6. Click **Allocate IP ranges for services**.

  7. Click **Allocate IP range**.

     * Enter a name for your range, such as "private-services-access-range".
     * Enter a description for your range, such as "Range of IP addresses to be used for the Private services access connection".
     * Select **Automatic** if you want Google to choose your range for you. 
       1. Enter a CIDR prefix of `/24` or less. For example, `/23` is an acceptable prefix. Note that smaller CIDR prefixes create larger IP address ranges.
     * Select **Custom** if you want to choose the range yourself. 
       1. Enter your desired range with a CIDR prefix of `/24` or less.
     * Click **Allocate**.
  8. Click **Private connections to services**.

  9. Click the **Create connection** button.

  10. Under the **Assigned allocation** dropdown, select the range you just created in the steps above.

  11. Click **Ok**.

  12. Click **Connect**.

  13. Refresh the page to see your new connection listed under the **Private connections to services** tab.




### Console: Redis

  1. Enable the Service Networking API:   
[Enable the Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)

If you are using Shared VPC, enable the API in both the Service Project and the Host Project.

  2. Follow the steps at [Create a Redis instance on a VPC network](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_on_a_vpc_network) until you see the **Advanced network options** expander, and open it.

**Note:** If you see the **Private service connection required** panel, a private services access connection has not been established yet. If you do not see this panel, the connection has already been established for your network, and any Redis instance created with this network uses the [private services access connection mode](https://docs.cloud.google.com/memorystore/docs/redis/networking#connection_modes).
  3. Click the **Set Up Connection** button in the **Private service connection** panel. Doing so opens a slide-out panel for setting up private services access.

  4. Allocate an IP range using one of the following methods:

     * Select an existing IP range.
     * Allocate a new IP range. 
       * Enter a **name** for your range.
       * Enter a valid CIDR range with a block size of `/24`. For example: `10.0.0.0/24`.
     * Use an automatically allocated IP range.
  5. Click the **Create Connection** button.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
