---
url: https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields/
title: Ignore unspecified fields \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:17.984130+00:00
---

# Ignore unspecified fields  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ignore unspecified fields

This page explains the default populating behavior of `spec` fields in Config Connector resources and how to migrate existing resources from the legacy `Merge` behavior to the recommended `Absent` behavior. This page might not be applicable if you're using a CustomResourceDefinition (CRD) added in version 1.114.0 and later because those CRDs support only the `Absent` behavior. For a list of CRDs that support the `Merge` behavior, see the Kinds with `Merge` support section of this page.

## `spec` fields populating behaviors

When Config Connector creates a resource, fields left unspecified in the Kubernetes resource `spec` field can have two different populating behaviors: `Absent` and `Merge`.

### Absent

The `Absent` behavior is the _recommended_ behavior. When a resource uses the `Absent` behavior, Config Connector doesn't populate unspecified fields into the Kubernetes resource `spec` field.

Starting in Config Connector version 1.123.1, the `Absent` behavior is the default populating behavior for all newly created resources unless you set the value of the `spec.stateIntoSpec` field to `Merge` in your ConfigConnector or ConfigConnectorContext custom resource. For resources that use the `cnrm.cloud.google.com/state-into-spec` annotation, Config Connector sets the value of the annotation to lowercase `absent` by default (the `spec.stateIntoSpec` field uses capitalized `Absent` or `Merge`). Resources reconciled by direct controllers use the `Absent` behavior without adding the annotation.

For CRDs added in [version 1.114.0 and later](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/master/config/crds/resources), the `Absent` behavior is the only supported populating behavior.

### Merge

The `Merge` behavior isn't supported in CRDs added in version 1.114.0 and later. When a resource uses the `Merge` behavior, `spec` fields take on values from the Google Cloud API after a successful reconciliation unless those fields aren't readable. For more details, see [Manage fields externally](https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally).

For CRDs added in [version 1.113.0 and earlier](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/v1.113.0/crds), Config Connector supports both the `Absent` and `Merge` behaviors. For the full list of supported resources, see Kinds with `Merge` support. In Config Connector versions earlier than 1.123.1, the default populating behavior for these CRDs was `Merge`, and Config Connector set the value of the `cnrm.cloud.google.com/state-into-spec` annotation to `merge` by default.

Because the `cnrm.cloud.google.com/state-into-spec` annotation is immutable after a resource is created, resources created before version 1.123.1 retain the `cnrm.cloud.google.com/state-into-spec: merge` annotation even after you upgrade Config Connector to version 1.123.1 or later. To configure new resources to use the `Absent` behavior, see Skip populating unspecified fields into spec. To migrate existing resources, see Migrate resources from `Merge` to `Absent`.

When a resource uses the `Merge` behavior, fields that aren't specified in your original YAML manifest are populated into the custom resource `spec` field in the Kubernetes API server. This behavior means that when you run the `kubectl get RESOURCE_KIND RESOURCE_NAME -o yaml` command, the `spec` field in the output can include subfields that aren't in your applied YAML file.

For example, assume the CRD schema lets you specify two fields named `foo` and `bar` in the `spec` field, but your applied YAML file specifies only the `foo` field:
    
    
    spec:
      foo: "foo"
    

If the YAML manifest is applied successfully and the resource is [UpToDate](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-your-resources#-specific_events), the `bar` field appears in the custom resource:
    
    
    spec:
      foo: "foo"
      bar: "bar"
    

Config Connector doesn't populate unspecified resource reference fields, such as `projectRef`, `folderRef`, `organizationRef`, or `billingAccountRef`, from Google Cloud into `spec`. For example, even though the `Project` kind supports `Merge`, all of its optional `spec` fields (`billingAccountRef`, `folderRef`, and `organizationRef`) are resource reference fields. As a result, `Merge` doesn't populate any unspecified fields on a `Project` resource.

**Note:** Explicitly setting `cnrm.cloud.google.com/state-into-spec: merge` in a manifest returns an admission webhook warning on all resources, even on CRDs that support `Merge`.

Due to the complexity of interactions between Config Connector and Google Cloud APIs, use the `Absent` behavior so that Config Connector skips populating the Kubernetes resource `spec` field with unspecified fields.

## Skip populating unspecified fields into spec

You can configure Config Connector to skip populating unspecified fields into the `spec` field for CRDs added in Config Connector [version 1.113.0 and earlier](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/v1.113.0/crds) in either of the following ways:

  * Set the value of the cluster-level or namespace-level `stateIntoSpec` field to `Absent`.
  * On the resource, set the value of the `cnrm.cloud.google.com/state-into-spec` annotation to `absent`.



### Configure the cluster-level or namespace-level `stateIntoSpec` override

When installing Config Connector or updating your Config Connector installation, you can set the value of the cluster-level or namespace-level `stateIntoSpec` field to `Absent` in the ConfigConnector or ConfigConnectorContext custom resource:
    
    
    spec:
      stateIntoSpec: Absent
    

This setting makes the `Absent` behavior the default `spec` fields populating behavior for any new resources created in the cluster or namespace when you don't specify the `cnrm.cloud.google.com/state-into-spec` annotation in the resource YAML manifests. Config Connector skips populating unspecified fields into the Kubernetes resource `spec` field for these resources.

The `stateIntoSpec` field in the ConfigConnector and ConfigConnectorContext custom resources doesn't have a default value. Config Connector determines the `spec` fields populating behavior based on the value of the `cnrm.cloud.google.com/state-into-spec` annotation, and it follows this precedence order to determine the value of the annotation when a resource is created:

  1. Use the value of the `cnrm.cloud.google.com/state-into-spec` annotation directly if it's specified and valid.
  2. If the annotation is unspecified, use the corresponding value of the `stateIntoSpec` field in the ConfigConnectorContext custom resource.
  3. If the ConfigConnectorContext custom resource doesn't exist or the `stateIntoSpec` field is unspecified, use the corresponding value of the `stateIntoSpec` field in the ConfigConnector custom resource.
  4. If the ConfigConnector custom resource doesn't exist or the `stateIntoSpec` field is unspecified, Config Connector version 1.123.1 and later defaults to the `absent` value. Versions earlier than 1.123.1 use the default behavior for the CRD, as described in `spec` fields populating behaviors.



CRDs added in [version 1.114.0 and later](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/master/config/crds/resources) support only the `Absent` populating behavior, regardless of the `stateIntoSpec` field in the ConfigConnector or ConfigConnectorContext custom resource.

If you have already created a resource with the `Merge` behavior, updating the value of the `stateIntoSpec` field to `Absent` in the ConfigConnector or ConfigConnectorContext custom resource doesn't change the existing resource's annotation. To migrate existing resources, see Migrate resources from `Merge` to `Absent`.

### Set the resource-level `cnrm.cloud.google.com/state-into-spec` annotation

When creating your YAML file, you can set the value of the `cnrm.cloud.google.com/state-into-spec` annotation to `absent`. This annotation skips populating unspecified fields into the Kubernetes resource `spec` field:
    
    
    metadata:
      annotations:
        cnrm.cloud.google.com/state-into-spec: absent
    

In Config Connector version 1.123.1 and later, this annotation defaults to the `absent` value if it's not specified (unless you override it by setting the value of the `spec.stateIntoSpec` field to `Merge` in your ConfigConnector or ConfigConnectorContext custom resource). In versions earlier than 1.123.1, this annotation defaulted to the `merge` value for CRDs added in version 1.113.0 and earlier, which means Config Connector populated all unspecified fields into the `spec` field.

This annotation is immutable, which means you can't update the annotation value directly on an existing Config Connector resource. If you have already created a resource with the `merge` value and want to change its behavior to the `absent` value, see Migrate resources from `Merge` to `Absent`.

To further explain the difference introduced by this annotation, assume that a resource has a `spec` field with the following schema:
    
    
    foo1: string
    foo2: string
    bars:
    - br1: string
      br2: string
    barz:
      bz1: string
      bz2: string
    

Also assume that you specified the `spec` field in your YAML manifest as:
    
    
    spec:
      foo1: "foo1"
      bars:
      - br1: "1_br1"
      - br1: "2_br1"
      barz:
        bz1: "bz1"
    

When the value of the `cnrm.cloud.google.com/state-into-spec` annotation is set to `merge`, the populated `spec` field in the created Kubernetes resource looks like the following:
    
    
    spec:
      foo1: "foo1"
      foo2: "foo2"
      bars:
      - br1: "1_br1"
        br2: "1_br2"
      - br1: "2_br1"
        br2: "2_br2"
      barz:
        bz1: "bz1"
        bz2: "bz2"
    

When you set the `cnrm.cloud.google.com/state-into-spec: absent` annotation, the final `spec` field in the created Kubernetes resource remains:
    
    
    spec:
      foo1: "foo1"
      bars:
      - br1: "1_br1"
      - br1: "2_br1"
      barz:
        bz1: "bz1"
    

## Migrate resources from `Merge` to `Absent`

Because the `cnrm.cloud.google.com/state-into-spec` annotation is immutable on an existing Kubernetes resource, upgrading Config Connector to version 1.123.1 or later doesn't automatically change existing resources from the `merge` value to the `absent` value.

Migrating your existing resources and namespaces from the `Merge` behavior to the `Absent` behavior helps prevent the following issues:

  * **Reconciliation errors on automatically updated fields** : Google Cloud automatically updates certain fields on underlying resources, such as maintenance versions or autoscaling settings. Resources with the `state-into-spec: merge` annotation might fail reconciliation or enter an endless update loop trying to revert the field to the older `spec` value.
  * **Conflicts with GitOps and configuration management tools** : tools like Config Sync and Argo CD can conflict with Config Connector when the `Merge` behavior populates unspecified subfields in lists.
  * **Validation errors on newer resource kinds** : if the value of the `spec.stateIntoSpec` field is set to `Merge` on a ConfigConnector or ConfigConnectorContext custom resource, managing resources that don't support the `Merge` behavior can cause validation errors (`invalid value "merge" for "cnrm.cloud.google.com/state-into-spec" annotation`).



### Identify affected namespaces and resources

Before migrating, check your cluster-level, namespace-level, and resource-level settings to identify where the `Merge` behavior is still used:

  * Check the cluster-level ConfigConnector custom resource for a `stateIntoSpec` field override:
        
        kubectl get configconnector configconnector.core.cnrm.cloud.google.com \
            -o jsonpath='{.spec.stateIntoSpec}{"\n"}'
        

  * Check all namespace-level ConfigConnectorContext custom resources for `stateIntoSpec` field overrides:
        
        kubectl get configconnectorcontext -A \
            -o custom-columns=NAMESPACE:.metadata.namespace,STATE_INTO_SPEC:.spec.stateIntoSpec
        

  * Check the value of the `cnrm.cloud.google.com/state-into-spec` annotation on an existing Config Connector resource:
        
        kubectl get RESOURCE_KIND RESOURCE_NAME -n NAMESPACE \
            -o jsonpath='{.metadata.annotations.cnrm\.cloud\.google\.com/state-into-spec}{"\n"}'
        

Replace the following:

    * `RESOURCE_KIND`: the kind of the Config Connector resource, such as SQLInstance.
    * `RESOURCE_NAME`: the name of the resource.
    * `NAMESPACE`: the namespace of the resource.



### Migrate a resource to `Absent`

To change an existing resource's populating behavior from `Merge` to `Absent`, you must [abandon the Kubernetes resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#keeping_resources_after_deletion) and re-acquire the underlying Google Cloud resource with the `cnrm.cloud.google.com/state-into-spec: absent` annotation. To abandon and re-acquire the resource, complete the following steps:

  1. If the value of the `spec.stateIntoSpec` field is set to `Merge` in your ConfigConnector or ConfigConnectorContext custom resource, update the value of the field to `Absent`:
         
         spec:
           stateIntoSpec: Absent
         

  2. Add the `cnrm.cloud.google.com/deletion-policy: abandon` annotation to the existing Config Connector resource in your cluster. This annotation helps ensure that deleting the Kubernetes resource in the next step doesn't delete the underlying Google Cloud resource:
         
         kubectl annotate RESOURCE_KIND RESOURCE_NAME -n NAMESPACE \
             cnrm.cloud.google.com/deletion-policy=abandon --overwrite
         

  3. Delete the resource from your Kubernetes cluster:
         
         kubectl delete RESOURCE_KIND RESOURCE_NAME -n NAMESPACE
         

  4. In your resource YAML manifest, set the value of the `cnrm.cloud.google.com/state-into-spec` annotation to `absent`:
         
         metadata:
           annotations:
             cnrm.cloud.google.com/state-into-spec: absent
         

Review the `spec` field in your YAML manifest to verify that it includes all of the fields that you want Config Connector to manage. Omit fields that you want Google Cloud or external systems to manage automatically, such as the `spec.maintenanceVersion` field on a SQLInstance resource.

  5. Optional: If your local YAML manifest also includes the `cnrm.cloud.google.com/deletion-policy: abandon` annotation and you no longer want the `abandon` deletion policy, remove that annotation from the YAML manifest.

  6. Apply the updated YAML manifest to [re-acquire the resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_an_existing_resource):
         
         kubectl apply -f MANIFEST_FILE
         

Replace `MANIFEST_FILE` with the path to your resource YAML file.




## When to use `cnrm.cloud.google.com/state-into-spec: absent`

In most cases, use the `cnrm.cloud.google.com/state-into-spec: absent` annotation to get the `Absent` populating behavior for `spec` fields. The following sections describe common scenarios that benefit from the `Absent` populating behavior.

### Avoid conflicts with fields automatically updated by Google Cloud

When a resource uses the `cnrm.cloud.google.com/state-into-spec: merge` annotation, Config Connector reads values from the Google Cloud API during initial reconciliation and writes them into the Kubernetes resource `spec` field. If a Google Cloud service later updates one of those fields automatically, Config Connector treats the older value stored in the `spec` field as the target state and attempts to revert the change on the underlying Google Cloud resource.

For example, if you create a SQLInstance resource with the `cnrm.cloud.google.com/state-into-spec: merge` annotation without specifying the `spec.maintenanceVersion` field, Config Connector populates the initial maintenance version into the `spec.maintenanceVersion` field. When Cloud SQL later performs an automatic maintenance update on the instance, the live maintenance version in Cloud SQL advances. During the next reconciliation, Config Connector attempts to patch the instance back to the older `spec.maintenanceVersion` value. Because Cloud SQL rejects maintenance version downgrades, reconciliation fails repeatedly with an `UpdateFailed` error (`The requested maintenance version is not an available maintenance version to upgrade`).

When you set the `cnrm.cloud.google.com/state-into-spec: absent` annotation, omit automatically updated fields such as `spec.maintenanceVersion` from your YAML manifest. Config Connector doesn't record those fields in the `spec` field, which lets Google Cloud update them without causing reconciliation conflicts.

### Manage unspecified fields in a list externally

Config Connector treats all list fields in the Kubernetes resource `spec` field as atomic fields. As a result, when the value of the `state-into-spec` annotation is set to `merge`, Config Connector reverts any change made to a subfield in a list from outside of Config Connector. However, you can use the `cnrm.cloud.google.com/state-into-spec: absent` annotation to let Config Connector leave unspecified subfields in a list unmanaged. For more information, see [Behavior for list fields in resource spec](https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally#behavior_for_list_fields_in_resource_spec).

### Resolve conflicts between configuration management tools and Config Connector

If you're using configuration management tools like [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) or [Argo CD](https://argoproj.github.io/cd/), you might notice conflicts between the configuration management tool and Config Connector. An example is the [KNV2005 error](https://docs.cloud.google.com/config-connector/docs/troubleshooting#knv2005_syncer_excessively_updating_resource) explained in the troubleshooting guide. These issues occur for the following reasons:

  * When the value of the `state-into-spec` annotation is set to `merge`, Config Connector populates and defaults unspecified values in lists in the `spec` field, such as the `spec.bars[0].br2` field.
  * Both configuration management tools and Config Connector treat list fields as atomic, so configuration management tools treat the added `spec.bars[0].br2` field as drift and remove it.



To resolve these issues, you can set the `cnrm.cloud.google.com/state-into-spec: absent` annotation so that Config Connector doesn't add the unspecified `spec.bars[0].br2` field into the `spec` field.

### Resolve GET/PUT symmetry issues

GET/PUT symmetry refers to a design principle in REST APIs. Specifically, it means that when a GET response is sent as a PUT request to the same URL, the expected result is an HTTP `200 OK` status code with no change in the state of the underlying REST resource.

When the value of the `state-into-spec` annotation is set to `merge`, the unspecified fields populated by Config Connector in the Kubernetes resource `spec` field are the result of a GET request. This behavior means that in future [reconciliations](https://docs.cloud.google.com/config-connector/docs/concepts/reconciliation), Config Connector might send a PUT or PATCH request to the underlying Google Cloud API with these unspecified field values learned from the GET request. This behavior usually isn't a problem, but some Google Cloud APIs might reject the PUT or PATCH request because of these unspecified field values. In the same example, the populated `spec.barz.bz2` field with value `"bz2"` might result in an HTTP 400 client error or other unexpected responses if the API implementation violates the GET/PUT symmetry principle.

To avoid this category of issues, you can set the `cnrm.cloud.google.com/state-into-spec: absent` annotation and check if the errors during reconciliation go away.

## Observed state

If you need to set the `cnrm.cloud.google.com/state-into-spec: absent` annotation, but your solution depends on the populated values from unspecified fields, check if these fields exist in the `status.observedState` field in the CRD schema. If they're represented in the `status.observedState` field, then you can set the `cnrm.cloud.google.com/state-into-spec: absent` annotation and still access the values of the unspecified fields after a successful reconciliation.

The `status.observedState` field contains the live state of the selected, observed fields of the resource that Config Connector observed in the last successful reconciliation. Config Connector selects observed fields that are computed `spec` fields and dependencies for common use cases. You can find the observed fields in the CRD schemas.

If you can't find the observed fields you want, check for an existing issue or open a new issue in the [public issue tracker](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues).

## Kinds with `Merge` support

The following are all the Config Connector kinds that support `Merge` populating behavior:

  * AccessContextManagerAccessLevel
  * AccessContextManagerAccessPolicy
  * AccessContextManagerServicePerimeter
  * AlloyDBBackup
  * AlloyDBCluster
  * AlloyDBUser
  * ApigeeEnvironment
  * ApigeeOrganization
  * ArtifactRegistryRepository
  * BigQueryDataset
  * BigQueryJob
  * BigQueryRoutine
  * BigQueryTable
  * BigtableAppProfile
  * BigtableGCPolicy
  * BigtableInstance
  * BigtableTable
  * BillingBudgetsBudget
  * BinaryAuthorizationAttestor
  * BinaryAuthorizationPolicy
  * CertificateManagerCertificate
  * CertificateManagerCertificateMap
  * CertificateManagerCertificateMapEntry
  * CloudBuildTrigger
  * CloudFunctionsFunction
  * CloudSchedulerJob
  * ComputeAddress
  * ComputeBackendBucket
  * ComputeBackendService
  * ComputeDisk
  * ComputeExternalVPNGateway
  * ComputeFirewall
  * ComputeFirewallPolicy
  * ComputeFirewallPolicyAssociation
  * ComputeForwardingRule
  * ComputeHTTPHealthCheck
  * ComputeHTTPSHealthCheck
  * ComputeHealthCheck
  * ComputeImage
  * ComputeInstance
  * ComputeInstanceGroup
  * ComputeInstanceGroupManager
  * ComputeInstanceTemplate
  * ComputeInterconnectAttachment
  * ComputeNetwork
  * ComputeNetworkEndpointGroup
  * ComputeNetworkFirewallPolicy
  * ComputeNetworkPeering
  * ComputeNodeGroup
  * ComputeNodeTemplate
  * ComputePacketMirroring
  * ComputeProjectMetadata
  * ComputeRegionNetworkEndpointGroup
  * ComputeReservation
  * ComputeResourcePolicy
  * ComputeRoute
  * ComputeRouter
  * ComputeRouterInterface
  * ComputeRouterNAT
  * ComputeRouterPeer
  * ComputeSSLCertificate
  * ComputeSSLPolicy
  * ComputeSecurityPolicy
  * ComputeServiceAttachment
  * ComputeSharedVPCHostProject
  * ComputeSharedVPCServiceProject
  * ComputeSnapshot
  * ComputeSubnetwork
  * ComputeTargetGRPCProxy
  * ComputeTargetHTTPProxy
  * ComputeTargetHTTPSProxy
  * ComputeTargetInstance
  * ComputeTargetPool
  * ComputeTargetSSLProxy
  * ComputeTargetTCPProxy
  * ComputeTargetVPNGateway
  * ComputeURLMap
  * ComputeVPNGateway
  * ComputeVPNTunnel
  * ConfigControllerInstance
  * ContainerAnalysisNote
  * ContainerAttachedCluster
  * ContainerCluster
  * ContainerNodePool
  * DLPDeidentifyTemplate
  * DLPInspectTemplate
  * DLPJobTrigger
  * DLPStoredInfoType
  * DNSManagedZone
  * DNSPolicy
  * DNSRecordSet
  * DataCatalogPolicyTag
  * DataCatalogTaxonomy
  * DataFusionInstance
  * DataflowFlexTemplateJob
  * DataflowJob
  * DataprocAutoscalingPolicy
  * DataprocCluster
  * DataprocWorkflowTemplate
  * EdgeContainerCluster
  * EdgeContainerNodePool
  * EdgeContainerVpnConnection
  * EdgeNetworkNetwork
  * EdgeNetworkSubnet
  * EventarcTrigger
  * FilestoreBackup
  * FilestoreInstance
  * FirestoreIndex
  * Folder
  * GKEHubFeature
  * GKEHubMembership
  * IAMAccessBoundaryPolicy
  * IAMAuditConfig
  * IAMCustomRole
  * IAMPartialPolicy
  * IAMPolicy
  * IAMPolicyMember
  * IAMServiceAccount
  * IAMServiceAccountKey
  * IAMWorkforcePool
  * IAMWorkforcePoolProvider
  * IAMWorkloadIdentityPool
  * IAMWorkloadIdentityPoolProvider
  * IAPBrand
  * IAPIdentityAwareProxyClient
  * IdentityPlatformConfig
  * IdentityPlatformOAuthIDPConfig
  * IdentityPlatformTenant
  * IdentityPlatformTenantOAuthIDPConfig
  * KMSCryptoKey
  * KMSKeyRing
  * LoggingLogBucket
  * LoggingLogExclusion
  * LoggingLogSink
  * LoggingLogView
  * MemcacheInstance
  * MonitoringAlertPolicy
  * MonitoringGroup
  * MonitoringMetricDescriptor
  * MonitoringMonitoredProject
  * MonitoringNotificationChannel
  * MonitoringService
  * MonitoringServiceLevelObjective
  * MonitoringUptimeCheckConfig
  * NetworkConnectivityHub
  * NetworkConnectivitySpoke
  * NetworkSecurityAuthorizationPolicy
  * NetworkSecurityClientTLSPolicy
  * NetworkSecurityServerTLSPolicy
  * NetworkServicesEndpointPolicy
  * NetworkServicesGRPCRoute
  * NetworkServicesGateway
  * NetworkServicesHTTPRoute
  * NetworkServicesMesh
  * NetworkServicesTCPRoute
  * NetworkServicesTLSRoute
  * OSConfigGuestPolicy
  * OSConfigOSPolicyAssignment
  * PrivateCACAPool
  * PrivateCACertificate
  * PrivateCACertificateAuthority
  * PrivateCACertificateTemplate
  * Project
  * PubSubLiteReservation
  * PubSubSchema
  * PubSubSubscription
  * PubSubTopic
  * RecaptchaEnterpriseKey
  * RedisInstance
  * ResourceManagerLien
  * ResourceManagerPolicy
  * RunJob
  * RunService
  * SQLDatabase
  * SQLSSLCert
  * SQLUser
  * SecretManagerSecret
  * SecretManagerSecretVersion
  * Service
  * ServiceDirectoryEndpoint
  * ServiceDirectoryNamespace
  * ServiceDirectoryService
  * ServiceIdentity
  * ServiceNetworkingConnection
  * SourceRepoRepository
  * SpannerDatabase
  * SpannerInstance
  * StorageBucket
  * StorageBucketAccessControl
  * StorageDefaultObjectAccessControl
  * StorageNotification
  * StorageTransferJob
  * TagsTagBinding
  * TagsTagKey
  * TagsTagValue
  * VPCAccessConnector



The following kinds don't support the `Merge` populating behavior starting from the corresponding version:

**Kind name** | **Version**  
---|---  
AlloyDBInstance | 1.129.2  
CertificateManagerDNSAuthorization | 1.124.0  
CloudIdentityGroup | 1.134.0  
CloudIdentityMembership | 1.134.0  
ComputeFirewallPolicyRule | 1.125.0  
GKEHubFeatureMembership | 1.128.0  
LoggingLogMetric | 1.118.1  
MonitoringDashboard | 1.119.0  
SQLInstance | 1.129.2  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
