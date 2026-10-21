---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/ErrorReason/
title: ErrorReason \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:22.195715+00:00
---

# ErrorReason  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/ErrorReason/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  ErrorReason Stay organized with collections  Save and categorize content based on your preferences. 

Defines the supported values for `google.rpc.ErrorInfo.reason` for the `vmwareengine.googleapis.com` error domain. Values contained in this enum are read-only and are included in the API response when the server encounters an error. Use the machine-readable `reason` field to identify and handle errors, as the associated human-readable error message might change over time. Each `ErrorInfo` object has an associated `metadata` field that contains additional parameters of the error, and a `domain` field that identifies the source of the error.

Enums  
---  
`ERROR_REASON_UNSPECIFIED` | Do not use this default value.  
`NETWORK_POLICY_NOT_CONFIGURED` | Issuing a request which requires network policy to be configured for the VMware Engine network while it is not configured. For example, attempting to reserve an external IP address when no network policy is configured for the VMware Engine network in the region.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_POLICY_NOT_CONFIGURED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`RESOURCE_HAS_NESTED_RESOURCES` | Issuing a request to delete the resource while it has nested resources. Before you delete a resource, you must delete all nested resources.A sample `ErrorInfo` object:
    
    
    {
      "reason": "RESOURCE_HAS_NESTED_RESOURCES",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "resourceType": "PrivateCloud",
         "nestedResourceType": "ExternalAddress"
       }
    }
      
  
`EXTERNAL_IP_ADDRESS_SERVICE_NOT_ACTIVE` | Issuing a request which requires the external IP address network service to be enabled while the service is disabled or not active. For example, attempting to reserve an external IP address for a private cloud's workload VM when the external IP address network service is disabled in the corresponding network policy.A sample `ErrorInfo` object:
    
    
    {
      "reason": "EXTERNAL_IP_ADDRESS_SERVICE_NOT_ACTIVE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`RESOURCE_IS_BEING_DELETED` | Issuing a request to delete resource while it is being deleted.A sample `ErrorInfo` object:
    
    
    {
      "reason": "RESOURCE_IS_BEING_DELETED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "resourceType": "PrivateCloud"
       }
    }
      
  
`NETWORK_PEERING_NOT_ALLOWED` | Issuing a request to create a service tenant network when network peering is not allowed in this project. For more information, contact support with your project ID and the API response: <https://cloud.google.com/vmware-engine/docs/getting-support>.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_PEERING_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`RESOURCE_IS_BEING_MODIFIED` | Issuing a request to modify a resource while it is being modified.A sample `ErrorInfo` object:
    
    
    {
      "reason": "RESOURCE_IS_BEING_MODIFIED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "resourceType": "PrivateCloud"
       }
    }
      
  
`NETWORK_SERVICE_IN_RECONCILING_STATE` | Request to delete or update a network policy when its services are in the `RECONCILING` state. Network policy can be modified after the reconciling will finish and the state of the network policy will be updated.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_SERVICE_IN_RECONCILING_STATE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`EXTERNAL_ADDRESSES_EXIST` | Issuing a request to delete a network policy or disable its external IP address network service while dependent external IP addresses still exist. For example, attempting to delete a network policy when reserved external IP addresses exist. Release all reserved external IP addresses from private clouds that use a network policy before attempting to delete the policy.A sample `ErrorInfo` object:
    
    
    {
      "reason": "EXTERNAL_ADDRESSES_EXIST",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`RESOURCE_STATE_DISALLOWS_REQUEST` | The resource state does not allow the operation to be fulfilled. For example, attempting to fetch credentials when the private cloud is in an invalid state or not in the required state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "RESOURCE_STATE_DISALLOWS_REQUEST",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "resourceType": "PrivateCloud"
         "allowedStates": "ACTIVE,UPDATING"
       }
    }
      
  
`RESOURCE_HAS_NESTED_RESOURCES_FORCE_SUPPORTED` | Issuing a request to delete the resource while it has nested resources. Before you delete a resource, you must delete all nested resources or set the `force` parameter to `true` to delete all nested resources at the same time.A sample `ErrorInfo` object:
    
    
    {
      "reason": "RESOURCE_HAS_NESTED_RESOURCES_FORCE_SUPPORTED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "resourceType": "PrivateCloud",
         "nestedResourceType": "Cluster"
       }
    }
      
  
`EXTERNAL_ADDRESS_NOT_CONFIGURED` | Issuing a request to create or update an external access rule, while an item in `destinationIpRanges` doesn't have a corresponding external address in either `ACTIVE` or `UPDATING` state in the scope of the parent network policy. Before you continue, create an `ExternalAddress` resource in the private cloud that assigns a workload VM to the destination IP address you want to use.A sample `ErrorInfo` object:
    
    
    {
      "reason": "EXTERNAL_ADDRESS_NOT_CONFIGURED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "ipRangeKind": "IP_ADDRESS",
         "ipRangeValue": "192.168.100.100"
       }
    }
      
  
`LEGACY_VMWARE_ENGINE_NETWORK_TYPE_NOT_ALLOWED` | Legacy VMware Engine network creation is not allowed on this project. Use a Standard VMware Engine network instead. Reason 1: Standard VMware Engine network is present in the project. Reason 2: Migration is complete and there is no existing Legacy VMware Engine network, or it's the first VMware Engine network.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LEGACY_VMWARE_ENGINE_NETWORK_TYPE_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`STANDARD_VMWARE_ENGINE_NETWORK_TYPE_NOT_ALLOWED` | Requesting to create a standard VMware Engine network which is not allowed because a legacy VMware Engine network is present in the project.A sample `ErrorInfo` object:
    
    
    {
      "reason": "STANDARD_VMWARE_ENGINE_NETWORK_TYPE_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`REFERENCED_LEGACY_VMWARE_ENGINE_NETWORK_NOT_SUPPORTED` | Issuing a request to perform an operation on a resource not supported by VMware Engine networks of type `LEGACY`. Provide a VMware Engine network of type `STANDARD` when performing this operation.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_LEGACY_VMWARE_ENGINE_NETWORK_NOT_SUPPORTED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "vmwareEngineNetworkName":
         "projects/56743/locations/global/vmwareEngineNetworks/my-ven"
         "resourceType": "NetworkPeering"
       }
    }
      
  
`REFERENCED_VMWARE_ENGINE_NETWORK_NOT_FOUND` | Issuing a request to perform an operation on a resource and referencing a VMware Engine network that doesn't exist.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_VMWARE_ENGINE_NETWORK_NOT_FOUND",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "vmwareEngineNetworkName":
         "projects/56743/locations/global/vmwareEngineNetworks/my-ven",
         "resourceType": "NetworkPeering"
       }
    }
      
  
`REFERENCED_VMWARE_ENGINE_NETWORK_INVALID_STATE` | Issuing a request that can't be fulfilled due to the state of the VMware Engine network.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_VMWARE_ENGINE_NETWORK_INVALID_STATE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "vmwareEngineNetworkName":
         "projects/56743/locations/global/vmwareEngineNetworks/my-ven",
         "resourceType": "NetworkPeering",
         "allowedStates": "ACTIVE,CREATING,UPDATING"
       }
    }
      
  
`RESOURCE_IS_REFERENCED` | Issuing a request to delete the resource while it is currently being referenced by other resources. Before you delete a resource, you must delete all referencing resources.A sample `ErrorInfo` object:{ "reason": "RESOURCE_IS_REFERENCED", . "domain": "vmwareengine.googleapis.com", "metadata": { . "resourceName": "VmwareEngineNetwork", "referencingResourceNames": "PrivateCloud,NetworkPeering" } }  
`MULTIPLE_LEGACY_VMWARE_ENGINE_NETWORKS_IN_REGION_NOT_ALLOWED` | Requesting to create a legacy VMware Engine network which is not allowed because a legacy network is already present in same region in the project.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "MULTIPLE_LEGACY_VMWARE_ENGINE_NETWORKS_IN_REGION_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`LEGACY_FIREWALL_TABLES` | Issuing a request to create a new external access firewall rule in a project that already has legacy firewall tables.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LEGACY_FIREWALL_TABLES",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`NO_RULE_DESTINATION_EXISTS` | Issuing a request to create or update an external access firewall rule with a destination IP range of `0.0.0.0/0` when no value can be inferred from external IP addresses. To be inferred as a destination IP address, an external IP address resource must be in either the `ACTIVE` or `UPDATING` state and in the scope of the same parent network policy.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NO_RULE_DESTINATION_EXISTS",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`NETWORK_PEERING_EXISTS` | Issuing a request to create a network peering that describes the same peer network and VMware Engine relationship as another network peering in the project.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_PEERING_EXISTS",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "networkPeeringName":
         "projects/56743/locations/global/networkPeerings/my-peering"
       }
    }
      
  
`PEERING_NOT_POSSIBLE_BETWEEN_INACCESSIBLE_NETWORKS` | Issuing a request to create a network peering between Peer Network and VMware Engine network that are not accessible.A sample `ErrorInfo` object:
    
    
    {
      "reason": "PEERING_NOT_POSSIBLE_BETWEEN_INACCESSIBLE_NETWORKS",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`PEERING_NOT_POSSIBLE_DUE_TO_IP_RANGE_OVERLAP` | Issuing a request to create a network peering between a peer network and VMware Engine network that have allocated one or more overlapping IP address ranges.A sample `ErrorInfo` object:
    
    
    {
      "reason": "PEERING_NOT_POSSIBLE_DUE_TO_IP_RANGE_OVERLAP",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`NETWORK_POLICY_FOR_VMWARE_ENGINE_NETWORK_IN_REGION_EXISTS` | Creating a network policy in a VMware Engine network in a region where another network policy already exists.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "NETWORK_POLICY_FOR_VMWARE_ENGINE_NETWORK_IN_REGION_EXISTS",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`MANAGEMENT_DNS_ZONE_BINDING_DISALLOWED_FOR_NON_PEERED_NETWORK` | Issuing a request to create a management DNS zone binding for a network that is not peered to private cloud's vmware engine network.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "MANAGEMENT_DNS_ZONE_BINDING_DISALLOWED_FOR_NON_PEERED_NETWORK",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`REFERENCED_STANDARD_VMWARE_ENGINE_NETWORK_NOT_SUPPORTED` | Issuing a request to perform an operation on a resource not supported by VMware Engine networks of type `STANDARD`. Provide a VMware Engine network of type `LEGACY` when performing this operation.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_STANDARD_VMWARE_ENGINE_NETWORK_NOT_SUPPORTED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "vmwareEngineNetworkName":
         "projects/56743/locations/us-central1/vmwareEngineNetworks/us-central1-default"
         "resourceType": "PrivateConnection"
       }
    }
      
  
`MANAGEMENT_IPS_FIREWALL_RULE_NOT_ALLOWED` | Firewall rule cannot allow traffic into management IP addresses from `any` source IP or to a non-HTTPS destination port.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "MANAGEMENT_IPS_FIREWALL_RULE_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`MANAGEMENT_DNS_ZONE_NETWORK_BINDING_EXISTS` | Issuing a request to create a management DNS zone binding for a network that is already bound to the management DNS zone.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "MANAGEMENT_DNS_ZONE_NETWORK_BINDING_EXISTS",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`REGIONAL_ROUTING_MODE_NOT_SUPPORTED` | Issuing a request for a private connection with routing mode `REGIONAL` and type that is not `PRIVATE_SERVICE_ACCESS`.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "REGIONAL_ROUTING_MODE_NOT_SUPPORTED",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`PEERED_VPC_PER_REGION_QUOTA_REACHED` | Issuing a request for a new private connection when the number of peerable VPCs exceeds the quota assigned.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "PEERED_VPC_PER_REGION_QUOTA_REACHED",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`STANDARD_VEN_DOES_NOT_EXIST` | When standard VEN is a prerequisite for the operation but it is not present.A sample `ErrorInfo` object:
    
    
    {
      "reason":
      "STANDARD_VEN_DOES_NOT_EXIST",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`PROJECT_NOT_MIGRATED` | The project needs to be migrated to Pantheon UI.A sample `ErrorInfo` object:
    
    
    {
      "reason": "PROJECT_NOT_MIGRATED",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`SERVICE_DISABLED` | The request is calling a disabled service for a consumer.Example of an ErrorInfo when the consumer "projects/123" is contacting "vmwareengine.googleapis.com" service which is disabled:
    
    
    { "reason": "SERVICE_DISABLED",
      "domain": "googleapis.com",
      "metadata": {
        "project": "projects/123",
        "service": "vmwareengine.googleapis.com"
      }
    }
    

This response indicates the "vmwareengine.googleapis.com" has been disabled in "projects/123".  
`DNS_FORWARDING_LEGACY_NETWORK_REQUIRED` | DNS forwarding requires a VMware Engine network of type `LEGACY`After you grant your user principal DNS bind permission, then you can bind your DNS zones in Cloud DNS to the Standard VMware Engine network intranet VPC.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DNS_FORWARDING_LEGACY_NETWORK_REQUIRED",
      "domain": "vmwareengine.googleapis.com",
    }
      
  
`INCORRECT_LOGGING_SERVER_PARAMETERS` | Provided logging server config parameters are incorrect.A sample `ErrorInfo` object:
    
    
    {
      "reason": "INCORRECT_LOGGING_SERVER_PARAMETERS",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`LOGGING_SERVER_INVALID_PROTOCOL` | Provided logging server protocol is invalid.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LOGGING_SERVER_INVALID_PROTOCOL",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`LOGGING_SERVER_HOSTNAME_NOT_REACHABLE` | Provided logging server hostname or IP is not reachable.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LOGGING_SERVER_HOSTNAME_NOT_REACHABLE",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`LOGGING_SERVER_HOSTNAME_AND_PORT_NOT_REACHABLE` | Provided logging server hostname and port aren't reachable.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LOGGING_SERVER_HOSTNAME_NOT_REACHABLE",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`CLUSTER_DRS_RULES_VIOLATION` | Updating the cluster would violate its DRS rules.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_DRS_RULES_VIOLATION",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`CLUSTER_INSUFFICIENT_STORAGE_CAPACITY` | Updating the cluster would make the storage capacity insufficient to meet the SLA.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_INSUFFICIENT_STORAGE_CAPACITY",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`CLUSTER_FTT_POLICY_VIOLATION` | Updating the cluster would violate its FTT policies.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_FTT_POLICY_VIOLATION",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`CLUSTER_INVALID_HOSTS_NUMBER` | Updating the cluster would make the number of hosts invalid.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_INVALID_HOSTS_NUMBER",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`NETWORK_POLICY_NOT_ALLOWED_ON_VPC_SC_ENABLED_PROJECTS` | Requesting to create or update Network Policy which is not allowed on VPC-SC enabled projects.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_POLICY_NOT_ALLOWED_ON_VPC_SC_ENABLED_PROJECTS",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`LOGGING_SERVER_NOT_UNIQUE` | The logging server specified is not unique in the private cloud. Please specify a unique logging server.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LOGGING_SERVER_NOT_UNIQUE",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`NETWORK_POLICY_EXISTS_ON_VPC_SC_ENABLED_PROJECT` | Network Policy exists on a VPC-SC enabled project. Delete it before retrying the request.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_POLICY_EXISTS_ON_VPC_SC_ENABLED_PROJECT",
      "domain": "vmwareengine.googleapis.com"
      "metadata": {
         "networkPolicyName":
         "projects/56743/locations/us-west1/networkPolicies/my-policy"
       }
    }
      
  
`NETWORK_POLICY_NOT_ALLOWED` | Issuing a request to create a network policy is not allowed for this project till VMware Engine API is added in the restricted services list in the project's VPC-SC perimeter.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_POLICY_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`PRIVATE_CONNECTION_NOT_ALLOWED` | Issuing a request to create a private connection is not allowed for this project till VMware Engine API is added in the restricted services list in the project's VPC-SC perimeter.A sample `ErrorInfo` object:
    
    
    {
      "reason": "PRIVATE_CONNECTION_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`RESOURCE_STATE_NOT_VALID` | The state of the resource is invalid for this operation.A sample `ErrorInfo` object:
    
    
    {
      "reason": "RESOURCE_STATE_NOT_VALID",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`CUSTOMER_ONBOARDING_IN_PROGRESS` | Customer onboarding is in progress. Please wait for it to finish.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CUSTOMER_ONBOARDING_IN_PROGRESS",
      "domain": "vmwareengine.googleapis.com"
    }
      
  
`SPANNING_PC_CREATION_UNSUPPORTED` | Issuing a request to create a new spanning private cloud or a cluster in a spanning private cloud.A sample `ErrorInfo` object:
    
    
    {
      "reason": "SPANNING_PC_CREATION_UNSUPPORTED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "privateCloudName":
           "projects/56743/locations/us-west1-a/privateClouds/my-pc"
       }
    }
      
  
`WRONG_ZONE_SELECTED_FOR_EARMARKED_PC` | Issuing a request to create a private cloud in a different zone than the zone in which earmarking is done.A sample `ErrorInfo` object:
    
    
    {
      "reason": "WRONG_ZONE_SELECTED_FOR_EARMARKED_PC",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "privateCloudName":
           "projects/56743/locations/us-west1-a/privateClouds/my-pc"
       }
    }
      
  
`NO_EARMARKS_FOR_PC` | Issuing a request to create a private cloud for which no earmarking is done.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NO_EARMARKS_FOR_PC",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "privateCloudName":
           "projects/56743/locations/us-west1-a/privateClouds/my-pc"
       }
    }
      
  
`DNS_BINDINGS_NOT_SUPPORTED_IN_LEGACY_VEN` | Issuing a request to create a management dns zone binding in a private cloud linked to a Vmware Engine Network of type `LEGACY`.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DNS_BINDINGS_NOT_SUPPORTED_IN_LEGACY_VEN",
      "domain": "vmwareengine.googleapis.com",
    }
      
  
`STRETCH_PC_NOT_ALLOWED` | Stretched private cloud creation is not allowed in projects without the gcp.requiresPhysicalZoneSeparation organizational policy constraint set to true.A sample `ErrorInfo` object:
    
    
    {
      "reason": "STRETCH_PC_NOT_ALLOWED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`IP_PLAN_NODE_LIMIT_EXCEEDED` | IP plan node limit exceeded.A sample `ErrorInfo` object:
    
    
    {
      "reason": "IP_PLAN_NODE_LIMIT_EXCEEDED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`CLUSTER_AND_DATASTORE_IN_DIFFERENT_LOCATIONS` | Cluster and Datastore are in different locations.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_AND_DATASTORE_IN_DIFFERENT_LOCATIONS",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`CLUSTER_AND_NFS_VOLUME_IN_DIFFERENT_LOCATIONS` | Cluster and NFS volume are in different locations.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_AND_NFS_VOLUME_IN_DIFFERENT_LOCATIONS",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`REFERENCED_DATASTORE_NOT_FOUND` | Datastore does not exist.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_DATASTORE_NOT_FOUND",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "datastoreName":
           "projects/56743/locations/us-west1/datastores/my-datastore"
       }
    }
      
  
`REFERENCED_DATASTORE_INVALID_STATE` | Datastore is in an invalid state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_DATASTORE_INVALID_STATE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "datastoreName":
           "projects/56743/locations/us-west1/datastores/my-datastore"
           "allowedStates": "ACTIVE,CREATING,UPDATING"
       }
    }
      
  
`DATASTORE_ALREADY_CONFIGURED` | A datastore with the same configuration already exists.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DATASTORE_ALREADY_CONFIGURED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`DATASTORE_AND_NFS_VOLUME_IN_DIFFERENT_LOCATIONS` | Datastore and NFS volume are in different locations.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DATASTORE_AND_NFS_VOLUME_IN_DIFFERENT_LOCATIONS",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`LOGGING_SERVER_IP_IN_MANAGEMENT_CIDR` | The logging server specified conflicts with management CIDR.A sample `ErrorInfo` object:
    
    
    {
      "reason": "LOGGING_SERVER_IP_IN_MANAGEMENT_CIDR",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {}
    }
      
  
`INCORRECT_VPC_NAME` | Incorrect VPC Name for the given Peer Type.A sample `ErrorInfo` object:
    
    
    {
      "reason": "INCORRECT_VPC_NAME",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "peerType": "STANDARD",
       }
    }
      
  
`SUBNET_SIZE_TOO_SMALL` |   
`SUBNET_ALREADY_IN_USE` | Subnet is already in use. Please use a different service subnet.A sample `ErrorInfo` object:
    
    
    {
      "reason": "SUBNET_ALREADY_IN_USE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetName":
           "projects/56743/locations/us-west1/subnets/my-subnet"
       }
    }
      
  
`NETWORK_PEERING_DOES_NOT_EXIST` | Network peering does not exist.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_PEERING_DOES_NOT_EXIST",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "vpcName":
           "projects/56743/global/networks/my-vpc"
           "vmwareEngineNetworkName":
           "projects/56743/locations/global/vmwareEngineNetworks/my-ven"
       }
    }
      
  
`NETWORK_PEERING_IS_INACTIVE` | Network peering is inactive. Mounting needs a network peering in active state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_PEERING_IS_INACTIVE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "networkPeeringName":
           "projects/56743/locations/us-west1/networkPeerings/my-network-peering",
           "networkPeeringStateDetails": "Permission denied on resource
           project 56743"
       }
    }
      
  
`DATASTORE_NOT_MOUNTED` | The unmount operation cannot be performed because datastore is not mounted.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DATASTORE_NOT_MOUNTED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "datastoreName":
           "projects/56743/locations/us-west1/datastores/my-datastore"
       }
    }
      
  
`P4SA_MISSING_PERMISSION_ON_CONSUMER_RESOURCE` | P4SA is missing permission on consumer project.A sample `ErrorInfo` object:
    
    
    {
      "reason": "P4SA_MISSING_PERMISSION_ON_CONSUMER_RESOURCE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "p4saEmail":
           "service-1234567890@gcp-sa-vmwareengine.iam.gserviceaccount.com",
           "permission": "file.instances.get",
           "consumerResource":
           "projects/1234567890/locations/us-west1-a/instances/my-instance"
       }
    }
      
  
`INVALID_PRINCIPAL` | Invalid principal for dns bind permission.A sample `ErrorInfo` object:
    
    
    {
      "reason": "INVALID_PRINCIPAL",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "principalName":
           "serviceAccount:test-sa@test-project.iam.gserviceaccount.com"
       }
    }
    }
      
  
`INVALID_FILESTORE_INSTANCE_STATE` | Filestore instance is in an invalid state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "FILESTORE_INSTANCE_STATE_NOT_VALID",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "resourceName":
           "projects/56743/locations/us-west1/instances/my-nfs-volume",
           "state": "CREATING",
           "allowedStates": "[ACTIVE,READY]"
       }
    }
      
  
`INVALID_NETAPP_VOLUME_STATE` | Netapp volume is in an invalid state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "INVALID_NETAPP_VOLUME_STATE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "resourceName":
           "projects/56743/locations/us-west1/volumes/my-nfs-volume",
           "state": "CREATING",
           "allowedStates": "[ACTIVE,READY]"
       }
    }
      
  
`INVALID_FILESTORE_INSTANCE_NETWORK_MODE` | Filestore instance has an invalid network configuration.A sample `ErrorInfo` object:
    
    
    {
      "reason": "INVALID_FILESTORE_INSTANCE_NETWORK_MODE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "instanceName":
           "projects/56743/locations/us-west1/instances/my-instance",
           "connectModes": "[NONE]"
           "expectedConnectModes": "[PRIVATE_SERVICE_ACCESS]"
       }
    }
      
  
`FILESTORE_INSTANCE_DELETE_PROTECTION_DISABLED` | Filestore instance has delete protection disabled.A sample `ErrorInfo` object:
    
    
    {
      "reason": "FILESTORE_INSTANCE_DELETE_PROTECTION_DISABLED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "instanceName":
           "projects/56743/locations/us-west1/instances/my-instance",
       }
    }
      
  
`NETAPP_VOLUME_DELETE_PROTECTION_DISABLED` | Netapp volume has delete protection disabled.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETAPP_VOLUME_DELETE_PROTECTION_DISABLED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "volumeName":
           "projects/56743/locations/us-west1/volumes/my-volume",
       }
    }
      
  
`UNSUPPORTED_FILESTORE_INSTANCE_NFS_VERSION` | Filestore instance has an invalid NFS versionA sample `ErrorInfo` object:
    
    
    {
      "reason": "UNSUPPORTED_FILESTORE_INSTANCE_NFS_VERSION",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "resourceName":
           "projects/56743/locations/us-west1/instances/my-instance",
           "nfsVersion": "NFS_V4",
           "supportedNfsVersions": "[NFS_V3]"
       }
    }
      
  
`UNSUPPORTED_NETAPP_VOLUME_NFS_VERSION` | Netapp volume has an invalid NFS versionA sample `ErrorInfo` object:
    
    
    {
      "reason": "UNSUPPORTED_NETAPP_VOLUME_NFS_VERSION",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "resourceName":
           "projects/56743/locations/us-west1/volumes/my-volume",
           "nfsVersion": "NFS_V4"
           "supportedNfsVersions": "[NFS_V3]"
       }
    }
      
  
`UNSUPPORTED_FILESTORE_INSTANCE_TIER` | Filestore instance has an unsupported type.A sample `ErrorInfo` object:
    
    
    {
      "reason": "UNSUPPORTED_FILESTORE_INSTANCE_TIER",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "resourceName":
           "projects/56743/locations/us-west1/instances/my-instance",
           "instanceTier": "BASIC_HDD"
           "supportedInstanceTiers": "[BASIC_SSD, HIGH_SCALE_SSD]"
       }
    }
      
  
`UNSUPPORTED_NETAPP_VOLUME_TIER` | Netapp volume has an unsupported type.A sample `ErrorInfo` object:
    
    
    {
      "reason": "UNSUPPORTED_NETAPP_VOLUME_TIER",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "volumeName":
           "projects/56743/locations/us-west1/volumes/my-volume",
           "volumeTier": "FLEX"
           "supportedVolumeTiers": "[STANDARD, EXTREME]"
       }
    }
      
  
`FILESTORE_INSTANCE_DOES_NOT_EXIST` | Filestore instance does not exist.A sample `ErrorInfo` object:
    
    
    {
      "reason": "FILESTORE_INSTANCE_DOES_NOT_EXIST",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "instanceName":
           "projects/56743/locations/us-west1/instances/my-instance",
       }
    }
      
  
`NETAPP_VOLUME_DOES_NOT_EXIST` | netapp volume does not exist.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETAPP_VOLUME_DOES_NOT_EXIST",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "volumeName":
           "projects/56743/locations/us-west1/volumes/my-volume",
       }
    }
      
  
`READ_WRITE_ACCESS_REQUIRED_FOR_NFS_DATASTORE` | NFS Datastore requires READ_WRITE access to FileShare, but only READ_ONLY is granted for the given subnetA sample `ErrorInfo` object:
    
    
    {
      "reason": "READ_WRITE_ACCESS_REQUIRED_FOR_NFS_DATASTORE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetName":
           "projects/56743/locations/us-west1/subnets/my-subnet"
           "subnetCidr": "10.0.0.0/26"
           "fileShareName":
           "projects/56743/locations/us-west1/instances/my-fileshare"
       }
    }
      
  
`NO_ACCESS_ALLOWED_FOR_NFS_DATASTORE` | NFS datastore service subnet is not given permission to access the file shareA sample `ErrorInfo` object:
    
    
    {
      "reason": "NO_ACCESS_ALLOWED_FOR_NFS_DATASTORE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetCidr":
           "10.0.0.0/26"
           "fileShareName":
           "projects/56743/locations/us-west1/instances/my-fileshare"
           "accessMode": "READ_ONLY"
       }
    }
      
  
`REFERENCED_SUBNET_NOT_FOUND` | Subnet does not exist.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_SUBNET_NOT_FOUND",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetName":
           "projects/56743/locations/us-west1/privateClouds/my-pc/subnets/my-subnet"
       }
    }
      
  
`IP_CIDR_NOT_CONFIGURED_FOR_SUBNET` | IP CIDR is not configured for the subnet.A sample `ErrorInfo` object:
    
    
    {
      "reason": "IP_CIDR_NOT_CONFIGURED_FOR_SUBNET",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetName":
           "projects/56743/locations/us-west1/privateClouds/my-pc/subnets/my-subnet"
       }
    }
      
  
`PRIVATE_CLOUD_OPERATION_DISALLOWED_IN_MAINTENANCE` | Private cloud operation is disallowed in maintenance.A sample `ErrorInfo` object:
    
    
    {
      "reason": "PRIVATE_CLOUD_OPERATION_DISALLOWED_IN_MAINTENANCE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "privateCloudName":
           "projects/56743/locations/us-west1/privateClouds/my-pc"
       }
    }
      
  
`UNSUPPORTED_NFS_VERSION_FOR_MOUNT_OPERATION` | NFS Version is not supported for mount operations.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NFS_V4_NOT_SUPPORTED",
      "domain": "vmwareengine.googleapis.com",
       "metadata": {
           "nfsVersion": "NFS_V4",
           "supportedNfsVersions": "[NFS_V3]"
       }
    }
      
  
`REFERENCED_SUBNET_NOT_ACTIVE` | Subnet is not in an active state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_SUBNET_NOT_ACTIVE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetName":
           "projects/56743/locations/us-west1/privateClouds/my-pc/subnets/my-subnet"
       }
    }
      
  
`NETWORK_PEERING_INVALID_ROUTE_CONFIG` | Network peering exchange route config is not set.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NETWORK_PEERING_INVALID_ROUTE_CONFIG",
      "domain": "vmwareengine.googleapis.com",
       "metadata": {
           "resourceName":
           "projects/my-project/locations/global/networkPeerings/my-peering",
           "importCustomRoutes": "false",
           "exportCustomRoutes": "false",
       }
    }
      
  
`ACTIVE_VMS_PRESENT_ON_MOUNTED_DATASTORE` | Indicates that active virtual machines are present on the mounted datastore.A sample `ErrorInfo` object:
    
    
    {
      "reason": "ACTIVE_VMS_PRESENT_ON_MOUNTED_DATASTORE",
      "domain": "vmwareengine.googleapis.com",
       "metadata": {
           "datastoreName":
           "projects/my-project/locations/us-west1/privateClouds/my-pc/clusters/my-cluster/datastores/my-datastore",
       }
    }
      
  
`VSPHERE_VERSION_UNSUPPORTED` | Indicates that the current vSphere version does not support this operation.A sample `ErrorInfo` object:
    
    
    {
      "reason": "VSPHERE_VERSION_UNSUPPORTED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "vsphereVersion": "7.0",
           "requiredVersion": "8.x",
       }
    }
      
  
`CLUSTER_NOT_FOUND` | Indicates that the cluster was not found.A sample `ErrorInfo` object:
    
    
    {
      "reason": "CLUSTER_NOT_FOUND",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "resourceName":
           "projects/my-project/locations/us-west1/privateClouds/my-pc/clusters/my-cluster",
       }
    }
      
  
`MANAGEMENT_VM_MIGRATION_INVALID_TARGET_TYPE` | Indicates that the target cluster for management VM migration is a management cluster, but must be a workload cluster.A sample `ErrorInfo` object:
    
    
    {
      "reason": "MANAGEMENT_VM_MIGRATION_INVALID_TARGET_TYPE",
      "domain": "vmwareengine.googleapis.com",
       "metadata": {
           "resourceName":
           "projects/my-project/locations/us-west1/privateClouds/my-pc/clusters/my-cluster",
       }
    }
      
  
`REFERENCED_RESOURCE_STATE_DISALLOWS_REQUEST` | Indicates that the referenced resource is not in a state that allows the requested operation. For example, the referenced cluster is not in an active state.A sample `ErrorInfo` object:
    
    
    {
      "reason": "REFERENCED_RESOURCE_STATE_DISALLOWS_REQUEST",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
         "resourceType": "CLUSTER"
         "allowedStates": "ACTIVE"
       }
    }
      
  
`DATASTORE_MOUNT_ALREADY_CONFIGURED` | A datastore mount with the same configuration already exists.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DATASTORE_MOUNT_ALREADY_CONFIGURED",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
        "datastoreName":
        "projects/my-project/locations/us-west1/privateClouds/my-pc/clusters/my-cluster/datastores/my-datastore"
      }
    }
      
  
`NON_USER_DEFINED_SUBNET_TYPE` | Indicates that the subnet type is unsupported for this operation.A sample `ErrorInfo` object:
    
    
    {
      "reason": "NON_USER_DEFINED_SUBNET_TYPE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
           "subnetName":
           "projects/my-project/locations/us-west1/privateClouds/my-pc/subnets/my-subnet"
       }
    }
      
  
`DATASTORE_ALREADY_CONFIGURED_ON_VSPHERE` | Indicates that a datastore mount with the same configuration already exists on vSphere.A sample `ErrorInfo` object:
    
    
    {
      "reason": "DATASTORE_ALREADY_CONFIGURED_ON_VSPHERE",
      "domain": "vmwareengine.googleapis.com",
      "metadata": {
        "datastoreName":
        "projects/my-project/locations/us-west1/privateClouds/my-pc/clusters/my-cluster/datastores/my-datastore"
      },
      "details": [
        {
          "@type": "type.googleapis.com/google.rpc.Help",
          "links": [
            {
              "description": "Google Cloud VMware Engine Support",
              "url":
              "https://cloud.google.com/vmware-engine/docs/getting-support"
            }
          ]
        }
      ]
      }
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
