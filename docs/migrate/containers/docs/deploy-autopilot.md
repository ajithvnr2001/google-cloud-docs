---
url: https://docs.cloud.google.com/migrate/containers/docs/deploy-autopilot/
title: Migrate and deploy applications to GKE Autopilot clusters \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:59.810457+00:00
---

# Migrate and deploy applications to GKE Autopilot clusters  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/deploy-autopilot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate and deploy applications to GKE Autopilot clusters

To deploy your migrated container workloads to GKE Autopilot clusters, you use the same procedure to migrate your workloads as you use for the existing architecture. The only changes are that:

  * You have to set `v2kServiceManager` to `true` in the migration plan before you generate the container artifacts. 

  * You have to review the new `services-config.yaml` file and make any edits to the initialization services. See [Using services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config).




To perform a migration:

  1. [Install Migrate to Containers version 1.15.0](https://docs.cloud.google.com/migrate/containers/docs/install-overview).

  2. [Add a migration source](https://docs.cloud.google.com/migrate/containers/docs/adding-a-migration-source) and [create a migration](https://docs.cloud.google.com/migrate/containers/docs/creating-a-migration) as you do today with the existing runtime.

  3. [Customize your migration plan](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan) as necessary.

**Note:** Prior to Migrate to Containers 1.10, use of the enhanced Linux service manager was disabled by default. If you are using Migrate to Containers 1.9 or older, you should have `v2kServiceManager` set to `true` in your migration plan (`my-migration.yaml`). If the enhanced Linux service manager is disabled for you, check your `services.yaml` file for comments about services that may not work with your new runtime. If you would like to include any of the disabled services, contact your support channel.
     1. Download the migration plan. The migration plan is represented by [AppXGenerateArtifactsFlow](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/references/crds/m2c-crds.md#appxgenerateartifactsflow).

For example, for a migration named "my-migration":
            
            migctl migration get my-migration

     2. Open the downloaded migration plan, `my-migration.yaml`, in a text editor.

     3. Verify the enhanced Linux service manager. The `v2kServiceManager` flag is set to `true` by default. However, if Migrate to Containers detects a system service that is not supported by the service manager, you will be alerted and the `v2kServiceManager` flag will be set to `false`. When the flag is `false` the migration will use a legacy runtime which supports your service.

The following alert is provided alongside the unsupported service:
            
            Service is not supported by v2k service manager, therefore legacy runtime
            will be used instead of v2k service manager, and migrated workload would
            not fit running on Autopilot clusters of Cloudrun.

When an unsupported service is found, you can also choose to manually set the flag to `true`. In this instance, you can either choose to keep the unsupported service on the generated image where it may not run or you can exclude the service by removing it from the migration plan.

To enable the new service manager, reset the flag to `true`:
            
            v2kServiceManager: true

     4. Perform any other customizations necessary for your migration as described in [Customize the migration plan](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan).

     5. When your edits are complete, save the edited file.

     6. Upload the edited migration plan:
            
            migctl migration update my-migration --main-config my-migration.yaml

  4. [Generate](https://docs.cloud.google.com/migrate/containers/docs/executing-a-migration) and [ review the migration artifacts](https://docs.cloud.google.com/migrate/containers/docs/review-deployment-files) as you do today with the existing runtime.

  5. Edit the new `services-config.yaml` file to configure the initialization properties of the container. Save the file and rebuild your container image to apply the changes.

See [Using services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config) for more.

  6. [Deploy the container to a GKE Autopilot cluster](https://docs.cloud.google.com/migrate/containers/docs/deploying-to-target-cluster) using `kubectl`:
         
         kubectl apply -f deployment_spec.yaml




### Example: Deploying the Quickstart container on an Autopilot cluster

Use the current [Quickstart](https://docs.cloud.google.com/migrate/containers/docs/quickstart) guide to migrate a container containing a simple web server and then deploy it on an Autopilot cluster. The only changes that you have to make to the Quickstart process are:

  1. In Step 3 of [Migrating the VM](https://docs.cloud.google.com/migrate/containers/docs/quickstart#migrating_the_vm), where you review the migration plan, set `v2kServiceManager` to `true` in the migration plan and then save the plan:
         
         
         v2kServiceManager: true

  2. In the [Deploying the migrated workload](https://docs.cloud.google.com/migrate/containers/docs/quickstart#deploying_the_migrated_workload) section, create and connect to a GKE Autopilot cluster before you deploy the container:

     1. Create a GKE Autopilot cluster:
            
            gcloud container clusters create-auto "CLUSTER_NAME"
            --project "PROJECT_NAME"  --region "REGION" --release-channel "regular"
            --subnetwork "projects/PROJECT_NAME/regions/**us-central1** /subnetworks/default"

     2. Connect to the cluster:
            
            gcloud container clusters get-credentials CLUSTER_NAME 
              --zone REGION --project PROJECT_NAME 
            

     3. Deploy the container as described in the [Deploying the migrated workload](https://docs.cloud.google.com/migrate/containers/docs/quickstart#deploying_the_migrated_workload) section.




### Changes to the AppXGenerateArtifactsFlow CRD

If you are using CRD files to control your migration, edit the [AppXGenerateArtifactsFlow](https://github.com/GoogleCloudPlatform/migrate-to-containers/blob/main/references/crds/m2c-crds.md#appxgenerateartifactsflow) CRD to set `v2kServiceManager` to `true`. See [Customizing a migration plan](https://docs.cloud.google.com/migrate/containers/docs/customizing-a-migration-plan#crd) for more on using CRD files to control migration.

## What's next

  * Learn how to [deploy containers to Cloud Run](https://docs.cloud.google.com/migrate/containers/docs/deploy-run).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
