---
url: https://docs.cloud.google.com/deploy/docs/deploying-application/
title: Deploy your application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:15:47.447820+00:00
---

# Deploy your application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/deploying-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Deploy your application Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud Deploy to get your application into your intended target runtime environments. Before you do this, you need to [create your delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets).

## Before you begin

This section describes the things you need to have in place before you can deploy your application using Cloud Deploy.

  * Make sure your [execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) has the necessary [IAM roles and permissions](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions).

  * [Create your delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets).

Cloud Deploy can deploy to Google Kubernetes Engine, Cloud Run, GKE attached clusters, and [custom targets](https://docs.cloud.google.com/deploy/docs/deploy-to-custom-targets). [Target configuration](https://docs.cloud.google.com/deploy/docs/config-files#target_definitions) differs depending on which of these you're deploying to.

  * Have your container images and manifests.

You need one or more container images to deploy and one or more Kubernetes manifests (to deploy to GKE) or service YAML files (to deploy to Cloud Run).

You need a continuous integration pipeline, or some other process, to build and place your images. Your [CI tool](https://docs.cloud.google.com/deploy/docs/integrating-ci) can be Cloud Build, Jenkins, or anything that results in container images that you can provide to your Cloud Deploy delivery pipeline.

  * [Have a `skaffold.yaml` configuration file](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold).

Cloud Deploy calls [`skaffold render`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) to render the Kubernetes manifests using this file and [`skaffold apply`](https://skaffold.dev/docs/workflows/ci-cd/#separation-of-rendering-and-deployment) to deploy them into your target. To do this, Skaffold requires at least a minimal `skaffold.yaml`. You can get one in either of two ways:

    * Create your own.

Note that the `skaffold.yaml` file must reference the `apiVersion` that is supported by Skaffold in the first line, as in this example:
          
          `apiVersion: skaffold/v4beta7`
          

    * Have it generated for you.

If you don't already have a `skaffold.yaml` file, you can [have Cloud Deploy create one for you](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#have_generate_your_skaffoldyaml). This file is suitable for onboarding, learning, or demonstrating Cloud Deploy, and shouldn't be used for production workloads.

See [Using Skaffold with Cloud Deploy](https://docs.cloud.google.com/deploy/docs/using-skaffold) for more details. Also, [Managing manifests in Cloud Deploy](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) has more details on using Skaffold and Cloud Deploy with manifest-management tools, such as Helm, Kustomize, and kpt.




## Set up Cloud Deploy for the runtime environment of your choice

Cloud Deploy can deploy your application to any of the following runtime environments:

  * [GKE](https://docs.cloud.google.com/deploy/docs/gke-targets)
  * [GKE attached clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets)
  * [Cloud Run](https://docs.cloud.google.com/deploy/docs/run-targets)



## Invoke your delivery pipeline to create a release

After you've configured Cloud Deploy to deploy to your runtime, you can now submit your application to be deployed according to the delivery pipeline you created.

  1. Run your regular continuous-integration (CI) process, creating the deployable artifact or artifacts.

  2. Initiate the delivery pipeline by calling Cloud Deploy to create a release.

Run the following command from the directory containing your Skaffold config:
         
         gcloud deploy releases create RELEASE_NAME --delivery-pipeline=PIPELINE_NAME --region=REGION
         

Because this command creates a tar file of the entire contents of the directory, and any subdirectories, you might not want to run this command from your home or root directory. Either run the command from the directory containing your Skaffold config, or include the `--source=` option, described later.

In this command...

`RELEASE_NAME` is a name to give to this release. The name must be unique among all releases for this delivery pipeline.

You can specify dynamic release names by including `'$DATE'` or `'$TIME'` or both. For example, if you invoke this command at 3:07pm UTC, `'rel-$TIME'` resolves to `rel-1507`. `'$DATE'` and `'$TIME'` must be in single-quotes, and the time is UTC time on the machine where you invoke the command.

`PIPELINE_NAME` is the name of the delivery pipeline that will manage deployment of this release through the progression of targets. This name must match the [`name` field in the pipeline definition](https://docs.cloud.google.com/deploy/docs/config-files#name).

`REGION` is the name of the region in which you're creating the release, for example `us-central1`. This is required.


**Note:** optionally, you can include `--source=SOURCE_PATH` to specify the location of the `skaffold.yaml` file. The default is the current directory.

This command uploads a tar file containing your configs to a Cloud Storage bucket and creates the release. Cloud Deploy also automatically creates a rollout and deploys your image to the first target defined in the delivery pipeline.

In addition to the parameters shown with this command, you can include _either_ of the following options:

  * `--images=<name=path/name:$IMAGE_SHA>,<name=path/name:$IMAGE_SHA>`

A collection of image name to image full-path replacements.

  * `--build-artifacts=<path/file>`

A reference to a Skaffold build artifacts output file, which can be passed in to represent the image full path replacements.




These two options are mutually exclusive.

You can also include one of the following flags to have Cloud Deploy generate a `skaffold.yaml` file for you:

  * [`--from-k8s-manifest=K8S_MANIFEST`](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--from-k8s-manifest)

The generated Skaffold config is based on the Kubernetes manifest you pass this flag. Using this flag with either the `--skaffold-file` flag or the `--source` flag, generates an error. See [Generating your `skaffold.yaml`](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#generating_your_skaffoldyaml) for more details.

  * [`--from-run-manifest=RUN_MANIFEST`](https://docs.cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--from-run-manifest)

The generated Skaffold config is based on the Cloud Run service YAML you pass this flag. Using this flag with either the `--skaffold-file` flag or the `--source` flag, generates an error. See [Generating your `skaffold.yaml`](https://docs.cloud.google.com/deploy/docs/using-skaffold/getting-started-skaffold#generating_your_skaffoldyaml) for more details.




These two options are mutually exclusive.

You can also include a `.gcloudignore` file if there are any files in the directory which you don't want included in the tar file.

### Create a release from the Google Cloud console

You can use the Google Cloud console to create a release for a delivery pipeline. This is useful for trying out Cloud Deploy, but is not suitable for production workloads.

The following procedure assumes you have already created a delivery pipeline and one or more targets. (You can also use the Google Cloud console) to [create your delivery pipeline](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets#create_pipeline_in_ui).)

  1. From the **Delivery pipeline details** page, for a specific delivery pipeline, click **Create release**.

![delivery pipeline details, showing the create release button ](https://docs.cloud.google.com/static/deploy/images/click_create_release.png)

  2. In the **Choose a container** field, paste or type the path to the container image you want to deploy. You can also use the default container pre-populated in this field, for evaluation.

You can also click **Select** to choose a container image from Artifact Registry.

  3. Provide a unique name for this release, in the **Release name** field, or use the default name provided.

  4. Provide a name for the rollout, in the **Rollout name** field, or use the default name provided.

This name is used for the rollout to the first target, for this release. For subsequent targets, you can name the rollout in the **Promote** dialog or on the `gcloud deploy releases promote` command.

  5. Optionally, include a description for this release, in the **Description** field. 

  6. Under **Deployment details** , enter a name for your GKE deployment or Cloud Run service, or use the default name provided.

For GKE, Cloud Deploy generates the manifest for you. For Cloud Run, Cloud Deploy generates the service definition, which is used to create the service.

  7. Click **Create**.

![The create release dialog](https://docs.cloud.google.com/static/deploy/images/create-release-dialog.png)




Cloud Deploy uses the generated manifest or Cloud Run service definition, and the generated `skaffold.yaml`, to create the release. 

### Change the deployment timeout

For deployments to GKE and GKE attached clusters, there are three separate timeouts that affect how long the system waits for Kubernetes to report a stable deployment:

  * Cloud Build has a timeout of 1 hour on operations that Cloud Build performs for Cloud Deploy.

You can change this timeout in the [configuration for your execution environment](https://docs.cloud.google.com/deploy/docs/config-files#executionconfigs).

  * [Skaffold](https://docs.cloud.google.com/deploy/docs/set-up-skaffold) has a [health-check timeout (`deploy.statusCheckDeadlineSeconds`)](https://skaffold.dev/docs/pipeline-stages/status-check/#configuring-timeout-for-status-check), which is the amount of time, in seconds, to wait for deployments to stabilize.

The default is 600 seconds (10 minutes). To use this timeout, [`deploy.statusCheck`](https://skaffold.dev/docs/references/yaml/#deploy-statusCheck) must be set to `true`. By default, it is. If `statusCheck` is `false`, there is no status check, the rollout is marked successful after `kubectl apply` finishes successfully.

  * For Kubernetes resources of `kind: Deployment`, there's [`Deployment.spec.progressDeadlineSeconds`](https://kubernetes.io/docs/concepts/workloads/controllers/_print/#progress-deadline-seconds), which is the amount of time Kubernetes waits for the Deployment to report as stable.

This timeout is applicable to `Deployment` resources only. Here's how these first two timeouts work together:

    * If `Deployment.spec.progressDeadlineSeconds`, in Kubernetes, is unset, then the Skaffold health-check timeout is the effective timeout, whether it's the default or is explicitly set.

    * If `Deployment.spec.progressDeadlineSeconds`, in Kubernetes, is set, then Skaffold ignores its own health-check timeout, and the Kubernetes progress deadline is the effective timeout. However, if the Kubernetes timeout is explicitly set to `600` (10 minutes), then Skaffold assumes that it's the default (unset) and ignores it, and the Skaffold timeout is used (if set).

    * If neither timeout is set, then the effective timeout is the Skaffold default of `600` (10 minutes).

Besides `Deployment`s, other Kubernetes resources can have timeouts, which do not influence the stability timeout. If any of these are present, review them to ensure they are not in conflict with the stability timeout.

If Skaffold (or Cloud Build) times out, the GKE deployment continues to run. Cloud Deploy shows a failure, but it can still succeed or fail on the GKE cluster.




To change your deployment stability timeout:

  1. Ensure that [`deploy.statusCheck`](https://skaffold.dev/docs/references/yaml/#deploy-statusCheck) is set to `true` in `skaffold.yaml`.

`true` is the default. When `true`, Skaffold waits for health checks to report a stable deployment, subject to the timeout value in the next step.

  2. In [`skaffold.yaml`](https://docs.cloud.google.com/deploy/docs/set-up-skaffold), set `statusCheckDeadlineSeconds` to the number of seconds you want to wait.
         
         deploy:
           ...
           statusCheck: true
           statusCheckDeadlineSeconds: 600
           ...
         

The default is `600` (10 minutes). Skaffold waits this amount of time for a stable deployment. If this time is exceeded before the deployment is stable, the deployment fails.

  3. Optionally, you can add [`tolerateFailuresUntilDeadline: true`](https://skaffold.dev/docs/status-check/#configuring-failure-behavior-for-status-check) after `statusCheckDeadlineSeconds`.

This setting tells Skaffold not to exit if a single deployment fails, but to tolerate failures until `statusCheckDeadlineSeconds` expires. This setting can help in situations where you have resources that might need more time (up to the status-check deadline) to reach a stable state.

For example, if you're using Istio or Cloud Service Mesh, you might have a failed deployment with a message similar to this one:
         
         error iptables validation failed; workload is not ready for Istio.
         When using Istio CNI, this can occur if a pod is scheduled before the node is ready.
         

  4. In your Kubernetes manifest, for resources of `kind: Deployment`, set `Deployment.spec.progressDeadlineSeconds` to the same value as you set for `statusCheckDeadlineSeconds`.




## What's next

  * Find out about [deploying to GKE](https://docs.cloud.google.com/deploy/docs/gke-targets)

  * Find out about [deploying to Cloud Run](https://docs.cloud.google.com/deploy/docs/run-targets)

  * Find out about [deploying to GKE attached clusters](https://docs.cloud.google.com/deploy/docs/anthos-targets)

  * Learn how to [create your delivery pipeline and targets](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets)

  * Learn how to [promote a release](https://docs.cloud.google.com/deploy/docs/promote-release)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
