---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/kubectl-apply/
title: Apply Kubernetes manifests \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:43.666318+00:00
---

# Apply Kubernetes manifests  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/kubectl-apply/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Apply Kubernetes manifests Stay organized with collections  Save and categorize content based on your preferences. 

Use the `kubectl-apply` module to apply Kubernetes manifests to your Google Kubernetes Engine clusters.

This module lets you embed manifests directly as string content or reference them from remote locations, files, templates, or entire directories. By using this module, you streamline the deployment of commonly used infrastructure components and performance optimizations. Supported components include the Kueue scheduler, the Jobset API, the NVIDIA GPU Operator, the NCCL gIB plugin, and ASAPD-Lite (for optimizing specific machine types, such as the [A4X Max machine type](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/create-a4x-max-cluster)).

For the complete list of inputs and outputs for this module, see the [`kubectl-apply` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/management/kubectl-apply#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `kubectl-apply` module, see the [`examples/a3-megagpu-8g.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-megagpu/gke-a3-megagpu.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `kubectl-apply` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **GKE**.



### Required roles

To get the permissions that you need to apply Kubernetes manifests to the cluster, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure manifests

You can specify manifests in your blueprint by using several methods:

  * **Provide the raw string** : specify the module configuration by using the `content: manifest_body format`.
  * **Remote URL:** a single URL to a manifest file, such as the `https://github.com/kubernetes-sigs/jobset/releases/download/v0.6.0/manifests.yaml` URL.
  * **Single local file:** a local YAML Ain't Markup Language (YAML) manifest file, such as the `./manifest.yaml` path.
  * **Template file:** a template file with the `.tftpl` extension to generate a manifest, such as the `./template.yaml.tftpl` path. You can pass variables to format the template file by using the `template_vars` field.
  * **Directory:** a directory that contains multiple YAML files or template files, such as the `./manifests/` path. You can pass variables to format the template files by using the `template_vars` field.



## Example configurations

The following sections provide examples that demonstrate how to configure the `kubectl-apply` module.

### Apply manifests

The following example demonstrates how to apply manifests by using different source methods:
    
    
    - id: existing-gke-cluster
      source: modules/scheduler/pre-existing-gke-cluster
      settings:
        project_id: $(vars.project_id)
        cluster_name: my-gke-cluster
        region: us-central1
    
    - id: kubectl-apply
      source: modules/management/kubectl-apply
      use: [existing-gke-cluster]
      settings:
        - content: |
            apiVersion: v1
            kind: Namespace
            metadata:
              name: my-namespace
        - source: "https://github.com/kubernetes-sigs/jobset/releases/download/v0.6.0/manifests.yaml"
        - source: $(ghpc_stage("manifests/configmap1.yaml"))
        - source: $(ghpc_stage("manifests/configmap2.yaml.tftpl"))
          template_vars: {name: "dev-config", public: "false"}
        - source: $(ghpc_stage("manifests"))/
          template_vars: {name: "dev-config", public: "false"}
    
    

### Deploy workload components

You can deploy workload components and performance optimizations by setting the `install: true` field for the component in the `settings` block. The module supports the installation of the following components:

  * **Kueue scheduler** : manages workload queuing and resource allocation.
        
        - id: workload_component_install
        source: modules/management/kubectl-apply
        use: [gke_cluster]
        settings:
          kueue:
            install: true
            version: v0.10.0
        

  * **Jobset API** : manages groups of related jobs as a single unit.
        
        ...
        settings:
          jobset:
            install: true
        

  * **NVIDIA GPU Operator** : automates the setup and management of software needed to provision GPUs.
        
        ...
        settings:
          nvidia_gpu_operator:
            install: true
        

  * **NCCL gIB plugin** : improves multi-GPU and multi-node communication speed.
        
        ...
        settings:
          nccl_gib_plugin:
            install: true
        

  * **ASAPD-Lite** : provides storage and data caching optimization for high-performance machine types, such as `a4x-max`.
        
        ...
        settings:
          asapd_lite:
            install: true
        




The `config_path` field in the `kueue` block also accepts a template file. If you provide a template file, then you must provide variables for the template by using the `config_template_vars` field. The following example demonstrates how to pass variables:
    
    
      - id: workload_component_install
        source: modules/management/kubectl-apply
        use: [gke_cluster]
        settings:
          kueue:
            install: true
            config_path: $(ghpc_stage("manifests/user-provided-kueue-config.yaml.tftpl"))
            config_template_vars: {name: "dev-config", public: "false"}
          jobset:
            install: true
    
    

You can specify a particular Kueue version that you want to use by using the `version` field. We recommend that you use the `v0.10.0` version. To view all available versions, see the [supported Kueue versions documentation](https://github.com/kubernetes-sigs/kueue/releases).
    
    
      - id: workload_component_install
        source: modules/management/kubectl-apply
        use: [gke_cluster]
        settings:
          kueue:
            install: true
            version: v0.10.0
            config_path: $(ghpc_stage("manifests/user-provided-kueue-config.yaml.tftpl"))
            config_template_vars: {name: "dev-config", public: "false"}
          jobset:
            install: true
    
    

## Helm release naming

The `kubectl-apply` module generates deterministic names for the Helm releases that are used to manage your manifests. This naming convention helps ensure consistent release names across redeployments.

The module determines the Helm release name for each manifest by using the following precedence hierarchy:

  1. **Explicit name:** the value of the `name` attribute in the `apply_manifests` list, if specified.
  2. **File basename:** the basename of the manifest file. For example, the value `kueue-manifest` is the basename for the `kueue-manifest.yaml` file.
  3. **Fallback:** a generated name in the format `MODULE_ID-raw-HASH`. Cluster Toolkit replaces `MODULE_ID` with the ID of the module, and replace `HASH` with the hash value.



### Set a custom name for the Helm release

To specify a custom name for a Helm release, add the `name` attribute to the `apply_manifests` entry in your cluster blueprint:
    
    
    - id: my-kubectl-apply
      source: modules/management/kubectl-apply
      settings:
        apply_manifests:
        - source: modules/management/kubectl-apply/manifests/kueue-v0.12.2.yaml
          name: custom-kueue-release
    

## Troubleshoot common errors

This section lists errors that you might encounter when you apply manifests directly from remote `http://` or `https://` URLs by using the `kubectl-apply` module. For more information about these methods, see Configure manifests.

For production environments, we recommend that you source manifests from local paths or a version-controlled Git repository, because the URL method introduces additional complexity.

If you use the URL method, then you can troubleshoot the configuration by using the solutions in this section.

### Race conditions when you apply manifests in parallel

The following issue occurs when you apply a manifest with custom resources, such as a `ClusterQueue` resource, at the same time as the manifest that defines the `CustomResourceDefinition` (CRD) object for those resources. Because the module applies manifests from the `apply_manifests` list in parallel, there is no guarantee that the cluster creates the CRD object before the resource that uses the CRD object. This race condition might result in errors like the following:
    
    
    Error: resource [kueue.x-k8s.io/v1beta1/ClusterQueue] isn't valid for cluster
    

To resolve this issue, use a two-stage deployment process to manually enforce the correct order of operations. Complete the following steps:

  1. **Initial deployment:** in your blueprint, include only the manifests that contain the CRD resources in the `apply_manifests` list. Your first deployment might look like the following example:
         
         settings:
           apply_manifests:
           # This manifest contains the CRDs for Kueue
           - source: "https://github.com/kubernetes-sigs/kueue/releases/download/v0.11.4/manifests.yaml"
         

  2. **Run the first deployment** : to deploy the CRD resources, use the [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) or the `terraform apply` command.

  3. **Second deployment:** after the first deployment succeeds, add the manifests that contain your custom resources to the `apply_manifests` list and deploy the updated blueprint. Because the CRD objects now exist in the cluster, the second deployment succeeds. The example settings for the second deployment might look like the following:
         
         settings:
         apply_manifests:
         # The CRD manifest is still present
         - source: "https://github.com/kubernetes-sigs/kueue/releases/download/v0.11.4/manifests.yaml"
         
         # Now, add your configuration manifest
         - source: "https://gist.githubusercontent.com/YourUser/..." # Your configuration URL
         

  4. **Run the deployment command again:** by having these custom resources exist in the cluster, the deployment is much more likely to succeed.




### Terraform template files from remote URLs

The following issue occurs when you attempt to render a template file with the `.tftpl` extension that you source from a remote URL. The `kubectl-apply` module can't render template files from remote sources.

To resolve this issue, you must render the template into YAML file locally, host that rendered file at a URL, and provide the URL of the rendered file in your blueprint.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`kubectl-apply` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/management/kubectl-apply#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
