---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.MembershipEndpointOrBuilder
title: Interface MembershipEndpointOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:25.615199+00:00
---

# Interface MembershipEndpointOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.MembershipEndpointOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MembershipEndpointOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.81.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.6  1.2.1  1.1.0  1.0.1  0.5.4 
    
    
    public interface MembershipEndpointOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApplianceCluster()
    
    
    public abstract ApplianceCluster getApplianceCluster()

Optional. Specific information for a GDC Edge Appliance cluster.

` .google.cloud.gkehub.v1beta1.ApplianceCluster appliance_cluster = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ApplianceCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.ApplianceCluster)` | The applianceCluster.  
  
### getApplianceClusterOrBuilder()
    
    
    public abstract ApplianceClusterOrBuilder getApplianceClusterOrBuilder()

Optional. Specific information for a GDC Edge Appliance cluster.

` .google.cloud.gkehub.v1beta1.ApplianceCluster appliance_cluster = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ApplianceClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.ApplianceClusterOrBuilder)` |   
  
### getEdgeCluster()
    
    
    public abstract EdgeCluster getEdgeCluster()

Optional. Specific information for a Google Edge cluster.

` .google.cloud.gkehub.v1beta1.EdgeCluster edge_cluster = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EdgeCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.EdgeCluster)` | The edgeCluster.  
  
### getEdgeClusterOrBuilder()
    
    
    public abstract EdgeClusterOrBuilder getEdgeClusterOrBuilder()

Optional. Specific information for a Google Edge cluster.

` .google.cloud.gkehub.v1beta1.EdgeCluster edge_cluster = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EdgeClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.EdgeClusterOrBuilder)` |   
  
### getGkeCluster()
    
    
    public abstract GkeCluster getGkeCluster()

Optional. Specific information for a GKE-on-GCP cluster.

` .google.cloud.gkehub.v1beta1.GkeCluster gke_cluster = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GkeCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.GkeCluster)` | The gkeCluster.  
  
### getGkeClusterOrBuilder()
    
    
    public abstract GkeClusterOrBuilder getGkeClusterOrBuilder()

Optional. Specific information for a GKE-on-GCP cluster.

` .google.cloud.gkehub.v1beta1.GkeCluster gke_cluster = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GkeClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.GkeClusterOrBuilder)` |   
  
### getKubernetesMetadata()
    
    
    public abstract KubernetesMetadata getKubernetesMetadata()

Output only. Useful Kubernetes-specific metadata.

` .google.cloud.gkehub.v1beta1.KubernetesMetadata kubernetes_metadata = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[KubernetesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.KubernetesMetadata)` | The kubernetesMetadata.  
  
### getKubernetesMetadataOrBuilder()
    
    
    public abstract KubernetesMetadataOrBuilder getKubernetesMetadataOrBuilder()

Output only. Useful Kubernetes-specific metadata.

` .google.cloud.gkehub.v1beta1.KubernetesMetadata kubernetes_metadata = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[KubernetesMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.KubernetesMetadataOrBuilder)` |   
  
### getKubernetesResource()
    
    
    public abstract KubernetesResource getKubernetesResource()

Optional. The in-cluster Kubernetes Resources that should be applied for a correctly registered cluster, in the steady state. These resources:

  * Ensure that the cluster is exclusively registered to one and only one Hub Membership.
  * Propagate Workload Pool Information available in the Membership Authority field.
  * Ensure proper initial configuration of default Hub Features.



` .google.cloud.gkehub.v1beta1.KubernetesResource kubernetes_resource = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[KubernetesResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.KubernetesResource)` | The kubernetesResource.  
  
### getKubernetesResourceOrBuilder()
    
    
    public abstract KubernetesResourceOrBuilder getKubernetesResourceOrBuilder()

Optional. The in-cluster Kubernetes Resources that should be applied for a correctly registered cluster, in the steady state. These resources:

  * Ensure that the cluster is exclusively registered to one and only one Hub Membership.
  * Propagate Workload Pool Information available in the Membership Authority field.
  * Ensure proper initial configuration of default Hub Features.



` .google.cloud.gkehub.v1beta1.KubernetesResource kubernetes_resource = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[KubernetesResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.KubernetesResourceOrBuilder)` |   
  
### getMultiCloudCluster()
    
    
    public abstract MultiCloudCluster getMultiCloudCluster()

Optional. Specific information for a GKE Multi-Cloud cluster.

` .google.cloud.gkehub.v1beta1.MultiCloudCluster multi_cloud_cluster = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiCloudCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.MultiCloudCluster)` | The multiCloudCluster.  
  
### getMultiCloudClusterOrBuilder()
    
    
    public abstract MultiCloudClusterOrBuilder getMultiCloudClusterOrBuilder()

Optional. Specific information for a GKE Multi-Cloud cluster.

` .google.cloud.gkehub.v1beta1.MultiCloudCluster multi_cloud_cluster = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MultiCloudClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.MultiCloudClusterOrBuilder)` |   
  
### getOnPremCluster()
    
    
    public abstract OnPremCluster getOnPremCluster()

Optional. Specific information for a GKE On-Prem cluster. An onprem user-cluster who has no resourceLink is not allowed to use this field, it should have a nil "type" instead.

` .google.cloud.gkehub.v1beta1.OnPremCluster on_prem_cluster = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OnPremCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.OnPremCluster)` | The onPremCluster.  
  
### getOnPremClusterOrBuilder()
    
    
    public abstract OnPremClusterOrBuilder getOnPremClusterOrBuilder()

Optional. Specific information for a GKE On-Prem cluster. An onprem user-cluster who has no resourceLink is not allowed to use this field, it should have a nil "type" instead.

` .google.cloud.gkehub.v1beta1.OnPremCluster on_prem_cluster = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OnPremClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.OnPremClusterOrBuilder)` |   
  
### getTypeCase()
    
    
    public abstract MembershipEndpoint.TypeCase getTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[MembershipEndpoint.TypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-gkehub/latest/com.google.cloud.gkehub.v1beta1.MembershipEndpoint.TypeCase)` |   
  
### hasApplianceCluster()
    
    
    public abstract boolean hasApplianceCluster()

Optional. Specific information for a GDC Edge Appliance cluster.

` .google.cloud.gkehub.v1beta1.ApplianceCluster appliance_cluster = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the applianceCluster field is set.  
  
### hasEdgeCluster()
    
    
    public abstract boolean hasEdgeCluster()

Optional. Specific information for a Google Edge cluster.

` .google.cloud.gkehub.v1beta1.EdgeCluster edge_cluster = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the edgeCluster field is set.  
  
### hasGkeCluster()
    
    
    public abstract boolean hasGkeCluster()

Optional. Specific information for a GKE-on-GCP cluster.

` .google.cloud.gkehub.v1beta1.GkeCluster gke_cluster = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gkeCluster field is set.  
  
### hasKubernetesMetadata()
    
    
    public abstract boolean hasKubernetesMetadata()

Output only. Useful Kubernetes-specific metadata.

` .google.cloud.gkehub.v1beta1.KubernetesMetadata kubernetes_metadata = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kubernetesMetadata field is set.  
  
### hasKubernetesResource()
    
    
    public abstract boolean hasKubernetesResource()

Optional. The in-cluster Kubernetes Resources that should be applied for a correctly registered cluster, in the steady state. These resources:

  * Ensure that the cluster is exclusively registered to one and only one Hub Membership.
  * Propagate Workload Pool Information available in the Membership Authority field.
  * Ensure proper initial configuration of default Hub Features.



` .google.cloud.gkehub.v1beta1.KubernetesResource kubernetes_resource = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kubernetesResource field is set.  
  
### hasMultiCloudCluster()
    
    
    public abstract boolean hasMultiCloudCluster()

Optional. Specific information for a GKE Multi-Cloud cluster.

` .google.cloud.gkehub.v1beta1.MultiCloudCluster multi_cloud_cluster = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multiCloudCluster field is set.  
  
### hasOnPremCluster()
    
    
    public abstract boolean hasOnPremCluster()

Optional. Specific information for a GKE On-Prem cluster. An onprem user-cluster who has no resourceLink is not allowed to use this field, it should have a nil "type" instead.

` .google.cloud.gkehub.v1beta1.OnPremCluster on_prem_cluster = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the onPremCluster field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
