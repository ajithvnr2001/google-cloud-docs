---
url: https://docs.cloud.google.com/run/docs/configuring/billing-settings/
title: Billing settings for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:27.979284+00:00
---

# Billing settings for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/billing-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Billing settings for services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes billing settings assuming the use of the default Cloud Run [autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) behavior. See [Billing behavior using manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling#cpu-allocation-and-billing) for additional considerations if you use manual scaling.

There are two billing settings in Cloud Run services:

  * **Request-based billing** (default): Cloud Run instances are only charged when they process requests, when they start, and when they shut down. See [instance lifecycle](https://docs.cloud.google.com/run/docs/reference/container-contract#lifecycle) for more details. This setting was previously called _CPU only allocated during request processing_.

  * **Instance-based billing** : Cloud Run instances are charged for the entire lifecycle of instances, even when there are no incoming requests. Instance-based billing can be useful for running short-lived background tasks and other asynchronous processing tasks. This setting was previously called _CPU always allocated_.




If you choose request-based billing, you are charged per request and only when the instance processes a request. If you choose instance-based billing, you are charged for the entire lifecycle of the instance. See the [Cloud Run pricing tables](https://cloud.google.com/run/pricing#tables) for details.

[Recommender](https://docs.cloud.google.com/run/docs/recommender#optimize-billing) automatically looks at traffic received by your Cloud Run service over the past month, and will recommend switching from _request-based billing_ to _instance-based billing_ , if this is cheaper.

**Note:** Unlike Cloud Run services, all Cloud Run jobs have instance-based billing.

## CPU allocation impact

Selecting a billing setting impacts how CPU is allocated.

  * With _request-based billing_ , CPU is only allocated during request processing.
  * With _instance-based billing_ , CPU is allocated for the entire container instance lifecycle.



## Budget spend caps

When you configure Cloud Billing Budget [spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps) in the Cloud Billing console or programmatically using the [Cloud Billing Budget API](https://docs.cloud.google.com/billing/docs/how-to/budget-api-spend-cap), those caps automatically apply to all Cloud Run resource types in your project.

You can monitor your spend cap progress directly from the [Cloud Run console](https://console.cloud.google.com/run/) overview page. When you hit a spend cap, Google Cloud pauses all Cloud Run workloads to prevent further costs to the following Cloud Run resources:

  * Services: any existing service will fail to serve traffic and return `5xx` errors.
  * Jobs: new task executions fail to start, and in-progress tasks fail to complete.
  * Worker pools: any existing instances stop processing tasks.



If you exceed your spend cap, you'll receive an alert notification and see an enforcement banner in the [Cloud Run console](https://console.cloud.google.com/run/). Enforced spend caps reset at the start of each month on the first day of the next billing cycle, unblocking your workloads and setting the spend amount to zero. If you exceed your spend cap and want to resume operations before the monthly reset, manually adjust or lift the cap in the Cloud Run console overview page.

**Note:** Compute Engine bills VPC connector VMs, so Cloud Run spend caps ignore them. If you want spend caps to fully cover egress networking, use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

## How to choose the appropriate billing setting

Choosing the appropriate billing setting for your use case depends on several factors, such as traffic patterns, background execution, and cost, each of which is described in the following sections.

**Note:** There is no container-based way to tell whether an instance changes from idle to actively serving. If detecting this kind of change is an issue for you, you should choose _instance-based billing_.

### Traffic patterns considerations

  * _Request-based billing_ is recommended when incoming traffic is sporadic, bursty or spiky.
  * _Instance-based billing_ is recommended when incoming traffic is steady, slowly varying.



### Background execution considerations

Selecting _instance-based billing_ allocates CPU even outside of request processing, letting you execute short-lived background tasks and other asynchronous processing work after returning responses. For example:

  * Leveraging monitoring agents like OpenTelemetry that may assume to be able to run in the background.
  * Using Go's Goroutines, Node.js async, Java threads, and Kotlin coroutines.
  * Using application frameworks that rely on built-in scheduling or background functionalities.



Idle instances, including those kept warm using [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances), can be shut down at any time. If you need to finish outstanding tasks before the container is terminated, you can trap SIGTERM to give a instance 10 seconds grace time before it is stopped.

Consider using Cloud Tasks for [executing asynchronous tasks](https://docs.cloud.google.com/run/docs/triggering/using-tasks). Cloud Tasks automatically retries failed tasks and supports running times up to 30 minutes.

### Cost considerations

If you are using _request-based billing_ , _instance-based billing_ can be more economical if:

  * Your Cloud Run service is processing high number of current requests at a rather steady rate.
  * You don't see a lot of "idle" instances when looking at the [instance count metric](https://docs.cloud.google.com/run/docs/monitoring).



You can use the [pricing calculator](https://cloud.google.com/products/calculator) to estimate cost differences.

### Autoscaling considerations

Cloud Run by default [autoscales](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) the number of container instances.

For a service set to _request-based billing_ , Cloud Run autoscales the number of instances based on CPU utilization only during request processing.

For a service set to _instance-based billing_ , Cloud Run autoscales the number of instances based on CPU utilization for the entire lifecycle of the container instance, except when [scaling to and from zero](https://docs.cloud.google.com/run/docs/about-instance-autoscaling#instance-based-billing), where it only uses requests.

See [manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling) for additional considerations if you use manual scaling instead of the Cloud Run autoscaling feature.

### Instance-based billing considerations

Even if the billing setting is set to _instance-based billing_ , Cloud Run [autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) is still in effect, and may terminate instances if they aren't needed to handle incoming traffic or current CPU utilization outside of requests. An instance will never stay idle for more than 15 minutes after processing a request unless it is kept active using [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances).

Combining instance-based billing with a number of [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) results in a number of instances up and running with full access to CPU resources, enabling background processing use cases. When using this pattern, Cloud Run applies [instance autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) even if a service is using CPU outside of any requests.

If you use healthcheck probes, you must use instance-based billing for every probe. See [container healthcheck probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#billing) for billing details.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set and update billing

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

If you select instance-based billing, you must specify at least 512MiB of [memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits).

You can change the billing setting using the Google Cloud console, the gcloud CLI, or a YAML file when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu, and click **Deploy container** to configure a new service. If you are configuring an existing service, click the service.

  3. If you are configuring a new service, fill out the initial service settings page.

  4. If you are configuring an existing service, click the **Scaling** tab.

  5. Under **Billing** , select **Request-based** for your instances to be charged only during request processing, or select **Instance-based** for your instances to be charged for the entire lifetime of instances.

  6. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update the billing setting](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update). To set instance-based billing for a given service:
    
    
    gcloud run services update SERVICE --no-cpu-throttling 

Replace SERVICE with the name of your service.

To set request-based billing:
    
    
    gcloud run services update SERVICE --cpu-throttling 

You can also set your billing setting during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy). To set your billing setting to instance-based billing:
    
    
    gcloud run deploy --image IMAGE_URL --no-cpu-throttling

To set your billing setting to request-based billing:
    
    
    gcloud run deploy --image IMAGE_URL --cpu-throttling

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `cpu` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/cpu-throttling: 'BOOLEAN'
               name: REVISION

Replace the following:

     * SERVICE: the name of your Cloud Run service
     * BOOLEAN: `true` to set request-billing, or `false` to set instance-based billing.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-cpu-allocation"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
    ** containers {**
    ** image = "us-docker.pkg.dev/cloudrun/container/hello"**
    ** resources {**
    **# If true, garbage-collect CPU when once a request finishes**
            cpu_idle = false
          }
        }
      }
    }

## View billing settings

To view the current billing settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service to open the **Service details** page.

  3. Click the **Scaling** tab to find the **Billing** setting.




### gcloud

  1. Run the following command to view the billing configuration:
         
         gcloud run services describe SERVICE --format=yaml

  2. In the YAML output, find the `run.googleapis.com/cpu-throttling` setting. A value of `false` indicates instance-based billing, and if this setting is missing, it indicates request-based billing.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
