---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vpc-clusters/
title: Troubleshoot IP address management in VPC clusters \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:20.850358+00:00
---

# Troubleshoot IP address management in VPC clusters  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vpc-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Troubleshoot IP address management in VPC clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Effective IP address management is crucial for the stability and scalability of Google Kubernetes Engine (GKE) [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips). Problems can prevent scaling, or cause workload failures such as Pods failing to schedule.

Use this document to troubleshoot and fix issues related to IP address allocation, network stability, and advanced networking features in GKE VPC-native clusters.

This information is primarily for Platform admins and operators who manage the cluster's network infrastructure. It also helps Application developers understand how underlying network limitations, such as exhausted IP address space, can affect their workloads. While developers might not directly configure VPCs, understanding these common issues helps them better collaborate with Platform admins and operators for quicker resolutions. For more information about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Diagnose IP address exhaustion

Running out of IP addresses in your cluster can prevent node scaling and disrupt your workloads. This section explains how to use IP address utilization monitoring in GKE to detect and resolve potential exhaustion issues.

GKE calculates IP address utilization using data from [ Network Analyzer insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer) and other GKE data sources. This monitoring is available for all VPC-native clusters.

To view a cluster's IP address utilization, do the following:

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster that you want to examine. This action opens the cluster's **Details** page.

  3. Navigate to the **IP utilization** page using one of the following methods:

     * Select the **Observability** tab, then in the observability navigation menu, click **IP utilization**.

     * In the **Networking** section, find the **Cluster Pod IPv4 range (default)** row, and click **View IP utilization**.

  4. Review the **Status of IP allocation** column. This column shows you the percentage of allocated IP addresses in your Pod's IP address range. GKE considers all IP addresses in a node's assigned CIDR range as allocated, regardless of whether individual IP addresses are assigned to Pods. This behavior means that the percentage reflects the entire Pod range for a node, not just the IP addresses in use. If clusters share the same IP address ranges, the utilization percentage shows their combined total.

  5. For a detailed view of IP address usage, including CIDR ranges, subnet information, and recommendations, click **Show details**.




If your IP address utilization is high (approaching 100%), consider these solutions to prevent IP address exhaustion:

  * Add more Pod IPv4 address ranges by using discontiguous [multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#cluster-add-pod-ipv4-range). This feature lets you add more IPv4 addresses for your Pods without needing to re-create your cluster or configure new subnets.
  * [Add more subnets with additional IPv4 address ranges in the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-subnet-cluster). This feature lets new node pools use IP addresses from newly added subnets.
  * Create a new cluster with a lower value for the maximum number of Pods. This approach reserves fewer IP addresses for each node, which can help you manage the overall IP address consumption in your cluster's network range. For more information, see [Configure maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr).
  * If you don't have enough IP address ranges or RFC 1918 address space, consider [non-RFC 1918 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) (including the Class E address space).



## Troubleshoot specific networking issues

The following sections provide guidance for resolving issues related to VPC-native clusters. You can also [view GKE IP address utilization insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/kubernetes-engine/gke-ip-utilization).

**Tip:** You can use `gcpdiag` to automate IP address exhaustion investigation.

### The default network resource is not ready

Symptoms
    

You get an error message similar to the following:
    
    
    projects/[PROJECT_NAME]/regions/XXX/subnetworks/default
    

Potential causes
    

There are parallel operations on the same subnet. For example, another VPC-native cluster is being created, or a secondary range is being added or deleted on the subnet.

Resolution
    

Retry the command.

### Invalid value for `IPCidrRange`

Symptoms
    

You get an error message similar to the following:
    
    
    resource.secondaryIpRanges[1].ipCidrRange': 'XXX'. Invalid IPCidrRange: XXX conflicts with existing subnetwork 'default' in region 'XXX'
    

Potential causes
    

Another VPC-native cluster is being created at the same time and is attempting to allocate the same ranges in the same VPC network.

    

The same secondary range is being added to the subnetwork in the same VPC network.

Resolution
    

If this error is returned on cluster creation when no secondary ranges were specified, retry the cluster creation command.

### Not enough free IP address space for Pods

Symptoms
    

Cluster is stuck in a provisioning state for an extended period of time.

    

Cluster creation returns a Managed Instance Group (MIG) error.

    

When you add one or more nodes to a cluster, the follow error appears:
    
    
    [IP_SPACE_EXHAUSTED] Instance 'INSTANCE_NAME' creation failed: IP space of 'projects/PROJECT_ID/regions/REGION/subnetworks/[SUBNET_NAME]-[SECONDARY_RANGE_NAME]-[HASH_8BYTES]' is exhausted. The secondary range name is in the format of 'gke-[CLUSTER_NAME]-[HASH_8BYTES]'.
    

Potential causes
    

**Node IP address exhaustion:** The primary IP address range of the subnet assigned to your cluster runs out of available IP addresses. This typically happens when scaling node pools or creating large clusters.

    

**High initial node count in scaled-down node pools:** GKE reserves IP addresses for Pods based on the initial capacity that you requested when you created a node pool. If you create a node pool with a high `initial_node_count` and then scale down the number of nodes, GKE continues to reserve IP address space based on the greater of the node pool's `initial_node_count` or the current number of nodes in the node pool. This situation can lead to a state where the cluster reports IP address exhaustion even if the current number of active nodes is low.

    

**Pod IP address exhaustion:** The Pod CIDR range assigned to your cluster is full. This occurs when the number of Pods exceeds the capacity of the Pod CIDR, especially with high Pod density per node or large deployments.

    

**Specific subnet naming conventions:** The way a subnet is named in an error message can help you figure out if the problem is with the node IP address range (where the nodes themselves get their IP address) or the Pod IP address range (where the containers inside the Pods get their IP addresses).

    

**Secondary range exhaustion (Autopilot):** In Autopilot clusters, secondary ranges assigned for Pod IP addresses are exhausted due to scaling or high Pod density.

Solution
    

Gather the following information about your cluster: name, control plane version, mode of operation, associated VPC name, and subnet name and CIDR. Additionally, note the default and any additional Cluster Pod IPv4 ranges (including names and CIDRs), whether VPC-native traffic routing is enabled, and the maximum Pods per node setting at both the cluster and node pool levels (if applicable). Note any impacted node pools and their specific IPv4 Pod IP address ranges and maximum Pods per node configurations if they differ from the cluster-wide settings. Also, record the default and custom (if any) configurations for maximum Pods per node in the node pool configuration.

    

Confirm IP address exhaustion issue

  * Network Intelligence Center: Check for high IP address allocation rates in the Pod IP address ranges in the Network Intelligence Center for your GKE cluster.

If you observe a high IP address allocation rate in the Pod ranges within Network Intelligence Center, then your Pod IP address range is exhausted.

If the Pod IP address ranges show normal allocation rates, but you are still experiencing IP address exhaustion, then it's likely your node IP address range is exhausted.

  * Audit logs: Examine the `resourceName` field in `IP_SPACE_EXHAUSTED` entries, comparing it to subnet names or secondary Pod IP address range names.

  * Check whether exhausted IP address range is node IP address range or Pod IP address range.

To verify whether exhausted IP address range is node IP address range or Pod IP address range, check whether the value of `resourceName` in the `ipSpaceExhausted` portion of a `IP_SPACE_EXHAUSTED` log entry correlates with subnet name or name of secondary IPv4 address range for Pods used in the impacted GKE cluster.

If value of `resourceName` is in format "[Subnet_name]", then node IP address range is exhausted. If value of resourceName is in format "[Subnet_name]-[Name_of_Secondary_IPv4_range_for_pods]-[HASH_8BYTES]", then Pod IP address range is exhausted.

**Note:** GKE truncates long strings used in subnet name and name of secondary IPv4 address range for Pods to 15 characters.


    

Resolve Pod IP address exhaustion:

  * Resize existing Pod CIDR: Increase the size of the current Pod IP address range. You can add Pod IP ranges to the cluster using [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).
  * Create additional subnets: Add subnets with dedicated Pod CIDRs to the cluster.


    

Reduce Pods per node to free up IP addresses:

  * Create a new node pool with a smaller [maximum number of Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr).
  * Migrate workloads to that node pool, and then delete the previous node pool. Reducing the maximum number of Pods per node lets you support more nodes on a fixed secondary IP address range for Pods. Refer to [Subnet secondary IP address range for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_pods) and [Node limiting ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#node_limiters) for details about the calculations involved.


    

Address node IP address exhaustion:

  * Review IP address planning: Ensure the node IP address range aligns with your scaling requirements.
  * Create new cluster (if necessary): If the node IP address range is severely constrained, create a replacement cluster with appropriate IP address range sizing. Refer to [IP ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing) and [IP range planning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#defaults_limits).



### Debug IP address exhaustion issues with `gcpdiag`

[`gcpdiag`](https://gcpdiag.dev) is an open source tool. It is not an officially supported Google Cloud product. You can use the `gcpdiag` tool to help you identify and fix Google Cloud project issues. For more information, see the [gcpdiag project on GitHub](https://github.com/GoogleCloudPlatform/gcpdiag/#gcpdiag---diagnostics-for-google-cloud-platform).

To examine IP address exhaustion causes on Autopilot and Standard GKE clusters, consider the following: 

  * **Cluster status:** Checks the cluster status if IP address exhaustion is reported.
  * **Network analyzer:** Queries stackdriver logs for network analyzer logs to confirm if there is Pod or node IP address exhaustion.
  * **Cluster Type:** Checks the cluster type and provides relevant recommendations based on the cluster type.



## Google Cloud console

  1. Complete and then copy the following command. 
    
    gcpdiag runbook gke/ip-exhaustion \
        --parameter project_id=PROJECT_ID \
        --parameter name=CLUSTER_NAME \
        --parameter location=ZONE|REGION \
        --parameter start_time=yyyy-mm-ddThh:mm:ssZ \
        --parameter end_time=yyyy-mm-ddThh:mm:ssZ \

  2. Open the Google Cloud console and activate Cloud Shell.
[Open Cloud console](https://console.cloud.google.com/kubernetes/list/overview?cloudshell=true)
  3. Paste the copied command.
  4. Run the `gcpdiag` command, which downloads the `gcpdiag` docker image, and then performs diagnostic checks. If applicable, follow the output instructions to fix failed checks. 



## Docker

You can [ run `gcpdiag` using a wrapper](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#installation) that starts `gcpdiag` in a [Docker](https://www.docker.com/) container. Docker or [Podman](https://podman.io/) must be installed.

  1. Copy and run the following command on your local workstation. 
         
         curl https://gcpdiag.dev/gcpdiag.sh >gcpdiag && chmod +x gcpdiag

  2. Execute the `gcpdiag` command. 
         
         ./gcpdiag runbook gke/ip-exhaustion \
             --parameter project_id=PROJECT_ID \
             --parameter name=CLUSTER_NAME \
             --parameter location=ZONE|REGION \
             --parameter start_time=yyyy-mm-ddThh:mm:ssZ \
             --parameter end_time=yyyy-mm-ddThh:mm:ssZ \




View [available parameters](https://gcpdiag.dev/runbook/diagnostic-trees/gke/ip-exhaustion/#parameters) for this runbook.

Replace the following:

  * PROJECT_ID: The ID of the project containing the resource
  * CLUSTER_NAME: The name of the target GKE cluster within your project.
  * LOCATION: The zone or region in which your cluster is located.
  * start_time: The time the issue started.
  * end_time: The time the issue ended. Set current time if issue is ongoing.



Useful flags:

  * `--universe-domain`: If applicable, the [Trusted Partner Sovereign Cloud](https://cloud.google.com/blog/products/identity-security/new-sovereign-controls-for-gcp-via-assured-workloads) domain hosting the resource
  * `--parameter` or `-p`: Runbook parameters



For a list and description of all `gcpdiag` tool flags, see the [`gcpdiag` usage instructions](https://github.com/GoogleCloudPlatform/gcpdiag?tab=readme-ov-file#usage).

### Confirm whether default SNAT is disabled

Use the following command to check the status of default SNAT:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of your cluster.

The output is similar to the following:
    
    
    networkConfig:
      disableDefaultSnat: true
      network: ...
    

### Cannot use `--disable-default-snat` without `--enable-ip-alias`

This error message, and `must disable default sNAT (--disable-default-snat) before using public IP address privately in the cluster`, mean that you should explicitly set the `--disable-default-snat` flag when creating the cluster since you are using public IP addresses in your private cluster.

If you see error messages like `cannot disable default sNAT ...` , this means the default SNAT can't be disabled in your cluster. To resolve this issue, review your cluster configuration.

### Debugging Cloud NAT with default SNAT disabled

If you have a private cluster created with the `--disable-default-snat` flag and have set up Cloud NAT for internet access and you aren't seeing internet-bound traffic from your Pods, make sure that the Pod range is included in the Cloud NAT configuration.

If there is a problem with Pod to Pod communication, examine the iptables rules on the nodes to verify that the Pod ranges are not masqueraded by iptables rules.

For more information, see the [GKE IP masquerade documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent).

If you have not configured an IP masquerade agent for the cluster, GKE automatically ensures that Pod to Pod communication is not masqueraded. However, if an IP masquerade agent is configured, it overrides the default IP masquerade rules. Verify that additional rules are configured in the IP masquerade agent to ignore masquerading the Pod ranges.

### The dual-stack cluster network communication is not working as expected

Potential causes
    The firewall rules created by the GKE cluster don't include the allocated IPv6 addresses.
Resolution
    You can validate the firewall rule by following these steps:

  1. Verify the firewall rule content:
         
         gcloud compute firewall-rules describe FIREWALL_RULE_NAME
         

Replace `FIREWALL_RULE_NAME` with the name of the firewall rule.

Each dual-stack cluster creates a firewall rule that allows nodes and Pods to communicate with each other. The firewall rule content is similar to the following:
         
         allowed:
         - IPProtocol: esp
         - IPProtocol: ah
         - IPProtocol: sctp
         - IPProtocol: tcp
         - IPProtocol: udp
         - IPProtocol: '58'
         creationTimestamp: '2021-08-16T22:20:14.747-07:00'
         description: ''
         direction: INGRESS
         disabled: false
         enableLogging: false
         id: '7326842601032055265'
         kind: compute#firewall
         logConfig:
           enable: false
         name: gke-ipv6-4-3d8e9c78-ipv6-all
         network: https://www.googleapis.com/compute/alpha/projects/my-project/global/networks/alphanet
         priority: 1000
         selfLink: https://www.googleapis.com/compute/alpha/projects/my-project/global/firewalls/gke-ipv6-4-3d8e9c78-ipv6-all
         selfLinkWithId: https://www.googleapis.com/compute/alpha/projects/my-project/global/firewalls/7326842601032055265
         sourceRanges:
         - 2600:1900:4120:fabf::/64
         targetTags:
         - gke-ipv6-4-3d8e9c78-node
         

The `sourceRanges` value must be the same as the `subnetIpv6CidrBlock`. The `targetTags` value must be the same as the tags on the GKE nodes. To fix this issue, [update the firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#updating_firewall_rules) with the cluster `ipAllocationPolicy` block information.




## What's next

  * For general information about diagnosing Kubernetes DNS issues, see [Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
