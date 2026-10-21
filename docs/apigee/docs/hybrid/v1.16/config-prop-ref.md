---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref/
title: Configuration property reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:57.034559+00:00
---

# Configuration property reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuration property reference Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/config-prop-ref.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/config-prop-ref.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/config-prop-ref.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/config-prop-ref.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/config-prop-ref.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/config-prop-ref.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/config-prop-ref.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/config-prop-ref.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/config-prop-ref.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/config-prop-ref.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/config-prop-ref.html)



This section lists all of the configuration properties that you can use to customize the runtime plane of your Apigee hybrid deployment.

**Note:** For instructions on how to add custom annotations, which are key/value maps used to attach metadata to Apigee hybrid Kubernetes pods, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations). 

#### About configuration properties

You can override many configuration properties, if needed, by adding them to `HYBRID_ROOT_DIR/overrides.yaml`.

**Tip:** Apigee provides a small set of sample configurations that you can use for further guidance. See [Sample overrides file](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#sample-override-configurations).

For example, to change the replica count minimum and maximum for the MART service, you could add this stanza to `overrides.yaml`: 
    
    
    mart:
        replicaCountMin: 3
        replicaCountMax: 6

You can also find these config properties and their default settings in `HYBRID_ROOT_INSTALL/1.0.0/values.yaml`

For more information, see [`Manage runtime plane components`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services).

Additionally, if you are configuring a deployment outside Google Cloud see [ Step 7: Create the overrides](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides) for information on setting these properties.

## Filter this page

To filter the properties displayed on this page, select **Basic** (most common properties) or **Advanced** (properties that rarely need changing): 

filter_list_alt**Display** AllBasicAdvanced **configuration properties on this page.** **Caution:** Do not change advanced properties without first testing them in lower environments and verifying them in the specific operating environment. 

## Top-level properties

The following table describes the top-level properties in the `overrides.yaml` file. These are properties that do not belong to another object, and apply at the org or environment level:

Property | Type | Description  
---|---|---  
`axHashSalt` | Advanced | **Introduced in version:** 1.3.0 **Default value:** `iloveapis123` **Chart:** `apigee-org` **Optional** The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) that contains a salt used when computing hashes to [obfuscate user data](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/obfuscate-userdata-for-analytics) before it is sent to Apigee analytics. If you do not specify a salt value, `iloveapis123` is used by default. [Create the secret](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret-using-kubectl) with the salt value as its input. You can use the same salt across multiple clusters to ensure consistent hashing results between the clusters. Apigee uses SHA512 to hash the original value before sending data from the runtime plane to the control plane. See: [Obfuscate user data for analytics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/obfuscate-userdata-for-analytics).  
`contractProvider` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `https://apigee.googleapis.com` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` Defines the API path for all APIs in your installation. Required if your hybrid installation is using [Data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) in the following format: 
    
    
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com

Where CONTROL_PLANE_LOCATION is the location where control plane data like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://cloud.devsite.corp.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).  For example:
    
    
    contractProvider: https://us-apigee.googleapis.com  
  
`customAutoscaling.enabled` | Basic | **Introduced in version:** 1.14.0 **Default value:** `true` **Chart:** `apigee-telemetry` Enables Apigee's [metric-based autoscaling](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/scale-and-autoscale#metrics-scaling) when set to `true` (the default). Set to `false` to disable custom autoscaling. Apply changes to `customAutoscaling.enabled` by updating the `apigee-telemetry` chart.  
`enhanceProxyLimits` | Advanced | **Introduced in version:** 1.14.0 **Default value:** `false` **Chart:** `apigee-org`, `apigee-virtualhost` **Required** `enhanceProxyLimits` is required for Apigee's Enhanced per-environment proxy limits feature. Set this to `enhanceProxyLimits: true` if your hybrid organization is entitled for Enhanced per-environment proxy limits.  **Note:** This feature is available as part of the [2024 subscription plan](https://cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements). See:

  * [API Proxy limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#api-proxies). 
  * [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits). 
  * [Subscription entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements). 

Setting `enhanceProxyLimits: true` is required for proxy chaining, endpoint chaining, and ServiceCallout chaining. For information, see: 

  * [Chaining API proxies together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies)
  * [ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy)

**Alert:** Do not set this value to `false` once set to `true`. Apply changes to `enhanceProxyLimits` by updating the `apigee-org` chart and the `apigee-virtualhost` chart for every environment group.  
`gcpProjectID` | Advanced | Deprecated: For v1.2.0 and later, use `gcp.projectID` instead. **Introduced in version:** 1.0.0 **Default value:** none **Chart:** `apigee-telemetry`, `apigee-org` **Required** ID of your Google Cloud project. Works with `k8sClusterName` (deprecated) and `gcpRegion` (deprecated) to identify the project and determine where the `apigee-logger` and the `apigee-metrics` push their data.  
`gcpRegion` | Advanced | Deprecated: For v1.2.0 and later, use `gcp.region` instead. **Introduced in version:** 1.0.0 **Default value:** `us-central1` **Chart:** `apigee-telemetry`, `apigee-org` **Required** The closet Google Cloud region or zone of your Kubernetes cluster. Works with `gcpProjectID` (deprecated) and `k8sClusterName` (deprecated) to identify the project and determine where the `apigee-logger` and the `apigee-metrics` push their data.  
`hub` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` The URL of a private image container repository used to pull images for all apigee components from a private repo.  `hub` provides a default path for all Apigee hybrid components. If you are using a private repository, use `hub` to set the repository URL for all components rather than using the individual `image.url` property for each component. Only configure indivisual URLs if you are using a separate repository for a specific component.  The image path for each individual component will be the value of `hub` plus the image name and tag for the component.  For example, if the value of `hub` `private-docker-host.example.com`, individual components will automatically resolve the image path: 
    
    
    hub: private-docker-host.example.com

as:
    
    
    containers:
    - name: apigee-udca
      image: private-docker-host.example.com/apigee-udca:1.16.11
      imagePullPolicy: IfNotPresent

**Note:** Prior to Apigee hybrid version 1.14.2, third party components had a unique to the version of the image from the third-party vendor. For example: 
    
    
    ## an example of internal component vs 3rd party
    containers:
      - name: apigee-udca
        image: private-docker-host.example.com/apigee-udca:1.16.11
        imagePullPolicy: IfNotPresent
    
      containers:
      - name: apigee-ingressgateway
        image: private-docker-host.example.com/apigee-asm-ingress:1.22.6-asm.2-distroless
        imagePullPolicy: IfNotPresent

The other components will follow a similar pattern. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for all components.  See [Use a private image repository with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/container-images). You can override image URL for components individualy with the following properties:

  * `ao.image.url`
  * `apigeeIngressGateway.image.url`
  * `cassandra.image.url`
  * `cassandra.auth.image.url`
  * `cassandra.backup.image.url`
  * `cassandra.restore.image.url`
  * `connectAgent.image.url`
  * `guardrails.image.url`
  * `ingressGateways[].image.url`
  * `istiod.image.url`
  * `kubeRBACProxy.image.url`
  * `logger.image.url`
  * `mart.image.url`
  * `metrics.adapter.image.url`
  * `metrics.prometheus.image.url`
  * `metrics.sdSidecar.image.url`
  * `mintTaskScheduler.image.url`
  * `redis.image.url`
  * `redis.envoy.image.url`
  * `runtime.image.url`
  * `synchronizer.image.url`
  * `udca.image.url`
  * `udca.fluentd.image.url`
  * `watcher.image.url`

  
`imagePullSecrets[].name` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-operator`, `apigee-redis`, `apigee-org`, `apigee-env` Kubernetes secret name configured as docker-registry type; used to pull images from private repo.  
`instanceID` | Basic | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-org` **Required** A unique identifier for this installation. A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters in length. You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).   
`kmsEncryptionKey` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `defaults.org.kmsEncryptionKey` **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kmsEncryptionKey** or **kmsEncryptionPath** or **kmsEncryptionSecret**. Local file system path for the Apigee KMS data's encryption key.  
`kmsEncryptionPath` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kmsEncryptionKey** or **kmsEncryptionPath** or **kmsEncryptionSecret**. The path to a file containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`kmsEncryptionSecret.key` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kmsEncryptionKey** or **kmsEncryptionPath** or **kmsEncryptionSecret**. The key of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`kmsEncryptionSecret.name` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kmsEncryptionKey** or **kmsEncryptionPath** or **kmsEncryptionSecret**. The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`kvmEncryptionKey` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `defaults.org.kmsEncryptionKey` **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kvmEncryptionKey** or **kvmEncryptionPath** or **kvmEncryptionSecret**. Local file system path for the Apigee KVM data's encryption key.  
`kvmEncryptionPath` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kvmEncryptionKey** or **kvmEncryptionPath** or **kvmEncryptionSecret**. The path to a file containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`kvmEncryptionSecret.key` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kvmEncryptionKey** or **kvmEncryptionPath** or **kvmEncryptionSecret**. The key of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`kvmEncryptionSecret.name` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` **Optional.** Use only one of **kvmEncryptionKey** or **kvmEncryptionPath** or **kvmEncryptionSecret**. The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`multiOrgCluster` | Advanced | **Introduced in version:** 1.10.0 **Default value:** `false` **Chart:** `apigee-telemetry` For multi-org clusters, this property enables the organization's metrics to be exported to the project listed in the `gcp.projectID` property. Apply this setting in the overrides file for each organization in a multi-org cluster. For more information, see [Adding multiple hybrid orgs to a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-org).   
`namespace` | Basic | **Introduced in version:** 1.0.0 **Default value:** `apigee` **Chart:** `apigee-datastore`, `apigee-env`, `apigee-ingress-manager`, `apigee-operator`, `apigee-org`, `apigee-redis`, `apigee-telemetry`, `apigee-virtualhost` The namespace of your Kubernetes cluster where the Apigee components will be installed.  
`org` | Basic |  **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-operator`, `apigee-telemetry`, `apigee-org`, `apigee-env`, `apigee-virtualhost` **Required** The hybrid-enabled organization that was provisioned for you by Apigee during the hybrid installation. An organization is the top-level container in Apigee. It contains all your API proxies and related resources. If the value is empty, you must update it with your org name once you have created it.  
`revision` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `"11611"` (Your Apigee hybrid version without periods. For example for version 1.12.0, the default value is `"1120"`.) **Chart:** `apigee-operator` Apigee hybrid supports rolling Kubernetes updates, which allow deployment updates to take place with zero downtime by incrementally updating Pod instances with new ones.  When updating certain YAML overrides that result in underlying Kubernetes `PodTemplateSpec` change, the `revision` override property must also be changed in the customer's `override.yaml`. This is required for the underlying Kubernetes _ApigeeDeployment_ (AD) controller to conduct a safe rolling update of from the previous version to the new version. You can use any lowercase text value, eg: `blue`, `a`, `1.0.0` **Note:**`revision` can accept only lowercase alpha characters, numbers, and punctuation. When the `revision` property is changed and applied, a rolling update will occur for all components  Changes to properties of the following objects require an update to `revision`: 

  * nodeSelector
  * envs
  * imagePullSecrets
  * gcpProjectID
  * k8sClusterName
  * contractProvider
  * org

For more information, see [Rolling updates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/revision).  
`serviceAccountSecretProviderClass` | Advanced | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-env`, `apigee-org`, `apigee-telemetry` The name of the organization-specific secret provider class (`SecretProviderClass`) used for storing service account keys in Vault. See [Storing service account keys in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-vault).   
`tolerations.effect` | Advanced | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-env`, `apigee-ingress-manager`, `apigee-operator`, `apigee-org`, `apigee-redis`, `apigee-telemetry`, `apigee-virtualhost` Sets a global default for the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) across Apigee hybrid components. **Note:** Top-level `tolerations` is a global fallback, not an additive default. It is applied to a component only when that component's own `tolerations` property is not set; a component-level `tolerations` setting replaces the top-level value rather than being merged with it.`effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`tolerations.key` | Advanced | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-env`, `apigee-ingress-manager`, `apigee-operator`, `apigee-org`, `apigee-redis`, `apigee-telemetry`, `apigee-virtualhost` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`tolerations.operator` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `"Equal"` **Chart:** `apigee-datastore`, `apigee-env`, `apigee-ingress-manager`, `apigee-operator`, `apigee-org`, `apigee-redis`, `apigee-telemetry`, `apigee-virtualhost` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-env`, `apigee-ingress-manager`, `apigee-operator`, `apigee-org`, `apigee-redis`, `apigee-telemetry`, `apigee-virtualhost` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`tolerations.value` | Advanced | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-env`, `apigee-ingress-manager`, `apigee-operator`, `apigee-org`, `apigee-redis`, `apigee-telemetry`, `apigee-virtualhost` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `ao`

_Apigee Operators_ (AO) creates and updates low level Kubernetes and Istio resources that are required to deploy and maintain a component. For example, the controller carries out the release of message processors.

**Note:** In version 1.2.0, Apigee Operators replaces Apigee Deployment Admissionhook (ADAH) and Apigee Deployment Controller (ADC).

The following table describes the properties of the apigee-operators `ao` object:

Property | Type | Description  
---|---|---  
`ao.args.disableIstioConfigInAPIServer` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `true` **Chart:** `apigee-ingress-manager` Stops Apigee from supplying configuration to customer-installed Cloud Service Mesh. 

  * Set to `true` for hybrid installations using Apigee ingress gateway.
  * Set to `false` for hybrid installations using Cloud Service Mesh (Apigee hybrid versions 1.8 and earlier).

  
`ao.args.disableManagedClusterRoles` | Advanced | **Introduced in version:** 1.10.0 **Default value:** `true` **Chart:** `apigee-operator` When `true` (the default), Apigee hybrid does not manage Kubernetes `ClusterRole` and `ClursterRoleBinding` directly. If you have a process that requires managing these resources, the process must be performed by a user with the correct permissions to do so.   
`ao.image.pullPolicy` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `IfNotPresent` **Chart:** `apigee-operator`, `apigee-ingress-manager` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`ao.image.tag` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `1.16.11` **Chart:** `apigee-operator`, `apigee-ingress-manager` The version label for this service's Docker image.  
`ao.image.url` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-operator`, `apigee-ingress-manager` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`ao.resources.limits.cpu` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `250m` **Chart:** `apigee-operator`, `apigee-ingress-manager` The CPU limit for the resource in a Kubernetes container, in millicores.  
`ao.resources.limits.memory` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `256Mi` **Chart:** `apigee-operator`, `apigee-ingress-manager` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`ao.resources.requests.cpu` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `250m` **Chart:** `apigee-operator`, `apigee-ingress-manager` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`ao.resources.requests.memory` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `256Mi` **Chart:** `apigee-operator`, `apigee-ingress-manager` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
`ao.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ao.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ao.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ao.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ao.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `apigeeIngressGateway`

Configures the Apigee ingress gateway for Apigee Hybrid. Use `apigeeIngressGateway` properties to apply common configuration to all instances of the Apigee ingress gateway.

See `ingressGateways` to configure individual instances uniquely.

Apply changes to `apigeeIngressGateway` properties with the `apigee-org` chart.

The following table describes the properties of the `apigeeIngressGateway` object:

Property | Type | Description  
---|---|---  
`apigeeIngressGateway.image.pullPolicy` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `IfNotPresent` **Chart:** `apigee-org` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`apigeeIngressGateway.image.tag` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `1.16.11` **Chart:** `apigee-org` The version label for this service's Docker image.  
`apigeeIngressGateway.image.url` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`apigeeIngressGateway.nodeSelector.key` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` **Required** Node selector label key used to target dedicated Kubernetes nodes for ingress gateway services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`apigeeIngressGateway.nodeSelector.value` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` Optional node selector label value used to target dedicated Kubernetes nodes for ingress gateway services and override the `nodeSelector.apigeeData` settings. See nodeSelector.  
`apigeeIngressGateway.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The minimum number of Apigee ingress gateway pods that must stay available during a voluntary disruption, such as during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. To set a different budget for a specific gateway, use `ingressGateways[].podDisruptionBudget.minAvailable`. For example, in `overrides.yaml`:
    
    
    apigeeIngressGateway:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`apigeeIngressGateway.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The maximum number of Apigee ingress gateway pods that can be unavailable during a voluntary disruption, such as during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. To set a different budget for a specific gateway, use `ingressGateways[].podDisruptionBudget.maxUnavailable`. For example, in `overrides.yaml`:
    
    
    apigeeIngressGateway:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`apigeeIngressGateway.proxyProtocol.mode` | Advanced |  **Introduced in version:** 1.16.6 **Default value:** `disable` **Chart:** `apigee-org` Sets the global default for [HAProxy PROXY-protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) parsing on all ingress gateway components. Allowed values are `strict`, `permissive`, or `disable`. You can override this global default on a per-gateway basis using `ingressGateways[].proxyProtocol.mode`.  
`apigeeIngressGateway.replicaCountMax` | Basic | **Introduced in version:** 1.11.0 **Default value:** `4` **Chart:** `apigee-org` The maximum number of pods that hybrid can automatically add for the ingress gateway available for autoscaling.  
`apigeeIngressGateway.replicaCountMin` | Basic | **Introduced in version:** 1.11.0 **Default value:** `2` **Chart:** `apigee-org` The minimum number of pods for the ingress gateway available for autoscaling.  
`apigeeIngressGateway.targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.10.5, 1.11.2, 1.12.1 **Default value:** `75` **Chart:** `apigee-org` The threshold of CPU usage for scaling the number of pods in the ReplicaSet, as a percentage of total available CPU resources. When CPU usage goes above this value, then hybrid will gradually increase the number of pods in the ReplicaSet, up to `apigeeIngressGateway.replicaCountMax`. For more information on scaling in Kubernetes, see [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) in the Kubernetes documentation.   
`apigeeIngressGateway.tolerations.effect` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`apigeeIngressGateway.tolerations.key` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`apigeeIngressGateway.tolerations.operator` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `"Equal"` **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`apigeeIngressGateway.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`apigeeIngressGateway.tolerations.value` | Advanced | **Introduced in version:** 1.11.0 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `cassandra`

Defines the hybrid service that manages the runtime data repository. This repository stores application configurations, distributed quota counters, API keys, and OAuth tokens for applications running on the gateway.

For more information, see [StorageClass configuration](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-config).

The following table describes the properties of the `cassandra` object:

Property | Type | Description  
---|---|---  
`cassandra.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-datastore` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`cassandra.auth.admin.password` | Basic | **Introduced in version:** 1.0.0 **Default value:** `iloveapis123` **Chart:** `apigee-datastore` **Required** Password for the Cassandra administrator. The admin user is used for any administrative activities performed on the Cassandra cluster, such as backup and restore.  
`cassandra.auth.ddl.password` | Basic | **Introduced in version:** 1.0.0 **Default value:** `iloveapis123` **Chart:** `apigee-datastore` **Required** Password for the Cassandra Data Definition Language (DDL) user. Used by MART for any of the data definition tasks like keyspace creation, update, and deletion.  
`cassandra.auth.default.password` | Basic | **Introduced in version:** 1.0.0 **Default value:** `iloveapis123` **Chart:** `apigee-datastore` **Required** The password for the default Cassandra user created when Authentication is enabled. This password must be reset when configuring Cassandra authentication. See [Configuring TLS for Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls).  
`cassandra.auth.dml.password` | Basic | **Introduced in version:** 1.0.0 **Default value:** `iloveapis123` **Chart:** `apigee-datastore` **Required** Password for the Cassandra Data Manipulation Language (DML) user. The DML user is used by the client communication to read and write data to Cassandra.  
`cassandra.auth.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-datastore`, `apigee-org` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`cassandra.auth.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-datastore`, `apigee-org` The version label for this service's Docker image.  
`cassandra.auth.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-org` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`cassandra.auth.jmx.password` | Basic | **Introduced in version:** 1.4.0 **Default value:** `iloveapis123` **Chart:** `apigee-datastore` **Required** Password for the Cassandra JMX operations user. Used to authenticate and communicate with the Cassandra JMX interface.  
`cassandra.auth.jmx.username` | Basic | **Introduced in version:** 1.4.0 **Default value:** `jmxuser` **Chart:** `apigee-datastore` **Required** Username for the Cassandra JMX operations user. Used to authenticate and communicate with the Cassandra JMX interface.  
`cassandra.auth.jolokia.password` | Basic | **Introduced in version:** 1.4.0 **Default value:** `iloveapis123` **Chart:** `apigee-datastore` **Required** Password for the Cassandra Jolokia JMX operations user. Used to authenticate and communicate with the Cassandra JMX API.  
`cassandra.auth.jolokia.username` | Basic | **Introduced in version:** 1.4.0 **Default value:** `apigee` **Chart:** `apigee-datastore` **Required** Username for the Cassandra Jolokia JMX operations user. Used to authenticate and communicate with the Cassandra JMX API.  
`cassandra.auth.secret` | Basic | **Introduced in version:** 1.3.3 **Default value:** None **Chart:** `apigee-datastore` The name of the file stored in a Kubernetes secret that contains the Cassandra users and passwords. You can create the secret using following the following instructions: [Create the Secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls#create-the-secret).  See also:

  * [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/k8s-secrets)
  * [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the Kubernetes documentation
  * [ Creating a Secret Using kubectl](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret) in the Kubernetes documentation

  
`cassandra.auth.secretProviderClass` | Advanced | **Introduced in version:** 1.10.3 **Default value:** None **Chart:** `apigee-datastore`, `apigee-operator` The Cassandra secret storage policy. When set, it must match the SecretProviderClass which references the external secret provider, like Hashicorp Vault. When unset, Apigee hybrid uses either the usernames and passwords stored in: 

  * `cassandra.auth.admin.password`
  * `cassandra.auth.ddl.password`
  * `cassandra.auth.default.password`
  * `cassandra.auth.dml.password`
  * `cassandra.auth.jmx.password`
  * `cassandra.auth.jmx.username`
  * `cassandra.auth.jolokia.password`
  * `cassandra.auth.jolokia.username`

or the Kubernetes secret stored in:

  * `cassandra.auth.secret`

See [Storing Cassandra secrets in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-cassandra-secrets-in-vault) for instructions to create the policy.  
`cassandra.backup.cloudProvider` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `GCP` **Chart:** `apigee-datastore` The name of a backup provider. Supported values: `GCP`, `HYBRID`, and `CSI`. Set the value to: 

  * `GCP` to store backup archives on Google Cloud Storage.
  * `HYBRID` to store backup archives on a remote SSH server.
  * `CSI` (recommended) to utilize Kubernetes CSI [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) for backup. For information on `CSI` backup and restore for cloud platforms such as Google Cloud, AWS, and Azure, see [CSI backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-csi-backup-restore). 

  
`cassandra.backup.dbStorageBucket` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` **Required if backup is enabled and`cassandra.backup.cloudProvider` is set to `GCP`.** The name of an existing Google Cloud Storage bucket that will be used to store backup archives. See [ Creating buckets](https://cloud.google.com/storage/docs/creating-buckets) if you need to create one. **Note:** Starting in Hybrid version 1.13, the bucket name doesn't need to be prefixed with `gs://`. Support for this prefix has been deprecated and will be removed in future releases.   
`cassandra.backup.enabled` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `false` **Chart:** `apigee-datastore` Data backup is not enabled by default. To enable, set to `true`. See [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/backup-recovery).  
`cassandra.backup.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-datastore` **Helm only** : The email address of the `apigee-cassandra` Google IAM service account (GSA) to associate with the cassandra backup Kubernetes service account when enabling Workload Identity on GKE clusters. Set this when you have set `gcp.workloadIdentity.enabled` to `true` and `cassandra.backup.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-cassandra@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity Federation on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).  
`cassandra.backup.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-datastore` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`cassandra.backup.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-datastore` The version label for this service's Docker image.  
`cassandra.backup.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`cassandra.backup.keyfile` | Advanced | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-datastore` **Required if backup is enabled and`cassandra.backup.cloudProvider` is set to `HYBRID`.** The path on your local file system to the SSH private key file.  
`cassandra.backup.schedule` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `0 2 * * *` **Chart:** `apigee-datastore` The schedule for the backup cron job. See [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/backup-recovery). | `cassandra.backup.server` | Advanced | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-datastore` **Required if backup is enabled and`cassandra.backup.cloudProvider` is set to `HYBRID`.** The IP address of your remote SSH backup server.  
`cassandra.backup.serviceAccountPath` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` Path to a [Google Service Account](https://cloud.google.com/iam/docs/service-account-overview) key file that has the **Storage Object Admin** (`roles/storage.objectAdmin`) role. This Google Service Account will be used for uploading backup archives to a specified `cassandra.backup.dbStorageBucket`. **If backup is enabled and`cassandra.backup.cloudProvider` is set to `GCP`, one of the following is required to ensure Apigee Hybrid can access the Google Cloud Storage bucket to upload backup archives:**

  * Specified `cassandra.backup.serviceAccountPath`.
  * Specified `cassandra.backup.serviceAccountRef`.
  * Configured [Workload Identity for Apigee Hybrid in GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).
  * Configured [Workload Identity Federation for Apigee Hybrid in AKS or EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).

  
`cassandra.backup.serviceAccountRef` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-datastore` The name of an existing Kubernetes secret that stores the content of a [Google Service Account](https://cloud.google.com/iam/docs/service-account-overview) key file that has the **Storage Object Admin** (`roles/storage.objectAdmin`) role. This Google Service Account will be used for uploading backup archives to a specified `cassandra.backup.dbStorageBucket`.  **If backup is enabled and`cassandra.backup.cloudProvider` is set to `GCP`, one of the following is required to ensure Apigee Hybrid can access the Google Cloud Storage bucket to upload backup archives:**

  * Specified `cassandra.backup.serviceAccountPath`.
  * Specified `cassandra.backup.serviceAccountRef`.
  * Configured [Workload Identity for Apigee Hybrid in GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).
  * Configured [Workload Identity Federation for Apigee Hybrid in AKS or EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).

  
`cassandra.backup.storageDirectory` | Advanced | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-datastore` **Required if backup is enabled and`cassandra.backup.cloudProvider` is set to `HYBRID`.** **Can either be an absolute or relative path to the`apigee` user's home directory.** The name of the backup directory on your backup SSH server.  
`cassandra.clusterName` | Basic | **Introduced in version:** 1.0.0 **Default value:** `apigeecluster` **Chart:** `apigee-datastore` Specifies the name of the Cassandra cluster. **Note:** For multi-region installs the value of `clusterName` needs to match for all regions.  
`cassandra.datacenter` | Basic | **Introduced in version:** 1.0.0 **Default value:** `dc-1` **Chart:** `apigee-datastore` Specifies the datacenter of the Cassandra node.  
`cassandra.dnsPolicy` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-datastore` **Note:** In Apigee hybrid v1.3, this property is no longer supported. When you set `hostNetwork` to true, the DNS policy is set to `ClusterFirstWithHostNet` for you.   
`cassandra.externalSeedHost` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` Hostname or IP of a Cassandra cluster node. If not set, the Kubernetes local service is used.  
`cassandra.heapNewSize` | Basic | **Introduced in version:** 1.0.0 **Default value:** `100M` **Chart:** `apigee-datastore` The amount of JVM system memory allocated to newer objects, in megabytes.   
`cassandra.hostNetwork` | Basic | **Introduced in version:** 1.1.1 **Default value:** `false` **Chart:** `apigee-datastore` Enables the Kubernetes [`hostNetwork`](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#host-namespaces) feature. Apigee uses this feature in multi-region installations to communicate between pods if the pod network namespace does not have connectivity between clusters (the clusters are running in "island network mode"), which is the default case in non-GKE installations, including Google Distributed Cloud on VMware or bare metal, AKS, EKS, and OpenShift. Set `cassandra.hostNetwork` to `false` for single region installations and multi-region installations with connectivity between pods in different clusters, for example GKE installations. Set `cassandra.hostNetwork` to `true` for multi-region installations with no communication between between pods in different clusters, for example Google Distributed Cloud on VMware or bare metal, AKS, EKS, and OpenShift installations. See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites). When `true`, [DNS policy](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/#pod-s-dns-policy) is automatically set to `ClusterFirstWithHostNet`.  
`cassandra.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-datastore` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`cassandra.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-datastore` The version label for this service's Docker image.  
`cassandra.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`cassandra.maxHeapSize` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `512M` **Chart:** `apigee-datastore` The upper limit of JVM system memory available for Cassandra operations, in megabytes.   
`cassandra.multiRegionSeedHost` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` IP address of an existing Cassandra cluster used to expand the existing cluster to a new region. See [Configure the multi-region seed host](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#configure-the-multi-region-seed-host).   
`cassandra.nodeSelector.key` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` **Required** Node selector label key used to target dedicated Kubernetes nodes for `cassandra` data services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`cassandra.nodeSelector.value` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` Optional node selector label value used to target dedicated Kubernetes nodes for `cassandra` data services and override the `nodeSelector.apigeeData` settings. See nodeSelector.  
`cassandra.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-datastore` The minimum number of Cassandra pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    cassandra:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`cassandra.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-datastore` The maximum number of Cassandra pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    cassandra:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`cassandra.port` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `9042` **Chart:** `apigee-datastore` Port number used to connect to cassandra.  
`cassandra.rack` | Basic | **Introduced in version:** 1.0.0 **Default value:** `ra-1` **Chart:** `apigee-datastore` Specifies the rack of the Cassandra node.  
`cassandra.readinessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `2` **Chart:** `apigee-datastore` The number of times Kubernetes will verify that readiness probes have failed before marking the pod _unready_. The minimum value is 1.  
`cassandra.readinessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `0` **Chart:** `apigee-datastore` The number of seconds after a container is started before a readiness probe is initiated.  
`cassandra.readinessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `10` **Chart:** `apigee-datastore` Determines how often to perform a readiness probe, in seconds. The minimum value is 1.  
`cassandra.readinessProbe.successThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-datastore` The minimum consecutive successes needed for a readiness probe to be considered successful after a failure. The minimum value is 1.  
`cassandra.readinessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-datastore` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`cassandra.replicaCount` | Basic | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-datastore` Cassandra is a replicated database. This property specifies the number of Cassandra nodes employed as a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/). **Note:** The default value of `1` is only acceptable for demo or test installations. For production installations, the value of `replicaCount` must be a multiple of `3`. To determine your desired `replicaCount` value, consider the following: 

  * Estimate the traffic demands for your proxies.
  * Load test and make reasonable predictions of your CPU utilization.
  * You can specify different `replicaCount` values in different regions.
  * You can expand the `replicaCount` in the future in your overrides file.

  
`cassandra.resources.requests.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `500m` **Chart:** `apigee-datastore` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`cassandra.resources.requests.memory` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1Gi` **Chart:** `apigee-datastore` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
`cassandra.restore.cloudProvider` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `GCP` **Chart:** `apigee-datastore` The name of a restore provider. Supported values: `GCP`, `HYBRID`, and `CSI`. Set the value to: 

  * `GCP` to restore data from a backup stored on Google Cloud Storage.
  * `HYBRID` to restore data from a backup stored on a remote SSH server.
  * `CSI` (recommended) to utilize Kubernetes CSI [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) for restore. For information on `CSI` backup and restore for cloud platforms such as Google Cloud, AWS, and Azure, see [CSI backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-csi-backup-restore). 

  
`cassandra.restore.dbStorageBucket` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` **Required if restore is enabled and`cassandra.restore.cloudProvider` is set to `GCP`.** The name of a Google Cloud Storage bucket that stores backup archives to be used for data restoration. **Note:** Starting in Hybrid version 1.13, the bucket name doesn't need to be prefixed with `gs://`. Support for this prefix has been deprecated and will be removed in future releases.   
`cassandra.restore.enabled` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `false` **Chart:** `apigee-datastore`, `apigee-org` Data restoration is not enabled by default. To enable, set to `true`. See [Cassandra backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/backup-recovery).  
`cassandra.restore.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-datastore` **Helm only** : The email address of the `apigee-cassandra` Google IAM service account (GSA) to associate with the cassandra restore Kubernetes service account when enabling Workload Identity on GKE clusters. Set this when you have set `gcp.workloadIdentity.enabled` to `true` and `cassandra.restore.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-cassandra@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity Federationon GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).  
`cassandra.restore.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-datastore` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`cassandra.restore.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-datastore` The version label for this service's Docker image.  
`cassandra.restore.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`cassandra.restore.serviceAccountPath` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` Path to a [Google Service Account](https://cloud.google.com/iam/docs/service-account-overview) key file that has the **Storage Object Admin** (`roles/storage.objectAdmin`) role. This Google Service Account will be used to download backup archives from a specified `cassandra.restore.dbStorageBucket`. **If restore is enabled and`cassandra.restore.cloudProvider` is set to `GCP`, one of the following is required to ensure Apigee Hybrid can access the Google Cloud Storage bucket to download backup archives for restoration:**

  * Specified `cassandra.restore.serviceAccountPath`.
  * Specified `cassandra.restore.serviceAccountRef`.
  * Configured [Workload Identity for Apigee Hybrid in GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).
  * Configured [Workload Identity Federation for Apigee Hybrid in AKS or EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).

  
`cassandra.restore.serviceAccountRef` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-datastore` The name of an existing Kubernetes secret that stores the content of a [Google Service Account](https://cloud.google.com/iam/docs/service-account-overview) key file that has the **Storage Object Admin** (`roles/storage.objectAdmin`) role. This Google Service Account will be used to download backup archives from a specified `cassandra.restore.dbStorageBucket`. **If restore is enabled and`cassandra.restore.cloudProvider` is set to `GCP`, one of the following is required to ensure Apigee Hybrid can access the Google Cloud Storage bucket to download backup archives for restoration:**

  * Specified `cassandra.restore.serviceAccountPath`.
  * Specified `cassandra.restore.serviceAccountRef`.
  * Configured [Workload Identity for Apigee Hybrid in GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).
  * Configured [Workload Identity Federation for Apigee Hybrid in AKS or EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).

  
`cassandra.restore.snapshotTimestamp` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-datastore` **Required if restore is enabled.** Timestamp of the backup that should be restored.  
`cassandra.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-datastore` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`cassandra.storage.capacity` | Basic | **Introduced in version:** 1.0.0 **Default value:** `10Gi` **Chart:** `apigee-datastore` **Required if`storage.storageclass` is specified** Specifies the disk size required, in mebibytes (Mi) or gibibytes (Gi). **Note:** This #cassandra-storage-capacity property is deprecated starting from v1.12.0.Use `cassandra.storage.storageSize` instead.   
`cassandra.storage.storageclass` | Basic | **Introduced in version:** 1.0.0 **Default value:** None  **Chart:** `apigee-datastore` Specifies the class of on-prem storage being used.  
`cassandra.storage.storageSize` | Basic | **Introduced in version:** 1.0.0 **Default value:** `10Gi` **Chart:** `apigee-datastore` **Required if`storage.storageclass` is specified** Specifies the disk size required, in mebibytes (Mi) or gibibytes (Gi).  
`cassandra.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `300` **Chart:** `apigee-datastore` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately.  
`cassandra.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-datastore` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`cassandra.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-datastore` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`cassandra.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-datastore` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`cassandra.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-datastore` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`cassandra.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-datastore` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `certManager`

Apigee uses [cert-manager](https://cert-manager.io/) for certificate validation. 

The following table describes the properties of the `certManager` object:

Property | Type | Description  
---|---|---  
`certManager.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`certManager.namespace` | Advanced | **Introduced in version:** 1.9.0 **Default value:** `cert-manager` **Chart:** `apigee-operator` The namespace for [cert-manager](https://cert-manager.io/). See [Running cert-manager in a custom namespace](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cert-manager-custom-namespace).  
  
## `connectAgent`

Apigee Connect allows the Apigee hybrid management plane to connect securely to the MART service in the runtime plane without requiring you to expose the MART endpoint on the internet.

The following table describes the properties of the `connectAgent` object:

Property | Type | Description  
---|---|---  
`connectAgent.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-org` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`connectAgent.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-org` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`connectAgent.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-org` **Helm only** : The email address of the Google IAM service account (GSA) for connectAgent to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. **Note:** connectAgent uses the `apigee-mart` service account.GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-mart@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`connectAgent.logLevel` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `INFO` **Chart:** `apigee-org` The level of log reporting. Values can be:

  * `INFO`: Informational messages in addition to warning, error, and fatal messages. Most useful for debugging.
  * `WARNING`: Non-fatal warnings in addition to error and fatal messages.
  * `ERROR`: Internal errors and errors that are not returned to the user in addition to fatal messages.
  * `FATAL`: Unrecoverable errors and events that cause Apigee Connect to crash.

  
`connectAgent.image.pullPolicy` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `IfNotPresent` **Chart:** `apigee-org` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`connectAgent.image.tag` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `1.16.11` **Chart:** `apigee-org` The version label for this service's Docker image.  
`connectAgent.image.url` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`connectAgent.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The minimum number of Apigee Connect agent pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    connectAgent:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`connectAgent.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The maximum number of Apigee Connect agent pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    connectAgent:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`connectAgent.replicaCountMax` | Basic | **Introduced in version:** 1.2.0 **Default value:** `5` **Chart:** `apigee-org` Maximum number of replicas available for autoscaling.  
`connectAgent.replicaCountMin` | Basic | **Introduced in version:** 1.2.0 **Default value:** `1` **Chart:** `apigee-org` Minimum number of replicas available for autoscaling. In production, you may want to increase `replicaCountMin` to 1, to have a greater number of connections to the control plane for reliability and scalability.  
`connectAgent.resources.limits.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `512m` **Chart:** `apigee-org` The CPU limit for the resource in a Kubernetes container, in millicores.  
`connectAgent.resources.limits.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `512Mi` **Chart:** `apigee-org` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`connectAgent.resources.requests.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `100m` **Chart:** `apigee-org` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`connectAgent.resources.requests.memory` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `30Mi` **Chart:** `apigee-org` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
`connectAgent.server` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `apigeeconnect.googleapis.com:443` **Chart:** `apigee-org` The location of the server and port for this service.  
`connectAgent.serviceAccountPath` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-org` One of either `serviceAccountPath` or `serviceAccountRef` is required. Path to Google Service Account key file for the `apigee-mart` service account.  In most installations, the value of `connectAgent.serviceAccountPath` must match the value of `mart.serviceAccountPath`.   
`connectAgent.serviceAccountRef` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org` One of either `serviceAccountPath` or `serviceAccountRef` is required. A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).  In most installations, the value of `connectAgent.serviceAccountRef` must match the value of `mart.serviceAccountRef`.   
`connectAgent.targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `75` **Chart:** `apigee-org` Target CPU utilization for the Apigee Connect agent on the pod. The value of this field enables Apigee Connect to auto-scale when CPU utilization reaches this value, up to `replicaCountMax`.  
`connectAgent.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `600` **Chart:** `apigee-org` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately.  
`connectAgent.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`connectAgent.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`connectAgent.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`connectAgent.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`connectAgent.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `defaults`

The Default encryption keys for the Apigee hybrid installation.

**Note:** You need to update these for your installation.

The following table describes the properties of the `defaults` object:

Property | Type | Description  
---|---|---  
`defaults.org.kmsEncryptionKey` | Basic | **Introduced in version:** 1.0.0 **Default value:** `aWxvdmVhcGlzMTIzNDU2Nw==` **Chart:** `apigee-org`, `apigee-env` Default encryption key for the org in KMS.   
`defaults.org.kvmEncryptionKey` | Basic | **Introduced in version:** 1.0.0 **Default value:** `aWxvdmVhcGlzMTIzNDU2Nw==` **Chart:** `apigee-org`, `apigee-env` Default encryption key for the org in KVM.   
`defaults.env.kmsEncryptionKey` | Basic | **Introduced in version:** 1.0.0 **Default value:** `aWxvdmVhcGlzMTIzNDU2Nw==` **Chart:** `apigee-env` Default encryption key for the environment (env) in KMS.   
`defaults.env.kvmEncryptionKey` | Basic | **Introduced in version:** 1.0.0 **Default value:** `aWxvdmVhcGlzMTIzNDU2Nw==` **Chart:** `apigee-env` Default encryption key for the environment (env) in KVM.   
`defaults.env.cacheEncryptionKey` | Basic | **Introduced in version:** 1.0.0 **Default value:** `aWxvdmVhcGlzMTIzNDU2Nw==` **Chart:** `apigee-env` Default cache encryption key for the environment (env).   
  
## `envs`

Defines an array of environments to which you can deploy your API proxies. Each environment provides an isolated context or _sandbox_ for running API proxies.

Your hybrid-enabled organization must have at least one environment.

For more information, see [About environments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/environments-about).

The following table describes the properties of the `envs` object:

Property | Type | Description  
---|---|---  
`envs[].cacheEncryptionKey` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` One of either `cacheEncryptionKey`, `cacheEncryptionPath`, or `cacheEncryptionSecret` is required. A base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`envs[].cacheEncryptionPath` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` One of either `cacheEncryptionKey`, `cacheEncryptionPath`, or `cacheEncryptionSecret` is required. The path to a file containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`envs[].cacheEncryptionSecret.key` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` One of either `cacheEncryptionKey`, `cacheEncryptionPath`, or `cacheEncryptionSecret` is required. The key of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`envs[].cacheEncryptionSecret.name` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` One of either `cacheEncryptionKey`, or `cacheEncryptionPath`, or `cacheEncryptionSecret` is required. The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/) containing a base64-encoded encryption key. See [Data encryption](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/key-encryption).  
`envs[].components.runtime.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The minimum number of runtime pods in this environment that must stay available during a voluntary disruption, such as during a node pool upgrade or a node drain. Overrides `runtime.podDisruptionBudget.minAvailable`. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, this environment uses `runtime.podDisruptionBudget.minAvailable` or `runtime.podDisruptionBudget.maxUnavailable`; if neither of those is set, the Apigee operator applies its default of `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    envs:
      - name: test
        components:
          runtime:
            podDisruptionBudget:
              minAvailable: "50%"  
  
`envs[].components.runtime.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The maximum number of runtime pods in this environment that can be unavailable during a voluntary disruption, such as during a node pool upgrade or a node drain. Overrides `runtime.podDisruptionBudget.maxUnavailable`. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, this environment uses `runtime.podDisruptionBudget.minAvailable` or `runtime.podDisruptionBudget.maxUnavailable`; if neither of those is set, the Apigee operator applies its default of `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    envs:
      - name: test
        components:
          runtime:
            podDisruptionBudget:
              maxUnavailable: 1  
  
`envs[].components.runtime.replicaCountMax` | Basic | **Introduced in version:** 1.9.3 **Default value:** 4 **Chart:** `apigee-env` Maximum number of replicas for autoscaling. Overrides `runtime.replicaCountMax` if specified.  
`envs[].components.runtime.replicaCountMin` | Basic | **Introduced in version:** 1.9.3 **Default value:** 1 **Chart:** `apigee-env` Minimum number of replicas for autoscaling. Overrides `runtime.replicaCountMin` if specified.  
`envs[].components.runtime.resources.limits.memory` | Advanced | **Introduced in version:** 1.15.0 **Default value:** None **Chart:** `apigee-env` The memory limit for the resource in a Kubernetes container, in mebibytes (Mi) or gibibytes (Gi). **Important:** Setting this property for this environment causes Apigee not to use the values of: 

  * `runtime.resources.limits.memory`
  * `runtime.resources.requests.memory`

If you set this property, you must also set `envs[].components.runtime.resources.requests.memory` for this environment.  **Note:** If you are using message payloads larger than 10MB for this environment, you must make the following configuration changes: 

  * Increase the heap size to 4Gi.
  * Increase [`envs[].components.runtime.resources.limits.memory`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-components-runtime-resources-limits-memory) to 6Gi.
  * Increase [`envs[].components.runtime.resources.requests.memory`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-components-runtime-resources-requests-memory) to 4Gi.

See [Configure large message payload support in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support) for more details.   
`envs[].components.runtime.resources.requests.memory` | Advanced | **Introduced in version:** 1.15.0 **Default value:** None **Chart:** `apigee-env` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes (`Mi`) or Gibibytes (`Gi`). **Important:** Setting this property for this environment causes Apigee not to use the values of: 

  * `runtime.resources.limits.memory`
  * `runtime.resources.requests.memory`

If you set this property, you must also set `envs[].components.runtime.resources.limits.memory` for this environment.  **Note:** If you are using message payloads larger than 10MB for this environment, you must make the following configuration changes: 

  * Increase the heap size to 4Gi.
  * Increase `envs[].components.runtime.resources.limits.memory` to 6Gi.
  * Increase `envs[].components.runtime.resources.requests.memory` to 4Gi.

See [Configure large message payload support in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support) for more details.   
`envs[].components.synchronizer.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The minimum number of synchronizer pods in this environment that must stay available during a voluntary disruption, such as during a node pool upgrade or a node drain. Overrides `synchronizer.podDisruptionBudget.minAvailable`. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, this environment uses `synchronizer.podDisruptionBudget.minAvailable` or `synchronizer.podDisruptionBudget.maxUnavailable`; if neither of those is set, the Apigee operator applies its default of `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    envs:
      - name: test
        components:
          synchronizer:
            podDisruptionBudget:
              minAvailable: "50%"  
  
`envs[].components.synchronizer.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The maximum number of synchronizer pods in this environment that can be unavailable during a voluntary disruption, such as during a node pool upgrade or a node drain. Overrides `synchronizer.podDisruptionBudget.maxUnavailable`. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, this environment uses `synchronizer.podDisruptionBudget.minAvailable` or `synchronizer.podDisruptionBudget.maxUnavailable`; if neither of those is set, the Apigee operator applies its default of `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    envs:
      - name: test
        components:
          synchronizer:
            podDisruptionBudget:
              maxUnavailable: 1  
  
`envs[].components.synchronizer.replicaCountMax` | Basic | **Introduced in version:** 1.9.3 **Default value:** 4 **Chart:** `apigee-env` Maximum number of replicas for autoscaling. Overrides `synchronizer.replicaCountMax` if specified.  
`envs[].components.synchronizer.replicaCountMin` | Basic | **Introduced in version:** 1.9.3 **Default value:** 1 **Chart:** `apigee-env` Minimum number of replicas for autoscaling. Overrides `synchronizer.replicaCountMin` if specified.  
`envs[].gsa.runtime` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-env` **Helm only** : The email address of the runtime Google IAM service account to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts.  **Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`envs[].gsa.synchronizer` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-env` **Helm only** : The email address of the synchronizer Google IAM service account to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts.  **Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`envs[].httpProxy.host` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` Specifies the host name or IP address where the HTTP proxy is running. List `httpProxy` properties in the order `scheme`, `host`, `port`. For example:
    
    
    envs:
      - name: test
        httpProxy:
          scheme: HTTP
          host: 10.12.0.47
          port: 3128
          ...

See also: [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/forward-proxy).  
`envs[].httpProxy.port` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` Specifies the port on which the HTTP proxy is running. If this property is omitted, by default it uses port `80` for HTTP and port `443` for HTTPS.  
`envs[].httpProxy.scheme` | Basic | **Introduced in version:** 1.2.0 **Default value:** `HTTPS` **Chart:** `apigee-env` Specifies the type of the HTTP proxy as HTTP or HTTPS. By default, it uses `HTTPS`.  
`envs[].httpProxy.username` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` If the HTTP proxy requires basic authentication, then use this property to provide a username.  
`envs[].httpProxy.password` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` If the HTTP proxy requires basic authentication, then use this property to provide a password.  
`envs[].managementCallsSkipProxy` | Advanced | **Introduced in version:** 1.15.1 **Default value:** `false` **Chart:** `apigee-env` If set to `true` for environment-level forward proxy, trace and analytics (which use `googleapis.com`) will skip forward proxy. Targets in the proxy (including `googleapis.com`) will be routed via the forward proxy. This setting cannot be used in tandem with `useForRuntimeManagement`.  
`envs[].name` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` **Required** Apigee environment name to be synchronized.  
`envs[].pollInterval` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` Interval used for polling organization and environment synchronization changes, in seconds.  
`envs[].port` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` TCP port number for HTTPS traffic.  
`envs[].securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-env` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`envs[].serviceAccountPaths.runtime` | Basic | **Introduced in version:** 1.4.0 **Default value:** None **Chart:** `apigee-env` Path to file on local system to a Google Service Account key with the **Cloud Trace Agent** role, usually the `apigee-runtime` service account. See the [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref/) for the default names of the service accounts and their assigned roles.  
`envs[].serviceAccountPaths.synchronizer` | Basic | **Introduced in version:** 1.0 **Default value:** None **Chart:** `apigee-env` Path to file on local system to a Google Service Account key with the **Apigee Synchronizer Manager** role.  
`envs[].serviceAccountSecretProviderClass` | Advanced | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-env` The name of the environment-specific secret provider class (`SecretProviderClass`) used for storing service account keys in Vault. See [Storing service account keys in Hashicorp Vault](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-vault).   
`envs[].serviceAccountSecretRefs.runtime` | Basic | **Introduced in version:** 1.4.0 **Default value:** None **Chart:** `apigee-env` The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/). You must [create the secret](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret-using-kubectl) using a Google Service Account key with the **Cloud Trace Agent** role as its input.   
`envs[].serviceAccountSecretRefs.synchronizer` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/). You must [create the secret](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret-using-kubectl) using a Google Service Account key with the **Apigee Synchronizer Manager** role as its input.   
  
## `gcp`

Identifies the Google Cloud project ID (required for all hybrid installations), the Workload Identity and federated workload identity configurations, and the region where the `apigee-logger` and the `apigee-metrics` push their data.

The following table describes the properties of the `gcp` object:

Property | Type | Description  
---|---|---  
`gcp.federatedWorkloadIdentity.audience` | Basic | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` The allowed audience of the Workload Identity Provider on non-GKE platforms. Used when `gcp.federatedWorkloadIdentity.type` is `kubernetes`. See [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`gcp.federatedWorkloadIdentity.credentialSourceFile` | Basic | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` The filename and path to the credential source file used by Workload Identity Federation to obtain the credentials for the service accounts. This is the value you provide for `credential-source-file` when you configure Workload Identity Federation with the `create-cred-config` command. Used when `gcp.federatedWorkloadIdentity.type` is `kubernetes`. See [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`gcp.federatedWorkloadIdentity.enabled` | Basic | **Introduced in version:** 1.12.0 **Default value:** `false` **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` Enables Workload Identity Federation on non-GKE platforms. Must not be set `true` if `gcp.workloadIdentity.enabled` is set to `true` in the same cluster. See [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`gcp.federatedWorkloadIdentity.sidecarSpec.annotations` | Advanced | **Introduced in version:** 1.16.2 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` A map of annotations to apply to hybrid pods when `gcp.federatedWorkloadIdentity.type` is `sidecar`. These can be supplemented or overridden by component-level annotations such as `runtime.annotations`. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).  
`gcp.federatedWorkloadIdentity.sidecarSpec.container` | Advanced | **Introduced in version:** 1.16.2 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` A Kubernetes container specification map for the sidecar container, such as `image`, `imagePullPolicy`, `name`, etc. For more information, see the Kubernetes container documentation. You must provide your custom container image here. Required when `gcp.federatedWorkloadIdentity.type` is `sidecar`. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).  
`gcp.federatedWorkloadIdentity.sidecarSpec.container.env` | Advanced | **Introduced in version:** 1.16.2 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` A list of environment variables to set for the sidecar container. For more information, see the Kubernetes container documentation. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).  
`gcp.federatedWorkloadIdentity.sidecarSpec.container.startupProbe` | Advanced | **Introduced in version:** 1.16.2 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` Defines a Kubernetes startup probe for the sidecar container. For more information, see the Kubernetes container documentation. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).  
`gcp.federatedWorkloadIdentity.sidecarSpec.container.volumeMounts` | Advanced | **Introduced in version:** 1.16.2 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` A list of additional Kubernetes volume mounts for the sidecar container in hybrid pods when `gcp.federatedWorkloadIdentity.type` is `sidecar`. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).  
`gcp.federatedWorkloadIdentity.sidecarSpec.volumes` | Advanced | **Introduced in version:** 1.16.2 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` A list of additional Kubernetes volumes to be mounted to hybrid pods when `gcp.federatedWorkloadIdentity.type` is `sidecar`. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).  
`gcp.federatedWorkloadIdentity.tokenExpiration` | Basic | **Introduced in version:** 1.12.0 **Default value:** `3600` **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` The lifetime of the token in seconds. Used when `gcp.federatedWorkloadIdentity.type` is `kubernetes`. See [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-token-expiration).  
`gcp.federatedWorkloadIdentity.type` | Advanced | **Introduced in version:** 1.16.2 **Default value:** `kubernetes` **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` The method used for obtaining Workload Identity Federation tokens. Supported values are:

  * `kubernetes`: Use Kubernetes Projected Service Account Tokens. See [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).
  * `sidecar`: Use a sidecar container to fetch tokens from an Identity Provider. See [Use sidecar authentication for Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/use-sidecar-for-wif).

  
`gcp.projectID` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-operator`, `apigee-telemetry`, `apigee-org` **Required** Identifies the Google Cloud project where `apigee-logger` and the `apigee-metrics` push their data.  
`gcp.region` | Basic | **Introduced in version:** 1.2.0 **Default value:** `us-central1` **Chart:** `apigee-env`, `apigee-org` **Required** Identifies the Google Cloud [region](https://cloud.google.com/compute/docs/regions-zones#available) where the `apigee-logger` and the `apigee-metrics` push their data.  
`gcp.workloadIdentity.enabled` | Basic | **Introduced in version:** 1.10.0 **Default value:**`false` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` Enables using Workload Identity Federation for GKE. This allows workloads in your GKE clusters to impersonate Identity and Access Management (IAM) service accounts to access Google Cloud services. Must not be set `true` if `gcp.federatedWorkloadIdentity.enabled` is set to `true` in the same cluster. When `enabled` is `false`, the default, Apigee uses different service account authentication methods, like service account keys files, Kubernetes secrets, Vault, or Workload Identity Federation on other platforms. See [Service account authentication methods in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-authentication-methods). When `workloadIdentityEnabled` is `true`, Apigee uses Kubernetes service accounts and maps them to the appropriate IAM service accounts for each component. Specify the IAM service accounts to map to the Kubernetes service accounts with:

  * `gcp.workloadIdentity.gsa`
  * `connectAgent.gsa`
  * `envs.gsa.runtime`
  * `envs.gsa.synchronizer`
  * `envs.gsa.udca`
  * `logger.gsa`
  * `mart.gsa`
  * `metrics.gsa`
  * `mintTaskScheduler.gsa`
  * `udca.gsa`
  * `watcher.gsa`

  
`gcp.workloadIdentity.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-datastore`, `apigee-telemetry`, `apigee-org`, `apigee-env` The email address of the Google IAM service account (GSA) for all components to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. `gcp.workloadIdentity.gsa` applies to all hybrid components. If you specify a value for `gcp.workloadIdentity.gsa`, you do not need to provide a GSA for any individual hybrid components. If you do supply a GSA for an individual component, that component's GSA overrides `gcp.workloadIdentity.gsa` for that component only.  GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-non-prod@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [`Enabling Workload Identity on GKE`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke).  
  
## `guardrails`

Identifies the Google service account (GSA) and key file used by the Apigee Guardrails service. The Apigee Guardrails service allows the guardrails pod in the apigee-operator chart to check if required APIs are enabled in the project for successful installation of Apigee hybrid, as described in [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides) and [Installing and upgrading hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides).

The following table describes the properties of the `guardrails` object:

Property | Type | Description  
---|---|---  
`guardrails.image.pullPolicy` | Advanced | **Introduced in version:** 1.16.0 **Default value:** `IfNotPresent` **Chart:** `apigee-org` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`guardrails.image.tag` | Advanced | **Introduced in version:** 1.16.0 **Default value:** `1.16.11` **Chart:** `apigee-org` The version label for this service's Docker image.  
`guardrails.image.url` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-org` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`guardrails.gsa` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` The email address of the `apigee-guardrails` Google IAM service account (GSA) to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-guardrails@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`guardrails.serviceAccountPath` | Basic | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` **Unless using Workload Identity, one of either serviceAccountPath or serviceAccountRef is required.** Path to the Google service account key file with the [Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) role.   
`guardrails.serviceAccountRef` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` **Unless using Workload Identity, one of either serviceAccountPath or serviceAccountRef is required.** A kubernetes secret reference to a Google service account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`guardrails.tolerations.effect` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`guardrails.tolerations.key` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`guardrails.tolerations.operator` | Advanced | **Introduced in version:** 1.16.0 **Default value:** `"Equal"` **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`guardrails.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`guardrails.tolerations.value` | Advanced | **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `httpProxy`

`httpProxy` provides configuration parameters for an HTTP forward proxy server. When configured in `overrides.yaml`, all internet communication for the Apigee Connect, Logger, MART, Metrics, Synchronizer, and UDCA components pass through the proxy server. 

**Note:** You can also configure environment-scoped HTTP proxy forwarding for API proxies. See [Configure proxy forwarding for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/forward-proxy).

See also: connectAgent, logger, mart, metrics, and synchronizer. 

The following table describes the properties of the `httpProxy` object:

Property | Type | Description  
---|---|---  
`httpProxy.host` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` The hostname of the HTTP Proxy.  
`httpProxy.password` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` If the HTTP proxy requires basic authentication, then use this property to provide a password.  
`httpProxy.port` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` The port of the HTTP Proxy.  
`httpProxy.scheme` | Basic | **Introduced in version:** 1.1.1 **Default value:** `HTTPS` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` The scheme used by the proxy. Values can be **`HTTP`** or **`HTTPS`**. Values must be uppercase only.  
`httpProxy.useForRuntimeManagement` | Advanced | **Introduced in version:** 1.15.1 **Default value:** None **Chart:** `apigee-org` If `useForRuntimeManagement` is set to `true`, debug or analytics data are routed by runtime using this forward proxy. You can set this flag even if runtime has its own proxy setup for its environment. In that case, runtime's debug or analytics data will use the proxy shared at the org level, whereas backend/proxy traffic will continue to use the environment level proxy (this includes calls to googleapis.com as well).  
`httpProxy.username` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` If the HTTP proxy requires basic authentication, then use this property to provide a username.  
  
## `ingressGateways`

Configures each individual instance of the Apigee ingress gateway. Use these properties when you want to manage individual instances separately by `ingressGateways[].name`.

See `apigeeIngressGateway` to apply common configuration across all instances of the Apigee ingress gateway.

Apply changes to `ingressGateways` properties with the `apigee-org` chart.

The following table describes the properties of the `ingressGateways` object:

Property | Type | Description  
---|---|---  
`ingressGateways[].name` | Basic | **Introduced in version:** 1.8.0 **Default value:** None **Chart:** `apigee-org` **Required** The name of ingress gateway. Other services will use this name to address traffic to the gateway. The name must meet the following requirements:

  * have a maximum length of 17 characters
  * contain only lowercase alphanumeric characters, '-' or '.'
  * start with an alphanumeric character
  * end with an alphanumeric character

For more information, see [DNS Subdomain Names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) in the Kubernetes documentation.   
`ingressGateways[].podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The minimum number of pods for this ingress gateway that must stay available during a voluntary disruption, such as during a node pool upgrade or a node drain. Overrides `apigeeIngressGateway.podDisruptionBudget.minAvailable`. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, this gateway uses `apigeeIngressGateway.podDisruptionBudget.minAvailable` or `apigeeIngressGateway.podDisruptionBudget.maxUnavailable`; if neither of those is set, the Apigee operator applies its default of `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    ingressGateways:
      - name: my-gateway
        podDisruptionBudget:
          minAvailable: "50%"  
  
`ingressGateways[].podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The maximum number of pods for this ingress gateway that can be unavailable during a voluntary disruption, such as during a node pool upgrade or a node drain. Overrides `apigeeIngressGateway.podDisruptionBudget.maxUnavailable`. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, this gateway uses `apigeeIngressGateway.podDisruptionBudget.minAvailable` or `apigeeIngressGateway.podDisruptionBudget.maxUnavailable`; if neither of those is set, the Apigee operator applies its default of `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    ingressGateways:
      - name: my-gateway
        podDisruptionBudget:
          maxUnavailable: 1  
  
`ingressGateways[].proxyProtocol.mode` | Advanced |  **Introduced in version:** 1.16.6 **Default value:** `disable` **Chart:** `apigee-org` Opts in to [HAProxy PROXY-protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt) parsing on the ingress gateway component. Allowed values are `strict`, `permissive`, or `disable`. When set, this per-gateway value overrides the global default configured in `apigeeIngressGateway.proxyProtocol.mode`.  
`ingressGateways[].replicaCountMax` | Basic | **Introduced in version:** 1.8.0 **Default value:** `10` **Chart:** `apigee-org` The maximum number of pods that hybrid can automatically add for the ingress gateway available for autoscaling.  
`ingressGateways[].replicaCountMin` | Basic | **Introduced in version:** 1.8.0 **Default value:** `2` **Chart:** `apigee-org` The minimum number of pods for the ingress gateway available for autoscaling.  
`ingressGateways[].resources.limits.cpu` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `2000m` **Chart:** `apigee-org` The CPU limit for the resource, in millicores.  
`ingressGateways[].resources.limits.memory` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `1Gi` **Chart:** `apigee-org` The memory limit for the resource, in mebibytes.  
`ingressGateways[].resources.requests.cpu` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `300m` **Chart:** `apigee-org` The CPU needed for normal operation of the resource, in millicores.  
`ingressGateways[].resources.requests.memory` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `128Mi` **Chart:** `apigee-org` The memory needed for normal operation of the resource, in mebibytes.  
`ingressGateways[].securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-org` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`ingressGateways[].svcAnnotations` | Basic | **Introduced in version:** 1.8.0 **Default value:** None **Chart:** `apigee-org` Optional key/value map used to annotate the ingress gateway on platforms that support annotation. For example:
    
    
    ingressGateways:
      svcAnnotations:
        networking.gke.io/load-balancer-type: "Internal"  
  
`ingressGateways[].svcLoadBalancerIP` | Basic | **Introduced in version:** 1.8.0 **Default value:** None **Chart:** `apigee-org` On platforms that support specifying the load balancer IP address, the load balancer will be created with this IP address. On platforms that do not allow you to specify the load balancer IP address, this property is ignored.  
`ingressGateways[].svcType` | Basic | **Introduced in version:** 1.8.1 **Default value:** LoadBalancer **Chart:** `apigee-org` Used to change the type of the default k8s service for ingress deployment. Set the value to `ClusterIP` if you want to disable creation of default load balancer. Possible values:

  * `ClusterIP`
  * `LoadBalancer`

  
`ingressGateways[].targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.10.5, 1.11.2, 1.12.1 **Default value:** `75` **Chart:** `apigee-org` The threshold of CPU usage for scaling the number of pods in the ReplicaSet, as a percentage of total available CPU resources. When CPU usage goes above this value, then hybrid will gradually increase the number of pods in the ReplicaSet, up to `ingressGateways[].replicaCountMax`. For more information on scaling in Kubernetes, see [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) in the Kubernetes documentation.   
`ingressGateways[].tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ingressGateways[].tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ingressGateways[].tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-operator` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ingressGateways[].tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`ingressGateways[].tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-operator` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `istiod`

Configures the Apigee ingress.

The following table describes the properties of the `istiod` object:

Property | Type | Description  
---|---|---  
`istiod.accessLogFile` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `/dev/stdout` **Chart:** `apigee-ingress-manager` The file address for the ingress access log, for example `/dev/stdout`. Leaving this value undefined disables access logging.  
`istiod.accessLogFormat` | Advanced | **Introduced in version:** 1.8.0 **Chart:** `apigee-ingress-manager` The format for the ingress access log.  Leaving this value undefined results in using the proxy's default access log format. **Default access log format:**
    
    
    '{"start_time":"%START_TIME%","remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%","user_agent":"%REQ(USER-AGENT)%","host":"%REQ(:AUTHORITY)%","request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%","request_time":"%DURATION%","status":"%RESPONSE_CODE%","status_details":"%RESPONSE_CODE_DETAILS%","bytes_received":"%BYTES_RECEIVED%","bytes_sent":"%BYTES_SENT%","upstream_address":"%UPSTREAM_HOST%","upstream_response_flags":"%RESPONSE_FLAGS%","upstream_response_time":"%RESPONSE_DURATION%","upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%","upstream_cluster":"%UPSTREAM_CLUSTER%","x_forwarded_for":"%REQ(X-FORWARDED-FOR)%","request_method":"%REQ(:METHOD)%","request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%","request_protocol":"%PROTOCOL%","tls_protocol":"%DOWNSTREAM_TLS_VERSION%","request_id":"%REQ(X-REQUEST-ID)%","sni_host":"%REQUESTED_SERVER_NAME%","apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'

The following is a copy of the default access log format with line breaks added for readability. 
    
    
    '{"start_time":"%START_TIME%",
      "remote_address":"%DOWNSTREAM_DIRECT_REMOTE_ADDRESS%",
      "user_agent":"%REQ(USER-AGENT)%",
      "host":"%REQ(:AUTHORITY)%",
      "request":"%REQ(:METHOD)% %REQ(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%",
      "request_time":"%DURATION%",
      "status":"%RESPONSE_CODE%",
      "status_details":"%RESPONSE_CODE_DETAILS%",
      "bytes_received":"%BYTES_RECEIVED%",
      "bytes_sent":"%BYTES_SENT%",
      "upstream_address":"%UPSTREAM_HOST%",
      "upstream_response_flags":"%RESPONSE_FLAGS%",
      "upstream_response_time":"%RESPONSE_DURATION%",
      "upstream_service_time":"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%",
      "upstream_cluster":"%UPSTREAM_CLUSTER%",
      "x_forwarded_for":"%REQ(X-FORWARDED-FOR)%",
      "request_method":"%REQ(:METHOD)%",
      "request_path":"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%",
      "request_protocol":"%PROTOCOL%",
      "tls_protocol":"%DOWNSTREAM_TLS_VERSION%",
      "request_id":"%REQ(X-REQUEST-ID)%",
      "sni_host":"%REQUESTED_SERVER_NAME%",
      "apigee_dynamic_data":"%DYNAMIC_METADATA(envoy.lua)%"}'  
  
`istiod.forwardClientCertDetails` | Advanced | **Introduced in version:** 1.9.2 **Default value:** `SANITIZE_SET` **Chart:** `apigee-ingress-manager` Determines how the Envoy proxy (for the Apigee ingress gateway) handles the `x-forwarded-client-cert` (XFCC) HTTP header.  Possible values are:

  * `SANITIZE_SET` (default) When the client connection is mTLS, reset the XFCC header with the client certificate information and send it to the next hop.
  * `FORWARD_ONLY` When the client connection is mTLS (Mutual TLS), forward the XFCC header in the request only.
  * `APPEND_FORWARD` When the client connection is mTLS, append the client certificate information to the request's XFCC header and forward it.
  * `SANITIZE` Do not forward the XFCC header.
  * `ALWAYS_FORWARD_ONLY` Always forward the XFCC header in the request, regardless of whether the client connection is mTLS.

For more information on these values, see the Envoy documentation for [Enum extensions.filters.network.http_connection_manager.v3.HttpConnectionManager.ForwardClientCertDetails](https://www.envoyproxy.io/docs/envoy/v1.26.1/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto.html#enum-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-forwardclientcertdetails). If you change this setting after installing Hybrid, apply it with `apigeectl init` and then restart your Apigee ingress gateway pods.  
`istiod.healthCheckUserAgents` | Advanced | **Introduced in version:** 1.12.0 **Default values:**
    
    
    - "GoogleStackdriverMonitoring-UptimeChecks(https://cloud.google.com/monitoring)"
    - "Edge Health Probe"

**Chart:** `apigee-ingress-manager` Enables non-Google Cloud loadbalancers to check the ingress gateway's health check endpoints (`/healthz/ingress` and `/healthz`) by overriding the default user-agent allow list in hybrid. **Note** : Usage of this configuration property is only supported in hybrid installations using Helm charts. It is not supported for use with `apigeectl`.To override the default user agents specified, use the following syntax, inserting the custom user agents: 
    
    
    istiod:
      healthCheckUserAgents:
      - "CUSTOM_USER_AGENT_1"
      - "CUSTOM_USER_AGENT_2"

To remove the user agent requirement, use the following: 
    
    
    istiod:
      healthCheckUserAgents: []

**Note** : The pods must be restarted for this to take effect. Use `kubectl rollout restart deployment -n apigee apigee-ingressgateway-manager` to restart the pods and `kubectl rollout status deployment -n apigee apigee-ingressgateway-manager` to check the status of the rollout.  
`istiod.image.pullPolicy` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `IfNotPresent` **Chart:** `apigee-ingress-manager` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`istiod.image.tag` | Advanced | **Introduced in version:** 1.8.0 **Default value:** `1.16.11` **Chart:** `apigee-ingress-manager` The version label for this service's Docker image.  
`istiod.image.url` | Advanced | **Introduced in version:** 1.8.0 **Default value:** None **Chart:** `apigee-ingress-manager` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`istiod.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-ingress-manager` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`istiod.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-ingress-manager` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`istiod.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-ingress-manager` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`istiod.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-ingress-manager` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`istiod.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-ingress-manager` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `k8sCluster`

Identifies Kubernetes cluster where the hybrid runtime is installed.

The following table describes the properties of the `k8sCluster` object:

Property | Type | Description  
---|---|---  
`k8sCluster.name` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-telemetry`, `apigee-org` The name of the Kubernetes cluster where the hybrid runtime is installed.  
`k8sCluster.region` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-telemetry`, `apigee-org` Identifies the Google Cloud [region](https://cloud.google.com/compute/docs/regions-zones#available) in which your Kubernetes cluster was created.  
  
## `kubeRBACProxy`

Identifies where Apigee should look for Kubernetes role-based access controls.

The following table describes the properties of the `kubeRBACProxy` object:

Property | Type | Description  
---|---|---  
`kubeRBACProxy.image.pullPolicy` | Advanced | **Introduced in version:** 1.2.0 **Default value:** `IfNotPresent` **Chart:** `apigee-operator`, `apigee-ingress-manager` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`kubeRBACProxy.image.tag` | Advanced | **Introduced in version:** `1.2.0` **Default value:** `1.16.11` **Chart:** `apigee-operator`, `apigee-ingress-manager` The version label for this service's Docker image.  
`kubeRBACProxy.image.url` | Advanced | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-operator`, `apigee-ingress-manager` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`kubeRBACProxy.resources.limits.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `500m` **Chart:** `apigee-operator`, `apigee-ingress-manager` The CPU limit for the resource in a Kubernetes container, in millicores.  
`kubeRBACProxy.resources.limits.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `128Mi` **Chart:** `apigee-operator`, `apigee-ingress-manager` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`kubeRBACProxy.resources.requests.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `5m` **Chart:** `apigee-operator`, `apigee-ingress-manager` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`kubeRBACProxy.resources.requests.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `64Mi` **Chart:** `apigee-operator`, `apigee-ingress-manager` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
  
## `logger`

Defines the service that manages operational logs. All of the Apigee hybrid services that run in your Kubernetes cluster output this information.

For more information, see [Logging overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/logging).

The following table describes the properties of the `logger` object:

Property | Type | Description  
---|---|---  
`logger.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-telemetry` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`logger.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-telemetry` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`logger.bufferChunkSize` | Advanced | **Introduced in version:** 1.12.0 **Default value:** 256k **Chart:** `apigee-telemetry` The initial buffer size to read log files.  
`logger.bufferMaxSize` | Advanced | **Introduced in version:** 1.12.0 **Default value:** 104857600 **Chart:** `apigee-telemetry` The limit of the buffer size per monitored file. Files exceeding this limit are removed from the monitored file list.  
`logger.bufferMemoryLimit` | Advanced | **Introduced in version:** 1.12.0 **Default value:** 150MB **Chart:** `apigee-telemetry` The limit of memory that logger can consumed. If reach, the logger will momentarily pause reading more data until the existing data is flushed in memory.  
`logger.enabled` | Basic | **Introduced in version:** 1.0.0 **Default value:** `false` **Chart:** `apigee-telemetry` Enables or disables logging on the cluster. For non-GKE set to `true`, for GKE on Google Cloud or Google Distributed Cloudset to `false`.  
`logger.envVars` | Basic | **Introduced in version:** 1.8.5 **Default value:** None **Chart:** `apigee-telemetry` Allows you to include the `NO_PROXY` Fluent Bit environment variable, which specifies URLs for which traffic is not routed through the HTTP proxy. The `NO_PROXY` variable should be defined as a comma-separated string of host names, in the format:
    
    
    logger:
      ...
      envVars:
        NO_PROXY: '_< comma-separated-values>_'

for example: 
    
    
      envVars:
        NO_PROXY: 'kubernetes.default.svc,oauth2.googleapis.com,logging.googleapis.com'

Use `envVars: NO_PROXY` optionally when you have HTTP forward proxy enabled. See [NO_PROXY](https://docs.fluentbit.io/manual/administration/http-proxy#no_proxy) in the Fluent Bit documentation.  
`logger.flushInterval` | Advanced | **Introduced in version:** 1.12.0 **Default value:** 1 **Chart:** `apigee-telemetry` The interval to wait before invoking the next buffer flushed, in seconds.  
`logger.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-telemetry` **Helm only** : The email address of the `apigee-logger` Google IAM service account (GSA) to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-logger@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`logger.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-telemetry` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`logger.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-telemetry` The version label for this service's Docker image.  
`logger.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`logger.livenessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `3` **Chart:** `apigee-telemetry` The number of times Kubernetes will verify that liveness probes have failed before restarting the container. The minimum value is 1.  
`logger.livenessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `0` **Chart:** `apigee-telemetry` The number of seconds after a container is started before a liveness probe is initiated.  
`logger.livenessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `60` **Chart:** `apigee-telemetry` Determines how often to perform a liveness probe, in seconds. The minimum value is 1.  
`logger.livenessProbe.successThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-telemetry` The minimum consecutive successes needed for a liveness probe to be considered successful after a failure. The minimum value is 1.  
`logger.livenessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-telemetry` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`logger.nodeSelector.key` | Basic | **Introduced in version:** 1.0.0 **Default value:** `apigee.cloud.google.com/apigee-logger-enabled` **Chart:** `apigee-telemetry` **Required** Node selector label key used to target dedicated Kubernetes nodes for `logger` runtime services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`logger.nodeSelector.value` | Basic | **Introduced in version:** 1.0.0 **Default value:** `true` **Chart:** `apigee-telemetry` **Required** Node selector label value used to target dedicated Kubernetes nodes for `logger` runtime services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`logger.resources.limits.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `200m` **Chart:** `apigee-telemetry` The CPU limit for the resource in a Kubernetes container, in millicores.  
`logger.resources.limits.memory` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `500Mi` **Chart:** `apigee-telemetry` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`logger.resources.requests.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `100m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`logger.resources.requests.memory` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `250Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
`logger.serviceAccountPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` One of either `serviceAccountPath` or `serviceAccountRef` is required. Path to Google Service Account key file with **Logs Writer** role.   
`logger.serviceAccountRef` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-telemetry` One of either `serviceAccountPath` or `serviceAccountRef` is required. A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`logger.storageMaxChunks` | Advanced | **Introduced in version:** 1.12.0 **Default value:** 128 **Chart:** `apigee-telemetry` The maximum number of chunks that can be up in memory. Chunks exceeding the limit will be saved in the file system.  
`logger.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `30` **Chart:** `apigee-telemetry` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately.  
`logger.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`logger.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`logger.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-telemetry` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`logger.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`logger.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `mart`

Defines the MART (Management API for RunTime data) service, which acts as an API provider for public Apigee APIs so that you can access and manage runtime data entities such as KMS (API Keys and OAuth tokens), KVM, Quota, and API products.

The following table describes the properties of the `mart` object:

Property | Type | Description  
---|---|---  
`mart.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-org` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`mart.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-org` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`mart.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-org` **Helm only** : The email address of the `apigee-mart` Google IAM service account (GSA) to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-mart@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federated).  
`mart.hostAlias` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-org` The host alias pointing to the MART object. You can set this property to `*` or a fully-qualified domain name.  
`mart.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-org`, `apigee-env` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`mart.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-org`, `apigee-env` The version label for this service's Docker image.  
`mart.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-org`, `apigee-env` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`mart.initCheckCF.resources.requests.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `10m` **Chart:** `apigee-org` The amount of CPU resources allocated to the initialization check of the Cloud Foundry process.  
`mart.livenessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `12` **Chart:** `apigee-org` The number of times Kubernetes will verify that liveness probes have failed before restarting the container. The minimum value is 1.  
`mart.livenessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `15` **Chart:** `apigee-org` The number of seconds after a container is started before a liveness probe is initiated.  
`mart.livenessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-org` Determines how often to perform a liveness probe, in seconds. The minimum value is 1.  
`mart.livenessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-org` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`mart.metricsURL` | Basic | **Introduced in version:** 1.0.0 **Default value:** `/v1/server/metrics` **Chart:** `apigee-org`  
`mart.nodeSelector.key` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-org` Optional node selector label key for targeting Kubernetes nodes for `mart` runtime services. If you do not specify a key for mart.nodeselector, then your runtime uses the node specified in the nodeSelector object. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`mart.nodeSelector.value` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-org` Optional node selector label value for targeting Kubernetes nodes for `mart` runtime services. See also the nodeSelector object. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`mart.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The minimum number of MART pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    mart:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`mart.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The maximum number of MART pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    mart:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`mart.readinessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `2` **Chart:** `apigee-org` The number of times Kubernetes will verify that readiness probes have failed before marking the pod _unready_. The minimum value is 1.  
`mart.readinessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `15` **Chart:** `apigee-org` The number of seconds after a container is started before a readiness probe is initiated.  
`mart.readinessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-org` Determines how often to perform a readiness probe, in seconds. The minimum value is 1.  
`mart.readinessProbe.successThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-org` The minimum consecutive successes needed for a readiness probe to be considered successful after a failure. The minimum value is 1.  
`mart.readinessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-org` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`mart.replicaCountMax` | Basic | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-org` Maximum number of replicas available for autoscaling.  
`mart.replicaCountMin` | Basic | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-org` Minimum number of replicas available for autoscaling.  
`mart.resources.limits.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `2000m` **Chart:** `apigee-org` The CPU limit for the resource in a Kubernetes container, in millicores.  
`mart.resources.limits.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `5Gi` **Chart:** `apigee-org` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`mart.resources.requests.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `500m` **Chart:** `apigee-org` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`mart.resources.requests.memory` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `512Mi` **Chart:** `apigee-org` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
`mart.serviceAccountPath` | Basic | **Introduced in version:** 1.1.1 **Default value:** None **Chart:** `apigee-org` One of either `serviceAccountPath` or `serviceAccountRef` is required. Path to Google Service Account key file with **no role**.   
`mart.serviceAccountRef` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org` One of either `serviceAccountPath` or `serviceAccountRef` is required. A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`mart.sslCertPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-org` Either `sslCertPath`/`sslKeyPath` or `sslSecret` is required. Local file system path for loading and encoding the SSL cert to a Secret.  
`mart.sslKeyPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-org` **Either`sslCertPath`/`sslKeyPath` or `sslSecret` is required**. Local file system path for loading and encoding the SSL key to a Secret.  
`mart.sslSecret` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-org` Either `sslCertPath`/`sslKeyPath` or `sslSecret` is required. The name of a file stored in a Kubernetes secret that contains the TLS certificate and private key. You must create the secret using the TLS certificate and key data as its input. See also:

  * [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/k8s-secrets)
  * [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the Kubernetes documentation
  * [ Creating a Secret Using kubectl](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret-using-kubectl) in the Kubernetes documentation

  
`mart.targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `75` **Chart:** `apigee-org` Target CPU utilization for the MART process on the pod. The value of this field enables MART to auto-scale when CPU utilization reaches this value, up to `replicaCountMax`.  
`mart.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `30` **Chart:** `apigee-org` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately.  
`mart.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mart.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mart.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mart.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mart.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `metrics`

Defines the service that collects operations metrics. You can use metrics data to monitor the health of Hybrid services, to set up alerts, and so on.

For more information, see [Metrics collection overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/metrics-collection).

The following table describes the properties of the `metrics` object:

Property | Type | Description  
---|---|---  
`metrics.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-telemetry` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`metrics.adapter.image.pullPolicy` | Advanced | **Introduced in version:** 1.8.1 **Default value:** `IfNotPresent` **Chart:** `apigee-telemetry` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`metrics.adapter.image.tag` | Advanced | **Introduced in version:** 1.8.1 **Default value:** `1.16.11` **Chart:** `apigee-telemetry` The version label for this service's Docker image.  
`metrics.adapter.image.url` | Advanced | **Introduced in version:** 1.8.1 **Default value:** None **Chart:** `apigee-telemetry` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`metrics.adapter.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The minimum number of metrics adapter pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    metrics:
      adapter:
        podDisruptionBudget:
          minAvailable: "50%"  
  
`metrics.adapter.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The maximum number of metrics adapter pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    metrics:
      adapter:
        podDisruptionBudget:
          maxUnavailable: 1  
  
`metrics.adapter.resources.limits.cpu` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the adapter resource in a Kubernetes container, in millicores.   
`metrics.adapter.resources.limits.memory` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `4Gi` **Chart:** `apigee-telemetry` The memory limit for the adapter resource in a Kubernetes container, in gibibytes.   
`metrics.adapter.resources.requests.cpu` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `100m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the adapter in a Kubernetes container, in millicores.   
`metrics.adapter.resources.requests.memory` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `128Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the adapter in a Kubernetes container, in mebibytes.   
`metrics.aggregator.resources.requests.cpu` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the aggregator in a Kubernetes container, in millicores.   
`metrics.aggregator.resources.requests.memory` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the aggregator in a Kubernetes container, in mebibytes.   
`metrics.aggregator.resources.limits.cpu` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the aggregator resource in a Kubernetes container, in millicores.   
`metrics.aggregator.resources.limits.memory` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `3Gi` **Chart:** `apigee-telemetry` The memory limit for the aggregator resource in a Kubernetes container, in gibibytes.   
`metrics.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-telemetry` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`metrics.app.resources.requests.cpu` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the app in a Kubernetes container, in millicores.   
`metrics.app.resources.requests.memory` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the app in a Kubernetes container, in mebibytes.   
`metrics.app.resources.limits.cpu` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the app resource in a Kubernetes container, in millicores.   
`metrics.app.resources.limits.memory` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `1Gi` **Chart:** `apigee-telemetry` The memory limit for the app resource in a Kubernetes container, in gibibytes.   
`metrics.appStackdriverExporter.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The minimum number of `appStackdriverExporter` pods that must stay available during a voluntary disruption, such as during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    metrics:
      appStackdriverExporter:
        podDisruptionBudget:
          minAvailable: "50%"  
  
`metrics.appStackdriverExporter.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The maximum number of `appStackdriverExporter` pods that can be unavailable during a voluntary disruption, such as during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    metrics:
      appStackdriverExporter:
        podDisruptionBudget:
          maxUnavailable: 1  
  
`metrics.appStackdriverExporter.resources.limits.cpu` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the stackdriverExporter resource in a Kubernetes container, in millicores.   
`metrics.appStackdriverExporter.resources.limits.memory` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `1Gi` **Chart:** `apigee-telemetry` The memory limit for the stackdriverExporter resource in a Kubernetes container, in gibibytes.   
`metrics.appStackdriverExporter.resources.requests.cpu` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `128m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the stackdriverExporter in a Kubernetes container, in millicores.   
`metrics.appStackdriverExporter.resources.requests.memory` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the stackdriverExporter in a Kubernetes container, in mebibytes.   
`metrics.collector.envVars` | Basic | **Introduced in version:** 1.13 **Default value:** None **Chart:** `apigee-telemetry` Allows you to pass in and override environment variables in OpenTelemetry. For example, you can define `HTTP_PROXY`, `HTTPS_PROXY`, or `NO_PROXY` to have its requests pass through the proxy server. The `HTTP_PROXY` variable can be defined as a string containing the host name, in the format: 
    
    
    metrics:
    ...
      envVars:
        HTTP_PROXY: '_< host-name>_'

for example: 
    
    
      envVars:
        HTTP_PROXY: 'http://1.1.1.1:80'

The `HTTPS_PROXY` variable can be defined as a string containing the host name, in the format: 
    
    
    metrics:
    ...
      envVars:
        HTTPS_PROXY: '_< host-name>_'

for example: 
    
    
      envVars:
        HTTPS_PROXY: 'https://1.1.1.1:80'

The `NO_PROXY` variable should be defined as a comma-separated string of host names, in the format: 
    
    
    metrics:
    ...
    envVars:
      NO_PROXY: '_< comma-separated-values>_'

for example: 
    
    
    envVars:
      NO_PROXY: 'https://1.1.1.1:80, https://1.1.1.1:81'

Use `envVars: HTTP_PROXY`, `envVars: HTTPS_PROXY`, or `envVars: NO_PROXY` optionally when you have HTTP forward proxy enabled. See [Proxy support](https://opentelemetry.io/docs/collector/configuration/#proxy-support) in the OpenTelemetry documentation.  
`metrics.collector.imagePullPolicy` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `IfNotPresent` **Chart:** `apigee-telemetry` Determines when kubelet pulls the pod's Docker image. Possible values include: 

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Use a private image repository with Apigee hybrid ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/container-images).  
`metrics.collector.image.tag` | Basic | **Introduced in version:** 1.12.0 **Default value:** `1.16.11` **Chart:** `apigee-telemetry` The version label for this service's Docker image.  
`metrics.collector.image.url` | Basic | **Introduced in version:** 1.12.0 **Default value:** None **Chart:** `apigee-telemetry` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`metrics.collector.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The minimum number of metrics collector pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods. Because the collector runs as a DaemonSet, that default sets `minAvailable` to 80% of the collector pods (rounded down) instead of using `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    metrics:
      collector:
        podDisruptionBudget:
          minAvailable: "50%"  
  
`metrics.collector.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The maximum number of metrics collector pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods. Because the collector runs as a DaemonSet, that default sets `minAvailable` to 80% of the collector pods (rounded down) instead of using `maxUnavailable: 1`. For example, in `overrides.yaml`:
    
    
    metrics:
      collector:
        podDisruptionBudget:
          maxUnavailable: 1  
  
`metrics.collector.resources.requests.cpu` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the app in a Kubernetes container, in millicores.  
`metrics.collector.resources.requests.memory` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the app in a Kubernetes container, in mebibytes.  
`metrics.collector.resources.limits.cpu` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the app resource in a Kubernetes container, in millicores.  
`metrics.collector.resources.limits.memory` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `1Gi` **Chart:** `apigee-telemetry` The memory limit for the app resource in a Kubernetes container, in gibibytes.  
`metrics.collector.livenessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `5` **Chart:** `apigee-telemetry` The number of times Kubernetes will verify that liveness probes have failed before restarting the container. The minimum value is 1.  
`metrics.collector.livenessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `30` **Chart:** `apigee-telemetry` The number of seconds after a container is started before a liveness probe is initiated.  
`metrics.collector.livenessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `10` **Chart:** `apigee-telemetry` Determines how often to perform a liveness probe, in seconds. The minimum value is 1.  
`metrics.collector.livenessProbe.successThreshold` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `1` **Chart:** `apigee-telemetry` The minimum consecutive successes needed for a liveness probe to be considered successful after a failure. The minimum value is 1.  
`metrics.collector.livenessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `5` **Chart:** `apigee-telemetry` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`metrics.collector.readinessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `3` **Chart:** `apigee-telemetry` The number of times Kubernetes will verify that readiness probes have failed before marking the pod unready. The minimum value is 1.  
`metrics.collector.readinessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `30` **Chart:** `apigee-telemetry` The number of seconds after a container is started before a readiness probe is initiated.  
`metrics.collector.readinessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `10` **Chart:** `apigee-telemetry` Determines how often to perform a readiness probe, in seconds. The minimum value is 1.  
`metrics.collector.readinessProbe.successThreshold` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `1` **Chart:** `apigee-telemetry` The minimum consecutive successes needed for a readiness probe to be considered successful after a failure. The minimum value is 1.  
`metrics.collector.readinessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.12.0 **Default value:** `5` **Chart:** `apigee-telemetry` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`metrics.disablePrometheusPipeline` | Basic | **Introduced in version:** 1.12.0 **Default value:** `true` **Chart:** `apigee-telemetry` Metrics for `ProxyV2` and `TargetV2` monitored resources are not emitted when set to `true`. Use metrics for `Proxy` and `Target` monitored resources instead.  
`metrics.enabled` | Basic | **Introduced in version:** 1.0.0 **Default value:** `true` **Chart:** `apigee-telemetry` Enables Apigee metrics. Set to `true` to enable metrics. Set to `false` to disable metrics.   
`metrics.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-telemetry` **Helm only** : The email address of the `apigee-metrics` Google IAM service account (GSA) to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-metrics@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federated).  
`metrics.nodeSelector.key` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` **Required** Node selector label key used to target dedicated Kubernetes nodes for `metrics` runtime services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`metrics.nodeSelector.value` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` **Required** Node selector label value used to target dedicated Kubernetes nodes for `metrics` runtime services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`metrics.prometheus.containerPort` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `9090` **Chart:** `apigee-telemetry` The port to connect to the Prometheus metrics service.  
`metrics.prometheus.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-telemetry` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`metrics.prometheus.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-telemetry` The version label for this service's Docker image.  
`metrics.prometheus.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`metrics.prometheus.livenessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `6` **Chart:** `apigee-telemetry` The number of times Kubernetes will verify that liveness probes have failed before restarting the container. The minimum value is 1.  
`metrics.prometheus.livenessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-telemetry` Determines how often to perform a liveness probe, in seconds. The minimum value is 1.  
`metrics.prometheus.livenessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `3` **Chart:** `apigee-telemetry` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`metrics.prometheus.readinessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `120` **Chart:** `apigee-telemetry` The number of times Kubernetes will verify that readiness probes have failed before marking the pod _unready_. The minimum value is 1.  
`metrics.prometheus.readinessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-telemetry` Determines how often to perform a readiness probe, in seconds. The minimum value is 1.  
`metrics.prometheus.readinessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `3` **Chart:** `apigee-telemetry` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`metrics.prometheus.resources.limits.cpu` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the prometheus resource in a Kubernetes container, in millicores.   
`metrics.prometheus.resources.limits.memory` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `4Gi` **Chart:** `apigee-telemetry` The memory limit for the prometheus resource in a Kubernetes container, in gibibytes.   
`metrics.prometheus.resources.requests.cpu` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `128m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the prometheus in a Kubernetes container, in millicores.   
`metrics.prometheus.resources.requests.memory` | Advanced | **Introduced in version:** 1.14.1 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the prometheus in a Kubernetes container, in mebibytes.   
`metrics.prometheus.sslCertPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` **Required** Path to the SSL cert for the Prometheus metrics collection process. Prometheus is a tool Apigee can use for collecting and processing metrics. See: 

  * metrics
  * For background information, the [Prometheus website](https://prometheus.io/)

  
`metrics.prometheus.sslKeyPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` **Required** Path to the SSL Key for the Prometheus metrics collection process. Prometheus is a tool Apigee can use for collecting and processing metrics. See: 

  * metrics
  * For background information, the [Prometheus website](https://prometheus.io/)

  
`metrics.proxy.resources.requests.cpu` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the proxy in a Kubernetes container, in millicores.   
`metrics.proxy.resources.requests.memory` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the proxy in a Kubernetes container, in mebibytes.   
`metrics.proxy.resources.limits.cpu` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the proxy resource in a Kubernetes container, in millicores.   
`metrics.proxy.resources.limits.memory` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `1Gi` **Chart:** `apigee-telemetry` The memory limit for the proxy resource in a Kubernetes container, in gibibytes.   
`metrics.proxyStackdriverExporter.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The minimum number of `proxyStackdriverExporter` pods that must stay available during a voluntary disruption, such as during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    metrics:
      proxyStackdriverExporter:
        podDisruptionBudget:
          minAvailable: "50%"  
  
`metrics.proxyStackdriverExporter.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-telemetry` The maximum number of `proxyStackdriverExporter` pods that can be unavailable during a voluntary disruption, such as during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. The Apigee operator rejects setting both at once. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    metrics:
      proxyStackdriverExporter:
        podDisruptionBudget:
          maxUnavailable: 1  
  
`metrics.proxyStackdriverExporter.resources.requests.cpu` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `128m` **Chart:** `apigee-telemetry` The CPU needed for normal operation of the stackdriverExporter in a Kubernetes container, in millicores.   
`metrics.proxyStackdriverExporter.resources.requests.memory` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `512Mi` **Chart:** `apigee-telemetry` The memory needed for normal operation of the stackdriverExporter in a Kubernetes container, in mebibytes.   
`metrics.proxyStackdriverExporter.resources.limits.cpu` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `500m` **Chart:** `apigee-telemetry` The CPU limit for the stackdriverExporter resource in a Kubernetes container, in millicores.   
`metrics.proxyStackdriverExporter.resources.limits.memory` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `1Gi` **Chart:** `apigee-telemetry` The memory limit for the stackdriverExporter resource in a Kubernetes container, in gibibytes.   
`metrics.proxyURL` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` URL for the metrics process sidecar proxy in the Kubernetes cluster.   
`metrics.sdSidecar.containerPort` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `9091` **Chart:** `apigee-telemetry` The port for connecting to the Cloud Monitoring metrics service.  
`metrics.sdSidecar.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-telemetry` Determines when Kubelet pulls this service's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists
  * `Always`: Always pull the policy, even if it already exists For more information, see [ Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).

  
`metrics.sdSidecar.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-telemetry` The version label for this service's Docker image.  
`metrics.sdSidecar.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`metrics.serviceAccountPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-telemetry` One of either `serviceAccountPath` or `serviceAccountRef` is required. Path to Google Service Account key file with **Monitoring Metric Writer** role.   
`metrics.serviceAccountRef` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-telemetry` One of either `serviceAccountPath` or `serviceAccountRef` is required. A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`metrics.stackdriverExporter.resources.requests.cpu` | Advanced | **Introduced in version:** 1.4.0 **Chart:** `apigee-telemetry` Deprecated: Starting in Hybrid version 1.8, `metrics:stackdriverExporter` has been replaced with `metrics:appStackdriverExporter` and `metrics:proxyStackdriverExporter`. See: 

  * metrics.appStackdriverExporter.resources.requests.cpu
  * metrics.proxyStackdriverExporter.resources.requests.cpu

  
`metrics.stackdriverExporter.resources.requests.memory` | Advanced | _Introduced in version:_ 1.4.0 **Chart:** `apigee-telemetry` Deprecated: Starting in Hybrid version 1.8, `metrics:stackdriverExporter` has been replaced with `metrics:appStackdriverExporter` and `metrics:proxyStackdriverExporter`. See: 

  * metrics.appStackdriverExporter.resources.requests.memory
  * metrics.proxyStackdriverExporter.resources.requests.memory

  
`metrics.stackdriverExporter.resources.limits.cpu` | Advanced | **Introduced in version:** 1.4.0 **Chart:** `apigee-telemetry` Deprecated: Starting in Hybrid version 1.8, `metrics:stackdriverExporter` has been replaced with `metrics:appStackdriverExporter` and `metrics:proxyStackdriverExporter`. See: 

  * metrics.appStackdriverExporter.resources.limits.cpu
  * metrics.proxyStackdriverExporter.resources.limits.cpu

  
`metrics.stackdriverExporter.resources.limits.memory` | Advanced | **Introduced in version:** 1.4.0 **Chart:** `apigee-telemetry` Deprecated: Starting in Hybrid version 1.8, `metrics:stackdriverExporter` has been replaced with `metrics:appStackdriverExporter` and `metrics:proxyStackdriverExporter`. See: 

  * metrics.appStackdriverExporter.resources.limits.memory
  * metrics.proxyStackdriverExporter.resources.limits.memory

  
`metrics.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `300` **Chart:** `apigee-telemetry` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately.  
`metrics.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`metrics.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`metrics.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-telemetry` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`metrics.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`metrics.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-telemetry` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `mintTaskScheduler`

`mintTaskScheduler` is the cron job to schedule monetization tasks, like recurring fee calculation on a periodic basis.

The following table describes the properties of the `mintTaskScheduler` object:

Property | Type | Description  
---|---|---  
`mintTaskScheduler.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-org` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`mintTaskScheduler.gsa` | Advanced | **Introduced in version:** 1.15.1 **Default value:** None **Chart:** `apigee-org` The email address of the `apigee-mint-task-scheduler` Google IAM service account (GSA) to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-mint-task-scheduler@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`mintTaskScheduler.image.pullPolicy` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `IfNotPresent` **Chart:** `apigee-org` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`mintTaskScheduler.image.tag` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `1.16.11` **Chart:** `apigee-org` The version label for this service's Docker image.  
`mintTaskScheduler.image.url` | Advanced | **Introduced in version:** 1.7.0 **Default value:** None **Chart:** `apigee-org` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`mintTaskScheduler.resources.limits.cpu` | Advanced | **Introduced in version:** 1.1.0 **Default value:** `2000m` **Chart:** `apigee-org` The CPU limit for the resource in a Kubernetes container, in millicores.  
`mintTaskScheduler.resources.limits.memory` | Advanced | **Introduced in version:** 1.1.0 **Default value:** `4Gi` **Chart:** `apigee-org` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`mintTaskScheduler.resources.requests.cpu` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `500m` **Chart:** `apigee-org` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`mintTaskScheduler.resources.requests.memory` | Advanced | **Introduced in version:** 1.7.0 **Default value:** `512Mi` **Chart:** `apigee-org` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes.  
`mintTaskScheduler.serviceAccountPath` | Basic | **Introduced in version:** 1.15.1 **Default value:** None **Chart:** `apigee-org` One of either `serviceAccountPath` or `serviceAccountRef` is required. Path to Google Service Account key file.   
`mintTaskScheduler.serviceAccountRef` | Basic | **Introduced in version:** 1.15.1 **Default value:** None **Chart:** `apigee-org` One of either `serviceAccountPath` or `serviceAccountRef` is required. A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`mintTaskScheduler.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mintTaskScheduler.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mintTaskScheduler.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mintTaskScheduler.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`mintTaskScheduler.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `newDataPipeline`

`newDataPipeline` determines if Apigee hybrid uses the [Pub/Sub data pipeline](https://docs.cloud.google.com/pubsub/docs/overview) for the runtime components to write data directly to the control plane.

The following table describes the properties of the `newDataPipeline` object:

Property | Type | Description  
---|---|---  
`newDataPipeline.debugSession` | Advanced | **Introduced in version:** 1.13.1 **Default value:** `true` **Chart:** `apigee-env` Determines if the Pub/Sub data pipeline is enabled. **Caution:** Do not change this property for installations running Apigee hybrid 1.14.1 or later.   
`newDataPipeline.analytics` | Advanced | **Introduced in version:** 1.13.1 **Default value:** `true` **Chart:** `apigee-env` Determines if analytics use the Pub/Sub data pipeline.  **Caution:** Do not change this property for installations running Apigee hybrid 1.14.1 or later.   
  
## `nodeSelector`

The `nodeSelector` object defines the node for your Apigee instance. Behind the scenes Apigee hybrid takes care to map the label key/value for `apigeeRuntime` and `apigeeData` to the individual Istio and MART components when you install or upgrade the `apigee-org` and `apigee-ingress-manager` charts. You can override this for individual objects in the mart:nodeSelector property. 

The following table describes the properties of the `nodeSelector` object:

Property | Type | Description  
---|---|---  
`nodeSelector.apigeeData.key` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `cloud.google.com/gke-nodepool` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` ApigeeData is the node for the Cassandra database. Node selector label key for targeting Kubernetes nodes for working with Apigee services data. See [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`nodeSelector.apigeeData.value` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `apigee-data` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` apigee-data is the node for the Cassandra database. Node selector label value for targeting Kubernetes nodes for working with Apigee services data. See [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`nodeSelector.apigeeRuntime.key` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `cloud.google.com/gke-nodepool` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` Apigee Runtime is the node for the runtime environment for the project. Node selector label key for targeting Kubernetes nodes for Apigee runtime services. See [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`nodeSelector.apigeeRuntime.value` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `apigee-runtime` **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` `apigee-runtime` is the node for the runtime environment for the project. Node selector label value for targeting Kubernetes nodes for Apigee runtime services. See [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`nodeSelector.requiredForScheduling` | Advanced | **Introduced in version:** 1.0.0 **Default value:** true **Chart:** `apigee-operator`, `apigee-datastore`, `apigee-telemetry`, `apigee-redis`, `apigee-ingress-manager`, `apigee-org`, `apigee-env`, `apigee-virtualhost` The `requiredForScheduling` property defaults to `true`. When `true`, it means that if Kubernetes cannot find nodes with the label key/value that is configured then the underlying Pods will not get scheduled on VM worker nodes. For production, `nodeSelector.requiredForScheduling` should be set to true.  See [Configure dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
  
## `redis`

The following table describes the properties of the `redis` object:

Property | Type | Description  
---|---|---  
`redis.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-redis` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`redis.auth.password` | Basic | **Introduced in version:** 1.6.0 **Default value:** `iloveapis123` **Chart:** `apigee-redis` **Required** Password for the Redis administrator. The admin user is used for any administrative activities performed on the Redis cluster.  
`redis.auth.secret` | Basic | **Introduced in version:** 1.9.1 **Default value:** None **Chart:** `apigee-redis` The name of the file stored in a Kubernetes secret that contains the password for the Redis administrator. The secret file should contain the key: 
    
    
    data:
        redis.auth.password: encoded_value

See also:

  * `redis.auth.password`
  * [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/k8s-secrets)
  * [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the Kubernetes documentation
  * [ Creating a Secret Using kubectl](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret) in the Kubernetes documentation

  
`redis.envoy.image.pullPolicy` | Advanced | **Introduced in version:** 1.6.0 **Default value:** `IfNotPresent` **Chart:** `apigee-redis` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`redis.envoy.image.tag` | Advanced | **Introduced in version:** 1.6.0 **Default value:** `1.16.11` **Chart:** `apigee-redis` The version label for this service's Docker image.  
`redis.envoy.image.url` | Advanced | **Introduced in version:** 1.6.0 **Default value:** None **Chart:** `apigee-redis` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`redis.envoy.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-redis` The minimum number of Redis Envoy pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    redis:
      envoy:
        podDisruptionBudget:
          minAvailable: "50%"  
  
`redis.envoy.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-redis` The maximum number of Redis Envoy pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    redis:
      envoy:
        podDisruptionBudget:
          maxUnavailable: 1  
  
`redis.image.pullPolicy` | Advanced | **Introduced in version:** 1.6.0 **Default value:** `IfNotPresent` **Chart:** `apigee-redis` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`redis.image.tag` | Advanced | **Introduced in version:** 1.6.0 **Default value:** `1.16.11` **Chart:** `apigee-redis` The version label for this service's Docker image.  
`redis.image.url` | Advanced | **Introduced in version:** 1.6.0 **Default value:** None **Chart:** `apigee-redis` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`redis.replicaCount` | Basic | **Introduced in version:** 1.6.0 **Default value:** `2` **Chart:** `apigee-redis` Redis is a replicated storage. This property specifies the number of Redis nodes employed as a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).  
`redis.resources.requests.cpu` | Advanced | **Introduced in version:** 1.6.0 **Default value:** `500m` **Chart:** `apigee-redis` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores. Apigee recommends a value from `500m` to `1000m`. With 0.5 cores, a Redis node can typically handle 10K QPS. With 1.0 core, it can typically handle 20K QPS. CPU request resources above 1000m are not helpful in most cases.  
`redis.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-redis` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`redis.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-redis` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`redis.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-redis` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`redis.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-redis` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`redis.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-redis` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `runtime`

The following table describes the properties of the `runtime` object:

Property | Type | Description  
---|---|---  
`runtime.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-env` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`runtime.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-env` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/customize-services#custom-annotations).  
`runtime.envVars` | Basic | **Introduced in version:** 1.13.1 **Default value:** None **Chart:** `apigee-env` Allows you to supply additional env variables to the runtime component in a key-value pair: 
    
    
    runtime:
      envVars:
        KEY_1: VALUE_N
        ... ...
        KEY_N: VALUE_N

for example: 
    
    
    runtime:
      envVars:
        RUNTIME_ENV_VAR1: "value of runtime env-var 1"
        RUNTIME_ENV_VAR2: "value of runtime env-var 2"  
  
`runtime.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-env` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`runtime.hpaBehavior.scaleDown.percent.periodSeconds` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 60 **Chart:** `apigee-env` The window of time for which the policy should hold true when scaling down a percentage of runtime instances.  
`runtime.hpaBehavior.scaleDown.percent.value` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 20 **Chart:** `apigee-env` The amount of change which is permitted by the policy when scaling down a percentage of runtime instances.  
`runtime.hpaBehavior.scaleDown.pods.periodSeconds` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 60 **Chart:** `apigee-env` The window of time for which the policy should hold true when scaling down a number of runtime instances.  
`runtime.hpaBehavior.scaleDown.pods.value` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 20 **Chart:** `apigee-env` The amount of change which is permitted by the policy when scaling down a number of runtime instances.  
`runtime.hpaBehavior.scaleDown.selectPolicy` | Advanced | **Introduced in version:** 1.7.0 **Default value:** Min **Chart:** `apigee-env` The decision that autoscaler makes between multiple autoscaling policies. Set the value to **Min** allows the smallest change in scaling down runtime instances. Set the value to **Max** allows the largest change in scaling down runtime instances.  
`runtime.hpaBehavior.scaleDown.stabilizationWindowSeconds` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 120 **Chart:** `apigee-env` The number of seconds for which past recommendations should be considered while scaling down.  
`runtime.hpaBehavior.scaleUp.percent.periodSeconds` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 60 **Chart:** `apigee-env` The window of time for which the policy should hold true when scaling up a percentage of runtime instances.  
`runtime.hpaBehavior.scaleUp.percent.value` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 20 **Chart:** `apigee-env` The window of time for which the policy should hold true when scaling up a percentage of runtime instances.  
`runtime.hpaBehavior.scaleUp.pods.periodSeconds` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 60 **Chart:** `apigee-env` The window of time for which the policy should hold true when scaling up a number of runtime instances.  
`runtime.hpaBehavior.scaleUp.pods.value` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 4 **Chart:** `apigee-env` The amount of change which is permitted by the policy when scaling up a number of runtime instances.  
`runtime.hpaBehavior.scaleUp.selectPolicy` | Advanced | **Introduced in version:** 1.7.0 **Default value:** Max **Chart:** `apigee-env` The decision that autoscaler makes between multiple autoscaling policies. Set the value to **Min** allows the smallest change in scaling up runtime instances. Set the value to **Max** allows the largest change in scaling up runtime instances.  
`runtime.hpaBehavior.scaleUp.stabilizationWindowSeconds` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 30 **Chart:** `apigee-env` The number of seconds for which past recommendations should be considered while scaling up runtime instances.  
`runtime.hpaMetrics.serverMainTaskWaitTime` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 400M **Chart:** `apigee-env` The desired average wait time (in ms) of processing queue in runtime instances for proxy requests at the http layer.  
`runtime.hpaMetrics.serverNioTaskWaitTime` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 400M **Chart:** `apigee-env` The desired average wait time (in ms) of processing queue in runtime instances for proxy requests to process policies.  
`runtime.hpaMetrics.targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.7.0 **Default value:** 75 **Chart:** `apigee-env` The desired CPU utilization percentage across all runtime instances.  
`runtime.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-env` The version label for this service's Docker image.  
`runtime.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`runtime.livenessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `2` **Chart:** `apigee-env` The number of times Kubernetes will verify that liveness probes have failed before restarting the container. The minimum value is 1.  
`runtime.livenessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `60` **Chart:** `apigee-env` The number of seconds after a container is started before a liveness probe is initiated.  
`runtime.livenessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-env` Determines how often to perform a liveness probe, in seconds. The minimum value is 1.  
`runtime.livenessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`runtime.nodeSelector.key` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` Optional Node selector label key for targeting Kubernetes nodes for `runtime` services. See nodeSelector property.  
`runtime.nodeSelector.value` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` Node selector label value for targeting Kubernetes nodes for `runtime` services. See [ Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-dedicated-nodes).  
`runtime.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The minimum number of runtime pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. To set a different budget for the runtime pods in a specific environment, use `envs[].components.runtime.podDisruptionBudget.minAvailable`. For example, in `overrides.yaml`:
    
    
    runtime:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`runtime.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The maximum number of runtime pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. To set a different budget for the runtime pods in a specific environment, use `envs[].components.runtime.podDisruptionBudget.maxUnavailable`. For example, in `overrides.yaml`:
    
    
    runtime:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`runtime.readinessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `2` **Chart:** `apigee-env` The number of times Kubernetes will verify that readiness probes have failed before marking the pod _unready_. The minimum value is 1.  
`runtime.readinessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `60` **Chart:** `apigee-env` The number of seconds after a container is started before a readiness probe is initiated.  
`runtime.readinessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-env` Determines how often to perform a readiness probe, in seconds. The minimum value is 1.  
`runtime.readinessProbe.successThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` The minimum consecutive successes needed for a readiness probe to be considered successful after a failure. The minimum value is 1.  
`runtime.readinessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`runtime.release.strategy` | Advanced | **Introduced in version:** 1.16.8 **Default value:** `rolling` **Chart:** `apigee-env` Selects the strategy used to roll out a new runtime (message processor) ReplicaSet when an environment configuration change triggers a release. You can also set this per environment with `envs[].components.runtime.release.strategy`. Allowed values:

  * `rolling` (default): Stands up the new ReplicaSet alongside the existing one and shifts traffic to it in stages before scaling down the old ReplicaSet. This provides staged traffic migration but temporarily requires extra compute headroom (up to roughly double the steady-state pod count) during the release. Recommended for most production environments.
  * `scale-down-first`: Replaces pods one at a time, draining an existing pod before creating its replacement. Because each swap is one-for-one, the release stays within the steady-state pod count and does not require extra compute headroom. Use this for clusters without node autoscaling, such as hardware-constrained or bare-metal installations. Releases are slower and do not include staged traffic migration.
  * `none`: Performs an immediate transition to the new ReplicaSet without staged traffic migration.

  
`runtime.replicaCountMax` | Basic | **Introduced in version:** 1.0.0 **Default value:** `4` **Chart:** `apigee-env` Maximum number of replicas available for autoscaling. If using [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits), this will be applied to all replicasets for the environment. Each replicaset will still autoscale independently.  
`runtime.replicaCountMin` | Basic | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` Minimum number of replicas available for autoscaling. If using [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits), this will be applied to all replicasets for the environment. Each replicaset will still autoscale independently..  
`runtime.resources.limits.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `4000m` **Chart:** `apigee-env` The CPU limit for the resource in a Kubernetes container, in millicores.  
`runtime.resources.limits.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `6Gi` **Chart:** `apigee-env` The memory limit for the resource in a Kubernetes container, in mebibytes (Mi) or gibibytes (Gi). **Note:** If you are using message payloads larger than 10MB, you must make the following configuration changes: 

  * Increase the heap size to 4Gi.
  * Increase `runtime.resources.limits.memory` to 6Gi.
  * Increase `runtime.resources.requests.memory` to 4Gi.

See [Configure large message payload support in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support) for more details.   
`runtime.resources.requests.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `500m` **Chart:** `apigee-env` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores. **Note:** To achieve smooth autoscaling of the message processors to accommodate traffic increases, we recommend that you do not exceed two cores (2000 millicores) if you decide to override the default.  Apigee runtime components are bounded by I/O, and adding more CPU capacity does not always help with traffic increases. When there are high CPU requests, message processors may not autoscale and liveliness probes may fail with high traffic.   
`runtime.resources.requests.memory` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `512Mi` (see note below) **Chart:** `apigee-env` The memory needed for normal operation of the resource in a Kubernetes container, in mebibytes (`Mi`) or Gibibytes (`Gi`). **Important:** For production environments, reset the value of `runtime.resources.requests.memory` to at least `1Gi` in your `overrides.yaml`. The default of `512Mi` is enough for initial operation and configuration, but should be raised for production. To achieve smooth autoscaling of the message processors to accommodate traffic increases, we recommend that you do not exceed 2.5Gi (2560Mi) if you decide to override the default. **Note:** If you are using message payloads larger than 10MB, you must make the following configuration changes: 

  * Increase the heap size to 4Gi.
  * Increase `runtime.resources.limits.memory` to 6Gi.
  * Increase `runtime.resources.requests.memory` to 4Gi.

See [Configure large message payload support in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support) for more details.   
`runtime.service.type` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `ClusterIP` **Chart:** `apigee-env` The type of service. You can set this to a service other than ClusterIP; for example, `LoadBalancer`.  
`runtime.targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `75` **Chart:** `apigee-env` Target CPU utilization for the runtime process on the pod. The value of this field enables the runtime to auto-scale when CPU utilization reaches this value, up to `replicaCountMax`.  
`runtime.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `3600` **Chart:** `apigee-env` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately. **Note:** This value is set by the Apigee controller and cannot be overridden.  
`runtime.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`runtime.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`runtime.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-env` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`runtime.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`runtime.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `securityContext`

Defines security settings for pods that can be applied at the global, environment, or component level.

Property | Type | Description  
---|---|---  
`securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-operator` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
  
## `synchronizer`

Ensures that the Message Processors are kept up to date with the latest deployed API proxy bundles. To do this, the Synchronizer polls the management plane; when a new contract is detected, the Synchronizer sends it to the runtime plane. By default, Synchronizer stores environment configuration data in Cassandra.

For more information, see [Configure the Synchronizer](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/synchronizer-access).

The following table describes the properties of the `synchronizer` object:

Property | Type | Description  
---|---|---  
`synchronizer.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-env` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`synchronizer.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-env` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`synchronizer.image.pullPolicy` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `IfNotPresent` **Chart:** `apigee-env` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`synchronizer.image.tag` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1.16.11` **Chart:** `apigee-env` The version label for this service's Docker image.  
`synchronizer.image.url` | Advanced | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`synchronizer.livenessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `2` **Chart:** `apigee-env` The number of times Kubernetes will verify that liveness probes have failed before restarting the container. The minimum value is 1.  
`synchronizer.livenessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `0` **Chart:** `apigee-env` The number of seconds after a container is started before a liveness probe is initiated.  
`synchronizer.livenessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-env` Determines how often to perform a liveness probe, in seconds. The minimum value is 1.  
`synchronizer.livenessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`synchronizer.nodeSelector.key` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` **Required** Optional node selector label key for targeting Kubernetes nodes for `synchronizer` runtime services. See nodeSelector.  
`synchronizer.nodeSelector.value` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` Optional node selector label value used for targeting Kubernetes nodes for `synchronizer` runtime services. See nodeSelector.  
`synchronizer.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The minimum number of synchronizer pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. To set a different budget for the synchronizer pods in a specific environment, use `envs[].components.synchronizer.podDisruptionBudget.minAvailable`. For example, in `overrides.yaml`:
    
    
    synchronizer:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`synchronizer.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-env` The maximum number of synchronizer pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. To set a different budget for the synchronizer pods in a specific environment, use `envs[].components.synchronizer.podDisruptionBudget.maxUnavailable`. For example, in `overrides.yaml`:
    
    
    synchronizer:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`synchronizer.pollInterval` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `60` **Chart:** `apigee-env` The length of time that Synchronizer waits between polling operations. Synchronizer polls Apigee control plane services to detect and pull new runtime contracts.  
`synchronizer.readinessProbe.failureThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `2` **Chart:** `apigee-env` The number of times Kubernetes will verify that readiness probes have failed before marking the pod _unready_. The minimum value is 1.  
`synchronizer.readinessProbe.initialDelaySeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `0` **Chart:** `apigee-env` The number of seconds after a container is started before a readiness probe is initiated.  
`synchronizer.readinessProbe.periodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `5` **Chart:** `apigee-env` Determines how often to perform a readiness probe, in seconds. The minimum value is 1.  
`synchronizer.readinessProbe.successThreshold` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` The minimum consecutive successes needed for a readiness probe to be considered successful after a failure. The minimum value is 1.  
`synchronizer.readinessProbe.timeoutSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1` **Chart:** `apigee-env` The number of seconds after which a liveness probe times out. The minimum value is 1.  
`synchronizer.replicaCount` | Basic | **Introduced in version:** 1.0.0 **Chart:** `apigee-env` Deprecated: Starting in Hybrid version 1.2, manage the Synchronizer replica count with: `synchronizer.replicaCountMax` and `synchronizer.replicaCountMin`  
`synchronizer.replicaCountMax` | Basic | **Introduced in version:** 1.2.0 **Default value:** `4` **Chart:** `apigee-env` Maximum number of replicas for autoscaling.  
`synchronizer.replicaCountMin` | Basic | **Introduced in version:** 1.2.0 **Default value:** `1` **Chart:** `apigee-env` Minimum number of replicas for autoscaling.  
`synchronizer.resources.limits.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `2000m` **Chart:** `apigee-env` The CPU limit for the resource in a Kubernetes container, in millicores.  
`synchronizer.resources.limits.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `5Gi` **Chart:** `apigee-env` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`synchronizer.resources.requests.cpu` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `100m` **Chart:** `apigee-env` The CPU needed for normal operation of the resource in a Kubernetes container, in millicores.  
`synchronizer.resources.requests.memory` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `1Gi` **Chart:** `apigee-env` The memory needed for normal operation of the resource in a Kubernetes container, in gigabytes.  
`synchronizer.serviceAccountPath` | Basic | **Introduced in version:** 1.0.0 **Default value:** None **Chart:** `apigee-env` One of either `serviceAccountPath` or `serviceAccountRef` is required. Path to Google Service Account key file with **Apigee Synchronizer Manager** role.   
`synchronizer.serviceAccountRef` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-env` One of either `serviceAccountPath` or `serviceAccountRef` is required. A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`synchronizer.serviceAccountSecret` | Basic | **Introduced in version:** 1.1.0 **Default value:** None **Chart:** `apigee-env` The name of a [Kubernetes secret](https://kubernetes.io/docs/concepts/configuration/secret/). You must create the secret using a Google Service Account key with the **Apigee Synchronizer Manager** role as its input.  
`synchronizer.targetCPUUtilizationPercentage` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `75` **Chart:** `apigee-env` Target CPU utilization for the Synchronizer process on the pod. The value of this field enables Synchronizer to auto-scale when CPU utilization reaches this value, up to `replicaCountMax`.   
`synchronizer.terminationGracePeriodSeconds` | Advanced | **Introduced in version:** 1.0.0 **Default value:** `30` **Chart:** `apigee-env` The maximum time between a request for pod deletion and when the pod is killed, in seconds. During this period, any prestop hooks will be executed and any running process should terminate gracefully. The pod will be killed when all running processes have terminated or at the end of the grace period, whichever comes first. If there are no running processes, the pod will be killed immediately.  
`synchronizer.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`synchronizer.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`synchronizer.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-env` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`synchronizer.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`synchronizer.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-env` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
## `virtualhosts`

The `virtualhosts` property is a required configuration property. Virtual hosts allow Apigee hybrid to handle API requests to a specified environment group.. 

For more information, see [Configure virtual hosts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/base-path-routing).

The following table describes the properties of the `virtualhosts` object:

Property | Type | Description  
---|---|---  
`virtualhosts[].additionalGateways` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-virtualhost` A list of Istio Gateways to route traffic to.  
`virtualhosts[].cipherSuites[]` | Advanced | **Introduced in version:** 1.9.2 **Default value:** None **Chart:** `apigee-virtualhost` This property configures the TLS ciphers used in the ingress gateway. **Note:** This property overrides the list of cipher suites enabled and does not append to it.Values for `virtualhosts.cipherSuites` must be in [OpenSSL format](https://www.ssl.org/cipher-suite-mapping). Below is a list of supported ciphers in OpenSSL format. You can find more information about the supported ciphers in the documentation for the [Boring FIPS build of Envoy](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/transport_sockets/tls/v3/common.proto.html). A blank value defaults to the cipher suites supported by the Boring FIPS build of Envoy. **TLS v1.3** : | Enabled by default | Additional ciphersuites  
---|---  
  
  * TLS_AES_128_GCM_SHA256
  * TLS_AES_256_GCM_SHA384
  * TLS_CHACHA20_POLY1305_SHA256

| TLS 1.3 ciperhsuites cannot   
be overridden.  
  
**TLS v1.2** :

Enabled by default | Additional ciphersuites  
---|---  
  
  * ECDHE-ECDSA-AES128-GCM-SHA256
  * ECDHE-RSA-AES128-GCM-SHA256
  * ECDHE-ECDSA-AES256-GCM-SHA384
  * ECDHE-RSA-AES256-GCM-SHA384

| 

  * AES128-GCM-SHA256
  * AES128-SHA
  * AES256-GCM-SHA384
  * AES256-SHA
  * ECDHE-ECDSA-AES128-GCM-SHA256
  * ECDHE-ECDSA-AES128-SHA
  * ECDHE-ECDSA-AES256-GCM-SHA384
  * ECDHE-ECDSA-AES256-SHA
  * ECDHE-ECDSA-CHACHA20-POLY1305
  * ECDHE-RSA-AES128-GCM-SHA256
  * ECDHE-RSA-AES128-SHA
  * ECDHE-RSA-AES256-GCM-SHA384
  * ECDHE-RSA-AES256-SHA
  * ECDHE-RSA-CHACHA20-POLY1305

  
  
**TLS v1.1** :

Enabled by default | Additional ciphersuites  
---|---  
TLS v1.1 is not enabled by default. | 

  * ECDHE-ECDSA-AES128-GCM-SHA256
  * ECDHE-RSA-AES128-GCM-SHA256
  * ECDHE-ECDSA-AES256-GCM-SHA384
  * ECDHE-RSA-AES256-GCM-SHA384
  * ECDHE-ECDSA-CHACHA20-POLY1305
  * ECDHE-RSA-CHACHA20-POLY1305
  * ECDHE-ECDSA-AES128-SHA
  * ECDHE-ECDSA-AES256-SHA
  * ECDHE-RSA-AES256-SHA

  
  
To enable more ciphersuites, add them to the `virtualhosts.cipherSuites` property along with the TLS version you want to enable them for in the `virtualhosts.minTLSProtocolVersion` property. For example, to enable all accepted TLS v.1.2 ciphersuites, add the following to your `virtualhosts` configuration:
    
    
    virtualhosts:
    - name: ENV_GROUP_NAME
      minTLSProtocolVersion: "1.2"
      cipherSuites:
      - "AES128-GCM-SHA256"
      - "AES128-SHA"
      - "AES256-GCM-SHA384"
      - "AES256-SHA"
      - "ECDHE-ECDSA-AES128-GCM-SHA256"
      - "ECDHE-ECDSA-AES128-SHA"
      - "ECDHE-ECDSA-AES256-GCM-SHA384"
      - "ECDHE-ECDSA-AES256-SHA"
      - "ECDHE-ECDSA-CHACHA20-POLY1305"
      - "ECDHE-RSA-AES128-GCM-SHA256"
      - "ECDHE-RSA-AES128-SHA"
      - "ECDHE-RSA-AES256-GCM-SHA384"
      - "ECDHE-RSA-AES256-SHA"
      - "ECDHE-RSA-CHACHA20-POLY1305"
    ...
    

If you want to enable older versions of TLS in your Apigee ingress gateway deployment, use the `virtualhosts.minTLSProtocolVersion` and `virtualhosts.cipherSuites` properties. 

For example, to enable TLS v.1.1:
    
    
    virtualhosts:
    - name: ENV_GROUP_NAME
      minTLSProtocolVersion: "1.1"
      cipherSuites:
      - "ECDHE-ECDSA-AES128-GCM-SHA256"
      - "ECDHE-RSA-AES128-GCM-SHA256"
      - "ECDHE-ECDSA-AES256-GCM-SHA384"
      - "ECDHE-RSA-AES256-GCM-SHA384"
      - "ECDHE-ECDSA-CHACHA20-POLY1305"
      - "ECDHE-RSA-CHACHA20-POLY1305"
      - "ECDHE-ECDSA-AES128-SHA"
      - "ECDHE-RSA-AES128-SHA"
      - "ECDHE-ECDSA-AES256-SHA"
      - "ECDHE-RSA-AES256-SHA"
    ...
    

**Note:** This property overrides the list of cipher suites supported by Envoy, and does not append to it.**Tip:** The `virtualhosts.cipherSuites` property uses the OpenSSL cipher suite format. For a list of ciphers with their names in both OpenSSL and IANA format, see [Translating OpenSSL cipher suite names to IANA](https://www.ssl.org/cipher-suite-mapping) in the SSL.org documentation.  
`virtualhosts[].name` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-virtualhost` **Required** The name of the virtual host.  
`virtualhosts[].maxTLSProtocolVersion` | Basic | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-virtualhost` The maximum version of the TLS protocol Envoy can select. Envoy automatically uses the optimal TLS protocol version between `virtualhosts[].minTLSProtocolVersion` and `virtualhosts[].maxTLSProtocolVersion`. The value must be a string representing the TLS version number. For example: 
    
    
    virtualhosts:
    - name: default
      maxTLSProtocolVersion: "1.3"

Where the string represents the TLS version number in the form `"#.#"`. In the example above, `"1.3"` represents the Istio TLS version `TLSV1_3`.  See also [ `ServerTLSSettings`](https://istio.io/latest/docs/reference/config/networking/gateway/#ServerTLSSettings) in the Istio documentation.  
`virtualhosts[].minTLSProtocolVersion` | Basic | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-virtualhost` The minimum version of the TLS protocol Envoy can select. Envoy automatically uses the optimal TLS protocol version between `virtualhosts[].minTLSProtocolVersion` and `virtualhosts[].maxTLSProtocolVersion`. The value must be a string representing the TLS version number. For example: 
    
    
    virtualhosts:
    - name: default
      minTLSProtocolVersion: "1.2"

Where the string represents the TLS version number in the form `"#.#"`. In the example above, `"1.2"` represents the Istio TLS version `TLSV1_2`.  See also [ `ServerTLSSettings`](https://istio.io/latest/docs/reference/config/networking/gateway/#ServerTLSSettings) in the Istio documentation.  
`virtualhosts[].requestTimeout` | Basic | **Introduced in version:** 1.10.0 **Default value:** `300` **Chart:** `apigee-virtualhost` The number of seconds after which a request times out. The minimum value is 1.  
`virtualhosts[].selector` | Basic | **Introduced in version:** 1.2.0 **Default value:** `app: apigee-ingressgateway` **Chart:** `apigee-virtualhost` **Required** A key-value selector-value pair for pointing to different ingress selectors.

  * `apigee-ingressgateway`: for Apigee hybrid installations using Apigee ingress gateway.
  * `istio-ingressgateway`: for Apigee hybrid installations using Cloud Service Mesh (Apigee hybrid versions 1.8 and earlier).

If no selector label is supplied, the configuration is supplied to Apigee ingress gateway.   
`virtualhosts[].sslCertPath` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-virtualhost` Either `sslCertPath`/`sslKeyPath` or `sslSecret` is required. The path on your system to a TLS certificate file. **Note:** For each configured environment, the Common Name (CN) in the cert must match the domain in the `hostAliases[]` property. For example, if the CN is `*.example.com`, the `hostAliases[]` could be `foo.example.com` or `bar.example.com`.   
`virtualhosts[].sslKeyPath` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-virtualhost` Either `sslCertPath`/`sslKeyPath` or `sslSecret` is required. The path on your system to the TLS private key file.  
`virtualhosts[].sslSecret` | Basic | **Introduced in version:** 1.2.0 **Default value:** None **Chart:** `apigee-virtualhost` **Either`sslCertPath`/`sslKeyPath` or `sslSecret` is required**. The name if the file stored in a Kubernetes secret that contains the Cassandra users and passwords. You can create the secret using following the following instructions: [Create the Secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls#create-the-secret).  See also:

  * [Storing data in a Kubernetes secret](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/k8s-secrets)
  * [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) in the Kubernetes documentation
  * [ Creating a Secret Using kubectl](https://kubernetes.io/docs/concepts/configuration/secret/#creating-a-secret) in the Kubernetes documentation

  
  
## `watcher`

The `watcher` property is a required configuration property. The watcher is a process that watches for configuration changes and triggers their application to the runtime plane. 

The following table describes the properties of the `watcher` object:

Property | Type | Description  
---|---|---  
`watcher.securityContext.seccompProfile.type` | Advanced |  **Introduced in version:** 1.16.0 **Default value:** None **Chart:** `apigee-org` Specifies the Seccomp profile type to apply to the pod's security context. Allowed values are `RuntimeDefault` (to use the container runtime's default profile) or `Unconfined` (to apply no Seccomp restrictions). If not specified, no profile is applied by Apigee. See [Configure Seccomp profiles for pod security](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles).  
`watcher.annotations` | Advanced | **Introduced in version:** 1.5.0 **Default value:** None **Chart:** `apigee-org` Optional key/value map used to annotate pods. For more information, see [Custom annotations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/customize-services#custom-annotations).  
`watcher.args.enableIssueScanning` | Advanced | **Introduced in version:** 1.10.0 **Default value:** `true` **Chart:** `apigee-org` Enables or disables Automated issue surfacing. When `true`, Watcher automatically scans the control plane and Kubernetes API server state to determine if there are any configuration issues. Set to `false` to disable Automated issue surfacing. For more information, see [Automated issue surfacing](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/automated-issue-surfacing).  
`watcher.args.enableLeaderElect` | Advanced | **Introduced in version:** 1.13.0 **Default value:** `true` **Chart:** `apigee-org` When `true` (the default) `watcher.args.enableLeaderElect` selects a single watcher pod to manage and report the routing information. Limiting this to a single pod is required to prevent downtime during upgrades or rollback. During these events, multiple versions of watcher can be running simultaneously. Each Watcher instance may have different route creation logic, which can cause downtime.`watcher.replicaCountMax`.   
`watcher.args.issueScanInterval` | Advanced | **Introduced in version:** 1.10.0 **Default value:** `60` **Chart:** `apigee-org` The interval in seconds for how often Watcher scans the runtime plane for automated issue surfacing. For more information, see [Automated issue surfacing](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/automated-issue-surfacing).  
`watcher.gsa` | Advanced | **Introduced in version:** 1.10.0 **Default value:** None **Chart:** `apigee-org` **Helm only** : The email address of the `apigee-watcher` Google IAM service account (GSA) to associate with the corresponding Kubernetes service account when enabling Workload Identity on GKE clusters using Helm charts. Set this when you have set `gcp.workloadIdentity.enabled` to `true`. GSA email addresses typically have the format of:
    
    
    GSA_NAME@PROJECT_ID.iam.gserviceaccount.com

For example:
    
    
    apigee-watcher@my-hybrid-project.iam.gserviceaccount.com

**Tip:** You can find the email address of your service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"

See [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federation).  
`watcher.image.pullPolicy` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `IfNotPresent` **Chart:** `apigee-org` Determines when [ kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/#kubelet) pulls the pod's Docker image. Possible values include:

  * `IfNotPresent`: Do not pull a new image if it already exists.
  * `Always`: Always pull the image, regardless of whether it exists already.

For more information, see [Updating images](https://kubernetes.io/docs/concepts/containers/images/#updating-images).  
`watcher.image.tag` | Advanced | **Introduced in version:** 1.4.0 **Default value:** `1.16.11` **Chart:** `apigee-org` The version label for this service's Docker image.  
`watcher.image.url` | Advanced | **Introduced in version:** 1.4.0 **Default value:** None **Chart:** `apigee-org` The location of the Docker image for this service. Use `[apigee-pull-push](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-pull-push) --list` to see the current repository URL for this component. **Tip:** Consider using `hub` to set a private repository URL for all components instead of configuring them individually.  
`watcher.podDisruptionBudget.minAvailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The minimum number of watcher pods that must stay available during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `minAvailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `minAvailable` and `maxUnavailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    watcher:
      podDisruptionBudget:
        minAvailable: "50%"  
  
`watcher.podDisruptionBudget.maxUnavailable` | Advanced |  **Introduced in version:** 1.16.10 **Default value:** None **Chart:** `apigee-org` The maximum number of watcher pods that can be unavailable during a voluntary disruption, for example during a node pool upgrade or a node drain. This field sets the `maxUnavailable` field of the [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) for these pods. It takes either an integer number of pods (`1`) or a percentage string (`"50%"`). `maxUnavailable` and `minAvailable` are mutually exclusive; set only one. Setting both at once is rejected by the Apigee operator. If you set neither field, the Apigee operator still generates a PodDisruptionBudget for these pods, using `maxUnavailable: 1` by default. For example, in `overrides.yaml`:
    
    
    watcher:
      podDisruptionBudget:
        maxUnavailable: 1  
  
`watcher.replicaCountMax` | Basic | **Introduced in version:** 1.3.0 **Default value:** `1` **Chart:** `apigee-org` The maximum number of watcher replicas. This should be kept at **`1`** to avoid conflicts.  Apigee hybrid uses one watcher pod per installation. Leader election automatically selects one watcher pod. Additional watcher pod replicas will be forced into an unstable state. See watcher.args.enableLeaderElect.  **Warning:** Do not exceed a value of 1 for watcher.replicaCountMax.  
`watcher.replicaCountMin` | Basic | **Introduced in version:** 1.3.0 **Default value:** `1` **Chart:** `apigee-org` The minimum number of watcher replicas.  
`watcher.resources.limits.cpu` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `1000m` **Chart:** `apigee-org` The CPU limit for the resource in a Kubernetes container, in millicores.  
`watcher.resources.limits.memory` | Advanced | **Introduced in version:** 1.11.0 **Default value:** `2Gi` **Chart:** `apigee-org` The memory limit for the resource in a Kubernetes container, in mebibytes.  
`watcher.serviceAccountPath` | Basic | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-org` **Required.** Path to Google Service Account key file with **Apigee Runtime Agent** role.   
`watcher.serviceAccountRef` | Advanced | **Introduced in version:** 1.3.0 **Default value:** None **Chart:** `apigee-org` **One of either serviceAccountPath or serviceAccountRef is required.** A kubernetes secret reference to a Google Service Account key file. See [Storing service account keys in Kubernetes secrets](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/storing-sa-keys-in-k8s-secrets).   
`watcher.tolerations.effect` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `effect` specifies the effect that matching a toleration with a taint will have. Values for `effect` can be:

  * `NoExecute`
  * `NoSchedule`
  * `PreferNoSchedule`

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`watcher.tolerations.key` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `key` identifies pods to which the toleration can be applied. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`watcher.tolerations.operator` | Advanced | **Introduced in version:** 1.10.1 **Default value:** `"Equal"` **Chart:** `apigee-org` Required to use the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `operator` specifies the operation used to trigger the `effect`. Values for `operator` can be:

  * `Equal` matches the value set in `value`.
  * `Exists` ignores the value set in `value`.

See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`watcher.tolerations.tolerationSeconds` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `tolerationSeconds` defines in seconds how long a pod stays bound to a failing or unresponsive node. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
`watcher.tolerations.value` | Advanced | **Introduced in version:** 1.10.1 **Default value:** None **Chart:** `apigee-org` Used by the [Taints and Tolerations feature of Kubernetes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).  `value` is the value that triggers the `effect` when `operator` is set to `Equal`. See [Taints and Tolerations: Concepts](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#concepts) for details.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
  *[KMS]: Key Management Service
  *[KVM]: Key Value Map
  *[JVM]: Java Virtual Machine
  *[GKE]: Google Kubernetes Engine
  *[MART]: Management API for Runtime data
