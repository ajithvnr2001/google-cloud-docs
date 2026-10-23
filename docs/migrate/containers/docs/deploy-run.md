---
url: https://docs.cloud.google.com/migrate/containers/docs/deploy-run/
title: Deploy containers to Cloud Run \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:54.671733+00:00
---

# Deploy containers to Cloud Run  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/deploy-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploy containers to Cloud Run

If you use the enhanced Linux service manager that is offered by default to migrate your container workloads, you can then deploy the container on [Cloud Run](https://docs.cloud.google.com/run/docs) without having to make any additional changes to the container.

**Note:** The container workload must be stateless to be deployed on Cloud Run. You cannot deploy a stateful container. See [Developing your service](https://docs.cloud.google.com/run/docs/developing) for more information, including the complete list of requirements for deploying containers on Cloud Run.

To deploy your container on Cloud Run:

  1. [Install Migrate to Containers version 1.15.0](https://docs.cloud.google.com/migrate/containers/docs/install-overview).

  2. [Add a migration source](https://docs.cloud.google.com/migrate/containers/docs/adding-a-migration-source) and [create a migration](https://docs.cloud.google.com/migrate/containers/docs/creating-a-migration) just as you do today with the existing runtime. 

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

  4. [Generate](https://docs.cloud.google.com/migrate/containers/docs/executing-a-migration) and [ review the migration artifacts](https://docs.cloud.google.com/migrate/containers/docs/review-deployment-files) just as you do today with the existing runtime.

  5. Edit the new `services-config.yaml` file to configure the initialization properties of the container. Save the file and rebuild your container image to apply the changes.

See [Using services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config) for more information about how to edit your `services.yaml` file.

  6. After you generate the migration artifacts, open the `deployment_spec.yaml` file in an editor to determine the location of the container image. For example, you should see something similar to the following:
         
         spec:
           containers:
           - image: gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL

Where `gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL` specifies the location of the container image.

  7. Use the following command to deploy the container on Cloud Run:
         
         gcloud run deploy my-runtime
             --image gcr.io/PROJECT_NAME/IMAGE_NAME:LABEL
             --region REGION --platform managed
             **--set-env-vars=HC_V2K_SERVICE_MANAGER=true** --port PORT 

The `--set-env-vars` property sets the `HC_V2K_SERVICE_MANAGER` environment variable to `true` to enable the enhanced Linux service manager.

The `--port` property specifies the port where requests is sent to the container. The default port is 8080.




### Example: Deploying the Quickstart container on Cloud Run

Use the current [Quickstart](https://docs.cloud.google.com/migrate/containers/docs/migrate-vm) guide to migrate a container containing a simple web server and then deploy it on Cloud Run. The only changes that you have to make to the Quickstart process are:

  1. In Step 3 of [Migrating the VM](https://docs.cloud.google.com/migrate/containers/docs/migrate-vm#migrating_the_vm), where you review the migration plan, set `v2kServiceManager` to `true` in the migration plan and then save the plan:
         
         v2kServiceManager: true

  2. After the migration completes, open the `deployment_spec.yaml` file in an editor to determine the location of the container. For example, you should see something similar to the following:
         
         spec:
           containers:
           - image: gcr.io/PROJECT_NAME/quickstart-instance:LABEL

  3. In the [Deploying the migrated workload](https://docs.cloud.google.com/migrate/anthos/docs/migrate-vm#deploying_the_migrated_workload) section, deploy the container image to Cloud Run by using the command:
         
         gcloud run deploy my-runtime
             --image gcr.io/PROJECT_NAME/quickstart-instance:LABEL
             --region REGION --platform managed
             --set-env-vars=HC_V2K_SERVICE_MANAGER=true --port 80 

The web server in the migrated container listens for requests on port 80 so make sure to specify that port when deploying the container.

You should see the following response, which includes the URL of the Cloud Run service:
         
         Allow unauthenticated invocations to [my-runtime] (y/N)?  y
         
         Deploying container to Cloud Run service [my-runtime] in project [PROJECT_NAME] region [REGION]
         Deploying new service... Done.
           ✓ Creating Revision…
           ✓ Routing traffic…
             Setting IAM Policy…
         Done.
         Service [my-runtime] revision [my-runtime-00001-sas] has been deployed and is serving 100 percent of traffic.
         **Service URL : https://my-runtime-s5ahdq-uc.a.run.app**

  4. From Cloud Shell, make a request to the container by using its service URL, passing in your credentials:
         
         curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" https://my-runtime-s5ahdq-uc.a.run.app

You should now see the "Hello World!" page.




## What's next

  * Learn how to [use services-config.yaml](https://docs.cloud.google.com/migrate/containers/docs/services-config).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
