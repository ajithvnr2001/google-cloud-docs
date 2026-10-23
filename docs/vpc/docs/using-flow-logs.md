---
url: https://docs.cloud.google.com/vpc/docs/using-flow-logs/
title: Configure VPC Flow Logs \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:14.484709+00:00
---

# Configure VPC Flow Logs  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/using-flow-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VPC Flow Logs

This page explains how to configure VPC Flow Logs. It assumes that you are familiar with the concepts described in [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) and [About VPC Flow Logs records](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records).

## Before you begin

Configure at least one of the following:

  * Recommended: The Network Management API lets you configure VPC Flow Logs for organizations, Virtual Private Cloud (VPC) networks, subnets, VLAN attachments for Cloud Interconnect, and Cloud VPN tunnels. To use the Network Management API, do the following:

    1. Enable the Network Management API in your Google Cloud project.

[Enable Network Management API](https://console.cloud.google.com/apis/api/networkmanagement.googleapis.com)

    2. Make sure that you have the [Network Management Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.admin) (`roles/networkmanagement.admin`), granted as follows:

       * Organization level (required if you want to configure VPC Flow Logs for an organization)
       * Project level (required if you want to configure VPC Flow Logs for a VPC network, subnet, VLAN attachment, or Cloud VPN tunnel)
    3. Additionally, if you want to configure VPC Flow Logs for an organization, make sure you have the [`resourcemanager.organizations.get` permission](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizations.get).

  * The Compute Engine API lets you configure VPC Flow Logs only for subnets. Configurations created with the Compute Engine API can't be managed with the Network Management API. To use the Compute Engine API, do the following:

    1. Enable the Compute Engine API in your Google Cloud project.

[Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

    2. Make sure that you have one of the following roles on the project:

       * [Compute Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)
       * [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)

For more information about which API to use to enable VPC Flow Logs for subnets, see Choose how to enable VPC Flow Logs for a subnet.




### Set up the Google Cloud CLI

Skip this step if you don't plan to use the gcloud CLI to configure VPC Flow Logs.

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

## Enable VPC Flow Logs

You enable VPC Flow Logs for a resource by creating a VPC Flow Logs configuration. VPC Flow Logs lets you create configurations at the organization and project levels:

  * An organization-level configuration enables flow logs for all subnets, VLAN attachments, and Cloud VPN tunnels in all VPC networks in the organization.
  * A project-level configuration lets you enable flow logs for the following resources: 
    * A specific VPC network, which includes all subnets, VLAN attachments, and Cloud VPN tunnels in the network
    * A specific subnet, VLAN attachment, or Cloud VPN tunnel



You can add more than one VPC Flow Logs configuration per resource. Each configuration generates a separate set of flow logs. If you associate a resource with multiple VPC Flow Logs configurations and their [scope](https://docs.cloud.google.com/vpc/docs/flow-logs#configurations) overlaps, your logging information might contain [duplicate logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs#duplicate-logs).

You can also modify the amount of information written to logging. For more information about the parameters that you can control, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).

### Enable VPC Flow Logs for a subnet

When you enable VPC Flow Logs for a subnet, you enable logging for all VMs in the subnet.

#### Choose how to enable VPC Flow Logs for a subnet

You can use the Network Management API or the Compute Engine API to enable VPC Flow Logs for subnets. Because the Network Management API offers more options for enabling VPC Flow Logs, we recommend that you use the Network Management API.

The Network Management API provides feature parity with the Compute Engine API—all options for configuring VPC Flow Logs for subnets that are available in the Compute Engine API are supported in the Network Management API. In addition, the Network Management API supports [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging), which isn't supported in the Compute Engine API.

For existing VPC Flow Logs configurations that are managed by the Compute Engine API, consider the following:

  * To move your configurations to the Network Management API, you can use either of the following approaches: 
    * You can create a copy of your VPC Flow Logs configurations by using the Network Management API and then delete the original configurations. For more information, see Enable VPC Flow Logs for a subnet (Network Management API) and Disable VPC Flow Logs for a subnet.
    * To simplify VPC Flow Logs configuration management, you can optionally consolidate your existing Compute Engine API-managed configurations. For example, instead of creating a separate configuration for each subnet, you can create a configuration for the VPC network or organization that contains your subnets and then delete the original configurations. For more information, see [Supported configurations](https://docs.cloud.google.com/vpc/docs/flow-logs#configurations).
  * Unlike the Compute Engine API, the Network Management API doesn't set the `enableFlowLogs` or `logConfig.enable` fields for subnets. If you are using third-party tools that depend on these fields, you can do either of the following: 
    * Use the `showEffectiveFlowLogsConfigs` method of the Network Management API to view all configurations for a specific subnet. For more information, see View all configurations for a resource in the _API_ tab.
    * Continue using the Compute Engine API to configure VPC Flow Logs for subnets, as described in Enable VPC Flow Logs for a subnet (Compute Engine API).



#### Enable VPC Flow Logs for a subnet (Network Management API)

This section describes how to enable VPC Flow Logs for a subnet by using the Network Management API (recommended).

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. On the **Subnets in current project** tab, select one or more subnets and then click menu**Manage flow logs**.

  3. In menu**Manage flow logs** , click **Add new configuration**.

  4. Do one of the following:

     * If you selected one subnet, in the **Configurations — Subnets** section, click **Add a configuration**.
     * If you selected multiple subnets, in the **Configure VPC Flow Logs** section, select **Network Management API**.
  5. For **Name** , enter a name for the new VPC Flow Logs configuration.

  6. Optional: Adjust the **Aggregation interval** and any of the settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * Whether to enable TCP connection logging. By default, **Connection logging** is deselected. If selected, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  7. Click **Save**.




###  gcloud 

To enable VPC Flow Logs for a subnet, use the [`gcloud network-management vpc-flow-logs-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

In the gcloud CLI, set your project to the Google Cloud project ID of the subnet and run one of the following commands:

  * To create a default VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --subnet=SUBNET
        

  * To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, metadata, and connection logging parameters when creating a VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --subnet=SUBNET \
            --aggregation-interval=AGGREGATION_INTERVAL \
            --filter-expr=FILTER_EXPRESSION \
            --flow-sampling=SAMPLING_RATE \
            --metadata=LOGGING_METADATA \
            --connection-logging=CONNECTION_LOGGING
        

Replace the following:

    * `CONFIG_NAME`: a name for the configuration.
    * `SUBNET`: the subnet that you want to log. Must be specified in the following format: `"projects/PROJECT_ID/regions/REGION/subnetworks/NAME"`, where: 
      * `PROJECT_ID` is the ID of the Google Cloud project that contains the subnet. The configuration must be created in this project.
      * `REGION` is the region of the subnet.
      * `NAME` is the name of the subnet.

To set the optional parameters in a custom configuration, replace the following:

    * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
    * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
    * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
    * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
      * Use `include-all-metadata` to include all metadata annotations (default).
      * Use `exclude-all-metadata` to exclude all metadata annotations.
      * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
        * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.
    * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `enabled` or `disabled` (default). For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).



###  API 

To enable VPC Flow Logs for a subnet, use the [`projects.locations.vpcFlowLogsConfigs.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

To create a default VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "subnet": "SUBNET"
    }
    

To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, metadata, and connection logging parameters when creating a VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "subnet": "SUBNET",
      "aggregationInterval": "AGGREGATION_INTERVAL",
      "filterExpr": "FILTER_EXPRESSION",
      "flowSampling": SAMPLING_RATE,
      "metadata": "LOGGING_METADATA",
      "connectionLogging": "CONNECTION_LOGGING"
    }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID of the subnet.
  * `CONFIG_NAME`: a name for the configuration.
  * `SUBNET`: the subnet that you want to log. Must be specified in the following format: `projects/PROJECT_ID/regions/REGION/subnetworks/NAME`, where: 
    * `PROJECT_ID` is the project ID of the subnet.
    * `REGION` is the region of the subnet.
    * `NAME` is the name of the subnet.

To set the optional parameters in a custom configuration, replace the following: 
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `INTERVAL_5_SEC` (default), `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, or `INTERVAL_15_MIN`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `INCLUDE_ALL_METADATA` to include all metadata annotations (default).
    * Use `EXCLUDE_ALL_METADATA` to exclude all metadata annotations.
    * Use `CUSTOM_METADATA` to include a custom list of metadata fields. To specify the metadata fields, use the `metadataFields` parameter: 
      * `metadataFields: METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `CUSTOM_METADATA`.


  * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `ENABLED` or `DISABLED` (default). For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).



#### Enable VPC Flow Logs for a subnet (Compute Engine API)

This section describes how to enable VPC Flow Logs for a subnet by using the Compute Engine API. We recommend that you enable VPC Flow Logs for a subnet by using the Network Management API.

**Note:** [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging) isn't supported when you configure VPC Flow Logs by using the Compute Engine API. To use TCP connection logging, configure VPC Flow Logs by using the Network Management API.

You can enable VPC Flow Logs when you create a subnet or for an existing subnet.

##### Enable VPC Flow Logs when you create a subnet

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the network where you want to add a subnet.

  3. Click **Add subnet**.

  4. For **Flow logs** , select **On**.

  5. Optional: Adjust the **Aggregation interval** and any of the following settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * The **Secondary sampling rate**. `50%` means that half of entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  6. Populate other fields [as appropriate](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets).

  7. Click **Add**.




###  gcloud 

Run the following command:
    
    
    gcloud compute networks subnets create SUBNET_NAME \
        --enable-flow-logs \
        [--logging-aggregation-interval=AGGREGATION_INTERVAL] \
        [--logging-flow-sampling=SAMPLING_RATE] \
        [--logging-filter-expr=FILTER_EXPRESSION] \
        [--logging-metadata=LOGGING_METADATA] \
        [--logging-metadata-fields=METADATA_FIELDS] \
        [other flags as needed]
    

Replace the following:

  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs in that subnet. The interval can be set to any of the following: 5-sec (default), 30-sec, 1-min, 5-min, 10-min, or 15-min.
  * `SAMPLING_RATE`: the secondary flow sampling rate. Secondary flow sampling can be set from `0.0` (no sampling) to `1.0` (all logs). Default is `0.5`. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and Examples of log filters.
  * `LOGGING_METADATA`: the [metadata annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#metadata) that you want to include in the logs:

    * Use `include-all` to include all metadata annotations.
    * Use `exclude-all` to exclude all metadata annotations (default).
    * Use `custom` to include a custom list of metadata fields that you specify in `METADATA_FIELDS`.
**Note:** If a subnet had flow logging enabled at any time before March 1, 2021, and if `LOGGING_METADATA` was never explicitly configured, the default value for `LOGGING_METADATA` is `include-all`.
  * `METADATA_FIELDS`: a comma-separated list of metadata fields you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `LOGGING_METADATA` is set to `custom`.




###  API 

Enable VPC Flow Logs when you create a new subnet.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
    {
      "logConfig": {
        "aggregationInterval": "AGGREGATION_INTERVAL",
        "flowSampling": SAMPLING_RATE,
        "filterExpr": EXPRESSION,
        "metadata": METADATA_SETTING,
        "metadataFields": METADATA_FIELDS,
        "enable": true
      },
      "ipCidrRange": "IP_RANGE",
      "network": "NETWORK_URL",
      "name": "SUBNET_NAME"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the subnet will be created.
  * `REGION`: the region where the subnet will be created.
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs in the subnet. The interval can be set to any of the following: `INTERVAL_5_SEC`, `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, or `INTERVAL_15_MIN`.
  * `SAMPLING_RATE`: the flow sampling rate. Flow sampling can be set from `0.0` (no sampling) to `1.0` (all logs). Default is `.0.5`.
  * `EXPRESSION`: the filter expression you use to filter which logs are actually written. The expression has a limit of 2,048 characters. For details, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering).
  * `METADATA_SETTING`: the [metadata annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#metadata) that you want to include in the logs:

    * Use `INCLUDE_ALL_METADATA` to include all metadata annotations.
    * Use `EXCLUDE_ALL_METADATA` to exclude all metadata annotations (default).
    * Use `CUSTOM_METADATA` to include a custom list of metadata fields that you specify in `METADATA_FIELDS`.
**Note:** If a subnet had flow logging enabled at any time before March 1, 2021, and if `METADATA_SETTING` was never explicitly configured, the default value for `METADATA_SETTING` is `INCLUDE_ALL_METADATA`.
  * `METADATA_FIELDS`: the metadata fields you want to capture when you have set `metadata: CUSTOM_METADATA`. This is a comma-separated list of metadata fields, such as `src_instance, src_vpc.project_id`.

  * `IP_RANGE`: the primary internal IP address range of the subnet.

  * `NETWORK_URL`: the Virtual Private Cloud network URL where the subnet will be created.

  * `SUBNET_NAME`: a name for the subnet.




For more information, see the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).

### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-network) to create a custom mode VPC network and subnets.

The following example creates three subnets as follows:

  * `subnet-01` has VPC Flow Logs disabled. When you create a subnet, VPC Flow Logs are disabled unless you explicitly enable them.
  * `subnet-02` has VPC Flow Logs enabled with the default flow log settings.
  * `subnet-03` has VPC Flow Logs enabled with some custom settings.


    
    
    module "test-vpc-module" {
      source       = "terraform-google-modules/network/google"
      version      = "~> 18.0"
      project_id   = var.project_id # Replace this with your project ID in quotes
      network_name = "my-custom-mode-network"
      mtu          = 1460
    
      subnets = [
        {
          subnet_name   = "subnet-01"
          subnet_ip     = "10.10.10.0/24"
          subnet_region = "us-west1"
        },
        {
          subnet_name           = "subnet-02"
          subnet_ip             = "10.10.20.0/24"
          subnet_region         = "us-west1"
          subnet_private_access = "true"
          subnet_flow_logs      = "true"
        },
        {
          subnet_name               = "subnet-03"
          subnet_ip                 = "10.10.30.0/24"
          subnet_region             = "us-west1"
          subnet_flow_logs          = "true"
          subnet_flow_logs_interval = "INTERVAL_10_MIN"
          subnet_flow_logs_sampling = 0.7
          subnet_flow_logs_metadata = "INCLUDE_ALL_METADATA"
          subnet_flow_logs_filter   = "false"
        }
      ]
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

##### Enable VPC Flow Logs for an existing subnet

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. On the **Subnets in current project** tab, select one or more subnets and then click menu**Manage flow logs**.

  3. In menu**Manage flow logs** , click **Add new configuration**.

  4. Do one of the following:

     * If you selected one subnet, in the **Configurations - Subnets (Compute Engine API)** section, click **Add a configuration**.
     * If you selected multiple subnets, in the **Configure VPC Flow Logs** section, select **Compute Engine API**.
  5. Optional: Adjust the **Aggregation interval** and any of the following settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * The **Secondary sampling rate**. `50%` means that half of entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  6. Click **Save**.




###  gcloud 

Run the following command:
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --enable-flow-logs \
        [--logging-aggregation-interval=AGGREGATION_INTERVAL] \
        [--logging-flow-sampling=SAMPLING_RATE] \
        [--logging-filter-expr=FILTER_EXPRESSION] \
        [--logging-metadata=LOGGING_METADATA] \
        [--logging-metadata-fields=METADATA_FIELDS] \
        [other flags as needed]
    

Replace the following:

  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs in that subnet. The interval can be set to any of the following: 5-sec (default), 30-sec, 1-min, 5-min, 10-min, or 15-min.
  * `SAMPLING_RATE`: the secondary flow sampling rate. Secondary flow sampling can be set from `0.0` (no sampling) to `1.0` (all logs). Default is `0.5`. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and Examples of log filters.
  * `LOGGING_METADATA`: the [metadata annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#metadata) that you want to include in the logs:

    * Use `include-all` to include all metadata annotations.
    * Use `exclude-all` to exclude all metadata annotations (default).
    * Use `custom` to include a custom list of metadata fields that you specify in `METADATA_FIELDS`.
**Note:** If a subnet had flow logging enabled at any time before March 1, 2021, and if `LOGGING_METADATA` was never explicitly configured, the default value for `LOGGING_METADATA` is `include-all`.
  * `METADATA_FIELDS`: a comma-separated list of metadata fields you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `LOGGING_METADATA` is set to `custom`.




###  API 

Enable VPC Flow Logs for an existing subnet.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    {
      "logConfig": {
        "enable": true
        ...other logging fields.
      },
      "fingerprint": "SUBNET_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the subnet is located.
  * `REGION`: the region where the subnet is located.
  * `SUBNET_NAME`: the name of the existing subnet.
  * `SUBNET_FINGERPRINT`: the fingerprint ID for the existing subnet, which is provided when you [describe a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet).
  * For the other logging fields, see Enabling VPC Flow Logging when you create a subnet.



For more information, see the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).

### Enable VPC Flow Logs for a VLAN attachment

###  Console 

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects)

  2. In the **VLAN attachments** tab, select one or more VLAN attachments and then click menu**Manage flow logs** in the selection bar at the top of the list.

  3. In menu**Manage flow logs** , click **Add new configuration**.

  4. For **Name** , enter a name for the new VPC Flow Logs configuration.

  5. Optional: Adjust the **Aggregation interval** and any of the settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  6. Click **Save**.




###  gcloud 

To enable VPC Flow Logs for a VLAN attachment, use the [`gcloud network-management vpc-flow-logs-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

In the gcloud CLI, set your project to the Google Cloud project ID of the VLAN attachment and run one of the following commands:

  * To create a default VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --interconnect-attachment=VLAN_ATTACHMENT
        

  * To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, and metadata parameters when creating a VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --interconnect-attachment=VLAN_ATTACHMENT \
            --aggregation-interval=AGGREGATION_INTERVAL \
            --filter-expr=FILTER_EXPRESSION \
            --flow-sampling=SAMPLING_RATE \
            --metadata=LOGGING_METADATA
        

Replace the following:

    * `CONFIG_NAME`: a name for the configuration.
    * `VLAN_ATTACHMENT`: the VLAN attachment that you want to log. Must be specified in the following format: `"projects/PROJECT_ID/regions/REGION/interconnectAttachments/NAME"`, where: 
      * `PROJECT_ID` is the ID of the Google Cloud project that contains the VLAN attachment. The configuration must be created in this project.
      * `REGION` is the region of the VLAN attachment.
      * `NAME` is the name of the VLAN attachment.

To set the optional parameters in a custom configuration, replace the following:

    * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
    * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
    * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
    * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
      * Use `include-all-metadata` to include all metadata annotations (default).
      * Use `exclude-all-metadata` to exclude all metadata annotations.
      * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
        * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.



### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-docs-samples) to create a VPC Flow Logs configuration for a VLAN attachment.

The following code block creates a default VPC Flow Logs configuration.
    
    
    resource "google_network_management_vpc_flow_logs_config" "vpc_flow_logs_config" {
      vpc_flow_logs_config_id = "vpcflowlogs-config"
      location                = "global"
      interconnect_attachment = google_compute_interconnect_attachment.attachment.id
    }

The preceding example assumes that the name of the `google_compute_interconnect_attachment` resource is `attachment`. For a full example of this configuration, see the [terraform-docs-samples](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/network_management/vpcflowlogs/interconnect_attachment_basic/main.tf) repository.

The following code block creates a VPC Flow Logs configuration where:

  * The aggregation interval is set to `INTERVAL_10_MIN`.
  * The secondary flow sampling rate is set to `0.7`.
  * The metadata to include in the logs is set to `INCLUDE_ALL_METADATA`.
  * The configuration state is set to `ENABLED`.


    
    
    resource "google_network_management_vpc_flow_logs_config" "vpc_flow_logs_config" {
      vpc_flow_logs_config_id = "vpcflowlogs-config"
      location                = "global"
      interconnect_attachment = google_compute_interconnect_attachment.attachment.id
      aggregation_interval    = "INTERVAL_10_MIN"
      description             = "VPC Flow Logs over an Interconnect Attachment."
      flow_sampling           = 0.7
      metadata                = "INCLUDE_ALL_METADATA"
      state                   = "ENABLED"
    }

The preceding example assumes that the name of the `google_compute_interconnect_attachment` resource is `attachment`. For a full example of this configuration, see the [terraform-docs-samples](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/network_management/vpcflowlogs/interconnect_attachment_full/main.tf) repository.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

To enable VPC Flow Logs for a VLAN attachment, use the [`projects.locations.vpcFlowLogsConfigs.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

To create a default VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "interconnectAttachment": "VLAN_ATTACHMENT"
    }
    

To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, and metadata parameters when creating a VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "interconnectAttachment": "VLAN_ATTACHMENT",
      "aggregationInterval": "AGGREGATION_INTERVAL",
      "filterExpr": "FILTER_EXPRESSION",
      "flowSampling": SAMPLING_RATE,
      "metadata": "LOGGING_METADATA"
    }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID of the VLAN attachment.
  * `CONFIG_NAME`: a name for the configuration.
  * `VLAN_ATTACHMENT`: the VLAN attachment that you want to log. Must be specified in the following format: `projects/PROJECT_ID/regions/REGION/interconnectAttachments/NAME`, where: 
    * `PROJECT_ID` is the project ID of the VLAN attachment.
    * `REGION` is the region of the VLAN attachment.
    * `NAME` is the name of the VLAN attachment.

To set the optional parameters in a custom configuration, replace the following: 
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `INTERVAL_5_SEC` (default), `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, or `INTERVAL_15_MIN`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `INCLUDE_ALL_METADATA` to include all metadata annotations (default).
    * Use `EXCLUDE_ALL_METADATA` to exclude all metadata annotations.
    * Use `CUSTOM_METADATA` to include a custom list of metadata fields. To specify the metadata fields, use the `metadataFields` parameter: 
      * `metadataFields: METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `CUSTOM_METADATA`.



### Enable VPC Flow Logs for a Cloud VPN tunnel

###  Console 

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn)

  2. In the **Cloud VPN tunnels** tab, select one or more Cloud VPN tunnels and then click menu**Manage flow logs** in the selection bar at the top of the list.

  3. In menu**Manage flow logs** , click **Add new configuration**.

  4. For **Name** , enter a name for the new VPC Flow Logs configuration.

  5. Optional: Adjust the **Aggregation interval** and any of the settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  6. Click **Save**.




###  gcloud 

To enable VPC Flow Logs for a Cloud VPN tunnel, use the [`gcloud network-management vpc-flow-logs-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

In the gcloud CLI, set your project to the Google Cloud project ID of the Cloud VPN tunnel and run one of the following commands:

  * To create a default VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --vpn-tunnel=VPN_TUNNEL
        

  * To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, and metadata parameters when creating a VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --vpn-tunnel=VPN_TUNNEL \
            --aggregation-interval=AGGREGATION_INTERVAL \
            --filter-expr=FILTER_EXPRESSION \
            --flow-sampling=SAMPLING_RATE \
            --metadata=LOGGING_METADATA
        

Replace the following:

    * `CONFIG_NAME`: a name for the configuration.
    * `VPN_TUNNEL`: the Cloud VPN tunnel that you want to log. Must be specified in the following format: `"projects/PROJECT_ID/regions/REGION/vpnTunnels/NAME"`, where: 
      * `PROJECT_ID` is the ID of the Google Cloud project that contains the Cloud VPN tunnel. The configuration must be created in this project.
      * `REGION` is the region of the Cloud VPN tunnel.
      * `NAME` is the name of the Cloud VPN tunnel.

To set the optional parameters in a custom configuration, replace the following:

    * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
    * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
    * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
    * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
      * Use `include-all-metadata` to include all metadata annotations (default).
      * Use `exclude-all-metadata` to exclude all metadata annotations.
      * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
        * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.



### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-docs-samples) to create a VPC Flow Logs configuration for a Cloud VPN tunnel.

The following code block creates a default VPC Flow Logs configuration.
    
    
    resource "google_network_management_vpc_flow_logs_config" "vpc_flow_logs_config" {
      vpc_flow_logs_config_id = "vpcflowlogs-config"
      location                = "global"
      vpn_tunnel              = google_compute_vpn_tunnel.tunnel.id
    }

The preceding example assumes that the name of the `google_compute_vpn_tunnel` resource is `tunnel`. For a full example of this configuration, see the [terraform-docs-samples](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/network_management/vpcflowlogs/vpn_tunnel_basic/main.tf) repository.

The following code block creates a VPC Flow Logs configuration where:

  * The aggregation interval is set to `INTERVAL_10_MIN`.
  * The secondary flow sampling rate is set to `0.7`.
  * The metadata to include in the logs is set to `INCLUDE_ALL_METADATA`.
  * The configuration state is set to `ENABLED`.


    
    
    resource "google_network_management_vpc_flow_logs_config" "vpc_flow_logs_config" {
      vpc_flow_logs_config_id = "vpcflowlogs-config"
      location                = "global"
      vpn_tunnel              = google_compute_vpn_tunnel.tunnel.id
      aggregation_interval    = "INTERVAL_10_MIN"
      description             = "VPC Flow Logs over a VPN Gateway."
      flow_sampling           = 0.7
      metadata                = "INCLUDE_ALL_METADATA"
      state                   = "ENABLED"
    }

The preceding example assumes that the name of the `google_compute_vpn_tunnel` resource is `tunnel`. For a full example of this configuration, see the [terraform-docs-samples](https://github.com/terraform-google-modules/terraform-docs-samples/blob/main/network_management/vpcflowlogs/vpn_tunnel_full/main.tf) repository.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

To enable VPC Flow Logs for a Cloud VPN tunnel, use the [`projects.locations.vpcFlowLogsConfigs.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

To create a default VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "vpnTunnel": "VPN_TUNNEL"
    }
    

To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, and metadata parameters when creating a VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "vpnTunnel": "VPN_TUNNEL",
      "aggregationInterval": "AGGREGATION_INTERVAL",
      "filterExpr": "FILTER_EXPRESSION",
      "flowSampling": SAMPLING_RATE,
      "metadata": "LOGGING_METADATA"
    }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID of the Cloud VPN tunnel. 
  * `CONFIG_NAME`: a name for the configuration. 
  * `VPN_TUNNEL`: the Cloud VPN tunnel that you want to log. Must be specified in the following format: `projects/PROJECT_ID/regions/REGION/vpnTunnels/NAME`, where: 
    * `PROJECT_ID` is the project ID of the Cloud VPN tunnel.
    * `REGION` is the region of the Cloud VPN tunnel.
    * `NAME` is the name of the Cloud VPN tunnel.

To set the optional parameters in a custom configuration, replace the following: 
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `INTERVAL_5_SEC` (default), `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, or `INTERVAL_15_MIN`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `INCLUDE_ALL_METADATA` to include all metadata annotations (default).
    * Use `EXCLUDE_ALL_METADATA` to exclude all metadata annotations.
    * Use `CUSTOM_METADATA` to include a custom list of metadata fields. To specify the metadata fields, use the `metadataFields` parameter: 
      * `metadataFields: METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `CUSTOM_METADATA`.



### Enable VPC Flow Logs for a VPC network

To enable VPC Flow Logs for all subnets, VLAN attachments, and Cloud VPN tunnels in a VPC network, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Networks in current project** tab, select one or more networks and then click menu**Manage flow logs** at the top of the list.

  3. In menu**Manage flow logs** , click **Add new configuration**.

  4. For **Name** , enter a name for the new VPC Flow Logs configuration.

  5. Optional: Adjust the **Aggregation interval** and any of the settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * Whether to enable TCP connection logging. By default, **Connection logging** is deselected. If selected, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  6. Click **Save**.




###  gcloud 

To enable VPC Flow Logs for a VPC network, use the [`gcloud network-management vpc-flow-logs-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

In the gcloud CLI, set your project to the Google Cloud project ID of the VPC network and run one of the following commands:

  * To create a default VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --network=NETWORK
        

  * To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, metadata, and connection logging parameters when creating a VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --network=NETWORK \
            --aggregation-interval=AGGREGATION_INTERVAL \
            --filter-expr=FILTER_EXPRESSION \
            --flow-sampling=SAMPLING_RATE \
            --metadata=LOGGING_METADATA \
            --connection-logging=CONNECTION_LOGGING
        

Replace the following:

    * `CONFIG_NAME`: a name for the configuration.
    * `NETWORK`: the VPC network that you want to log. Must be specified in the following format: `"projects/PROJECT_ID/global/networks/NAME"`, where: 
      * `PROJECT_ID` is the ID of the Google Cloud project that contains the VPC network. The configuration must be created in this project.
      * `NAME` is the name of the VPC network.

To set the optional parameters in a custom configuration, replace the following:

    * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
    * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
    * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
    * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
      * Use `include-all-metadata` to include all metadata annotations (default).
      * Use `exclude-all-metadata` to exclude all metadata annotations.
      * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
        * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.
    * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `enabled` or `disabled` (default). If enabled, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).



###  API 

To enable VPC Flow Logs for a VPC network, use the [`projects.locations.vpcFlowLogsConfigs.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

To create a default VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "network": "NETWORK"
    }
    

To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, metadata, and connection logging parameters when creating a VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "network": "NETWORK",
      "aggregationInterval": "AGGREGATION_INTERVAL",
      "filterExpr": "FILTER_EXPRESSION",
      "flowSampling": SAMPLING_RATE,
      "metadata": "LOGGING_METADATA",
      "connectionLogging": "CONNECTION_LOGGING"
    }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID of the VPC network.
  * `CONFIG_NAME`: a name for the configuration.
  * `NETWORK`: the VPC network that you want to log. Must be specified in the following format: `projects/PROJECT_ID/global/networks/NAME`, where: 
    * `PROJECT_ID` is the project ID of the VPC network.
    * `NAME` is the name of the VPC network.

To set the optional parameters in a custom configuration, replace the following: 
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `INTERVAL_5_SEC` (default), `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, or `INTERVAL_15_MIN`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `INCLUDE_ALL_METADATA` to include all metadata annotations (default).
    * Use `EXCLUDE_ALL_METADATA` to exclude all metadata annotations.
    * Use `CUSTOM_METADATA` to include a custom list of metadata fields. To specify the metadata fields, use the `metadataFields` parameter: 
      * `metadataFields: METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `CUSTOM_METADATA`.


  * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `ENABLED` or `DISABLED` (default). If enabled, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).



### Enable VPC Flow Logs for an organization

To enable VPC Flow Logs for all subnets, VLAN attachments, and Cloud VPN tunnels in all VPC networks in an organization, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. Click **Add VPC Flow Logs configuration** and then click **Add a configuration for the organization**.

  3. For **Name** , enter a name for the new VPC Flow Logs configuration.

  4. Optional: Adjust the **Aggregation interval** and any of the settings in the **Advanced settings** section:

     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include cross-project annotations. By default, **Cross-project metadata annotations** is selected. For more information, see [Cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project).
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * Whether to enable TCP connection logging. By default, **Connection logging** is deselected. If selected, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  5. Click **Save**.




###  gcloud 

To enable VPC Flow Logs for an organization, use the [`gcloud network-management vpc-flow-logs-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/create).

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

  * To create a default VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --organization=ORGANIZATION
        

  * To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, metadata, and connection logging parameters when creating a VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs create CONFIG_NAME \
            --location=global \
            --organization=ORGANIZATION \
            --aggregation-interval=AGGREGATION_INTERVAL \
            --filter-expr=FILTER_EXPRESSION \
            --flow-sampling=SAMPLING_RATE \
            --metadata=LOGGING_METADATA \
            --cross-project-metadata=CROSS_PROJECT_METADATA \
            --connection-logging=CONNECTION_LOGGING
        

Replace the following:

    * `CONFIG_NAME`: a name for the configuration
    * `ORGANIZATION`: the ID of the organization

To set the optional parameters in a custom configuration, replace the following:

    * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
    * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
    * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
    * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
      * Use `include-all-metadata` to include all metadata annotations (default).
      * Use `exclude-all-metadata` to exclude all metadata annotations.
      * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
        * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.
    * `CROSS_PROJECT_METADATA`: cross-project annotations. Can be set to `cross-project-metadata-enabled` (default) or `cross-project-metadata-disabled`. For more information, see [Cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project).
    * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `enabled` or `disabled` (default). If enabled, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).



###  API 

To enable VPC Flow Logs for an organization, use the `organizations.locations.vpcFlowLogsConfigs.create` method.

You enable VPC Flow Logs by creating a VPC Flow Logs configuration. You can create the configuration with all of its parameters set to their default values, or you can customize the default values.

To create a default VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    

To create a custom VPC Flow Logs configuration, specify each parameter that you want to customize.

For example, to customize the aggregation interval, filtering, secondary sampling rate, metadata, and connection logging parameters when creating a VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    POST -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs?vpc_flow_logs_config_id=CONFIG_NAME
    {
      "aggregationInterval": "AGGREGATION_INTERVAL",
      "filterExpr": "FILTER_EXPRESSION",
      "flowSampling": SAMPLING_RATE,
      "metadata": "LOGGING_METADATA",
      "crossProjectMetadata": "CROSS_PROJECT_METADATA",
      "connectionLogging": "CONNECTION_LOGGING"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the quota project. API requests are counted against this project. For more information, see the [**Quotas and System Limits** page](https://console.cloud.google.com/iam-admin/quotas?service=networkmanagement.googleapis.com&metric=api-requests) in the Google Cloud console.
  * `ORGANIZATION_ID`: the ID of the organization.
  * `CONFIG_NAME`: a name for the configuration.

To set the optional parameters in a custom configuration, replace the following: 
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `INTERVAL_5_SEC` (default), `INTERVAL_30_SEC`, `INTERVAL_1_MIN`, `INTERVAL_5_MIN`, `INTERVAL_10_MIN`, or `INTERVAL_15_MIN`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `INCLUDE_ALL_METADATA` to include all metadata annotations (default).
    * Use `EXCLUDE_ALL_METADATA` to exclude all metadata annotations.
    * Use `CUSTOM_METADATA` to include a custom list of metadata fields. To specify the metadata fields, use the `metadataFields` parameter: 
      * `metadataFields: METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `CUSTOM_METADATA`.


  * `CROSS_PROJECT_METADATA`: cross-project annotations. Can be set to `CROSS_PROJECT_METADATA_ENABLED` (default) or `CROSS_PROJECT_METADATA_DISABLED`. For more information, see [Cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project).
  * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `ENABLED` or `DISABLED` (default). If enabled, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).



When VPC Flow Logs is enabled for an organization, flow logs are written and billed to the Google Cloud project of the resource that reports flow logs. For more information, see [Pricing and billing](https://docs.cloud.google.com/vpc/docs/flow-logs#pricing).

## View VPC Flow Logs configuration status

You can check which resources have VPC Flow Logs enabled by viewing their VPC Flow Logs configurations. To view all configurations, see View VPC Flow Logs configurations (all). If you use the Compute Engine API to enable and manage VPC Flow Logs, see View VPC Flow Logs configurations (Compute Engine API only).

### View VPC Flow Logs configurations (all)

###  Console 

To view all VPC Flow Logs configurations, do the following:

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. In the **Organization-level configurations** and **Project-level configurations** sections, view your active and paused configurations. If the status of a VPC Flow Logs configuration for a resource is **On** , it means that logging is turned on.




You can also view VPC Flow Logs configurations in the **Flow log configs** column on the resource page. For example, to view which VPC networks and subnets have VPC Flow Logs configurations:

  1. Go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the **Networks in current project** or **Subnets in current project** tab and in the **Flow log configs** column, view your active and paused VPC Flow Logs configurations.




###  gcloud 

To view VPC Flow Logs configurations, use the [`gcloud network-management vpc-flow-logs-configs list`](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/list) and [`gcloud network-management vpc-flow-logs-configs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/describe) commands.

#### View organization-level configurations

  * To view all VPC Flow Logs configurations for an organization, run the following command:
        
        gcloud network-management vpc-flow-logs-configs list --location=global \
            --organization=ORGANIZATION
        

  * To view a specific VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs describe CONFIG_NAME \
            --location=global \
            --organization=ORGANIZATION
        

Replace the following:

    * `ORGANIZATION`: the ID of the organization
    * `CONFIG_NAME`: the name of the configuration



#### View project-level configurations

  * To view all VPC Flow Logs configurations in a project, run the following command:
        
        gcloud network-management vpc-flow-logs-configs list --location=global
        

  * To view a specific VPC Flow Logs configuration, run the following command:
        
        gcloud network-management vpc-flow-logs-configs describe CONFIG_NAME \
            --location=global
        

Replace `CONFIG_NAME` with the name of the VPC Flow Logs configuration that you want to view.




#### View all configurations for a resource

To view all VPC Flow Logs configurations for a VPC network, subnet, VLAN attachment, or a VPN tunnel, run the following command:
    
    
    gcloud network-management vpc-flow-logs-configs show-effective-flow-logs-configs \
        --location=global \
        --resource=TARGET_RESOURCE
    

Replace `TARGET_RESOURCE` with one of the following resources:

  * `"projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET"`: lists all configurations for the subnet, including the following:

    * All configurations for which the subnet is the target resource
    * All configurations for the VPC network of the subnet
    * All configurations for the organization that owns the project of the subnet
    * Compute Engine API only: the VPC Flow Logs configuration for the subnet

To identify the configuration in the output, look for `"scope": "COMPUTE_API_SUBNET"`. This configuration doesn't exist if you use only the Network Management API to configure VPC Flow Logs.

  * `"projects/PROJECT_ID/regions/REGION/interconnectAttachments/VLAN_ATTACHMENT"`: lists all configurations for the VLAN attachment, including the following:

    * All configurations for which the VLAN attachment is the target resource
    * All configurations for the VPC network of the VLAN attachment
    * All configurations for the organization that owns the project of the VLAN attachment
  * `"projects/PROJECT_ID/regions/REGION/vpnTunnels/VPN_TUNNEL"`: lists all configurations for the Cloud VPN tunnel, including the following:

    * All configurations for which the Cloud VPN tunnel is the target resource
    * All configurations for the VPC network of the Cloud VPN tunnel
    * All configurations for the organization that owns the project of the Cloud VPN tunnel
  * `"projects/PROJECT_ID/global/networks/NETWORK"`: lists all configurations for the VPC network, including the following:

    * All configurations for which the network is the target resource
    * All configurations for the organization that owns the project of the network



When specifying the target resource, replace the following:

  * `PROJECT_ID`: the project ID of the target resource
  * `REGION`: the region of the target resource, if the resource is a subnet, VLAN attachment, or VPN tunnel
  * `SUBNET`: the name of the subnet
  * `VLAN_ATTACHMENT`: the name of the VLAN attachment
  * `VPN_TUNNEL`: the name of the VPN tunnel
  * `NETWORK`: the name of the network



###  API 

#### View organization-level configurations

  * To view all VPC Flow Logs configurations for an organization, use the `organizations.locations.vpcFlowLogsConfigs.list` method:
        
        GET -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs
        

  * To view a specific VPC Flow Logs configuration for an organization, use the `organizations.locations.vpcFlowLogsConfigs.get` method:
        
        GET -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME
        

Replace the following:

    * `PROJECT_ID`: the ID of the quota project. API requests are counted against this project.
    * `ORGANIZATION_ID`: the ID of the organization.
    * `CONFIG_NAME`: the name of the configuration.
  * If you don't have the necessary permissions to perform the preceding tasks at the organization level, you can use the following request to view all VPC Flow Logs configurations for the organization of your project:
        
        GET https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs:queryOrgVpcFlowLogsConfigs
        

Replace `PROJECT_ID` with the ID of the project.




#### View project-level configurations

  * To view all VPC Flow Logs configurations in a project, use the [`projects.locations.vpcFlowLogsConfigs.list` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/list):
        
        GET https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs
        

  * To view a specific VPC Flow Logs configuration, use the [`projects.locations.vpcFlowLogsConfigs.get` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/get):
        
        GET https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME
        

Replace the following:

    * `PROJECT_ID`: the ID of the project
    * `CONFIG_NAME`: the name of the VPC Flow Logs configuration



#### View all configurations for a resource

To view all VPC Flow Logs configurations for a VPC network, subnet, VLAN attachment, or a VPN tunnel, use the following request:
    
    
      GET https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs:showEffectiveFlowLogsConfigs?resource="TARGET_RESOURCE"
      

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project
  * `TARGET_RESOURCE`: one of the following target resources:

    * `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET`: lists all configurations for the subnet, including the following:

      * All configurations for which the subnet is the target resource
      * All configurations for the VPC network of the subnet
      * All configurations for the organization that owns the project of the subnet
      * Compute Engine API only: the VPC Flow Logs configuration for the subnet

To identify the configuration in the output, look for `"scope": "COMPUTE_API_SUBNET"`. This configuration doesn't exist if you use only the Network Management API to configure VPC Flow Logs.

    * `projects/PROJECT_ID/regions/REGION/interconnectAttachments/VLAN_ATTACHMENT`: lists all configurations for the VLAN attachment, including the following:

      * All configurations for which the VLAN attachment is the target resource
      * All configurations for the VPC network of the VLAN attachment
      * All configurations for the organization that owns the project of the VLAN attachment
    * `projects/PROJECT_ID/regions/REGION/vpnTunnels/VPN_TUNNEL`: lists all configurations for the Cloud VPN tunnel, including the following:

      * All configurations for which the Cloud VPN tunnel is the target resource
      * All configurations for the VPC network of the Cloud VPN tunnel
      * All configurations for the organization that owns the project of the Cloud VPN tunnel
    * `projects/PROJECT_ID/global/networks/NETWORK`: lists all configurations for the VPC network, including the following:

      * All configurations for which the network is the target resource
      * All configurations for the organization that owns the project of the network

When specifying the target resource, replace the following:

    * `PROJECT_ID`: the project ID of the target resource
    * `REGION`: the region of the target resource, if the resource is a subnet, VLAN attachment, or VPN tunnel
    * `SUBNET`: the name of the subnet
    * `VLAN_ATTACHMENT`: the name of the VLAN attachment
    * `VPN_TUNNEL`: the name of the VPN tunnel
    * `NETWORK`: the name of the network



### View VPC Flow Logs configurations (Compute Engine API only)

This section describes how to view which VPC Flow Logs configurations for subnets are managed by the Compute Engine API. To view all VPC Flow Logs configurations, see View VPC Flow Logs configurations.

###  Console 

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. In the **Project-level configurations** section, click the **Subnets (Compute Engine API)** tab and view which subnets in the project have VPC Flow Logs enabled.

These configurations are managed by the Compute Engine API. Configurations that are managed by the Network Management API are displayed in the **Subnets** tab.




###  gcloud 

To view which subnets in a VPC network have VPC Flow Logs enabled, run the following command:
    
    
    gcloud compute networks subnets list \
        --project PROJECT_ID \
        --network="NETWORK" \
        --format="csv(name,region,logConfig.enable)"

Replace the following:

  * `PROJECT_ID`: the ID of the project you are querying
  * `NETWORK`: the name of the network containing the subnets



## Update VPC Flow Logs configuration

You can update a VPC Flow Logs configuration. For more information about the parameters that you can modify, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).

### Update an organization-level configuration

Updating a VPC Flow Logs configuration for an organization applies the modified configuration to all subnets, VLAN attachments, and Cloud VPN tunnels in all VPC networks in the organization.

###  Console 

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. In the **Organization-level configurations** section, select one or more configurations that you want to update and click **Edit**.

  3. Adjust any of the following:

     * The **Aggregation interval**. By default, the aggregation interval is set to **5 sec**.
     * Whether to set the **Status** of the VPC Flow Logs configuration to on or off. The **On** status means that the selected VPC Flow Logs configuration is active and generates flow logs.
     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include cross-project annotations. By default, **Cross-project metadata annotations** is selected. For more information, see [Cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project).
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * Whether to enable TCP connection logging. By default, **Connection logging** is deselected. If selected, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  4. Click **Save**.




###  gcloud 

Use the [`gcloud network-management vpc-flow-logs-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/update). The square brackets `[]` in the following commands indicate optional parameters.

To update a VPC Flow Logs configuration for an organization, run the following command:
    
    
    gcloud network-management vpc-flow-logs-configs update CONFIG_NAME \
        --location=global \
        --organization=ORGANIZATION \
        [--aggregation-interval=AGGREGATION_INTERVAL] \
        [--filter-expr=FILTER_EXPRESSION] \
        [--flow-sampling=SAMPLING_RATE] \
        [--metadata=LOGGING_METADATA] \
        [--cross-project-metadata=CROSS_PROJECT_METADATA] \
        [--connection-logging=CONNECTION_LOGGING] \
        [--state=STATE]
    

For example, to update the aggregation interval parameter, run the following command:
    
    
    gcloud network-management vpc-flow-logs-configs update CONFIG_NAME \
        --location=global \
        --organization=ORGANIZATION \
        --aggregation-interval=AGGREGATION_INTERVAL
    

Replace the following:

  * `CONFIG_NAME`: the name of the configuration that you want to update. The configuration is located in the same Google Cloud project as the resource for which the configuration is used.
  * `ORGANIZATION`: the ID of the organization.



To update the optional parameters, replace the following:

  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `include-all-metadata` to include all metadata annotations (default).
    * Use `exclude-all-metadata` to exclude all metadata annotations.
    * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
      * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.
  * `CROSS_PROJECT_METADATA`: cross-project annotations. Can be set to `cross-project-metadata-enabled` (default) or `cross-project-metadata-disabled`. For more information, see [Cross-project annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#cross-project).
  * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `enabled` or `disabled` (default). If enabled, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
  * `STATE`: the state of the configuration. Can be `enabled` (default) or `disabled`.



###  API 

Use the `organizations.locations.vpcFlowLogsConfigs.patch` method. For information about the fields that you can modify, see [REST Resource: projects.locations.vpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig).

To update a VPC Flow Logs configuration for an organization, include the following parameters in your API request:
    
    
    PATCH -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME?updateMask=FIELDS
    {
      ...fields to modify
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the quota project. API requests are counted against this project. For more information, see the [**Quotas and System Limits** page](https://console.cloud.google.com/iam-admin/quotas?service=networkmanagement.googleapis.com&metric=api-requests) in the Google Cloud console.
  * `ORGANIZATION_ID`: the ID of the organization for which the configuration is used.
  * `CONFIG_NAME`: the name of the configuration that you want to update.
  * `FIELDS`: the name of the field or fields that you want to update, comma-separated—for example, `aggregationInterval,flowSampling,metadata,connectionLogging`.



For example, to update the `aggregationInterval` field for a configuration `my-config` in `my-organization`, use the following API request:
    
    
    PATCH -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/my-organization/locations/global/vpcFlowLogsConfigs/my-config?updateMask=aggregationInterval
    {
      aggregationInterval:AGGREGATION_INTERVAL
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the quota project. API requests are counted against this project.
  * `AGGREGATION_INTERVAL` with any of the supported values for this parameter.



### Update a project-level configuration

Project-level configurations include configurations for VPC networks, subnets, VLAN attachments, and Cloud VPN tunnels. Updating a VPC Flow Logs configuration for a VPC network applies the modified configuration to all subnets, VLAN attachments, and Cloud VPN tunnels in the network.

To update a VPC Flow Logs configuration managed by the Compute Engine API, see Update configuration parameters for subnets.

###  Console 

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. In the **Project-level configurations** section, select one or more configurations that you want to update and click **Edit**.

  3. Adjust any of the following:

     * The **Aggregation interval**. By default, the aggregation interval is set to **5 sec**.
     * Whether to set the **Status** of the VPC Flow Logs configuration to on or off. The **On** status means that the selected VPC Flow Logs configuration is active and generates flow logs.
     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * Whether to enable TCP connection logging. By default, **Connection logging** is deselected. If selected, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
     * The **Secondary sampling rate**. `100%` means that all entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  4. Click **Save**.




You can also use the menu **Manage flow logs** menu in the following locations to edit your VPC Flow Logs configurations:

  * The **Networks in current project** and **Subnets in current project** tabs on the [VPC networks](https://console.cloud.google.com/networking/networks/list) page
  * The **VLAN attachments** tab on the [Interconnect](https://console.cloud.google.com/hybrid/interconnects) page
  * The **VPN tunnels** tab on the [VPN](https://console.cloud.google.com/hybrid/vpn) page



###  gcloud 

Use the [`gcloud network-management vpc-flow-logs-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/update). The square brackets `[]` in the following command indicate optional parameters.
    
    
    gcloud network-management vpc-flow-logs-configs update CONFIG_NAME \
        --location=global \
        [--network=NETWORK | --subnet=SUBNET | --interconnect-attachment=VLAN_ATTACHMENT | --vpn-tunnel=VPN_TUNNEL] \
        [--aggregation-interval=AGGREGATION_INTERVAL] \
        [--filter-expr=FILTER_EXPRESSION] \
        [--flow-sampling=SAMPLING_RATE] \
        [--metadata=LOGGING_METADATA] \
        [--connection-logging=CONNECTION_LOGGING] \
        [--state=STATE]
    

For example, to update the aggregation interval parameter, run the following command:
    
    
    gcloud network-management vpc-flow-logs-configs update CONFIG_NAME \
        --location=global \
        --aggregation-interval=AGGREGATION_INTERVAL
    

Replace the following:

  * `CONFIG_NAME`: the name of the configuration that you want to update. The configuration is located in the same Google Cloud project as the resource for which the configuration is used.



To update the optional parameters, replace the following:

  * `NETWORK`, `SUBNET`, `VLAN_ATTACHMENT`, or `VPN_TUNNEL`: the name of the target resource. Only one resource can be specified per configuration. Use this option to update the name of the target resource. Must be specified in the following format: 
    * VPC network: `projects/PROJECT_ID/global/networks/NAME`
    * Subnet: `projects/PROJECT_ID/regions/REGION/subnetworks/NAME`
    * VLAN attachment: `projects/PROJECT_ID/regions/REGION/interconnectAttachments/NAME`
    * Cloud VPN tunnel: `projects/PROJECT_ID/regions/REGION/vpnTunnels/NAME`
    * Replace the following: 
      * `PROJECT_ID`: the ID of the Google Cloud project that contains the resource.
      * `REGION`: the region of the resource.
      * `NAME`: the name of the resource.
  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs generated by this configuration. This parameter can be set to `interval-5-sec`(default), `interval-30-sec`, `interval-1-min`, `interval-5-min`,`interval-10-min`, or `interval-15-min`. 
  * `FILTER_EXPRESSION`: an expression that defines which logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and [Examples of log filters](https://docs.cloud.google.com/vpc/docs/using-flow-logs#filtering-examples). 
  * `SAMPLING_RATE`: the secondary flow sampling rate. This parameter can be set from greater than `0.0` to `1.0` (all logs, default). For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling). 
  * `LOGGING_METADATA`: the metadata annotations that you want to include in the logs: 
    * Use `include-all-metadata` to include all metadata annotations (default).
    * Use `exclude-all-metadata` to exclude all metadata annotations.
    * Use `custom-metadata` to include a custom list of metadata fields. To specify the metadata fields, use the `--metadata-fields` flag: 
      * `--metadata-fields=METADATA_FIELDS`: replace `METADATA_FIELDS` with a comma-separated list of metadata fields that you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `metadata` is set to `custom-metadata`.
  * `CONNECTION_LOGGING`: TCP connection logging. Can be set to `enabled` or `disabled` (default). If enabled, VPC Flow Logs captures connection events for TCP traffic from and to VMs and serverless endpoints. For more information, see [TCP connection logging](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging).
  * `STATE`: the state of the configuration. Can be `enabled` (default) or `disabled`.



###  API 

Use the [`projects.locations.vpcFlowLogsConfigs.patch` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/patch). For information about the fields that you can modify, see [REST Resource: projects.locations.vpcFlowLogsConfigs](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig).

To update a VPC Flow Logs configuration, include the following parameters in your API request:
    
    
    PATCH https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME?updateMask=FIELDS
    {
      ...fields to modify
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that contains the VPC Flow Logs configuration. This ID is the same as the project ID of the resource for which the configuration is used.
  * `CONFIG_NAME`: the name of the configuration that you want to update.
  * `FIELDS`: the name of the field or fields that you want to update, comma-separated—for example, `aggregationInterval,flowSampling,metadata,connectionLogging`. 



For example, to update the `aggregationInterval` field for a configuration `my-config` in `my-project`, use the following API request:
    
    
    PATCH https://networkmanagement.googleapis.com/v1/projects/my-project/locations/global/vpcFlowLogsConfigs/my-config?updateMask=aggregationInterval
    {
      aggregationInterval:AGGREGATION_INTERVAL
    }
    

Replace `AGGREGATION_INTERVAL` with any of the supported values for this parameter.

#### Update configuration parameters for subnets

This section describes how to update a VPC Flow Logs configuration managed by the Compute Engine API.

To view which VPC Flow Logs configurations are managed by the Compute Engine API, see View which subnets in a network have VPC Flow Logs enabled.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Under **Subnets in current project** , click the subnet that you want to update.

  3. Click **Edit**.

  4. Optional: Adjust any of the following settings:

     * The **Aggregation interval**. By default, the aggregation interval is set to **5 sec**.
     * Whether to configure log filtering. By default, **Keep only logs that match a filter** is deselected.
     * Whether to include metadata in the final log entries. By default, **Metadata annotations** includes all fields.
     * The **Secondary sampling rate**. `50%` means that half of entries generated by the primary flow log sampling process are kept. The primary flow log sampling rate isn't configurable. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  5. Click **Save**.




Alternatively, you can update your VPC Flow Logs configuration parameters by using the menu **Manage flow logs** menu under **Subnets in current project** on the [VPC networks](https://console.cloud.google.com/networking/networks/list) page.

###  gcloud 

Run the following command:
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        [--logging-aggregation-interval=AGGREGATION_INTERVAL] \
        [--logging-flow-sampling=SAMPLING_RATE] \
        [--logging-filter-expr=FILTER_EXPRESSION] \
        [--logging-metadata=LOGGING_METADATA] \
        [--logging-metadata-fields=METADATA_FIELDS] \
    

Replace the following:

  * `AGGREGATION_INTERVAL`: the aggregation interval for flow logs in that subnet. The interval can be set to any of the following: 5-sec (default), 30-sec, 1-min, 5-min, 10-min, or 15-min.
  * `SAMPLING_RATE`: the secondary flow sampling rate. Secondary flow sampling can be set from `0.0` (no sampling) to `1.0` (all logs). Default is `0.5`. For more information, see [Log sampling and processing](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling).
  * `FILTER_EXPRESSION`: an expression that defines what logs you want to keep. The expression has a limit of 2,048 characters. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) and Examples of log filters.
  * `LOGGING_METADATA`: the [metadata annotations](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#metadata) that you want to include in the logs:

    * Use `include-all` to include all metadata annotations.
    * Use `exclude-all` to exclude all metadata annotations (default).
    * Use `custom` to include a custom list of metadata fields that you specify in `METADATA_FIELDS`.
**Note:** If a subnet had flow logging enabled at any time before March 1, 2021, and if `LOGGING_METADATA` was never explicitly configured, the default value for `LOGGING_METADATA` is `include-all`.
  * `METADATA_FIELDS`: a comma-separated list of metadata fields you want to include in the logs. For example, `src_instance,dst_instance`. Can be set only if `LOGGING_METADATA` is set to `custom`.




###  API 

Modify the log sampling fields to update VPC Flow Logs behaviors.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    {
      "logConfig": {
        ...fields to modify
      },
      "fingerprint": "SUBNET_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the subnet is located.
  * `REGION`: the region where the subnet is located.
  * `SUBNET_NAME`: the name of the existing subnet.
  * `SUBNET_FINGERPRINT`: the fingerprint ID for the existing subnet, which is provided when you [describe a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet).
  * For the fields that you can modify, see Enable VPC Flow Logs when you create a subnet.



For more information, see the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).

## Stop logs collection

You can pause logs collection for a resource by turning off all of its active VPC Flow Logs configurations.

If you no longer need a VPC Flow Logs configuration, you can delete the configuration. Logs collection is stopped and the configuration is deleted.

To stop collecting only [TCP connection logs](https://docs.cloud.google.com/vpc/docs/flow-logs#connection-logging), update the configuration to set connection logging to disabled.

To stop logs collection and delete a VPC Flow Logs configuration managed by the Compute Engine API, see disable VPC Flow Logs for a subnet.

### Turn off a VPC Flow Logs configuration

###  Console 

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. In the **Organization-level configurations** or **Project-level configurations** sections, select one or more VPC Flow Logs configurations that you want to turn off and change the configuration status to **Turn off**.

If your selection includes both active and inactive configurations, in the **Change configuration status** menu, click **Turn all off**.




###  gcloud 

To pause logs collection for a VPC Flow Logs configuration, use the [`gcloud network-management vpc-flow-logs-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/update).

**Pause an organization-level configuration**
    
    
    gcloud network-management vpc-flow-logs-configs update CONFIG_NAME \
        --location=global \
        --organization=ORGANIZATION \
        --state=disabled
    

Replace the following:

  * `CONFIG_NAME`: the name of the configuration
  * `ORGANIZATION`: the ID of the organization



**Pause a project-level configuration**
    
    
    gcloud network-management vpc-flow-logs-configs update CONFIG_NAME \
        --location=global \
        --state=disabled
    

Replace `CONFIG_NAME` with the name of the configuration.

###  API 

**Pause an organization-level configuration**

To pause logs collection, use the `organizations.locations.vpcFlowLogsConfigs.patch` method.
    
    
    PATCH -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME?updateMask=state
    {
      "state": "DISABLED"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the quota project. API requests are counted against this project.
  * `ORGANIZATION_ID`: the ID of the organization.
  * `CONFIG_NAME`: the name of the configuration.



**Pause a project-level configuration**

To pause logs collection, use the [`projects.locations.vpcFlowLogsConfigs.patch` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/patch).
    
    
    PATCH https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME?updateMask=state
    {
      "state": "DISABLED"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that contains the configuration. This ID is the same as the project ID of the resource for which the configuration is used.
  * `CONFIG_NAME`: the name of the configuration.



### Delete a VPC Flow Logs configuration

###  Console 

  1. In the Google Cloud console, go to the **VPC Flow Logs** page.

[Go to VPC Flow Logs](https://console.cloud.google.com/networking/vpc-flow-logs)

  2. In the **Organization-level configurations** or **Project-level configurations** sections, select one or more VPC Flow Logs configurations that you want to delete and click **Delete**.




###  gcloud 

To delete a VPC Flow Logs configuration, use the [`gcloud network-management vpc-flow-logs-configs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/delete).

**Delete an organization-level configuration**
    
    
    gcloud network-management vpc-flow-logs-configs delete CONFIG_NAME \
        --location=global \
        --organization=ORGANIZATION
    

Replace the following:

  * `CONFIG_NAME`: the name of the configuration
  * `ORGANIZATION`: the ID of the organization



**Delete a project-level configuration**
    
    
    gcloud network-management vpc-flow-logs-configs delete CONFIG_NAME \
        --location=global
    

Replace `CONFIG_NAME` with the name of the configuration that you want to delete.

###  API 

**Delete an organization-level configuration**

To delete a VPC Flow Logs configuration, use the `organizations.locations.vpcFlowLogsConfigs.delete` method.
    
    
    DELETE -H "x-goog-user-project:PROJECT_ID" https://networkmanagement.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the quota project. API requests are counted against this project.
  * `ORGANIZATION_ID`: the ID of the organization.
  * `CONFIG_NAME`: the name of the configuration.



**Delete a project-level configuration**

To delete a VPC Flow Logs configuration, use the [`projects.locations.vpcFlowLogsConfigs.delete` method](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/delete).
    
    
    DELETE https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/vpcFlowLogsConfigs/CONFIG_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that contains the configuration
  * `CONFIG_NAME`: the name of the configuration



#### Disable VPC Flow Logs for a subnet

This section describes how to delete a VPC Flow Logs configuration managed by the Compute Engine API. When you disable VPC Flow Logs for a subnet, logs collection is stopped and the configuration is deleted.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the subnet that you want to update.

  3. Click **Edit**.

  4. For **Flow logs** , select **Off**.

  5. Click **Save**.




###  gcloud 

Run the following command:
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --no-enable-flow-logs
    

###  API 

Disable VPC Flow Logs on a subnet to stop collecting log records.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    {
      "logConfig": {
        "enable": false
      },
      "fingerprint": "SUBNET_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the subnet is located
  * `REGION`: the region where the subnet is located
  * `SUBNET_NAME`: the name of the existing subnet
  * `SUBNET_FINGERPRINT`: the fingerprint ID for the existing subnet, which is provided when you [describe a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet)



For more information, see the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).

## Examples of log filters

This section provides examples of log filters that you can configure to only preserve logs that match the filter. For more information, see [Log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering).

**Example 1. Limit logs collection to a specific VM named`my-vm`**

In this case, only logs where the `src_instance` field as reported by the source of the traffic is `my-vm` or the `dst_instance` field as reported by the destination of the traffic is `my-vm` are recorded.
    
    
    gcloud network-management vpc-flow-logs-configs update my-config \
        --location=global \
        --filter-expr="(src_instance.vm_name == 'my-vm' && reporter=='SRC') || (dest_instance.vm_name == 'my-vm' && reporter=='DEST')"
    

If you enabled VPC Flow Logs by using the Compute Engine API, run the following command instead:
    
    
    gcloud compute networks subnets update my-subnet \
        --logging-filter-expr="(src_instance.vm_name == 'my-vm' && reporter=='SRC') || (dest_instance.vm_name == 'my-vm' && reporter=='DEST')"
    

**Example 2. Limit logs collection to packets whose source IP addresses are in the`10.0.0.0/8` subnet**
    
    
    gcloud network-management vpc-flow-logs-configs update my-config \
        --location=global \
        --filter-expr="inIpRange(connection.src_ip, '10.0.0.0/8')"
    

If you enabled VPC Flow Logs by using the Compute Engine API, run the following command instead:
    
    
    gcloud compute networks subnets update my-subnet \
        --logging-filter-expr="inIpRange(connection.src_ip, '10.0.0.0/8')"
    

**Example 3. Limit logs collection to VM traffic that is external to a VPC network**
    
    
    gcloud network-management vpc-flow-logs-configs update my-config \
        --location=global \
        --filter-expr="!(has(src_vpc.vpc_name) && has(dest_vpc.vpc_name))"
    

If you enabled VPC Flow Logs by using the Compute Engine API, run the following command instead:
    
    
    gcloud compute networks subnets update my-subnet \
        --logging-filter-expr="!(has(src_vpc.vpc_name) && has(dest_vpc.vpc_name))"
    

**Example 4. Limit logs collection to a specific destination VLAN attachment or Cloud VPN tunnel,`my-gateway`**
    
    
    gcloud network-management vpc-flow-logs-configs update my-config \
        --location=global \
        --filter-expr="dest_gateway.name == 'my-gateway'"
    

**Example 5. Limit logs collection to VLAN attachments**
    
    
    gcloud network-management vpc-flow-logs-configs update my-config \
        --location=global \
        --filter-expr="dest_gateway.type == 'INTERCONNECT_ATTACHMENT'"
    

**Example 6. Limit logs collection to a specific source VPC network,`my-network`**
    
    
    gcloud network-management vpc-flow-logs-configs update my-config \
        --location=global \
        --filter-expr="src_vpc.vpc_name == 'my-network'"
    

## Troubleshooting

The following sections can help you diagnose issues with your VPC Flow Logs configuration.

### Flow logs for subnets appear to be disabled even though you enabled them

  * When you're configuring a proxy-only subnet for internal Application Load Balancers and you're using the `gcloud compute networks subnets` command to enable VPC Flow Logs, the command appears to succeed, but flow logs aren't actually enabled. The `--enable-flow-logs` flag doesn't take effect when you also include the `--purpose=INTERNAL_HTTPS_LOAD_BALANCER` flag.

When you use the Google Cloud console or the API to enable flow logs, you see the error message: "Invalid value for field 'resource.enableFlowLogs': 'true'. Invalid field set in subnetwork with purpose INTERNAL_HTTPS_LOAD_BALANCER."

Because proxy-only subnets have no VMs, VPC Flow Logs isn't supported. This is intended behavior.




## What's next

  * [Access flow logs](https://docs.cloud.google.com/vpc/docs/access-flow-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
