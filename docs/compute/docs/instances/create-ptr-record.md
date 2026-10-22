---
url: https://docs.cloud.google.com/compute/docs/instances/create-ptr-record/
title: Create a PTR record for a VM instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:54.523292+00:00
---

# Create a PTR record for a VM instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-ptr-record/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a PTR record for a VM instance Stay organized with collections  Save and categorize content based on your preferences. 

Configurable [PTR records](https://www.cloudns.net/wiki/article/40/) let you define the reverse DNS record associated with the external IP address of a VM instance so that applications that rely on these records can operate as intended.

Some applications require reverse DNS records (PTR records) to resolve IP addresses to domain names. For example, applications that use SMTP require a PTR record that points to the domain from which an email is being sent. Without that record, spam filters can mark emails with low reputation, which causes email to end up in spam folders or not be sent at all.

You can add PTR records to only the primary network interface of a VM instance. PTR records are not available for load balancer frontends, [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview), or other non-VM IP addresses.

IPv6 PTR records are only available if the instance's primary network interface is connected to a dual-stack or IPv6-only subnet that has an external IPv6 address range. For dual-stack network interfaces, you can have separate IPv4 and IPv6 PTR records.

To create custom PTR records that override the automatically created internal DNS PTR names, see [Managed reverse lookup zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#managed_reverse_lookup_zones).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Verify your domain ownership

Before you create a VM with a custom PTR record, verify that you own the domain name. Verifying ownership is a security measure to prove to Google that you are the domain owner.

You can verify your domain name in 2 ways:

  * If you have a Google account, you can verify by using Search Console.
  * If you have a Google or non-Google account, you can verify by adding your VM's IP address to your DNS configuration.



### Verify by using Search Console

  1. Open [Search Console](https://search.google.com/search-console/welcome) and sign in by using the Google Account that you will use to add a PTR record to your instance. You can verify domain ownership with multiple accounts.
  2. Enter the PTR domain name.
  3. Click **Continue**.
  4. Follow the instructions, and then click **Go to Property**.
  5. Click on **Settings** (found in the menu on the left near the bottom), and then click **Ownership Verification**.



After you verify that you own the domain, in the **Settings** pane, click on **Users** to see other verified owners. To add PTR records in other domains, click the property picker on the left that displays your current domain. Click **Add a property** to add those domains.

If your domain name is not immediately verified, use the **Recommended Method** to obtain verification.

### Verify by adding your VM's IP address to your DNS configuration

  1. If your VM does not exist yet, [reserve a regional static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) and use it later during VM creation.
  2. Add an "A" record with the VM's external IP address to the DNS configuration of your domain.



## Create VM instances with PTR records

You can specify PTR records when you create new instances. To add a PTR record for an existing instance, see Add PTR records.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the VM details.

  3. Expand the **Advanced options** section, and then do the following:

     1. Expand the **Networking** section.
     2. Create one or more network interfaces to use with this VM. Alternatively, you can use the default network interface.
     3. In the **Network interfaces** section, expand the first network interface, which is the primary network interface.
     4. In the **Public DNS PTR record** section, select each type of PTR record that you want to add.
     5. In the **PTR domain name** field, enter a domain name for each type of PTR record that you want to add.
     6. In the **External IPv4 address** or **External IPv6 address** field, choose your previously reserved IP address. If you have verified your VM's IP address through your DNS configuration, then you must specify that address.
     7. To confirm the network interface settings, click **Done**.
  4. Configure the remaining properties for your new VM.

  5. At the bottom of the page, click **Create**.




After the VM starts, you can run a reverse DNS lookup on the external IP address of your VM to confirm that the PTR record is working as expected.

###  gcloud 

  * To create a new instance with an associated IPv4 PTR record, use the [`gcloud instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
        
        gcloud compute instances create INSTANCE_NAME \
            --image-family IMAGE_FAMILY \
            --image-project IMAGE_PROJECT \
            --public-ptr \
            --public-ptr-domain DOMAIN_NAME \
            --address=IP_ADDRESS
        

Replace the following:

    * `INSTANCE_NAME`: the name of the new VM instance.
    * `IMAGE_FAMILY`: one of the [available image families](https://docs.cloud.google.com/compute/docs/images#image_families).
    * `IMAGE_PROJECT`: the Google Cloud project against which all image and image family references are resolved. If you don't supply a project name, the current default project is used.
    * `DOMAIN_NAME`: the domain name to add to this instance.
    * `IP_ADDRESS`: your previously reserved IP address. If you have verified your VM's IP address through your DNS configuration, then you must specify that address.
  * To create a new instance with an associated IPv6 PTR record, do the following:

    1. [Create a dual-stack or IPv6-only VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6).
    2. Add an IPv6 PTR record.



###  REST 

  * To create a new instance with an IPv4 PTR record, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
        {
          "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
          "name": "INSTANCE_NAME",
          "disks": [
            {
              "initializeParams": {
                "sourceImage": "projects/debian-cloud/global/images/family/debian-10"
              },
              "boot": true
            }
          ],
          "networkInterfaces": [
            {
              "network": "NETWORK",
              "accessConfigs": [
                {
                  "type": "ONE_TO_ONE_NAT",
                  "name": "External NAT",
                  "natIP": "IP_ADDRESS",
                  "publicPtrDomainName": "DOMAIN_NAME",
                  "setPublicPtr": true
                }
              ]
            }
          ]
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of your project.
    * `ZONE`: the zone of your instance.
    * `MACHINE_TYPE`: the machine type.
    * `INSTANCE_NAME`: the name of the instance.
    * `NETWORK`: the URL of the network.
    * `IP_ADDRESS`: your previously reserved IP address. If you have verified your VM's IP address through your DNS configuration, then you must specify that address.
    * `DOMAIN_NAME`: the domain name to add.
  * To create a new instance with an IPv6 PTR record, do the following:

    1. [Create a dual-stack or IPv6-only VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6).
    2. Add an IPv6 PTR record.



## Add PTR records

You can add PTR records by updating the access configuration on the primary network interface, `nic0`, of a VM instance.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the instance that you want to edit.

  3. Click **Edit**.

  4. In the **Network interfaces** section, click the primary network interface.

  5. In the **Public DNS PTR record** section, select each type of PTR record that you want to add.

  6. In the **PTR domain name** field, enter a domain name for each type of PTR record that you want to add.

  7. Click **Done** , and then click **Save**.




###  gcloud 

  1. If your VM doesn't have an access configuration, add one by using the [`gcloud compute instances add-access-config` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-access-config).
         
         gcloud compute instances add-access-config INSTANCE_NAME
         

Replace `INSTANCE_NAME` with the name of your instance.

  2. Update the access configuration to add the PTR record by using the [`gcloud compute instances update-access-config` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-access-config). To add both IPv4 and IPv6 PTR records, use the following commands individually.

     * For IPv4:
           
           gcloud compute instances update-access-config INSTANCE_NAME \
               --public-ptr \
               --public-ptr-domain DOMAIN_NAME
           

     * For IPv6:
           
           gcloud compute instances update-access-config INSTANCE_NAME \
               --ipv6-public-ptr-domain=DOMAIN_NAME
           

Replace the following:

     * `INSTANCE_NAME`: the name of the instance to update.
     * `DOMAIN_NAME`: the domain name to add.



###  REST 

  1. If your VM doesn't have an access configuration, add one by making a `POST` request to the [`instances.addAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/addAccessConfig).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/addAccessConfig?networkInterface="nic0"
         

  2. Update the access configuration to add the PTR record by making a `POST` request to the [`instances.updateAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/updateAccessConfig). To add both IPv4 and IPv6 PTR records, make the following requests individually.

     * For IPv4:
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateAccessConfig?networkInterface=nic0
           {
             "setPublicPtr": true,
             "publicPtrDomainName": "DOMAIN_NAME",
             "type": "ONE_TO_ONE_NAT"
           }
           

     * For IPv6:
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateAccessConfig?networkInterface=nic0
           {
             "publicPtrDomainName": "DOMAIN_NAME",
             "type": "DIRECT_IPV6"
           }
           

Replace the following:

     * `PROJECT_ID`: the project ID.
     * `ZONE`: the zone of the instance.
     * `INSTANCE_NAME`: the instance name.
     * `DOMAIN_NAME`: the domain name to add.



## Remove PTR records

To remove PTR records, update the access configuration on the primary network interface, `nic0`, of a VM instance. When you remove a PTR record, Google Cloud responds to reverse DNS lookups with a default fully qualified domain name of `googleusercontent.com`.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the instance that you want to edit.

  3. Click **Edit**.

  4. In the **Network interfaces** section, click the primary network interface.

  5. In the **Public DNS PTR record** section, clear the checkbox for each type of PTR record that you want to remove.

  6. Click **Done** , and then click **Save**.




###  gcloud 

To remove a PTR record, use the [`gcloud compute instances update-access-config` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-access-config). To remove both IPv4 and IPv6 PTR records, use the following commands separately.

  * For IPv4:
        
        gcloud compute instances update-access-config INSTANCE_NAME \
            --no-public-ptr
        

  * For IPv6:
        
        gcloud compute instances update-access-config INSTANCE_NAME \
            --no-ipv6-public-ptr
        




Replace `INSTANCE_NAME` with the name of the instance to update.

###  REST 

To remove a PTR record, make a `POST` request to the [`instances.updateAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/updateAccessConfig). To remove both IPv4 and IPv6 PTR records, make the following requests individually.

  * For IPv4:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateAccessConfig?networkInterface=nic0
        {
          "setPublicPtr": false,
          "type": "ONE_TO_ONE_NAT"
        }
        

  * For IPv6:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateAccessConfig?networkInterface=nic0
        {
          "publicPtrDomainName": "",
          "type": "DIRECT_IPV6"
        }
        




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone of the instance.
  * `INSTANCE_NAME`: the instance name.



## Limitations

  * The PTR record logic doesn't handle some edge cases correctly and reverts the DNS PTR records to the fully qualified domain name (FQDN) `googleusercontent.com`. This can happen in the following situations:

    * When a VM is migrated to another host as part of the [live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
    * When an unexpected, rare host error occurs.

To restore functionality, apply the PTR record again.

  * When you stop a VM that has an IPv6 PTR record, the IPv6 PTR record is temporarily deregistered and not visible on the VM. The record is added back automatically when you restart the VM.




## What's next

  * For an overview of how to configure and manage static external IP addresses for your resources, see [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).
  * To learn how to create and manage virtual machine instances, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
