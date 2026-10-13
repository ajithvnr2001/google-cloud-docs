---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolAutoConfigOrBuilder
title: Interface NodePoolAutoConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:13.656441+00:00
---

# Interface NodePoolAutoConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolAutoConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface NodePoolAutoConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface NodePoolAutoConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLinuxNodeConfig()
    
    
    public abstract LinuxNodeConfig getLinuxNodeConfig()

Output only. Configuration options for Linux nodes.

` .google.container.v1.LinuxNodeConfig linux_node_config = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig)` | The linuxNodeConfig.  
  
### getLinuxNodeConfigOrBuilder()
    
    
    public abstract LinuxNodeConfigOrBuilder getLinuxNodeConfigOrBuilder()

Output only. Configuration options for Linux nodes.

` .google.container.v1.LinuxNodeConfig linux_node_config = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfigOrBuilder)` |   
  
### getNetworkTags()
    
    
    public abstract NetworkTags getNetworkTags()

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster creation. Each tag within the list must comply with RFC1035.

`.google.container.v1.NetworkTags network_tags = 1;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTags)` | The networkTags.  
  
### getNetworkTagsOrBuilder()
    
    
    public abstract NetworkTagsOrBuilder getNetworkTagsOrBuilder()

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster creation. Each tag within the list must comply with RFC1035.

`.google.container.v1.NetworkTags network_tags = 1;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NetworkTagsOrBuilder)` |   
  
### getNodeKubeletConfig()
    
    
    public abstract NodeKubeletConfig getNodeKubeletConfig()

NodeKubeletConfig controls the defaults for autoprovisioned node-pools.

Currently only `insecure_kubelet_readonly_port_enabled` can be set here.

`.google.container.v1.NodeKubeletConfig node_kubelet_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeKubeletConfig)` | The nodeKubeletConfig.  
  
### getNodeKubeletConfigOrBuilder()
    
    
    public abstract NodeKubeletConfigOrBuilder getNodeKubeletConfigOrBuilder()

NodeKubeletConfig controls the defaults for autoprovisioned node-pools.

Currently only `insecure_kubelet_readonly_port_enabled` can be set here.

`.google.container.v1.NodeKubeletConfig node_kubelet_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodeKubeletConfigOrBuilder)` |   
  
### getResourceManagerTags()
    
    
    public abstract ResourceManagerTags getResourceManagerTags()

Resource manager tag keys and values to be attached to the nodes for managing Compute Engine firewalls using Network Firewall Policies.

`.google.container.v1.ResourceManagerTags resource_manager_tags = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceManagerTags)` | The resourceManagerTags.  
  
### getResourceManagerTagsOrBuilder()
    
    
    public abstract ResourceManagerTagsOrBuilder getResourceManagerTagsOrBuilder()

Resource manager tag keys and values to be attached to the nodes for managing Compute Engine firewalls using Network Firewall Policies.

`.google.container.v1.ResourceManagerTags resource_manager_tags = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ResourceManagerTagsOrBuilder)` |   
  
### hasLinuxNodeConfig()
    
    
    public abstract boolean hasLinuxNodeConfig()

Output only. Configuration options for Linux nodes.

` .google.container.v1.LinuxNodeConfig linux_node_config = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the linuxNodeConfig field is set.  
  
### hasNetworkTags()
    
    
    public abstract boolean hasNetworkTags()

The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster creation. Each tag within the list must comply with RFC1035.

`.google.container.v1.NetworkTags network_tags = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkTags field is set.  
  
### hasNodeKubeletConfig()
    
    
    public abstract boolean hasNodeKubeletConfig()

NodeKubeletConfig controls the defaults for autoprovisioned node-pools.

Currently only `insecure_kubelet_readonly_port_enabled` can be set here.

`.google.container.v1.NodeKubeletConfig node_kubelet_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nodeKubeletConfig field is set.  
  
### hasResourceManagerTags()
    
    
    public abstract boolean hasResourceManagerTags()

Resource manager tag keys and values to be attached to the nodes for managing Compute Engine firewalls using Network Firewall Policies.

`.google.container.v1.ResourceManagerTags resource_manager_tags = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resourceManagerTags field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
