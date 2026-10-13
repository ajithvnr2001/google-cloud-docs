---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.3.0/dbcluster/
title: DBCluster v1.3.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:36.490753+00:00
---

# DBCluster v1.3.0 custom resource definition  |  AlloyDB Omni using the container orchestrator: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.3.0/dbcluster/

This page documents AlloyDB Omni version **17.7.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  DBCluster v1.3.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/kubernetes-crds-1.3.0/dbcluster)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/kubernetes-crds-1.3.0/dbcluster)



## Spec schema

DBClusterSpec defines the desired state of DBCluster.
    
    
    allowExternalIncomingTraffic: boolean
    availability:
      autoFailoverTriggerThreshold: integer
      autoHealTriggerThreshold: integer
      enableAutoFailover: boolean
      enableAutoHeal: boolean
      enableStandbyAsReadReplica: boolean
      healthcheckPeriodSeconds: integer
      numberOfStandbys: integer
    connectedModeSpec:
      apiKeySecret: string
      clusterId: string
      displayLocation: string
      gcpProjectId: string
      gcpZone: string
    controlPlaneAgentsVersion: string
    databaseImage: string
    databaseVersion: string
    isDeleted: boolean
    mode: string
    primarySpec:
      adminUser:
        passwordRef:
          name: string
      allowExternalIncomingTrafficToInstance: boolean
      auditLogTarget:
        syslog:
          certsSecretRef:
            name: string
            namespace: string
          host: string
      availabilityOptions:
        healthcheckPeriodSeconds: integer
        livenessProbe: string
      dbLoadBalancerOptions:
        annotations: object
        gcp:
          loadBalancerIP: string
          loadBalancerType: string
      features:
        googleMLExtension:
          config:
            vertexAIKeyRef: string
            vertexAIRegion: string
          enabled: boolean
        memoryAgent:
          enabled: boolean
      isStopped: boolean
      mode: string
      parameters: object
      resources:
        cpu: integer or string
        disks:
        - accessModes: string
          annotations: object
          name: string
          selector:
            matchExpressions:
            - key: string
              operator: string
              values: string
            matchLabels: object
          size: string
          storageClass: string
          volumeName:
        memory: string or integer
      schedulingconfig:
        nodeaffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            preference:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchFields:
              - key: string
                operator: string
                values: string
            weight: integer
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchFields:
              - key: string
                operator: string
                values: string
        podAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: string
                  operator: string
                  values: string
                matchLabels: object
              namespaceSelector:
                matchExpressions:
                - key: string
                  operator: string
                  values: string
                matchLabels: object
                namespaces: string
                topologyKey: string
            weight: integer
          requiredDuringSchedulingIgnoredDuringExecution:
            labelSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels: object
            namespaceSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels: object
            namespaces: string
            topologyKey: string
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: string
                  operator: string
                  type: string
                matchLabels: object
              namespaceSelector:
                matchExpressions:
                - key: string
                  operator: string
                  values: string
                matchLabels: object
              namespaces: string
              topologyKey: string
            weight: integer
          requiredDuringSchedulingIgnoredDuringExecution:
            labelSelector:
              matchExpressions:
              - key: string
                operator: string
                values: string
              matchLabels: object
            namespaceSelector:
              matchExpressions:
              - key: string
                operator: string
                type: string
              matchLabels: object
            namespaces: string
            topologyKey: string
        tolerations:
        - effect: string
          key: string
          operator: string
          tolerationSeconds: integer
          value: string
      services: object
      sidecarRef:
        name: string
      sourceCidrRanges:
      tls:
        certSecret:
          name: string
      walArchiveSetting:
        archiveMode: string
        location: string
    tls:
      certSecret:
        name: string
    

FieldType  
Required or optional |  Description  
---|---  
`allowExternalIncomingTraffic`  
`boolean`  
 _Optional_ |  N/A   
`availability`  
`object`  
 _Optional_ |  Availability contains adjustable settings for DBCluster high availability (HA) features.   
`availability.autoFailoverTriggerThreshold`  
`integer`  
 _Optional_ |  AutoFailoverTriggerThreshold is the number of consecutive healthcheck failures on the primary instance that triggers an automatic failover. If set to 0, then it will use the system default value. Use the EnableAutoFailover flag to disable automatic failover.   
`availability.autoHealTriggerThreshold`  
`integer`  
 _Optional_ |  AutoHealTriggerThreshold is the number of consecutive healthcheck failures on the standby instance that triggers automatic healing. Use the EnableAutoHeal flag to disable automatic healing.   
`availability.enableAutoFailover`  
`boolean`  
 _Optional_ |  EnableAutoFailover means this DBCluster will trigger a failover if it detects the primary instance is unhealthy and standby instance is healthy. If set to true, then automatic failover is enabled. If set to false, then autofailover isn't triggered even if the system detects that the primary instance is unhealthy. The default value is true. When it is enabled, if the system detects that the primary instance is unhealthy for the given threshold, it will trigger a failover. This feature is only applicable if this is an HA DBCluster and if the standby is healthy.   
`availability.enableAutoHeal`  
`boolean`  
 _Optional_ |  EnableAutoHeal means this DBCluster will trigger an autoheal if it detects the standby instance is unhealthy. If set to true, then autoheal is enabled. If set to false, then autoheal is not triggered even if the system detects that the standby instance is unhealthy. The default value is true. When it is enabled, if the system detects that the standby instance is unhealthy for the given threshold, it triggers an autoheal. This feature is only applicable if this is an HA DBCluster.   
`availability.enableStandbyAsReadReplica`  
`boolean`  
 _Required_ |  EnableStandbyAsReadReplica determine whether the standbys can accept user queries or not. If set to true, a new endpoint is created to enable read-only access to the standbys.   
`availability.healthcheckPeriodSeconds`  
`integer`  
 _Optional_ |  HealthcheckPeriodSeconds is the number of seconds the healthcheck prober waits before checking the health of the primary and standby instances again and updating the status accordingly.   
`availability.numberOfStandbys`  
`integer`  
 _Optional_ |  NumberOfStandbys is the number of standbys that should be created for this DBCluster. If set to any value greater than 0, then HA is enabled on the cluster and the system will create the indicated number of standby instances. The maximum allowed standby instances is 5. To check the current status of HA on this DBCluster, look at the HAReady condition under the DBCluster status. If HAReady is true, then setup has been complete and ready. If set to 0, then HA is disabled on the cluster, and deletes any existing standby instances. Any number between 0 and 5 inclusive is supported. The default value is 0. For more information, see [Manage high availability in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.3.0/alloydb/docs/omni/kubernetes-ha).   
`connectedModeSpec`  
`object`  
 _Optional_ |  N/A   
`connectedModeSpec.apiSecretKey`  
`string`  
 _Optional_ |  N/A   
`connectedModeSpec.clusterId`  
`string`  
 _Optional_ |  N/A   
`connectedModeSpec.displayLocation`  
`string`  
 _Optional_ |  N/A   
`connectedModeSpec.gcpProjectId`  
`string`  
 _Optional_ |  N/A   
`connectedModeSpec.gcpZone`  
`string`  
 _Optional_ |  N/A   
`controlPlaneAgentsVersion`  
`string`  
 _Required_ |  ControlPlaneAgentsVersion is the desired control plane agents version for the cluster for example, "0.5.2". The controlPlaneAgentsVersion must be compatible with the chosen databaseVersion. To know what versions are compatible, check the list of available versions in {link}. This version is applied to all instances of the database cluster. In the case of a new database cluster, the instance is be created using the specified version. In the case of an existing database cluster, the operator will aptempt to upgrade or downgrade to the specified controlPlaneAgentsVersion. The field status.currentControlPlaneAgentsVersion indicates the current version for control plane agents.  
`databaseImage`  
`string`  
 _Optional_ |  DatabaseImage is the Uniform Resource Identifier of a customized database image within the container registry. If databaseImage is specified, then the operator uses this container image for the database instead of the default database container image of the specified databaseVersion. We recommend that the databaseImage container is based on the default database image used of the chosen databaseVersion.   
`databaseVersion`  
`string`  
 _Required_ |  DatabaseVersion is the desired database version for the cluster for example, "15.4.5". This field is required. This version is applied to all instances of the database cluster. In the case of a new database cluster, the instance is created using the specified version. In the case of an existing database cluster, the operator aptempts to upgrade or downgrade to the specified databaseVersion. The field status.currentDatabaseVersion indicates the current database version.   
`isDeleted`  
`boolean`  
 _Optional_ |  IsDeleted indicates a request to delete the DBCluster. By default, this field is false. This fields applies to all instances of the database cluster. When set this to true, the control plane will attempt to release the related resources, including network endpoints. See the status fields for indication of success or failures, if any.   
`mode`  
`string`  
 _Optional_ |  Indicates the mode of this DBCluster. It accepts any of the following values `""` or `disasterRecovery`.   
`primarySpec`  
`object`  
 _Required_ |  PrimarySpec contains the specifications of the Primary instance of the database cluster. The primary instance contains the compute and storage resources serving the read-write endpoints of the database cluster.   
`primarySpec.adminUser`  
`object`  
 _Required_ |  AdminUser represents the admin user specification. This is the initial database user that the control plane creates. Additional database users are managed by the end-user directly. This field can also be used to reset the password of the initial user.   
`primarySpec.adminUser.passwordRef`  
`object`  
 _Optional_ |  PasswordRef is the name of the secret containing the admin user's password. This value is used during initial provisioning or password reset to set the admin user to that password. The secret must be under the same project as the Database cluster. The name of the secret must follow this pattern: db-pw-. Additionally, the key of the password (inside the secret) must be the same as the database cluster name.   
`primarySpec.adminUser.passwordRef.name`  
`string`  
 _Optional_ |  The name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`primarySpec.allowExternalIncomingTrafficToInstance`  
`boolean`  
 _Optional_ |  AllowExternalIncomingTrafficToInstance is used to configure the external LB creation.   
`primarySpec.AuditLogTarget`  
`object`  
 _Optional_ |  AuditLogTarget configures the sink for the database audit logs.   
`primarySpec.AuditLogTarget.syslog`  
`object`  
 _Optional_ |  N/A   
`primarySpec.AuditLogTarget.certsSecretRef`  
`object`  
 _Required_ |  CertsSecretRef contains the certificates to be used for the TLS connection to the syslog server.   
`primarySpec.AuditLogTarget.certsSecretRef.name`  
`string`  
 _Optional_ |  name is unique within a namespace to reference a secret resource.   
`primarySpec.AuditLogTarget.certsSecretRef.namespace`  
`string`  
 _Optional_ |  namespace defines the space within which the secret name must be unique.   
`primarySpec.AuditLogTarget.syslog.host`  
`string`  
 _Required_ |  Host is the syslog server FQDN or the IP address.   
`primarySpec.availabilityOptions`  
`object`  
 _Optional_ |  AvailabilityOptions contains adjustable settings for HA features.   
`primarySpec.availabilityOptions.healthcheckPeriodSeconds`  
`integer`  
 _Optional_ |  HealthcheckPeriodSeconds is the number of seconds the healthcheck prober will wait before checking the health of the primary and standby instances again and updating the status accordingly. This field is propagated down from the DBCluster's spec.   
`primarySpec.availabilityOptions.livenessProbe`  
`string`  
 _Optional_ |  LivenessProbe enables or disables the liveness probe which is used to trigger a container restart. When set to Enabled, the liveness probe runs periodic health checks on the database. It restarts the container if it fails three consecutive health checks. LivenessProbe is automatically disabled for HA instances. When set to Disabled, the liveness probe is not running health checks on the database. The default value is Enabled.   
`primarySpec.dbLoadBalancerOptions`  
`object`  
 _Optional_ |  DBNetworkServiceOptions allows to override some details of the Kubernetes Service that are created to expose a connection to the database.   
`primarySpec.dbLoadBalancerOptions.annotations`  
`object`  
 _Optional_ |  Annotations provided by the customer are added to the service object of type loadbalancer.   
`primarySpec.dbLoadBalancerOptions.gcp`  
`object`  
 _Optional_ |  Contains Google Cloud-specific attributes for the Kubernetes LoadBalancer.   
`primarySpec.dbLoadBalancerOptions.gcp.loadBalancerIP`  
`string`  
 _Optional_ |  LoadBalancerIP is a static IP address. For more information, see [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address).   
`primarySpec.dbLoadBalancerOptions.gcp.loadBalancerType`  
`string`  
 _Optional_ |  A LoadBalancer can be internal or external. For more information, see [Internal load balancer](https://kubernetes.io/docs/concepts/services-networking/service/#internal-load-balancer).   
`primarySpec.features`  
`object`  
 _Optional_ |  Feature specification.   
`primarySpec.features.googleMLExtension`  
`object`  
 _Optional_ |  Google machine learning (ML) Extension Specification.   
`primarySpec.features.googleMLExtension.config`  
`object`  
 _Optional_ |  Google ML Extension Configuration.   
`primarySpec.features.googleMLExtension.config.vertexAIKeyRef`  
`string`  
 _Optional_ |  N/A   
`primarySpec.features.googleMLExtension.config.vertexAIRegion`  
`string`  
 _Optional_ |  N/A   
`primarySpec.features.googleMLExtension.enabled`  
`boolean`  
 _Required_ |  N/A   
`primarySpec.features.memoryAgent`  
`object`  
 _Optional_ |  N/A   
`primarySpec.features.memoryAgent.enabled`  
`boolean`  
 _Required_ |  Indicate interest to enable or disable memory agent for the database. The default is true.   
`primarySpec.features.memoryAgent.enabled`  
`boolean`  
 _Required_ |  Indicate interest to enable or disable memory agent for the database. The default is true.   
`primarySpec.isStopped`  
`boolean`  
 _Optional_ |  IsStopped stops the instance when set to true. By default, this field is set to false. When stopped, the compute resources (CPU, memory) of the instance are released. However, the instance keeps the storage resource and network endpoints so that restarting is transparent to the downstream services. See the status field for success or failures, if any.   
`primarySpec.mode`  
`string`  
 _Optional_ |  Mode specifies how this instance is managed by the operator. Possible values are as follows: `ManuallySetUpStandby`, `Pause`, `Recovery`, and `Maintenance`.   
`primarySpec.parameters`  
`object`  
 _Optional_ |  Parameters allows to set database parameters for the database cluster. Parameters take a key/value pair corresponding to the parameter name/value as defined by the database engine.   
`primarySpec.resources`  
`object`  
 _Required_ |  Resource specification for the database container. When any of the fields inside the resource changes, the operator restarts the database instance with the new resource specification.   
`primarySpec.resources.cpu`  
`integer or string`  
 _Required_ |  The amount of CPU allocated to the database container.   
`primarySpec.resources.disks`  
`object`  
 _Required_ |  The specifications of the disks allocated to the database container.   
`primarySpec.resources.disks.accessModes`  
`string`  
 _Optional_ |  AccessModes contains the desired access modes for the volume. For more information, see [Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).   
`primarySpec.resources.disks.annotations`  
`object`  
 _Optional_ |  Additional annotations added to the Persistent Volume Claim. This field lets you integrate with other tools.   
`primarySpec.resources.disks.name`  
`string`  
 _Required_ |  Name of the disk. The allowed values are: DataDisk, LogDisk, BackupDisk, and ObsDisk.   
`primarySpec.resources.disks.selector`  
`object`  
 _Optional_ |  A label query over volumes to consider for binding. If this field is set, then the volume with matching labels is used as the backing volume for the disk. For more information, see [PersistentVolumeClaimSpec](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#PersistentVolumeClaimSpec).   
`primarySpec.resources.disks.selector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.resources.disks.selector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.resources.disks.selector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`primarySpec.resources.disks.selector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.resources.disks.selector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.resources.disks.size`  
`string`  
 _Required_ |  Disk size in bytes for example, "10Gi" for 10 Gibibytes. This field is required. The allowed size unit prefixes are: "Ki", "Mi", "Gi", "Ti, "Pi" and "Ei" for 2-base. Also "K", "M", "G", "T, "P" and "E" for 10-base. For more information, see [Unit prefix](https://en.wikipedia.org/wiki/Unit_prefix).   
`primarySpec.resources.disks.storageClass`  
`string`  
 _Optional_ |  StorageClass points to a particular CSI storage class. This field is optional. If the field is not set, then the default CSI storage class for the Kubernetes cluster is used. If there is no default for the Kubernetes cluster, then the Persistence Volume Claim will fail and the database cluster will fail to provision. For more information, see [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes).   
`primarySpec.resources.disks.volumeName`  
`string`  
 _Optional_ |  VolumeName is the binding reference to the Persistent Volume tied to this disk. This field is optional. This allows to reuse an existing volume. Note that if this field is specified, the value "storageClass" will not take effect. For more information, see [Binding](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding).   
`primarySpec.resources.memory`  
`string or integer`  
 _Required_ |  The amount of memory allocated to the database container.   
`primarySpec.resources.memory`  
`string or integer`  
 _Required_ |  The amount of memory allocated to the database container.   
`primarySpec.schedulingConfig`  
`object`  
 _Optional_ |  SchedulingConfig specifies how the instance should be scheduled on Kubernetes nodes. When any field inside the scheduling config changes, it can lead to rescheduling of the Kubernetes pod onto a different node based on the config.   
`primarySpec.schedulingConfig.nodeAffinity`  
`object`  
 _Optional_ |  NodeAffinity describes node affinity scheduling rules for the instance.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prefers to schedule pods to nodes that satisfy the affinity expressions specified by this field, but the scheduler might choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, which means that for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum, if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference`  
`object`  
 _Required_ |  A node selector term, associated with the corresponding weight.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's labels.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's fields.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the affinity requirements specified by this field isn't met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field aren't met at some point during pod execution, for example due to an update, the system might or might not try to eventually evict the pod from its node.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms`  
`object`  
 _Required_ |  A list of node selector terms. The terms are ORed.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's labels.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields`  
`object`  
 _Optional_ |  A list of node selector requirements by the node's fields.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.key`  
`string`  
 _Required_ |  The label key that the selector applies to.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.operator`  
`string`  
 _Required_ |  Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`primarySpec.schedulingConfig.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.values`  
`string`  
 _Optional_ |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which is interpreted as an integer. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAffinity`  
`object`  
 _Optional_ |  PodAffinity describes pod affinity scheduling rules for the instance.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler will prioritize nodes that meet the affinity expressions specified in this field when scheduling pods. The scheduler might still choose a node that doesn't fully meet the criteria. The most preferred node is the one with the highest total weight. This weight is calculated by adding up values for each node that satisfies all scheduling requirements (such as resource requests or requiredDuringScheduling affinity expressions). For each matching podAffinityTerm, the node's weight increases, and the node(s) with the highest total weight are selected as the most preferred.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm`  
`object`  
 _Required_ |  A pod affinity term, associated with the corresponding weight.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`primarySpec.schedulingConfig.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the affinity requirements specified by this field isn't met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field aren't met at some point during pod execution - for example, due to a pod label update - the system might or might not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, which means that all terms must be satisfied.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.  
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`primarySpec.schedulingConfig.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`primarySpec.schedulingConfig.podAntiAffinity`  
`object`  
 _Optional_ |  PodAntiAffinity describes pod anti-affinity scheduling rules for the instance.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  The scheduler prefers to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but the scheduler might choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, in other words, for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum, if the node has pods which matches the corresponding podAffinityTerm. The node(s) with the highest sum are the most preferred.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm`  
`object`  
 _Required_ |  A pod affinity term, associated with the corresponding weight.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`primarySpec.schedulingConfig.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight`  
`integer`  
 _Required_ |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution`  
`object`  
 _Optional_ |  If the anti-affinity requirements specified by this field isn't met at scheduling time, the pod is not scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (for example, due to a pod label update), the system might or might not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, which means that all terms must be satisfied.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector`  
`object`  
 _Optional_ |  A label query over a set of resources, in this case, pods.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector`  
`object`  
 _Optional_ |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key`  
`string`  
 _Required_ |  key is the label key that the selector applies to.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces`  
`string`  
 _Optional_ |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace".   
`primarySpec.schedulingConfig.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey`  
`string`  
 _Required_ |  This pod must be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces. Co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
`primarySpec.schedulingConfig.tolerations`  
`object`  
 _Optional_ |  Tolerations enable the management of whether to allow or disallow scheduling an instance on a Kubernetes node that has a specific taint applied.   
`primarySpec.schedulingConfig.tolerations.effect`  
`string`  
 _Optional_ |  Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.   
`primarySpec.schedulingConfig.tolerations.key`  
`string`  
 _Optional_ |  Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists. This combination means to match all values and all keys.   
`primarySpec.schedulingConfig.tolerations.operator`  
`string`  
 _Optional_ |  Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.   
`primarySpec.schedulingConfig.tolerations.tolerationSeconds`  
`integer`  
 _Optional_ |  TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, this field isn't set, which means tolerate the taint forever (do not evict). Zero and negative values are treated as 0 (evict immediately) by the system.   
`primarySpec.schedulingConfig.tolerations.value`  
`string`  
 _Optional_ |  Value is the taint value the toleration matches to. If the operator is Exists, the value must be empty; otherwise, it must be a regular string.   
`primarySpec.services`  
`object`  
 _Optional_ |  Services list the optional semi-managed services that you can choose from.   
`primarySpec.sidecarRef`  
`object`  
 _Optional_ |  SidecarRef is a reference to a sidecar Custom Resource. If set, sidecar containers included in the sidecar Custom Resource are injected into the database pod.   
`primarySpec.sidecarRef.name`  
`string`  
 _Optional_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names).   
`primarySpec.sourceCidrRanges`  
`string`  
 _Optional_ |  Source IP CIDR ranges allowed for a client.   
`primarySpec.tls`  
`object`  
 _Optional_ |  TLS is the desired server certificate configuration for the instance. This field is optional. When this field is changed, the instance pods restart to load the specified certificate.   
`primarySpec.tls.certSecret`  
`object`  
 _Optional_ |  CertSecret contains the name of a certificate secret within the same namespace. The secret must contain entries ca.crt (CA certificate), tls.key (server private key), and tls.crt (server leaf certificate). This secret is used to set the TLS config for the database instance.   
`primarySpec.tls.certSecret.name`  
`string`  
 _Optional_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names)  
`primarySpec.walArchiveSetting`  
`object`  
 _Optional_ |  WalArchiveSetting specifies wal archive settings. If set, archive_mode is enabled to archive wal logs to specified location. For more information, see [Continuous Archiving and Point-in-Time Recovery (PITR)](https://www.postgresql.org/docs/15/continuous-archiving.html).   
`primarySpec.walArchiveSetting.archiveMode`  
`string`  
 _Optional_ |  ArchiveMode specifies archive_mode. For more information, see [archive_mode](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-ARCHIVE-MODE).   
`primarySpec.walArchiveSetting.location`  
`string`  
 _Optional_ |  Location is the location where archived WAL logs are stored.   
`tls`  
`object`  
 _Optional_ |  TLS is the desired server certificate configuration for the cluster.By default, this field is empty and a new self-signed CA and leaf certificate are generated for the cluster. When this field is changed, the database cluster pods will restart to load the specified certificate. The field status.certificateReference indicates the current CA certificate secret and key.   
`tls.certSecret`  
`object`  
 _Optional_ |  CertSecret references the certificate secret within the same namespace. The secret must contain entries ca.crt (CA certificate), tls.key (server private key), and tls.crt (server leaf certificate). This secret is used to set the TLS config for the database instances that a part of the database cluster.   
`tls.certSecret.name`  
`string`  
 _Optional_ |  Name of the referent. For more information, see [Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names)  
  
## Status schema

DBClusterStatus defines the observed state of DBCluster.
    
    
    healthCheck:
      isRegistered: boolean
      lastHealthCheckTime: string
    certificateReference:
      certificateKey: string
      secretRef:
        name: string
        namespace: string
    conditions:
    - lastTransitionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
    criticalIncidents:
    - code: string
      createTime: string
      message: string
      messageTemplateParams: object
      resource:
        component: string
        location:
          cluster: string
          group: string
          kind: string
          name: string
          namespace: string
          version: string
      stackTrace:
      - component: string
        message: string
      transientUntil: string
    latestFailoverStatus:
      failoverName: string
      status:
        conditions:
        - lastTransitionTime: string
          message: string
          observedGeneration: integer
          reason: string
          status: string
          type: string
        createTime: string
        criticalIncidents:
        - code: string
          createTime: string
          message: string
          messageTemplateParams: object
          resource:
            component: string
            location:
              cluster: string
              group: string
              kind: string
              name: string
              namespace: string
              version: string
          stackTrace:
          - component: string
            message: string
          transientUntil: string
      endTime: string
      internal:
        attempt: integer
        newPrimary: string
        oldPrimary: string
        phase: string
      observedGeneration: integer
      reconciled: boolean
      startTime: string
      state: string
    observedGeneration: integer
    phase: string
    primary:
      allocatedResources:
        cpu: integer or string
        disks:
          accessModes: string
          annotations: string
          name: string
          selector:
            matchExpressions:
            - key: string
              operator: string
              values: string
              matchLabels: object
            size: string
            storageClass: string
            volumeName: string
        memory: integer or string
      conditions:
      - lastTransitionTime: string
        message: string
        observedGeneration: integer
        reason: string
        status: string
        type: string
      currentControlPlaneAgentsVersion: string
      currentDatabaseImage: string
      currentDatabaseVersion: string
      currentParameters: object
      endpoint: string
      endpoints:
      - name: string
        value: string
      latestExport:
        creationTimeStamp: string
        exportName: string
        spec:
          dbclusterRef: string
          exportLocation:
            gcsOptions:
              bucket: string
              key: string
              secretRef:
                name: string
                namespace: string
            type: string
        status:
          completeTime: string
          conditions:
          - lastTransitionTime: string
            message: string
            observedGeneration: integer
            reason: string
            status: string
            type: string
          criticalIncidents:
          - code: string
            createTime: string
            message: string
            messageTemplateParams: object
            resource:
              component: string
              location:
                cluster: string
                group: string
                kind: string
                name: string
                namespace: string
                version: string
            stackTrace:
            - component: string
              message: string
            transientUntil: string
          exportSubDirectory: string
          observedGeneration: integer
          phase: string
          reconciled: boolean
          startTime: string
      latestImport:
        creationTimeStamp: string
        importName: string
        spec:
          databaseName: string
          dbclusterRef: string
          downloadOnly: boolean
          dumpStorage:
            gcsOptions:
              bucket: string
              key: string
              secretRef:
                name: string
                namespace: string
            type: string
          logStorage:
            gcsOptions:
              bucket: string
              key: string
              secretRef:
                name: string
                namespace: string
            type: string
        status:
          completeTime: string
          conditions:
          - lastTransitionTime: string
            message: string
            observedGeneration: integer
            reason: string
            status: string
            type: string
          criticalIncidents:
          - code: string
            createTime: string
            message: string
            messageTemplateParams: object
            resource:
              component: string
              location:
                cluster: string
                group: string
                kind: string
                name: string
                namespace: string
                version: string
            stackTrace:
            - component: string
              message: string
            transientUntil: string
          dumpPath: string
          observedGeneration: integer
          phase: string
          reconciled: boolean
          startTime: string
      phase: string
      url: string
      walArchiveSetting:
        location: string
    reconciled: boolean
    registrationStatus:
      IsHA: boolean
      IsRegistered: boolean
      RegistrationTime: string
    restoredFrom:
      restoredTime: string
      sourceDBCluster: object
    serviceAccounts: string
    

FieldType  
Required or optional |  Description  
---|---  
`healthCheck`  
`object`  
 _Optional_ |  HealthStatus represents the health check.   
`healthCheck.isRegistered`  
`boolean`  
 _Optional_ |  N/A   
`healthCheck.lastHealthCheckTime`  
`string`  
 _Optional_ |  N/A   
`certificateReference`  
`object`  
 _Optional_ |  CertificateReference refers to a secret and a key of the server CA certificate that can be used to connect to the database. If spec.TLS is provided, this value should refer to the same secret after the database has been configured to use the provided server certificate.   
`certificateReference.certificateKey`  
`string`  
 _Optional_ |  CertificateKey is the key used to search the secret for the Certificate.   
`certificateReference.secretRef`  
`object`  
 _Optional_ |  SecretRef is a reference to the secret that contains the Certificate.   
`certificateReference.secretRef.name`  
`string`  
 _Optional_ |  name is unique within a namespace to reference a secret resource.   
`certificateReference.secretRef.namespace`  
`string`  
 _Optional_ |  namespace defines the space within which the secret name must be unique.   
`conditions`  
`list (object)`  
_Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`conditions[]`  
`object`  
 _Optional_ |  Conditions contains details for one aspect of the current state of this API Resource.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another, which occurs when the underlying condition changed. If the time when the underlying condition changed is unknown, use the time when the API field changed.   
`conditions[].message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This can be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is 12 and the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types can define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value must be a CamelCase string. This field might not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  The status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  The type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression that it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`criticalIncidents`  
`object`  
 _Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[]`  
`object`  
 _Optional_ |  CriticalIncident contains all information about an ongoing critical incident.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident, as well as information about the Kubernetes resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind of the Kubernetes resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  Group is the Version of the Kubernetes resource.   
`criticalIncidents[].stackTrace`  
`object`  
 _Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace.component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`latestFailoverStatus`  
`object`  
 _Optional_ |  LatestFailoverStatus is the status of the most recently updated failover for the database cluster This status is a copy of the status of the current or most recently updated failover operation for the database cluster. This can be used to conveniently monitor the status of a currently running failover operation.   
`latestFailoverStatus.failoverName`  
`string`  
 _Optional_ |  FailoverName is the Name of the latest failover.   
`latestFailoverStatus.status`  
`object`  
 _Optional_ |  Status represents status of the latest failover for the database cluster.   
`latestFailoverStatus.status.conditions`  
`object`  
 _Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`latestFailoverStatus.status.conditions.lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another, which occurs when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`latestFailoverStatus.status.conditions.message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This may be an empty string.   
`latestFailoverStatus.status.conditions.observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`latestFailoverStatus.status.conditions.reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types can define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`latestFailoverStatus.status.conditions.status`  
`string`  
 _Required_ |  The status of the condition, one of True, False, Unknown.   
`latestFailoverStatus.status.conditions.type`  
`string`  
 _Required_ |  The type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression that it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`latestFailoverStatus.status.createTime`  
`string`  
 _Optional_ |  CreateTime is the time when the internal failover workflow mechanism was created.   
`latestFailoverStatus.status.criticalIncidents`  
`object`  
 _Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`latestFailoverStatus.status.criticalIncidents.code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`latestFailoverStatus.status.criticalIncidents.createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`latestFailoverStatus.status.criticalIncidents.message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`latestFailoverStatus.status.criticalIncidents.messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`latestFailoverStatus.status.criticalIncidents.resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident as well as information about the Kubernetes resource.   
`latestFailoverStatus.status.criticalIncidents.resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`latestFailoverStatus.status.criticalIncidents.resource.location`  
`object`  
 _Optional_ |  Location   
`latestFailoverStatus.status.criticalIncidents.resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`latestFailoverStatus.status.criticalIncidents.resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`latestFailoverStatus.status.criticalIncidents.resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind of the Kubernetes resource.   
`latestFailoverStatus.status.criticalIncidents.resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`latestFailoverStatus.status.criticalIncidents.resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`latestFailoverStatus.status.criticalIncidents.resource.location.version`  
`string`  
 _Optional_ |  Group is the Version of the k8s resource.   
`latestFailoverStatus.status.criticalIncidents.stackTrace`  
`object`  
 _Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`latestFailoverStatus.status.criticalIncidents.stackTrace.component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`latestFailoverStatus.status.criticalIncidents.stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`latestFailoverStatus.status.criticalIncidents.transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`latestFailoverStatus.status.endTime`  
`string`  
 _Optional_ |  EndTime is the time failover reached its final state.   
`latestFailoverStatus.status.internal`  
`object`  
 _Optional_ |  Internal is used by the system controllers. Do not depend on the information in this section.   
`latestFailoverStatus.status.internal.attempt`  
`integer`  
 _Required_ |  Attempt is used for retry logic and the default value is `0`.   
`latestFailoverStatus.status.internal.newPrimary`  
`string`  
 _Required_ |  NewPrimary is the instance that you're attempting to failover to.   
`latestFailoverStatus.status.internal.oldPrimary`  
`string`  
 _Required_ |  OldPrimary is the instance that was the primary at the start of the failover.   
`latestFailoverStatus.status.internal.phase`  
`string`  
 _Optional_ |  Phase is used to keep track of the current state of the failover.   
`latestFailoverStatus.status.observedGeneration`  
`integer`  
 _Optional_ |  The generation observed by the controller.   
`latestFailoverStatus.status.reconciled`  
`boolean`  
 _Optional_ |  Whether the resource was reconciled by the controller.   
`latestFailoverStatus.status.startTime`  
`string`  
 _Optional_ |  StartTime is the time that the failover operation started.   
`latestFailoverStatus.status.state`  
`string`  
 _Optional_ |  State is the current state of the failover operation. The values are InProgress, Success, Failed_RollbackInProgress, Failed_RollbackSuccess, and Failed_RollbackFailed. 

  * InProgress means the failover is still in progress.
  * Success means that the failover completed. This is complete when the new primary instance is successfully promoted.
  * Failed_RollbackInProgress means that the operator is unable to promote the new primary instance, and that it's attempting to restart the old primary instance.
  * Failed_RollbackSuccess means that the operator was unable to promote the new primary instance, and that it successfully restarted the old primary instance.
  * Failed_RollbackFailed means that the operator was unable to promote the new primary instance, and that the operator wasn't able to restart the old primary instance. The DBCluster might need to be manually repaired.

  
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`phase`  
`string`  
 _Optional_ |  N/A   
`primary`  
`object`  
 _Optional_ |  Primary contains the status of the primary Instance.   
`primary.allocatedResources`  
`object`  
 _Optional_ |  AllocatedResources represents the current configuration of memory, CPU, and disks.   
`primary.allocatedResources.cpu`  
`integer or string`  
 _Required_ |  The amount of CPU allocated to the database container.   
`primary.allocatedResources.disks`  
`object`  
 _Required_ |  The specifications of the disks allocated to the database container.   
`primary.allocatedResources.disks.accessModes`  
`string`  
 _Optional_ |  AccessModes contains the desired access modes for the volume. For more information, see [Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).   
`primary.allocatedResources.disks.annotations`  
`object`  
 _Optional_ |  Additional annotations added to the Persistent Volume Claim. This allows integration with other tools.   
`primary.allocatedResources.disks.name`  
`string`  
 _Required_ |  Name of the disk. This field is required. The allowed values are: "DataDisk", "LogDisk" , "BackupDisk" and "ObsDisk".   
`primary.allocatedResources.disks.selector`  
`object`  
 _Optional_ |  A label query over volumes to consider for binding. If this field is set, then the volume with matching labels is used as the backing volume for the disk. For more information, see [PersistentVolumeClaimSpec](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#PersistentVolumeClaimSpec)  
`primary.allocatedResources.disks.selector`  
`object`  
 _Optional_ |  A label query over volumes to consider for binding. If this field is set, then the volume with matching labels is used as the backing volume for the disk. For more information, see [PersistentVolumeClaimSpec](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#PersistentVolumeClaimSpec).   
`primary.allocatedResources.disks.selector.matchExpressions`  
`object`  
 _Optional_ |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`primary.allocatedResources.disks.selector.matchExpressions.operator`  
`string`  
 _Required_ |  operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, and DoesNotExist.   
`primary.allocatedResources.disks.selector.matchExpressions.values`  
`string`  
 _Optional_ |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
`primary.allocatedResources.disks.selector.matchlabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primary.allocatedResources.disks.selector.matchlabels`  
`object`  
 _Optional_ |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
`primary.allocatedResources.disks.size`  
`string`  
 _Required_ |  Disk size in bytes for example, "10Gi" for 10 Gibibytes. This field is required. The allowed size unit prefixes are: "Ki", "Mi", "Gi", "Ti, "Pi" and "Ei" for 2-base. Also "K", "M", "G", "T, "P" and "E" for 10-base. For more information, see [Unit prefix](https://en.wikipedia.org/wiki/Unit_prefix).   
`primary.allocatedResources.disks.storageClass`  
`string`  
 _Optional_ |  StorageClass points to a particular CSI storage class. This field is optional. If the field is not set, then the default CSI storage class for the Kubernetes cluster is used. If there is no default for the Kubernetes cluster, then the Persistence Volume Claim will fail and the database cluster will fail to provision. For more information, see [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes).   
`primary.allocatedResources.disks.volumeName`  
`string`  
 _Optional_ |  VolumeName is the binding reference to the Persistent Volume tied to this disk. This field is optional. This allows to reuse an existing volume. Note that if this field is specified, the value "storageClass" will not take effect. For more information, see [Binding](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#binding).   
`primary.allocatedResources.memory`  
`string or integer`  
 _Required_ |  The amount of memory allocated to the database container.   
`primary.allocatedResources.memory`  
`string or integer`  
 _Required_ |  The amount of memory allocated to the database container.   
`primary.conditions`  
`object`  
 _Required_ |  Conditions represents the latest available observations of the Instance's current state.   
`primary.conditions.lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another, which occurs when the underlying condition changed. If the time when the underlying condition changed is unknown, you can use the time when the API field changed.   
`primary.conditions.message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This can be an empty string.   
`primary.conditions.observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is 12 but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`primary.conditions.reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types can define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field might not be empty.   
`primary.conditions.status`  
`string`  
 _Required_ |  The status of the condition, one of True, False, Unknown.   
`primary.conditions.type`  
`string`  
 _Required_ |  The type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression that it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`primary.currentControlPlaneAgentsVersion`  
`string`  
 _Optional_ |  CurrentControlPlaneAgentsVersion is the control plane agents version that the primary instance is running. This value must match the value of spec.controlPlaneAgentsVersion after the primary instance is provisioned or the upgrade or downgrade completes successfully.   
`primary.currentDatabaseImage`  
`string`  
 _Optional_ |  CurrentDatabaseImage is the customized database image that the primary instance is using. This value must match the value of spec.databaseImage after the primary instance is provisioned or the upgrade or downgrade completes successfully.   
`primary.currentDatabaseVersion`  
`string`  
 _Optional_ |  CurrentDatabaseVersion is the current database version that the primary instance is running. This value should match the value of spec.databaseVersion after the primary instance is provisioned or the upgrade or downgrade has concluded successfully.   
`primary.currentParameters`  
`object`  
 _Optional_ |  CurrentParameters indicates the current values of the parameters. CurrentParameters allows to verify that the spec.primarySpec.parameters field has been applied to the database. Only the parameters names in spec.primarySpec.parameters will be included in this field.   
`primary.endpoint`  
`string`  
 _Optional_ |  Endpoint is the address that can be used to establish database connections. Deprecated: use the Endpoints field instead.   
`primary.endpoints`  
`object`  
 _Optional_ |  Endpoints contains all the endpoint through which you can access this instance.   
`primary.endpoints.name`  
`string`  
 _Required_ |  Name contains the name of the endpoint.   
`primary.endpoints.value`  
`string`  
 _Optional_ |  Value contains the endpoint information.   
`primary.endpoints.value`  
`string`  
 _Optional_ |  Value contains the endpoint information.   
`primary.latestExport`  
`object`  
 _Optional_ |  LatestExport represents the latest export for the database instance.   
`primary.latestExport.creationTimeStamp`  
`string`  
 _Optional_ |  CreationTimeStamp represents the creation time of the export for the database instance.   
`primary.latestExport.exportName`  
`string`  
 _Optional_ |  ExportName is the Name of the latest export.   
`primary.latestExport.spec`  
`object`  
 _Optional_ |  Spec represents the spec of the export for the database instance.   
`primary.latestExport.spec.dbclusterRef`  
`string`  
 _Optional_ |  DBClusterRef is the dbcluster name within the same namespace to export from.   
`primary.latestExport.spec.exportLocation`  
`object`  
 _Required_ |  ExportLocation specifies a storage location for the export files. You must ensure proper write access to the storage bucket from within the Operator.   
`primary.latestExport.spec.exportLocation.gcsOptions`  
`object`  
 _Optional_ |  GCSOptions is a reference to Cloud Storage-dependent options.   
`primary.latestExport.spec.exportLocation.gcsOptions.bucket`  
`string`  
 _Required_ |  Bucket is a required field, for example, dbs-dump-bucket. You must ensure proper write access to the storage bucket from within the Operator.   
`primary.latestExport.spec.exportLocation.gcsOptions.key`  
`string`  
 _Required_ |  The object key for the dump files, for example, ods-dump/scottschema.dmp.   
`primary.latestExport.spec.exportLocation.gcsOptions.secretRef`  
`object`  
 _Optional_ |  SecretRef is a reference to the secret that stores Cloud Storage access information.   
`primary.latestExport.spec.exportLocation.gcsOptions.secretRef.name`  
`string`  
 _Optional_ |  name is unique within a namespace to reference a secret resource.   
`primary.latestExport.spec.exportLocation.gcsOptions.secretRef.namespace`  
`string`  
 _Optional_ |  namespace defines the space within which the secret name must be unique.   
`primary.latestExport.spec.exportLocation.type`  
`string`  
 _Required_ |  The type of Repository, for example, S3 or GCS, which tells the agent which storage system or API to use.   
`primary.latestExport.status`  
`object`  
 _Optional_ |  Status represents the of the latest import for the database instance.   
`primary.latestExport.status.completeTime`  
`string`  
 _Optional_ |  CompleteTime is the time when the export completed.   
`primary.latestExport.status.conditions`  
`object`  
 _Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`primary.latestExport.status.conditions.lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another. This must be when the underlying condition changed. If the time when the underlying condition changed is unknown, use the time when the API field changed.   
`primary.latestExport.status.conditions.message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This may be an empty string.   
`primary.latestExport.status.conditions.observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12 and the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`primary.latestExport.status.conditions.reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value must be a CamelCase string. This field might not be empty.   
`primary.latestExport.status.conditions.status`  
`string`  
 _Required_ |  The status of the condition, one of True, False, Unknown.   
`primary.latestExport.status.conditions.type`  
`string`  
 _Required_ |  The type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression that it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`primary.latestExport.status.criticalIncidents`  
`object`  
 _Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`primary.latestExport.status.criticalIncidents.code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`primary.latestExport.status.criticalIncidents.createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`primary.latestExport.status.criticalIncidents.message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`primary.latestExport.status.criticalIncidents.messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`primary.latestExport.status.criticalIncidents.resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident, as well as information about the Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`primary.latestExport.status.criticalIncidents.resource.location`  
`object`  
 _Optional_ |  Location   
`primary.latestExport.status.criticalIncidents.resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind name of the Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.location.version`  
`string`  
 _Optional_ |  Group is the Version of the Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.resource.location.version`  
`string`  
 _Optional_ |  Group is the Version of the Kubernetes resource.   
`primary.latestExport.status.criticalIncidents.stackTrace`  
`object`  
 _Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`primary.latestExport.status.criticalIncidents.stackTrace.component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`primary.latestExport.status.criticalIncidents.stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`primary.latestExport.status.criticalIncidents.transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`primary.latestExport.status.exportSubDirectory`  
`string`  
 _Optional_ |  ExportSubDirectory is the subdirectory appended to ExportLocation to store exported files.   
`primary.latestExport.status.observedGeneration`  
`integer`  
 _Optional_ |  ExportSubDirectory is the subdirectory appended to ExportLocation to store exported files.   
`primary.latestExport.status.phase`  
`string`  
 _Optional_ |  Phase is a summary of current state of the export.   
`primary.latestExport.status.reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`primary.latestExport.status.startTime`  
`string`  
 _Optional_ |  StartTime is the time when the export started.   
`primary.latestImport`  
`object`  
 _Optional_ |  LatestImport represents the latest import for the database instance.   
`primary.latestImport.creationTimeStamp`  
`string`  
 _Optional_ |  CreationTimeStamp represents the creation time of the import for the database instance.   
`primary.latestImport.importName`  
`string`  
 _Optional_ |  ImportName is the Name of the latest import.   
`primary.latestImport.spec`  
`object`  
 _Optional_ |  Spec represents the spec of the import for the database instance.   
`primary.latestImport.spec.databaseName`  
`string`  
 _Optional_ |  DatabaseName is the database resource name within Instance to import into.   
`primary.latestImport.spec.dbclusterRef`  
`string`  
 _Optional_ |  DBClusterRef is the dbcluster name within the same namespace to import into.   
`primary.latestImport.spec.downloadOnly`  
`boolean`  
 _Optional_ |  DownloadOnly when set to true means dump file will be downloaded but not imported into DB. Default is false.   
`primary.latestImport.spec.dumpStorage`  
`object`  
 _Required_ |  DumpStorage specifies a storage location for the import dump files. You must ensure proper read access to the storage bucket from within the Operator.   
`primary.latestImport.spec.dumpStorage.gcsOptions`  
`object`  
 _Optional_ |  GCSOptions is a reference to Cloud Storage-dependent options.   
`primary.latestImport.spec.dumpStorage.gcsOptions.bucket`  
`string`  
 _Required_ |  Bucket is a required field, for example, dbs-dump-bucket. You must ensure proper write access to the storage bucket from within the Operator.   
`primary.latestImport.spec.dumpStorage.gcsOptions.key`  
`string`  
 _Required_ |  The object key for the dump files, for example, ods-dump/scottschema.dmp.   
`primary.latestImport.spec.dumpStorage.gcsOptions.secretRef`  
`object`  
 _Optional_ |  SecretRef is a reference to the secret that stores Cloud Storage access information.   
`primary.latestImport.spec.dumpStorage.gcsOptions.secretRef.name`  
`string`  
 _Optional_ |  name is unique within a namespace to reference a secret resource.   
`primary.latestImport.spec.dumpStorage.gcsOptions.secretRef.namespace`  
`string`  
 _Optional_ |  namespace defines the space within which the secret name must be unique.   
`primary.latestImport.spec.dumpStorage.type`  
`string`  
 _Required_ |  The type of Repository, for example, S3 or GCS, which tells the agent which storage system or API to use.   
`primary.latestImport.spec.logStorage`  
`object`  
 _Optional_ |  LogStorage optionally specifies a storage location to copy import log to. You must ensure proper write access to the storage bucket from within the Operator.   
`primary.latestImport.spec.logStorage.gcsOptions`  
`object`  
 _Optional_ |  GCSOptions is a reference to Cloud Storage-dependent options.   
`primary.latestImport.spec.logStorage.gcsOptions.bucket`  
`string`  
 _Required_ |  Bucket is a required field, for example, dbs-dump-bucket. You must ensure proper write access to the storage bucket from within the Operator.   
`primary.latestImport.spec.logStorage.gcsOptions.key`  
`string`  
 _Required_ |  Object key for the dump files.   
`primary.latestImport.spec.logStorage.gcsOptions.secretRef`  
`object`  
 _Optional_ |  SecretRef is a reference to the secret that stores Cloud Storage access information.   
`primary.latestImport.spec.logStorage.gcsOptions.secretRef.name`  
`string`  
 _Optional_ |  name is unique within a namespace to reference a secret resource.   
`primary.latestImport.spec.logStorage.gcsOptions.secretRef.namespace`  
`string`  
 _Optional_ |  namespace defines the space within which the secret name must be unique.   
`primary.latestImport.spec.logStorage.type`  
`string`  
 _Required_ |  The type of Repository that tells the agent which storage system or API to use.   
`primary.latestImport.status`  
`object`  
 _Optional_ |  Status represents the of the latest import for the database instance.   
`primary.latestImport.status.completeTime`  
`string`  
 _Optional_ |  CompleteTime is the time import completed.   
`primary.latestImport.status.conditions`  
`object`  
 _Optional_ |  Conditions represents the latest available observations of the Entity's current state.   
`primary.latestImport.status.conditions.lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another. This must be when the underlying condition changed. If the time when the underlying condition changed is unknown, use the time when the API field changed.   
`primary.latestImport.status.conditions.message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This may be an empty string.   
`primary.latestImport.status.conditions.observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is 12 and the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`primary.latestImport.status.conditions.reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value must be a CamelCase string. This field might not be empty.   
`primary.latestImport.status.conditions.status`  
`string`  
 _Required_ |  The status of the condition, one of True, False, Unknown.   
`primary.latestImport.status.conditions.type`  
`string`  
 _Required_ |  type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regula expression that it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`primary.latestImport.status.criticalIncidents`  
`object`  
 _Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`primary.latestImport.status.criticalIncidents.code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`primary.latestImport.status.criticalIncidents.createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`primary.latestImport.status.criticalIncidents.message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`primary.latestImport.status.criticalIncidents.messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`primary.latestImport.status.criticalIncidents.resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident, as well as information about the Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`primary.latestImport.status.criticalIncidents.resource.location`  
`object`  
 _Optional_ |  Location   
`primary.latestImport.status.criticalIncidents.resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind of the Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.resource.location.version`  
`string`  
 _Optional_ |  Group is the Version of the Kubernetes resource.   
`primary.latestImport.status.criticalIncidents.stackTrace`  
`object`  
 _Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`primary.latestImport.status.criticalIncidents.stackTrace.component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`primary.latestImport.status.criticalIncidents.stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`primary.latestImport.status.criticalIncidents.transientUntil`  
`string`  
 _Optional_ |  TransientUntil, if present, indicates that the issue must be considered transient until the specified time.   
`primary.latestImport.status.dumpPath`  
`string`  
 _Optional_ |  DumpPath is the path of the downloaded dump file for download only import.   
`primary.latestImport.status.observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`primary.latestImport.status.phase`  
`string`  
 _Optional_ |  Phase is a summary of current state of the import.   
`primary.latestImport.status.reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`primary.latestImport.status.startTime`  
`string`  
 _Optional_ |  StartTime is the time import started.   
`primary.phase`  
`string`  
 _Optional_ |  Phase is a summary of current state of the Instance.   
`primary.walArchiveSetting`  
`object`  
 _Optional_ |  WalArchiveSetting represents the current write-ahead log (WAL) archive settings.   
`primary.walArchiveSetting.location`  
`string`  
 _Optional_ |  N/A   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`registrationStatus`  
`object`  
 _Optional_ |  RegistrationStatus represents the status of migration for the database cluster.   
`registrationStatus.isHA`  
`boolean`  
 _Optional_ |  IsHA is set to true when DBClusterSpec HA Availability setting has at least 1 numberOfStandbys setup.   
`registrationStatus.isRegistered`  
`boolean`  
 _Optional_ |  N/A   
`registrationStatus.isRegistered`  
`string`  
 _Optional_ |  RegistrationTime represents the time when the on-premises database cluster was registered with Google Cloud.   
`restoredFrom`  
`object`  
 _Optional_ |  RestoredFrom is the status showing the most recent restore source for current DBCluster.   
`restoredFrom.restoredTime`  
`string`  
 _Optional_ |  Time point of the source DBCluster that this DBCluster restores from.   
`restoredFrom.sourceDBCluster`  
`string`  
 _Optional_ |  The source DBCluster that this DBCluster restores from.   
`restoredFrom.sourceDBCluster`  
`string`  
 _Optional_ |  The source DBCluster that this DBCluster restores from.   
`serviceAccounts`  
`object`  
 _Optional_ |  ServiceAccounts contains the service accounts created by the control plane to be used by different operations. By granting permissions to these service accounts, the database can interact with other services within the Kubernetes ecosystem. For further information, including what permissions is required, refer to the documentation of each operation.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
