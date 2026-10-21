---
url: https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling/
title: Manual scaling \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:53.852681+00:00
---

# Manual scaling  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Manual scaling Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manually scale your service. It also provides instructions for a common use case, changing the instance count based on a schedule using Cloud Scheduler jobs and the Cloud Run Admin API.

## Overview

Manual scaling lets you set a specific instance count, regardless of traffic or utilization, and without requiring redeployment. All of this gives you the option to write your own scaling logic using an external system. For an example, see Schedule-based scaling.

By default, Cloud Run [automatically scales out](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) to a specified or default maximum number of instances, depending on traffic, CPU, or your own [custom CPU or concurrency utilization targets](https://docs.cloud.google.com/run/docs/configuring/scaling-controls). However, for some use cases, you might want the ability to set a specific number of instances by using manual scaling.

### Revision-level minimum and maximum settings and manual scaling

If you set your service to manual scaling, any [revision-level minimum](https://docs.cloud.google.com/run/docs/configuring/min-instances#service-vs-revision-level) and maximum instance settings are ignored.

### Traffic splits for manual scaling

The following list describes how instances are allocated when splitting traffic under manual scaling. This includes behavior for traffic-tag-only revisions.

  * During a traffic split, each revision is allocated instances proportionally, based on traffic split, similar to [traffic splitting with service-level minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances#traffic-splitting).

  * If the number of revisions receiving traffic exceeds the manual instance count, some of the revisions will have no instances. Traffic sent to those revisions will get the same error as if the revisions were disabled.

  * For all revisions receiving traffic in a traffic split, any revision-level minimum and maximum instances are disabled.

  * If a revision is active _only_ [due to traffic tags](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags):

    * If revision-level minimum instances is set, the specified number of instances will start but does _not_ count toward the total service manual instance count. The revision will _not_ autoscale.
    * If revision-level minimum instances is not set, the revision scales out to at most _one_ instance, in response to traffic sent to the tag URL.



## Billing behavior using manual scaling

When you use manual scaling, billing behavior is similar to the behavior when you use the [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) feature.

That is, with manual scaling and [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings#choosing-instance-based-billing), manually scaled idle instances are billed as _active_ instances.

If you use manual scaling with [request-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings), manually scaled idle instances are billed as _idle minimum-instances_. For complete billing details, see the [pricing page](https://cloud.google.com/run/pricing).

### Required roles

To get the permissions that you need to deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity
  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) on the Artifact Registry repository of the deployed container image (if applicable)



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure manual scaling

**Note:** Changing scaling mode from automatic to manual or vice-versa, or changing the manual instance count does _not_ create a new revision.

You can configure the scaling mode using the Google Cloud console, the Google Cloud CLI, YAML file, or API when you [create a service or update a revision](https://docs.cloud.google.com/run/docs/deploying):

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. If you are configuring a new service, click **Deploy container** to display the **Create service** form. If you are configuring an existing service, click the service to display its detail panel, then click the **Scaling** tab.

  3. Click **Manual scaling**.

  4. Specify the number of container instances for the service in the **Number of instances** field.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To specify scaling for a new service, use the [deploy command](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy):
    
    
    gcloud run deploy SERVICE \
        --scaling=INSTANCE_COUNT \
        --image IMAGE_URL

Replace the following:

  * SERVICE: the name of your service.
  * INSTANCE_COUNT: the number of instances for the service. This sets the service to manual scaling. Specify a value of `0` to disable the service. Specify a value of `auto` to use the default Cloud Run autoscaling behavior.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .



Specify scaling for an existing service by using the following [update command](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update):
    
    
    gcloud run services update SERVICE \
       --scaling=INSTANCE_COUNT

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `scalingMode` and `manualInstanceCount` attributes:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           annotations:
           run.googleapis.com/scalingMode: MODE
           run.googleapis.com/manualInstanceCount: INSTANCE_COUNT

Replace the following:

     * SERVICE: the name of your Cloud Run service
     * MODE: `manual` for manual scaling, or `automatic` for the default Cloud Run autoscaling behavior.
     * INSTANCE_COUNT: the number of instances you are manually scaling for the service. Specify a value of `0` to disable the service.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




###  REST API

To update the number of instances for a given service in manual scaling, send a `PATCH` HTTP request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/patch).

For example, using `curl`:
    
    
        curl -H "Content-Type: application/json" \
        -H "Authorization: Bearer ACCESS_TOKEN" \
        -X PATCH \
        -d '{"scaling":{"manualInstanceCount":MANUAL_INSTANCE_COUNT }}' \
        https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE?update_mask=scaling.manualInstanceCount

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to update a service](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into `gcloud`, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * MANUAL_INSTANCE_COUNT: the number of instances for the service. This sets the service to manual scaling. Specify a value of `0` to disable the service.
  * SERVICE: the name of the service.
  * REGION: the Google Cloud region that the service is deployed in.
  * PROJECT_ID: the Google Cloud project ID.



To switch the scaling mode from manual to automatic, send a `PATCH` request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/patch) and set the `scalingMode` field to `AUTOMATIC`.

For example, run the following `curl` command:
    
    
          curl -H "Content-Type: application/json" \
          -H "Authorization: Bearer ACCESS_TOKEN" \
          -X PATCH \
          -d '{"launchStage":"BETA","scaling":{"scalingMode": "AUTOMATIC","manualInstanceCount":null}}' \
          https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE?update_mask=launchStage,scaling.scalingMode,scaling.manualInstanceCount

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE_NAME"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
      scaling {
        scaling_mode = "MANUAL"
        manual_instance_count = "INSTANCE_COUNT"
      }
    }
    

Replace the following:

  * SERVICE_NAME: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * INSTANCE_COUNT: the number of instances you are manually scaling for the service. This number of instances is divided among all revisions with specified traffic based on the percent of traffic they are receiving.



## View scaling configuration for your service

To view the scaling configuration instances for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** panel.

  3. Click the **Scaling** tab to find the scaling settings.




###  gcloud 

Use the following command to view the current scaling configuration for the service:
    
    
    gcloud run services describe SERVICE

Replace SERVICE with the name of your service.

Look for the field `Scaling: Manual (Instances: )` near the top of the text returned from the `describe`.

###  YAML 

Use the following command to download the service [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
    
    
    gcloud run services describe SERVICE --format export > service.yaml

The scaling configuration is contained in the `scalingMode` and `manualInstanceCount` attributes.

## Disable a service

When you disable a service, any requests that are currently being processed will be allowed to complete. However, any further requests to the service URL will fail with a `Service unavailable` or `Service disabled` error.

Requests to service revisions that are only active due to traffic tags are not impacted because those revisions are not disabled.

To disable a service, you set scaling to zero. You can disable a service using the Google Cloud console, the Google Cloud CLI, YAML file, or API:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you want to disable to display its detail panel, then click the **Scaling** tab.

  3. Select **Manual scaling**.

  4. Enter the value `0` (zero) in the field labelled **Number of instances**.

  5. Click **View diff & deploy**, then **Deploy changes**.




###  gcloud 

To disable a service, use the following command to set scaling to zero:
    
    
    gcloud run services update SERVICE --scaling=0

Replace SERVICE with the name of your service.

### YAML

  1. Download your service's [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Set the `manualInstanceCount` attribute to zero (`0`):
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           annotations:
           run.googleapis.com/scalingMode: manual
           run.googleapis.com/manualInstanceCount: `0`

Replace SERVICE with the name of your Cloud Run service.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml




###  REST API

To disable a service, send a `PATCH` HTTP request to the Cloud Run Admin API [`service` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/patch).

For example, using `curl`:
    
    
        curl -H "Content-Type: application/json" \
        -H "Authorization: Bearer ACCESS_TOKEN" \
        -X PATCH \
        -d '{"scaling":{"manualInstanceCount":0 }}' \
        https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/services/SERVICE?update_mask=scaling.manualInstanceCount

Replace the following:

  * ACCESS_TOKEN: a valid access token for an account that has the [IAM permissions to update a service](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into `gcloud`, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * SERVICE: the name of the service.
  * REGION: the Google Cloud region that the service is deployed in.
  * PROJECT_ID: the Google Cloud project ID.



### Terraform

To disable a service, set the `manual_instance_count` attribute to zero (`0`):
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE_NAME"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
        }
      }
      scaling {
        scaling_mode = "MANUAL"
        manual_instance_count = "0"
      }
    }
    

Replace the following:

  * SERVICE_NAME: the name of your Cloud Run service.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG`



## Schedule-based scaling example

A common use case of manual scaling is changing the instance count based on a predefined schedule. In this example, we use Cloud Scheduler to schedule two jobs, each of which invokes the Cloud Run Admin API to scale the number of instances. The first Cloud Scheduler job sets the service to manually scale to a specified number of instances during business hours (9am-5pm, M-F). The second job sets the service to scale down to a specified number of instances during off-hours.

In this example, we use the [Cloud Run quickstart](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container) for simplicity, but you can use a service of your choice.

To set up schedule-based manual scaling:

  1. Deploy your service using the following command:
         
         gcloud run deploy SERVICE \
            --image=us-docker.pkg.dev/cloudrun/container/hello \
            --region=REGION \
            --project PROJECT_ID

Replace the following:

     * SERVICE: the name of the Cloud Run service.
     * REGION: the region the Cloud Run service is deployed to.
     * PROJECT_ID: the Google Cloud project ID.
  2. Configure your service for manual scaling to 10 instances using the following command:
         
         gcloud run services update SERVICE \
            --region=REGION \
            --scaling=10

  3. Create a Cloud Scheduler job that manually scales to a specified number of service instances during business hours:
         
         gcloud scheduler jobs create http hello-start-instances \
           --location=REGION \
           --schedule="0 9 * * MON-FRI" \
           --time-zone=America/Los_Angeles \
           --uri=https://run.googleapis.com/v2/projects/PROJECT_ID/
           locations/REGION/services/hello?update_mask=launchStage,scaling.manualInstanceCount \
           --headers=Content-Type=application/json,X-HTTP-Method-Override=PATCH \
           --http-method=PUT \
           --message-body='{"scaling":{"manualInstanceCount":INSTANCE_COUNT}}' \
           --oauth-service-account-email=PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace the following:

     * REGION: the region the Cloud Run service is deployed to.
     * PROJECT_ID: the Google Cloud project ID.
     * INSTANCE_COUNT: the number of instances you want to scale to—for example, `10`.
     * PROJECT_NUMBER: the Google Cloud project number.

This command creates a Cloud Scheduler job that makes an HTTP call to the Cloud Run Admin API, setting the number of instances to the number you specify. The example uses the Compute Engine default service account `PROJECT_NUMBER-compute@developer.gserviceaccount.com` for the Cloud Scheduler jobs. You can use any service account that has permissions to update Cloud Run services.

**Note:** This example uses the `X-HTTP-Method-Override=PATCH` header because the Cloud Scheduler CLI does not support setting `http-method=PATCH`. If you configure the Cloud Scheduler job using the Google Cloud console, you can set the HTTP method to PATCH, and exclude the header.
  4. Create a Cloud Scheduler job that manually scales down service instances during off hours:
         
         gcloud scheduler jobs create http hello-stop-instances \
           --location=REGION \
           --schedule="0 17 * * MON-FRI" \
           --time-zone=America/Los_Angeles \
           --uri=https://run.googleapis.com/v2/projects/PROJECT_ID/
           locations/REGION/services/hello?update_mask=launchStage,scaling.manualInstanceCount \
           --headers=Content-Type=application/json,X-HTTP-Method-Override=PATCH \
           --http-method=PUT \
           --message-body='{"scaling":{"manualInstanceCount":INSTANCE_COUNT}}' \
           --oauth-service-account-email=PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace the following:

     * REGION: the region the Cloud Run service is deployed to.
     * PROJECT_ID: the Google Cloud project ID.
     * INSTANCE_COUNT: the number of instances you want to scale to. To disable the service, set this to `0`.
     * PROJECT_NUMBER: the Google Cloud project number.

This command creates a Cloud Scheduler job that makes an HTTP call to the Cloud Run Admin API, setting manual scaling instances to the number of instances you specified. Setting the instances to zero effectively disables the service, but not the Cloud Scheduler jobs. Those jobs continue to run and will reset (and re-enable) the service to an increased number of instances as scheduled.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
