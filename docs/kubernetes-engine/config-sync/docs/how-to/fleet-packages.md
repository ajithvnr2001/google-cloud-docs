---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages/
title: Deploy fleet packages \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:50.709880+00:00
---

# Deploy fleet packages  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Deploy fleet packages Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Config Sync fleet packages to deploy Kubernetes resources across clusters that are registered to a fleet. After you create and deploy a fleet package, when you add a new cluster to your fleet, the fleet package automatically deploys the Kubernetes configuration files in the Git repository to the new cluster.

A `FleetPackage` is a declarative API to deploy Kubernetes raw manifests to a fleet of clusters. Any Kubernetes resources that you want to deploy with a fleet package must be [already-hydrated (WET)](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices#create-wet-repo).

## Before you begin

  1. Create, or make sure you have access to, a Git repository with the Kubernetes resources that you want to deploy across a fleet.

  2. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud`, and `nomos` commands. If you use [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works), the Google Cloud CLI is pre-installed. If you previously installed the Google Cloud CLI, get the latest version by running `gcloud components update`.

**Note:** For existing gcloud CLI installations, make sure to set the `compute/region` and `compute/zone` [properties](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). By setting default locations, you can avoid errors in gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`.
  3. Enable the Config Sync (`anthosconfigmanagement`) API and the `ConfigDelivery` API:
         
         gcloud services enable anthosconfigmanagement.googleapis.com configdelivery.googleapis.com
         

  4. Set a default location:
         
         gcloud config set config_delivery/location us-central1
         

**Note:** the only available location for the `ConfigDelivery` API is `us-central1`.
  5. Set a default project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of the fleet host project.

  6. Ensure that your clusters are [registered to a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).

  7. Use Cloud Build repositories to [create a connection to a supported provider](https://docs.cloud.google.com/build/docs/repositories#2nd-gen-repos) like GitHub or GitLab. When you use a fleet package, you need to set up Cloud Build only once per repository that you want to sync.

**Important:** Your Cloud Build connection must be located in `us-central1` because the Git connection and `FleetPackage` must be in the same region. The `ConfigDelivery` API is available only in `us-central1`.



### Review cluster requirements

Before you install Config Sync on your cluster, review [cluster configuration recommendations and requirements](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/cluster-requirements).

### Prepare your environment

To prepare your environment for Config Sync fleet packages, [grant the required IAM roles to the user registering the cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/prerequisites#grant_iam_roles).

## Install Config Sync

You can install Config Sync with either the Google Cloud console or Google Cloud CLI.

### Console

To install Config Sync, all clusters must be registered to a fleet. When you install Config Sync in the Google Cloud console, selecting individual clusters automatically registers those clusters to your fleet.

  1. In the Google Cloud console, go to the **Config** page under the **Features** section. 

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. Click _add_ **Install Config Sync**.

  3. Under **Installation options** , select **Install Config Sync on entire fleet (recommended)**.

  4. Click **Install Config Sync**. In the **Settings** tab, after a few minutes, you should see **Enabled** in the **Status** column for the clusters in your fleet.




###  gcloud 

  1. Enable the `ConfigManagement` fleet feature:
         
         gcloud beta container fleet config-management enable
         

  2. To enable Config Sync, create a file named `apply-spec.yaml` with the following content:
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: true
         

  3. Apply the `apply-spec.yaml` file:
         
         gcloud beta container fleet config-management apply \
             --membership=MEMBERSHIP_NAME \
             --config=apply-spec.yaml
         

Replace `MEMBERSHIP_NAME` with the fleet membership name that you chose when you registered your cluster. To find the membership name, run the `gcloud container fleet memberships list` command.




## Create a service account for Cloud Build

Fleet packages use Cloud Build to fetch the Kubernetes resources from your Git repository and deploys to your clusters. Cloud Build requires a service account that has the permissions to run this job. To create the service account and grant the required permissions, complete the following steps:

  1. Create the service account:
         
         gcloud iam service-accounts create "SERVICE_ACCOUNT_NAME"
         

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. The name must be an alphanumeric ID between 6 and 30 characters, for example `my-service-account`. After you create a service account, you cannot change its name.

  2. Add an IAM policy binding for the Resource Bundle Publisher role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
            --role='roles/configdelivery.resourceBundlePublisher'
         

If prompted, select `None` as the condition for the policy.

  3. Add an IAM policy binding for the [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
            --role='roles/logging.logWriter'
         

If prompted, select `None` as the condition for the policy.

  4. Add an IAM policy binding for the [Artifact Registry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
            --role='roles/artifactregistry.writer'
         

If prompted, select `None` as the condition for the policy.




## Create a fleet package

To create a fleet package, you define a `FleetPackage` spec that points to the repository with your Kubernetes resources that you connected to Cloud Build. Then you apply the `FleetPackage` which fetches the resources from Git and deploys them across the fleet.

  1. Create a file named `fleetpackage-spec.yaml` with the following content:
         
         resourceBundleSelector:
           cloudBuildRepository:
             name: projects/PROJECT_ID/locations/us-central1/connections/CONNECTION_NAME/repositories/REPOSITORY_NAME
             tag: TAG
             serviceAccount: projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
             path: CONFIG_FILE_PATH
             # Match all files and directories to generate variants
             variantsPattern: "*"
         target:
           fleet:
             project: projects/PROJECT_ID
         rolloutStrategy:
           rolling:
             maxConcurrent: MAX_CLUSTERS
         variantSelector:
           variantNameTemplate: "VARIANT_NAME"
         # set the state to SUSPENDED to pause new rollouts
         # set the state back to ACTIVE to resume rollouts
         # state: SUSPENDED
         

Replace the following:

     * `CONNECTION_NAME`: the name that you chose when you connected your Git host to Cloud Build. You can view all Cloud Build connections in your project by running [`gcloud builds connections list`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/connections/list) or by opening the **Repositories** page in the Google Cloud console:

[Open the Repositories page](https://console.cloud.google.com/cloud-build/repositories)

     * `REPOSITORY_NAME`: the name of your repository. This must be identical to the value entered when you set up your Cloud Build connection.

     * `TAG`: the Git tag of your repository. The format must be the full semantic version with the major, minor, and patch number. For example, `v1.0.0` is a valid tag, while `v1` or `v1.0` are invalid tags.

     * `CONFIG_FILE_PATH`: the path to your Kubernetes resources in the repository. If your files are in the root of the repository, you can omit this field.

     * `MAX_CLUSTERS`: the maximum number of clusters to deploy Kubernetes resources at one time. For example, if you set this to `1`, resource bundles deploy to one cluster at a time.

     * `VARIANT_NAME`: the variant to deploy to your clusters. The name must match a variant in your repository (the filename without extension or the directory name). For example, if you have a file named `prod.yaml`, set this field to `prod`. To use the default behavior (for example, to deploy the same configuration to all clusters in a fleet), set this field to `default` and ensure that your repository contains a file named `default.yaml`.

For a complete list of all fields you can configure, see the [`FleetPackage` reference documentation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest).

  2. Create the fleet package:
         
         gcloud container fleet packages create FLEET_PACKAGE_NAME \
             --source=fleetpackage-spec.yaml
         

Replace `FLEET_PACKAGE_NAME` with a name for your fleet package rollout.

  3. Verify that the fleet package was created:
         
         gcloud container fleet packages list
         

The output lists the status of the build trigger. After a few seconds, the `MESSAGE` field updates with output similar to the following:
         
         MESSAGES: Build status: WORKING. The release is still being built; see the build status on the following page:
         

You can click the link provided to view the streaming logs for the Cloud Build job. It can take a few minutes for Cloud Build to process the build trigger.

If the build trigger is successful, the fleet package starts rolling out the Kubernetes resources across your fleet.

  4. When the build trigger successfully completes, the output of `gcloud container fleet packages list` is similar to the following:
         
         NAME               STATE   CREATE_TIME           ACTIVE_ROLLOUT            LAST_COMPLETED_ROLLOUT  MESSAGES
         my-fleet-package   ACTIVE  2024-07-09T15:15:56   rollout-20240709-153621
         

The fleet package starts rolling out the Kubernetes resources across your fleet.




Now that you've deployed a fleet package, when you add a new cluster to your fleet, the Kubernetes resources defined in the fleet package automatically deploy to the new cluster.

## Update a fleet package

You can update a fleet package to change settings or change the resources that the fleet package deploys, such as in the following examples:

  * Change the rollout strategy by changing the value of the `maxConcurrent` field.
  * Temporarily pause a fleet package by setting `state: SUSPENDED`. When a fleet package is suspended, any in-progress rollouts continue. No new rollouts are created or scheduled until you change the state back to `ACTIVE`.
  * Update the Kubernetes resources that the fleet package deploys by updating the `tag` field to pull from a different Git tag.



To update a fleet package, complete the following steps:

  1. Update your `FleetPackage` spec with your changes.

  2. Update the fleet package:
         
         gcloud container fleet packages update FLEET_PACKAGE_NAME \
             --source=fleetpackage-spec.yaml
         

It can take a few minutes before the change is picked up and starts rolling out to your clusters.




## Inspect resource bundles and releases

When you create or update a fleet package based on your Git repository, the `FleetPackages` API automatically creates _resource bundle_ and _release_ resources. Inspecting these resources is useful for troubleshooting, especially if you need to verify variants generated from your repository.

To inspect resource bundles and releases, use one or more of the following commands:

  * View detailed information about a specific resource bundle:
        
        gcloud container fleet packages resource-bundles describe flpkg-rb-FLEET_PACKAGE_NAME
        

  * List all releases associated with a resource bundle:
        
        gcloud container fleet packages resource-bundles releases list \
            --resource-bundle flpkg-rb-FLEET_PACKAGE_NAME
        

  * View detailed information about a specific release, including which resource bundle it uses. This command is particularly useful for debugging issues related to variants because it lets you inspect exactly which variants were included in a specific release:
        
        gcloud container fleet packages resource-bundles releases describe RELEASE_NAME\
            --resource-bundle flpkg-rb-FLEET_PACKAGE_NAME
        




Replace the following:

  * `FLEET_PACKAGE_NAME`: the name of your fleet package. The resource bundle name is automatically prefixed with `flpkg-rb-`.
  * `RELEASE_NAME`: the name of the release from the `list` command output.



## Manage fleet package rollouts

You can monitor the progress of fleet package deployments and manage active rollouts. When a fleet package is changed, a new rollout is automatically created. The following commands help you get detailed information about rollouts. For example, if you need to debug a deployment issue, you can examine the rollout details, and pause or cancel a rollout if needed.

  1. Listing a rollout lets you see the status of all rollouts tied to a package, including errors that might cause a rollout to fail. To list rollouts and view their status, run the following command:
         
         gcloud container fleet packages rollouts list --fleet-package FLEET_PACKAGE_NAME
         

The output resembles the following:
         
         ROLLOUT                   RELEASE  START_TIME              END_TIME                STATE     MESSAGE
         rollout-20250515-132857   v2-0-0   2025-05-15T13:28:58Z                            STALLED
         rollout-20250418-165528   v1-0-0   2025-04-18T16:55:29Z    2025-04-18T16:57:47Z    COMPLETED
         

  2. Describing a rollout gives you detailed information about a specific rollout, including the status for each targeted cluster and any cluster-specific errors. To describe a rollout, run the following command:
         
         gcloud container fleet packages rollouts describe ROLLOUT_NAME --fleet-package FLEET_PACKAGE_NAME
         

Replace ROLLOUT_NAME with the name of your rollout. You can get the full rollout name from the `list` command in the previous step.

The output resembles the following:
         
         CLUSTER    CURRENT_VERSION  SYNC_STATE  DESIRED_VERSION  START_TIME              END_TIME                STATE      MESSAGES
         cluster1   v2.0.0           SYNCED      v2.0.0           2025-05-15T13:28:58Z    2025-05-15T13:30:27Z    COMPLETED
         cluster2   v1.0.0           SYNCED      v2.0.0           2025-05-15T13:30:27Z                            ERROR      Membership no longer exists
         

  3. You can manage active rollouts by running the following commands:

     * Suspending a rollout puts an ongoing rollout into a `SUSPENDED` state. Any in-progress package updates continue, and no further package updates are scheduled. To suspend a rollout, run the following command:
           
           gcloud container fleet packages rollouts suspend ROLLOUT_NAME --fleet-package FLEET_PACKAGE_NAME
           

     * Resuming a rollout changes a `SUSPENDED` rollout back to an `IN_PROGRESS` state. Package updates deploy to target clusters as planned. To resume a rollout, run the following command:
           
           gcloud container fleet packages rollouts resume ROLLOUT_NAME --fleet-package FLEET_PACKAGE_NAME
           

     * Cancelling an ongoing rollout immediately terminates the rollout, putting it into an `ABORTED` state. All pending package updates planned as part of the rollout are canceled. To cancel a rollout, run the following command:
           
           gcloud container fleet packages rollouts abort ROLLOUT_NAME --fleet-package FLEET_PACKAGE_NAME
           




## Deployment strategies

You can deploy resources in different ways, either by deploying to a subset of clusters by specifying labels, or using variants pattern-matching for deploying different resources. You can combine both strategies for greater control over which resources are deployed to different clusters.

### Deploy to a subset of clusters

You can deploy the same resource to a subset of clusters by using labels and specifying the `target.fleet.selector.matchLabels` field with your labels (key-value pair). For example, if you set `matchLabels` as `country: "us"`, the fleet package service deploys your resources only to clusters with the label `country` that matches `"us"`.

Fleet packages supports only fleet membership labels. GKE cluster labels are not supported.

  1. (Optional) If you don't already have labels that you want to use, add them by completing the following steps:

     1. Get a list of memberships in the fleet:
            
            gcloud container fleet memberships list
            

     2. Add a label to the membership:
            
            gcloud container fleet memberships update MEMBERSHIP_NAME \
                --update-labels=KEY=VALUE
            

Replace the following:

        * `MEMBERSHIP_NAME`: the name of the cluster registered to the fleet.
        * `KEY` and `VALUE`: the label to add to the membership. If a label exists, its value is modified. Otherwise, a new label is created. Keys must start with a lowercase character and contain only hyphens (-), underscores (_), lowercase characters, and numbers. Values must contain only hyphens (-), underscores (_), lowercase characters, and numbers.

Repeat this command for each membership to which you want to add a label.

  2. Create or update your `FleetPackage` spec with the label selector:
         
         resourceBundleSelector:
           cloudBuildRepository:
             name: projects/PROJECT_ID/locations/us-central1/connections/CONNECTION_NAME/repositories/REPOSITORY_NAME
             tag: TAG
             serviceAccount: projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
             path: CONFIG_FILE_PATH
         target:
           fleet:
             project: projects/PROJECT_ID
             selector:
               **matchLabels :
                 KEY: "VALUE"**
         rolloutStrategy:
           rolling:
             maxConcurrent: MAX_CLUSTERS
         

  3. Create or update the fleet package:

### Create a fleet package
         
         gcloud container fleet packages create FLEET_PACKAGE_NAME \
             --source=fleetpackage-spec.yaml
         

### Update a fleet package
         
         gcloud container fleet packages update FLEET_PACKAGE_NAME \
             --source=fleetpackage-spec.yaml
         




### Deploy variant resources to clusters

You can deploy unique configurations to different clusters (for example, `dev` versus `prod`) by adding variant definitions to your fleet package.

For a conceptual overview of how variants are generated from your repository structure, see [How variants are generated](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages#variants).

To deploy a fleet package with variants, complete the following steps:

  1. Create or update your `FleetPackage` spec to include the `variantsPattern` and `variantNameTemplate` fields:
         
         resourceBundleSelector:
           cloudBuildRepository:
             name: projects/PROJECT_ID/locations/us-central1/connections/CONNECTION_NAME/repositories/REPOSITORY_NAME
             tag: TAG
             serviceAccount: projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
             path: CONFIG_FILE_PATH
             **variantsPattern : VARIANT_PATTERN**
         target:
           fleet:
             project: projects/PROJECT_ID
         rolloutStrategy:
           rolling:
             maxConcurrent: MAX_CLUSTERS
         target:
           fleet:
             project: projects/PROJECT_ID
          **variantSelector :
           variantNameTemplate: VARIANT_NAME_TEMPLATE**
         

Replace the following:

     * `VARIANT_PATTERN`: a glob pattern to generate variants from your repository, such as `*` (matches all files and directories) or `*.yaml` (matches only files). For more information about which patterns are supported, see [`variantsPattern` matching](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages#variant-pattern).
     * `VARIANT_NAME_TEMPLATE `: a string or template to select a variant for each cluster. You can use metadata variables like `${membership.labels['env']}` or `${membership.location}`.
**Note:** Ensure that your `variantsPattern` generates unique variant names. If two files map to the same name (for example, `app1/deploy.yaml` and `app2/deploy.yaml`, both resolving to `deploy`), the rollout might fail due to a name collision.
  2. Create or update the fleet package:

### Create a fleet package
         
         gcloud container fleet packages create FLEET_PACKAGE_NAME \
             --source=fleetpackage-spec.yaml
         

### Update a fleet package
         
         gcloud container fleet packages update FLEET_PACKAGE_NAME \
             --source=fleetpackage-spec.yaml
         




## Delete a fleet package

Deleting a fleet package also deletes the following resources:

  * The Kubernetes resources deployed on your clusters
  * The fleet package rollout history



To delete a fleet package, run the following command:
    
    
    gcloud container fleet packages delete FLEET_PACKAGE_NAME --force
    

## Troubleshoot

To find methods for diagnosing and resolving errors related to Cloud Build, see [Troubleshooting build errors](https://docs.cloud.google.com/build/docs/troubleshooting).

## What's next

  * Refer to the [`FleetPackage` fields reference page](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
