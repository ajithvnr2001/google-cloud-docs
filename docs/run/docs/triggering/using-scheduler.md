---
url: https://docs.cloud.google.com/run/docs/triggering/using-scheduler/
title: Running services on a schedule \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:57.223599+00:00
---

# Running services on a schedule  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/using-scheduler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Running services on a schedule Stay organized with collections  Save and categorize content based on your preferences. 

You can use Cloud Scheduler to securely trigger a Cloud Run service on a schedule. This is similar to using cron jobs.

Possible use cases include:

  * Performing backups on a timed basis
  * Performing recurrent administration tasks, such as: 
    * Re-generating a sitemap
    * Deleting old data, content, configuration, or revisions
    * Synchronizing content between data systems
    * Processing daily email notifications
    * Verifying and reporting on access to downstream services
  * Generating documents, such as bills



This page shows how to securely use Cloud Scheduler with Cloud Run in the same Google Cloud project.

## Before you start

[Enable the Cloud Scheduler API](http://console.cloud.google.com/apis/library/cloudscheduler.googleapis.com) on the project you are using.

## Creating and deploying your service

To create and deploy:

  1. In your service, implement the job that you want to run on a schedule.

  2. Note which request type your service is expecting to receive the job requests from, for example, `GET` or `POST`. When you create the scheduled job that invokes your service, you'll need to specify the HTTP method that matches this.

  3. When you [deploy the service](https://docs.cloud.google.com/run/docs/deploying) you are using with Cloud Scheduler, make sure you select ** Require authentication.** Don't allow public access.




The following example shows how to deploy a Cloud Run service using Terraform:
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "my-scheduled-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.run_api
      ]
    }

Replace `us-docker.pkg.dev/cloudrun/container/hello` with a reference to your own container image.

## Creating a service account for Cloud Scheduler

You need to create a service account to associate with Cloud Scheduler, and give that service account the permission to invoke your Cloud Run service. You can use an existing service account to represent Cloud Scheduler, or you can create a new one.

To create a service account and give it permission to invoke the Cloud Run service:

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

  2. Select a project.

  3. Enter a service account name to display in the Google Cloud console.

The Google Cloud console generates a service account ID based on this name. Edit the ID if necessary. You cannot change the ID later.

  4. Optional: Enter a description of the service account.

  5. Click **Create and continue**.

  6. Optional: Click the **Select a role** field.

  7. Select **Cloud Run** > **Cloud Run Invoker**.

  8. Click **Done**.




###  Command line

  1. Create the service account:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
            --display-name "DISPLAYED_SERVICE_ACCOUNT_NAME"

Replace

     * SERVICE_ACCOUNT_NAME with a **lower case** name unique within your Google Cloud project, for example `my-invoker-service-account-name`.
     * DISPLAYED_SERVICE_ACCOUNT_NAME with the name you want to display for this service account, for example, in the console, for example, `My Invoker Service Account`.
  2. For Cloud Run, give your service account permission to invoke your service:
         
         gcloud run services add-iam-policy-binding SERVICE \
            --member=serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
            --role=roles/run.invoker

Replace

     * SERVICE with the name of the service you want to be invoked by Cloud Scheduler.
     * SERVICE_ACCOUNT_NAME with the name of the service account.
     * PROJECT_ID with your Google Cloud project ID.
  3. Grant your service account access to the project so that it has permission to complete specific actions on the resources in your project:
         
         gcloud projects add-iam-policy-binding RESOURCE_ID \
            --member=PRINCIPAL --role=roles/run.invoker

Replace

     * RESOURCE_ID: Your Google Cloud project ID.

     * PRINCIPAL: An identifier for the principal, or member, which usually has the following form: PRINCIPAL_TYPE:ID. For example, `user:my-user@example.com`. For a full list of the values that PRINCIPAL can have, see the [Policy Binding reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy#Binding).




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To create a service account using Terraform: 
    
    
    resource "google_service_account" "default" {
      account_id   = "scheduler-sa"
      description  = "Cloud Scheduler service account; used to trigger scheduled Cloud Run jobs."
      display_name = "scheduler-sa"
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.iam_api
      ]
    }
    
    resource "google_cloud_run_service_iam_member" "default" {
      location = google_cloud_run_v2_service.default.location
      service  = google_cloud_run_v2_service.default.name
      role     = "roles/run.invoker"
      member   = "serviceAccount:${google_service_account.default.email}"
    }

## Creating a Cloud Scheduler job

You'll need to create a job that invokes your service at specified times. You can use either the console or the command line:

To create a job you can use either the console or the gcloud command line. Click on the appropriate tab:

###  Console 

  1. Visit the Cloud Scheduler console page.

[Go to Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

  2. Click **Create job**.

![screenshot](https://docs.cloud.google.com/static/scheduler/docs/images/cron-console.png)

  3. Supply a name for the job.

  4. Specify the frequency, or job interval, at which the job is to run, using a configuration string. For example, the string `0 */3 * * *` runs the job every 3 hours. The string you supply here can be any [crontab](http://man7.org/linux/man-pages/man5/crontab.5.html) compatible string.

For more information, see [Configuring Job Schedules](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).

  5. From the dropdown list, choose the timezone to be used for the job frequency.

  6. Specify `HTTP` as the target:

     1. Specify the fully qualified URL of your service, for example `https://myservice-abcdef-uc.a.run.app` The job will send requests to this URL.

     2. Specify the HTTP method: the method must match what your previously deployed Cloud Run service is expecting. The default is `POST`.

     3. Optionally, specify the data to be sent to the target. This data is sent in the body of the request when either the `POST` or `PUT` HTTP method is selected.

     4. Click **More** to show the auth settings.

     5. From the dropdown menu, select **Add OIDC token**.

     6. In the _Service account_ field, copy the service account email of the service account you created previously.

     7. In the **Audience** field, copy the full URL of your service.

  7. Click **Create** to create and save the job.




###  Command line 

You need to use OIDC authentication to access an authenticated Cloud Run service from Cloud Scheduler. OIDC authentication includes the service account and audience flags. For more information, see [Use Authentication for HTTP Targets](https://docs.cloud.google.com/scheduler/docs/http-target-auth).

To create the Cloud Scheduler job:
    
    
    gcloud scheduler jobs create http test-job --schedule "5 * * * *"   
           --http-method=HTTP-METHOD   
           --uri=SERVICE-URL   
           --oidc-service-account-email=SERVICE-ACCOUNT-EMAIL     
           --oidc-token-audience=SERVICE-URL

Replace

  * HTTP-METHOD with the HTTP method (i.e. GET, POST, PUT, etc).
  * SERVICE-URL with your service URL.
  * SERVICE-ACCOUNT-EMAIL with your service account email.



### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To create a Cloud Scheduler job for the Cloud Run service: 
    
    
    resource "google_cloud_scheduler_job" "default" {
      name             = "scheduled-cloud-run-job"
      region           = "us-central1"
      description      = "Invoke a Cloud Run container on a schedule."
      schedule         = "*/8 * * * *"
      time_zone        = "America/New_York"
      attempt_deadline = "320s"
    
      retry_config {
        retry_count = 1
      }
    
      http_target {
        http_method = "POST"
        uri         = google_cloud_run_v2_service.default.uri
    
        oidc_token {
          service_account_email = google_service_account.default.email
        }
      }
    
      # Use an explicit depends_on clause to wait until API is enabled
      depends_on = [
        google_project_service.scheduler_api
      ]
    }

Your Cloud Run service will be triggered via a request by the Cloud Scheduler job at the frequency you defined. You can confirm and monitor this by examining the [logs for this service](https://docs.cloud.google.com/run/docs/logging#viewing_logs_in).

## What's next

  * [Logging and viewing logs](https://docs.cloud.google.com/run/docs/logging)
  * [Monitoring health and performance](https://docs.cloud.google.com/run/docs/monitoring)
  * [Triggering from Pub/Sub](https://docs.cloud.google.com/run/docs/triggering/pubsub-push)
  * [Invoking with HTTPS](https://docs.cloud.google.com/run/docs/triggering/https-request)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
