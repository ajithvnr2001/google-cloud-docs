---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads/
title: Control privileged workload admission in Autopilot mode \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:10.622398+00:00
---

# Control privileged workload admission in Autopilot mode  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Control privileged workload admission in Autopilot mode Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

You can run privileged workloads in Google Kubernetes Engine (GKE) Autopilot mode by installing allowlists for those workloads in your clusters. This document shows you how to do the following tasks: 

  * Configure GKE to run only specific privileged workloads in Autopilot mode.
  * Install allowlists for privileged workloads.



This document is for the following types of roles:

  * Security engineers who want to ensure that third-party workloads need an allowlist to run on your clusters and come from GKE-approved sources.
  * Platform engineers who want to enable third-party workloads on clusters to unblock application teams.



You should already be familiar with the following concepts:

  * [About privileged workload admission in Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads)
  * [Kubernetes custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
  * [GKE Autopilot security constraints](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security)
  * [GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners)



## About privileged workloads in Autopilot

Autopilot mode enforces a default set of constraints on workloads to improve your security posture. You can modify these constraints to run specific privileged workloads by installing _allowlists_ that correspond to those workloads. By default, Autopilot lets you install allowlists from Autopilot partners and specific open source projects. Eligible GKE customers can also create allowlists for customer-owned privileged workloads that they upload to Cloud Storage buckets.

Each allowlist is a file that matches a specific privileged workload. To run a privileged workload, you do the following:

  1. Configure the cluster to allow the installation of allowlists from specific paths. By default, all allowlists from Autopilot partners and approved open source projects are supported.
  2. Create an [AllowlistSynchronizer](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#allowlist-installation) in the cluster that installs the allowlist and keeps the allowlist up-to-date.



### Bugs and feature requests for privileged workloads and allowlists

The owner of a privileged workload is responsible for creating, developing, and maintaining their workloads and allowlists. If you encounter a bug or have a feature request for a privileged workload or allowlist, contact the corresponding owner.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Verify that you can configure clusters to install allowlists from your selected source. Organization administrators can use an organization policy to control the paths that you can add to a cluster. For more information, see [Organization Policy Service managed constraint for allowlists](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#about-managed-constraint).
  * For customer-owned privileged workloads that are available to eligible GKE customers, verify both of the following conditions:

    * Your organization administrator added your allowlist bucket path to an organization policy. For more information, see [Restrict privileged GKE workloads in organizations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations).
    * The allowlist that you want to install is in the Cloud Storage bucket. For more information, see [Create allowlists for privileged Autopilot workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-privileged-allowlists).



### Requirements

  * The AllowlistSynchronizer custom resource requires GKE version 1.32.2-gke.1652000 or later.
  * You must know which privileged workload you want to run in your cluster.
  * To modify the allowlist path configuration for a cluster, your cluster must run GKE version 1.35 or later.



## Configure allowlist paths for a cluster

This section shows you how to configure a cluster to support the installation of allowlists from a set of approved paths. By default, Autopilot supports allowlist installation from GKE partners and approved open source projects. You can modify this default configuration for individual clusters. You can also specify approved allowlist sources for an entire organization, folder, or project by [using an organization policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations).

  1. Identify the paths to allowlist files to add to the cluster. You can specify multiple paths when you create or update your cluster. You can also disable allowlist installation from any source by specifying an empty string instead of a path. For more information about the paths that you can specify, see [Allowlist paths](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#allowlist-paths).

  2. To control the approved allowlist sources for a cluster, use the `--autopilot-privileged-admission` flag when you create or update an Autopilot or Standard cluster, like in the following command:
         
         gcloud container clusters create-auto CLUSTER_NAME \
             --location=LOCATION \
             --autopilot-privileged-admission=ALLOWLIST1_PATH,ALLOWLIST2_PATH,...
         

Replace the following:

     * `CLUSTER_NAME`: a name for your new cluster.
     * `LOCATION`: the location of the cluster control plane, such as `us-central1`.
     * `ALLOWLIST1_PATH,ALLOWLIST2_PATH,...`: a comma-separated list of paths to allowlist files or directories. For example, `gke://*,gs://my-agent/privileged-logging-agent.yaml`. You can also disable allowlist installation from any source by specifying an empty string (`""`).

**Caution:** The `gke://*` path allows WorkloadAllowlists from all GKE-approved sources, which is the default Autopilot behavior. If you omit this value when you use the `--autopilot-privileged-admission` flag, the cluster can't run any GKE-approved allowlist.



If you update an existing cluster without specifying the `--autopilot-privileged-admission` flag, the existing path configuration for that cluster doesn't change. You don't have to specify this flag every time that you update a cluster.

After the cluster creation or update operation completes, you can install allowlists from the specified paths by creating AllowlistSynchronizers.

**Note:** Running your own privileged workloads in Autopilot is available only to eligible Google Cloud customers. If your command fails with a message like `Cluster is not authorized to use custom allowlist paths`, then you don't yet have access. For more information, see [Sources of privileged Autopilot workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#privileged-workload-sources).

## Create a new AllowlistSynchronizer

To run a privileged workload, you add the path to the corresponding allowlist file to an AllowlistSynchronizer specification in a YAML file. You then deploy the AllowlistSynchronizer to your cluster.

**Best Practice:** Create separate AllowlistSynchronizers for the specific applications or teams that the corresponding workloads support. 

  1. In a text editor, create a new YAML file.
  2. Add the following content to the YAML file:
         
         apiVersion: auto.gke.io/v1
         kind: AllowlistSynchronizer
         metadata:
           name: ALLOWLIST_SYNCHRONIZER_NAME
         spec:
           allowlistPaths:
           - ALLOWLIST1_PATH
           - ALLOWLIST2_PATH
         

Replace the following:

     * `ALLOWLIST_SYNCHRONIZER_NAME`: the name of the new synchronizer. Choose a descriptive name that identifies the workload or team that the allowlist supports.
     * `ALLOWLIST1_PATH, ALLOWLIST2_PATH, ...`: a list of paths to allowlist files or directories that you want to install, such as in the following example for GKE-approved allowlists:
           
           allowlistPaths:
           - Gke-Org/accelerators/*
           - Wiz/wiz-sensor/v1/wiz-sensor-v1.yaml
           

Or in the following example for customer-owned allowlists:
           
           allowlistPaths:
           - my-agent/log-collector/*
           - my-agent/privileged-logging-agent.yaml
           

The cluster configuration must support the paths that you specify, as described in the Configure allowlist paths for a cluster section. Additionally, each AllowlistSynchronizer must contain either exclusively GKE-approved allowlists, for exclusively customer-owned allowlists.

  3. If you install allowlists from a [ customer-owned Cloud Storage bucket](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#customer-owned-privileged-workloads), add the `spec.projectNumber` and `spec.bucketName` fields to your AllowlistSynchronizer. For more details, see the [ AllowlistSynchronizer CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/allowlistsynchronizer).

  4. Deploy the YAML file to your cluster:
         
         kubectl apply -f PATH_TO_YAML_FILE
         

Replace `PATH_TO_YAML_FILE` with the path to the YAML file that you created in the previous step.

The AllowlistSynchronizer controller installs allowlist files from the specified paths in your cluster.

  5. Wait until the synchronizer reports a `Ready` status:
         
         kubectl wait --for=condition=Ready allowlistsynchronizer/ALLOWLIST_SYNCHRONIZER_NAME \
             --timeout=60s
         




You can also integrate allowlist installation and privileged workload deployment into your continuous integration and continuous deployment (CI/CD) pipeline. Configure your workflow to wait until the allowlist successfully installs before deploying the corresponding workload.

## Update an existing AllowlistSynchronizer

You can update an existing AllowlistSynchronizer to add or remove allowlist files. You might update existing synchronizers in situations like the following:

  * The workload owner adds a new allowlist file that has a different name.
  * You want to add a new workload allowlist to an existing synchronizer that groups related allowlists.
  * You want to remove an allowlist from a synchronizer because you no longer want to use the corresponding workload.



To update an existing AllowlistSynchronizer object, do the following:

  1. List the existing synchronizers in your cluster:
         
         kubectl get allowlistsynchronizer
         

  2. Open the specification of the synchronizer that you want to update in a text editor.

**Best Practice:** To ensure that you track changes to synchronizers, update the YAML file that you used to create the synchronizer. Store these files in a version control system. 
  3. Update the `spec.allowlistPaths` field to add, modify, or remove allowlist file paths.

  4. Save and close the text editor.

  5. Apply the updated configuration to the cluster:
         
         kubectl apply -f PATH_TO_YAML_FILE
         

Replace `PATH_TO_YAML_FILE` with the path to the YAML file that you updated in the previous step.




When you deploy an updated synchronizer configuration, the `managedAllowlistStatus.generation` field in the status of the AllowlistSynchronizer object increments by one. The AllowlistSynchronizer controller then applies your changes.

## Monitor the status of allowlist synchronization

After you install an AllowlistSynchronizer or update an existing synchronizer, you can monitor the synchronization status. The status helps you to track the installation, removal, or modifications of allowlist files as well as any errors that might occur.

To monitor the general status of the synchronization, run the following command:
    
    
    kubectl get allowlistsynchronizer ALLOWLIST_SYNCHRONIZER_NAME -o yaml
    

The output is similar to the following:
    
    
    ...
    status:
      conditions:
      - type: Ready
        status: "False"
        reason: "SyncError"
        message: "some allowlists failed to sync: example-allowlist-1.yaml"
        lastTransitionTime: "2024-10-12T10:00:00Z"
        observedGeneration: 2
      managedAllowlistStatus:
        - filePath: "gs://path/to/example-allowlist-2.yaml"
          generation: 1
          phase: Installed
          lastSuccessfulSync: "2024-10-10T10:00:00Z"
        - filePath: "gs://path/to/example-allowlist-1.yaml"
          phase: Failed
          lastError: "Initial install failed: invalid contents"
          lastSuccessfulSync: "2024-10-08T10:00:00Z"
    

In this example output, the `example-allowlist-1.yaml` allowlist failed to synchronize, and the `example-allowlist-2.yaml` allowlist was successfully installed. For a description of these fields, see [AllowlistSynchronizer status](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/allowlistsynchronizer#allowlistsynchronizer_status).

## Verify that an allowlist exists in your cluster

To verify that an allowlist exists in your cluster, run the following command:
    
    
    kubectl get workloadallowlist
    

The output is a list of the installed allowlists in the cluster. Check that the output includes the allowlist that you want to use.

## Deploy the privileged workload

After an allowlist installs successfully, you can deploy the corresponding workload in your cluster. The workload owner should also provide you with installation instructions for the workload. For a list of Autopilot partners and links to their documentation, see [Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).

### Use private image mirror repositories

You can mirror the container images of privileged workloads in private repositories that you own. To run these mirrored images in a workload, you must meet all of the following requirements:

  * The SHA-256 digest of the mirrored image must match the image digest of the publicly-available workload.
  * The SHA-256 image digest that you specify must exist in the `WorkloadAllowlist` object that is synchronized to your cluster.



If the workload supports mirrored images, the allowlist specification for that workload contains a list of image digests to the `containers.imageDigests` field in the allowlist specification for that workload. Typically, this field has a separate digest for every available version of the container image. To view this list of image digests, do the following:

  1. Verify that the allowlist exists in your cluster.
  2. Get the specification of the installed allowlist:
         
         kubectl get workloadallowlist ALLOWLIST_NAME -o yaml
         

Replace `ALLOWLIST_NAME` with the name of the installed allowlist. For example, `company-name-solution-v1.0.0`.

For workloads that support this feature, the output is similar to the following. The `imageDigests` field has a list of allowed digests.
         
         # lines omitted for clarity
         - containerName: pause-container1
           imageDigests:
           - cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229
           - 932ea160d395f3d7f76c0c17a52a63c4cfe1836a900f1058b6bc20b16fd10d23
         

If the output doesn't include an `imageDigests` field, or if the digest for the release that you want to use isn't in the list, contact the workload owner directly and ask them to update their allowlist. After the workload owner adds image digests to their allowlist, the allowlist synchronizer in your cluster automatically installs the updated allowlist.

  3. Add one of the supported image digests to your workload manifest.




For example, consider the following image in a partner's publicly-available Pod specification:
    
    
    ...
      containers:
      - name: pause-container1
        **image : partner-repo/pause1@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229**
        securityContext:
          privileged: true
    

You can use a mirrored image if the digest matches the publicly-available digest, such as in the following example:
    
    
    ...
      containers:
      - name: pause-container1
        **image : my-private-repo/pause1@sha256:cb5c1bddd1b5665e1867a7fa1b5fa843a47ee433bbb75d4293888b71def53229**
        securityContext:
          privileged: true
    

You must include the SHA-256 digest in your image field, similar to the preceding example. If the digests don't match, the mirrored image won't run. To preserve image digests when you mirror partner images, consider using a tool like [crane](https://github.com/google/go-containerregistry/blob/main/cmd/crane/README.md), [ORAS](https://oras.land/), or [skopeo](https://github.com/containers/skopeo).

## Delete a privileged workload

To stop allowing a privileged workload to run in your clusters, remove the path to the corresponding allowlist from your AllowlistSynchronizer. The synchronizer uninstalls the allowlist.

If you delete a `WorkloadAllowlist` object from your cluster instead of updating the synchronizer, the synchronizer re-installs the allowlist. Ensure that you remove the path from the AllowlistSynchronizer.

To uninstall an allowlist, do the following:

  1. In the YAML manifest for the AllowlistSynchronizer that manages the allowlist, remove the path to the allowlist that you want to uninstall. For instructions, see the Update an existing AllowlistSynchronizer section.
  2. To verify that the allowlist was uninstalled, get a list of `WorkloadAllowlist` objects in your cluster:
         
         kubectl get workloadallowlist
         

In the output, ensure that the allowlist that you wanted to remove doesn't appear.

  3. Delete the workload from your cluster. For instructions, see the workload provider's documentation.




## Prevent allowlist installation in your clusters

To prevent the installation of privileged workload allowlists in specific clusters, specify an empty string (`""`) in the `--autopilot-privileged-admission` flag when you create or update a cluster.

  * To disable specific allowlist paths for a cluster, omit the paths to those allowlists when you create or update a cluster:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=LOCATION \
            --autopilot-privileged-admission=ALLOWLIST1_PATH,ALLOWLIST2_PATH,...
        

Replace `ALLOWLIST1_PATH,ALLOWLIST2_PATH,...` with a comma-separated list of paths to allowlist sources. Omit the paths that you want to disable.

  * To disable all allowlists in an existing cluster, specify an empty string as the approved path:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=LOCATION \
            --autopilot-allowlist-paths=""
        

**Caution:** This operation disables the installation of all allowlists, including allowlists for partner workloads and approved open source workloads. Verify that your running applications have no dependencies on these workloads.



## Troubleshoot

If the synchronization or the workload deployment fail, see [Troubleshoot deploying privileged Autopilot workloads](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-privileged-workloads).

## What's next

  * Learn about the available workloads from [GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners)
  * [Run privileged open-source workloads on GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads)
  * Learn about the default [GKE Autopilot security capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security)
  * Read the [AllowlistSynchronizer CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/allowlistsynchronizer)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
