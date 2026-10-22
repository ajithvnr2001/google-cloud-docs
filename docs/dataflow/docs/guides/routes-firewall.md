---
url: https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall/
title: Configure internet access and firewall rules \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:12.556642+00:00
---

# Configure internet access and firewall rules  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Configure internet access and firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to complete the following tasks:

  * Configure Dataflow virtual machine (VM) instances for internet access
  * Use tags to secure worker VM networking.
  * Define firewall rules for the network associated with your Dataflow jobs



This document requires that you have basic knowledge of Google Cloud networks. To define a network for your Dataflow job, see [Specify your network and subnetwork](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks). For more information about how to troubleshoot networking issues, see [Troubleshoot Dataflow networking issues](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-networking).

**Note:** The `default` network has configurations that allow Dataflow jobs to run. However, other services might also use this network. Make sure your changes to the `default` network are compatible with all of your services. Alternatively, create a separate network for Dataflow.

## Access to Google Cloud APIs for Dataflow

Dataflow worker virtual machines (VMs) must reach Google Cloud APIs and services. The set of dependent Google Cloud endpoints might change over time, but they all support VPC Service Controls. Use one of the following methods to configure access to Google Cloud APIs:

  * Configure [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). With Private Google Access, VMs that have only internal IP addresses can access IP addresses for Google Cloud and services.

  * Configure a [Private Service Connect endpoint IP address](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) to access Google Cloud APIs and services.

  * [Configure worker VMs](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip) with external IP addresses.




By default, firewall rules and DNS configurations allow access to Google Cloud APIs. However, you might be actively restricting access to a subset of Google Cloud APIs, such as if you're using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity). In this case, at a minimum, provide access to `restricted.googleapis.com`. If you're using Private Service Connect, provide access to the `vpc-sc` [bundle](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis). Providing access to more permissive [domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-options), such as `private.googleapis.com`, also provides the required functionality.

To allow access to the necessary Google Cloud APIs through a given domain, your environment must meet the following requirements:

  * Firewall rules must allow egress to all address ranges under the chosen domain.

  * DNS must resolve `*.googleapis.com` to your chosen domain.




For example, if your firewall rules limit egress to the `restricted.googleapis.com` address range, then `*.googleapis.com` must resolve to addresses within that range. For more information, see [Configure DNS for googleapis.com](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#dns-config-google-apis).

Similarly, if you're using Private Service Connect, then you must [create DNS records](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default) for the `googleapis.com` default domain to ensure access to at least all services in the `vpc-sc` [bundle](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis).

## Internet access for Dataflow

Depending on your use case, your VMs might also need access to resources outside Google Cloud. Use one of the following methods to configure internet access for Dataflow:

  * [Configure worker VMs](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip) with an external IP address so that they meet the [internet access requirements](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs).

  * Configure a NAT solution, such as [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview). This option is for running jobs that access APIs and services outside of Google Cloud that require internet access. For example, Python SDK jobs might require access to the Python Package Index (PyPI) to download pipelines dependencies. In this case, you must either configure worker VMs with external IP addresses or use Cloud NAT. You can also supply Python pipeline dependencies during job submission. For example, you can [use custom containers](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) to supply Python pipeline dependencies, which removes the need to access PyPI at runtime.

For more information, see [Managing Python Pipeline Dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/) in the Apache Beam documentation.




### Turn off external IP address

By default, Dataflow assigns both external and internal IP addresses to workers. When you turn off external IP addresses, the Dataflow job can only access resources in the following places: 

  * Another instance in the same VPC network
  * A [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * A network with [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) enabled



Without external IP addresses, you can still perform administrative and monitoring tasks. You can access your workers by using SSH through the options listed in the preceding list. However, the pipeline cannot access the internet, and internet hosts cannot access your Dataflow workers.

By not using external IP addresses, you can better secure your data processing infrastructure. You can also reduce the number of external IP addresses that you consume against your [Google Cloud project quota](https://docs.cloud.google.com/vpc/docs/quota).

If you turn off external IP addresses, your Dataflow jobs cannot access APIs and services outside of Google Cloud that require internet access.

To turn off external IP addresses, do one of the following:

###  Java 

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for your network or subnetwork.
  2. In the parameters of your Dataflow job, specify `--usePublicIps=false` and `--network=NETWORK-NAME` or `--subnetwork=SUBNETWORK-NAME`. 

Depending on your choice, replace one of the following:

     * NETWORK-NAME: the name of your Compute Engine network
     * SUBNETWORK-NAME: the name of your Compute Engine subnetwork



###  Python 

  1. To stage all Python package dependencies, follow the Apache Beam [pipeline dependencies instructions](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/).
  2. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for your network or subnetwork.
  3. In the parameters of your Dataflow job, specify `--no_use_public_ips` and `--network=NETWORK` or `--subnetwork=SUBNETWORK`.

Depending on your choice, replace one of the following:

     * NETWORK-NAME: the name of your Compute Engine network
     * SUBNETWORK-NAME: the name of your Compute Engine subnetwork



###  Go 

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for your network or subnetwork.
  2. In the parameters of your Dataflow job, specify `--no_use_public_ips` and `--network=NETWORK` or `--subnetwork=SUBNETWORK`.

Depending on your choice, replace one of the following:

     * NETWORK-NAME: the name of your Compute Engine network
     * SUBNETWORK-NAME: the name of your Compute Engine subnetwork



## Use tags to secure worker VM networking

Tags let you apply network firewall rules to specific VM instances. When you run a Dataflow job, you can specify tags for the Dataflow worker VMs that execute the job. Any firewall rules for those tags are then applied to the Dataflow worker VMs.

Dataflow supports two types of tags for VM networking:

  * Secure tags
  * Network tags



### Use secure tags with Dataflow

[Secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview), also called Identity and Access Management (IAM)-governed tags, are key-value pairs that you create and manage in Resource Manager. Unlike network tags, secure tags support access control using IAM.

The benefits of using secure tags, instead of network tags, include the following:

  * Secure tags prevent unauthorized modification of tags and the resulting unwanted changes to firewall rules.

  * The [global](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [regional](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies) network firewall policies support secure tags. By using secure tags, you can group multiple firewall rules and update them simultaneously, with the updates governed by IAM access controls.

  * Secure tags inherit from parent resources in the Google Cloud hierarchy, which lets you define tags at higher levels, such as the organization level. For more information, see [Tag inheritance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).

  * With secure tags, ingress firewall rules can include sources in VPC networks connected using VPC Network Peering. For Dataflow jobs, that means a firewall rule can include sources in both the worker VM network and peered VPC networks.




For more information about the differences between secure tags and network tags, see [Comparison of Tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).

To apply secure tags to a Dataflow job, perform the following steps:

  1. Configure secure tags for your firewall policies. For more information, see [Configure secure tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#configure-secure-tags).

  2. Grant the **Tag User** role (`roles/resourcemanager.tagUser`) to the [Dataflow service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#df-service-account) on the resource (tag values). For more information about the necessary permissions, see [Manage tags on resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions-attach).

  3. When you create the Dataflow job, use the `use_vm_tags` [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options) with the following format:




### Java
    
    
    --dataflowServiceOptions=use_vm_tags=tagKeys/KEY1:tagValues/VALUE1;tagKeys/KEY2:tagValues/VALUE2
    

### Python
    
    
    --dataflow_service_options=use_vm_tags=tagKeys/KEY1:tagValues/VALUE1;tagKeys/KEY2:tagValues/VALUE2
    

### Go
    
    
    --dataflow_service_options=use_vm_tags=tagKeys/KEY1:tagValues/VALUE1;tagKeys/KEY2:tagValues/VALUE2
    

###  gcloud 

Use the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command with the `additional-experiments` option. If you're using Flex Templates, use the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command.
    
    
    --additional-experiments=use_vm_tags=tagKeys/KEY1:tagValues/VALUE1;tagKeys/KEY2:tagValues/VALUE2
    

### Use network tags with Dataflow

[Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) are text attributes that you can set on firewall rules and attach to Compute Engine VMs. Unlike secure tags, network tags are text strings; they aren't a resource that is managed by Resource Manager.

To apply network tags to a Dataflow job, use the `use_network_tags` [experiment](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#experimental), as follows:

### Java
    
    
    --dataflowServiceOptions=use_network_tags=TAG_NAME
    

### Python
    
    
    --dataflow_service_options=use_network_tags=TAG_NAME
    

### Go
    
    
    --dataflow_service_options=use_network_tags=TAG_NAME
    

###  gcloud 

Use the [`gcloud dataflow jobs run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run) command with the `additional-experiments` option. If you're using Flex Templates, use the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command.
    
    
    --additional-experiments=use_network_tags=TAG_NAME
    

Specifying the network tag also adds the default network tag `Dataflow` to Flex template launcher VMs.

Replace TAG_NAME with the names of your tags. If you add more than one tag, separate each tag with a semicolon (`;`), as follows: `TAG_NAME_1;TAG_NAME_2;TAG_NAME_3;...`.

After a job starts, you cannot add more network tags to the job.

Dataflow always adds the default network tag `dataflow` to every worker VM it creates.

See the [limits](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) that apply to network tags.

## Firewall rules for Dataflow

Firewall rules let you allow or deny traffic to and from your VMs. If your Dataflow jobs use [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) or [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine), then you only need to ensure that firewall rules allow access to Google Cloud APIs. Otherwise, you must configure additional firewalls rules so that Dataflow VMs can send and receive network traffic on TCP port `12345` for streaming jobs and on TCP port `12346` for batch jobs. A project owner, editor, or security administrator must create necessary firewall rules in the VPC network used by your Dataflow VMs.

Before you configure firewall rules for Dataflow, read the following documents:

  * [VPC firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls) and [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls)

  * [Hierarchical firewall policies overview](https://docs.cloud.google.com/vpc/docs/firewall-policies) and [Use Hierarchical firewall policies and rules](https://docs.cloud.google.com/vpc/docs/using-firewall-policies)




When you create firewall rules for Dataflow, specify the Dataflow network tags. Otherwise, the firewall rules apply to all VMs in the VPC network.

Where applicable, Hierarchical firewall policies are evaluated first and these rules preempt VPC firewall rules. If the Dataflow job is in a project which is part of a folder or organization where Hierarchical firewall policies are used, the `compute.orgFirewallPolicyAdmin` role is required to make policy modifications.

If you don't create custom network tags when you run the pipeline code, Dataflow VMs use the default `dataflow` tag. In the absence of custom network tags, create the firewall rules with the default `dataflow` tag.

If you create custom network tags when you run the pipeline code, Dataflow VMs use those tags. Create the firewall rules with the custom tags.

Some VPC networks, such as the automatically created `default` network, include a `default-allow-internal` rule that meets the firewall requirement for Dataflow.

### Example firewall ingress rule

The ingress firewall rule permits Dataflow VMs to receive packets from each other. You must always create ingress allow firewall rules or traffic is always blocked, even if egress rules allow such traffic.

In the following example, a firewall ingress rule is created for Dataflow, where all worker VMs have the default network tag `dataflow`. A project owner, editor, or security admin can use the following `gcloud` command to create an ingress allow rule that permits traffic on TCP ports `12345` and `12346` from VMs with the network tag `dataflow` to other VMs with the same tag:
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME_INGRESS \
        --action=allow \
        --direction=ingress \
        --network=NETWORK  \
        --target-tags=CUSTOM_TAG \
        --source-tags=CUSTOM_TAG \
        --priority=PRIORITY_NUM \
        --rules tcp:12345-12346
    

Replace the following:

  * `FIREWALL_RULE_NAME_INGRESS`: a name for the firewall rule

  * `NETWORK`: the name of the network that your worker VMs use

  * `CUSTOM_TAG`: a comma-delimited list of network tags

The following is a list of guidelines for using network tags:

    * If you omit `--target-tags`, the rule applies to all VMs in the VPC network.

    * If you omit `--source-tags` and all other source specifications, traffic from any source is allowed.

    * If you have not specified custom network tags and you want the rule to be specific to Dataflow VMs, use `dataflow` as the network tag.

    * If you have specified custom network tags and you want the rule to be specific to Dataflow VMs, use your custom network tags.

  * `PRIORITY_NUM`: the priority of the firewall rule

Lower numbers have higher priorities, and `0` is the highest priority.




### Example firewall egress rule

The egress firewall rule permits Dataflow VMs to send packets to each other. If you've created any egress deny firewall rules, you might need to create custom egress allow firewall rules in your VPC network.

In this example, a firewall egress rule is created for Dataflow, where all worker VMs have the default network tag of `dataflow`. A project owner, editor, or security administrator can use the following `gcloud` command to create an egress allow rule that permits traffic from TCP ports `12345` and `12346` on VMs with the network tag `dataflow` to other VMs with the same tag:
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME_EGRESS \
        --network=NETWORK \
        --action=allow \
        --direction=egress \
        --target-tags=CUSTOM_TAG \
        --source-tags=CUSTOM_TAG \
        --destination-ranges=DESTINATION-RANGES\
        --priority=PRIORITY_NUM  \
        --rules tcp:12345-12346
    

Replace the following:

  * `FIREWALL_RULE_NAME_EGRESS`: a name for the firewall rule

  * `NETWORK`: the name of the network that your worker VMs use

  * `CUSTOM_TAG`: a comma-delimited list of network tags

The following is a list of guidelines for using network tags:

    * If you omit `--target-tags`, the rule applies to all VMs in the VPC network.

    * If you omit `--source-tags` and all other source specifications, traffic from any source is allowed.

    * If you have not specified custom network tags and you want the rule to be specific to Dataflow VMs, use `dataflow` as the network tag.

    * If you have specified custom network tags and you want the rule to be specific to Dataflow VMs, use your custom network tags.

  * `DESTINATION-RANGES`: a comma-delimited list of CIDRs

Include the selected subnetwork's primary IP address range.

  * `PRIORITY_NUM`: the priority of the firewall rule

Lower numbers have higher priorities, and `0` is the highest priority.




For specific TCP ports used by Dataflow, you can [view the project container manifest](https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest#view_a_manifest). The container manifest explicitly specifies the ports in order to map host ports into the container.

## SSH access to worker VMs

Dataflow does not require SSH; however, SSH is useful for troubleshooting.

If your worker VM has an external IP address, you can [connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) through either the Google Cloud console or by using the Google Cloud CLI. To connect by using SSH, you must have a firewall rule that allows incoming connections on TCP port 22 from at least the IP address of the system on which you're running `gcloud` or the system running the web browser that you use to access the Google Cloud console.

You can view network configuration and activity by opening an [SSH session on one of your workers](https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh#sa_ssh) and running `iproute2`. For more information, see the [`iproute2` page](https://wiki.linuxfoundation.org/networking/iproute2) in the Linux Foundation wiki.

If you need to connect to a worker VM that only has an internal IP address, see [Choose a connection option for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip).

What's next

  * [Learn about Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview). Connectivity Tests is a diagnostics tool that lets you check connectivity between network endpoints.
  * [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
