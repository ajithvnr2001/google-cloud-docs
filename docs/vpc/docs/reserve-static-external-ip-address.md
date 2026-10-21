---
url: https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address/
title: Reserve a static external IP address \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:45.512896+00:00
---

# Reserve a static external IP address  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reserve a static external IP address

You can reserve static external IP addresses. You can also list and release your reserved static external IP addresses. To assign a static external IP address to a virtual machine (VM) instance, see [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).

External IP addresses can be [static or ephemeral](https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses). If a VM requires a fixed external IP address that does not change, you can obtain a static external IP address. You can reserve new external IP addresses or promote existing ephemeral external IP addresses.

If you require a static internal IP address, see [Reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) instead.

This page shows how to reserve static external IP addresses from Google's pool of external IP addresses. For information about reserving static external IP addresses that were imported through bring your own IP (BYOIP) addresses, see [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

## Before you begin

  * Read about [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).
  * Read about [quotas and limits for static external IP addresses](https://docs.cloud.google.com/compute/resource-usage#external_ip_addresses).
  * Read about [external IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).
  * If you haven't already, set up authentication. [Authentication](https://docs.cloud.google.com/docs/authentication) is the process by which your identity is verified for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate as follows. 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to reserve and manage static IP addresses, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to reserve and manage static IP addresses. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to reserve and manage static IP addresses:

  * `compute.addresses.create` on the IP address
  * `compute.addresses.createInternal` on the IP address
  * `compute.networks.list` on the network
  * `compute.subnetworks.use` on the subnet
  * `compute.subnetworks.list` on the subnet



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## About static external IP addresses

A static external IP address is a resource that reserves an IP address for use by other resources in your project. A reserved address remains fixed and available for your customers and services until you decide to release it. You can also promote an ephemeral external IP address to a static external IP address.

For more information, see [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).

**Note:** Google-provided static external IP addresses are not announced to the public internet until you associate them with a resource, such as a VM or an external forwarding rule.

The following table lists the static external IP addresses supported by Google Cloud.

IP address type | Resource | IP range | Source | Associated with  
---|---|---|---|---  
Regional external IPv4 addresses | VMs and regional load balancers | `/32` | Google's pool of external IP addresses or imported through BYOIP | Project  
Regional external IPv6 addresses | VMs and supported regional load balancers | `/96` | Subnet's external IPv6 address range, which can be sourced from Google's pool of external IP addresses or imported through BYOIP | Subnet  
Global external IPv4 addresses | Global load balancers | `/32` | Google's pool of external IP addresses or imported through BYOIP | Project  
Global external IPv6 addresses | Global load balancers | `/64` | Google's pool of external IP addresses | Project  
  
For a list of regional and global load balancers, see the [Summary of load balancer types](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#lb-summary).

Assigned external IP addresses exist on the same physical host as the VM and exist in the same region as the VM for all purposes, including routing, latency, and pricing. This is true regardless of [internet geolocation](https://wikipedia.org/wiki/Internet_geolocation) lookup information.

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

## Reserve a new static external IP address

After reserving the address, assign it to a [new VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#assign_new_instance) while creating it or to an [existing VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign).

**Note:** If you reserve a static external IP address but don't assign it to a resource such as a VM or a forwarding rule, then you are charged at a higher rate than for static and ephemeral external IP addresses that are in use. For more information, see [External IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).**Note:** The Google Cloud console doesn't support selecting the IPv6 network tier. To explicitly set external IPv6 addresses to Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages)), use the gcloud CLI or the API.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page. 

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.
  3. In the **Name** field, enter an IP address name.
  4. Specify whether the network service tier is **Premium** or **Standard**.
  5. Specify whether it is an **IPv4** or **IPv6** address.
  6. Specify whether this IP address is **Regional** or **Global**. 
     * If you are reserving a static IP address for a global load balancer, choose **Global** and then click **Reserve**.
     * If you are reserving a static IP address for a VM or for a regional load balancer, choose **Regional** , and then select the region to create the address in.
  7. If you are reserving a regional external IPv6 address, then also choose the following:

     * **Network** : the VPC network
     * **Subnetwork** : the subnet from which to assign the static regional IPv6 address
     * **Static IPv6 range** : to specify a static external IPv6 address range to reserve, select **Let me choose** , and then enter a custom `/96` IPv6 address range from the subnet's `/64` external IPv6 address range. Otherwise, the system automatically assigns a static external IPv6 address range in the subnet for you.

For Google-provided external IPv6 subnet ranges, IP addresses for VMs must be from the first half (`/65`) of the subnet's `/64` external IPv6 address range and IP addresses for load balancing must be from the second half (`/65`). For more information, see [External IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6).

     * **Endpoint type** : choose **VM instance** or **External passthrough Network Load Balancer**

  8. Optional: If you are reserving the static external IP address for a VM, then in the **Attached to** list, select a VM to attach the IP address to.

  9. Click **Reserve** to reserve the IP address.




###  gcloud 

To reserve a static external IP address, use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).

Use the following instructions to reserve a static external IPv4 or IPv6 address:

**Note:** Global IP addresses can be used only with global load balancers.

  * To reserve a global external IP address:
        
        gcloud compute addresses create ADDRESS_NAME \
          --global \
          --ip-version=IP_VERSION
        

Replace the following:

    * `ADDRESS_NAME`: the name that you want to associate with this address.
    * `IP_VERSION`: the IP version, either `IPv4` or `IPv6`.
  * To reserve a regional external IPv4 address:
        
        gcloud compute addresses create ADDRESS_NAME \
           --region=REGION
        

Replace the following:

    * `ADDRESS_NAME`: the name that you want to associate with this address.
    * `REGION`: a region for the IP address.
  * To reserve a regional external IPv6 address:
        
        gcloud compute addresses create ADDRESS_NAME \
           --region=REGION \
           --subnet=SUBNET_NAME \
           --ip-version=IPV6 \
           --endpoint-type=ENDPOINT_TYPE  \
           --addresses=IPV6_ADDRESS
        

Replace the following:

    * `ADDRESS_NAME`: the name that you want to associate with this address.
    * `REGION`: a region for the IP address.
    * `SUBNET_NAME`: the subnet to assign the static regional IPv6 address from. The subnet must have an [assigned external IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).
    * `ENDPOINT_TYPE`: for regional external IPv6 addresses, specify the endpoint type, either `VM` or `NETLB`.
    * `IPV6_ADDRESS`: the IPv6 address to reserve, which must be a `/96` IPv6 address range from the subnet. If unspecified, an IPv6 address is automatically allocated.

For Google-provided external IPv6 subnet ranges, IP addresses for VMs must be from the first half (`/65`) of the subnet's `/64` external IPv6 address range and IP addresses for load balancing must be from the second half (`/65`). For more information, see [External IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6).




To view the result, use the [`gcloud compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe):
    
    
    gcloud compute addresses describe ADDRESS_NAME
    

### Terraform

You can use the [`google_compute_address` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_address) to create a regional external IP address.

**Note:** You can't include a specific IP address during the reservation process unless you [Bring your own IP addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).
    
    
    resource "google_compute_address" "default" {
      name   = "my-test-static-ip-address"
      region = "us-central1"
    }

The following sample shows how to use the [`google_compute_global_address` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_address) to create a global external IPv6 address:
    
    
    resource "google_compute_global_address" "default" {
      project      = var.project_id # Replace this with your service project ID in quotes
      name         = "ipv6-address"
      address_type = "EXTERNAL"
      ip_version   = "IPV6"
    }

###  API 

  * To create a regional IPv4 address, call the regional [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
        

Your request body should contain the following:
        
        {
          "name": "ADDRESS_NAME"
        }
        

Replace the following:

    * `PROJECT_ID`: the project ID for this request
    * `REGION`: the name of the region for this request
    * `ADDRESS_NAME`: the name that you want to associate with the address
  * For global static IPv4 addresses, call the [`globalAddresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses
        

Your request body should contain the following:
        
        {
          "name": "ADDRESS_NAME"
        }
        

  * For global static IPv6 addresses, call the [`globalAddresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses
        

Your request body should contain the following:
        
        {
          "name": "ADDRESS_NAME",
          "ipVersion": "IPV6"
        }
        

To see the result, use the [`addresses.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/get).

  * For regional static IPv6 addresses, call the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
        

Your request body should contain the following:
        
        {
          "name": "ADDRESS_NAME",
          "ipVersion": "IPV6",
          "ipv6EndpointType": "VM|LB",
          "networkTier": "IPV6_NETWORK_TIER",
          "subnetwork": "SUBNET"
          "address": "IPV6_ADDRESS"
        }
        

Replace the following:

    * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.
    * `SUBNET`: the subnet for this project.
    * `IPV6_ADDRESS`: the IPv6 address to reserve, which must be a `/96` IPv6 address range from the subnet. If unspecified, an IP address is automatically allocated.

For Google-provided external IPv6 subnet ranges, IP addresses for VMs must be from the first half (`/65`) of the subnet's `/64` external IPv6 address range and IP addresses for load balancing must be from the second half (`/65`). For more information, see [External IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6).

To see the result, use the [`addresses.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/get).




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // reserveNewRegionalExternal reserves a new regional external IP address in Google Cloud Platform.
    func reserveNewRegionalExternal(w io.Writer, projectID, region, addressName string, isPremium bool) (*computepb.Address, error) {
    	// projectID := "your_project_id"
    	// region := "europe-central2"
    	// addressName := "your_address_name"
    	// isPremium := true
    	ctx := context.Background()
    
    	networkTier := computepb.[AccessConfig_STANDARD](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_NETWORK_TIER_AccessConfig_FIXED_STANDARD_AccessConfig_PREMIUM_AccessConfig_STANDARD_AccessConfig_STANDARD_OVERRIDES_FIXED_STANDARD).String()
    	if isPremium {
    		networkTier = computepb.[AccessConfig_PREMIUM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AccessConfig_UNDEFINED_NETWORK_TIER_AccessConfig_FIXED_STANDARD_AccessConfig_PREMIUM_AccessConfig_STANDARD_AccessConfig_STANDARD_OVERRIDES_FIXED_STANDARD).String()
    	}
    
    	address := &computepb.Address{
    		Name:        &addressName,
    		NetworkTier: &networkTier,
    	}
    
    	client, err := compute.[NewAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_AddressesClient_NewAddressesRESTClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewAddressesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &computepb.InsertAddressRequest{
    		Project:         projectID,
    		Region:          region,
    		AddressResource: address,
    	}
    
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("unable to reserve regional address: %w", err)
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("waiting for the regional address reservation operation to complete: %w", err)
    	}
    
    	addressResult, err := client.Get(ctx, &computepb.GetAddressRequest{
    		Project: projectID,
    		Region:  region,
    		Address: addressName,
    	})
    	if err != nil {
    		return nil, fmt.Errorf("unable to get reserved regional address: %w", err)
    	}
    
    	fmt.Fprintf(w, "Regional address %v reserved: %v", addressName, addressResult.GetAddress())
    
    	return addressResult, err
    }
    
    // reserveNewGlobalExternal reserves a new global external IP address in Google Cloud Platform.
    func reserveNewGlobalExternal(w io.Writer, projectID, addressName string, isV6 bool) (*computepb.Address, error) {
    	// projectID := "your_project_id"
    	// addressName := "your_address_name"
    	// isV6 := false
    	ctx := context.Background()
    	ipVersion := computepb.[Address_IPV4](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_Address_UNDEFINED_IP_VERSION_Address_IPV4_Address_IPV6_Address_UNSPECIFIED_VERSION).String()
    	if isV6 {
    		ipVersion = computepb.[Address_IPV6](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_Address_UNDEFINED_IP_VERSION_Address_IPV4_Address_IPV6_Address_UNSPECIFIED_VERSION).String()
    	}
    
    	address := &computepb.Address{
    		Name:      &addressName,
    		IpVersion: &ipVersion,
    	}
    
    	client, err := compute.[NewGlobalAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_GlobalAddressesClient_NewGlobalAddressesRESTClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewGlobalAddressesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &computepb.InsertGlobalAddressRequest{
    		Project:         projectID,
    		AddressResource: address,
    	}
    
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("unable to reserve global address: %w", err)
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("waiting for the global address reservation operation to complete: %w", err)
    	}
    
    	addressResult, err := client.Get(ctx, &computepb.GetGlobalAddressRequest{
    		Project: projectID,
    		Address: addressName,
    	})
    	if err != nil {
    		return nil, fmt.Errorf("unable to get reserved global address: %w", err)
    	}
    
    	fmt.Fprintf(w, "Global address %v reserved: %v", addressName, addressResult.GetAddress())
    
    	return addressResult, nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html);
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).[AddressType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.AddressType.html);
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).IpVersion;
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).NetworkTier;
    import com.google.cloud.compute.v1.[AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html);
    import com.google.cloud.compute.v1.[GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html);
    import com.google.cloud.compute.v1.[InsertAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAddressRequest.html);
    import com.google.cloud.compute.v1.[InsertGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalAddressRequest.html);
    import com.google.common.collect.Lists;
    import java.io.IOException;
    import java.util.List;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ReserveNewExternalAddress {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Address name you want to use.
        String addressName = "your-address-name";
        // 'IPV4' or 'IPV6' depending on the IP version. IPV6 if True.
        boolean ipV6 = false;
        // 'STANDARD' or 'PREMIUM' network tier. Standard option available only in regional ip.
        boolean isPremium = false;
        // region (Optional[str]): The region to reserve the IP address in, if regional.
        // Must be None if global.
        String region = null;
    
        reserveNewExternalIpAddress(projectId, addressName, ipV6, isPremium, region);
      }
    
      // Reserves a new external IP address in the specified project and region.
      public static List<Address> reserveNewExternalIpAddress(String projectId, String addressName,
                                                              boolean ipV6, boolean isPremium,
                                                              String region)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        String ipVersion = ipV6 ? IpVersion.IPV6.name() : IpVersion.IPV4.name();
        String networkTier = !isPremium && region != null
                ? NetworkTier.STANDARD.name() : NetworkTier.PREMIUM.name();
    
        [Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).Builder address = [Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).newBuilder()
                .setName(addressName)
                .[setAddressType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.Builder.html#com_google_cloud_compute_v1_Address_Builder_setAddressType_java_lang_String_)([AddressType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.AddressType.html).EXTERNAL.name())
                .setNetworkTier(networkTier);
    
        // Use global client if no region is specified
        if (region == null) {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html) client = [GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html).create()) {
            address.setIpVersion(ipVersion);
    
            [InsertGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalAddressRequest.html) addressRequest = [InsertGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalAddressRequest.html).newBuilder()
                    .setProject(projectId)
                    .setRequestId(UUID.randomUUID().toString())
                    .setAddressResource(address.build())
                    .build();
    
            client.insertCallable().futureCall(addressRequest).get(30, TimeUnit.SECONDS);
    
            return Lists.newArrayList(client.list(projectId).iterateAll());
          }
        } else {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html) client = [AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html).create()) {
            address.setRegion(region);
    
            [InsertAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAddressRequest.html) addressRequest = [InsertAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAddressRequest.html).newBuilder()
                    .setProject(projectId)
                    .setRequestId(UUID.randomUUID().toString())
                    .setAddressResource(address.build())
                    .setRegion(region)
                    .build();
    
            client.insertCallable().futureCall(addressRequest).get(30, TimeUnit.SECONDS);
    
            return Lists.newArrayList(client.list(projectId, region).iterateAll());
          }
        }
      }
    }

###  Python 
    
    
    from typing import Optional
    
    from google.cloud.compute_v1.services.addresses.client import AddressesClient
    from google.cloud.compute_v1.services.global_addresses import GlobalAddressesClient
    from google.cloud.compute_v1.types import Address
    
    
    def reserve_new_external_ip_address(
        project_id: str,
        address_name: str,
        is_v6: bool = False,
        is_premium: bool = False,
        region: Optional[str] = None,
    ):
        """
        Reserves a new external IP address in the specified project and region.
    
        Args:
        project_id (str): Your Google Cloud project ID.
        address_name (str): The name for the new IP address.
        is_v6 (bool): 'IPV4' or 'IPV6' depending on the IP version. IPV6 if True.
        is_premium (bool): 'STANDARD' or 'PREMIUM' network tier. Standard option available only in regional ip.
        region (Optional[str]): The region to reserve the IP address in, if regional. Must be None if global.
    
        Returns:
        None
        """
    
        ip_version = "IPV6" if is_v6 else "IPV4"
        network_tier = "STANDARD" if not is_premium and region else "PREMIUM"
    
        address = Address(
            name=address_name,
            address_type="EXTERNAL",
            network_tier=network_tier,
        )
        if not region:  # global IP address
            client = GlobalAddressesClient()
            address.ip_version = ip_version
            operation = client.insert(project=project_id, address_resource=address)
        else:  # regional IP address
            address.region = region
            client = AddressesClient()
            operation = client.insert(
                project=project_id, region=region, address_resource=address
            )
    
        operation.result()
    
        print(f"External IP address '{address_name}' reserved successfully.")
    
    

## Promote an ephemeral external IP address

If your VM has an [ephemeral external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#ephemeraladdress) and you want to permanently assign the IP address to your project, promote the ephemeral external IP address to a static external IP address. Promoting an ephemeral external IP address to reserved does not cause Google Cloud to drop packets sent to the VM. This includes packets sent to the VM directly or by means of a load balancer.

###  Console 

  1. Go to the **IP addresses** page. 

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **External IP addresses**.
  3. Optional: In the **Filter** field, search for the ephemeral IP address that you want to promote.
  4. In the **More actions** menu (more_vert) of the IP address that you want to promote, select **Promote to static IP address**.
  5. Enter a name for the new static IP address, and then click **Reserve**.



###  gcloud 

Use the following instructions to promote a static external IPv4 or IPv6 address:

  * To promote an ephemeral external IPv4 address to a static external IPv4 address, provide the ephemeral external IP address by using the `--addresses` flag with the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create). Use the `region` flag to promote an ephemeral regional IP address or the `global` flag to promote an ephemeral global IP address.
        
        gcloud compute addresses create ADDRESS_NAME --addresses=IP_ADDRESS \
            [--region=REGION | --global]
        

Replace the following:

    * `ADDRESS_NAME`: the name that you want to associate with this address.
    * `IP_ADDRESS`: the IP address that you want to promote.
    * `REGION`: the region that the regional IP address belongs to.
  * To promote an ephemeral regional external IPv6 address to a static regional external IPv6 address, provide the ephemeral external IP address by using the `--addresses` flag with the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
        
        gcloud compute addresses create ADDRESS_NAME \
          --region=REGION \
          --addresses=IPV6_ADDRESS \
          --prefix-length=96
        

Replace the following:

    * `ADDRESS_NAME`: a name for the IP address resource.
    * `REGION`: the region for the IPv6 address resource.
    * `IPV6_ADDRESS`: the IPv6 address that you're promoting.



###  API 

To promote an ephemeral regional IP address, call the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
    

To promote an ephemeral global IP address, make a `POST` request to the following URI:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses
    

Specify the values for the required fields of the request body:

  * For IPv4 addresses, your request body should contain the following fields:
        
        {
          "name": "ADDRESS_NAME",
          "address": "IPV4_ADDRESS"
          "addressType": "EXTERNAL"
        }
        

  * For IPv6 addresses, your request body should contain the following fields:
        
        {
          "name": "ADDRESS_NAME",
          "address": "IPV6_ADDRESS"
          "prefixLength": 96
          "addressType": "EXTERNAL"
        }
        

Replace the following:

    * `ADDRESS_NAME`: the name that you want to associate with this address
    * `IPV4_ADDRESS|IPV6_ADDRESS`: the IPv4 or IPv6 address that you want to promote
    * `REGION`: the region that the IPv4 or IPv6 address belongs to
    * `PROJECT_ID`: the project ID for this request



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // promoteEphemeralAddress promotes an ephemeral IP address to a reserved static external IP address.
    func promoteEphemeralAddress(w io.Writer, projectID, region, ephemeralIP, addressName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-central2"
    	// ephemeral_ip := "214.123.100.121"
    	ctx := context.Background()
    
    	client, err := compute.[NewAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_AddressesClient_NewAddressesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewAddressesRESTClient: %w", err)
    	}
    	defer client.Close()
    
    	addressResource := &computepb.Address{
    		Name:        proto.String(addressName),
    		AddressType: proto.String("EXTERNAL"),
    		Address:     proto.String(ephemeralIP),
    	}
    
    	req := &computepb.InsertAddressRequest{
    		Project:         projectID,
    		Region:          region,
    		AddressResource: addressResource,
    	}
    
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to insert address promoted: %v", err)
    	}
    
    	// Wait for the operation to complete
    	err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to complete promotion operation: %v", err)
    	}
    
    	fmt.Fprintf(w, "Ephemeral IP %s address promoted successfully", ephemeralIP)
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html);
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).[AddressType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.AddressType.html);
    import com.google.cloud.compute.v1.[AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html);
    import com.google.cloud.compute.v1.[InsertAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAddressRequest.html);
    import com.google.common.collect.Lists;
    import java.io.IOException;
    import java.util.List;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class PromoteEphemeralIp {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Region where the VM and IP is located.
        String region = "your-region-id";
        // Ephemeral IP address to promote.
        String ephemeralIp = "your-ephemeralIp";
        // Name of the address to assign.
        String addressName = "your-addressName";
    
        promoteEphemeralIp(projectId, region, ephemeralIp, addressName);
      }
    
      // Promote ephemeral IP found on the instance to a static IP.
      public static List<Address> promoteEphemeralIp(String projectId, String region,
                                                     String ephemeralIp, String addressName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html) client = [AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html).create()) {
          [Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html) addressResource = [Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html).newBuilder()
                  .setName(addressName)
                  .setRegion(region)
                  .[setAddressType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.Builder.html#com_google_cloud_compute_v1_Address_Builder_setAddressType_java_lang_String_)([AddressType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.AddressType.html).EXTERNAL.name())
                  .setAddress(ephemeralIp)
                  .build();
    
          [InsertAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAddressRequest.html) addressRequest = [InsertAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAddressRequest.html).newBuilder()
                  .setRegion(region)
                  .setProject(projectId)
                  .setAddressResource(addressResource)
                  .setRequestId(UUID.randomUUID().toString())
                  .build();
    
          client.insertCallable().futureCall(addressRequest).get(30, TimeUnit.SECONDS);
    
          return Lists.newArrayList(client.list(projectId, region).iterateAll());
        }
      }
    }

###  Python 
    
    
    import uuid
    
    from google.cloud.compute_v1 import [AddressesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.addresses.AddressesClient.html)
    from google.cloud.compute_v1.types import [Address](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Address.html)
    
    
    def promote_ephemeral_ip(project_id: str, ephemeral_ip: str, region: str):
        """
        Promote ephemeral IP found on the instance to a static IP.
    
        Args:
            project_id (str): Project ID.
            ephemeral_ip (str): Ephemeral IP address to promote.
            region (str): Region where the VM and IP is located.
        """
        addresses_client = AddressesClient()
    
        # Create a new static IP address using existing ephemeral IP
        address_resource = Address(
            name=f"ip-reserved-{uuid.uuid4()}",  # new name for promoted IP address
            region=region,
            address_type="EXTERNAL",
            address=ephemeral_ip,
        )
        operation = addresses_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.addresses.AddressesClient.html#google_cloud_compute_v1_services_addresses_AddressesClient_insert)(
            project=project_id, region=region, address_resource=address_resource
        )
        operation.result()
    
        print(f"Ephemeral IP {ephemeral_ip} has been promoted to a static IP.")
    
    

The external IP address remains attached to the VM even after it has been promoted to a static external IP address. If you need to assign the newly promoted static external IP address to another resource, [unassign the static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip) from the existing VM.

## List static external IP addresses

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
    
    

## Describe a static external IP address

To get information about a static external IP address, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **External IP addresses**.

  3. Click the IP address that you want to get more information about.




###  gcloud 

Use the [`gcloud compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe). Replace `ADDRESS_NAME` with the name of the external IP address that you want to describe.

  * For a global IPv4 or IPv6 address, use the following command:
        
        gcloud compute addresses describe ADDRESS_NAME --global

  * For a regional IPv4 or IPv6 address, use the following command:
        
        gcloud compute addresses describe ADDRESS_NAME --region=REGION




###  API 

  * To describe a regional IPv4 or IPv6 address, call the [`addresses.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/get):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME
        

Replace the following:

    * `PROJECT_ID`: the project ID for the request
    * `REGION`: the name of the region for the request
    * `ADDRESS_NAME`: the name of the IP address
  * To describe a global IPv4 or IPv6 address, call the [`globalAddresses.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/get):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses/ADDRESS_NAME
        

Replace the following:

    * `PROJECT_ID`: the project ID for the request
    * `ADDRESS_NAME`: the name of the IP address



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // getExternalAddress retrieves the external IP address of the given address.
    func getRegionalExternal(w io.Writer, projectID, region, addressName string) (*computepb.Address, error) {
    	// projectID := "your_project_id"
    	// region := "europe-west3"
    	// addressName := "your_address_name"
    
    	ctx := context.Background()
    	addressesClient, err := compute.[NewAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_AddressesClient_NewAddressesRESTClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewAddressesRESTClient: %w", err)
    	}
    	defer addressesClient.Close()
    
    	req := &computepb.GetAddressRequest{
    		Project: projectID,
    		Region:  region,
    		Address: addressName,
    	}
    
    	address, err := addressesClient.Get(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("unable to get address: %w", err)
    	}
    
    	fmt.Fprintf(w, "Regional address %s has external IP address: %s\n", addressName, address.GetAddress())
    
    	return address, nil
    }
    
    func getGlobalExternal(w io.Writer, projectID, addressName string) (*computepb.Address, error) {
    
    	ctx := context.Background()
    	globalAddressesClient, err := compute.[NewGlobalAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_GlobalAddressesClient_NewGlobalAddressesRESTClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewGlobalAddressesRESTClient: %w", err)
    	}
    	defer globalAddressesClient.Close()
    
    	req := &computepb.GetGlobalAddressRequest{
    		Project: projectID,
    		Address: addressName,
    	}
    
    	address, err := globalAddressesClient.Get(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("unable to get address: %w", err)
    	}
    
    	fmt.Fprintf(w, "Global address %s has external IP address: %s\n", addressName, address.GetAddress())
    
    	return address, nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html);
    import com.google.cloud.compute.v1.[AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html);
    import com.google.cloud.compute.v1.[GetAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAddressRequest.html);
    import com.google.cloud.compute.v1.[GetGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalAddressRequest.html);
    import com.google.cloud.compute.v1.[GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class GetStaticIpAddress {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Region where the VM and IP is located.
        String region = "your-region-id";
        // Name of the address to assign.
        String addressName = "your-addressName";
    
        getStaticIpAddress(projectId, region, addressName);
      }
    
      // Retrieves a static external IP address, either regional or global.
      public static [Address](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Address.html) getStaticIpAddress(String projectId, String region, String addressName)
              throws IOException {
        // Use regional client if a region is specified
        if (region != null) {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html) client = [AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html).create()) {
            [GetAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAddressRequest.html) request = [GetAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAddressRequest.html).newBuilder()
                    .setProject(projectId)
                    .setRegion(region)
                    .setAddress(addressName)
                    .build();
    
            return client.get(request);
          }
        } else {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html) client = [GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html).create()) {
            [GetGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalAddressRequest.html) request = [GetGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalAddressRequest.html).newBuilder()
                    .setProject(projectId)
                    .setAddress(addressName)
                    .build();
    
            return client.get(request);
          }
        }
      }
    }

###  Python 
    
    
    from typing import Optional
    
    from google.cloud.compute_v1.services.addresses.client import AddressesClient
    from google.cloud.compute_v1.services.global_addresses import GlobalAddressesClient
    from google.cloud.compute_v1.types import Address
    
    
    def get_static_ip_address(
        project_id: str, address_name: str, region: Optional[str] = None
    ) -> Address:
        """
        Retrieves a static external IP address, either regional or global.
    
        Args:
        project_id (str): project ID.
        address_name (str): The name of the IP address.
        region (Optional[str]): The region of the IP address if it's regional. None if it's global.
    
        Raises: google.api_core.exceptions.NotFound: in case of address not found
    
        Returns:
        Address: The Address object containing details about the requested IP.
        """
        if region:
            # Use regional client if a region is specified
            client = AddressesClient()
            address = client.get(project=project_id, region=region, address=address_name)
        else:
            # Use global client if no region is specified
            client = GlobalAddressesClient()
            address = client.get(project=project_id, address=address_name)
    
        return address
    
    

## Release a static external IP address

If you no longer need a static external IPv4 or IPv6 address, you can release the IP address by deleting the IP address resource.

If you are using the Google Cloud console, you can release a static IP address only if it is not being used by another resource.

If you're using the gcloud CLI or API, you can release an IP address whether or not it's being used by another resource.

  * If the IP address is not being used by a resource, the IP address is returned to the pool of available external IP addresses.

  * If the IP address is being used by a resource, it remains attached to the resource until the resource is deleted.


**Important:** After the IP address is released, you might not be able to reserve the same static IPv4 or IPv6 address because some other user might have already reserved it.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **External IP addresses**.

  3. Optional: In the **Filter** field, enter `static` and then select **Static : Type** from the drop-down list.

  4. Select the static external IP address that you want to release.

  5. Click **Release static address**.

If you don't see this option, click the **More actions** menu (more_vert) in the top menu bar, and then select **Release static address** from the list.




###  gcloud 

Use the [`compute addresses delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/delete):
    
    
    gcloud compute addresses delete ADDRESS_NAME
    

Replace `ADDRESS_NAME` with the name of the IPv4 or IPv6 address to release.

###  API 

  * To release a regional IPv4 or IPv6 address, call the [`addresses.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/delete):
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME
        

Replace the following:

    * `PROJECT_ID`: the project ID for this request
    * `REGION`: the name of the region for this request
    * `ADDRESS_NAME`: the name of the IP address
  * To release a global IPv4 or IPv6 address, call the [`globalAddresses.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalAddresses/delete):
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/addresses/ADDRESS_NAME
        

Replace the following:

    * `ADDRESS_NAME`: the name of the IP address
    * `PROJECT_ID`: the project ID for this request



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	"cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // releaseRegionalStaticExternal releases a static regional external IP address.
    func releaseRegionalStaticExternal(w io.Writer, projectID, region, addressName string) error {
    	// projectID := "your_project_id"
    	// region := "us-central1"
    	// addressName := "your_address_name"
    
    	ctx := context.Background()
    	addressesClient, err := compute.[NewAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_AddressesClient_NewAddressesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewAddressesRESTClient: %w", err)
    	}
    	defer addressesClient.Close()
    
    	req := &computepb.DeleteAddressRequest{
    		Project: projectID,
    		Region:  region,
    		Address: addressName,
    	}
    
    	op, err := addressesClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to release static external IP address: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Static external IP address released\n")
    
    	return nil
    }
    
    // releaseGlobalStaticExternal releases a static global external IP address.
    func releaseGlobalStaticExternal(w io.Writer, projectID, addressName string) error {
    	// projectID := "your_project_id"
    	// addressName := "your_address_name"
    
    	ctx := context.Background()
    	addressesClient, err := compute.[NewGlobalAddressesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_GlobalAddressesClient_NewGlobalAddressesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewGlobalAddressesRESTClient: %w", err)
    	}
    	defer addressesClient.Close()
    
    	req := &computepb.DeleteGlobalAddressRequest{
    		Project: projectID,
    		Address: addressName,
    	}
    
    	op, err := addressesClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to release static external IP address: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Static external IP address released\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html);
    import com.google.cloud.compute.v1.[DeleteAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAddressRequest.html);
    import com.google.cloud.compute.v1.[DeleteGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalAddressRequest.html);
    import com.google.cloud.compute.v1.[GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ReleaseStaticAddress {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // The region to reserve the IP address in, if regional. Must be None if global
        String region = "your-region =";
        // Name of the address to release.
        String addressName = "your-addressName";
    
        releaseStaticAddress(projectId, addressName, region);
      }
    
      // Releases a static external IP address that is currently reserved.
      // This action requires that the address is not being used by any forwarding rule.
      public static void releaseStaticAddress(String projectId, String addressName, String region)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation;
        // Use global client if no region is specified
        if (region == null) {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html) client = [GlobalAddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalAddressesClient.html).create()) {
            [DeleteGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalAddressRequest.html) request = [DeleteGlobalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalAddressRequest.html).newBuilder()
                    .setProject(projectId)
                    .setAddress(addressName)
                    .build();
    
            operation = client.deleteCallable().futureCall(request).get(30, TimeUnit.SECONDS);
          }
        } else {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try ([AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html) client = [AddressesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddressesClient.html).create()) {
            [DeleteAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAddressRequest.html) request = [DeleteAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAddressRequest.html).newBuilder()
                    .setProject(projectId)
                    .setRegion(region)
                    .setAddress(addressName)
                    .build();
    
            operation = client.deleteCallable().futureCall(request).get(30, TimeUnit.SECONDS);
          }
        }
        if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
          System.out.printf("Can't release external IP address '%s'. Caused by : %s",
                  addressName, operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
        }
        System.out.printf("External IP address '%s' released successfully.", addressName);
      }
    }

###  Python 
    
    
    from typing import Optional
    
    from google.cloud.compute_v1.services.addresses.client import AddressesClient
    from google.cloud.compute_v1.services.global_addresses import GlobalAddressesClient
    
    
    def release_external_ip_address(
        project_id: str,
        address_name: str,
        region: Optional[str] = None,
    ) -> None:
        """
        Releases a static external IP address that is currently reserved.
        This action requires that the address is not being used by any forwarding rule.
    
        Args:
            project_id (str): project ID.
            address_name (str): name of the address to release.
            region (Optional[str]): The region to reserve the IP address in, if regional. Must be None if global.
    
    
        """
        if not region:  # global IP address
            client = GlobalAddressesClient()
            operation = client.delete(project=project_id, address=address_name)
        else:  # regional IP address
            client = AddressesClient()
            operation = client.delete(
                project=project_id, region=region, address=address_name
            )
    
        operation.result()
        print(f"External IP address '{address_name}' released successfully.")
    
    

## What's next

  * Learn how to [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) for a new or existing VM.
  * Learn about [IP address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications) for forwarding rules, and how to [use forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#use-forwarding-rules), in the _Forwarding rules overview_.
  * Learn more about [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
