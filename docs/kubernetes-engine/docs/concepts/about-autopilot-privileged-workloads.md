---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads/
title: About privileged workload admission in Autopilot mode \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:10.722995+00:00
---

# About privileged workload admission in Autopilot mode  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About privileged workload admission in Autopilot mode Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

You can control which privileged workloads can run in Google Kubernetes Engine (GKE) Autopilot mode by using allowlists and policies. This document describes the default constraints that Autopilot enforces on workloads, the types of privileged workloads that you can run in Autopilot mode, and the methods of controlling privileged workload admission.

This document is for the following people:

  * Platform admins and operators who want to run privileged GKE workloads from various sources in Autopilot mode.
  * Identity and account admins who want to improve the security posture of your organization by blocking all privileged workloads except for specific workloads.



## About privileged workloads in Autopilot mode

To improve your security posture, Autopilot mode clusters and nodes enforce specific [security constraints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security) by default. For example, Autopilot rejects most Pods that set the `spec.securityContext.privileged` field to `true` in a container. _Privileged workloads_ in Autopilot are workloads that don't meet these default constraints. By default, Autopilot nodes in a Google Cloud organization reject privileged workloads.

Specific privileged workloads can run in Autopilot mode only if the cluster has _allowlists_ that match those workloads. When a cluster admin creates or modifies a cluster, they can specify paths to allowlists that the cluster can run. By default, every Google Cloud organization supports allowlists from Autopilot partners and verified open source projects.

Organization administrators can modify this default behavior in the following ways by using [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview):

  * Allow all workloads from [GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners) and verified open source workloads. This is the default behavior in all Google Cloud organizations.
  * Allow specific partner workloads or verified open source workloads.
  * Allow only specific customer-owned privileged workloads.
  * Deny all privileged workloads.



This _deny all, and then allow some_ approach is a security best practice that lets you control exactly what runs with elevated privileges in your GKE clusters.

You might want to control privileged workloads in Autopilot mode in situations like the following:

  * You [run workloads in Autopilot mode in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters) and you want privileged workloads to run on those nodes.
  * You want to allow only a specific set of privileged workloads to run in your organization, folder, or project.



### Sources of privileged Autopilot workloads

The following table describes the types of privileged workloads that you can run in Autopilot:

Privileged workload types  
---  
Autopilot partner workloads | A subset of Google Cloud partners provide privileged workloads for Autopilot mode. GKE verifies these partner workloads. These workloads are available to any customer. By default, any customer can install the corresponding allowlists in any Autopilot or Standard cluster. For more information about the available partner workloads, see [Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).  
Open source workloads | Specific privileged open source workloads have allowlists that let you run those workloads in Autopilot mode. GKE verifies these workloads. By default, any customer can install the corresponding allowlists in any Autopilot or Standard cluster. For more information about the available open source workloads, see [Run privileged open source workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads).  
Customer-owned workloads | If you're an eligible customer who has privileged workloads that you want to run in Autopilot nodes, you can create allowlists for those workloads. This capability is disabled by default for all Google Cloud organizations. You use Organization Policy Service to add allowlist paths for specific workloads, and then update clusters to install those allowlists. **Note** : Running your own privileged workloads in Autopilot is available only to eligible Google Cloud customers. To check whether you're eligible, contact [Cloud Customer Care](https://cloud.google.com/support-hub).For more information, see the Customer-owned privileged workloads section.  
  
## How privileged workload admission control works

To allow specific privileged workloads to run in your Autopilot nodes, you install _allowlists_ that correspond to each workload. These allowlists are WorkloadAllowlist Kubernetes custom resources. GKE validates the workload details against any WorkloadAllowlists in the cluster, and allows admission only if the details match. By default, every Autopilot or Standard cluster in a Google Cloud organization lets you install WorkloadAllowlists for Autopilot partner workloads and for open source workloads.

At a high level, running privileged workloads in Autopilot nodes involves these steps:

  1. The organization administrator verifies that the `container.managed.autopilotPrivilegedAdmission` managed Organization Policy constraint allows the installation of allowlists from a specific source. For more information, see the Organization Policy managed constraint for allowlists section.
  2. For customer-owned privileged workloads, the platform administrator creates allowlists that match the privileged workloads. For more information, see the Customer-owned privileged workloads section.
  3. The cluster admin configures an Autopilot or Standard cluster to allow installation of allowlists from a specific source. For more information, see the Cluster configuration section.
  4. The cluster admin creates an AllowlistSynchronizer that references the path to the allowlist. The AllowlistSynchronizer installs the allowlist and keeps the allowlist up to date. For more information, see the Allowlist installation section.



After these steps are completed, an app operator can deploy the privileged workload in the cluster.

## Organization Policy managed constraint for allowlists

By default, every Google Cloud organization enforces an organization policy that's based on the `container.managed.autopilotPrivilegedAdmission` [managed constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#managed-constraints). This constraint defines a set of file or directory paths from which GKE clusters can install allowlists. The cluster configuration must use allowlist paths from the parameters of this constraint.

By default, the `autopilotPrivilegedAdmission` constraint allows the use of all allowlists that are owned by approved GKE partners and open source projects. This setting matches the default configuration of GKE clusters, which can install any of those approved allowlists.

As an organization policy administrator, you can modify the set of allowlist paths that can be applied to GKE clusters in your organization, folder, or project. For example, to allow the use of a custom allowlist that your organization owns, you add that allowlist path to the managed constraint.

### Managed constraint parameters

The `autopilotPrivilegedAdmission` managed constraint has the following specification:
    
    
    spec:
      rules:
      - enforce: true
        parameters:
          allowAnyGKEPath: ALLOW_GKE_PATHS
          allowPaths:
          - PATH1
          - PATH2
          - PATH3
    

The following fields in the specification control the set of allowlists that clusters can use:

  * `allowAnyGKEPath`: a boolean value that controls whether clusters can use the default set of GKE-approved allowlist paths. This parameter supports the following values:

    * `True`: cluster admins can configure clusters without modifying the allowlist configuration, with one or more allowlist paths that start with `gke://`, or with an empty string to disable all allowlists for the cluster. `True` is the default value for this parameter.

    * `False`: cluster admins must configure clusters with an empty string for allowlist sources or with any allowlist paths from the `allowPaths` parameter.

**Caution:** If you set the `allowAnyGKEPath` parameter to `False`, cluster creation or modification requests must explicitly set the cluster allowlist configuration to an empty string or to one or more paths from the `allowPaths` parameter of this constraint. All Autopilot and Standard clusters in the organization, folder, or project are affected.
  * `allowPaths`: a list of approved allowlist sources that cluster admins can specify values from when they configure a cluster. You can specify paths to specific allowlist files or to entire directories.




The following table describes the results of configuring these parameters in different ways:

`allowAnyGKEPath` value | `allowPaths` value | Result  
---|---|---  
`True` | Empty or unspecified. | Cluster admins can do any of the following actions during cluster creation or modification:

  * **Use the default allowlist configuration** : omit any allowlist configuration options, so that the cluster can install allowlists from any path that has the `gke://` prefix.
  * **Disable allowlist installation** : specify an empty value for the cluster allowlist configuration.
  * **Specify GKE allowlist paths** : specify one or more allowlist paths that have the `gke://` prefix. The cluster can install allowlists only from those paths.

  
`False` | Empty or unspecified. | Cluster admins must specify an empty value for the cluster allowlist configuration. If cluster admins skip allowlist path configuration, then cluster creation or modification fails. **Caution** : This configuration requires all clusters to disable all allowlists, including allowlists for partner workloads. Before you specify this configuration, verify that your clusters don't depend on those workloads.  
`True` | Values are specified. | Cluster admins can do any of the following actions during cluster creation or modification:

  * **Use the default allowlist configuration** :omit any allowlist configuration options, so that the cluster can install allowlists from any path that has the `gke://` prefix.
  * **Disable allowlist installation** : specify an empty value for the cluster allowlist configuration.
  * **Specify allowlist paths** : specify one or more allowlist paths that have either the `gke://` prefix or are specified in the `allowPaths` parameter.

  
`False` | Values are specified. | Cluster admins must do one of the following actions during cluster creation or modification:

  * **Disable allowlist installation** : specify an empty value for the cluster allowlist configuration.
  * **Specify allowlist paths** : specify one or more allowlist paths from the `allowPaths` parameter.

**Caution** : This configuration requires that clusters disable allowlists for partner workloads. Before you specify this configuration, verify that your clusters don't depend on those partner workloads.  
  
For more information about controlling privileged workload admission in organization policies, see [Restrict privileged GKE workloads in organizations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations).

## Customer-owned privileged workloads

**Note:** Running your own privileged workloads in Autopilot is available only to eligible Google Cloud customers. To request access to this feature, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

As a GKE customer, you might have your own specialized workloads that require more privileges in the cluster than the default Autopilot security constraints allow. In GKE version 1.35 and later, you can exempt these workloads from the default Autopilot constraints by creating allowlists.

An allowlist is a YAML file that defines a WorkloadAllowlist Kubernetes custom resource. The specification of a WorkloadAllowlist matches various fields in the Kubernetes Pod specification. When you define a WorkloadAllowlist, you match the values in the WorkloadAllowlist to corresponding fields in the specification of your privileged workload. You store the YAML files in a Cloud Storage bucket.

To install these customer-owned allowlists in a cluster, the following steps must happen:

  1. Your organization administrator adds the Cloud Storage paths to an organization policy. For more information, see the About the Organization Policy managed constraint section.
  2. You add the Cloud Storage paths to a cluster configuration. For more information, see the Cluster configuration section.



For more information about creating your own WorkloadAllowlists, see [Create allowlists for privileged Autopilot workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-privileged-allowlists).

## Cluster configuration

To run a privileged workload in Autopilot mode, a cluster admin adds one or more approved allowlist paths to the cluster configuration. After you add the paths to the cluster, app operators can install the corresponding allowlists and privileged workloads in the cluster.

By default, you can install allowlists from Autopilot partners and approved open source projects. This default set of approved sources for allowlists might change because of an organization policy, as described in the preceding section. If an organization policy controls the approved allowlist paths, you must coordinate with your organization administrator to identify those paths. You can then specify one or more of the approved paths in the cluster configuration.

For more information about configuring clusters, see [Run privileged workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads#configure-allowlist-cluster).

## Allowlist installation

To install an allowlist from an approved source in your cluster, you use a Kubernetes custom resource named the AllowlistSynchronizer. You define and create AllowlistSynchronizers similarly to how you create other Kubernetes resources like Pods and Deployments. Each AllowlistSynchronizer has a list of paths to allowlists that you want to install in the cluster.

When you create an AllowlistSynchronizer, GKE installs allowlists from these paths and keeps the allowlists up-to-date. Every 10 minutes, GKE checks for changes to allowlist files. If an update exists, the synchronizer installs the updated allowlist in the cluster.

After GKE installs an allowlist based on an AllowlistSynchronizer, you can create the corresponding privileged workload in the cluster.

For more information about installing allowlists in a cluster, see [Run privileged workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads#create-allowlistsynchronizer).

## Allowlist paths

When you configure allowlist support in your organization policy or clusters, you specify paths to one or more WorkloadAllowlists that you've approved for installation. The syntax for these paths depends on who created the WorkloadAllowlist, as follows:

  * Specific Autopilot partners and approved open source projects:
        
        gke://REPOSITORY_PATH/SELECTOR
        

Replace the following:

    * `REPOSITORY_PATH`: the path to the directory that contains allowlists for the workload, such as `Grafana/alloy`. For more information about the allowlist paths for these workloads, see the following pages: 
      * [Autopilot partner workloads](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners#allowlisted-partner-workloads)
      * [Privileged open source workloads with Autopilot support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads)
    * `SELECTOR`: the name of a specific file or the `*` character, which selects every file in that directory.

For example, the following path selects any allowlist in the `Grafana/alloy` directory:
    
    gke://Grafana/alloy/*
    

  * Customer-owned privileged workloads:
        
        gs://DIRECTORY_PATH/SELECTOR
        

Replace `DIRECTORY_PATH` with the path to the directory in Cloud Storage that contains your allowlist files. You can specify multiple paths.




You can specify one or more of the preceding paths in your organization policy or cluster configuration. For example, you can add GKE partner workloads and customer-owned workloads to the same configuration. You can also use the `*` character to select all allowlists. For example, `gke://*` selects any GKE-approved allowlist from any source.

The following table describes the configuration that's needed in organization policies or clusters to support certain objectives:

Objective | Organization policy configuration | Cluster configuration  
---|---|---  
Allow all GKE-approved WorkloadAllowlists | Do the following: 

  1. Set the `allowAnyGKEPath` parameter to the default value of `True`.
  2. Keep the `allowPaths` parameter empty.

| Do one of the following: 

  * Don't configure allowlists for your cluster. By default, all clusters allow the installation of GKE-approved WorkloadAllowlists.
  * Specify only `gke://*` as the approved path when you configure allowlists for your cluster.

  
Allow only specific GKE-approved WorkloadAllowlists | Do the following: 

  1. Set the `allowAnyGKEPath` parameter to `False`.
  2. Specify paths to specific GKE-approved WorkloadAllowlists in the `allowPaths` parameter.

| Specify paths to specific GKE-approved WorkloadAllowlists when you create or update a cluster. An organization policy might restrict which GKE-approved paths you can specify.  
Allow only customer-managed WorkloadAllowlists | Do the following: 

  1. Set the `allowAnyGKEPath` parameter to `False`.
  2. Specify paths to customer-managed WorkloadAllowlists in the `allowPaths` parameter.

| Specify paths to customer-managed WorkloadAllowlists when you create or update a cluster. The paths that you specify must be in the `allowPaths` parameter of an organization policy.  
Prevent the use of WorkloadAllowlists | Do the following: 

  1. Set the `allowAnyGKEPath` parameter to `False`.
  2. Keep the `allowPaths` parameter empty.

| Set an empty string `""` as the approved path when you create or update a cluster.  
  
## What's next

  * [Restrict privileged GKE workloads in organizations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations).
  * [Run privileged workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
