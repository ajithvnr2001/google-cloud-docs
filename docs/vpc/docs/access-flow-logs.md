---
url: https://docs.cloud.google.com/vpc/docs/access-flow-logs/
title: Access flow logs \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:52.409121+00:00
---

# Access flow logs  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/access-flow-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access flow logs

This page describes how to access flow logs by using Cloud Logging.

## Access flow logs in the Logs Explorer

VPC Flow Logs writes logs to the Google Cloud project of the log reporter. You can view flow logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). VPC Flow Logs uses the following logs to collect log entries:

  * The `networkmanagement.googleapis.com/vpc_flows` log collects log entries for Virtual Private Cloud (VPC) networks, subnets, VLAN attachments for Cloud Interconnect, and Cloud VPN tunnels.
  * The `compute.googleapis.com/vpc_flows` log collects log entries for subnets. This log is generated only if you [enabled VPC Flow Logs for subnets by using the Compute Engine API](https://docs.cloud.google.com/vpc/docs/using-flow-logs#compute-engine).



### Configure IAM

To configure access control for logging, see the [access control guide for Logging](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).

### View flow logs by using resource filters

To view flow logs in a Google Cloud project by using resource filters, see the following sections. You can also view these logs by using Logs Explorer queries, as described in Filter flow logs by using queries.

#### View flow logs for all configurations (`networkmanagement.googleapis.com/vpc_flows`)

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resources**.

  3. In the **Select resource** list, click **VPC Flow Logs Config** and then click **Apply**.




#### View flow logs for a specific configuration (`networkmanagement.googleapis.com/vpc_flows`)

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resources**.

  3. In the **Select resource** list, click **VPC Flow Logs Config** and select the VPC Flow Logs configuration that you want to view.

  4. Click **Apply**.




#### View flow logs for all configurations (`compute.googleapis.com/vpc_flows`)

Follow these steps if you [enabled VPC Flow Logs by using the Compute Engine API](https://docs.cloud.google.com/vpc/docs/using-flow-logs#compute-engine).

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resources**.

  3. In the **Select resource** list, click **Subnetwork** and then click **Apply**.

  4. Click **All log names**.

  5. In the **Select log names** list, find **Compute Engine** , click **vpc_flows** , and then click **Apply**.




#### View flow logs for a specific subnet (`compute.googleapis.com/vpc_flows`)

Follow these steps if you [enabled VPC Flow Logs by using the Compute Engine API](https://docs.cloud.google.com/vpc/docs/using-flow-logs#compute-engine).

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resources**.

  3. In the **Select resource** list, click **Subnetwork**.

  4. In the **Subnetwork ID** list, select the subnet and then click **Apply**.

  5. Click **All log names**.

  6. In the **Select log names** list, find **Compute Engine** , click **vpc_flows** , and then click **Apply**.




### Filter flow logs by using queries

To view flow logs in a Google Cloud project by using Logs Explorer queries, do the following.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If you don't see the query editor field in the **Query** pane, click the **Show query** toggle.

  3. In the query editor field, enter a query:

     * For example, to view flow logs for a specific source Cloud VPN tunnel, enter the following query:
           
           resource.type="vpc_flow_logs_config"
           logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
           jsonPayload.reporter="SRC_GATEWAY"
           labels.target_resource_name="projects/PROJECT_NUMBER/regions/REGION/vpnTunnels/NAME"
           

Replace the following:

       * `PROJECT_ID`: the Google Cloud project ID of the Cloud VPN tunnel
       * `PROJECT_NUMBER`: the project number of the Cloud VPN tunnel
       * `REGION`: the region of the Cloud VPN tunnel
       * `NAME`: the name of the Cloud VPN tunnel
     * If you [enabled](https://docs.cloud.google.com/vpc/docs/using-flow-logs#compute-engine) VPC Flow Logs for a subnet by using the Compute Engine API, the query must target `compute.googleapis.com`. For example, enter the following query, replacing `PROJECT_ID` with your Google Cloud project ID and `SUBNET_NAME` with your subnet:
           
           resource.type="gce_subnetwork"
           logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows"
           resource.labels.subnetwork_name="SUBNET_NAME"
           

For more examples of queries that you can run to view your flow logs, see Examples of Logs Explorer queries for VPC Flow Logs.

  4. Click **Run query**.




#### Examples of Logs Explorer queries for VPC Flow Logs

This section provides examples of Logs Explorer queries that you can run to view your flow logs. Include the following information in all queries:

  * Specify the resource type and log name of the log that you want to query, as described in the following table. You can query both logs in a single query.

Log | Resource type and log name  
---|---  
`networkmanagement.googleapis.com/vpc_flows`  
Collects logs for configurations that are managed by the Network Management API. | 
        
        resource.type="vpc_flow_logs_config"
        logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
          
  
`compute.googleapis.com/vpc_flows`  
Collects logs for configurations that are managed by the Compute Engine API.  | 
        
        resource.type="gce_subnetwork"
        logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows"  
  
Replace `PROJECT_ID` with the Google Cloud project ID of the reporting resource.

  * If you use multiple VPC Flow Logs configurations per resource, specify the name of the configuration that you want to query and the target resource by adding the `resource.labels.name` and `labels.target_resource_name` fields to the query. This ensures duplicate logs are excluded from the query results. For more information, see Duplicate logs.

    * `resource.labels.name` is the name of the configuration. You can specify multiple configurations per query.
    * `labels.target_resource_name` is the name of the reporting VPC network, subnet, VLAN attachment, or Cloud VPN tunnel. Configurations for organizations don't set a target resource.
    * These fields are available only in the `networkmanagement.googleapis.com/vpc_flows` log.



See the following table for examples of Logs Explorer queries that you can use to view your flow logs.

Logs you want to view | Query  
---|---  
All flow logs | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")  
  
Logs for a specific configuration | 
    
    
    resource.type="vpc_flow_logs_config"
    logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
    resource.labels.name="CONFIG_NAME"  
  
Logs for VM instances in a specific VPC network | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    (jsonPayload.src_vpc.vpc_name="NETWORK_NAME" OR
    jsonPayload.dest_vpc.vpc_name="NETWORK_NAME")  
  
Logs for VM instances in a specific subnet | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    (jsonPayload.src_vpc.subnetwork_name="SUBNET_NAME" OR
    jsonPayload.dest_vpc.subnetwork_name="SUBNET_NAME")  
  
Logs for a specific VM instance | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    (jsonPayload.src_instance.vm_name="VM_NAME" OR
    jsonPayload.dest_instance.vm_name="VM_NAME")
      
  
Logs for a specific Google Kubernetes Engine cluster | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    (jsonPayload.src_gke_details.cluster.cluster_name="CLUSTER_NAME" OR
    jsonPayload.dest_gke_details.cluster.cluster_name="CLUSTER_NAME")
      
  
Logs for only egress VM traffic from a subnet | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    jsonPayload.reporter="SRC" AND
    jsonPayload.src_vpc.subnetwork_name="SUBNET_NAME" AND
    (jsonPayload.dest_vpc.subnetwork_name!="SUBNET_NAME" OR NOT
    jsonPayload.dest_vpc.subnetwork_name:*)  
  
Logs for only egress VM traffic from a VPC network | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    jsonPayload.reporter="SRC" AND
    jsonPayload.src_vpc.vpc_name="VPC_NAME" AND
    (jsonPayload.dest_vpc.vpc_name!="VPC_NAME" OR NOT jsonPayload.dest_vpc:*)  
  
Logs for traffic to a specific subnet range | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    ip_in_net(jsonPayload.connection.dest_ip, "SUBNET_RANGE")  
  
Logs for an individual destination port | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    jsonPayload.connection.dest_port=PORT
    jsonPayload.connection.protocol=PROTOCOL  
  
Logs for multiple destination ports | 
    
    
    resource.type=("vpc_flow_logs_config" OR "gce_subnetwork")
    logName=("projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows" OR
    "projects/PROJECT_ID/logs/compute.googleapis.com%2Fvpc_flows")
    jsonPayload.connection.dest_port=(PORT_1 OR PORT_2)
    jsonPayload.connection.protocol=PROTOCOL  
  
Logs for a specific source Cloud VPN tunnel | 
    
    
    resource.type="vpc_flow_logs_config"
    logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
    jsonPayload.reporter="SRC_GATEWAY"
    labels.target_resource_name="projects/PROJECT_NUMBER/regions/REGION/vpnTunnels/NAME"  
  
Logs for all destination VLAN attachments | 
    
    
    resource.type="vpc_flow_logs_config"
    logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
    jsonPayload.reporter="DEST_GATEWAY"
    jsonPayload.dest_gateway.type="INTERCONNECT_ATTACHMENT"  
  
Logs for all destination VLAN attachments in a specific region | 
    
    
    resource.type="vpc_flow_logs_config"
    logName="projects/PROJECT_ID/logs/networkmanagement.googleapis.com%2Fvpc_flows"
    jsonPayload.reporter="DEST_GATEWAY"
    jsonPayload.dest_gateway.type="INTERCONNECT_ATTACHMENT"
    jsonPayload.dest_gateway.location="REGION"  
  
Replace the following:

  * `PROJECT_ID`: the project ID
  * `CONFIG_NAME`: the name of the VPC Flow Logs configuration
  * `SUBNET_NAME`: the name of the subnet
  * `VM_NAME`: the name of the VM
  * `SUBNET_RANGE`: a CIDR range, such as `192.168.1.0/24`
  * `CLUSTER_NAME`: the name of the GKE cluster
  * `VPC_NAME`: the name of the VPC network
  * `PORT_1` and `PORT_2`: the destination ports
  * `PROTOCOL`: the communication protocol
  * `PROJECT_NUMBER`: the project number of the Cloud VPN tunnel
  * `REGION`: the region of the VLAN attachment or Cloud VPN tunnel
  * `NAME`: the name of the Cloud VPN tunnel



## Route logs to BigQuery, Pub/Sub, and custom targets

You can route flow logs from Logging to a destination of your choice as described in the [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview) in the Logging documentation. Refer to the previous section for example filters.

## Troubleshooting

### No `vpc_flows` appear in Logging for the `gce_subnetwork` resource

  * Confirm that logging is [enabled](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-logging-existing) for the given subnet.
  * VPC flows are only supported for VPC networks. If you have a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy), you don't see any logs.
  * In [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) networks, logs only appear in the host project, not the service projects. Make sure that you look for the logs in the host project.
  * Logging exclusion filters block specified logs. Make sure that there are no exclusion rules that discard VPC Flow Logs: 
    1. Go to [Log router](https://console.cloud.google.com/logs/router).
    2. In the more_vert **More actions** menu for your logging bucket, click **View sink details**.
    3. Make sure that there are no exclusion rules that might discard VPC Flow Logs.
  * Use the Google Cloud CLI or API to determine if a [log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) configuration is filtering all the traffic in a given subnet. For example, if `filterExpr` is set to `false`, you don't see any logs.



### No RTT or byte values on some of the logs

  * RTT measurements may be missing if not enough packets were sampled to capture RTT. This is more likely to happen for low volume connections.
  * RTT values are available only for TCP flows reported from VMs.
  * Some packets are sent with no payload. If header-only packets are sampled, the bytes value is usually zero. For more information, see [Record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format).



### Some flows are missing

  * Ingress packets are sampled after ingress [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls). Make sure that there aren't any ingress firewall rules that deny the packets that you expect to be logged. If you're not sure whether VPC firewall rules are blocking ingress packets, you can enable [Firewall Rules Logging](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview) and inspect the logs.
  * Only TCP, UDP, ICMP, ESP, and GRE protocols are supported. VPC Flow Logs does not support any other protocols.
  * Logs [are sampled](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). Some packets in very low volume flows might be missed.



### Missing GKE annotations in some logs

Make sure that your GKE cluster is a [supported version](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

### Missing logs for some GKE flows

Make sure [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) is enabled in the cluster. Otherwise, flows between Pods on the same node are not logged.

### Duplicate logs

Each VPC Flow Logs configuration generates a separate set of logs. If your logging information contains duplicate logs, check if the reporting resource is associated with more than one configuration.

A resource is associated with more than one configuration if you create multiple configurations per resource or if you create multiple configurations and their scopes overlap as described in the following list:

  * VPC Flow Logs is configured for the organization, and you have additional configurations for the organization or VPC networks, subnets, VLAN attachments, or Cloud VPN tunnels in any of the organization's projects.

By default, a VPC Flow Logs configuration for an organization generates logs for all VM instances in all subnets, all VLAN attachments, and all Cloud VPN tunnels in the organization. If you create additional configurations, each additional configuration generates its own set of logs.

  * VPC Flow Logs is configured for a VPC network, and you have additional configurations for subnets, VLAN attachments, or Cloud VPN tunnels in the same network.

By default, a VPC Flow Logs configuration for a VPC network generates logs for all VM instances in all subnets, all VLAN attachments, and all Cloud VPN tunnels in the network. If you create additional configurations, each additional configuration generates its own set of logs.

  * VPC Flow Logs is configured for a subnet through both the Network Management API and the Compute Engine API. Both the Compute Engine API-managed VPC Flow Logs configuration for the subnet and each applicable configuration that you create by using the Network Management API to generate logs.




For more information about which resources are logged by each VPC Flow Logs configuration scope, see [Supported configurations](https://docs.cloud.google.com/vpc/docs/flow-logs#configurations). To view your VPC Flow Logs configurations, see [View VPC Flow Logs configurations (all)](https://docs.cloud.google.com/vpc/docs/using-flow-logs#view-flow-logs-configurations).

To filter out duplicate logs when viewing them, you can use the following fields:

  * To filter logs by log name, specify the `resource_type` and `log_name` fields.
  * To filter logs by configuration and target resource name, specify the `resource.labels.name` and `labels.target_resource_name` fields.



For more information about these fields and how to use them, see Examples of Logs Explorer queries for VPC Flow Logs.

## What's next

  * View [Logging](https://docs.cloud.google.com/logging/docs) documentation
  * View [Logging sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) documentation
  * Analyze flow logs in [Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
