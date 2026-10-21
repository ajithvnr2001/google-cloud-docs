---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-migrate-cluster-mode/
title: Prepare to migrate to Autopilot from Standard \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:12.794462+00:00
---

# Prepare to migrate to Autopilot from Standard  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-migrate-cluster-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Prepare to migrate to Autopilot from Standard Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides considerations and recommendations that will help you to migrate workloads from Standard Google Kubernetes Engine (GKE) clusters to Autopilot clusters with minimal disruption to your services. This page is for cluster administrators who have already decided to migrate to Autopilot. If you need more information before you decide to migrate, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) and [Compare GKE Autopilot and Standard](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison).

## How migration works

Autopilot clusters automate many of the optional features and functionality that require manual configuration in Standard clusters. Additionally, Autopilot clusters enforce more secure default configurations for applications to provide a more production-ready environment, and reduce your required management overhead compared to Standard mode. Autopilot clusters apply many GKE best practices and recommendations by default. Autopilot uses a workload-centric configuration model, where you request what you need in your Kubernetes manifests and GKE provisions the corresponding infrastructure.

When you migrate your Standard workloads to Autopilot, you should prepare your workload manifests to ensure that they're compatible with Autopilot clusters, for example by ensuring that your manifests request infrastructure that you would normally have to provision yourself.

To prepare and execute a successful migration, you'll do the following high-level tasks:

  1. Run a pre-flight check on your existing Standard cluster to confirm compatibility with Autopilot.
  2. If applicable, modify your workload manifests to become Autopilot compatible.
  3. Do a dry-run where you check that your workloads function correctly on Autopilot.
  4. Plan and create the Autopilot cluster.
  5. If applicable, update your infrastructure-as-code tooling.
  6. Perform the migration.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Standard cluster with running workloads.
  * Ensure that you have an Autopilot cluster with no workloads to perform dry-runs. To create a new Autopilot cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## Enable the pre-flight check component in your cluster

In GKE version 1.31.6-gke.1027000 and later, the Autopilot pre-flight check component is disabled by default. You must enable the pre-flight check component before you can run the check in a cluster. If your cluster runs a GKE version earlier than 1.31.6-gke.1027000, skip to the next section.

**Caution:** Enabling the pre-flight check component triggers a control plane update operation that might take up to 30 minutes to complete. The control plane in zonal Standard clusters is unavailable during this time. Regional Standard clusters and Autopilot clusters, which update one control plane replica at a time, remain available.

  * Enable the pre-flight check component in your cluster:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=LOCATION \
            --enable-autopilot-compatibility-auditing
        

Replace the following:

    * `CLUSTER_NAME`: the name of your Standard cluster.
    * `LOCATION`: the location of your Standard cluster, such as `us-central1`.

The update operation takes up to 30 minutes to complete.




## Run a pre-flight check on your Standard cluster

The Google Cloud CLI and the Kubernetes Engine API provide a _pre-flight check_ tool that validates the specifications of your running Standard workloads to identify incompatibilities with Autopilot clusters. This tool is available in GKE version 1.26 and later.

  * To use this tool on the command-line, run the following command:


    
    
    gcloud container clusters check-autopilot-compatibility CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of your Standard cluster. Optionally, add `--format=json` to this command to get the output in a JSON file.

The output contains findings for all your running Standard workloads, categorized and with actionable recommendations to ensure compatibility with Autopilot, where applicable. The following table describes the categories:

Pre-flight tool results  
---  
`Passed` | The workload will run as expected with no configuration needed for Autopilot.   
`Passed with optional configuration` | The workload will run on Autopilot, but you can make optional configuration changes to optimize the experience. If you don't make configuration changes, Autopilot applies a default configuration for you. For example, if your workload was running on N2 machines in Standard mode, GKE applies the general-purpose [_compute class_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes) for Autopilot. You can optionally modify the workload to request the Balanced compute class, which is backed by N2 machines.  
`Additional configuration required` | The workload won't run on Autopilot unless you make a configuration change. For example, consider a container that uses the NET_ADMIN capability in Standard. Autopilot drops this capability by default for improved security, so you'll need to enable NET_ADMIN on the cluster before you deploy the workload.  
`Incompatibility` | The workload won't run on Autopilot because it uses functionality that Autopilot doesn't support. For example, Autopilot clusters reject privileged Pods (`privileged: true` in the Pod specification) to improve the default security posture. The only way to run that application in Autopilot would be to remove the privileged setting.  
  
## Modify your workload specifications based on the pre-flight results

After you run the pre-flight check, step through the JSON output and identify workloads that need to change. We recommend implementing even the optional configuration recommendations. Each finding also provides a link to documentation that shows you what the workload specification should look like.

The most important difference between Autopilot and Standard is that infrastructure configuration in Autopilot is automated based on the workload specification. Kubernetes scheduling controls, such as node taints and tolerations, are automatically added to your running workloads. If necessary, you should also modify your infrastructure-as-code configurations, such as Helm charts or Kustomize overlays, to match.

**Note:** As a best practice, make copies of your original workload specifications so that rolling back your migration takes less time.

Some common configuration changes you'll need to make include the following:

Common configuration changes for Autopilot  
---  
Compute and architecture configuration | Autopilot clusters use the E-series machine type by default. If you need other machine types, your workload specification must request a compute class, which tells Autopilot to place those Pods on nodes that use specific machine types or architectures. For details, see [Compute classes in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes).  
Accelerators | GPU-based workloads must request GPUs in the workload specification. Autopilot automatically provisions nodes with the required machine type and accelerators. For details, see [Deploy GPU workloads in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus).  
Resource requests | All Autopilot workloads need to specify values for `resources.requests` in the Pod specification. GKE uses these values to provision appropriate machine sizes to run the Pods. Autopilot has specific automatically applied default requests if you omit any, and enforces specific minimums and maximums based on the compute class or hardware request of your workload. For details, see [Resource requests in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests).  
Fault-tolerant workloads on Spot VMs | If your workloads run on Spot VMs in Standard, request Spot Pods in the workload configuration by setting a node selector for `cloud.google.com/gke-spot=true`. For details, see [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods).  
  
## Perform a dry-run on a staging Autopilot cluster

After you modify each workload manifest, do a dry-run deployment on a new staging Autopilot cluster to ensure that the workload runs as expected.

### Command line

Run the following command:
    
    
    kubectl create --dry-run=server -f=PATH_TO_MANIFEST
    

Replace `PATH_TO_MANIFEST` with the path to the modified workload manifest.

### IDE

If you use the Cloud Shell Editor, the dry-run command is built-in and runs on any open manifests. If you use Visual Studio Code or Intellij IDEs, install the Cloud Code extension to automatically run the dry-run on any open manifests.

The **Problems** pane in the IDE shows any dry-run issues, such as in the following image which shows a failed dry-run for a manifest that specified `privileged: true`.

![Output of dry-run in Visual Studio code for a manifest named application.yaml. The message reads as follows: Failed server dry-run apply on current-context: admission webhook denied the request.](https://docs.cloud.google.com/static/kubernetes-engine/images/autopilot_dry_run_privileged_fail.png)

## Plan the destination Autopilot cluster

When your dry-run no longer displays issues, plan and create the new Autopilot cluster for your workloads. This cluster is different from the Autopilot cluster that you used to test your manifest modifications in the preceding section.

Use [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview) for basic configuration requirements. Then, read the [Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), which provides information specific to your use case at different layers.

Additionally, consider the following:

  * Autopilot clusters are VPC-native, so we don't recommend migrating to Autopilot from routes-based Standard clusters.
  * Use the same or a similar VPC for the Autopilot cluster and the Standard cluster, including any custom firewall rules and VPC settings.
  * Autopilot clusters use GKE Dataplane V2 and only support Cilium NetworkPolicies. Calico NetworkPolicies are not supported.
  * If you want to use IP masquerading in Autopilot, use an [Egress NAT policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/egress-nat-policy-ip-masq-autopilot).
  * Specify the [primary IPv4 range](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--cluster-ipv4-cidr) for the cluster during cluster creation, with the same range size as the Standard cluster.
  * Learn about the [quota differences](https://docs.cloud.google.com/kubernetes-engine/quotas) between modes, especially if you have large clusters.
  * Learn about the [Pods-per-node maximums](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#max_pods_default) for Autopilot, which are different from Standard. This matters more if you use node or Pod affinity often.
  * All Autopilot clusters use [Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery).



### Create the Autopilot cluster

When you're ready to create the cluster, use [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster). All Autopilot clusters are regional and are automatically enrolled in a release channel, although you can specify the channel and cluster version. We recommend deploying a small sample workload to the cluster to trigger node auto-provisioning so that your production workloads can schedule immediately.

## Update your infrastructure-as-code tooling

The following infrastructure-as-code providers support Autopilot:

  * [Terraform](https://www.hashicorp.com/blog/terraform-adds-support-for-gke-autopilot)
  * [Crossplane](https://github.com/crossplane-contrib/provider-gcp/blob/master/examples/gke/autopilot.yaml)
  * [Pulumi](https://github.com/crossplane-contrib/provider-gcp/blob/master/examples/gke/autopilot.yaml)
  * [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview)



Read your preferred provider's documentation and modify your configurations.

## Choose a migration approach

The migration method that you use depends on your individual workload and how comfortable you are with networking concepts such as [multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services) and [multi-cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress), as well as how you manage the state of the Kubernetes objects in your cluster.

Workload type | Pre-flight tool results | Migration approach  
---|---|---  
Stateless | 

  * Passed
  * Passed with optional configuration
  * Additional configuration required

| 

  * **No downtime:** Update your Kubernetes manifests if applicable and redeploy on Autopilot. Use multi-cluster Ingress and multi-cluster Services for traffic cutover. For high-level steps, see Manually migrate stateless workloads with no downtime.
  * **Downtime:** Update your Kubernetes manifests if applicable and redeploy on Autopilot during scheduled downtime. Change your DNS records to the new IP addresses of your Services and end downtime. For high-level steps, see Alternative: Manually migrate all workloads during downtime.

For `Passed` and `Passed with optional configuration` workloads, you can also use Backup for GKE to move all workloads to the Autopilot cluster. You must still update your pipeline and upstream manifests to target the Autopilot cluster. For high-level steps, see Migrate all workloads using Backup for GKE.  
Stateful | 

  * Passed
  * Passed with optional configuration

|  Use one of the following methods:

  * **Backup for GKE:** Use Backup for GKE to move stateful workloads to the Autopilot cluster while maintaining existing PersistentVolume relationships. For high-level steps, see Migrate all workloads using Backup for GKE. Cross-regional migration is supported.
  * **Manual:** Move the stateful workloads manually. This approach requires more careful planning for the PersistentVolumes and Compute Engine disks. For high-level steps, see Manually migrate stateful workloads. Cross-regional migration is not supported.

All stateful workload migrations require downtime to avoid data loss.  
Additional configuration required | Update your Kubernetes manifests and redeploy on Autopilot during scheduled downtime. For high-level steps, see Manually migrate stateful workloads.  
  
## High-level migration steps

Before you begin a migration, ensure that you resolved any `Incompatible` or `Additional configuration required` results from the pre-flight check. If you deploy workloads with those results on Autopilot without modifications, the workloads will fail.

The following sections are a high-level overview of a hypothetical migration. Actual steps will vary depending on your environment and each of your workloads. Plan, test, and re-test workloads for issues before migrating a production environment. Considerations include the following:

  * The duration of the migration process depends on how many workloads you're migrating.
  * Downtime is _required_ while you migrate stateful workloads.
  * Manual migration lets you focus on individual workloads during the migration so that you can resolve issues in real time on a case-by-case basis.
  * In all cases, ensure that you migrate Services, Ingresses, and other Kubernetes objects that facilitate the functionality of your stateless and stateful workloads.

**Tip:** Always communicate an upcoming migration to your end-users and warn them about potential service disruptions and downtime.

### Migrate all workloads using Backup for GKE

**Caution:** This approach requires downtime for your cluster, for both stateful and stateless workloads. Notify your users of the upcoming downtime.

If all the workloads (stateful and stateless) running in your Standard cluster are compatible with Autopilot and the preflight tool returns either `Passed` or `Passed with optional configuration` for every workload, you can use [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) to back up the entire state of your Standard cluster and workloads and restore the backup onto the Autopilot cluster.

This approach has the following benefits:

  * You can move all workloads from Standard to Autopilot operation with minimal configuration needed.
  * You can move stateless and stateful workloads and retain the relationships between workloads, as well as associated PersistentVolumes.
  * Rollbacks are intuitive and managed by Google. You can roll the entire migration back or selectively roll back specific workloads.
  * You can migrate stateful workloads across Google Cloud regions. Manual migration of stateful workloads can only happen in the same region.



When you use this method, GKE applies Autopilot default configurations to workloads that received a `Passed with optional configuration` result from the pre-flight tool. Before you migrate these workloads, ensure that you're comfortable with those defaults.

### Manually migrate stateless workloads with no downtime

To migrate stateless workloads with no downtime for your services, you register the source and destination clusters to a [GKE Fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts) and use multi-cluster Services and multi-cluster Ingress to ensure that your workloads remain available during the migration.

  1. Enable multi-cluster Services and multi-cluster Ingress for your source cluster and your destination cluster. For instructions, see [Configuring multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services) and [Setting up Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup).
  2. If you have backend dependencies such as a database workload, export those Services from your Standard cluster using multi-cluster Services. This lets workloads in your Autopilot cluster access the dependencies in the Standard cluster. For instructions, see [Registering a Service for export](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#registering_a_service_for_export).
  3. Deploy a multi-cluster Ingress and a multi-cluster Service to control inbound traffic between clusters. Configure the multi-cluster Service to only send traffic to the Standard cluster. For instructions, see [Deploying Ingress across clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress#features).
  4. Deploy your stateless workloads with updated manifests to the Autopilot cluster. Your exported multi-cluster Services automatically match and send traffic to the corresponding stateful workloads.
  5. Update your multi-cluster Service to direct inbound traffic to the Autopilot cluster. For instructions, see [Cluster selection](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress#cluster_selection).



You're now serving your stateless workloads from the Autopilot cluster. If you only had stateless workloads in the source cluster, and no dependencies remain, proceed to Complete the migration. If you have stateful workloads, proceed to Manually migrate stateful workloads.

### Manually migrate stateful workloads

After migrating your stateless workloads, you must quiesce and migrate your stateful workloads from the Standard cluster. This step requires downtime for your cluster.

**Note:** Your source and destination clusters must be in the same Google Cloud region to manually migrate existing persistent disks. If you need to migrate the stateful workloads to a cluster in a different region, use Backup for GKE.

  1. Start your environment downtime.
  2. Quiesce your stateful workloads.
  3. Ensure that you modified your workload manifests for Autopilot compatibility. For details, see Modify your workload specifications based on the pre-flight results.
  4. Deploy the workloads on your Autopilot cluster.

**Note:** Migrate persistent data by re-deploying your PersistentVolumeClaims to use your existing Compute Engine disks. For instructions, see [Using pre-existing persistent disks as PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/preexisting-pd).
  5. Deploy the Services for your stateful workloads on the Autopilot cluster.

  6. Update your in-cluster networking to let your stateless workloads continue to communicate with their backend workloads:

     * If you used a static IP address in your Standard cluster backend Services, reuse that IP address in Autopilot.
     * If you let Kubernetes assign an IP address, deploy your backend Services, get the new IP address, and update your DNS to use the new IP address.



At this stage, the following should be true:

  * You're running all your stateless workloads in Autopilot.
  * Any backend stateful workloads are also running in Autopilot.
  * Your stateless and stateful workloads can communicate with each other.
  * Your multi-cluster Service directs all inbound traffic to your Autopilot cluster.



When you've migrated all the workloads and Kubernetes objects to the new cluster, proceed to Complete the migration.

### Alternative: Manually migrate all workloads during downtime

**Caution:** This approach requires downtime for your cluster, for both stateful and stateless workloads. Notify your downstream users of the upcoming downtime.

If you don't want to use multi-cluster Services and multi-cluster Ingress to migrate workloads with minimal downtime, migrate all your workloads during downtime. This method results in longer downtime for your services, but doesn't require working with multi-cluster features.

  1. Start your downtime.
  2. Deploy your stateless manifests on the Autopilot cluster.
  3. Manually migrate your stateful workloads. For instructions, see the Manually migrate stateful workloads section.
  4. Modify DNS records for both intra-cluster and inbound external traffic to use the new IP addresses of Services.
  5. End your downtime.



## Complete the migration

After moving all your workloads and Services to the new Autopilot cluster, end your downtime and allow your environment to soak for a predetermined duration. When you're satisfied with the state of your migration and are sure that you won't need to roll the migration back, you can clean up migration artifacts and complete the migration.

### Optional: Clean up multi-cluster features

If you used multi-cluster Ingress and multi-cluster Services to migrate, and you don't want your Autopilot cluster to remain registered to a Fleet, do the following:

  1. For inbound external traffic, deploy an Ingress and set it to the IP address of the Services that expose your workloads. For instructions, see [Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb).
  2. For intra-cluster traffic, such as from frontend workloads to stateful dependencies, update cluster DNS records to use the IP addresses of those Services.
  3. Delete the multi-cluster Ingress and the multi-cluster Service resources that you created during the migration.
  4. [Disable multi-cluster Ingress and multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#disabling_mcs).
  5. [Unregister the Autopilot cluster from the Fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister).



### Delete the Standard cluster

After enough time has passed after the migration completes, and you're satisfied with the state of your new cluster, delete the Standard cluster. We recommend that you keep your backed up Standard manifests.

## Roll back a faulty migration

If you experience issues and want to revert to the Standard cluster, do one of the following, depending on how you performed the migration:

  * If you used Backup for GKE to create backups during the migration, restore the backups onto the original Standard cluster. For instructions, see [Restore a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore).

  * If you manually migrated workloads, repeat the migration steps in the previous sections with the Standard cluster as the destination and the Autopilot cluster as the source. At a high-level, this involves the following steps:

    1. Start downtime.
    2. Manually migrate stateful workloads to the Standard cluster. For instructions, see the Manually migrate stateful workloads section.
    3. Move stateless workloads to the Standard cluster using the original manifests that you backed up prior to the migration.
    4. Deploy your Ingress to the Standard cluster and cutover your DNS to the new IP addresses for Services.
    5. Delete the Autopilot cluster.



## What's next

  * [Plan Autopilot resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests)
  * [Set up monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/gke)
  * [Set up and use the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
