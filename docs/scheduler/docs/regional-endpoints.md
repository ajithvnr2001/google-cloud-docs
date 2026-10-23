---
url: https://docs.cloud.google.com/scheduler/docs/regional-endpoints/
title: Use regional endpoints \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:39.397320+00:00
---

# Use regional endpoints  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Use regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Scheduler regional endpoints let you keep API traffic within a single Google Cloud region to help meet [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) and data sovereignty requirements. When you send a request to a regional endpoint, TLS terminates, and Cloud Scheduler processes the request entirely within the specified region.

Cloud Scheduler regional endpoints have the format `https://cloudscheduler.REGION.rep.googleapis.com` where `REGION` is a [supported region](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints)—for example, `https://cloudscheduler.us-central1.rep.googleapis.com`.

For information about using Private Service Connect to access Cloud Scheduler regional endpoints privately from inside a Virtual Private Cloud (VPC) network, see [About accessing regional and multi-regional Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

## Limitations and restrictions

The following limitations and restrictions apply when you use Cloud Scheduler regional endpoints.

  * A regional endpoint serves only the resources in its own region. The location in the resource name must match the region of the endpoint. For example, you can send requests for resources in `projects/PROJECT_ID/locations/us-central1` to `cloudscheduler.us-central1.rep.googleapis.com`. Requests for resources in other regions fail.
  * Regional endpoints apply to requests sent to the Cloud Scheduler API. They don't change how Cloud Scheduler sends requests to your job targets. If your jobs run in a VPC Service Controls perimeter, see the requirements for job targets in [Secure cron jobs with VPC Service Controls](https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc).



## Send requests to a regional endpoint

You can send requests to a regional endpoint using the Google Cloud CLI, the REST API, or the Cloud Scheduler client libraries.

###  gcloud 

Set the `api_endpoint_overrides/cloudscheduler` property to the regional endpoint, and then run `gcloud scheduler` commands for resources in that region:
    
    
    gcloud config set api_endpoint_overrides/cloudscheduler \
        https://cloudscheduler.REGION.rep.googleapis.com/
    gcloud scheduler jobs list --location=REGION

Replace `REGION` with a region that offers regional endpoints—for example, `us-central1`.

To use the default global endpoint again, unset the property:
    
    
    gcloud config unset api_endpoint_overrides/cloudscheduler

###  REST 

Use the regional endpoint as the host of the request URL. For example, the following command lists the jobs in a region:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://cloudscheduler.REGION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/jobs"

Replace the following:

  * `REGION`: a region that offers regional endpoints—for example, `us-central1`.
  * `PROJECT_ID`: your Google Cloud project ID.



###  Client libraries 

Set the API endpoint when you create the client. The following examples create a client for `us-central1`:

###  Go 
    
    
    import (
    scheduler "cloud.google.com/go/scheduler/apiv1"
    "google.golang.org/api/option"
    )
    
    client, err := scheduler.NewCloudSchedulerClient(ctx,
    option.WithEndpoint("cloudscheduler.us-central1.rep.googleapis.com:443"))

###  Java 
    
    
    import com.google.cloud.scheduler.v1.[CloudSchedulerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1.CloudSchedulerClient.html);
    import com.google.cloud.scheduler.v1.[CloudSchedulerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1.CloudSchedulerSettings.html);
    
    [CloudSchedulerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1.CloudSchedulerSettings.html) settings =
      [CloudSchedulerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1.CloudSchedulerSettings.html).newBuilder()
          .setEndpoint("cloudscheduler.us-central1.rep.googleapis.com:443")
          .build();
    try ([CloudSchedulerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1.CloudSchedulerClient.html) client = [CloudSchedulerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-scheduler/latest/com.google.cloud.scheduler.v1.CloudSchedulerClient.html).create(settings)) {
    // Send requests for resources in us-central1.
    }

###  Python 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import [scheduler_v1](https://docs.cloud.google.com/python/docs/reference/cloudscheduler/latest)
    
    client = [scheduler_v1](https://docs.cloud.google.com/python/docs/reference/cloudscheduler/latest).[CloudSchedulerClient](https://docs.cloud.google.com/python/docs/reference/cloudscheduler/latest/google.cloud.scheduler_v1.services.cloud_scheduler.CloudSchedulerClient.html)(
      client_options=ClientOptions(
          api_endpoint="cloudscheduler.us-central1.rep.googleapis.com"
      )
    )

## What's next

  * [Cloud Scheduler locations](https://docs.cloud.google.com/scheduler/docs/locations)
  * [Access regional and multi-regional Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
