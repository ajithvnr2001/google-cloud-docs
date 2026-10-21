---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-privileged-allowlists/
title: Create allowlists for privileged workloads in Autopilot \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:10.879693+00:00
---

# Create allowlists for privileged workloads in Autopilot  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-privileged-allowlists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Create allowlists for privileged workloads in Autopilot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

**Note:** Running your own privileged workloads in Autopilot is available only to eligible Google Cloud customers. To request access to this feature, contact [Cloud Customer Care](https://cloud.google.com/support-hub).

This document shows you how to create _allowlists_ that let you deploy privileged workloads in your Autopilot nodes. You store these allowlists in Cloud Storage buckets. This document is for platform admins and operators who want to exempt specific customer-owned workloads from the default Autopilot security constraints for specific Kubernetes workloads. You should already be familiar with [privileged workload admission control in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads).

## About privileged workloads in Autopilot

Autopilot mode enforces a default set of constraints on workloads to improve your security posture. You can bypass these constraints to run specific privileged workloads by installing _allowlists_ that correspond to those workloads. By default, any Autopilot or Standard cluster lets you install allowlists from Autopilot partners and specific open source projects.

Eligible GKE customers can create and manage allowlists for their own privileged workloads that aren't compatible with the default Autopilot constraints. These allowlists are WorkloadAllowlist Kubernetes custom resources that you define in YAML files and store in Cloud Storage buckets. Identity and account admins use organization policies to let you configure your clusters to recognize these customer-managed allowlists and buckets. Cluster admins can install these allowlists so that the privileged workloads can run in Autopilot mode.

For more information about the process and the people involved, see [How privileged Autopilot workload admission control works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-privileged-workloads#how-it-works).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Cloud Storage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storage.googleapis.com)

  * Ensure that you have a GKE cluster that runs version 1.35 or later. You can also [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) for this task.
  * Verify that you have a Cloud Storage bucket that you can use to store allowlist files. You can also [create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for this task.
  * Open the YAML manifest that defines the privileged workload that you want to run in Autopilot.



### Required roles

To get the permissions that you need to store allowlists in Cloud Storage and configure synchronization, ask your administrator to grant you the following IAM roles on your bucket: 

  * Store allowlists in your bucket: [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) 
  * Give access to the GKE service agent: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create and upload a WorkloadAllowlist

Allowlists are WorkloadAllowlist custom resources that you define in YAML files. The fields in the specification of a WorkloadAllowlist are similar to the fields in a Kubernetes Pod specification. When you install an allowlist in your cluster and deploy a privileged workload, GKE validates the privileged workload specification against the installed allowlist. The workload can run only if all of the fields in the allowlist specification match the corresponding fields in the workload specification.

To create a new WorkloadAllowlist and upload it to your Cloud Storage bucket, follow these steps:

  1. Identify the privileged workload to allowlist.
  2. Add the following annotation to the `metadata.annotations` field in your Pod specification:
         
         cloud.google.com/generate-allowlist: "true"
         

For Pods that are managed by a controller, such as a DaemonSet or a Deployment, add the annotation to the `spec.template.metadata.annotations` field.

**Note:** To use this annotation on a cluster that existed before your project or organization was granted access to the feature, you must first issue any `gcloud container clusters update` command with the `--autopilot-privileged-admission` flag set. If you haven't yet configured any custom allowlist paths, you can maintain the GKE default behavior by using the `--autopilot-privileged-admission=gke://*` flag. For more information, see the documentation for the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--autopilot-privileged-admission) command.
  3. Attempt to create the privileged workload in your cluster:
         
         kubectl apply -f WORKLOAD_FILE_PATH
         

Replace WORKLOAD_FILE_PATH with the path to your workload manifest file. GKE rejects the workload with an error message that includes a WorkloadAllowlist manifest. The output is similar to the following:
         
         This workload can be enabled using the following Custom Resource. To be used in-cluster, the WorkloadAllowlist must be uploaded to Google Cloud Storage and then installed using an AllowlistSynchronizer. Refer to https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-privileged-allowlists.
         
         Note that many common partner workloads are already allowlisted. These can be installed directly using an AllowlistSynchronizer. Refer to https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners.
         ---
         **apiVersion: auto.gke.io/v1
         kind: WorkloadAllowlist
         metadata:
             name: test-pod-allowlist-2025-09-11t22-40-37
             annotations:
                 autopilot.gke.io/no-connect: "true"
         exemptions:
             - autogke-disallow-privilege
         matchingCriteria:
             containers:
                 - name: pause-container2
                   image: k8s.gcr.io/pause2
                   securityContext:
                     privileged: true**
         

  4. In a text editor, create a YAML file that contains the generated WorkloadAllowlist.

**Best practice** : 

Use a versioning scheme for your allowlist files. Versioned files help you to keep file names unique in the bucket.

  5. Set the `metadata.name` field of the allowlist. **Best practice** : 

Set the allowlist name to the same value as the filename. This practice ensures that the allowlist name is unique within your Cloud Storage bucket. Attempting to install multiple allowlists with the same name can lead to unexpected behavior.

  6. Optional: Generalize the WorkloadAllowlist so that it can exempt similar workloads. Use one of the following methods:

     * Specific fields support regular expressions, such as `matchingCriteria.containers[*].image` and `matchingCriteria.containers[*].args`. Use a regular expression that matches multiple values across different workloads.

     * Specific fields, such as `matchingCriteria.containers` and `matchingCriteria.securityContext.capabilities.add`, match any workload with a subset of the values from the WorkloadAllowlist. In the WorkloadAllowlist, specify additional values to match other workloads.

For more information about all of the supported fields and values that you can use, see the [WorkloadAllowlist CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/workloadallowlist).

  7. [Upload the manifest file to your Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).




If your organization policies allow the installation of allowlists from your bucket in clusters, cluster admins can do the following:

  1. Add your allowlist paths to a cluster.
  2. Create an AllowlistSynchronizer to install the allowlists from your bucket.



For more information about how to configure a cluster and install allowlists, see [Control privileged workload admission in Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads).

## Example allowlist configuration

The `matchingCriteria` field in a WorkloadAllowlist specification has a similar structure to the Kubernetes Pod specification. The [WorkloadAllowlist CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/workloadallowlist) is the source of truth for all of the fields, values, and expressions that you can use.

This section shows you an example allowlist that matches a workload that has the following properties:

  * The `container-1` container in the workload runs in privileged mode.
  * The workload mounts the `/var/log/` directory from the node file system in write mode.


  1. Review the example workload:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: example-privileged-workload
           labels:
             env: dev
         spec:
           selector:
             matchLabels:
               env: dev
           template:
             metadata:
               labels:
                 env: dev
             spec:
               containers:
               - name: container-1
                 image: example-image-1
                 resources:
                   requests:
                     cpu: "400m"
                     memory: "4Gi"
                 # Run the container in privileged mode
                 securityContext:
                   privileged: true
               - name: container-2
                 image: example-image-2
                 volumeMounts:
                 - name: write-varlog
                   mountPath: /logs
                   readOnly: false
               # Mount a host directory
               volumes:
               - name: write-varlog
                 hostPath:
                   path: /var/log
                   type: Directory
         

By default, Autopilot rejects this workload.

  2. Review the example WorkloadAllowlist:
         
         apiVersion: auto.gke.io/v1
         kind: WorkloadAllowlist
         minGKEVersion: 1.32.0-gke.1000000
         metadata:
           name: example-privileged-workload
           annotations:
             autopilot.gke.io/no-connect: "true"
         # List of constraints that the allowlist modifies
         **exemptions :
         - autogke-disallow-privilege
         - autogke-no-write-mode-hostpath
         matchingCriteria:
           containers:
           - name: container-1
             image: example-image-1
             securityContext:
               privileged: true
           - name: container-2
             image: example-image-2
             volumeMounts:
             - name: write-varlog
               mountPath: /logs
               readOnly: false
           volumes:
           - name: write-varlog
             hostPath:
               path: /var/log**
         

This WorkloadAllowlist has the following properties:

     * The values in the `exemptions` field specify the Autopilot constraints that the allowlist bypasses.
     * The values in the `matchingCriteria` field specify the containers that the example workload uses and the fields that would normally violate Autopilot constraints.

The allowlist has only the values for fields that violate constraints. Other fields in the workload, such as the `resources.requests` field, are ignored.




When you install this example WorkloadAllowlist in a cluster, GKE allows the privileged workload to run in that cluster. For example, in a Standard cluster that has Autopilot nodes, installing this WorkloadAllowlist lets the privileged workload run on the Autopilot nodes.

## Grant access to the GKE service agent

To synchronize allowlists from your bucket in a cluster, the [GKE service agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#kubernetes-engine-service-agent) in the cluster project requires the following IAM roles:

  * [Storage Bucket Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.bucketViewer) (`roles/storage.bucketViewer`)
  * [Storage Object Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)



To grant these roles to the service agent, follow these steps:

  1. Find the project number of your cluster project:
         
         gcloud projects describe CLUSTER_PROJECT_ID \
             --format='value(projectNumber)'
         

  2. Grant the `roles/storage.bucketViewer` role:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
             --project=BUCKET_PROJECT_ID \
             --role=roles/storage.bucketViewer
         

Replace the following:

     * `BUCKET_NAME`: the name of your Cloud Storage bucket.
     * `CLUSTER_PROJECT_NUMBER`: the project number of the cluster project, from the output of the previous step.
     * `BUCKET_PROJECT_ID`: the ID of the project that contains your bucket.
  3. Grant the `roles/storage.objectViewer` role:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
             --project=BUCKET_PROJECT_ID \
             --role=roles/storage.objectViewer
         




## What's next

  * [Add your allowlist paths to an organization policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/privileged-admission-organizations)
  * [Configure clusters and install allowlists](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
