---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/schedule-builds/
title: Schedule custom OS image builds \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:38.241793+00:00
---

# Schedule custom OS image builds  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/schedule-builds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Schedule custom OS image builds Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

You can schedule recurring Image Builder runs by using Cloud Scheduler and Cloud Build triggers. When you schedule custom OS image builds, Cloud Build automatically updates your baseline images with operating system patches and organizational security policies without requiring manual intervention.

## Before you begin

  * Complete the environment setup steps in [Prepare your environment](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Required roles

To get the permissions that you need to create triggers and schedule builds, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * Cloud Scheduler Job Runner (`roles/cloudscheduler.jobRunner`) or Cloud Scheduler Admin (`roles/cloudscheduler.admin`) 
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a scheduled build pipeline

You can configure recurring image builds by using the gcloud CLI or the Go client library:

###  gcloud 

To schedule recurring OS image builds by using the gcloud CLI, complete the following steps:

  1. Create a manual Cloud Build trigger that specifies your target `cloudbuild.yaml` file by running the [`gcloud builds triggers create manual` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual). Because Cloud Scheduler invokes this trigger manually rather than on repository events, don't specify push or pull request filters:
         
         gcloud builds triggers create manual \
             --name="TRIGGER_NAME" \
             --region=REGION \
             --build-config=CLOUDBUILD_YAML_PATH \
             --project=PROJECT_ID
         

  2. Retrieve the unique ID (`trigger_id`) generated for your new trigger by running the [`gcloud builds triggers describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/builds/triggers/describe):
         
         gcloud builds triggers describe TRIGGER_NAME \
             --region=REGION \
             --format="value(id)" \
             --project=PROJECT_ID
         

  3. To create a Cloud Scheduler job that sends an `HTTP POST` request to the Cloud Build API (`projects.locations.triggers.run`) according to your required unix cron schedule, for example, weekly on Mondays at 6:00 AM using `'0 6 * * 1'`, run the [`gcloud scheduler jobs create http` command](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/http):
         
         gcloud scheduler jobs create http JOB_NAME \
             --schedule="CRON_SCHEDULE" \
             --uri="https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/triggers/TRIGGER_ID:run" \
             --message-body="{}" \
             --oauth-service-account-email="SERVICE_ACCOUNT_EMAIL" \
             --location=REGION \
             --project=PROJECT_ID
         




Replace the following:

  * `TRIGGER_NAME`: the name for your manual Cloud Build trigger, for example, `weekly-ubuntu-builder`.
  * `REGION`: the region to create the trigger, for example, `us-central1`.
  * `CLOUDBUILD_YAML_PATH`: the path to your [`cloudbuild.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/build-configuration-schema) file in your local directory, for example, `cloudbuild.yaml`.
  * `PROJECT_ID`: your project ID.
  * `JOB_NAME`: the name for your Cloud Scheduler cron job, for example, `weekly-custom-os-patching`.
  * `CRON_SCHEDULE`: the unix cron schedule expression, for example, `'0 6 * * 1'`.
  * `TRIGGER_ID`: the unique ID (`trigger_id`) generated for your trigger.
  * `SERVICE_ACCOUNT_EMAIL`: the service account email that authorizes Cloud Scheduler to invoke the trigger. This service account requires `roles/cloudbuild.builds.editor` permissions.



###  Go 

To schedule pipelines programmatically by using the Cloud Build and Cloud Scheduler Go client libraries, use the `scheduleBuild` function.

Before you run this sample, complete the following prerequisites:

  * Upload your [`imagebuilder.yaml`](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema) configuration file to your Cloud Storage bucket, for example, `gs://STAGING_BUCKET/imagebuilder.yaml`.
  * Grant the scheduling service account `cloud-build-trigger-scheduler@PROJECT_ID.iam.gserviceaccount.com`, the Cloud Build Editor role (`roles/cloudbuild.builds.editor`) on your project and the Service Account User role (`roles/iam.serviceAccountUser`) on the service account that runs the build. For more information, see [Schedule builds](https://docs.cloud.google.com/build/docs/schedule-builds) in the Cloud Build documentation.


    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	scheduler "cloud.google.com/go/scheduler/apiv1"
    	"cloud.google.com/go/scheduler/apiv1/schedulerpb"
    	"google.golang.org/api/cloudbuild/v1"
    )
    
    // scheduleBuild creates a manual Cloud Build trigger that runs an Image
    // Builder pipeline, and a Cloud Scheduler job that runs the trigger every day.
    //
    // Before you run this sample, upload your imagebuilder.yaml configuration file
    // to Cloud Storage, create a generic Artifact Registry repository, and create a
    // service account to run the build.
    //
    // The job runs the trigger as the default scheduling service account,
    // cloud-build-trigger-scheduler@PROJECT_ID.iam.gserviceaccount.com. Grant that
    // service account the Cloud Build Editor role, and the Service Account User
    // role on the service account that runs the build. For details, see
    // https://cloud.google.com/build/docs/schedule-builds.
    func scheduleBuild(w io.Writer, projectID, gcsWorkdir, configPath, serviceAccount string) error {
    	// projectID := "my-project-id"
    	region := "us-central1"
    	// gcsWorkdir := "gs://my-bucket/workdir/"
    	// configPath := "gs://my-bucket/imagebuilder.yaml"
    	repository := "vm-images"
    	packageName := "custom-os-images"
    	// serviceAccount := "image-builder@my-project-id.iam.gserviceaccount.com"
    	triggerName := "scheduled-image-builder"
    	jobName := "scheduled-image-builder-job"
    	schedule := "0 9 * * *"
    
    	ctx := context.Background()
    	cbService, err := cloudbuild.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("cloudbuild.NewService: %w", err)
    	}
    	schedulerClient, err := scheduler.NewCloudSchedulerClient(ctx)
    	if err != nil {
    		return fmt.Errorf("scheduler.NewCloudSchedulerClient: %w", err)
    	}
    	defer schedulerClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/scheduler/latest/apiv1.html#cloud_google_com_go_scheduler_apiv1_CloudSchedulerClient_Close)()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, region)
    	sa := fmt.Sprintf("projects/%s/serviceAccounts/%s", projectID, serviceAccount)
    
    	trigger := &cloudbuild.BuildTrigger{
    		Name:        triggerName,
    		Description: "Manual trigger for scheduled VM image builds",
    		EventType:   "MANUAL",
    		Build: &cloudbuild.Build{
    			ServiceAccount: sa,
    			// AutomapSubstitutions exposes these substitutions to every step as
    			// environment variables. See
    			// https://cloud.google.com/build/docs/configuring-builds/substitute-variable-values#mapping_substitutions_to_environment_variables
    			Substitutions: map[string]string{
    				"_GCS_WORKDIR":               gcsWorkdir,
    				"_SERVICE_ACCOUNT":           sa,
    				"_IMAGE_OUTPUT_PATH":         "image-builder/binaryOut",
    				"_IMAGE_BUILDER_CONFIG_PATH": configPath,
    				"_ARTIFACT_REGISTRY_RESOURCE_URI": fmt.Sprintf(
    					"projects/%s/locations/%s/repositories/%s/packages/%s/versions/v${BUILD_ID}",
    					projectID, region, repository, packageName,
    				),
    			},
    			Steps: []*cloudbuild.BuildStep{
    				{
    					Id:     "imagebuilder-customize",
    					Name:   "us-docker.pkg.dev/image-builder-official/release/builder:stable",
    					Script: "#!/usr/bin/env bash\n/build",
    					Results: []*cloudbuild.StepResult{
    						{
    							Name:            "base_image",
    							AttestationType: "https://cloudbuild.googleapis.com/attestations/build_content_restrictions",
    						},
    						{Name: "image_builder_telemetry_metrics"},
    					},
    				},
    				{
    					Id:      "imagebuilder-validate",
    					Name:    "us-docker.pkg.dev/image-builder-official/release/validator:stable",
    					Script:  "#!/usr/bin/env bash\n/validate",
    					Results: []*cloudbuild.StepResult{{Name: "image_builder_telemetry_metrics"}},
    				},
    				{
    					Id:      "imagebuilder-publish",
    					Name:    "us-docker.pkg.dev/image-builder-official/release/builder:stable",
    					Script:  "#!/usr/bin/env bash\n/publish",
    					Results: []*cloudbuild.StepResult{{Name: "image_builder_telemetry_metrics"}},
    				},
    			},
    			Options: &cloudbuild.BuildOptions{
    				AutomapSubstitutions:  true,
    				DynamicSubstitutions:  true,
    				RequestedVerifyOption: "VERIFIED",
    				SubstitutionOption:    "ALLOW_LOOSE",
    				// Builds that run as a user-specified service account must set a
    				// logging option.
    				Logging: "CLOUD_LOGGING_ONLY",
    			},
    			Artifacts: &cloudbuild.Artifacts{
    				GenericArtifacts: []*cloudbuild.GenericArtifact{
    					{
    						Folder:       "${_IMAGE_OUTPUT_PATH}",
    						RegistryPath: "${_ARTIFACT_REGISTRY_RESOURCE_URI}",
    					},
    				},
    			},
    			Timeout: "3600s",
    		},
    	}
    	createdTrigger, err := cbService.Projects.Locations.Triggers.Create(parent, trigger).
    		Context(ctx).Do()
    	if err != nil {
    		return fmt.Errorf("Triggers.Create: %w", err)
    	}
    	fmt.Fprintf(w, "Created trigger %s (ID: %s)\n", createdTrigger.Name, createdTrigger.Id)
    
    	schedulerSA := fmt.Sprintf(
    		"cloud-build-trigger-scheduler@%s.iam.gserviceaccount.com", projectID,
    	)
    	job := &schedulerpb.Job{
    		Name:        fmt.Sprintf("%s/jobs/%s", parent, jobName),
    		Description: "Runs the Image Builder trigger on a schedule",
    		Schedule:    schedule,
    		Target: &schedulerpb.Job_HttpTarget{
    			HttpTarget: &schedulerpb.HttpTarget{
    				Uri: fmt.Sprintf(
    					"https://cloudbuild.googleapis.com/v1/projects/%s/locations/%s/triggers/%s:run",
    					projectID, region, createdTrigger.Id,
    				),
    				HttpMethod: schedulerpb.[HttpMethod_POST](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/scheduler/latest/apiv1/schedulerpb.html#cloud_google_com_go_scheduler_apiv1_schedulerpb_HttpMethod_HTTP_METHOD_UNSPECIFIED_HttpMethod_POST_HttpMethod_GET_HttpMethod_HEAD_HttpMethod_PUT_HttpMethod_DELETE_HttpMethod_PATCH_HttpMethod_OPTIONS),
    				AuthorizationHeader: &schedulerpb.HttpTarget_OauthToken{
    					OauthToken: &schedulerpb.OAuthToken{
    						ServiceAccountEmail: schedulerSA,
    					},
    				},
    			},
    		},
    	}
    	req := &schedulerpb.CreateJobRequest{Parent: parent, Job: job}
    	createdJob, err := schedulerClient.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateJob: %w", err)
    	}
    	fmt.Fprintf(w, "Created job %s with schedule %q\n", createdJob.Name, createdJob.Schedule)
    	return nil
    }
    

## What's next

  * Learn how to [Automate builds on repository events](https://docs.cloud.google.com/compute/docs/images/image-builder/automate-builds-on-events) on Git push, tag, or merge events using Terraform.
  * Review the [Customization recipe schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema) to define software packages and validation procedures.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
