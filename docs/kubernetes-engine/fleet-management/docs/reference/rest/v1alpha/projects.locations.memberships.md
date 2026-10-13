---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships
title: REST Resource: projects.locations.memberships \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:06.015591+00:00
---

# REST Resource: projects.locations.memberships  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.memberships Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Membership
    * JSON representation
  * MembershipEndpoint
    * JSON representation
  * GkeCluster
    * JSON representation
  * OnPremCluster
    * JSON representation
  * OnPremCluster.ClusterType
  * MultiCloudCluster
    * JSON representation
  * EdgeCluster
    * JSON representation
  * ApplianceCluster
    * JSON representation
  * KubernetesMetadata
    * JSON representation
  * KubernetesResource
    * JSON representation
  * ResourceManifest
    * JSON representation
  * ResourceOptions
    * JSON representation
  * MembershipState
    * JSON representation
  * MembershipState.Code
  * Authority
    * JSON representation
  * MonitoringConfig
    * JSON representation
  * Membership.ClusterTier
  * Membership.MembershipType
  * Methods



## Resource: Membership

Membership contains information about a member cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "state": {
        object ([MembershipState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MembershipState))
      },
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "externalId": string,
      "lastConnectionTime": string,
      "uniqueId": string,
      "authority": {
        object ([Authority](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Authority))
      },
      "monitoringConfig": {
        object ([MonitoringConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MonitoringConfig))
      },
      "clusterTier": enum ([Membership.ClusterTier](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership.ClusterTier)),
      "membershipType": enum ([Membership.MembershipType](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership.MembershipType)),
    
      // Union field type can be only one of the following:
      "endpoint": {
        object ([MembershipEndpoint](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MembershipEndpoint))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
`name` |  `string` Output only. The full, unique name of this Membership resource in the format `projects/*/locations/*/memberships/{membershipId}`, set during creation.`membershipId` must be a valid RFC 1123 compliant DNS label:

  1. At most 63 characters in length
  2. It must consist of lower case alphanumeric characters or `-`
  3. It must start and end with an alphanumeric character

Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this membership. These labels are not leveraged by multi-cluster features, instead, we prefer cluster labels, which can be set on GKE cluster or other cluster types.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Output only. Description of this membership, limited to 63 characters. Must match the regex: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\ ]*`This field is present for legacy purposes.  
`state` |  `object (`[MembershipState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MembershipState)`)` Output only. State of the Membership resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Membership was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Membership was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Membership was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`externalId` |  `string` Optional. An externally-generated and managed ID for this Membership. This ID may be modified after creation, but this is not recommended.The ID must match the regex: `[a-zA-Z0-9][a-zA-Z0-9_\-\.]*`If this Membership represents a Kubernetes cluster, this value should be set to the UID of the `kube-system` namespace object.  
`lastConnectionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. For clusters using Connect, the timestamp of the most recent connection established with Google Cloud. This time is updated every several minutes, not continuously. For clusters that do not use GKE Connect, or that have never connected successfully, this field will be unset.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uniqueId` |  `string` Output only. Google-generated UUID for this resource. This is unique across all Membership resources. If a Membership resource is deleted and another resource with the same name is created, it gets a different uniqueId.  
`authority` |  `object (`[Authority](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Authority)`)` Optional. How to identify workloads from this Membership. See the documentation on Workload Identity for more details: <https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity>  
`monitoringConfig` |  `object (`[MonitoringConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MonitoringConfig)`)` Optional. The monitoring config information for this membership.  
`clusterTier` |  `enum (`[Membership.ClusterTier](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership.ClusterTier)`)` Output only. The tier of the cluster.  
`membershipType` |  `enum (`[Membership.MembershipType](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership.MembershipType)`)` Output only. The type of the membership.  
Union field `type`. Type of resource represented by this Membership `type` can be only one of the following:  
`endpoint` |  `object (`[MembershipEndpoint](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MembershipEndpoint)`)` Optional. Endpoint information to reach this member.  
  
## MembershipEndpoint

MembershipEndpoint contains information needed to contact a Kubernetes API, endpoint and any additional Kubernetes metadata.

JSON representation  
---  
      
    
    {
      "kubernetesMetadata": {
        object ([KubernetesMetadata](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#KubernetesMetadata))
      },
      "kubernetesResource": {
        object ([KubernetesResource](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#KubernetesResource))
      },
      "googleManaged": boolean,
    
      // Union field type can be only one of the following:
      "gkeCluster": {
        object ([GkeCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#GkeCluster))
      },
      "onPremCluster": {
        object ([OnPremCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#OnPremCluster))
      },
      "multiCloudCluster": {
        object ([MultiCloudCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MultiCloudCluster))
      },
      "edgeCluster": {
        object ([EdgeCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#EdgeCluster))
      },
      "applianceCluster": {
        object ([ApplianceCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ApplianceCluster))
      }
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
`kubernetesMetadata` |  `object (`[KubernetesMetadata](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#KubernetesMetadata)`)` Output only. Useful Kubernetes-specific metadata.  
`kubernetesResource` |  `object (`[KubernetesResource](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#KubernetesResource)`)` Optional. The in-cluster Kubernetes Resources that should be applied for a correctly registered cluster, in the steady state. These resources:

  * Ensure that the cluster is exclusively registered to one and only one Hub Membership.
  * Propagate Workload Pool Information available in the Membership Authority field.
  * Ensure proper initial configuration of default Hub Features.

  
`googleManaged` |  `boolean` Output only. Whether the lifecycle of this membership is managed by a google cluster platform service.  
Union field `type`. Cluster information of the registered cluster. `type` can be only one of the following:  
`gkeCluster` |  `object (`[GkeCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#GkeCluster)`)` Optional. Specific information for a GKE-on-GCP cluster.  
`onPremCluster` |  `object (`[OnPremCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#OnPremCluster)`)` Optional. Specific information for a GKE On-Prem cluster. An onprem user-cluster who has no resourceLink is not allowed to use this field, it should have a nil "type" instead.  
`multiCloudCluster` |  `object (`[MultiCloudCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MultiCloudCluster)`)` Optional. Specific information for a GKE Multi-Cloud cluster.  
`edgeCluster` |  `object (`[EdgeCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#EdgeCluster)`)` Optional. Specific information for a Google Edge cluster.  
`applianceCluster` |  `object (`[ApplianceCluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ApplianceCluster)`)` Optional. Specific information for a GDC Edge Appliance cluster.  
  
## GkeCluster

GkeCluster contains information specific to GKE clusters.

JSON representation  
---  
      
    
    {
      "resourceLink": string,
      "clusterMissing": boolean
    }  
  
Fields  
---  
`resourceLink` |  `string` Immutable. Self-link of the Google Cloud resource for the GKE cluster. For example://container.googleapis.com/projects/my-project/locations/us-west1-a/clusters/my-clusterZonal clusters are also supported.  
`clusterMissing` |  `boolean` Output only. If clusterMissing is set then it denotes that the GKE cluster no longer exists in the GKE Control Plane.  
  
## OnPremCluster

OnPremCluster contains information specific to GKE On-Prem clusters.

JSON representation  
---  
      
    
    {
      "resourceLink": string,
      "clusterMissing": boolean,
      "adminCluster": boolean,
      "clusterType": enum ([OnPremCluster.ClusterType](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#OnPremCluster.ClusterType))
    }  
  
Fields  
---  
`resourceLink` |  `string` Immutable. Self-link of the Google Cloud resource for the GKE On-Prem cluster. For example://gkeonprem.googleapis.com/projects/my-project/locations/us-west1-a/vmwareClusters/my-cluster //gkeonprem.googleapis.com/projects/my-project/locations/us-west1-a/bareMetalClusters/my-cluster  
`clusterMissing` |  `boolean` Output only. If clusterMissing is set then it denotes that API(gkeonprem.googleapis.com) resource for this GKE On-Prem cluster no longer exists.  
`adminCluster` |  `boolean` Immutable. Whether the cluster is an admin cluster.  
`clusterType` |  `enum (`[OnPremCluster.ClusterType](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#OnPremCluster.ClusterType)`)` Immutable. The on prem cluster's type.  
  
## OnPremCluster.ClusterType

ClusterType describes on prem cluster's type.

Enums  
---  
`CLUSTERTYPE_UNSPECIFIED` | The ClusterType is not set.  
`BOOTSTRAP` | The ClusterType is bootstrap cluster.  
`HYBRID` | The ClusterType is baremetal hybrid cluster.  
`STANDALONE` | The ClusterType is baremetal standalone cluster.  
`USER` | The ClusterType is user cluster.  
  
## MultiCloudCluster

MultiCloudCluster contains information specific to GKE Multi-Cloud clusters.

JSON representation  
---  
      
    
    {
      "resourceLink": string,
      "clusterMissing": boolean
    }  
  
Fields  
---  
`resourceLink` |  `string` Immutable. Self-link of the Google Cloud resource for the GKE Multi-Cloud cluster. For example://gkemulticloud.googleapis.com/projects/my-project/locations/us-west1-a/awsClusters/my-cluster //gkemulticloud.googleapis.com/projects/my-project/locations/us-west1-a/azureClusters/my-cluster //gkemulticloud.googleapis.com/projects/my-project/locations/us-west1-a/attachedClusters/my-cluster  
`clusterMissing` |  `boolean` Output only. If clusterMissing is set then it denotes that API(gkemulticloud.googleapis.com) resource for this GKE Multi-Cloud cluster no longer exists.  
  
## EdgeCluster

EdgeCluster contains information specific to Google Edge Clusters.

JSON representation  
---  
      
    
    {
      "resourceLink": string
    }  
  
Fields  
---  
`resourceLink` |  `string` Immutable. Self-link of the Google Cloud resource for the Edge Cluster. For example://edgecontainer.googleapis.com/projects/my-project/locations/us-west1-a/clusters/my-cluster  
  
## ApplianceCluster

ApplianceCluster contains information specific to GDC Edge Appliance Clusters.

JSON representation  
---  
      
    
    {
      "resourceLink": string
    }  
  
Fields  
---  
`resourceLink` |  `string` Immutable. Self-link of the Google Cloud resource for the Appliance Cluster. For example://transferappliance.googleapis.com/projects/my-project/locations/us-west1-a/appliances/my-appliance  
  
## KubernetesMetadata

KubernetesMetadata provides informational metadata for Memberships representing Kubernetes clusters.

JSON representation  
---  
      
    
    {
      "kubernetesApiServerVersion": string,
      "nodeProviderId": string,
      "nodeCount": integer,
      "vcpuCount": integer,
      "memoryMb": integer,
      "updateTime": string
    }  
  
Fields  
---  
`kubernetesApiServerVersion` |  `string` Output only. Kubernetes API server version string as reported by `/version`.  
`nodeProviderId` |  `string` Output only. Node providerID as reported by the first node in the list of nodes on the Kubernetes endpoint. On Kubernetes platforms that support zero-node clusters (like GKE-on-GCP), the nodeCount will be zero and the nodeProviderId will be empty.  
`nodeCount` |  `integer` Output only. Node count as reported by Kubernetes nodes resources.  
`vcpuCount` |  `integer` Output only. vCPU count as reported by Kubernetes nodes resources.  
`memoryMb` |  `integer` Output only. The total memory capacity as reported by the sum of all Kubernetes nodes resources, defined in MB.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which these details were last updated. This updateTime is different from the Membership-level updateTime since EndpointDetails are updated internally for API consumers.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## KubernetesResource

KubernetesResource contains the YAML manifests and configuration for Membership Kubernetes resources in the cluster. After memberships.create or memberships.patch, these resources should be re-applied in the cluster.

JSON representation  
---  
      
    
    {
      "membershipCrManifest": string,
      "membershipResources": [
        {
          object ([ResourceManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ResourceManifest))
        }
      ],
      "connectResources": [
        {
          object ([ResourceManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ResourceManifest))
        }
      ],
      "resourceOptions": {
        object ([ResourceOptions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ResourceOptions))
      }
    }  
  
Fields  
---  
`membershipCrManifest` |  `string` Input only. The YAML representation of the Membership CR. This field is ignored for GKE clusters where Hub can read the CR directly.Callers should provide the CR that is currently present in the cluster during memberships.create or memberships.patch, or leave this field empty if none exists. The CR manifest is used to validate the cluster has not been registered with another Membership.  
`membershipResources[]` |  `object (`[ResourceManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ResourceManifest)`)` Output only. Additional Kubernetes resources that need to be applied to the cluster after Membership creation, and after every update.This field is only populated in the Membership returned from a successful long-running operation from memberships.create or memberships.patch. It is not populated during normal memberships.get or memberships.list requests. To get the resource manifest after the initial registration, the caller should make a memberships.patch call with an empty field mask.  
`connectResources[]` |  `object (`[ResourceManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ResourceManifest)`)` Output only. The Kubernetes resources for installing the GKE Connect agentThis field is only populated in the Membership returned from a successful long-running operation from memberships.create or memberships.patch. It is not populated during normal memberships.get or memberships.list requests. To get the resource manifest after the initial registration, the caller should make a memberships.patch call with an empty field mask.  
`resourceOptions` |  `object (`[ResourceOptions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#ResourceOptions)`)` Optional. Options for Kubernetes resource generation.  
  
## ResourceManifest

ResourceManifest represents a single Kubernetes resource to be applied to the cluster.

JSON representation  
---  
      
    
    {
      "manifest": string,
      "clusterScoped": boolean
    }  
  
Fields  
---  
`manifest` |  `string` Output only. YAML manifest of the resource.  
`clusterScoped` |  `boolean` Output only. Whether the resource provided in the manifest is `clusterScoped`. If unset, the manifest is assumed to be namespace scoped.This field is used for REST mapping when applying the resource in a cluster.  
  
## ResourceOptions

ResourceOptions represent options for Kubernetes resource generation.

JSON representation  
---  
      
    
    {
      "connectVersion": string,
      "v1beta1Crd": boolean,
      "k8sVersion": string,
      "k8sGitVersion": string
    }  
  
Fields  
---  
`connectVersion` |  `string` Optional. The Connect agent version to use for connectResources. Defaults to the latest GKE Connect version. The version must be a currently supported version, obsolete versions will be rejected.  
`v1beta1Crd` |  `boolean` Optional. Use `apiextensions/v1beta1` instead of `apiextensions/v1` for CustomResourceDefinition resources. This option should be set for clusters with Kubernetes apiserver versions <1.16.  
`k8sVersion` |  `string` Optional. Major and minor version of the Kubernetes cluster. This is only used to determine which version to use for the CustomResourceDefinition resources, `apiextensions/v1beta1` or`apiextensions/v1`.  
`k8sGitVersion` |  `string` Optional. Git version of the Kubernetes cluster. This is only used to gate the Connect Agent migration to svc.id.goog on GDC-SO 1.33.100 patch and above.  
  
## MembershipState

MembershipState describes the state of a Membership resource.

JSON representation  
---  
      
    
    {
      "code": enum ([MembershipState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MembershipState.Code))
    }  
  
Fields  
---  
`code` |  `enum (`[MembershipState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#MembershipState.Code)`)` Output only. The current state of the Membership resource.  
  
## MembershipState.Code

Code describes the state of a Membership resource.

Enums  
---  
`CODE_UNSPECIFIED` | The code is not set.  
`CREATING` | The cluster is being registered.  
`READY` | The cluster is registered.  
`DELETING` | The cluster is being unregistered.  
`UPDATING` | The Membership is being updated.  
`SERVICE_UPDATING` | The Membership is being updated by the Hub Service.  
  
## Authority

Authority encodes how Google will recognize identities from this Membership. See the workload identity documentation for more details: <https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity>

JSON representation  
---  
      
    
    {
      "issuer": string,
      "workloadIdentityPool": string,
      "identityProvider": string,
      "oidcJwks": string,
      "scopeTenancyWorkloadIdentityPool": string,
      "scopeTenancyIdentityProvider": string
    }  
  
Fields  
---  
`issuer` |  `string` Optional. A JSON Web Token (JWT) issuer URI. `issuer` must start with `https://` and be a valid URL with length <2000 characters, it must use `location` rather than `zone` for GKE clusters.If set, then Google will allow valid OIDC tokens from this issuer to authenticate within the workloadIdentityPool. OIDC discovery will be performed on this URI to validate tokens from the issuer.Clearing `issuer` disables Workload Identity. `issuer` cannot be directly modified; it must be cleared (and Workload Identity disabled) before using a new issuer (and re-enabling Workload Identity).  
`workloadIdentityPool` |  `string` Output only. The name of the workload identity pool in which `issuer` will be recognized.There is a single Workload Identity Pool per Hub that is shared between all Memberships that belong to that Hub. For a Hub hosted in {PROJECT_ID}, the workload pool format is `{PROJECT_ID}.hub.id.goog`, although this is subject to change in newer versions of this API.  
`identityProvider` |  `string` Output only. An identity provider that reflects the `issuer` in the workload identity pool.  
`oidcJwks` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. OIDC verification keys for this Membership in JWKS format (RFC 7517).When this field is set, OIDC discovery will NOT be performed on `issuer`, and instead OIDC tokens will be validated using this field.A base64-encoded string.  
`scopeTenancyWorkloadIdentityPool` |  `string` Optional. Output only. The name of the scope-tenancy workload identity pool. This pool is set in the fleet-level feature.  
`scopeTenancyIdentityProvider` |  `string` Optional. Output only. The identity provider for the scope-tenancy workload identity pool.  
  
## MonitoringConfig

MonitoringConfig informs Fleet-based applications/services/UIs how the metrics for the underlying cluster is reported to cloud monitoring services. It can be set from empty to non-empty, but can't be mutated directly to prevent accidentally breaking the constinousty of metrics.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "location": string,
      "cluster": string,
      "kubernetesMetricsPrefix": string,
      "clusterHash": string
    }  
  
Fields  
---  
`projectId` |  `string` Optional. Project used to report Metrics  
`location` |  `string` Optional. Location used to report Metrics  
`cluster` |  `string` Optional. Cluster name used to report metrics. For Anthos on VMWare/Baremetal/MultiCloud clusters, it would be in format {clusterType}/{clusterName}, e.g., "awsClusters/cluster_1".  
`kubernetesMetricsPrefix` |  `string` Optional. Kubernetes system metrics, if available, are written to this prefix. This defaults to kubernetes.io for GKE, and kubernetes.io/anthos for Anthos eventually. Noted: Anthos MultiCloud will have kubernetes.io prefix today but will migration to be under kubernetes.io/anthos.  
`clusterHash` |  `string` Optional. For GKE and Multicloud clusters, this is the UUID of the cluster resource. For VMWare and Baremetal clusters, this is the kube-system UID.  
  
## Membership.ClusterTier

ClusterTier describes the tier of the GKE cluster as it relates to enterprise functionality. A cluster in the ENTERPRISE tier will have access to all enterprise features. A cluster in the STANDARD tier will not have access to enterprise features.

Enums  
---  
`CLUSTER_TIER_UNSPECIFIED` | The ClusterTier is not set.  
`STANDARD` | The ClusterTier is standard.  
`ENTERPRISE` | The ClusterTier is enterprise.  
  
## Membership.MembershipType

MembershipType describes if the membership supports all features or only lightweight compatible ones.

Enums  
---  
`MEMBERSHIP_TYPE_UNSPECIFIED` | The MembershipType is not set.  
`LIGHTWEIGHT` | The membership supports only lightweight compatible features.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/create)`

|  Creates a new Membership.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/delete)`

|  Removes a Membership.  
  
### `[generateConnectManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/generateConnectManifest)`

|  Generates the manifest for deployment of the GKE connect agent.  
  
### `[generateExclusivityManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/generateExclusivityManifest)`

|  GenerateExclusivityManifest generates the manifests to update the exclusivity artifacts in the cluster if needed.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/get)`

|  Gets the details of a Membership.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/list)`

|  Lists Memberships in a given project and location.  
  
### `[listAdmin](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/listAdmin)`

|  Lists Memberships of admin clusters in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/patch)`

|  Updates an existing Membership.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[validateCreate](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate)`

|  ValidateCreateMembership is a preflight check for CreateMembership.  
  
### `[validateExclusivity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateExclusivity)`

|  ValidateExclusivity validates the state of exclusivity in the cluster.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
