---
url: https://docs.cloud.google.com/compute/docs/instances/view-network-properties/
title: View the network configuration for an instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:26:52.394797+00:00
---

# View the network configuration for an instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-network-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View the network configuration for an instance Stay organized with collections  Save and categorize content based on your preferences. 

Use the instructions on this page to view the network interfaces, networks, subnets, and IP addresses for a compute instance.

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




### Required roles

To get the permissions that you need to view the network configuration for an instance, ask your administrator to grant you the Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) or Compute Network Admin (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view the network configuration for an instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view the network configuration for an instance:

  * View network configuration for an instance: `compute.instances.get` on the instance 
  * View IP addresses for an instance: `compute.instances.list` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View IP addresses

You can view the internal and external IP addresses for your instance. The [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses) can be either IPv4 or IPv6 addresses.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Optional: Use the filter_list **Filter** box to restrict the number of instances shown.

  3. If the instance has an external IP address, it appears under the **External IP** column.

If the **External IP** column is empty, then there is no external IP address for the instance. If the instance doesn't have an external IP address, then you can [assign one](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign).




![VM instances page showing internal and external IPs.](https://docs.cloud.google.com/static/compute/images/ips_screenshot.png)

Depending on the column display options, you might see more columns or fewer columns than appear in the previous image.

###  gcloud 

There are two commands you can use to view the IP addresses for an instance:

  * `gcloud compute instances list` shows all IP addresses used by a compute instance, either static or ephemeral.
  * `gcloud compute addresses list` shows all the reserved IP addresses that are assigned to a compute instance.



This task shows how to view IP addresses using `gcloud compute instances` commands.

  1. To view the internal and external IP addresses for your instances use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list).
         
         gcloud compute instances list

You can append the `--filter` clause to restrict the number of instances returned by the command, for example, `--filter='zone:us-central1-c'`.

The output is similar to the following:
         
         NAME           ZONE            MACHINE_TYPE    PREEMPTIBLE  INTERNAL_IP                EXTERNAL_IP                     STATUS
         webapp1        us-central1-c   c3-highmem-88   true         192.0.2.11                                                 RUNNING
         my-instance    us-central1-c   n4-standard-2                192.0.2.126                203.0.113.6                     RUNNING
         my-dual-stack  us-central1-a   e2-micro                     192.0.2.54                 203.0.113.7                     RUNNING
                                                                                               2001:db8:2:2:2:2:2:2/96
         new-ipv6-only  us-central1-a   n4-standard-2                2001:db8:1:1:1:1:1:1/96                                    RUNNING
         

If the External IP address field is empty, then there is no defined IP address of that type for the instance; you can [assign one](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign).

  2. To view the internal or external IP address for a specific instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with a `--format` flag to filter the output.

### Internal addresses

To view the internal IP address for a specific instance, use either of the following commands:

     * IPv4 addresses:
           
           gcloud compute instances describe INSTANCE_NAME \
                  --zone=ZONE \
                  --format='get(networkInterfaces[0].networkIP)'
             
           
           192.0.2.11

     * IPv6 addresses:
           
           gcloud compute instances describe INSTANCE_NAME \
                  --zone=ZONE \
                  --format='get(networkInterfaces[0].ipv6Address)'
             
           
           2001:db8:2:2:2:2:2:2

### External addresses

To view the external IP address for a specific instance, use either of the following commands:

     * IPv4 addresses:
           
           gcloud compute instances describe INSTANCE_NAME \
                  --zone=ZONE \
                  --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
             
           
           203.0.113.6

     * IPv6 addresses:
           
           gcloud compute instances describe INSTANCE_NAME \
                  --zone=ZONE \
                  --format='get(networkInterfaces[0].ipv6AccessConfigs[0].externalIpv6)'
             
           
           2001:db8:3:3:3:3:3:3

Replace the following:

     * `INSTANCE_NAME`: the name of the instance whose internal or external IP you want to view
     * `ZONE`: the name of the zone where the instance is located

If the command doesn't return an IP address, then the instance doesn't have an external IP address configured.




###  REST 

Make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get). By appending a `$fields` query parameter to the request, you can restrict the output to just the fields of interest.
    
    
     GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/INSTANCE_NAME$fields=name,networkInterfaces.networkIP,networkInterfaces.accessConfigs.natIP,networkInterfaces.ipv6AccessConfigs.externalIpv6
     

Replace the following:

  * `PROJECT_NAME`: the name of the project that contains the instance
  * `ZONE`: the zone for the instance that you want to query
  * `INSTANCE_NAME`: the name of the instance resource to return



If any of the IP addresses are not configured, then that field doesn't appear in the output. For a compute instance that uses a dual-stack network with an external IPv6 address, your response body resembles the following:
    
    
    {
      "name": "my-dual-stack-vm",
      "networkInterfaces": [
        {
          "networkIP": "10.0.0.2",
          "accessConfigs": [
            {
              "natIP": "104.155.21.204"
            }
          ],
          "ipv6AccessConfigs": [
            {
              "externalIpv6": "2600:1900:4010:8b2:0:0:0:0"
            }
          ]
        }
      ]
    }
    

The following fields contain the required information:

  * `networkIP`: the assigned internal IPv4 address
  * `natIP`: the assigned external IPv4 address
  * `externalIpv6`: the assigned external IPv6 address



###  Python 
    
    
    from enum import Enum
    from typing import List
    
    from google.cloud import compute_v1
    
    
    def get_instance(project_id: str, zone: str, instance_name: str) -> compute_v1.Instance:
        """
        Get information about a VM instance in the given zone in the specified project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            instance_name: name of the VM instance you want to query.
        Returns:
            An Instance object.
        """
        instance_client = compute_v1.InstancesClient()
        instance = instance_client.get(
            project=project_id, zone=zone, instance=instance_name
        )
    
        return instance
    
    
    class IPType(Enum):
        INTERNAL = "internal"
        EXTERNAL = "external"
        IP_V6 = "ipv6"
    
    
    def get_instance_ip_address(
        instance: compute_v1.Instance, ip_type: IPType
    ) -> List[str]:
        """
        Retrieves the specified type of IP address (ipv6, internal or external) of a specified Compute Engine instance.
    
        Args:
            instance (compute_v1.Instance): instance to get
            ip_type (IPType): The type of IP address to retrieve (ipv6, internal or external).
    
        Returns:
            List[str]: Requested type IP addresses of the instance.
        """
        ips = []
        if not instance.network_interfaces:
            return ips
        for interface in instance.network_interfaces:
            if ip_type == IPType.EXTERNAL:
                for config in interface.access_configs:
                    if config.type_ == "ONE_TO_ONE_NAT":
                        ips.append(config.nat_i_p)
            elif ip_type == IPType.IP_V6:
                for ipv6_config in getattr(interface, "ipv6_access_configs", []):
                    if ipv6_config.type_ == "DIRECT_IPV6":
                        ips.append(ipv6_config.external_ipv6)
    
            elif ip_type == IPType.INTERNAL:
                # Internal IP is directly available in the network interface
                ips.append(interface.network_i_p)
        return ips
    
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html);
    import com.google.cloud.compute.v1.[AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html).Type;
    import com.google.cloud.compute.v1.[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class GetVmAddress {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Instance ID of the Google Cloud project you want to use.
        String instanceId = "your-instance-id";
        // IPType you want to search.
        IpType ipType = IpType.INTERNAL;
    
        getVmAddress(projectId, instanceId, ipType);
      }
    
      // Retrieves the specified type of IP address
      // (ipv6, internal or external) of a specified Compute Engine instance.
      public static List<String> getVmAddress(String projectId, String instanceId, IpType ipType)
              throws IOException {
        List<String> result = new ArrayList<>();
        [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = getInstance(projectId, instanceId);
    
        for ([NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html) networkInterface : instance.[getNetworkInterfacesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getNetworkInterfacesList__)()) {
          if (ipType == IpType.EXTERNAL) {
            for ([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) accessConfig : networkInterface.getAccessConfigsList()) {
              if (accessConfig.getType().equals(Type.ONE_TO_ONE_NAT.name())) {
                result.add(accessConfig.getNatIP());
              }
            }
          } else if (ipType == IpType.IP_V6) {
            for ([AccessConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AccessConfig.html) accessConfig : networkInterface.getAccessConfigsList()) {
              if (accessConfig.hasExternalIpv6()
                      && accessConfig.getType().equals(Type.DIRECT_IPV6.name())) {
                result.add(accessConfig.getExternalIpv6());
              }
            }
          } else if (ipType == IpType.INTERNAL) {
            result.add(networkInterface.getNetworkIP());
          }
        }
    
        return result;
      }
    
      private static [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) getInstance(String projectId, String instanceId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
          [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html) request = [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html).newBuilder()
                  .setInstance(instanceId)
                  .setProject(projectId)
                  .setZone("us-central1-b")
                  .build();
          return instancesClient.get(request);
        }
      }
    
      public enum IpType {
        INTERNAL("internal"),
        EXTERNAL("external"),
        IP_V6("ipv6");
    
        private final String type;
    
        IpType(String type) {
          this.type = type;
        }
    
        public String getType() {
          return type;
        }
      }
    }

## View network interfaces for an instance

Each compute instance has at least one virtual network interface (vNIC), and each network interface uses a unique subnet in a VPC network. You can view the configured network interfaces, Dynamic Network Interfaces (NICs), and properties of the network interfaces for an instance using the following methods.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Optional: Use the filter_list **Filter** box to restrict the number of instances shown.

  3. Click the name of the instance that you want to inspect.

  4. In the **Networking** section, under **Network interfaces** , you can see the following:

     * Network interface (NIC) names for the instance, for example `nic0` or `nic0.14`
     * The VPC network and subnet associated with each NIC
     * VLAN ID for Dynamic NIC
     * Network interface type
     * Primary internal and external IP address
     * IP stack type

![The network interfaces section of the VM instance details page.](https://docs.cloud.google.com/static/compute/docs/networking/console-network-interfaces.png)

  5. You can click the name of a NIC to open the **Network interface details** page. On this page, you can see the firewalls and routes used by the NIC and also perform a connectivity test for the NIC.




###  gcloud 

To view the network interfaces (NICs) for a compute instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe). You can append a `--format` option to the command to restrict the information returned to specific fields and change how it is displayed, for example:
    
    
    gcloud compute instances describe INSTANCE_NAME --zone=ZONE \
        --format="flattened(name,networkInterfaces[].name, networkInterfaces[].network.basename(), networkInterfaces[].stackType, networkInterfaces[].nicType)"
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to view
  * `ZONE`: the zone for the instance that you want to view



The output is similar to the following:
    
    
    name:                           test-instance
    networkInterfaces[0].name:      nic0
    networkInterfaces[0].network:   default
    networkInterfaces[0].nicType:   GVNIC
    networkInterfaces[0].stackType: IPV4_ONLY
    networkInterfaces[1].name:      nic1
    networkInterfaces[1].network:   prod-ipv6
    networkInterfaces[1].nicType:   GVNIC
    networkInterfaces[1].stackType: IPV4_IPV6
    networkInterfaces[1].name:      nic1.2
    networkInterfaces[1].network:   alt-ipv6-net
    networkInterfaces[1].nicType:   GVNIC
    networkInterfaces[1].stackType: IPV4_IPV6
    networkInterfaces[1].parentNicName: nic1
    

###  REST 

Construct a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get). By appending a `$fields` query parameter to the request, you can restrict the output to just the `networkInterfaces` property.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: ID of the project that contains the instance
  * `ZONE`: zone of the instance
  * `INSTANCE_NAME`: the name of the instance



HTTP method and URL: 
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?fields=networkInterfaces

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?fields=networkInterfaces"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?fields=networkInterfaces" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "networkInterfaces": [
      {
        "kind": "compute#networkInterface",
        "network": "https://www.googleapis.com/compute/v1/projects/my-project/global/networks/network-name-1",
        "subnetwork": "https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/subnet-name-1",
        "networkIP": "10.128.0.15",
        "name": "nic0",
        "accessConfigs": [
          {
            "kind": "compute#accessConfig",
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT",
            "networkTier": "PREMIUM"
          }
        ],
        "fingerprint": "mBy9xvkWA9M=",
        "stackType": "IPV4_ONLY",
        "nicType": "GVNIC"
      },
      {
        "kind": "compute#networkInterface",
        "network": "https://www.googleapis.com/compute/v1/projects/my-project/global/networks/network-name-2",
        "subnetwork": "https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/subnet-name-2",
        "networkIP": "10.0.20.2",
        "name": "nic1",
        "accessConfigs": [
          {
            "kind": "compute#accessConfig",
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT",
            "networkTier": "PREMIUM"
          }
        ],
        "ipv6AccessConfigs": [
          {
            "kind": "compute#accessConfig",
            "type": "DIRECT_IPV6",
            "name": "external-ipv6",
            "externalIpv6": "2600:1900:4000:8447:0:0:0:0",
            "externalIpv6PrefixLength": 96,
            "publicPtrDomainName": "",
            "networkTier": "PREMIUM"
          }
        ],
        "fingerprint": "rx6hfNA94f4=",
        "stackType": "IPV4_IPV6",
        "ipv6AccessType": "EXTERNAL",
        "nicType": "GVNIC",
        "parentNicName": "nic1"
      },
      {
        "kind": "compute#networkInterface",
        "network": "https://www.googleapis.com/compute/v1/projects/my-project/global/networks/network-name-3",
        "subnetwork": "https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/subnet-name-3",
        "networkIP": "10.0.26.2",
        "name": "nic1.1",
        "accessConfigs": [
          {
            "kind": "compute#accessConfig",
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT",
            "networkTier": "PREMIUM"
          }
        ],
        "ipv6AccessConfigs": [
          {
            "kind": "compute#accessConfig",
            "type": "DIRECT_IPV6",
            "name": "external-ipv6",
            "externalIpv6": "2600:1900:4000:8450:0:0:0:0",
            "externalIpv6PrefixLength": 96,
            "publicPtrDomainName": "",
            "networkTier": "PREMIUM"
          }
        ],
        "fingerprint": "rx6hfNA94f4=",
        "stackType": "IPV4_IPV6",
        "ipv6AccessType": "EXTERNAL",
        "nicType": "GVNIC",
        "parentNicName": "nic1"
      }
      ]
    }
    

## View all compute instances within a network

Use one of the following methods to view all compute instances within a certain network.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networks/list)

  2. Optional: Use the filter_list **Filter** box to restrict the number of networks shown.

  3. Click the name of the network for which you want to list the compute instances.

  4. Select the **Instances** tab to view the instances within that network.




###  gcloud 

To view the compute instances that use a specific network, use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list).

Use a `--filter` flag to list only the instances that use a specific network. You can also use a `--format` flag to restrict and format the results, for example:
    
    
    gcloud compute instances list \
        --filter 'networkInterfaces[].network:NETWORK_NAME' \
        --format="table(name:sort=1,machineType.basename(),zone.basename(),networkInterfaces[].subnetwork)"
    

The output is similar to the following:
    
    
    NAME: c2-tier1-multinic
    MACHINE_TYPE: c2-standard-30
    ZONE: us-central1-c
    SUBNETWORK: ['https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/default', 'https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/webapps-external-subnet']  
    
    NAME: c3-with-lssd
    MACHINE_TYPE: c3-standard-4-lssd
    ZONE: us-central1-a
    SUBNETWORK: ['https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/default']  
    
    NAME: example-instance3
    MACHINE_TYPE: n2-custom-2-163840-ext
    ZONE: us-central1-b
    SUBNETWORK: ['https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/default']  
    
    NAME: n4-test-windows
    MACHINE_TYPE: n4-standard-2
    ZONE: us-central1-c
    SUBNETWORK: ['https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/default']
    

## Determine if Tier_1 networking is enabled

Use one of the following methods to determine if per VM Tier_1 networking performance is enabled for an instance.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Optional: Use the filter_list **Filter** box to restrict the number of instances shown.

  3. Click the name of the instance that you want to inspect.

  4. In the **Networking** section, check the value for **Total egress bandwidth tier** :

     * `TIER_1`: Tier_1 networking is enabled.
     * `-`: Tier_1 networking is not enabled.



###  gcloud 

To view the `networkPerformanceConfig` setting for an instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe). You can append a `--format` option to the command to restrict the information returned to specific fields and change how it is displayed, for example:
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --zone=ZONE \
        --format="text(name, networkPerformanceConfig)"
    

If Tier_1 networking is not configured for the instance, then the `networkPerformanceConfig` field is not included in the output. If Tier_1 networking is enabled for an instance, then the output is similar to the following:
    
    
    name:                                              c2-tier1-multinic
    networkPerformanceConfig.totalEgressBandwidthTier: TIER_1
    

###  REST 

Construct a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get). By appending a `$fields` query parameter to the request, you can restrict the output to just the `name`, `networkPerformanceConfig`, and `nicType` fields.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/INSTANCE_NAME?$fields=name,networkPerformanceConfig,networkInterfaces.nicType
    

Replace the following:

  * `PROJECT_NAME`: the name of the project that contains the instance
  * `ZONE`: the zone for the instance that you want to query
  * `INSTANCE_NAME`: the name of the instance resource to return



If Tier_1 networking is not configured for the instance, then the `networkPerformanceConfig` field is not included in the output. If Tier_1 networking is enabled for an instance, then the output is similar to the following:
    
    
    {
      "name": "c2-tier1-multinic",
      "networkInterfaces": [
        {
          "nicType": "GVNIC"
        },
        {
          "nicType": "GVNIC"
        }
      ],
      "networkPerformanceConfig": {
        "totalEgressBandwidthTier": "TIER_1"
      }
    }
    

## What's next

  * Learn about Compute Engine network interface and IP address concepts in [Networking overview for VMs](https://docs.cloud.google.com/compute/docs/networking/network-overview)
  * [Create VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)
  * [Benchmark higher network bandwidth for VM instances](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms)
  * [Optimize application latency with load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
