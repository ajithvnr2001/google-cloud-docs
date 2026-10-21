---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access/
title: Configure internet access for workload VMs \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:18.373110+00:00
---

# Configure internet access for workload VMs  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure internet access for workload VMs

You configure the internet access network service for VMware workloads in Google Cloud VMware Engine on a per-region basis. You can direct internet-bound traffic from your workload VMs by using Google Cloud's internet edge or an on-premises connection.

VMware Engine offers the following methods for configuring internet access for workload VMs:

  * **VMware Engine internet access service** : Enables direct internet access for workload VMs using Google Cloud's internet edge. See Configure the internet access service.
  * **On-premises connection** : Routes internet-bound traffic from workload VMs through your on-premises connection. See Use an on-premises connection for workload internet access.
  * **Consumer VPC network** : Routes internet-bound traffic from workload VMs through your consumer VPC network. See Use a VPC in your project for workload internet access.



Workload VMs that can access the internet can also access Google Cloud services using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). Access to Google Cloud services using Private Google Access stays within Google Cloud networks and does not exit to the internet.

The internet access network service supports the following:

  * Up to 100 public IP addresses for each region
  * Up to 100 external access rules per network policy
  * Throughput of up to 2 Gbps for each region
  * TCP, UDP, and ICMP protocols



The internet access network service doesn't support Application Level Gateway (ALG) capability.

## Before you begin

To make changes to the internet access settings of your private cloud, you must have [admin access](https://docs.cloud.google.com/vmware-engine/docs/iam) to VMware Engine.

To enable internet access, you need an _edge services CIDR address range_. When you enable the internet access or public IP network services, gateways deploy in the service tenant context.

Use the edge services CIDR address range for addressing VMware Engine internet and public IP gateways. The address range must meet the following requirements:

  * Comply with [RFC 1918](https://tools.ietf.org/html/rfc1918) as a private range.
  * Have no overlap with any other VMware Engine address ranges, such as the address range used for management appliances or NSX segments.
  * Have no overlap with any address ranges being advertised to VMware Engine, such as those used for Virtual Private Cloud (VPC) network subnets or on-premises networks.
  * Dedicate an IP address range with 26 subnet mask bits (_/26_).



### Google Cloud CLI and API requirements

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

## Configure the internet access service

To give your workload VMs internet access, create or update a network policy.

By default, the internet access network service is disabled.

### Enable the internet access service in a region

###  Console 

To enable the internet access service in a region, do the following:

  1. In the Google Cloud console, go to the **Network policies** page.

[Go to Network policies](https://console.cloud.google.com/vmwareengine/network-policies)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to enable the internet access service for.

  3. Click **Create** to create a new policy. If you want to edit an existing network policy, click the **More** more_vert icon at the end of a row and select **Edit**.

  4. Fill out the details of your network policy, including choosing the network and region that the policy applies to.

  5. Toggle **Internet access** to **Enabled** and, optionally, enable **External IP address service**.

**Note:** You can enable internet access and leave public IP service disabled. If you do so, point-to-site VPN and public IP allocation are not available.
  6. In the **Edge Services CIDR** field, enter the address range to use when addressing the VMware Engine internet gateway (_/26_ address range).

  7. Click **Create**.




The status for the service changes to **Enabled** when the operation is complete, usually after several minutes.

###  gcloud 

Using the `gcloud` tool, run the following command to create a network policy:
    
    
    gcloud vmware network-policies create NETWORK_POLICY_NAME \
        --vmware-engine-network projects/PROJECT_ID/locations/LOCATIONS/vmwareEngineNetworks/NETWORK_ID \
        --edge-services-cidr=IP_RANGE \
        --location=LOCATION \
        --internet-access

Replace the following:

  * `NETWORK_POLICY_NAME`: the name for this network policy.
  * `NETWORK_ID`: the network this network policy applies to
  * `IP_RANGE`: the CIDR range to use for internet access and external IP access gateways, in CIDR notation. An RFC 1918 CIDR block with a "/26" prefix is required.
  * `LOCATION`: `global` for legacy networks or the region of a standard network



###  API 
    
    
    curl -X POST -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/networkPolicies?networkPolicyId=NETWORK_POLICY_NAME
    
    '{
      "vmwareEngineNetwork":"projects/PROJECT_ID/locations/LOCATION/vmwareEngineNetworks/NETWORK_ID",
      "edgeServiceCidr":"IP_RANGE",
      "internetAccess": {
        "enabled": true
       },
       "externalIp": {
         "enabled": true
       }
    }'
    

Replace the following:

  * `NETWORK_POLICY_NAME`: the name for this network policy. This must be in the format `REGION-default`.
  * `PROJECT_ID`: the project ID for this request
  * `LOCATION`: `global` for legacy networks or the region of a standard network
  * `IP_RANGE`: the CIDR range to use for internet access and external IP access gateways, in CIDR notation. An RFC 1918 CIDR block with a "/26" prefix is required.
  * `NETWORK_ID`: the network for this this network policy



###  Python 
    
    
    from google.api_core import operation
    from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
    
    
    def create_network_policy(
        project_id: str,
        region: str,
        ip_range: str,
        internet_access: bool,
        external_ip: bool,
    ) -> operation.Operation:
        """
        Creates a new network policy in a given network.
    
        Args:
            project_id: name of the project you want to use.
            region: name of the region you want to use. I.e. "us-central1"
            ip_range: the CIDR range to use for internet access and external IP access gateways,
                in CIDR notation. An RFC 1918 CIDR block with a "/26" suffix is required.
            internet_access: should internet access be allowed.
            external_ip: should external IP addresses be assigned.
    
        Returns:
            An operation object representing the started operation. You can call its .result() method to wait for
            it to finish.
    
        Raises:
            ValueError if the provided ip_range doesn't end with /26.
        """
        if not ip_range.endswith("/26"):
            raise ValueError(
                "The ip_range needs to be an RFC 1918 CIDR block with a '/26' suffix"
            )
    
        network_policy = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NetworkPolicy.html)()
        network_policy.vmware_engine_network = f"projects/{project_id}/locations/{region}/vmwareEngineNetworks/{region}-default"
        network_policy.edge_services_cidr = ip_range
        network_policy.internet_access.enabled = internet_access
        network_policy.external_ip.enabled = external_ip
    
        request = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[CreateNetworkPolicyRequest](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.CreateNetworkPolicyRequest.html)()
        request.network_policy = network_policy
        request.parent = f"projects/{project_id}/locations/{region}"
        request.network_policy_id = f"{region}-default"
    
        client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
        return client.[create_network_policy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_create_network_policy)(request)
    
    

#### Guidelines for HCX Mobility Optimized Networking (MON)

If you migrate VMs using HCX with Mobility Optimized Networking (MON), you need a specific routing configuration to ensure internet connectivity.

If you've enabled MON for Layer 2 Extension (L2E) segments, VMware Engine doesn't automatically advertise routes for migrated VMs to its internet service. To ensure that these VMs can access the internet, you must enable static route redistribution to BGP at the Tier-1 router.

This step is required to advertise the routes of your MON-enabled segments, which lets them route internet traffic through the VMware Engine environment. Without this configuration, VMs on these segments can't access the public internet.

### Disable the internet access service in a region

To disable the internet access service in a region, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Network policies** page.

[Go to Network policies](https://console.cloud.google.com/vmwareengine/network-policies)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to disable the internet access service for.

  3. In the row corresponding to the relevant network policy, click the **More** more_vert icon.

  4. Toggle **Internet access** to **Disabled**.

     * You must disable public IP service before you can disable internet access.
     * You must delete any allocated public IP addresses and point-to-site VPN gateways before you can disable public IP service.
  5. Click **Save**.




The status for the service changes to **Disabled** when the operation is complete, usually after several minutes.

###  gcloud 

Using the `gcloud` tool, run the following command to update network policy:
    
    
    gcloud vmware network-policies update NETWORK_POLICY_NAME \
      --no-internet-access \
      --location LOCATION

Replace the following:

  * `NETWORK_POLICY_NAME`: the name for this network policy
  * `LOCATION`: `global` for legacy networks or the region of a standard network



###  API 
    
    
    curl -X PATCH -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/networkPolicies/NETWORK_POLICY_NAME?updateMask=internetAccess.enabled,externalIp.enabled -d "{
      "internetAccess": {
        "enabled": false
     },
      "externalIp": {
        "enabled": false
       }
    }"
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `LOCATION`: `global` for legacy networks or the region of a standard network
  * `NETWORK_POLICY_NAME`: the name for this network policy



###  Python 
    
    
    from google.api_core import operation
    from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
    
    
    def update_network_policy(
        project_id: str, region: str, internet_access: bool, external_ip: bool
    ) -> operation.Operation:
        """
        Updates a network policy in a given network.
    
        Args:
            project_id: name of the project you want to use.
            region: name of the region you want to use. I.e. "us-central1".
            internet_access: should internet access be allowed.
            external_ip: should external IP addresses be assigned.
    
        Returns:
            An operation object representing the started operation. You can call its .result() method to wait for
            it to finish.
        """
    
        client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
        request = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.UpdateNetworkPolicyRequest.html)()
        request.update_mask = "internetAccess.enabled,externalIp.enabled"
        network_policy = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NetworkPolicy.html)()
        network_policy.name = (
            f"projects/{project_id}/locations/{region}/networkPolicies/{region}-default"
        )
        network_policy.vmware_engine_network = f"projects/{project_id}/locations/{region}/vmwareEngineNetworks/{region}-default"
        network_policy.internet_access.enabled = internet_access
        network_policy.external_ip.enabled = external_ip
    
        request.network_policy = network_policy
    
        return client.[update_network_policy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_update_network_policy)(request)
    
    

## Use a VPC in your project for workload internet access

You can optionally direct internet-bound traffic from your workload VMs in VMware Engine through a VPC in your project. This option is only available for standard VMware Engine networks that are peered with your VPC network.

To access the internet from your workload VMs through a VPC in your project, you must complete the following steps:

  1. Configure internet access in your VPC. 
     * **If you use Cloud NAT:** Ensure that Cloud NAT is configured to provide internet access to resources in your VPC network. No specific route for `0.0.0.0/0` is required, as Cloud NAT provides internet connectivity directly.
     * **If you don't use Cloud NAT:** Ensure that you have a route in your VPC for destination `0.0.0.0/0` that directs traffic to a next hop that provides internet access, such as an instance-based firewall or proxy. Additionally, you must [configure VPC Network Peering to exchange custom routes](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peering-connection). Update the peering connection to export custom routes from your VPC and import custom routes to it.
  2. Disable the internet access and public IP service for the VMware Engine network by following the steps in Disable the internet access service in a region.



After you complete these steps, internet-bound traffic from your workload VMs routes through the peering connection to your VPC network and uses the internet access solution configured there.

For more details, see [Configure internet access for workload VMs using VPC](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-configure-internet-access-vpc).

## Use an on-premises connection for workload internet access

You can optionally direct internet-bound traffic from your workload VMs in VMware Engine through an on-premises connection. How VMware Engine directs traffic depends on the state of the following:

  * Default route (`0.0.0.0/0`) advertisement from on-premises
  * VMware Engine public IP service
  * VMware Engine internet access service
  * VPC Service Controls on the VPC peering connection between your VPC network and VMware Engine (legacy VMware Engine networks only)



### Enable routing internet traffic through an on-premises connection

To access the internet from your workload VMs through an on-premises connection, you must complete two steps:

  1. Advertise the default route (`0.0.0.0/0`) from on-premises over an on-premises connection (Cloud VPN or Cloud Interconnect). Check the [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) gateway or [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) where the on-premises connection to your VPN terminates.
  2. Disable the internet access and public IP service for the VMware Engine network.



###  Console 

  1. In the Google Cloud console, go to the **Network policies** page.

[Go to Network policies](https://console.cloud.google.com/vmwareengine/network-policies)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to enable the internet access service for.

  3. In the row corresponding to the relevant network policy, click the **More** more_vert icon.

  4. Toggle **Public IP** to **Disabled**.

**Note:** You must delete any allocated external IP address and point-to-site VPN gateways before you can disable the public IP service.
  5. Toggle **Internet access** to **Disabled**.

  6. Click **Save**.

  7. **If using a Legacy VMware Engine network:** enable **VPC service controls** on the VPC peering connection between your VPC network and VMware Engine using the [`gcloud services vpc-peerings enable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls):
         
         gcloud services vpc-peerings enable-vpc-service-controls \
            --network=VPC_NETWORK \
            --service=servicenetworking.googleapis.com




###  gcloud 

Using the `gcloud` tool, run the following command to update network policy:
    
    
    gcloud vmware network-policies update NETWORK_POLICY_NAME \
      --no-internet-access \
      --no-external-ip-address \
      --location LOCATION

Replace the following:

  * `NETWORK_POLICY_NAME`: the name for this network policy
  * `LOCATION`: `global` for legacy networks or the region of a standard network



**If using a Legacy VMware Engine network:** enable **VPC service controls** on the VPC peering connection between your VPC network and VMware Engine using the [`gcloud services vpc-peerings enable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls):
    
    
    gcloud services vpc-peerings enable-vpc-service-controls \
       --network=VPC_NETWORK \
       --service=servicenetworking.googleapis.com

###  API 
    
    
    curl -X PATCH -H "Authorization: Bearer TOKEN"  -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/networkPolicies/NETWORK_POLICY_NAME?updateMask=internetAccess.enabled,externalIp.enabled
    
    "{
      "internetAccess: {
        "enabled": false
       },
      "externalIp: {
        "enabled": false
       }
    }"
    

**If using a Legacy VMware Engine network:** enable **VPC service controls** on the VPC peering connection between your VPC network and VMware Engine using the [`gcloud services vpc-peerings enable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls):
    
    
    gcloud services vpc-peerings enable-vpc-service-controls \
       --network=VPC_NETWORK_NAME \
       --service=servicenetworking.googleapis.com

###  Python 

Set the _internet_access_ and _external_ip_ to `False`.
    
    
    from google.api_core import operation
    from google.cloud import [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest)
    
    
    def update_network_policy(
        project_id: str, region: str, internet_access: bool, external_ip: bool
    ) -> operation.Operation:
        """
        Updates a network policy in a given network.
    
        Args:
            project_id: name of the project you want to use.
            region: name of the region you want to use. I.e. "us-central1".
            internet_access: should internet access be allowed.
            external_ip: should external IP addresses be assigned.
    
        Returns:
            An operation object representing the started operation. You can call its .result() method to wait for
            it to finish.
        """
    
        client = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[VmwareEngineClient](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html)()
        request = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.UpdateNetworkPolicyRequest.html)()
        request.update_mask = "internetAccess.enabled,externalIp.enabled"
        network_policy = [vmwareengine_v1](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest).[NetworkPolicy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.types.NetworkPolicy.html)()
        network_policy.name = (
            f"projects/{project_id}/locations/{region}/networkPolicies/{region}-default"
        )
        network_policy.vmware_engine_network = f"projects/{project_id}/locations/{region}/vmwareEngineNetworks/{region}-default"
        network_policy.internet_access.enabled = internet_access
        network_policy.external_ip.enabled = external_ip
    
        request.network_policy = network_policy
    
        return client.[update_network_policy](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest/google.cloud.vmwareengine_v1.services.vmware_engine.VmwareEngineClient.html#google_cloud_vmwareengine_v1_services_vmware_engine_VmwareEngineClient_update_network_policy)(request)
    
    

**If using a Legacy VMware Engine network:** enable **VPC service controls** on the VPC peering connection between your VPC network and VMware Engine using the [`gcloud services vpc-peerings enable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls):
    
    
    gcloud services vpc-peerings enable-vpc-service-controls \
       --network=VPC_NETWORK \
       --service=servicenetworking.googleapis.com

If using a legacy Google Cloud VMware Engine network, you must enable VPC Service Controls to route legacy VEN internet access through either an on-premises connection or VPC in your project. This requirement applies only to legacy Google Cloud VMware Engine networks, rather than standard VENs.

When you enable VPC Service Controls, Google Cloud makes the following routing changes in the service producer VPC network (in this case, the service tenant project peered with VMware Engine):

  * Removes the IPv4 default route (destination `0.0.0.0/0`, next hop default internet gateway).
  * Begins forwarding internet traffic using the VPC peering default route.



Example:

To enable VPC Service Controls for a connection peering a network named "my-network" on the current project, use the [`gcloud services vpc-peerings enable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls):
    
    
    gcloud services vpc-peerings enable-vpc-service-controls \
        --network=my-network \
        --service=servicenetworking.googleapis.com

**Note:** When routing internet traffic through an on-premises connection, consider the following: 

  * You must run the `gcloud services vpc-peerings enable-vpc-service-controls` command from the project that owns the network and the peering connection called `servicenetworking.googleapis.com`, which is peered for accessing VMware Engine private cloud resources. If you use Shared VPC, you must run the command from the host project that owns the Shared VPC and not from the service projects from where VMware Engine private clouds were created.
  * When a default route (`0.0.0.0/0`) is advertised from on-premises, VMware Engine forwards internet traffic through the on-premises connection whether you enable **Internet access** or not. To forward traffic through the VMware Engine internet access service, don't advertise the default route from on-premises over an on-premises connection (Cloud VPN or Cloud Interconnect).
  * If you use Apigee with VPC peering on the same VPC network as VMware Engine, following the guidance in this section to route internet traffic through an on-premises connection also routes Apigee outbound communication through your on-premises connection. As a result, Apigee no longer uses its configured external IP address for outbound communication to external API backend services, and you must update any firewall configurations that rely on Apigee's external IP address.



### Disable routing internet traffic through an on-premises connection

To disable routing internet traffic from your workload VMs through an on-premises connection, stop advertising the default route (`0.0.0.0/0`) and disable VPC Service Controls on the VPC peering connection.

**If using a Legacy VMware Engine network:** disable VPC Service Controls on the VPC peering connection between your VPC network and VMware Engine, use the [`gcloud services vpc-peerings disable-vpc-service-controls` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/disable-vpc-service-controls):
    
    
    gcloud services vpc-peerings disable-vpc-service-controls \
        --network=VPC_NETWORK_NAME \
        --service=servicenetworking.googleapis.com

**Note:** If you disable VPC Service Controls on the VPC peering connection, internet access by using an on-premises connection fails, even if the default route is advertised and propagated over the VPC peering connection.

## What's next

  * Learn how to allocate a [public IP address](https://docs.cloud.google.com/vmware-engine/docs/concepts-public-ip-address) for a VM in your private cloud.
  * Learn how [external access rules](https://docs.cloud.google.com/vmware-engine/docs/networking/external-access-rules) filter network traffic to and from private cloud resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
