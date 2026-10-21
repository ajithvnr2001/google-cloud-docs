---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/schedule-builds/
title: Schedule custom OS image builds \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:09:47.286895+00:00
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

You can configure recurring image builds by using the gcloud CLI or the Go client SDKs:

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

You can schedule pipelines programmatically inside your enterprise applications by using the Google Cloud Go API client libraries (`cloudbuild/v1` and `cloudscheduler/v1`).

The following complete Go example demonstrates how to parse command-line flags and construct the `Build` request from your `imagebuilder.yaml` definition. The program then registers a manual Cloud Build trigger and provisions a Cloud Scheduler job when you supply the `--cron_schedule` flag.
    
    
    // Program main demonstrates how to submit or schedule a Image Builder pipeline using Go SDKs.
    package main
    
    import (
        "context"
        "flag"
        "fmt"
        "os"
    
        "google.golang.org/api/cloudbuild/v1"
        "google.golang.org/api/cloudscheduler/v1"
    )
    
    var (
        projectID        = flag.String("project_id", "", "The target Project ID")
        region           = flag.String("region", "us-central1", "Region of resources")
        gcsWorkdir       = flag.String("gcs_workdir", "", "The storage workspace directory URI, e.g. gs://my-bucket/workdir/")
        serviceAccount   = flag.String("service_account", "", "Service account email to run the worker VM")
        imageBuilderYAML = flag.String("config_path", "imagebuilder.yaml", "Path to the imagebuilder.yaml configuration file")
        arRepositoryID   = flag.String("ar_repo_id", "os-images", "Name of the target generic Artifact Registry repository")
        arPackageName    = flag.String("ar_package_name", "custom-os", "Package identifier for OS images")
        cronSchedule     = flag.String("cron_schedule", "", "Optional cron schedule to run this build periodically (e.g. '0 6 * * 1')")
    )
    
    func main() {
        flag.Parse()
    
        if *projectID == "" || *serviceAccount == "" || *gcsWorkdir == "" {
            fmt.Fprintln(os.Stderr, "Error: --project_id, --gcs_workdir, and --service_account are required flags")
            flag.Usage()
            os.Exit(1)
        }
    
        ctx := context.Background()
    
        if *cronSchedule != "" {
            fmt.Printf("Scheduling build with cron schedule: %s\n", *cronSchedule)
            if err := scheduleBuild(ctx); err != nil {
                fmt.Fprintf(os.Stderr, "Failed to schedule Cloud Build: %v\n", err)
                os.Exit(1)
            }
        } else {
            fmt.Println("Submitting build request immediately to Cloud Build API...")
            if err := triggerBuild(ctx); err != nil {
                fmt.Fprintf(os.Stderr, "Failed to trigger Cloud Build: %v\n", err)
                os.Exit(1)
            }
        }
    }
    
    func createBuildRequest() *cloudbuild.Build {
        subs := map[string]string{
            "_GCS_WORKDIR":                    *gcsWorkdir,
            "_SERVICE_ACCOUNT":                fmt.Sprintf("projects/%s/serviceAccounts/%s", *projectID, *serviceAccount),
            "_IMAGE_OUTPUT_PATH":              "image-builder/binaryOut",
            "_IMAGE_BUILDER_CONFIG_PATH":      *imageBuilderYAML,
            "_ARTIFACT_REGISTRY_RESOURCE_URI": fmt.Sprintf("projects/%s/locations/%s/repositories/%s/packages/%s/versions/v${BUILD_ID}", *projectID, *region, *arRepositoryID, *arPackageName),
        }
    
        return &cloudbuild.Build{
            Steps: []*cloudbuild.BuildStep{
                {
                    Name:   "us-central1-docker.pkg.dev/image-builder-official/release/builder:stable",
                    Script: "#!/usr/bin/env bash\n/build",
                    Id:     "imagebuilder-customize",
                },
                {
                    Name:   "us-central1-docker.pkg.dev/image-builder-official/release/validator:stable",
                    Script: "#!/usr/bin/env bash\n/validate",
                    Id:     "imagebuilder-validate",
                },
                {
                    Name:   "us-central1-docker.pkg.dev/image-builder-official/release/builder:stable",
                    Script: "#!/usr/bin/env bash\n/publish",
                    Id:     "imagebuilder-publish",
                },
            },
            Substitutions: subs,
            Options: &cloudbuild.BuildOptions{
                AutomapSubstitutions:  true,
                RequestedVerifyOption: "VERIFIED",
                SubstitutionOption:    "ALLOW_LOOSE",
                DynamicSubstitutions:  true,
            },
            Timeout: "3600s",
        }
    }
    
    func triggerBuild(ctx context.Context) error {
        cbService, err := cloudbuild.NewService(ctx)
        if err != nil {
            return err
        }
        build := createBuildRequest()
        op, err := cbService.Projects.Locations.Builds.Create(fmt.Sprintf("projects/%s/locations/%s", *projectID, *region), build).Do()
        if err != nil {
            return err
        }
        fmt.Printf("Build submitted: %s\n", op.Name)
        return nil
    }
    
    func scheduleBuild(ctx context.Context) error {
        cbService, err := cloudbuild.NewService(ctx)
        if err != nil {
            return err
        }
        csService, err := cloudscheduler.NewService(ctx)
        if err != nil {
            return err
        }
    
        // 1. Create a manual Cloud Build trigger
        trigger := &cloudbuild.BuildTrigger{
            Build:       createBuildRequest(),
            Name:        "scheduled-image-builder-trigger",
            Description: "Manual trigger invoked periodically via Cloud Scheduler for Image Builder",
        }
        createdTrigger, err := cbService.Projects.Locations.Triggers.Create(fmt.Sprintf("projects/%s/locations/%s", *projectID, *region), trigger).Do()
        if err != nil {
            return fmt.Errorf("failed creating trigger: %w", err)
        }
        fmt.Printf("Created Cloud Build trigger with ID: %s\n", createdTrigger.Id)
    
        // 2. Create the Cloud Scheduler job
        targetURI := fmt.Sprintf("https://cloudbuild.googleapis.com/v1/projects/%s/locations/%s/triggers/%s:run", *projectID, *region, createdTrigger.Id)
        job := &cloudscheduler.Job{
            Name:        fmt.Sprintf("projects/%s/locations/%s/jobs/weekly-image-builder-job", *projectID, *region),
            Schedule:    *cronSchedule,
            Description: "Scheduled job to run custom OS Image Builder pipeline",
            HttpTarget: &cloudscheduler.HttpTarget{
                Uri:        targetURI,
                HttpMethod: "POST",
                OauthToken: &cloudscheduler.OAuthToken{
                    ServiceAccountEmail: *serviceAccount,
                },
            },
        }
    
        createdJob, err := csService.Projects.Locations.Jobs.Create(fmt.Sprintf("projects/%s/locations/%s", *projectID, *region), job).Do()
        if err != nil {
            return fmt.Errorf("failed creating scheduler job: %w", err)
        }
        fmt.Printf("Successfully scheduled job: %s\n", createdJob.Name)
        return nil
    }
    

#### Execute the scheduled Go application

To run the compiled Go binary and schedule recurring execution every Monday at 6:00 AM, run the following command:
    
    
    go run main.go \
      --project_id PROJECT_ID \
      --region us-central1 \
      --gcs_workdir gs://STAGING_BUCKET/workdir/ \
      --service_account SERVICE_ACCOUNT_EMAIL \
      --config_path gs://STAGING_BUCKET/imagebuilder.yaml \
      --cron_schedule '0 6 * * 1'
    

## What's next

  * Learn how to [Automate builds on repository events](https://docs.cloud.google.com/compute/docs/images/image-builder/automate-builds-on-events) on Git push, tag, or merge events using Terraform.
  * Review the [Customization recipe schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema) to define software packages and validation procedures.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
