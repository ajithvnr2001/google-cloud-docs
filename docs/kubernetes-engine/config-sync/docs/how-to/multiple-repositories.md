---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories/
title: Configure syncing from more than one source of truth \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:21.652470+00:00
---

# Configure syncing from more than one source of truth  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Configure syncing from more than one source of truth Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure more than one root and namespace-scoped source of truth by creating [RootSync and RepoSync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields) objects.

Having a root source of truth lets you sync [cluster-scoped](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects) and [namespace-scoped](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects) configs. A root source of truth can use admin-level credentials to enforce policies on application namespaces and override local changes that drift from the state that you declared in your configs. A central administrator typically governs the root sources of truth.

Namespace-scoped sources of truth are optional and can contain namespace-scoped configs synced to a particular namespace across clusters. You can delegate the setup and control of a namespace-scoped source of truth to non-administrative users. Although Config Sync automatically detects changes from the source of truth, you can add an extra layer of drift detection by adding an admission webhook to a namespace-scoped source of truth. For details on how to do this, see [Prevent config drift](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift).

## Before you begin

  * Create, or make sure you have access to, an [unstructured](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo) source of truth that can contain the configs that Config Sync syncs to. Config Sync supports Git repositories, Helm charts, and OCI images as the source of truth. Namespace-scoped sources of truth must use the unstructured format.
  * Create, or make sure you have access to, a cluster that is on a Google Kubernetes Engine [supported platform and version](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support) and meets the [requirements for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#cluster-requirements).



### Create a RoleBinding

A RoleBinding is required to grant permissions to the `RepoSync` that you create in this guide. To create the RoleBinding, complete the following steps:

  1. In the root source, declare a `RoleBinding` configuration that grants the `SERVICE_ACCOUNT_NAME` service account permission to manage objects in the namespace. Config Sync automatically creates the `SERVICE_ACCOUNT_NAME` service account when the RepoSync config is synced to the cluster.

A `RoleBinding` may reference a `Role` in the same namespace. Alternatively, a `RoleBinding` can reference a `ClusterRole` and bind that `ClusterRole` to the namespace of the `RoleBinding`. While you should adhere to the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) by granting fine-grained permissions to a user-defined `Role`, you can define a `ClusterRole` or use [user-facing roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles), and reference the same `ClusterRole` in multiple `RoleBindings` across different namespaces.

**Note:** A `RoleBinding` referencing a `ClusterRole` only gives you access to the namespace of the `RoleBinding`, but not cluster-wide access.

### Default ClusterRoles

Save the `RoleBinding` manifest that references a default `ClusterRole`, for example `admin` or `edit`, as `FILENAME`:
         
         kind: RoleBinding
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: syncs-repo
           namespace: NAMESPACE
         subjects:
         - kind: ServiceAccount
           name: SERVICE_ACCOUNT_NAME
           namespace: config-management-system
         roleRef:
           kind: ClusterRole
           name: CLUSTERROLE_NAME
           apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `FILENAME`: the name for the RoleBinding manifest.
     * `NAMESPACE`: add the name of your namespace.
     * `SERVICE_ACCOUNT_NAME`: add the name of the reconciler's service account. If the RepoSync name is `repo-sync`, `SERVICE_ACCOUNT_NAME` is `ns-reconciler-NAMESPACE`. Otherwise, it is `ns-reconciler-NAMESPACE-REPO_SYNC_NAME-REPO_SYNC_NAME_LENGTH`. For example, if your RepoSync name is `prod`, then the `SERVICE_ACCOUNT_NAME` would be `ns-reconciler-NAMESPACE-prod-4`. The integer `4` is used as `prod` contains 4 characters.
     * `CLUSTERROLE_NAME`: add the name of the default ClusterRole.

### User-defined roles

You can declare a `ClusterRole` or a `Role` by granting a list of permissions to each resource that is managed by the `RepoSync` object. This allows for fine-grained permissions. See [referring to resources](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources) for more details.

For example, the following `ClusterRole` or `Role` grants permissions to manage `Deployment` and `ServiceAccount` objects:
    
    # ROOT_REPO/namespaces/NAMESPACE/sync-role.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ROLE_KIND
    metadata:
      namespace: NAMESPACE # only set this field for a 'Role'
      name: RECONCILER_ROLE
    rules:
    # Update 'apiGroups' and 'resources' to reference actual resources managed by 'RepoSync'.
    - apiGroups: ["apps"]
      resources: ["deployments"]
      verbs: ["*"]
    - apiGroups: [""]
      resources: ["serviceaccounts"]
      verbs: ["*"]
    

Save the `RoleBinding` manifest that references the `ClusterRole` or `Role` as `FILENAME`:
    
    # ROOT_REPO/namespaces/NAMESPACE/FILENAME.yaml
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: syncs-repo
      namespace: NAMESPACE
    subjects:
    - kind: ServiceAccount
      name: SERVICE_ACCOUNT_NAME
      namespace: config-management-system
    roleRef:
      kind: ROLE_KIND
      name: RECONCILER_ROLE
      apiGroup: rbac.authorization.k8s.io
    

Replace the following:

     * `FILENAME`: the name for the RoleBinding manifest.
     * `ROLE_KIND`: set `ClusterRole` or `Role`.
     * `NAMESPACE`: add the name of your namespace.
     * `SERVICE_ACCOUNT_NAME`: add the name of the reconciler's service account. If the RepoSync name is `repo-sync`, `SERVICE_ACCOUNT_NAME` is `ns-reconciler-NAMESPACE`. Otherwise, it is `ns-reconciler-NAMESPACE-REPO_SYNC_NAME-REPO_SYNC_NAME_LENGTH`. For example, if your RepoSync name is `prod`, then the `SERVICE_ACCOUNT_NAME` would be `ns-reconciler-NAMESPACE-prod-4`. The integer `4` is used as `prod` contains 4 characters.
     * `RECONCILER_ROLE`: add the name of the `ClusterRole` or `Role`.

  2. Apply the RoleBinding:
         
         kubectl apply -f FILENAME
         




## Limitations

  * [`NamespaceSelectors`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors) (including annotations pointing to Selectors) only work in a root source of truth.
  * If you [installed Config Sync using the Google Cloud console or Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync), Config Sync automatically created a RootSync object named `root-sync`. Because of this, you can't name any of your RootSync objects `root-sync`.



## Choose your preferred configuration method

Choose between one of the two methods for configuring your sources:

  * **Control sources in a root source of truth**. This method centralizes all configuration of a source of truth in another source of truth, allowing a central administrator complete control of the setup.

  * **Control sources with the Kubernetes API**. Use this method if you want to delegate control of your source of truth to different owners.




## Control sources in a root source of truth

To control sources with a root source, you need a RoleBinding to authorize access. If you don't have one, see the Create a RoleBinding section.

### Control root sources in a root source of truth

Config Sync supports syncing from more than one source of truth. The central administrator can use a root source of truth to manage all other sources. Because Config Sync manages the RootSync objects, this method prevents any local changes to RootSync configurations in the cluster.

To use this method, complete the following tasks:

  1. Save one of the following manifests as `root-sync.yaml`. Use the manifest version that corresponds to the source type for your configs.

### Git
         
         # root-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceType: git
           sourceFormat: unstructured
           git:
             repo: ROOT_REPOSITORY
             revision: ROOT_REVISION
             branch: ROOT_BRANCH
             dir: ROOT_DIRECTORY
             auth: ROOT_AUTH_TYPE
             gcpServiceAccountEmail: ROOT_EMAIL
             secretRef:
               name: ROOT_SECRET_NAME
             noSSLVerify: ROOT_NO_SSL_VERIFY
             caCertSecretRef:
               name: ROOT_CA_CERT_SECRET_NAME
         

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_REPOSITORY`: add the URL of the Git repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `ROOT_REVISION`: add the Git revision (tag or hash) or branch to sync from. This field is optional and the default value is `HEAD`. When using a hash, it must be a full hash, and not an abbreviated form.
     * `ROOT_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`. We recommend using the `revision` field to specify a branch name for simplicity. If both the `revision` field and the `branch` field are specified, `revision` takes precedence over `branch`.
     * `ROOT_DIRECTORY`: add the path in the Git repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_SECRET_NAME`: add the name of your Secret. If this field is set, you must add the Secret's public key to the Git provider. This field is optional.

     * `ROOT_NO_SSL_VERIFY`: To disable the SSL certificate verification, set this field to `true`. The default value is `false`.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Git provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses Git as the source.

### OCI
    
    # root-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: ROOT_SYNC_NAME
      namespace: config-management-system
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: ROOT_IMAGE
        dir: ROOT_DIRECTORY
        auth: ROOT_AUTH_TYPE
        gcpServiceAccountEmail: ROOT_EMAIL
        caCertSecretRef:
          name: ROOT_CA_CERT_SECRET_NAME
    

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_IMAGE`: the URL of the OCI image to use as the root repository, for example `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`: 
       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`**. Other formats (for example, `tar+bz2`) will not be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `ROOT_DIRECTORY`: add the path in the repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your OCI provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses an OCI image as the source.

### Helm
    
    # root-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: ROOT_SYNC_NAME
      namespace: config-management-system
    spec:
      sourceType: helm
      sourceFormat: unstructured
      helm:
        repo: ROOT_HELM_REPOSITORY
        chart: HELM_CHART_NAME
        version: HELM_CHART_VERSION
        releaseName: HELM_RELEASE_NAME
        namespace: HELM_RELEASE_NAMESPACE
        values:
          foo:
            bar: VALUE_1
          baz:
          - qux: VALUE_2
            xyz: VALUE_3
        includeCRDs: HELM_INCLUDE_CRDS
        auth: ROOT_AUTH_TYPE
          gcpServiceAccountEmail: ROOT_EMAIL
          secretRef:
            name: ROOT_SECRET_NAME
        caCertSecretRef:
          name: ROOT_CA_CERT_SECRET_NAME
    

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_HELM_REPOSITORY`: the URL of the Helm repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `HELM_CHART_NAME`: add the name of your Helm chart. This field is required.
     * `HELM_CHART_VERSION`: the version of your chart. This field is optional. If no value is specified, the latest version is used.
     * `HELM_RELEASE_NAME`: the name of the Helm release. This field is optional.
     * `HELM_RELEASE_NAMESPACE`: the target namespace for a release. It only sets a namespace for resources that contain `namespace: {{ .Release.Namespace }}` in their templates. This field is optional. If no value is specified, the default namespace `config-management-system` is used.
     * `HELM_INCLUDE_CRDS`: set to `true` if you want the Helm template to also generate a CustomResourceDefinition. This field is optional. If no value is specified, the default is `false` and a CRD won't be generated.
     * `VALUE`: values to use instead of default values that accompany the Helm chart. Format this field the same way as [helm chart's values.yaml](https://helm.sh/docs/chart_best_practices/values/) file. This field is optional.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `token`: Use a username and password to access a private Helm repository.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_SECRET_NAME`: add the [name of your Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#helm-access) if `token` is the `ROOT_AUTH_TYPE`. This field is optional.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Helm provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses Helm as the source.

  2. Commit the changes to the root source of truth:
         
         git add .
          git commit -m 'Setting up a new root source of truth.'
          git push
         

  3. You can repeat the above steps if you need to configure multiple root sources. You can also store configurations of multiple RootSync objects in a root source of truth synced by another RootSync object, to manage multiple RootSync objects centrally in a GitOps fashion.




### Control namespace-scoped objects in a root source of truth

Namespace-scoped sources of truth can be managed by a root source of truth. Because the namespace-scoped sources are managed by Config Sync, this method prevents any local changes to the namespace-scoped source definitions.

To use this method, complete the following tasks:

  1. In the root source of truth, declare a `namespace` configuration:
         
         # ROOT_SOURCE/namespaces/NAMESPACE/namespace.yaml
         apiVersion: v1
         kind: Namespace
         metadata:
           name: NAMESPACE
         

Replace `NAMESPACE` with a name for your namespace.

  2. In the root source of truth, create one of the following `RepoSync` objects in the same namespace. Use the manifest that corresponds to the source type for your configs:

### Git
         
         #ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RepoSync
         metadata:
           name: REPO_SYNC_NAME
           namespace: NAMESPACE
         spec:
           sourceType: git
           sourceFormat: unstructured
           git:
             repo: NAMESPACE_REPOSITORY
             revision: NAMESPACE_REVISION
             branch: NAMESPACE_BRANCH
             dir: "NAMESPACE_DIRECTORY"
             auth: NAMESPACE_AUTH_TYPE
             gcpServiceAccountEmail: NAMESPACE_EMAIL
             secretRef:
               name: NAMESPACE_SECRET_NAME
             noSSLVerify: NAMESPACE_NO_SSL_VERIFY
             caCertSecretRef:
               name: NAMESPACE_CA_CERT_SECRET_NAME
         

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_REPOSITORY`: add the URL of the Git repository to use as the namespace repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. If you don't enter a protocol, the URL is treated as an HTTPS URL. This field is required.
     * `NAMESPACE_REVISION`: add the Git revision (tag or hash) or branch to sync from. This field is optional and the default value is `HEAD`. When using a hash, it must be a full hash, and not an abbreviated form.
     * `NAMESPACE_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`. We recommend using the `revision` field to specify a branch name for simplicity. If both the `revision` field and the `branch` field are specified, `revision` takes precedence over `branch`.
     * `NAMESPACE_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a repository in Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a repository in Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `NAMESPACE_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_SECRET_NAME`: add the name you intend to give your Secret. This field is optional.

     * `NAMESPACE_NO_SSL_VERIFY`: To disable the SSL certificate verification, set this field to `true`. The default value is `false`.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Git provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### OCI
    
    # ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    metadata:
      name: REPO_SYNC_NAME
      namespace: NAMESPACE
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: NAMESPACE_IMAGE
        dir: NAMESPACE_DIRECTORY
        auth: NAMESPACE_AUTH_TYPE
        gcpServiceAccountEmail: NAMESPACE_EMAIL
        caCertSecretRef:
          name: NAMESPACE_CA_CERT_SECRET_NAME
    

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_IMAGE`: the URL of the OCI image to use as the namespace source, for example `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`:

       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`**. Other formats (for example, `tar+bz2`) will not be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `NAMESPACE_DIRECTORY`: add the path in the source to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the source.

     * `NAMESPACE_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your OCI provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### Helm
    
    # ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    metadata:
      name: REPO_SYNC_NAME
      namespace: NAMESPACE
    spec:
      sourceType: helm
      sourceFormat: unstructured
      helm:
        repo: NAMESPACE_REPOSITORY
        chart: HELM_CHART_NAME
        version: HELM_CHART_VERSION
        releaseName: HELM_RELEASE_NAME
        namespace: HELM_RELEASE_NAMESPACE
        values:
          foo:
            bar: VALUE_1
          baz:
          - qux: VALUE_2
            xyz: VALUE_3
        includeCRDs: HELM_INCLUDE_CRDS
        auth: NAMESPACE_AUTH_TYPE
          gcpServiceAccountEmail: NAMESPACE_EMAIL
          secretRef:
            name: NAMESPACE_SECRET_NAME
        caCertSecretRef:
          name: NAMESPACE_CA_CERT_SECRET_NAME
    

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_REPOSITORY`: the URL of the Helm repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `HELM_CHART_NAME`: add the name of your Helm chart. This field is required.
     * `HELM_CHART_VERSION`: the version of your chart. This field is optional. If no value is specified, the latest version is used.
     * `HELM_RELEASE_NAME`: the name of the Helm release. This field is optional.
     * `HELM_RELEASE_NAMESPACE`: the target namespace for a release. It only sets a namespace for resources that contain `namespace: {{ .Release.Namespace }}` in their templates. This field is optional. If no value is specified, the default namespace `config-management-system` is used.
     * `HELM_INCLUDE_CRDS`: set to `true` if you want the Helm template to also generate a CustomResourceDefinition. This field is optional. If no value is specified, the default is `false` and a CRD won't be generated.
     * `VALUE`: values to use instead of default values that accompany the Helm chart. Format this field the same way as [helm chart's values.yaml](https://helm.sh/docs/chart_best_practices/values/) file. This field is optional.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `token`: Use a username and password to access a private Helm repository.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_SECRET_NAME`: add the [name of your Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl#helm-access) if `token` is the `ROOT_AUTH_TYPE`. This field is optional.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Helm provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

  3. If you are using `gcpserviceaccount` as the auth type and don't have Workload Identity Federation for GKE enabled, you must create an [IAM policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) between the Kubernetes service account for _each_ namespace and the Google service account. See [Grant access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret) for instructions on how to create this binding.

  4. Commit the changes to the root source of truth:
         
         git add .
          git commit -m 'Setting up a new namespace-scoped source of truth.'
          git push
         

  5. If required, [create a Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret) based on your preferred authentication method. If you used `none` as your authentication type, you can skip this step.

The Secret must meet following requirements:

     * Create the Secret in the same namespace as the RepoSync.
     * The Secret's name must match the `spec.git.secretRef` name you defined in `repo-sync.yaml`.
     * You must add the Secret's public key to the Git provider.
  6. To verify the configuration, use `kubectl get` on one of the objects in the namespace source. For example:
         
         kubectl get rolebindings -n NAMESPACE
         

  7. You can repeat the above steps if you need to configure more than one namespace-scoped source.




### Control namespace-scoped sources in a namespace-scoped source

Config Sync supports syncing from more than one namespace-scoped source of truth per namespace. Namespace-scoped sources of truth can be managed in a namespace-scoped source of truth in the same namespace.

To use this method, complete the following tasks:

  1. In the namespace-scoped source of truth, create one of the following `RepoSync` objects in the same namespace. Use the manifest that corresponds to the source type for your configs:

### Git
         
         #ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RepoSync
         metadata:
           name: REPO_SYNC_NAME
           namespace: NAMESPACE
         spec:
           sourceType: git
           sourceFormat: unstructured
           git:
             repo: NAMESPACE_REPOSITORY
             revision: NAMESPACE_REVISION
             branch: NAMESPACE_BRANCH
             dir: "NAMESPACE_DIRECTORY"
             auth: NAMESPACE_AUTH_TYPE
             gcpServiceAccountEmail: NAMESPACE_EMAIL
             secretRef:
               name: NAMESPACE_SECRET_NAME
             noSSLVerify: NAMESPACE_NO_SSL_VERIFY
             caCertSecretRef:
               name: NAMESPACE_CA_CERT_SECRET_NAME
         

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_REPOSITORY`: add the URL of the Git repository to use as the namespace repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. If you don't enter a protocol, the URL is treated as an HTTPS URL. This field is required.
     * `NAMESPACE_REVISION`: add the Git revision (tag or hash) or branch to sync from. This field is optional and the default value is `HEAD`. When using a hash, it must be a full hash, and not an abbreviated form.
     * `NAMESPACE_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`. We recommend using the `revision` field to specify a branch name for simplicity. If both the `revision` field and the `branch` field are specified, `revision` takes precedence over `branch`.
     * `NAMESPACE_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a repository in Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a repository in Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `NAMESPACE_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_SECRET_NAME`: add the name you intend to give your Secret. This field is optional.

     * `NAMESPACE_NO_SSL_VERIFY`: To disable the SSL certificate verification, set this field to `true`. The default value is `false`.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Git provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### OCI
    
    # ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    metadata:
      name: REPO_SYNC_NAME
      namespace: NAMESPACE
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: NAMESPACE_IMAGE
        dir: NAMESPACE_DIRECTORY
        auth: NAMESPACE_AUTH_TYPE
        gcpServiceAccountEmail: NAMESPACE_EMAIL
        caCertSecretRef:
          name: NAMESPACE_CA_CERT_SECRET_NAME
    

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_IMAGE`: the URL of the OCI image to use as the namespace source, for example `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`:

       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`**. Other formats (for example, `tar+bz2`) will not be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `NAMESPACE_DIRECTORY`: add the path in the source to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the source.

     * `NAMESPACE_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your OCI provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### Helm
    
    # ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    metadata:
      name: REPO_SYNC_NAME
      namespace: NAMESPACE
    spec:
      sourceType: helm
      sourceFormat: unstructured
      helm:
        repo: NAMESPACE_REPOSITORY
        chart: HELM_CHART_NAME
        version: HELM_CHART_VERSION
        releaseName: HELM_RELEASE_NAME
        namespace: HELM_RELEASE_NAMESPACE
        values:
          foo:
            bar: VALUE_1
          baz:
          - qux: VALUE_2
            xyz: VALUE_3
        includeCRDs: HELM_INCLUDE_CRDS
        auth: NAMESPACE_AUTH_TYPE
          gcpServiceAccountEmail: NAMESPACE_EMAIL
          secretRef:
            name: NAMESPACE_SECRET_NAME
        caCertSecretRef:
          name: NAMESPACE_CA_CERT_SECRET_NAME
    

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_REPOSITORY`: the URL of the Helm repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `HELM_CHART_NAME`: add the name of your Helm chart. This field is required.
     * `HELM_CHART_VERSION`: the version of your chart. This field is optional. If no value is specified, the latest version is used.
     * `HELM_RELEASE_NAME`: the name of the Helm release. This field is optional.
     * `HELM_RELEASE_NAMESPACE`: the target namespace for a release. It only sets a namespace for resources that contain `namespace: {{ .Release.Namespace }}` in their templates. This field is optional. If no value is specified, the default namespace `config-management-system` is used.
     * `HELM_INCLUDE_CRDS`: set to `true` if you want the Helm template to also generate a CustomResourceDefinition. This field is optional. If no value is specified, the default is `false` and a CRD won't be generated.
     * `VALUE`: values to use instead of default values that accompany the Helm chart. Format this field the same way as [helm chart's values.yaml](https://helm.sh/docs/chart_best_practices/values/) file. This field is optional.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `token`: Use a username and password to access a private Helm repository.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_SECRET_NAME`: add the [name of your Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl#helm-access) if `token` is the `ROOT_AUTH_TYPE`. This field is optional.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Helm provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

  2. If you are using `gcpserviceaccount` as the auth type and don't have Workload Identity Federation for GKE enabled, you must create an [IAM policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) between the Kubernetes service account for _each_ namespace and the Google service account. See [Grant access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret) for instructions on how to create this binding.

  3. Commit the changes to the root source of truth:
         
         git add .
          git commit -m 'Setting up a new namespace-scoped source of truth.'
          git push
         

  4. If required, [create a Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret) based on your preferred authentication method. If you used `none` as your authentication type, you can skip this step.

The Secret must meet following requirements:

     * Create the Secret in the same namespace as the RepoSync.
     * The Secret's name must match the `spec.git.secretRef` name you defined in `repo-sync.yaml`.
     * You must add the Secret's public key to the Git provider.
  5. To verify the configuration, use `kubectl get` on one of the objects in the namespace-scoped source of truth. For example:
         
         kubectl get rolebindings -n NAMESPACE
         

  6. You can repeat the above steps if you need to configure more than one namespace-scoped source.




## Control a source of truth with the Kubernetes API

In this method, the central administrator delegates declaration of other `RootSync` objects to other administrators. For `RepoSync` objects, the central administrator only declares the namespace in the root source of truth and delegates declaration of the `RepoSync` object to the application operator.

### Control more than one root source of truth

Other administrators can control a root source of truth by completing the following tasks:

  1. Save one of the following manifests as `root-sync.yaml`. Use the manifest version that corresponds to the source type for your configs.

### Git
         
         # root-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceType: git
           sourceFormat: unstructured
           git:
             repo: ROOT_REPOSITORY
             revision: ROOT_REVISION
             branch: ROOT_BRANCH
             dir: ROOT_DIRECTORY
             auth: ROOT_AUTH_TYPE
             gcpServiceAccountEmail: ROOT_EMAIL
             secretRef:
               name: ROOT_SECRET_NAME
             noSSLVerify: ROOT_NO_SSL_VERIFY
             caCertSecretRef:
               name: ROOT_CA_CERT_SECRET_NAME
         

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_REPOSITORY`: add the URL of the Git repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `ROOT_REVISION`: add the Git revision (tag or hash) or branch to sync from. This field is optional and the default value is `HEAD`. When using a hash, it must be a full hash, and not an abbreviated form.
     * `ROOT_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`. We recommend using the `revision` field to specify a branch name for simplicity. If both the `revision` field and the `branch` field are specified, `revision` takes precedence over `branch`.
     * `ROOT_DIRECTORY`: add the path in the Git repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_SECRET_NAME`: add the name of your Secret. If this field is set, you must add the Secret's public key to the Git provider. This field is optional.

     * `ROOT_NO_SSL_VERIFY`: To disable the SSL certificate verification, set this field to `true`. The default value is `false`.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Git provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses Git as the source.

### OCI
    
    # root-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: ROOT_SYNC_NAME
      namespace: config-management-system
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: ROOT_IMAGE
        dir: ROOT_DIRECTORY
        auth: ROOT_AUTH_TYPE
        gcpServiceAccountEmail: ROOT_EMAIL
        caCertSecretRef:
          name: ROOT_CA_CERT_SECRET_NAME
    

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_IMAGE`: the URL of the OCI image to use as the root repository, for example `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`: 
       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`**. Other formats (for example, `tar+bz2`) will not be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `ROOT_DIRECTORY`: add the path in the repository to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the repository.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your OCI provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses an OCI image as the source.

### Helm
    
    # root-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: ROOT_SYNC_NAME
      namespace: config-management-system
    spec:
      sourceType: helm
      sourceFormat: unstructured
      helm:
        repo: ROOT_HELM_REPOSITORY
        chart: HELM_CHART_NAME
        version: HELM_CHART_VERSION
        releaseName: HELM_RELEASE_NAME
        namespace: HELM_RELEASE_NAMESPACE
        values:
          foo:
            bar: VALUE_1
          baz:
          - qux: VALUE_2
            xyz: VALUE_3
        includeCRDs: HELM_INCLUDE_CRDS
        auth: ROOT_AUTH_TYPE
          gcpServiceAccountEmail: ROOT_EMAIL
          secretRef:
            name: ROOT_SECRET_NAME
        caCertSecretRef:
          name: ROOT_CA_CERT_SECRET_NAME
    

Replace the following:

     * `ROOT_SYNC_NAME`: add the name of your RootSync object.
     * `ROOT_HELM_REPOSITORY`: the URL of the Helm repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `HELM_CHART_NAME`: add the name of your Helm chart. This field is required.
     * `HELM_CHART_VERSION`: the version of your chart. This field is optional. If no value is specified, the latest version is used.
     * `HELM_RELEASE_NAME`: the name of the Helm release. This field is optional.
     * `HELM_RELEASE_NAMESPACE`: the target namespace for a release. It only sets a namespace for resources that contain `namespace: {{ .Release.Namespace }}` in their templates. This field is optional. If no value is specified, the default namespace `config-management-system` is used.
     * `HELM_INCLUDE_CRDS`: set to `true` if you want the Helm template to also generate a CustomResourceDefinition. This field is optional. If no value is specified, the default is `false` and a CRD won't be generated.
     * `VALUE`: values to use instead of default values that accompany the Helm chart. Format this field the same way as [helm chart's values.yaml](https://helm.sh/docs/chart_best_practices/values/) file. This field is optional.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `token`: Use a username and password to access a private Helm repository.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `ROOT_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `ROOT_SECRET_NAME`: add the [name of your Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#helm-access) if `token` is the `ROOT_AUTH_TYPE`. This field is optional.

     * `ROOT_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Helm provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

This manifest creates a `RootSync` object that uses Helm as the source.

  2. Apply the changes:
         
         kubectl apply -f root-sync.yaml
         

  3. You can repeat the above steps if you need to configure more than one root source of truth.




### Control namespace-scoped sources of truth

#### Central administrator tasks

The central administrator completes the following tasks:

  1. In the root source of truth, declare a `namespace` configuration for namespace-scoped sources.
         
         # ROOT_REPO/namespaces/NAMESPACE/namespace.yaml
          apiVersion: v1
          kind: Namespace
          metadata:
            name: NAMESPACE
         

Replace `NAMESPACE` with a name for your namespace.

  2. In the root source of truth, declare a `RoleBinding` to give the application operators permissions. Use [RBAC escalation prevention](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping) to ensure that the application operator cannot later apply a role binding with permissions not granted by this role binding.

To declare the RoleBinding, create the following manifest:
         
         # ROOT_REPO/namespaces/NAMESPACE/operator-rolebinding.yaml
          kind: RoleBinding
          # Add RBAC escalation prevention
          apiVersion: rbac.authorization.k8s.io/v1
          metadata:
            name: operator
            namespace: NAMESPACE
          subjects:
          - kind: User
            name: USERNAME
            apiGroup: rbac.authorization.k8s.io
          roleRef:
            kind: ClusterRole
            name: OPERATOR_ROLE
            apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `NAMESPACE`: add the namespace you created in the root source of truth.
     * `USERNAME`: add the username of the application operator.
     * `OPERATOR_ROLE`: as the central administrator, you can set `OPERATOR_ROLE` to enforce what kinds of configurations can be synced from the namespace-scoped source. You can choose one of the following roles:

       * A default ClusterRole:

         * `admin`
         * `edit`

To learn more, see [User-facing roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles).

       * A user-defined ClusterRole or Role declared in the root source of truth. This role allows for fine grained permissions.

  3. Commit the changes to the root source of truth:
         
         git add .
          git commit -m 'Setting up new namespace-scoped source of truth.'
          git push
         




#### Application operator tasks

The application operator can control namespace-scoped sources by completing the following tasks:

  1. Declare a `RoleBinding` configuration that grants the auto-provisioned `SERVICE_ACCOUNT_NAME` service account permission to manage objects in the namespace. Config Sync automatically creates the `SERVICE_ACCOUNT_NAME` service account when the `RepoSync` config is synced to the cluster.

To declare the RoleBinding, create the following manifest:
         
         # sync-rolebinding.yaml
         kind: RoleBinding
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: syncs-repo
           namespace: NAMESPACE
         subjects:
         - kind: ServiceAccount
           name: SERVICE_ACCOUNT_NAME
           namespace: config-management-system
         roleRef:
           kind: ClusterRole
           name: RECONCILER_ROLE
           apiGroup: rbac.authorization.k8s.io
         

Replace the following:

     * `NAMESPACE`: add the namespace you created in the root source of truth.
     * `SERVICE_ACCOUNT_NAME`: add the name of the reconciler's service account. If the RepoSync name is `repo-sync`, `SERVICE_ACCOUNT_NAME` is `ns-reconciler-NAMESPACE`. Otherwise, it is `ns-reconciler-NAMESPACE-REPO_SYNC_NAME`.
     * `RECONCILER_ROLE`: as the application operator you can set `RECONCILER_ROLE` to enforce what kinds of configuration can be synced from the namespace-scoped source. You can only further restrict the set of permissions the central administrator has granted you. As a result, this role cannot be more permissive than the `OPERATOR_ROLE` that the central administrator declared in the previous section.
  2. Apply the RoleBinding configuration:
         
         kubectl apply -f sync-rolebinding.yaml
         

  3. If required, [create a Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret) based on your preferred authentication method. If you used `none` as your authentication type, you can skip this step.

The Secret must meet the following requirements:

     * Create the Secret in the same namespace as the RepoSync.
     * The Secret's name must match the `spec.git.secretRef` name you defined in `root-sync.yaml`.
     * You must add the Secret's public key to the Git provider.
  4. Declare a `RepoSync` configuration:

### Git
         
         #ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RepoSync
         metadata:
           name: REPO_SYNC_NAME
           namespace: NAMESPACE
         spec:
           sourceType: git
           sourceFormat: unstructured
           git:
             repo: NAMESPACE_REPOSITORY
             revision: NAMESPACE_REVISION
             branch: NAMESPACE_BRANCH
             dir: "NAMESPACE_DIRECTORY"
             auth: NAMESPACE_AUTH_TYPE
             gcpServiceAccountEmail: NAMESPACE_EMAIL
             secretRef:
               name: NAMESPACE_SECRET_NAME
             noSSLVerify: NAMESPACE_NO_SSL_VERIFY
             caCertSecretRef:
               name: NAMESPACE_CA_CERT_SECRET_NAME
         

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_REPOSITORY`: add the URL of the Git repository to use as the namespace repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. If you don't enter a protocol, the URL is treated as an HTTPS URL. This field is required.
     * `NAMESPACE_REVISION`: add the Git revision (tag or hash) or branch to sync from. This field is optional and the default value is `HEAD`. When using a hash, it must be a full hash, and not an abbreviated form.
     * `NAMESPACE_BRANCH`: add the branch of the repository to sync from. This field is optional and the default value is `master`. We recommend using the `revision` field to specify a branch name for simplicity. If both the `revision` field and the `branch` field are specified, `revision` takes precedence over `branch`.
     * `NAMESPACE_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `ssh`: Use a SSH key pair
       * `cookiefile`: Use a `cookiefile`
       * `token`: Use a token
       * `gcpserviceaccount`: Use a Google service account to access a repository in Cloud Source Repositories.
       * `gcenode`: Use a Google service account to access a repository in Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.

For more information on these authentication types, see [Granting Config Sync read-only access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret).

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `NAMESPACE_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_SECRET_NAME`: add the name you intend to give your Secret. This field is optional.

     * `NAMESPACE_NO_SSL_VERIFY`: To disable the SSL certificate verification, set this field to `true`. The default value is `false`.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Git provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### OCI
    
    # ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    metadata:
      name: REPO_SYNC_NAME
      namespace: NAMESPACE
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: NAMESPACE_IMAGE
        dir: NAMESPACE_DIRECTORY
        auth: NAMESPACE_AUTH_TYPE
        gcpServiceAccountEmail: NAMESPACE_EMAIL
        caCertSecretRef:
          name: NAMESPACE_CA_CERT_SECRET_NAME
    

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_IMAGE`: the URL of the OCI image to use as the namespace source, for example `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`:

       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`**. Other formats (for example, `tar+bz2`) will not be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `NAMESPACE_DIRECTORY`: add the path in the source to the root directory that contains the configuration that you want to sync to. This field is optional and the default is the root directory (`/`) of the source.

     * `NAMESPACE_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your OCI provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### Helm
    
    # ROOT_SOURCE/namespaces/NAMESPACE/repo-sync.yaml
    apiVersion: configsync.gke.io/v1beta1
    kind: RepoSync
    metadata:
      name: REPO_SYNC_NAME
      namespace: NAMESPACE
    spec:
      sourceType: helm
      sourceFormat: unstructured
      helm:
        repo: NAMESPACE_REPOSITORY
        chart: HELM_CHART_NAME
        version: HELM_CHART_VERSION
        releaseName: HELM_RELEASE_NAME
        namespace: HELM_RELEASE_NAMESPACE
        values:
          foo:
            bar: VALUE_1
          baz:
          - qux: VALUE_2
            xyz: VALUE_3
        includeCRDs: HELM_INCLUDE_CRDS
        auth: NAMESPACE_AUTH_TYPE
          gcpServiceAccountEmail: NAMESPACE_EMAIL
          secretRef:
            name: NAMESPACE_SECRET_NAME
        caCertSecretRef:
          name: NAMESPACE_CA_CERT_SECRET_NAME
    

Replace the following:

     * `REPO_SYNC_NAME`: add the name of your RepoSync object. The name should be unique across the namespace.
     * `NAMESPACE`: add the name of your namespace.
     * `NAMESPACE_REPOSITORY`: the URL of the Helm repository to use as the root repository. You can enter URLs using either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples` uses the HTTPS protocol. This field is required.
     * `HELM_CHART_NAME`: add the name of your Helm chart. This field is required.
     * `HELM_CHART_VERSION`: the version of your chart. This field is optional. If no value is specified, the latest version is used.
     * `HELM_RELEASE_NAME`: the name of the Helm release. This field is optional.
     * `HELM_RELEASE_NAMESPACE`: the target namespace for a release. It only sets a namespace for resources that contain `namespace: {{ .Release.Namespace }}` in their templates. This field is optional. If no value is specified, the default namespace `config-management-system` is used.
     * `HELM_INCLUDE_CRDS`: set to `true` if you want the Helm template to also generate a CustomResourceDefinition. This field is optional. If no value is specified, the default is `false` and a CRD won't be generated.
     * `VALUE`: values to use instead of default values that accompany the Helm chart. Format this field the same way as [helm chart's values.yaml](https://helm.sh/docs/chart_best_practices/values/) file. This field is optional.
     * `ROOT_AUTH_TYPE`: add one of the following authentication types:

       * `none`: Use no authentication
       * `token`: Use a username and password to access a private Helm repository.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

This field is required.

     * `NAMESPACE_EMAIL`: If you added `gcpserviceaccount` as your `ROOT_AUTH_TYPE`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

     * `NAMESPACE_SECRET_NAME`: add the [name of your Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl#helm-access) if `token` is the `ROOT_AUTH_TYPE`. This field is optional.

     * `NAMESPACE_CA_CERT_SECRET_NAME`: add the name of your Secret. If this field is set, your Helm provider must be using a certificate issued by this certificate authority (CA). The Secret must contain the CA certificate under a key named `cert`. This field is optional.

To learn more about how to configure the Secret object for the CA certificate, see [Configure Certificate Authority](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl#ca-certificate)

For an explanation of the fields and a complete list of fields that you can add to the `spec` field, see [RootSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

  5. Apply the `RepoSync` configuration:
         
         kubectl apply -f repo-sync.yaml
         

  6. To verify the configuration, use `kubectl get` on one of the objects in the namespace-scoped source. For example:
         
         kubectl get rolebindings -n NAMESPACE
         

  7. You can repeat the above steps if you need to configure multiple namespace-scoped source of truth .




## Verify the sync status of the source of truth

You can use the [`nomos status` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command) to inspect the sync status of the source of truth:
    
    
    nomos status
    

You should see output similar to the following example:
    
    
    my_managed_cluster-1
      --------------------
      <root>   git@github.com:foo-corp/acme/admin@main
      SYNCED   f52a11e4
      --------------------
      bookstore  git@github.com:foo-corp/acme/bookstore@v1
      SYNCED     34d1a8c8
    

In this example output, the namespace-scoped source, in this case a Git repository, is configured for a namespace named `bookstore`.

## Verify the RootSync installation

When you create a RootSync object, Config Sync creates a reconciler with the `root-reconciler` prefix. A reconciler is a Pod that is deployed as a Deployment. It syncs manifests from a source of truth to a cluster.

You can verify that the RootSync object is working correctly by checking the status of the root-reconciler Deployment:
    
    
    kubectl get -n config-management-system deployment \
        -l configsync.gke.io/sync-name=ROOT_SYNC_NAME
    

Replace `ROOT_SYNC_NAME` with the name of RootSync.

You should see output similar to the following example:
    
    
    NAME              READY   UP-TO-DATE   AVAILABLE   AGE
    root-reconciler   1/1     1            1           3h42m
    

For further ways to explore the status of your RootSync object, see [Monitoring RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).

## Verify the RepoSync installation

When you create a RepoSync object, Config Sync creates a reconciler with the `ns-reconciler-NAMESPACE` prefix, where `NAMESPACE` is the namespace you created your RepoSync object in.

You can verify that the RepoSync object is working correctly by checking the status of the namespace reconciler Deployment:
    
    
    kubectl get -n config-management-system deployment \
      -l configsync.gke.io/sync-name=REPO_SYNC_NAME \
      -l configsync.gke.io/sync-namespace=NAMESPACE
    

Replace `REPO_SYNC_NAME` with the name of RepoSync, and replace `NAMESPACE` with the namespace that you created your namespace-scoped source of truth in.

For further ways to explore the status of your RepoSync object, see [Exploring the RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).

## Remove a source of truth

Select the **Central control method** or **Kubernetes API method** tab to view the relevant instructions.

### Central control method

If you used the **Control sources of truth in a root source of truth** method, a central administrator can follow the following two steps to remove a source of truth:

  1. Decide if you'd like to delete or keep the resources that are managed through your RootSync and RepoSync objects.

     * To delete all the resources that your RootSync or RepoSync objects manage, sync your RootSync or RepoSync object to an empty source. For example, a GitHub repository with no configs. If your RootSync or RepoSync object contains another RootSync or RepoSync object, the inner RootSync or RepoSync needs to sync to an empty Git repository first.

     * If you've [enabled the webhook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) and want to keep your resources, [disable drift prevention for abandoned resources](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#disable_drift_prevention_for_abandoned_resources). If you haven't enabled the webhook, you don't have to take any additional steps to keep your resources.

  2. Remove the RootSync or RepoSync object from the source of truth.




### Kubernetes API method

If you used the **Control namespace-scoped sources of truth with the Kubernetes API** method, application operators can use the following steps to remove a namespace-scoped source of truth:

  1. Decide if you'd like to delete or keep the resources that are managed through your RootSync and RepoSync objects.

     * To delete all the resources that your RootSync or RepoSync objects manage, sync your RootSync or RepoSync object to an empty source. For example, a GitHub repository with no configs. If your RootSync or RepoSync object contains another RootSync or RepoSync object, the inner RootSync or RepoSync needs to sync to an empty Git repository first.

     * If you've [enabled the webhook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) and want to keep your resources, [disable drift prevention for abandoned resources](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift#disable_drift_prevention_for_abandoned_resources). If you haven't enabled the webhook, you don't have to take any additional steps to keep your resources.

  2. Delete the RootSync or RepoSync object by running the following command:
         
         kubectl delete -f FILE_NAME
         

Replace `FILE_NAME` with the name of your RootSync or RepoSync configuration file. For example, `root-sync.yaml`.




## What's next

  * Learn how to [prevent config drift](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) in namespace-scoped sources of truth.
  * Discover how to [monitor your RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).
  * Learn how to [break up a source of truth into multiple sources of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/breaking-up-repo).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
