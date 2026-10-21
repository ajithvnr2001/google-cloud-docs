---
url: https://docs.cloud.google.com/filestore/docs/configure-nfsv4-managed-ad/
title: Create a Filestore instance with Managed Microsoft AD \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:20.040617+00:00
---

# Create a Filestore instance with Managed Microsoft AD  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/configure-nfsv4-managed-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create a Filestore instance with Managed Microsoft AD Stay organized with collections  Save and categorize content based on your preferences. 

Create a Filestore instance that uses the NFSv4.1 protocol with Managed Microsoft AD.

## Before you begin

Before you create a new Filestore instance ensure you have enough quota. Instance quota ranges by the region location and service tier you want to use. To increase available quota, you must submit a [quota increase request](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).

## Create the Managed Microsoft AD domain

If you want to use Managed Microsoft AD with a Filestore instance, the Managed Microsoft AD domain must be created before the Filestore instance.

  1. Both the Managed Microsoft AD domain and the Filestore instance must use the same [VPC](https://docs.cloud.google.com/vpc/docs/vpc) while on the same project.

If your Managed Microsoft AD service is hosted in a project separate from the Filestore instance you want to use, then the Filestore VPC network needs to be peered to the Managed Microsoft AD domain.

For more information, see [Deploy Managed Microsoft AD with cross-project access using domain peering](https://docs.cloud.google.com/managed-microsoft-ad/docs/shared-vpc-managedad-cloudsql).

  2. [Complete all the setup steps to create a Filestore instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

  3. Ensure that Managed Microsoft AD users have [POSIX RFC 2307](https://www.rfc-editor.org/rfc/rfc2307.txt) and [RFC 2307bis](https://datatracker.ietf.org/doc/html/draft-howard-rfc2307bis-01) fields populated, similar to the following.

For more information on how to configure objects in Managed Microsoft AD, see [Managed Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).

###  Active Directory Users and Computers 

The following steps describe the attributes you need to set for LDAP users and groups. You can manage POSIX attributes by using the _Active Directory Users and Computers_ MMC snap-in.

Open the _Attribute Editor_ as follows:

     1. Click **Start**.
     2. Click **Windows Administrative Tools** , and select **Active Directory Users and Computers**.

The **Active Directory Users and Computers** window opens.

     3. Select the domain name that you want to view. To expand its contents, click the arrow_rightexpander arrow.

     4. In the Active Directory Users and Computers **View** menu, select **Advanced Features**.

     5. In the left pane, double-click **Users**.

     6. In the users list, double-click a user to see its **Attribute Editor** tab.

LDAP users must have the following attributes set:

        * `uid`
        * `uidNumber`
        * `cn`
        * `gidNumber`
        * `objectClass`

Each user must have a unique `uidNumber`. Note that the value for the `uid` attribute is case sensitive. For the `objectClass` attribute, `user` is the default setting on most Active Directory (AD) deployments. The following is an example:
    
    uid: Alice
    uidNumber: 139
    gidNumber: 555
    objectClass: user
    

LDAP groups must have the following attributes set:

        * `cn`
        * `gidNumber`
        * `objectClass`

Each group must have a unique `gidNumber`. Note that the value for the `cn` attribute is case sensitive. For the `objectClass` attribute, `group` is the default setting on most AD deployments. The following is an example:
    
    cn: AliceGroup
    gidNumber: 555
    objectClass: group
    

  4. Grant Filestore access to create and manage objects in Managed Microsoft AD using the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
         
         gcloud projects add-iam-policy-binding MANAGED_MICROSOFT_AD_PROJECT_ID \
         --member=serviceAccount:service-$(gcloud projects describe PROJECT_ID \
         --format='value(projectNumber)')@cloud-filer.iam.gserviceaccount.com \
         --role=roles/managedidentities.filestoreintegrator
         

Replace the following:

     * MANAGED_MICROSOFT_AD_PROJECT_ID is the project ID of the project where the Managed Microsoft AD domain is located.
     * PROJECT_ID is the project ID of the project where the Filestore instance is located.

You might see an error, similar to the following:
    
    INVALID_ARGUMENT: Service account service-123456789012@cloud-filer.iam.gserviceaccount.com does not exist.
    

If so, use the following command to resolve it:
    
    gcloud beta services identity create --service=file.googleapis.com --project \ MANAGED_MICROSOFT_AD_PROJECT_ID
    




## Create a Filestore instance with Managed Microsoft AD

###  Google Cloud console 

### Set up the instance parameters

  1. In the Google Cloud console, go to the Filestore instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click **Create Instance**.

  3. Specify the basic parameters of the instance:

     1. In the **Instance ID** field, enter the name you want to use for the Filestore instance.
     2. In **Instance Type** , select **Regional** or **Zonal**.

To create an enterprise instance, you must run operations directly through the Filestore API.

     3. In **Allocated Capacity** , enter the capacity you want to use. You must enter a value between 1 TB and 10 TB, in increments of 256 GiB (0.25 TiB).

     4. In **Region** , select the region you want to use.

     5. In **VPC Network** , select the network you want to use for the Filestore instance and NFS clients.

        * If Managed Microsoft AD is in the same project as the Filestore instance, the VPC network needs to be authorized in the Managed Microsoft AD domain.
        * If Managed Microsoft AD is in a separate project, then the VPC network should be configured with Active Directory network peering on the Managed Microsoft AD configuration.
     6. In **Allocated IP range** , select **Use an automatically allocated IP range (recommended)**.

     7. In **Protocol** , select **NFSv4.1**.




### Configure the instance's authentication settings

  1. Configure the instance's authentication settings. 
     1. Click **Authentication**.
     2. Select the project hosting Managed Microsoft AD. For the purpose of this guide, we'll assume the current project is the one we want to use. In the **Join an Active Directory domain** list, select the Managed Microsoft AD domain you want to use.
     3. In the **Computer account name** field, enter the computer account name you want to use to identify the Filestore instance in the Managed Microsoft AD domain. The name is limited to 15 alphanumeric characters.
     4. In the **File share name** field, enter the name of the share as it will be used by the NFSv4.1 clients.
  2. In the **Access Control** pane, complete either of the following steps:

     * If using Managed Microsoft AD, select **Restrict access by IP address or range**.

       1. Set the access rule by IP or subnet you want to define. For the purpose of this guide, use the following settings:
       2. In the **IP address or range 1** field, enter the IP address or range you want to use.
       3. Click the **Access 1** drop-down list, and select **Admin**. Click the **Mount`sec=` 1** drop-down list, and select the **sys** checkbox.

The Filestore default `/` owner is `root`. To enable access to the instance for other users and groups, you must create an access rule that enables management VM access using the `Admin` role and the `sec=sys` security setting.

     * If you're not using Managed Microsoft AD, select **Grant access to all clients on the VPC network**.

If Managed Microsoft AD is not used, the only supported security setting is `sec=sys`.

  3. Click **Create** to create the instance.




###  gcloud 

  1. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

If you already have the gcloud CLI installed, run the following command to update it:
         
         gcloud components update
         

  2. Run the [`gcloud beta filestore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/create) command to create a Filestore zonal, regional, or enterprise instance:
         
         gcloud beta filestore instances create INSTANCE-ID \
            --description="DESCRIPTION" \
            --region=LOCATION \
            --tier=TIER \
            --protocol=PROTOCOL \
            --file-share=name="FILE_SHARE_NAME",capacity=CAPACITYTB \
            --network=name="VPC_NETWORK",connect-mode=CONNECT_MODE,reserved-ip-range="RESERVED_IP_RANGE" \
            --managed-ad=domain=projects/MANAGED_AD_PROJECT_ID/locations/global/domains/MANAGED_AD_DOMAIN_NAME,computer=DOMAIN_COMPUTER_ACCOUNT \
            --project=CONSUMER_PROJECT_ID
         
         

Where:

     * INSTANCE_ID is the instance ID of the Filestore instance that you want to create. See [Name your instance](https://docs.cloud.google.com/filestore/docs/creating-instances#name_your_instance).
     * DESCRIPTION is a description for the instance you want to use.
     * LOCATION is the location where you want the Filestore instance to reside.
     * TIER is the [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) you want to use.
     * PROTOCOL is [`NFS_v4_1`](https://docs.cloud.google.com/filestore/docs/about-supported-protocols).
     * FILE_SHARE_NAME is the name you specify for the NFS file share that is served from the instance.
     * CAPACITY is the size you want for the file share, between 1 TiB to 10 TiB.
     * VPC_NETWORK is the name of the VPC network you want the instance to use. See [Select the VPC network](https://docs.cloud.google.com/filestore/docs/creating-instances#selecting_vpc_network).

       * If you want to specify a Shared VPC from a service project, you must specify the fully-qualified network name, which is in the following format:
    
    projects/HOST_PROJECT_ID/global/networks/SHARED_VPC_NAME
    

Specify `connect-mode=PRIVATE_SERVICE_ACCESS`, similar to the following:
    
    --network=name=projects/host/global/networks/shared-vpc-1,connect-mode=PRIVATE_SERVICE_ACCESS
    

       * You can't specify a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) for the vpc_network value. If necessary, create a new VPC network to use by following the instructions in [Create an auto mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network).
     * MANAGED_AD_PROJECT_ID is the project ID where the Managed Microsoft AD service is located.

     * MANAGED_AD_DOMAIN_NAME is the domain name of the Managed Microsoft AD service you want to use. You choose this domain name when creating a Managed Microsoft AD domain.

     * DOMAIN_COMPUTER_ACCOUNT is any name that you want the cluster to be called in the domain.

     * CONSUMER_PROJECT_ID is the project ID of the project that contains the Filestore instance.

     * CONNECT_MODE is `DIRECT_PEERING` or `PRIVATE_SERVICE_ACCESS`. If you are specifying a Shared VPC as the network, you must also specify `PRIVATE_SERVICE_ACCESS` as the connect mode. This flag is required for VPC Network Peering, which is a requirement when using Managed Microsoft AD.

     * RESERVED_IP_RANGE is the IP address range for the Filestore instance. If you are specifying `connect-mode=PRIVATE_SERVICE_ACCESS`, and want to use a reserved IP address range, you must specify the name of an [allocated address range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) instead of a CIDR range. See [Configure a reserved IP address](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_a_reserved_ip_address_range). We recommend that you skip this flag to allow Filestore to automatically find a free IP address range and assign it to the instance.




## Disconnect a Managed Microsoft AD from a Filestore instance

###  Google Cloud console 

  1. Disconnect a Filestore instance connected to Managed Microsoft AD.

In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the instance you want to edit.

  3. In the **NFS mount point** pane, under **Protocol** , next to **Directory service name** , click  delete  **Disconnect AD domain**.

  4. In the **Disconnect from domain failed** window, read the alert, then, click **Edit instance**.

At least one rule in **Access control** must be mapped to the Administrator role with the `sys` mount security setting, such as, **Access=Admin Mount** and **`sec=`sys**.

  5. In the **Edit share** pane, locate the rule where **Access** is set to **Admin**. Click **Mount`sec=` ...**, and select `sys` to add that option to the existing setting.

  6. Click **OK**.

  7. Click **Save**.

  8. Next to **Directory service name** , click  delete  **Disconnect AD domain**.

  9. In the field in the **Disconnect from domain?** window, enter the name of the domain from which you want to disconnect.

  10. Click **Disconnect**.




### Edit the access rules

  1. Refresh the page. Note that **Directory service name** is now set to **None**.

  2. Click **Edit**.

  3. In the **Edit share** pane, locate any rule that sets access for a role other than **Admin** , such as **Editor**. In the rule, click **Mount`sec=` ...**, and select `sys` to add it to the existing setting. Click **OK**.

  4. Click **Save**.

  5. Refresh the page.

The rule settings update.




## Reconnect a Managed Microsoft AD to a Filestore instance

###  Google Cloud console 

  1. Reconnect a Filestore instance to Managed Microsoft AD.

In the **NFS mount point** pane, under **Protocol** , next to **Directory service name** , click  edit  **Join AD domain**.

  2. In the **Join this instance to an Active Directory Domain** window, select **Use domains from the current project** , in the **Join an Active Directory Domain** menu, select the domain you want to use.

  3. In the **Computer account name** menu, enter a name.

  4. Click **Join Domain**.

  5. Refresh the page. Note that **Directory service name** has been updated with your selection.

  6. Click **Edit**.

  7. In the **Edit share** pane, click **Mount`sec=` ...** in all applicable rules and remove the `sys` selection. Click **OK**.

  8. Click **Save**.

  9. Refresh the page.




The rule settings update.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
