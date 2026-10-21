---
url: https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address/
title: Configure static external IP addresses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:52.391347+00:00
---

# Configure static external IP addresses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure static external IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

You can assign static external IP addresses to your virtual machine (VM) and bare metal instances. You can also change, list, and release static IP addresses for your instances. To reserve a static external IP address, see [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).

External IP addresses can be [static or ephemeral](https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses). If an instance requires a fixed external IP address that does not change, do the following:

  1. Obtain a static external IP address. You can reserve new external IP addresses or promote existing ephemeral external IP addresses.
  2. Assign the reserved IP address to an existing instance, or assign it when creating a new instance.



If you require a static IP address on your internal Compute Engine network, see instead [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address).

For information about reserving a static external IP address or creating a global external IP address, see [Reserve a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).

## Before you begin

  * Read about [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).
  * Read about [quotas and limits for static external IP addresses](https://docs.cloud.google.com/compute/resource-usage#external_ip_addresses).
  * Read about [external IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).
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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to configure and manage static IP addresses, ask your administrator to grant you the following IAM roles on your project: 

  * To create and update instances: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 
  * To set policy constraints for an organization: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure and manage static IP addresses. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure and manage static IP addresses:

  * `compute.instances.update`
  * `compute.instances.updateNetworkInterface`
  * `compute.instances.addAccessConfig`
  * `compute.instances.deleteAccessConfig`
  * `compute.networks.list`
  * `compute.subnetworks.use`
  * `compute.subnetworks.list`
  * To create instances: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To edit organization policies: 
    * `orgpolicy.policy.get`
    * `orgpolicy.policies.create`
    * `orgpolicy.policies.delete`
    * `orgpolicy.policies.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * Only one resource at a time can use a static external IP address.

  * Each compute instance can have multiple network interfaces, and each interface can have the following IP addresses assigned according to its [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types):

    * IPv4-only interfaces: 
      * An internal IPv4 address (required)
      * An external IPv4 address (optional)
    * Dual-stack (IPv4 and IPv6) interfaces: 
      * An internal IPv4 address (required)
      * An external IPv4 address (optional)
      * A `/96` IPv6 address range, either internal or external, but not both (required)
    * IPv6-only interfaces: 
      * A `/96` IPv6 address range, either internal or external, but not both (required)
  * You can't unassign or change the external IPv6 address of a compute instance with an IPv6-only network interface. You can, however, promote an ephemeral external IP address of a resource to a static external IP address so that the address remains reserved even after the resource is deleted.

  * You cannot change the name of a static IP address.




**Note:** Network interfaces can receive traffic from multiple [ forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts), which might serve other external IP addresses. Any number of external IP addresses can reference a network interface through these forwarding rules, but each network interface can be assigned only one external IPv4 address and one external `/96` IPv6 address range. 

For more information about load balancing and forwarding rules, read the [load balancing](https://docs.cloud.google.com/load-balancing/docs) documentation. 

## View available static external IP addresses

To list static external IP addresses that you have reserved for your project, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **External IP addresses**.




###  gcloud 

Use the [`gcloud compute addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list):

  * To list all IP addresses, use the following command:
        
        gcloud compute addresses list

  * To list all global IP addresses, use the following command:
        
        gcloud compute addresses list --global

  * To list all regional IP addresses in a given region, use the following command:
        
        gcloud compute addresses list \
            --regions=REGION
        

Replace `REGION` with the region that you want to list addresses for. You can list addresses of multiple regions by specifying comma-separated region names:
        
        gcloud compute addresses list \
            --regions=REGION1,REGION2,..REGION_n_
        




###  API 

  * To list regional IPv4 or IPv6 addresses, call the [`addresses.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/list):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
        

Replace the following:

    * `PROJECT_ID`: the project ID for this request
    * `REGION`: the name of the region for this request
  * To list all addresses in all regions, call the [`addresses.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/aggregatedList):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/addresses
        

  * To list global IPv4 or IPv6 addresses, call the [`globalAddresses.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/list):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses
        

Replace the following:

`PROJECT_ID`: the project ID for this request




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"google.golang.org/api/iterator"
    
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // listRegionalExternal retrieves list external IP addresses in Google Cloud Platform region.
    func listRegionalExternal(w io.Writer, projectID, region string) ([]*computepb.Address, error) {
    	// projectID := "your_project_id"
    	// region := "europe-west3"
    
    	ctx := context.Background()
    	// Create the service client.
    	addressesClient, err := compute.[NewAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_AddressesClient_NewAddressesRESTClient)(ctx)
    	if err != nil {
    		return nil, err
    	}
    	defer addressesClient.Close()
    
    	// Build the request.
    	req := &computepb.ListAddressesRequest{
    		Project: projectID,
    		Region:  region,
    	}
    
    	// List the addresses.
    	it := addressesClient.List(ctx, req)
    
    	// Iterate over the results.
    	var addresses []*computepb.Address
    	for {
    		address, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return nil, err
    		}
    		addresses = append(addresses, address)
    	}
    
    	// Print the addresses.
    	fmt.Fprint(w, "Fetched addresses: \n")
    	for _, address := range addresses {
    		fmt.Fprintf(w, "%s\n", *address.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name))
    	}
    
    	return addresses, nil
    }
    
    // listGlobalExternal retrieves list external global IP addresses in Google Cloud Platform.
    func listGlobalExternal(w io.Writer, projectID string) ([]*computepb.Address, error) {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	// Create the service client.
    	addressesClient, err := compute.[NewGlobalAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_GlobalAddressesClient_NewGlobalAddressesRESTClient)(ctx)
    	if err != nil {
    		return nil, err
    	}
    	defer addressesClient.Close()
    
    	// Build the request.
    	req := &computepb.ListGlobalAddressesRequest{
    		Project: projectID,
    	}
    
    	// List the addresses.
    	it := addressesClient.List(ctx, req)
    
    	// Iterate over the results.
    	var addresses []*computepb.Address
    	for {
    		address, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return nil, err
    		}
    		addresses = append(addresses, address)
    	}
    
    	// Print the addresses.
    	fmt.Fprint(w, "Fetched addresses: \n")
    	for _, address := range addresses {
    		fmt.Fprintf(w, "%s\n", *address.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name))
    	}
    
    	return addresses, nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html);
    import com.google.cloud.compute.v1.[AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html);
    import com.google.cloud.compute.v1.[GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html);
    import com.google.cloud.compute.v1.[ListAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAddressesRequest.html);
    import com.google.cloud.compute.v1.[ListGlobalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalAddressesRequest.html);
    import com.google.common.collect.Lists;
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class ListStaticExternalIp {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Region where the VM and IP is located.
        String region = "your-region-id";
    
        listStaticExternalIp(projectId, region);
      }
    
      // Lists all static external IP addresses, either regional or global.
      public static List<Address> listStaticExternalIp(String projectId, String region)
              throws IOException {
        // Use regional client if a region is specified
        if (region != null) {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html) client = [AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html).create()) {
            [ListAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAddressesRequest.html) request = [ListAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAddressesRequest.html).newBuilder()
                    .setProject(projectId)
                    .setRegion(region)
                    .build();
    
            return Lists.newArrayList(client.list(request).iterateAll());
          }
        } else {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html) client = [GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html).create()) {
            [ListGlobalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalAddressesRequest.html) request = [ListGlobalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalAddressesRequest.html).newBuilder()
                    .setProject(projectId)
                    .build();
    
            return Lists.newArrayList(client.list(request).iterateAll());
          }
        }
      }
    }

###  Python 
    
    
    from typing import List, Optional
    
    from google.cloud.compute_v1.services.addresses.client import AddressesClient
    from google.cloud.compute_v1.services.global_addresses import GlobalAddressesClient
    from google.cloud.compute_v1.types import Address
    
    
    def list_static_ip_addresses(
        project_id: str, region: Optional[str] = None
    ) -> List[Address]:
        """
        Lists all static external IP addresses, either regional or global.
    
        Args:
        project_id (str): project ID.
        region (Optional[str]): The region of the IP addresses if regional. None if global.
    
        Returns:
        List[Address]: A list of Address objects containing details about the requested IPs.
        """
        if region:
            # Use regional client if a region is specified
            client = AddressesClient()
            addresses_iterator = client.list(project=project_id, region=region)
        else:
            # Use global client if no region is specified
            client = GlobalAddressesClient()
            addresses_iterator = client.list(project=project_id)
    
        return list(addresses_iterator)  # Convert the iterator to a list to return
    
    

## Configure static external IP addresses

The following sections describe how to configure static external IP addresses for your instances.

### Create an instance that uses a static external IP address

After you have [reserved a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static), you can assign it to an instance.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. To assign a static external IP address to the instance, do the following:

     1. In the navigation menu, click **Networking**.

     2. In the **Network interfaces** section, specify the network interfaces that you want for the instance by using the following options:

        * To add a network interface, click **Add a network interface**. Then, in the **Network** list, select a network.

        * To delete a network interface, click delete **Delete**.

     3. Select one of the following options:

        * To assign a static external IPv4 address, do the following:

          1. Expand a network interface.
          2. Select the IP address from the **External IPv4 address** list.
        * To assign a static external IPv6 address, do the following:

          1. Expand a network interface that contains a subnet with an external IPv6 address range.
          2. Select that subnet from the **Subnetwork** list.
          3. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)** or **IPv6 (single-stack)**.
          4. Select the newly reserved external IPv6 address from the **External IPv6 address** list. Alternatively, select **Reserve static external IPv6 address** and reserve a new static external IPv6 address.
          5. For **Network Service Tier** , select **Premium**.
     4. To finish modifying the network interface, click **Done**.

  3. Continue with the instance creation process.




###  gcloud 

You can create an instance and assign a static regional external IP address that you have already reserved.

  * To assign a static external IPv4 address, do the following:
        
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --address=IPV4_ADDRESS
        

  * To assign a static external IPv6 address, do the following:
        
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --subnet=SUBNET \
            --stack-type=STACK_TYPE \
            --external-ipv6-address=IPV6_ADDRESS \
            --external-ipv6-prefix-length=96 \
            --ipv6-network-tier=PREMIUM
        

Replace the following:

    * `INSTANCE_NAME`: the name of the compute instance.
    * `ZONE`: the zone to create the instance in
    * `IPV4_ADDRESS`: the IPv4 address to assign to the instance. Use the reserved static external IP address, not the address name.
    * `SUBNET`: a subnet that contains external IPv6 addresses
    * `STACK_TYPE`: the stack type for the instance, either `IPV4_IPV6` (dual-stack) or `IPV6_ONLY`
    * `IPV6_ADDRESS`: the IPv6 address to assign to the instance. Use the reserved static external IP address, not the address name.



###  Terraform 

You can use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to assign an external IP address.
    
    
    resource "google_compute_instance" "default" {
      name         = "dns-proxy-nfs"
      machine_type = "n1-standard-1"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = "ubuntu-1404-trusty-v20160627"
        }
      }
    
      network_interface {
        network = "default"
        access_config {
          nat_ip = google_compute_address.default.address
        }
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

  * To assign a static external IPv4 address to a new compute instance, do the following:

In your request to [create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), explicitly provide the [`networkInterfaces[].accessConfigs[].natIP`](https://docs.cloud.google.com/compute/docs/reference/latest/instances#networkInterfaces.accessConfigs.natIP) property and the external IPv4 address that you want to use, for example:
        
        {
          "name": "INSTANCE_NAME",
          "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
          "networkInterfaces": [{
              "accessConfigs": [{
                "type": "ONE_TO_ONE_NAT",
                "name": "External NAT",
                "natIP": "IPV4_ADDRESS"
              }],
              "network": "global/networks/default"
          }],
          "disks": [{
              "autoDelete": "true",
                "boot": "true",
                "type": "PERSISTENT",
                "initializeParams": {
                    "sourceImage": "SOURCE_IMAGE"
                 }
          }]
        }
        

Replace the following:

    * `INSTANCE_NAME`: the name of the compute instance
    * `ZONE`: the zone to create the instance in
    * `MACHINE_TYPE`: Optional: a full or partial URL of the machine type resource to use when creating the instance, in the format: `zones/ZONE/machineTypes/MACHINE_TYPE`
    * `IPV4_ADDRESS`: the IPv4 address to assign to the instance. Use the reserved static external IP address, not the address name.
    * `SOURCE_IMAGE`: a specific version of a public image, such as `projects/debian-cloud/global/images/debian-10-buster-v20200309` or an image family, such as `projects/debian-cloud/global/images/family/debian-10`
  * To assign a static external IPv6 address to a new instance, do the following:

In your request to [create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), explicitly provide the [`networkInterfaces[].ipv6AccessConfigs[].externalIpv6`](https://docs.cloud.google.com/compute/docs/reference/latest/instances#networkInterfaces.ipv6AccessConfigs.externalIpv6) property and the external IPv6 address that you want to use, for example:
        
        {
          "name": "INSTANCE_NAME",
          "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
          "networkInterfaces": [{
                  "ipv6AccessConfigs": [{
                 "externalIpv6": "IPV6_ADDRESS",
                 "externalIpv6PrefixLength": 96,
                 "name": "external-ipv6-access-config",
                 "networkTier": "PREMIUM",
                 "type": "DIRECT_IPV6"
                  }],
              "stackType": "STACK_TYPE",
              "subnetwork":"SUBNETWORK"
          }],
          "disks": [{
              "autoDelete": "true",
              "boot": "true",
              "mode": "READ_WRITE",
              "type": "PERSISTENT",
              "initializeParams": {
                  "sourceImage": "SOURCE_IMAGE"
              },
          }],
        }
        

Replace the following:

    * `INSTANCE_NAME`: the name of the compute instance
    * `ZONE`: the zone to create the instance in
    * `MACHINE_TYPE`: Optional: a full or partial URL of the machine type resource to use when creating the instance, in the format: `zones/ZONE/machineTypes/MACHINE_TYPE`
    * `IPV6_ADDRESS`: the IPv6 address to assign to the instance. Use the reserved static external IP address, not the address name.
    * `STACK_TYPE`: the stack type for the instance, either `IPV4_IPV6` (dual-stack) or `IPV6_ONLY`
    * `SUBNET`: a subnet that contains external IPv6 addresses
    * `SOURCE_IMAGE`: a specific version of a public image, such as `"projects/debian-cloud/global/images/debian-10-buster-v20200309"` or an image family, such as `"projects/debian-cloud/global/images/family/debian-10"`



###  Go 
    
    
    // assignStaticExternalToNewVM creates a new VM instance and assigns a static external IP address to it.
    // NOTE: ip address is expected to exist and be located in the same region as new VM
    func assignStaticExternalToNewVM(w io.Writer, projectID, zone, instanceName, ipAddress string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// ipAddress := 301.222.11.123
    
    	ctx := context.Background()
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	imagesClient, err := compute.NewImagesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	// List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details.
    	newestDebianReq := &computepb.GetFromFamilyImageRequest{
    		Project: "debian-cloud",
    		Family:  "debian-12",
    	}
    	newestDebian, err := imagesClient.GetFromFamily(ctx, newestDebianReq)
    	if err != nil {
    		return fmt.Errorf("unable to get image from family: %w", err)
    	}
    
    	req := &computepb.InsertInstanceRequest{
    		Project: projectID,
    		Zone:    zone,
    		InstanceResource: &computepb.Instance{
    			Name: proto.String(instanceName),
    			Disks: []*computepb.AttachedDisk{
    				{
    					InitializeParams: &computepb.AttachedDiskInitializeParams{
    						DiskSizeGb:  proto.Int64(10),
    						SourceImage: newestDebian.SelfLink,
    						DiskType:    proto.String(fmt.Sprintf("zones/%s/diskTypes/pd-standard", zone)),
    					},
    					AutoDelete: proto.Bool(true),
    					Boot:       proto.Bool(true),
    					Type:       proto.String(computepb.AttachedDisk_PERSISTENT.String()),
    				},
    			},
    			MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
    			NetworkInterfaces: []*computepb.NetworkInterface{
    				{
    					AccessConfigs: []*computepb.AccessConfig{
    						{
    							Type:        proto.String(computepb.AccessConfig_ONE_TO_ONE_NAT.String()),
    							Name:        proto.String("External NAT"),
    							NetworkTier: proto.String(computepb.AccessConfig_PREMIUM.String()),
    							NatIP:       proto.String(ipAddress),
    						},
    					},
    				},
    			},
    		},
    	}
    
    	op, err := instancesClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Static address %s assigned to new VM", ipAddress)
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type;
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).NetworkTier;
    import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
    import com.google.cloud.compute.v1.[AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html);
    import com.google.cloud.compute.v1.[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import java.io.IOException;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class AssignStaticExternalNewVmAddress {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Instance ID of the Google Cloud project you want to use.
        String instanceId = "your-instance-id";
        // Name of the zone to create the instance in. For example: "us-west3-b"
        String zone = "your-zone-id";
        // machine type of the VM being created. This value uses the
        // following format: "zones/{zone}/machineTypes/{type_name}".
        // For example: "zones/europe-west3-c/machineTypes/f1-micro"
        String machineType = String.format("zones/%s/machineTypes/{your-machineType-id}", zone);
        // boolean flag indicating if the instance should have an external IPv4 address assigned.
        boolean externalAccess = true;
        // external IPv4 address to be assigned to this instance. If you specify
        // an external IP address, it must live in the same region as the zone of the instance.
        // This setting requires `external_access` to be set to True to work.
        String externalIpv4 = "your-externalIpv4-id";
    
        assignStaticExternalNewVmAddress(projectId, instanceId, zone,
                externalAccess, machineType, externalIpv4);
      }
    
      // Create a new VM instance with assigned static external IP address.
      public static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) assignStaticExternalNewVmAddress(String projectId, String instanceName,
                                                              String zone, boolean externalAccess,
                                                              String machineType, String externalIpv4)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        String sourceImage;
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
          sourceImage = imagesClient.[getFromFamily](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html#com_google_cloud_compute_v1_ImagesClient_getFromFamily_com_google_cloud_compute_v1_GetFromFamilyImageRequest_)("debian-cloud", "debian-13").getSelfLink();
        }
        [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attachedDisk = buildAttachedDisk(sourceImage, zone);
    
        return createInstance(projectId, instanceName, zone,
                attachedDisk, machineType, externalAccess, externalIpv4);
      }
    
      private static [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) buildAttachedDisk(String sourceImage, String zone) {
        [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html) initializeParams = [AttachedDiskInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskInitializeParams.html).newBuilder()
                .setSourceImage(sourceImage)
                .setDiskSizeGb(10)
                .setDiskType(String.format("zones/%s/diskTypes/pd-standard", zone))
                .build();
    
        return [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                .[setInitializeParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.Builder.html#com_google_cloud_compute_v1_AttachedDisk_Builder_setInitializeParams_com_google_cloud_compute_v1_AttachedDiskInitializeParams_)(initializeParams)
                // Remember to set auto_delete to True if you want the disk to be deleted
                // when you delete your VM instance.
                .setAutoDelete(true)
                .setBoot(true)
                .build();
      }
    
      // Send an instance creation request to the Compute Engine API and wait for it to complete.
      private static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) createInstance(String projectId, String instanceName,
                                             String zone, [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disks,
                                             String machineType, boolean externalAccess,
                                             String externalIpv4)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) client = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instanceResource =
                  buildInstanceResource(instanceName, disks, machineType, externalAccess, externalIpv4);
    
          [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) build = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRequestId(UUID.randomUUID().toString())
                  .setZone(zone)
                  .setInstanceResource(instanceResource)
                  .build();
          client.insertCallable().futureCall(build).get(60, TimeUnit.SECONDS);
    
          [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html) getInstanceRequest = [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html).newBuilder()
                  .setInstance(instanceName)
                  .setProject(projectId)
                  .setZone(zone)
                  .build();
    
          return client.get(getInstanceRequest);
        }
      }
    
      private static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) buildInstanceResource(String instanceName, [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) disk,
                                                    String machineType, boolean externalAccess,
                                                    String externalIpv4) {
        [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface =
                networkInterface(externalAccess, externalIpv4);
    
        return [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
                .setName(instanceName)
                .addDisks(disk)
                .setMachineType(machineType)
                .addNetworkInterfaces(networkInterface)
                .build();
      }
    
      private static [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface(boolean externalAccess, String externalIpv4) {
        [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).Builder build = [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder()
                .setNetwork("global/networks/default");
        if (externalAccess) {
          [AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Builder accessConfig = [AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).newBuilder()
                  .setType(Type.ONE_TO_ONE_NAT.name())
                  .setName("External NAT")
                  .setNetworkTier(NetworkTier.PREMIUM.name());
          if (externalIpv4 != null) {
            accessConfig.[setNatIP](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.Builder.html#com_google_cloud_compute_v1_AccessConfig_Builder_setNatIP_java_lang_String_)(externalIpv4);
          }
          build.[addAccessConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.Builder.html#com_google_cloud_compute_v1_NetworkInterface_Builder_addAccessConfigs_com_google_cloud_compute_v1_AccessConfig_)(accessConfig.build());
        }
    
        return build.build();
      }
    }

###  Python 
    
    
    from __future__ import annotations
    
    import re
    import sys
    from typing import Any
    import warnings
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
    def get_image_from_family(project: str, family: str) -> compute_v1.Image:
        """
        Retrieve the newest image that is part of a given family in a project.
    
        Args:
            project: project ID or project number of the Cloud project you want to get image from.
            family: name of the image family you want to get image from.
    
        Returns:
            An Image object.
        """
        image_client = compute_v1.ImagesClient()
        # List of public operating system (OS) images: https://cloud.google.com/compute/docs/images/os-details
        newest_image = image_client.get_from_family(project=project, family=family)
        return newest_image
    
    
    def disk_from_image(
        disk_type: str,
        disk_size_gb: int,
        boot: bool,
        source_image: str,
        auto_delete: bool = True,
    ) -> compute_v1.AttachedDisk:
        """
        Create an AttachedDisk object to be used in VM instance creation. Uses an image as the
        source for the new disk.
    
        Args:
             disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            boot: boolean flag indicating whether this disk should be used as a boot disk of an instance
            source_image: source image to use when creating this disk. You must have read access to this disk. This can be one
                of the publicly available images or an image from one of your projects.
                This value uses the following format: "projects/{project_name}/global/images/{image_name}"
            auto_delete: boolean flag indicating whether this disk should be deleted with the VM that uses it
    
        Returns:
            AttachedDisk object configured to be created using the specified image.
        """
        boot_disk = compute_v1.AttachedDisk()
        initialize_params = compute_v1.AttachedDiskInitializeParams()
        initialize_params.source_image = source_image
        initialize_params.disk_size_gb = disk_size_gb
        initialize_params.disk_type = disk_type
        boot_disk.initialize_params = initialize_params
        # Remember to set auto_delete to True if you want the disk to be deleted when you delete
        # your VM instance.
        boot_disk.auto_delete = auto_delete
        boot_disk.boot = boot
        return boot_disk
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_instance(
        project_id: str,
        zone: str,
        instance_name: str,
        disks: list[compute_v1.AttachedDisk],
        machine_type: str = "n1-standard-1",
        network_link: str = "global/networks/default",
        subnetwork_link: str = None,
        internal_ip: str = None,
        external_access: bool = False,
        external_ipv4: str = None,
        accelerators: list[compute_v1.AcceleratorConfig] = None,
        preemptible: bool = False,
        spot: bool = False,
        instance_termination_action: str = "STOP",
        custom_hostname: str = None,
        delete_protection: bool = False,
    ) -> compute_v1.Instance:
        """
        Send an instance creation request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            disks: a list of compute_v1.AttachedDisk objects describing the disks
                you want to attach to your new instance.
            machine_type: machine type of the VM being created. This value uses the
                following format: "zones/{zone}/machineTypes/{type_name}".
                For example: "zones/europe-west3-c/machineTypes/f1-micro"
            network_link: name of the network you want the new instance to use.
                For example: "global/networks/default" represents the network
                named "default", which is created automatically for each project.
            subnetwork_link: name of the subnetwork you want the new instance to use.
                This value uses the following format:
                "regions/{region}/subnetworks/{subnetwork_name}"
            internal_ip: internal IP address you want to assign to the new instance.
                By default, a free address from the pool of available internal IP addresses of
                used subnet will be used.
            external_access: boolean flag indicating if the instance should have an external IPv4
                address assigned.
            external_ipv4: external IPv4 address to be assigned to this instance. If you specify
                an external IP address, it must live in the same region as the zone of the instance.
                This setting requires `external_access` to be set to True to work.
            accelerators: a list of AcceleratorConfig objects describing the accelerators that will
                be attached to the new instance.
            preemptible: boolean value indicating if the new instance should be preemptible
                or not. Preemptible VMs have been deprecated and you should now use Spot VMs.
            spot: boolean value indicating if the new instance should be a Spot VM or not.
            instance_termination_action: What action should be taken once a Spot VM is terminated.
                Possible values: "STOP", "DELETE"
            custom_hostname: Custom hostname of the new VM instance.
                Custom hostnames must conform to RFC 1035 requirements for valid hostnames.
            delete_protection: boolean value indicating if the new virtual machine should be
                protected against deletion or not.
        Returns:
            Instance object.
        """
        instance_client = compute_v1.InstancesClient()
    
        # Use the network interface provided in the network_link argument.
        network_interface = compute_v1.NetworkInterface()
        network_interface.network = network_link
        if subnetwork_link:
            network_interface.subnetwork = subnetwork_link
    
        if internal_ip:
            network_interface.network_i_p = internal_ip
    
        if external_access:
            access = compute_v1.AccessConfig()
            access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
            access.name = "External NAT"
            access.network_tier = access.NetworkTier.PREMIUM.name
            if external_ipv4:
                access.nat_i_p = external_ipv4
            network_interface.access_configs = [access]
    
        # Collect information into the Instance object.
        instance = compute_v1.Instance()
        instance.network_interfaces = [network_interface]
        instance.name = instance_name
        instance.disks = disks
        if re.match(r"^zones/[a-z\d\-]+/machineTypes/[a-z\d\-]+$", machine_type):
            instance.machine_type = machine_type
        else:
            instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
    
        instance.scheduling = compute_v1.Scheduling()
        if accelerators:
            instance.guest_accelerators = accelerators
            instance.scheduling.on_host_maintenance = (
                compute_v1.Scheduling.OnHostMaintenance.TERMINATE.name
            )
    
        if preemptible:
            # Set the preemptible setting
            warnings.warn(
                "Preemptible VMs are being replaced by Spot VMs.", DeprecationWarning
            )
            instance.scheduling = compute_v1.Scheduling()
            instance.scheduling.preemptible = True
    
        if spot:
            # Set the Spot VM setting
            instance.scheduling.provisioning_model = (
                compute_v1.Scheduling.ProvisioningModel.SPOT.name
            )
            instance.scheduling.instance_termination_action = instance_termination_action
    
        if custom_hostname is not None:
            # Set the custom hostname for the instance
            instance.hostname = custom_hostname
    
        if delete_protection:
            # Set the delete protection bit
            instance.deletion_protection = True
    
        # Prepare the request to insert an instance.
        request = compute_v1.InsertInstanceRequest()
        request.zone = zone
        request.project = project_id
        request.instance_resource = instance
    
        # Wait for the create operation to complete.
        print(f"Creating the {instance_name} instance in {zone}...")
    
        operation = instance_client.insert(request=request)
    
        wait_for_extended_operation(operation, "instance creation")
    
        print(f"Instance {instance_name} created.")
        return instance_client.get(project=project_id, zone=zone, instance=instance_name)
    
    
    def assign_static_external_ip_to_new_vm(
        project_id: str, zone: str, instance_name: str, ip_address: str
    ) -> compute_v1.Instance:
        """
        Create a new VM instance with assigned static external IP address.
    
        Args:
            project_id (str): project ID or project number of the Cloud project you want to use.
            zone (str): name of the zone to create the instance in. For example: "us-west3-b"
            instance_name (str): name of the new virtual machine (VM) instance.
            ip_address(str): external address to be assigned to this instance. It must live in the same
            region as the zone of the instance and be precreated before function called.
    
        Returns:
            Instance object.
        """
        newest_debian = get_image_from_family(project="debian-cloud", family="debian-12")
        disk_type = f"zones/{zone}/diskTypes/pd-standard"
        disks = [disk_from_image(disk_type, 10, True, newest_debian.self_link, True)]
        instance = create_instance(
            project_id,
            zone,
            instance_name,
            disks,
            external_ipv4=ip_address,
            external_access=True,
        )
        return instance
    
    

### Change or assign an external IP address to an existing instance

You can change or assign an external IP address, either ephemeral or static, to an existing IPv4-only or dual-stack instance. This procedure is not supported for IPv6-only instances.

A compute instance can have multiple interfaces. A single-stack interface can have one external IP address. A dual-stack interface can have one external IPv4 address and one external IPv6 address. If the instance already has an external IP address, you must remove that address first. Then you can assign a new external IP address to the existing instance.

**Note:** If you need to update the IP address of a forwarding rule, see [Change the IP address of a forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#update-forwarding-rule).

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance that you want to assign an external IP to. The **Instance details** page displays.

  3. From the **Instance details** page, complete the following steps:

     1. Click **Edit**.
     2. Expand **Network interfaces**.
     3. Select the required external IP address to assign to the instance. If the instance is IPv4-only and you want to assign an IPv6 address, you must first change the stack type to dual-stack. 
        1. For **External IPv4 address** , select either **Ephemeral** or a static external IPv4 address.
        2. For **External IPv6 address** , select either **Ephemeral (Automatic)** , **Ephemeral (Custom)** , or a static external IPv6 address.
     4. Click **Done**.
  4. Click **Save**.




###  gcloud 

  1. Optional: Reserve a static external IP address.

If you want to assign a static external IP address, you must reserve an address and make sure that the address is not in use by another resource. If necessary, follow the instructions to [reserve a new static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) or to unassign a static external IP address.

If you intend to use an ephemeral external IP address, you can skip this step, and Compute Engine randomly assigns an ephemeral external IP address.

  2. Remove any existing IP address assignment, as described in Unassign a static external IP address.

  3. Assign the new external IP address.

     * To assign an IPv4 address, use the [`instances add-access-config` sub-command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-access-config):

**Note:** Don't replace `IP_ADDRESS` with the name of the static IP address. You must use the actual IP address.
           
           gcloud compute instances add-access-config INSTANCE_NAME \
             --access-config-name="ACCESS_CONFIG_NAME" --address=IP_ADDRESS
           

Replace the following:

       * `INSTANCE_NAME`: the name of the instance.
       * `ACCESS_CONFIG_NAME`: the name to call this access config. Make sure to include the full name between quotes.
       * `IP_ADDRESS`: the IP address to add.

If you want Compute Engine to assign an ephemeral external IP address rather than using a static external IP address, omit the `--address IP_ADDRESS` property:
    
    gcloud compute instances add-access-config INSTANCE_NAME \
      --access-config-name="ACCESS_CONFIG_NAME"
    

     * To change an instance to dual-stack and assign it an IPv6 address, use the [`instance network-interfaces update` sub-command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update):
           
           gcloud compute instances network-interfaces update INSTANCE_NAME \
             --network-interface=NIC \
             --ipv6-network-tier=PREMIUM \
             --stack-type=STACK_TYPE \
             --external-ipv6-address=IPV6_ADDRESS \
             --external-ipv6-prefix-length=96 \
             --zone=ZONE
           

Replace the following:

       * `INSTANCE_NAME`: the name of the instance.
       * `NIC`: the name of the network interface.
       * `STACK_TYPE`: the stack type for the instance, which must be `IPV4_IPV6`. You can't change the stack type to IPV6_ONLY.
       * `IPV6_ADDRESS`: the IPv6 address to assign to the instance. Specify the first IPv6 address in the `/96` range.
       * `ZONE`: the zone of the instance.



###  REST 

You can change the external IPv4 or IPv6 address of an instance by adding a new access configuration for that instance.

  1. Remove any existing IP address assignment, as described in Unassign a static external IP address.

  2. Delete the existing access configuration by making a `POST` request to the [`instances.deleteAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/deleteAccessConfig).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/deleteAccessConfig
         

  3. Add a new access configuration to the network interface of the instance by making a `POST` request to the [`instances.addAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/addAccessConfig).

     * For IPv4 addresses, make the following request:
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/addAccessConfig
           {
           "natIP": "IPV4_ADDRESS",
           "name": "ACCESS_CONFIG_NAME"
           }
           

     * For IPv6 addresses, update the `stackType` of the network interface to `IPV4_IPV6` and update the [`networkInterfaces[].ipv6AccessConfigs[].externalIpv6`](https://docs.cloud.google.com/compute/docs/reference/latest/instances#networkInterfaces.accessConfigs.natIP) property and the external IPv6 address that you want to use.

For more information, see [Assign a static external IP address to a new instance](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#api_1).




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/protobuf/proto"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // assignStaticAddressToExistingVM assigns a static external IP address to an existing VM instance.
    // Note: VM and assigned IP must be in the same region.
    func assignStaticAddressToExistingVM(w io.Writer, projectID, zone, instanceName, IPAddress, networkInterfaceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// IPAddress := "34.111.222.333"
    	// networkInterfaceName := "nic0"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	reqGet := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, reqGet)
    	if err != nil {
    		return fmt.Errorf("could not get instance: %w", err)
    	}
    
    	var networkInterface *computepb.NetworkInterface
    	for _, ni := range instance.NetworkInterfaces {
    		if *ni.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name) == networkInterfaceName {
    			networkInterface = ni
    			break
    		}
    	}
    
    	if networkInterface == nil {
    		return fmt.Errorf("No network interface named '%s' found on instance %s", networkInterfaceName, instanceName)
    	}
    
    	var accessConfig *computepb.AccessConfig
    	for _, ac := range networkInterface.AccessConfigs {
    		if *ac.Type == computepb.[AccessConfig_ONE_TO_ONE_NAT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_TYPE_AccessConfig_DIRECT_IPV6_AccessConfig_ONE_TO_ONE_NAT).String() {
    			accessConfig = ac
    			break
    		}
    	}
    
    	if accessConfig != nil {
    		// network interface is immutable - deletion stage is required in case of any assigned ip (static or ephemeral).
    		reqDelete := &computepb.DeleteAccessConfigInstanceRequest{
    			Project:          projectID,
    			Zone:             zone,
    			Instance:         instanceName,
    			AccessConfig:     *accessConfig.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Name),
    			NetworkInterface: networkInterfaceName,
    		}
    
    		opDelete, err := instancesClient.DeleteAccessConfig(ctx, reqDelete)
    		if err != nil {
    			return fmt.Errorf("unable to delete access config: %w", err)
    		}
    
    		if err = opDelete.Wait(ctx); err != nil {
    			return fmt.Errorf("unable to wait for the operation: %w", err)
    		}
    	}
    
    	reqAdd := &computepb.AddAccessConfigInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    		AccessConfigResource: &computepb.AccessConfig{
    			NatIP: &IPAddress,
    			Type:  proto.String(computepb.[AccessConfig_ONE_TO_ONE_NAT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_TYPE_AccessConfig_DIRECT_IPV6_AccessConfig_ONE_TO_ONE_NAT).String()),
    		},
    		NetworkInterface: networkInterfaceName,
    	}
    
    	opAdd, err := instancesClient.AddAccessConfig(ctx, reqAdd)
    	if err != nil {
    		return fmt.Errorf("unable to add access config: %w", err)
    	}
    
    	if err = opAdd.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Static address %s assigned to the instance %s\n", IPAddress, instanceName)
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type;
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class AssignStaticExistingVm {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Instance ID of the Google Cloud project you want to use.
        String instanceId = "your-instance-id";
        // Name of the zone to create the instance in. For example: "us-west3-b"
        String zone = "your-zone-id";
        // Name of the network interface to assign.
        String netInterfaceName = "your-netInterfaceName-id";
    
        assignStaticExistingVmAddress(projectId, instanceId, zone, netInterfaceName);
      }
    
      // Updates or creates an access configuration for a VM instance to assign a static external IP.
      // As network interface is immutable - deletion stage is required
      // in case of any assigned ip (static or ephemeral).
      // VM and ip address must be created before calling this function.
      // IMPORTANT: VM and assigned IP must be in the same region.
      public static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) assignStaticExistingVmAddress(String projectId, String instanceId,
                                                           String zone, String netInterfaceName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) client = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = client.get(projectId, zone, instanceId);
    
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = null;
          for ([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) netInterface : instance.[getNetworkInterfacesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getNetworkInterfacesList__)()) {
            if (netInterface.getName().equals(netInterfaceName)) {
              networkInterface = netInterface;
              break;
            }
          }
    
          if (networkInterface == null) {
            throw new IllegalArgumentException(
                    String.format(
                            "No '{network_interface_name}' variable found on instance %s.",
                            instanceId)
            );
          }
          [AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) accessConfig = null;
          for ([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) config : networkInterface.[getAccessConfigsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html#com_google_cloud_compute_v1_NetworkInterface_getAccessConfigsList__)()) {
            if (config.getType().equals(Type.ONE_TO_ONE_NAT.name())) {
              accessConfig = config;
              break;
            }
          }
    
          if (accessConfig != null) {
            // Delete the existing access configuration first
            client.[deleteAccessConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_deleteAccessConfigAsync_com_google_cloud_compute_v1_DeleteAccessConfigInstanceRequest_)(projectId, zone, instanceId,
                            accessConfig.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html#com_google_cloud_compute_v1_AccessConfig_getName__)(), netInterfaceName)
                    .get(30, TimeUnit.SECONDS);
          }
    
          // Add a new access configuration with the new IP
          [AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) newAccessConfig = [AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).newBuilder()
                  // Leave this field undefined to use an IP from a shared ephemeral IP address pool
                  // .setNatIP(ipAddress)
                  .setType(Type.ONE_TO_ONE_NAT.name())
                  .setName("external-nat")
                  .build();
    
          client.[addAccessConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_addAccessConfigAsync_com_google_cloud_compute_v1_AddAccessConfigInstanceRequest_)(projectId, zone, instanceId, netInterfaceName, newAccessConfig)
                  .get(30, TimeUnit.SECONDS);
    
          // return updated instance
          return client.get(projectId, zone, instanceId);
        }
      }
    }

###  Python 
    
    
    import uuid
    
    from google.cloud.compute_v1 import [InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)
    from google.cloud.compute_v1.types import [AccessConfig](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AccessConfig.html)
    from google.cloud.compute_v1.types import [AddAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AddAccessConfigInstanceRequest.html)
    from google.cloud.compute_v1.types import [DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteAccessConfigInstanceRequest.html)
    
    
    def assign_static_ip_to_existing_vm(
        project_id: str,
        zone: str,
        instance_name: str,
        ip_address: str,
        network_interface_name: str = "nic0",
    ):
        """
        Updates or creates an access configuration for a VM instance to assign a static external IP.
        As network interface is immutable - deletion stage is required in case of any assigned ip (static or ephemeral).
        VM and ip address must be created before calling this function.
        IMPORTANT: VM and assigned IP must be in the same region.
    
        Args:
            project_id (str): Project ID.
            zone (str): Zone where the VM is located.
            instance_name (str): Name of the VM instance.
            ip_address (str): New static external IP address to assign to the VM.
            network_interface_name (str): Name of the network interface to assign.
    
        Returns:
            google.cloud.compute_v1.types.Instance: Updated instance object.
        """
        client = InstancesClient()
        instance = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
        network_interface = next(
            (ni for ni in instance.network_interfaces if ni.name == network_interface_name),
            None,
        )
    
        if network_interface is None:
            raise ValueError(
                f"No network interface named '{network_interface_name}' found on instance {instance_name}."
            )
    
        access_config = next(
            (ac for ac in network_interface.access_configs if ac.type_ == "ONE_TO_ONE_NAT"),
            None,
        )
    
        if access_config:
            # Delete the existing access configuration first
            delete_request = DeleteAccessConfigInstanceRequest(
                project=project_id,
                zone=zone,
                instance=instance_name,
                access_config=access_config.name,
                network_interface=network_interface_name,
                request_id=str(uuid.uuid4()),
            )
            delete_operation = client.[delete_access_config](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_delete_access_config)(delete_request)
            delete_operation.result()
    
        # Add a new access configuration with the new IP
        add_request = AddAccessConfigInstanceRequest(
            project=project_id,
            zone=zone,
            instance=instance_name,
            network_interface="nic0",
            access_config_resource=AccessConfig(
                nat_i_p=ip_address, type_="ONE_TO_ONE_NAT", name="external-nat"
            ),
            request_id=str(uuid.uuid4()),
        )
        add_operation = client.[add_access_config](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_add_access_config)(add_request)
        add_operation.result()
    
        updated_instance = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
        return updated_instance
    
    

## Restrict external IP addresses to specific instances

For certain workloads, you might have essential requirements that include security and network restrictions. For example, you might want to restrict external IP addresses so that only specific Compute Engine instances can use them. This option can help to prevent data exfiltration or maintain network isolation.

Using an [Organization Policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview), you can restrict external IP addresses to specific instances with constraints to control use of external IP addresses for your instances within an organization or a project.

**Caution:** Restricting external IPs to specific instances can prevent existing GKE clusters and managed instance groups (MIGs) from adding new instances. If a GKE cluster or a MIG is configured to create instances that have external IP addresses, autohealing and autoscaling actions fail.

The constraint for controlling external IP address on instances is:
    
    
    constraints/compute.vmExternalIpAccess
    

If you don't specify a organization policy for external IP addresses, then external IP addresses are allowed for all instances. To use the constraint, you specify an organization policy with one of the following configurations:

  * Specify an empty `allowedValues` list, so that all compute instances are blocked from having any external IP address.
  * Specify an `allowedValues` list of compute instances that can have external IP addresses. 
    * Only the compute instances that are listed in the `allowedValues` list can be assigned an external IP address, either ephemeral or static.
    * All other compute instances in the organization or project that are not explicitly defined in the policy are prohibited from having external IP addresses.
  * Alternatively, specify the `deniedValues` list to prevent only designated compute instances from having external IP addresses. Use this approach with caution, especially if the organization policy constraint applies to a project where it overrides a constraint applied at a parent folder or organization. Because _only_ the compute instances specified in a `deniedValues` list are prevented from having external IP addresses, any newly created compute instances in the project can have external IP addresses.



Instances are identified in the allow and deny lists using the instance's URI:
    
    
    projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

### Specifications for restricting external IP addresses

  * You can apply the `compute.vmExternalIpAccess` [list constraint](https://docs.cloud.google.com/organization-policy/overview#constraints) only to compute instances.
  * You cannot apply the constraint retroactively. All compute instances that have external IP addresses before you enable the policy retain their external IP addresses.
  * This constraint accepts either an `allowedValues` or a `deniedValues` list, but not both in the same policy.
  * It is up to you or an administrator with the required permissions to manage and maintain the compute instance lifecycle and integrity. The constraint only verifies the instance's URI, and it does not prevent the instances in the allowlist from being altered, deleted, or recreated.



### Guidelines for restricting external IP addresses

Use the following guidelines to permit or deny external IP addresses for compute instances:

  * If your security goal is to allow the creation of only some compute instances with external IP addresses, but prevent the creation of other instances with external IP addresses, keep the following in mind when using an `allowedValues` list or `deniedValues` list in a `constraints/compute.vmExternalIpAccess` organization policy constraint:

    * Verify that the `constraints/compute.vmExternalIpAccess` organization policy constraint is not overridden by a `constraints/compute.vmExternalIpAccess` organization policy constraint [defined on a child resource](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).

    * **Recommended** : Use an `allowedValues` list in a `constraints/compute.vmExternalIpAccess` organization policy constraint to specify _only_ the compute instances that are allowed to have external IP addresses. Any newly created instances in the project are automatically excluded from having external IP addresses because they aren't listed in the `allowedValues` list in the organization policy constraint. For an example, see Set the policy at the project level.

  * You can exempt specific projects in a resource hierarchy from the `constraints/compute.vmExternalIpAccess` organization policy constraint by using the `setOrgPolicy` method and specifying [`restoreDefault`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy#RestoreDefault).

  * When using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), applying the `constraints/compute.vmExternalIpAccess` organization policy constraint to the Shared VPC host project only applies to compute instances actually located in the host project itself. Instances located in service projects are not affected unless you apply the `constraints/compute.vmExternalIpAccess` organization policy constraint to each service project.

  * Use the organization policy together with IAM roles to better control your environment. This policy applies to only compute instances. To better control and restrict external IP addresses on network devices, you can grant the `compute.networkAdmin` role to only the appropriate parties.




### Using an external IP address organization policy with managed services

The `constraints/compute.vmExternalIpAccess` organization policy constraint applies to newly created compute instances located in a project that is in scope for the organization policy constraint. Affected instances include Google Kubernetes Engine nodes, Dataflow instances, and Managed Service for Apache Spark instances _if they are created in your project and if your project is in scope for this organization policy constraint_.

Instance-based [managed services that use private services access](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services) are powered by compute instances located in service producer projects that are separate from your project. Compute instances for managed services have network interfaces in a service producer network that peers with your VPC network. If the `constraints/compute.vmExternalIpAccess` organization policy constraint applies to your project (the project that contains your VPC network), then the organization policy constraint doesn't have any effect on the compute instances for managed services outside of your project.

Some managed services offer their own organization policy constraints that offer similar capabilities; for example, Cloud SQL has `constraints/sql.restrictPublicIp`.

### Permissions needed for restricting external IP addresses

To set a constraint on either the project or the organization level, you must have been granted the `orgpolicy.policyAdmin` role on the organization.

### Set the policy constraint at the organization level

**Note:** The length of each string used for each instance URI cannot exceed 200 characters.

###  Console 

  1. Go to the **Organizational Policies** page. 

[Go to Organizational Policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. If necessary, select the required organization from the project drop-down menu.
  3. In the **Filter** menu, enter the text `Define allowed`.

You should see two rows displayed in the **Policies** table.

  4. Select the **Define allowed external IPs for VM instances** policy by clicking the policy name in the **Name** column of the table.

  5. On the policy details page, click **Manage policy** to edit the external IP policy. If you can't access the **Manage policy** link, you don't have the correct permissions. 

  6. Click **Manage policy**.

The **Edit policy** page opens.

  7. For **Applies to** , select **Override parent's policy**.

  8. For **Policy enforcement** , choose **Merge with parent**.

  9. Click **Add a rule**.

     1. For **Policy values** , select **Custom**.

     2. For **Policy type** , select whether the given values should be accepted or denied by the organization policy.

     3. In the **Custom value** field, enter a URI for an instance. The URI must be in the following format:
            
            projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
            

     4. To add more compute instances, click **Add value** and then enter URIs for additional instances.

  10. To enforce the policy, click **Set policy**.




###  gcloud 

To set a constraint for external IP access, you first need your organization ID. You can find the organization ID by running the [`organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list) and looking for the numeric ID in the response:
    
    
    gcloud organizations list
    

The gcloud CLI returns a list of organizations in the following format:
    
    
    DISPLAY_NAME               ID
    example-organization1      29252605212
    example-organization2      1234567890
    

Use the [`gcloud resource-manager org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy) to set the policy. You need to provide your policy as a JSON file. Create a JSON file in the following format:
    
    
    {
    "constraint": "constraints/compute.vmExternalIpAccess",
    "listPolicy": {
      "allowedValues": [
         "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME",
         "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME",
         "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
      ]
     }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request, such as `example-project`. Note that this is different than setting up organization policies, which require the organization numeric ID.
  * `ZONE`: the zone of the instance
  * `INSTANCE_NAME`: the name of the instance



Alternatively, you can specify a `deniedValues` list to indicate instances that you explicitly want to prohibit from having an external IP address. Any instance not on the list would implicitly be allowed to have an external IP address. You can only specify either `allowedValues` or `deniedValues` but not both.

Then, pass in the file with your request:
    
    
    gcloud resource-manager org-policies set-policy MY_POLICY.JSON --organization=ORGANIZATION_ID
    

Replace `ORGANIZATION_ID` with the numeric ID of the organization.

If you don't want any instances to have external IP access, you can set a policy with `allValues` set to `DENY`:
    
    
    {
      "constraint": "constraints/compute.vmExternalIpAccess",
      "listPolicy": {
        "allValues": "DENY"
      }
    }
    

###  REST 

Use the [`setOrgPolicy()` API](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy) to define your constraint. The instances in the `allowedValues` list that you specify are allowed to have external IP addresses. Alternatively, you can specify a `deniedValues` list to express instances that you explicitly want to prohibit from having an external IP address. Any instance not on the list would implicitly be allowed to have an external IP address. You can only specify either `allowedValues` or `deniedValues` but not both.

For example, the following is a request to apply the `compute.vmExternalIpAccess` constraint to an organization where instances from certain projects within the organization are allowed to have external IP addresses:
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/organizations/ORGANIZATION_ID:setOrgPolicy
    

where `ORGANIZATION_ID` is the numeric ID of the organization.

Now, in your request body, provide the policy for this constraint:
    
    
    {
      "policy": {
        "constraint": "constraints/compute.vmExternalIpAccess",
        "listPolicy": {
          "allowedValues": [
            "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME",
            "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME",
            "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
            ]
          }
        }
     }

If you don't want any instances to have external IP access, you can set a policy with `allValues` set to `DENY`:
    
    
    {
      "policy": {
        "constraint": "constraints/compute.vmExternalIpAccess",
        "listPolicy": {
          "allValues": "DENY"
          }
        }
     }

### Set the policy at the project level

Setting a policy at the project level overrides the policy at the organization level. For example, if the organization level has `example-vm-1` on the `allowedValues` list but the policy at the project level has the same instance on the `deniedValues` list, the instance wouldn't be allowed to have an external IP address.

###  Console 

Follow the same process documented in Set a policy constraint at the organization level but choose your project from the project selector instead of the organization.

![Project selector.](https://docs.cloud.google.com/static/compute/images/project-selector.png)

###  gcloud 

Use the [`gcloud resource-manager org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy) to set the policy. You need to provide your policy as a JSON file. Create a JSON file in the following format:
    
    
    {
     "constraint": "constraints/compute.vmExternalIpAccess",
     "listPolicy": {
      "allowedValues": [
       "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
      ]
     }
    }

Replace the following:

  * `PROJECT_ID`: the project ID for this request, such as `example-project`. Note that this is different than setting up organization policies, which require the organization numeric ID.
  * `ZONE`: the zone of the instance.
  * `INSTANCE_NAME`: the name of the instance.



Alternatively, you can specify a `deniedValues` list of instances that you explicitly want to prohibit from having an external IP address. Any instance not on the list would implicitly be allowed to have an external IP address. You can only specify either `allowedValues` or `deniedValues` but not both.

Then, pass in the file with your request:
    
    
    gcloud resource-manager org-policies set-policy MY_POLICY.JSON --project=example-project
    

###  REST 

Use the [`setOrgPolicy` API](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy) to define your constraint. The instances in the `allowedValues` list that you specify are allowed to have external IP addresses. Alternatively, you can specify a `deniedValues` list to express instances that you explicitly want to prohibit from having an external IP address. Any instance not on the list is implicitly allowed to have an external IP address. You can specify only `allowedValues` or `deniedValues` but not both.

For example, the following is a request to set the `compute.vmExternalIpAccess` constraint on a project to allow specific instances to have external IP addresses:
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setOrgPolicy
    

Replace `PROJECT_ID` with the project ID for this request.

The request body contains the policy for this constraint:
    
    
    {
      "policy": {
        "constraint": "constraints/compute.vmExternalIpAccess",
        "listPolicy": {
          "allowedValues": [
            "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
          ]
        }
      }
    }
    

## Manage static external IP addresses

The following sections describe how to manage static external IP addresses for your instances.

### Determine if an external IP address is ephemeral or static

Static and ephemeral external IP addresses behave and appear the same in most contexts. However, with static external IP addresses, you can use the same IP address for the same resource even if you delete and re-create the resource. 

In general, an ephemeral IP address is released if you stop or delete the resource.

To determine if an address is static or ephemeral, do the following:

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Find the address in the list and check the **Type** column for the type of IP address.




### Unassign a static external IP address

Unassigning an IP address removes it from the resource but keeps the IP address reserved. After the IP address is unassigned, you can reassign the IP address to another resource. This procedure is supported for dual-stack instances, but not IPv6-only instances.

**Note:** You are charged at a higher rate for unassigned static external IP addresses than you are for static and ephemeral external IP addresses that are in use. For more information, see [External IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).

You can also unassign the IPv4 or IPv6 address by [deleting the instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **External IP addresses**.

  3. Select the static IP address that you want to unassign.

  4. Click more_vert**View actions** and select the **Reassign to another resource** option.

  5. From the **Attach to** drop-down list, select **None**.

  6. Click **OK**.




###  gcloud 

  1. Check if a static IP address is in use by using the [`gcloud compute addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list):
         
         gcloud compute addresses list
         

The output is similar to the following:
         
         NAME                      REGION    ADDRESS                  STATUS
         example-address-ipv4      REGION    198.51.100.1             RESERVED
         example-address-new-ipv4  REGION    203.0.113.1              IN_USE
         example-address-ipv6      REGION    2001:db8:1:1:1:1:1:1     RESERVED
         example-address-new-ipv6  REGION    2001:db8:4:4:4:4:4:4     IN_USE
         

     * If the IP address is not in use, the status is `RESERVED`.
     * If the IP address is in use, the status is `IN_USE`.
  2. Retrieve the name of the instance that is using the IP address:
         
         gcloud compute addresses describe ADDRESS_NAME \
           --region=REGION
         

Replace the following:

     * `ADDRESS_NAME`: the name of the IPv6 address resource.
     * `REGION`: the region of the IPv6 address resource.

The output is similar to the following:
    
    address: IP_ADDRESS
    addressType: EXTERNAL
    ...
    region: https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/addresses/ADDRESS_NAME
    status: IN_USE
    subnetwork: https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/subnetworks/SUBNET
    **users** :
    - https://www.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances/INSTANCE_NAME
    

The `users` field displays the name of the instance that is using the IP address.

  3. Unassign the IP address from the instance.

     * To unassign an IPv4 address, delete the instance's access config file:

       1. Get the name of the access config to delete. To get the name, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe). Replace `INSTANCE_NAME` with the name of the instance.
              
              gcloud compute instances describe INSTANCE_NAME
              

The access config appears in the following format:
              
              networkInterfaces:
                - accessConfigs:
                  - kind: compute#accessConfig
                    name: external-nat
                    natIP: 203.0.113.1
                    type: ONE_TO_ONE_NAT
              

**Note:** The `name` of your access config might be different than `external-nat`; make sure to check for your own access config name. In some cases, an earlier version of the access config name, `External NAT`, might be used.
       2. Delete the access config by using the [`gcloud compute instances delete-access-config` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete-access-config):
              
              gcloud compute instances delete-access-config INSTANCE_NAME \
                --access-config-name="ACCESS_CONFIG_NAME"
              

Replace the following:

          * `INSTANCE_NAME`: the name of the instance.
          * `ACCESS_CONFIG_NAME`: the name of the access config to delete. Be sure to include the full name between quotes.
     * To unassign an IPv6 address range, use the [`instance network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update):
           
           gcloud compute instances network-interfaces update INSTANCE_NAME \
             --network-interface=nic0 \
             --stack-type=IPV4_ONLY \
             --zone=ZONE
           

Replace the following:

       * `INSTANCE_NAME`: the name of the instance that is using the IP address.
       * `ZONE`: the zone of the instance.
  4. Check that your static external IP address is now available and marked as `RESERVED` instead of `IN_USE`.
         
         gcloud compute addresses list \
           --filter="ADDRESS_NAME AND region=REGION"
         

Replace the following:

     * `ADDRESS_NAME`: the name of the IP address resource.
     * `REGION`: the region of the IP address resource.



Now that your static external IP address is available, you can choose to assign it to another instance.

###  REST 

To unassign a static external IPv4 or IPv6 address, perform the following steps:

  * For IPv4 addresses, delete the access configuration attached to the instance that's using the address.

    1. To check the access configuration details of an instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
           

    2. Delete the existing access configuration by making a `POST` request to the [`instances.deleteAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/deleteAccessConfig).
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/deleteAccessConfig
           

Replace the following:

       * `PROJECT_ID`: the project ID for this request
       * `ZONE`: the zone where the instance is located
       * `INSTANCE_NAME`: the name of the instance
  * For IPv6 addresses, update the stack type of the network interface for the instance where the IPv6 address is attached.

    1. Make a `PATCH` request to the [`instances.updateNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateNetworkInterface).

    2. In the request body, update the value of the `stackType` field to `IPV4_ONLY`.

For example:
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateNetworkInterface
           
           {
             "networkInterfaces": [{
               ...
               "stackType" : "IPV4_ONLY"
               ...
               }]
           }
           




###  Java 
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type;
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UnassignStaticIpAddress {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Instance ID of the Google Cloud project you want to use.
        String instanceId = "your-instance-id";
        // Name of the zone to create the instance in. For example: "us-west3-b"
        String zone = "your-zone";
        // Name of the network interface to assign.
        String netInterfaceName = "your-netInterfaceName";
    
        unassignStaticIpAddress(projectId, instanceId, zone, netInterfaceName);
      }
    
      public static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) unassignStaticIpAddress(String projectId, String instanceId,
                                                     String zone, String netInterfaceName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) client = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = client.get(projectId, zone, instanceId);
          [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface = null;
          for ([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) netIterface : instance.[getNetworkInterfacesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getNetworkInterfacesList__)()) {
            if (netIterface.getName().equals(netInterfaceName)) {
              networkInterface = netIterface;
              break;
            }
          }
    
          if (networkInterface == null) {
            throw new IllegalArgumentException(
                    String.format(
                            "No '{network_interface_name}' variable found on instance %s.",
                            instanceId)
            );
          }
    
          [AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) accessConfig = null;
          for ([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) config : networkInterface.[getAccessConfigsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html#com_google_cloud_compute_v1_NetworkInterface_getAccessConfigsList__)()) {
            if (config.getType().equals(Type.ONE_TO_ONE_NAT.name())) {
              accessConfig = config;
              break;
            }
          }
    
          if (accessConfig != null) {
            // Delete the existing access configuration first
            client.[deleteAccessConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_deleteAccessConfigAsync_com_google_cloud_compute_v1_DeleteAccessConfigInstanceRequest_)(projectId, zone, instanceId,
                            accessConfig.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html#com_google_cloud_compute_v1_AccessConfig_getName__)(), netInterfaceName).get(30, TimeUnit.SECONDS);
          }
    
          // return updated instance
          return client.get(projectId, zone, instanceId);
        }
      }
    }

###  Python 
    
    
    import uuid
    
    from google.cloud.compute_v1 import [InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)
    from google.cloud.compute_v1.types import [DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeleteAccessConfigInstanceRequest.html)
    
    
    def unassign_static_ip_from_existing_vm(
        project_id: str,
        zone: str,
        instance_name: str,
        network_interface_name: str = "nic0",
    ):
        """
        Updates access configuration for a VM instance to unassign a static external IP.
        VM (and IP address in case of static IP assigned) must be created before calling this function.
    
        Args:
            project_id (str): Project ID.
            zone (str): Zone where the VM is located.
            instance_name (str): Name of the VM instance.
            network_interface_name (str): Name of the network interface to unassign.
        """
        client = InstancesClient()
        instance = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
        network_interface = next(
            (ni for ni in instance.network_interfaces if ni.name == network_interface_name),
            None,
        )
    
        if network_interface is None:
            raise ValueError(
                f"No network interface named '{network_interface_name}' found on instance {instance_name}."
            )
    
        access_config = next(
            (ac for ac in network_interface.access_configs if ac.type_ == "ONE_TO_ONE_NAT"),
            None,
        )
    
        if access_config:
            # Delete the existing access configuration
            delete_request = DeleteAccessConfigInstanceRequest(
                project=project_id,
                zone=zone,
                instance=instance_name,
                access_config=access_config.name,
                network_interface=network_interface_name,
                request_id=str(uuid.uuid4()),
            )
            delete_operation = client.[delete_access_config](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_delete_access_config)(delete_request)
            delete_operation.result()
    
        updated_instance = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
        return updated_instance
    
    

### Release a static external IP address

If you no longer need a static external IPv4 or IPv6 address, you can release the IP address by deleting the IP address resource. Deleting an instance doesn't automatically release a static external IP address. You must manually release static external IP addresses when you no longer require them.

To release a static external IP address, see [Release a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) in the VPC documentation.

## What's next

  * Learn more about [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).
  * Learn more about [networks and firewalls](https://docs.cloud.google.com/compute/docs/networks-and-firewalls).
  * Learn how to [address Compute Engine instances using internal DNS](https://docs.cloud.google.com/compute/docs/networking/using-internal-dns#access_by_internal_DNS).
  * Review [VPC pricing](https://docs.cloud.google.com/vpc/network-pricing#vpc-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
