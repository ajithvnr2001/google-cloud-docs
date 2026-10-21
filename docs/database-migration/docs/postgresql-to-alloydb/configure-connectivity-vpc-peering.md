---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/
title: Configure private IP connectivity \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:28.684373+00:00
---

# Configure private IP connectivity  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpc-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Configure private IP connectivity Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-vpc-peering "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-vpc-peering "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  
  
You can migrate your data over private networks by establishing connectivity between your source and destination databases private IP addresses. You can use one of the two approaches To configure private IP addresses for your destination database, you can use private services access or Private Service Connect. 

Each connection method offers distinct advantages and trade-offs. Make sure you choose the approach that best fits your scenario. For more information about private services access and Private Service Connect in AlloyDB for PostgreSQL, see [Private IP overview](https://docs.cloud.google.com/alloydb/docs/private-ip) in the AlloyDB for PostgreSQL documentation.

## Configure connectivity using VPC peering

VPC peering works by configuring the VPCs to communicate with one another. If your source is in the same Google Cloud project in AlloyDB or Compute Engine, then this allows the destination to communicate with the source directly. If your source is accessible with VPN, then configure the source network and Cloud VPN to communicate with each other with the VPN. For more information, see [ connecting VPCs through VPNs](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpns#vpc-vpn). 

VPC chaining isn't supported. If your source is in a different Google Cloud project, then see [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) to learn how to connect resources from multiple projects to a common VPC network for VPC peering.

The source database server's firewall must be configured to allow the entire **internal IP range** allocated for the **private service connection** of the [VPC network that the AlloyDB destination instance is going to use](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#dest).

To find the **internal IP range** in the console:

  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.

  2. Select the VPC network that you want to use.

  3. Select the **PRIVATE SERVICE CONNECTION** tab.


Make sure the replication connections section of the `pg_hba.conf` file or the security groups definitions in AWS RDS on the source database are updated to accept connections from the AlloyDB VPC's IP address range. Note: To use Virtual Private Cloud networking, you must enable the [Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com) for your Google Cloud project. 

VPC peering uses private services access, which must be configured once for each project using VPC peering. After you have established `private services access`, test your migration job to verify connectivity.

### Configuring private services access for Database Migration Service

If you are using private IP for any of your Database Migration Service instances, you only need to configure private services access one time for every Google Cloud project that has or needs to connect to a Database Migration Service instance.

**Important:** When you create a private connection between your VPC network and the Database Migration Service service, it becomes available for use by any Google service that supports private services access. If you later delete the private connection, you remove private connectivity to your Database Migration Service instances and _any other service that is using that connection_. Removing the private connection does not delete or deprovision any resources.

Establishing private services access requires the compute.networkAdmin IAM role. After private services access is established for your network, you no longer need the `compute.networkAdmin` IAM role to configure an instance to use private IP.

Private services access requires you to first allocate an internal IP address range, then create a private connection, and then export a custom route.

An allocated range is a reserved CIDR block that can't otherwise be used in your local VPC network. When you create a private connection, you specify an allocation. The private connection links your VPC network with the underlying ("service producer") VPC network.

When you create a private connection, the VPC network and service producer network exchange subnet routes only. You must export the VPC network's custom routes so that the service provider's network can import them and correctly route traffic to your on-premises network.

A peering configuration establishes the intent to connect to another VPC network. Your network and the other network are not connected until each one has a peering configuration for the other. After the other network has a corresponding configuration to peer with your network, the peering state changes to ACTIVE in both networks, and they are connected. If there's no matching peering configuration in the other network, the peering state remains INACTIVE, indicating that your network is not connected to the other one.

Once connected, the two networks always exchange subnet routes. You can optionally import both static and dynamic custom routes from a peered network if it has been configured to export them

**Note:** Because a private connection is implemented as a VPC Network Peering connection, the behaviors and constraints of peering connections also apply to private connections, such as VPC Network Peering [limits](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering).

There are two parts to the private services access configuration process:

  * Allocating an IP address range. The range encompasses all of your instances.
  * Creating a private connection from your VPC network to the service producer network.



### Allocating an IP address range

### Console

  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.
  2. Select the VPC network that you want to use.
  3. Select the **Private service connection** tab.
  4. Select the **Allocated IP ranges for services** tab.
  5. Click **Allocate IP range**.
  6. For the **Name** of the allocated range, specify `google-managed-services-VPC_NETWORK_NAME`, where `VPC_NETWORK_NAME` is the name of the VPC network you are connecting (for example, `google-managed-services-default`). The **Description** is optional.

  7. Click **ALLOCATE** to create the allocated range.




### gcloud

Do one of the following:

  * To specify an address range and a prefix length (subnet mask), use the `addresses` and `prefix-length` flags. For example, to allocate the CIDR block `192.168.0.0/16`, specify `192.168.0.0` for the address and `16` for the prefix length.
        
        gcloud compute addresses create google-managed-services-[VPC_NETWORK_NAME] \
            --global \
            --purpose=VPC_PEERING \
            --addresses=192.168.0.0 \
            --prefix-length=16 \
            --network=[VPC_NETWORK_NAME]
        

  * To specify a prefix length (subnet mask) only, just use the `prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network. The following example selects an unused IP address range with a `16` bit prefix length.
        
        gcloud compute addresses create google-managed-services-[VPC_NETWORK_NAME] \
            --global \
            --purpose=VPC_PEERING \
            --prefix-length=16 \
            --network=[VPC_NETWORK_NAME]
        




Replace `[VPC_NETWORK_NAME]` with the name of your VPC network, such as `my-vpc-network`.

The following example allocates an IP range that allows resources in the VPC network `my-vpc-network` to connect to Database Migration Service instances using private IP.
    
    
    gcloud compute addresses create google-managed-services-my-vpc-network \
        --global \
        --purpose=VPC_PEERING \
        --prefix-length=16 \
        --network=my-vpc-network \
        --project=my-project
    

### Creating a private connection

### Console

  1. [Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list) in the Google Cloud console.
  2. Select the VPC network that you want to use.
  3. Select the **Private service connection** tab.
  4. Select the **Private connections to services** tab.
  5. Click **Create connection** to create a private connection between your network and a service producer.
  6. For the **Assigned allocation** , select one or more existing allocated ranges that aren't being used by other service producers, and then click **OK**.
  7. Click **CONNECT** to create the connection.



### gcloud

  1. Create a private connection.
         
         gcloud services vpc-peerings connect \
             --service=servicenetworking.googleapis.com \
             --ranges=google-managed-services-[VPC_NETWORK_NAME] \
             --network=[VPC_NETWORK_NAME] \
             --project=[PROJECT_ID]
         

Replace `[VPC_NETWORK_NAME]` with the name of your VPC network and `[PROJECT_ID]` with the ID of the project that contains your VPC network.

The command initiates a long-running operation, returning an operation name.

  2. Check whether the operation was successful.
         
         gcloud services vpc-peerings operations describe \
             --name=[OPERATION_NAME]
         

Replace `[OPERATION_NAME]` with the operation name that was returned from the previous step.




You can specify more than one allocated range when you create a private connection. For example, if a range has been exhausted, you can assign additional allocated ranges. The service uses IP addresses from all the provided ranges in the order that you specified.

### Exporting custom routes

Update an existing VPC Network Peering connection to change whether your VPC network exports or imports custom routes to or from the peer VPC network.

Your network imports custom routes only if the peer network is also exporting custom routes, and the peer network receives custom routes only if it imports them.

###  Console 

  1. Go to the VPC Network Peering page in the Google Cloud console.   
[Go to the VPC Network Peering page](https://console.cloud.google.com/networking/vpc-connectivity/peering)
  2. Select the peering connection to update.
  3. Click **EDIT**.
  4. Update your custom route settings by selecting or deselecting **Import custom routes** or **Export custom routes**.
  5. Click **SAVE**.



###  gcloud 

Update the peering connection to change your import or export settings for custom routes.
    
    
    gcloud compute networks peerings update [PEERING-NAME] \
        --network=[MY-LOCAL-NETWORK] \
        [--[no-]import-custom-routes] \
        [--[no-]export-custom-routes]
    

### Granting the `roles/servicenetworking.serviceAgent` role
    
    
      gcloud beta services identity create \
        --service=servicenetworking.googleapis.com \
        --project=project-id
    
    
    
      gcloud projects add-iam-policy-binding project-id \
        --member="service-account-prefix@service-networking.iam.gserviceaccount.com" \
        --role="roles/servicenetworking.serviceAgent"
    

## Configure connectivity using Private Service Connect interfaces

For homogeneous AlloyDB for PostgreSQL migrations, AlloyDB for PostgreSQL can use Private Service Connect interfaces to establish a connection over private networks. This connectivity method is only available when you [migrate to an existing instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance).

To use Private Service Connect interfaces, do the following:

  1. Create an AlloyDB for PostgreSQL cluster enabled for Private Service Connect, and a primary instance in that cluster. See [Enable Private Service Connect](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#enable-psc) in the AlloyDB for PostgreSQL documentation.

  2. Configure Private Service Connect for outbound connectivity on your instance. See [Configure outbound connectivity](https://docs.cloud.google.com/alloydb/docs/configure-private-service-connect#configure-outbound-connectivity) in the AlloyDB for PostgreSQL documentation.

Make sure that the VPC network where you create the network attachment is the network where you can reach the private IP address of your source database.

  3. At a later stage, when you [create the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance), select **PSC interface** for your connectivity method.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


