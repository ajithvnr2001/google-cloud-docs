---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates/
title: Access private registries with private CA certificates \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:18.985782+00:00
---

# Access private registries with private CA certificates  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Access private registries with private CA certificates Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to allow workloads running in Google Kubernetes Engine (GKE) to access private image registries by using the public key of the certificate authority (CA) that issued the certificate for the registry.

This page is for Security specialists who manage access for their organization's workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with [Secret Manager](https://cloud.google.com/security/products/secret-manager).

## How accessing private registries works

You store the public key of the CA used to issue certificates for your private registries in Secret Manager and configure which registry fully-qualified domain names (FQDNs) use that public key for certificate validation. GKE automatically fetches the key and updates the container runtime registry configuration during node bootstrapping. When you deploy a workload that uses a container image from your private registry, the following steps occur:

  1. The kubelet on the node tries to pull the image from the private registry.
  2. The registry presents a server-side TLS certificate.
  3. The container runtime validates the registry certificate cryptographically and to ensure that the FQDN matches what you specified.
  4. If the validation passes, GKE pulls the image and schedules your workload.



## Benefits

This method of accessing private registries provides benefits like the following:

  1. **Improve reliability of container runtime configuration** : Using methods like DaemonSets to set the containerd configuration adds a risk of a race condition occurring, where other DaemonSets might run before your configuration DaemonSet.
  2. **Reduce vulnerability to privilege escalation attacks** : Removes the need to run privileged DaemonSets that modify your container runtime configuration.
  3. **Reduce management overhead** : Secret Manager lets you store CA public keys in a central location; manage access to the keys using IAM; and implement version control and annotations. For more information, see the [Secret Manager product overview](https://cloud.google.com/security/products/secret-manager).
  4. **Improve auditability** : Cloud Logging already collects logs, including when certificates are added to a cluster and when GKE nodes pull images.



## Pricing

In this document, you use the following billable components of Google Cloud:

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Secret Manager](https://cloud.google.com/secret-manager/pricing)
  * [Logging](https://cloud.google.com/stackdriver/pricing#logging-costs): GKE generates Admin Activity audit logs and, if enabled, Data Access audit logs for this feature. For information about the different types of audit logs, see [GKE audit logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging).



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Secret Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com)

  * You must already have a private registry and private CA certificates to access the registry. This guide doesn't cover setting up a private registry or creating certificates.




### Requirements

To use private CA public keys to access private registries, you must meet the following requirements:

  * Your clusters must use GKE version 1.27.3-gke.1700 or later.
  * You must either use a [Container-Optimized OS with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd) node image, which is the default for all GKE clusters, or Ubuntu node images with containerd that are version 1.33.0 or later. Windows Server node images aren't supported.
  * Your node pools must have the `cloud-platform` access scope for your nodes to download the certificates. For more information, see [Default access scopes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#default_access_scopes). This document includes instructions to set the access scope when you create a cluster or node pool.



### Limitations

Consider the following limitations:

  * If GKE can't access the certificate during the node boot process, the node boots without the private CA certificate. Workloads on that node can't access the private registry. To resolve this issue, see [Troubleshoot issues with the container runtime](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime#certificate-not-present-private-registry).
  * You can't use private CA certificates in Ubuntu node images with a version that's earlier than 1.33.0.
  * You can't use private CA certificates in Windows Server nodes.
  * Each cluster supports up to five private CA certificates for private registries.
  * Each certificate can have up to 25 fully-qualified domain names (FQDNs).
  * Each domain can only be used in a single certificate file. However, certificate bundles are supported.
  * Certificates must be [PEM-encoded](https://wikipedia.org/wiki/Privacy-Enhanced_Mail).
  * The server doesn't automatically rotate certificates. For more information, see Rotate your private CA certificates in this document.
  * FQDNs have the following limitations: 
    * The maximum FQDN length is 255 characters, including special characters.
    * FQDNs can only use letters, numbers, and dashes (-).
    * [Punycode](https://wikipedia.org/wiki/Punycode) isn't supported.
    * Wildcard characters aren't supported.



## Migrate from configuration DaemonSets

In GKE Standard clusters, you can deploy privileged DaemonSets to modify your container runtime configuration. This method directly modifies the containerd configuration on each node.

If you use privileged DaemonSets to configure access to private registries, consider the following before you use this document:

  * Storing private CA public keys in Secret Manager only configures _access_ to private registries. Other registry-related configuration isn't supported.
  * Enabling this feature causes your cluster to use containerd's [CRI hostpath configuration model](https://github.com/containerd/containerd/blob/main/docs/hosts.md#cri), which is incompatible with the previous configuration model. If you have any DaemonSets that modify the containerd host configuration, such as for insecure private registries, mirrors, or proxies, update the DaemonSets to use the CRI hostpath model.

For the available fields in the CRI hostpath model, see [Registry configuration](https://github.com/containerd/containerd/blob/main/docs/hosts.md#hoststoml-content-description---detail) in the containerd GitHub repository.

**Note:** If you disable this feature later, your nodes revert to the previous model for registry configuration in containerd. You must modify your DaemonSets to use the previous model. For information about the previous configuration model, see [Configure registry credentials](https://github.com/containerd/containerd/blob/main/docs/cri/registry.md#configure-registry-credentials).



When you enable this feature, GKE applies the CRI hostpath configuration model to _new_ nodes in the cluster. Existing nodes continue to use the previous configuration model until they're recreated during events like upgrades.

### Update DaemonSets to support both configuration models

To reduce the risk of your configuration DaemonSets not working on nodes that support a specific configuration model, ensure that your DaemonSets conditionally use a specific configuration model depending on the containerd configuration files on the node. For an example DaemonSet that implements this conditional logic, in the `GoogleCloudPlatform/k8s-node-tools` GitHub repository, see the [insecure-registry-config.yaml manifest](https://raw.githubusercontent.com/GoogleCloudPlatform/k8s-node-tools/master/containerd/container-insecure-registry/insecure-registry-config.yaml).

## Store your CA public keys in Secret Manager

Store the _public keys_ of your private CAs that issue your private registry certificates as secrets in Secret Manager. For instructions, in the Secret Manager documentation, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

## Configure access to Secret Manager from GKE

To ensure that the cluster's IAM service account has the necessary permissions to pull secrets from Secret Manager, ask your administrator to grant the following IAM roles to the cluster's IAM service account on the secret: 

**Important:** You must grant these roles to the cluster's IAM service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Access secret content: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 
  * Access secret metadata: [Secret Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to pull secrets from Secret Manager. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to pull secrets from Secret Manager:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `secretmanager.secrets.get`
  * `secretmanager.secrets.list`
  * `secretmanager.versions.get`
  * `secretmanager.versions.list`
  * `secretmanager.versions.access`



Your administrator might also be able to give the cluster's IAM service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you didn't associate a custom IAM service account with your cluster or node pool, which is our recommended approach, the cluster uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

**Note:** If you don't use custom IAM service accounts to create your GKE clusters or node pools, ensure that the default Compute Engine service account in your project has the required permissions for GKE. In organizations that enforce the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account won't automatically get the required permissions for GKE. This constraint is enforced by default for organizations that were created on or after May 3, 2024. For details, see [Default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent). 

If possible, we recommend that you configure your clusters and node pools with a minimally privileged IAM service account. For instructions, see [Use least-privileged service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

## Create a runtime configuration file

To enable the ability to use private CA certificates for private registries in GKE, you create a YAML file to modify the containerd configuration.

  1. Get your Google Cloud project number:
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"
         

The output is your numerical project number.

  2. Save the following configuration as `containerd-configuration.yaml`. You could use either `registryHosts` (preferred) or `privateRegistryAccessConfig` field




### registryHosts
    
    
    registryHosts:
    - server: "REGISTRY_SERVER_FQDN"
      hosts:
      - host: "MIRROR_FQDN"
        capabilities:
        - "HOST_CAPABILITY_PULL"
        - "HOST_CAPABILITY_RESOLVE"
        ca:
        - gcpSecretManagerSecretUri: "projects/PROJECT_ID_OR_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION"
    

Replace the following:

  * `REGISTRY_SERVER_FQDN`: the hostname of the registry server. This should be fully-qualified domain names or IPv4 addresses.
  * `MIRROR_FQDN`: the hostname of the registry mirror. This should be fully-qualified domain names or IPv4 addresses.
  * `PROJECT_ID_OR_NUMBER`: the project ID or project number that you got in the previous step.
  * `SECRET_NAME`: the secret name in Secret Manager.
  * `SECRET_VERSION`: the version number of your secret in Secret Manager. You can optionally use a version alias, but we recommend using the version number to avoid management complexity.



For a description of these fields, see [registryHosts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration#registryHosts) in the Available containerd configuration options.

### privateRegistryAccessConfig
    
    
    privateRegistryAccessConfig:
      certificateAuthorityDomainConfig:
      - gcpSecretManagerCertificateConfig:
          secretURI: "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION"
        fqdns:
          - "FQDN1"
          - "FQDN2"
      enabled: true
    

Replace the following:

  * `PROJECT_NUMBER`: the project number that you got in the previous step.
  * `SECRET_VERSION`: the version number of your secret in Secret Manager. You can optionally use a version alias, but we recommend using the version number to avoid management complexity.
  * `FQDN1`, `FQDN2`: the fully-qualified domain names for your private registries. You can also use an IPv4 address if a certificate was issued for that address, but we don't recommend it.

For a description of these fields, see [privateRegistryAccessConfig](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration#privateRegistryAccessConfig) in the Available containerd configuration options.




## Apply containerd configuration to new clusters

This section shows you how to apply a containerd configuration file when you create a new GKE cluster.

Run the following command to create Autopilot clusters:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=LOCATION \
        --scopes="cloud-platform" \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

**Note** : If your configuration file does not use secrets from Secret Manager, such as for the `privateRegistryAccessConfig` feature or when using `registryHosts` with certificates stored in Secret Manager, you can remove the `--scopes="cloud-platform"` flag.

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `LOCATION`: the Compute Engine location of your new cluster.
  * `PATH_TO_CONFIG_FILE`: the path to the configuration file that you created, like `~/containerd-configuration.yaml`.



You can enable the containerd configuration on new Standard clusters by running the `gcloud container clusters create` command with the same options. And unless you specify a different containerd configuration, new node pools that are created in the cluster inherit the cluster-level default containerd configuration.

### Apply containerd configuration to new node pools

You can apply the containerd configuration to a new GKE node pool with following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --scopes="cloud-platform" \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

**Note** : If your configuration file does not use secrets from Secret Manager, such as for the `privateRegistryAccessConfig` feature or when using `registryHosts` with certificates stored in Secret Manager, you can remove the `--scopes="cloud-platform"` flag.

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of the existing cluster.
  * `LOCATION`: the Compute Engine location of your new node pool.
  * `PATH_TO_CONFIG_FILE`: the path to the configuration file that you created, like `~/containerd-configuration.yaml`.



## Apply containerd configuration to existing clusters

This section shows you how to apply a containerd configuration to existing clusters and nodes.

Updating the cluster-level containerd configuration applies only to node pools that don't have their own settings defined at the node pool level (such as `registryHosts` or `writableCgroups`). GKE re-creates the nodes in these node pools to apply the new configuration. Node pools with node pool-level settings continue to use their own configuration and their nodes are not re-created. Updating a cluster or node pool with a containerd configuration re-creates the nodes to apply the configuration. This might cause temporary disruptions in running workloads. GKE only re-creates nodes if automatic upgrades are enabled. This re-creation respects any [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) that you set. In Standard clusters that don't have automatic upgrades enabled, you must manually re-create your nodes to apply the configuration.

### Check access scopes

If your configuration file uses secrets from Secret Manager, your cluster or node pool must have the `cloud-platform` access scope. This section shows you how to check your access scopes and update an existing cluster with a new or modified runtime configuration file.

For details about the default access scopes in new clusters, see [Access scopes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#default_access_scopes).

#### Check Autopilot access scopes

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=nodeConfig \
        --format='csv[delimiter="\\n",no-heading](oauthScopes)'

If you are using secrets from Secret Manager and your cluster doesn't have the `https://www.googleapis.com/auth/cloud-platform` access scope, create a new cluster with this access scope.

#### Check Standard access scopes

To check your Standard cluster access scopes, check a node pool:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --format='value[delimiter="\\n"](config.oauthScopes)'

Replace `NODE_POOL_NAME` with the name of the node pool.

If you are using secrets from Secret Manager and your cluster doesn't have the `https://www.googleapis.com/auth/cloud-platform` access scope, create a new node pool with the `cloud-platform` access scope and delete your existing node pool.

### Update the cluster to use your configuration file

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

### Update a node pool to use a configuration file

To update the containerd configuration for a node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool that you want to update.
  * `CLUSTER_NAME`: the name of the existing cluster.
  * `LOCATION`: the Compute Engine location of the cluster.
  * `PATH_TO_CONFIG_FILE`: the path to the configuration file that you created, like `~/containerd-configuration.yaml`.



### Re-create nodes in Standard clusters

If your Standard cluster doesn't use automatic upgrades, you must manually re-create your node pools to apply the new configuration. To trigger a manual node re-creation, upgrade your cluster to the same GKE version that it already uses.
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
        --location=LOCATION \
        --cluster-version=VERSION

Replace `VERSION` with the same GKE patch version that the cluster already uses.

## Verify that your cluster can access the private registry

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten="nodePoolDefaults.nodeConfigDefaults.containerdConfig"
    

The output is similar to the following:

### registryHosts
    
    
    containerdConfig:
      registryHosts:
      - server: example.io
        hosts:
        - host: example.mirror.io
          capabilities:
          - "HOST_CAPABILITY_PULL"
          - "HOST_CAPABILITY_RESOLVE"
          ca:
          - gcpSecretManagerSecretUri: projects/123456789012/secrets/example-secret-name/versions/1
    

### privateRegistryAccessConfig
    
    
    containerdConfig:
      privateRegistryAccessConfig:
        certificateAuthorityDomainConfig:
        - fqdns:
          - 203.0.113.105
          gcpSecretManagerCertificateConfig:
            secretUri: projects/123456789012/secrets/example-secret-name/versions/1
        enabled: true
    

## Deploy a workload that accesses a private image

In this section, you deploy a static Pod that references an image from your private registry.

  1. Save the following manifest as `private-registry-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: private-registry-pod
         spec:
           containers:
           - name: private-image
             image: IMAGE_NAME
         

Replace `IMAGE_NAME` with your private image name.

  2. Deploy the Pod:
         
         kubectl create -f private-registry-pod.yaml
         




## Rotate your private CA certificates

Secret Manager and GKE can't automatically rotate private CA certificates in Secret Manager. To perform a certificate rotation, do the following steps. These steps require that you recreate existing nodes twice. We recommend that you perform certificate rotations during scheduled downtime to minimize the impact of workload disruptions.

  1. Create a PEM-encoded certificate bundle that contains both your old and new certificates.
  2. [Add the bundle as a new secret version in Secret Manager](https://docs.cloud.google.com/secret-manager/docs/add-secret-version).
  3. Update your runtime configuration file `secretURI` field with the new secret version number.
  4. Update your cluster to use the new secret version.
  5. Get the timestamp of the update operation:
         
         gcloud container operations list \
             --filter="operationType ~ UPDATE_CLUSTER AND targetLink ~ CLUSTER_NAME" \
             --sort-by=startTime \
             --limit=1 \
             --format='value(endTime)'
         

The output is similar to the following:
         
         2024-01-31T09:27:30.864308964Z
         

  6. Look for nodes that were created before the update operation ended:
         
         kubectl get nodes -o json | jq ".items[] |
         select(.metadata.creationTimestamp | fromdateiso8601 < $(date -d
         CLUSTER_UPDATE_TIMESTAMP +%s)) | .metadata.name"
         

Replace `CLUSTER_UPDATE_TIMESTAMP` with the timestamp from the previous step.

The output is a list of node names that haven't been recreated with the updated configuration. When the output is **blank** , proceed to the next step.

  7. Create a new version of your secret in Secret Manager with only the new certificate.

  8. Repeat the previous steps to update your cluster, get the operation timestamp, and verify that your nodes use the new secret version.

  9. Delete the old secret version from Secret Manager.




## View audit logs in Logging

This section shows you how to use Logging to check whether GKE installed your secret version on your nodes.

If downloadinging secret fails, nodes will have two conditions set: `PrivateCA4CRUserConfigError` or `PrivateCA4CRInternalError` depending on error types. And you could check Logging message for detailed errors.

  1. Go to the **Logs Explorer** page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Search logs with specific queries:




### registryHosts

Query the logs with following filter.
    
    
    resource.type="gce_instance"
    (textPayload:"Successfully fetched secret" OR textPayload:"error pulling certificate")
    

If your certificate installation succeeded, you could find following log entry:
    
    
    Successfully fetched secret "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION"
    Successfully wrote secret payload for "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION"
    

If your certificate installation failed, you could find following log entry:
    
    
    User error pulling certificate "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION" from GSM: ...
    Or
    Internal error pulling certificate "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION" from GSM: ....
    

### privateRegistryAccessConfig

Query the logs with following filter.
    
    
    resource.type="gce_instance"
    textPayload:"Installed certificate \\\"projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION\\\""
    

If your certificate installation succeeded, the output is similar to the following:
    
    
    "Installed certificate "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION""
    

If your certificate installation failed, the output is similar to the following:
    
    
    "Failed to install certificate "projects/PROJECT_NUMBER/secrets/SECRET_NAME/versions/SECRET_VERSION""
    

## Best practices

We recommend that you use the following best practices when you use this feature:

  * Don't use aliases for Secret Manager secret versions. Use the auto-generated version number for each secret version. An alias might point to a different certificate version over time, which might cause complexities in tracking the specific versions that your workloads use.
  * Use [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to control when GKE can recreate your nodes to apply updated containerd configurations.
  * Provide access to secrets at the secret level, not at the project level.



## Disable containerd configuration options

### Disable `privateRegistryAccessConfig`

  1. Update your configuration file to specify `enabled: false` in `privateRegistryAccessConfig` and delete any other fields in the item, like in the following example:
         
         privateRegistryAccessConfig:
           **enabled : false**

  2. Apply the updated configuration file to your cluster. For instructions, see [Apply containerd configuration to existing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration#containerd-configuration-existing-clusters).



### Disable `registryHosts`

  1. Update your configuration file to specify an empty array in the `registryHosts` item, like in the following example:
         
         registryHosts: []

  2. Apply the updated configuration file to your cluster. For instructions, see [Apply containerd configuration to existing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration#containerd-configuration-existing-clusters).



## Troubleshoot

For troubleshooting steps, see [Troubleshooting the container runtime](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime#troubleshoot-private-registries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
