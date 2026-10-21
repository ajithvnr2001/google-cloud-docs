---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features/
title: Manage fleet-level features \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:11:50.693574+00:00
---

# Manage fleet-level features  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Manage fleet-level features Stay organized with collections  Save and categorize content based on your preferences. 

Fleets let you manage enterprise and other fleet-enabled features across multiple clusters at the same time. This lets you, for example, apply a common set of policies or create a single-service mesh across your fleet of clusters. This page provides an overview of how you can manage features for your fleet. For more information about configuring and using individual features, see their documentation.

If you've enabled Google Kubernetes Engine, you can manage features in the Google Cloud console. All fleet users can manage features using the command line.

Some features let you create fleet-level default feature configuration for your fleet clusters. For example, you can ensure that every cluster you create in your fleet has Policy Controller installed and configured.

You can learn more about how fleet-level feature management on your clusters works "under the hood" in the Feature authorization section.

## Fleet-level features

You can manage the following features at fleet level:

  * Managed [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/auto-control-plane-with-fleet)
  * [Security posture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)
  * [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview)
  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller)
  * [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet)
  * [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup)
  * [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services) (GKE clusters only)
  * [Continuous validation for Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview-cv)



This list does not include all features that use or require fleets. For example, [fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) relies on clusters being members of a fleet but does not require configuration at fleet level, and Cloud Service Mesh requires fleet membership for all control plane and setup options.

You can find out more about which features are available in which environments in the [Deployment options](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options) page.

## Set up fleet-level features

The following sections describe how you can enable and configure fleet-level features.

To use a fleet-level feature, in most cases you _enable_ the feature for your fleet and _configure_ it for your fleet members. Some configuration (or other additional setup) is generally required to actually use the feature with your clusters and workloads.

You can create fleet-default cluster configurations for some features, meaning that any new clusters you create in your fleet will be created with your specified settings for that feature already configured.

### Enable features with fleet-level defaults

You can create fleet-level default settings for your GKE clusters for some features. After creating these settings, any GKE cluster that you [register during cluster creation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster) is automatically configured with your fleet-level configurations. So, for example, if you set up defaults for Policy Controller, each new cluster you create in your fleet will have your specified version of Policy Controller installed, with your specified policy bundles and other settings. Fleet default settings are not automatically applied to _existing_ fleet member clusters, although you can sync existing clusters to your default settings by using the Google Cloud console.

The general process for enabling features with fleet-level defaults is as follows:

###  Console 

  1. In your fleet host project, go to the **Feature Manager** page:

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

The features that support configuring fleet-level defaults using the Google Cloud console are listed under **Fleet-level Feature Management**.

  2. For your chosen feature, click **Configure** and follow the instructions to enable and configure defaults for the feature.

  3. Optional: Select and sync existing clusters in your fleet to your new settings.




###  gcloud 

  1. Create a YAML file specifying your chosen fleet defaults for the feature.
  2. Run the `enable` command for the feature, passing it your configuration file. Each fleet-level feature has its own `enable` command. For example, to enable Cloud Service Mesh for your fleet with the default configuration specified in `mesh.yaml`, run the following command in your fleet host project:
         
         gcloud container fleet mesh enable --fleet-default-member-config mesh.yaml
         




Alternatively, for some features you can specify fleet defaults using parameters to the `fleet create` or `fleet update` command. See the guide for your chosen feature for more details.

###  Terraform 

Define a `google_gke_hub_feature` resource with a `fleet_default_member_config` block that specifies your chosen fleet defaults. For details and supported fleet features, see the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature).

Not all features support fleet default configuration using all of these options. For detailed instructions on how to set up fleet defaults for each supported feature, see the following documentation:

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#configure_your_fleet)
  * [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#configure-fleet)
  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller#configure-fleet)
  * [Security posture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fleet-security-posture)
  * [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure-fleet) (command line only)
  * [Continuous validation for Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enable-cv-fleet) (preview, command line only)



### Enable and configure fleet features on individual clusters

As an alternative to fleet default configuration, you can choose to configure fleet features separately on individual clusters. This might be a good option if:

  * You want to configure an existing cluster to use a feature.
  * You want to use services where fleet default configuration is not available, or not available using your chosen tool.



#### Enable features

Note that this step is not required for all features. See the guide for your chosen feature for more details.

###  Console 

You can enable features from the **Feature Manager** page in the Google Cloud console.

To enable a feature for your fleet:

  1. In your fleet host project, go to the **Feature Manager** page:

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

Features that can be enabled but not configured from this page are listed under **Manage other enterprise-ready features**.

  2. Click **Enable** in the panel for the feature you want to enable.

  3. Click the **Enable...** button in the details panel that displays.




###  gcloud 

Each fleet-level feature has its own `enable` command. For example, to enable GKE Identity Service for your fleet, you run the following command in your fleet host project:
    
    
    gcloud container fleet identity-service enable
    

See the [Google Cloud SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet) (and its [beta](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet) and [alpha](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet) equivalents) for a complete list of commands, or the individual feature documentation sets for more details.

To learn how to check if a feature has already been enabled and view other feature status, see View fleet feature status.

#### Configure individual clusters

The configuration steps you follow depend on the feature. See the following guides for more information:

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#configure_per_cluster)
  * Security posture: 
    * [Automatically audit workloads for configuration issues](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/protect-workload-configuration)
    * [Automatically scan workloads for known vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/security-posture-vulnerability-scanning)
  * [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync#configuring-config-sync)
  * [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller#installing)
  * [GKE Identity Service](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure_clusters)
  * [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup)



## View fleet feature status

The easiest way to view fleet feature status is by using the **Feature Manager** dashboard in the Google Cloud console.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

For supported features, this page displays how many of your fleet clusters have the following status:

  * Have this feature enabled
  * Have this feature enabled successfully
  * Have a warning for this feature
  * Have an error for this feature



You can also see whether fleet default settings have been configured for the feature, and how many fleet member clusters have these settings. For enabled features, you can click through to a detail page that lists the clusters using the feature, and, if configured, lets you select and sync clusters to your fleet default settings.

For features that can't be configured using this page (listed under **Manage other enterprise-ready features**), you can see whether the feature has been enabled for your fleet, and view a details panel that shows how many clusters have the feature installed and other relevant information.

### View feature status using gcloud

###  gcloud 

Run the following command to list all enabled features:
    
    
    gcloud container fleet features list
    

## Disable a fleet-level feature

To disable a feature at fleet level, do the following in your fleet host project.

###  Console 

Only the fleet features listed under **Manage other enterprise-ready features** can be disabled from the Google Cloud console.

  1. In your fleet host project, go to the **Feature Manager** page:

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

  2. Click **Details** in the panel for the feature you want to disable.

  3. Click the **Disable...** button in the details panel that displays.




###  gcloud 

Each fleet-level feature has its own `disable` command. For example, to disable Cloud Service Mesh for your fleet, run the following command in your fleet host project:
    
    
    gcloud container fleet mesh disable
    

See the [Google Cloud SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet) (and its [beta](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet) and [alpha](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet) equivalents) for a complete list of commands, or the individual feature documentation sets for more details.

For expected behavior after you disable a feature for your fleet, see the relevant feature documentation. In many cases, the relevant configuration still exists on your cluster but you are no longer able to centrally manage the feature using fleet commands or the Google Cloud console.

## Feature authorization

In order to manage features at fleet-level, they must be authorized through role-based access control to perform their functions on clusters. Google Cloud uses a service called Feature Authorizer that automatically sets and updates permissions for fleet-enabled features, which saves you from having to set feature permissions manually on every cluster, especially when Google releases feature updates.

When you [register a cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation), the manifest applied to the cluster contains a [`ClusterRoleBinding`](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) that gives the Feature Authorizer a `cluster-admin` role on the cluster, and the role is attached to a service account named `service-project-number@gcp-sa-gkehub.iam.gserviceaccount.com`.

When you disable a fleet-enabled feature in your project, Feature Authorizer deletes the corresponding `ClusterRole` and `ClusterRoleBinding` for the feature, which removes the feature's ability to operate on the cluster.

### View Feature Authorizer in audit logs

To view Feature Authorizer activity in GKE [audit logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging):

  1. Open Logs Explorer in the Google Cloud console.

[Go to the Logs page](https://console.cloud.google.com/logs/query)

  2. Run the following advanced query:
         
         resource.type="k8s_cluster"
         resource.labels.cluster_name="CLUSTER_NAME"
         resource.labels.location="CLUSTER_LOCATION"
         protoPayload.authenticationInfo.principalEmail="system:serviceaccount:gke-connect:connect-agent-sa"
         protoPayload.authenticationInfo.authoritySelector="service-PROJECT_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com"
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that you want to view the logs for.
     * `CLUSTER_LOCATION`: the Google Cloud location that the cluster was created in.
     * `PROJECT_NUMBER`: the Google Cloud project number for the project that owns the cluster.



For non-GKE clusters, find out where the [Kubernetes audit logs](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/) are stored, and run a similar query.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
