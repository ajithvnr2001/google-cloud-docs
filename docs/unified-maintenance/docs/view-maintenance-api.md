---
url: https://docs.cloud.google.com/unified-maintenance/docs/view-maintenance-api/
title: View resource maintenances by using the API \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:55.791914+00:00
---

# View resource maintenances by using the API  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/view-maintenance-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  View resource maintenances by using the API Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Unified Maintenance API to return information about maintenance on your resources.

This document describes how to use Cloud Shell to call the Unified Maintenance API to return resource maintenance.

To view upcoming and historical maintenance activities in Cloud Hub, see [View maintenance activities](https://docs.cloud.google.com/hub/docs/maintenance).

## Before you begin

Before you view maintenance on your resources using Unified Maintenance, verify that Unified Maintenance supports your [resource types](https://docs.cloud.google.com/unified-maintenance/docs/supported-services).

To view maintenance activities for App Hub applications ([Preview](https://cloud.google.com/products#product-launch-stages)), you must define applications from your existing Google Cloud resources in [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) or create and deploy them with [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview).

## Filters

You can filter which maintenance activities are returned by several parameters:

  * State (`SUCCEEDED`, or `STARTED`, for example)
  * Resource name
  * Resource location
  * Resource type
  * Maintenance name
  * Maintenance start time
  * Maintenance end time



For more information, see [Unified Maintenance API](https://docs.cloud.google.com/unified-maintenance/docs/reference/rest/v1beta/projects.locations.resourceMaintenances/list) documentation.

## View resource maintenances

You can use the Unified Maintenance API to return maintenance activity information for a Google Cloud project. If you are managing applications in a [folder-level boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), use the folder's management project.

To list all maintenance activities:

  1. Go to Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/cloudshell)

  2. Run the command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type:
         application/json" \
         https://maintenance.googleapis.com/v1beta/projects/PROJECT_ID/locations/LOCATION/resourceMaintenances
         

Replace:

     * `PROJECT_ID`: The project ID of your project.
     * `LOCATION`: Region or zone containing your project. Set to `global`, `region`, or `-` (to match all locations).
  3. Unified Maintenance returns information about resource maintenances for your specified project.




### View maintenances for a resource

You can use the Unified Maintenance API to return maintenances for a specified resource.

To filter and print maintenances for a specified resource:

  1. Go to Cloud Shell.

[Go to Cloud Shell](https://console.cloud.google.com/cloudshell)

  2. Run the command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type:
         application/json" \
         https://maintenance.googleapis.com/v1beta/projects/PROJECT_ID/locations/LOCATION/resourceMaintenances?filter=FILTER=%22RESOURCE_NAME%22
         

Replace:

     * `PROJECT_ID`: The project ID of your project.
     * `LOCATION`: Region or zone containing your project. Set to `global`, `region`, or `-` (to match all locations).
     * `RESOURCE_NAME`: The full resource name of your resource.

**Note:** For target resources that are regional and global, the location of `ResourceMaintenance` is always the same as the target resource location.  
For target resources that are zonal, the `ResourceMaintenance` location is a region corresponding to the zone of target resource. For example, for a Cloud SQL instance in the `us-west1-a` zone, the `ResourceMaintenance` is in the `us-west1` region.

## What's next

  * Learn how to [configure alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications) based on different webhooks.
  * Use Unified Maintenance to [reschedule or perform on-demand updates](https://docs.cloud.google.com/unified-maintenance/docs/reschedule-and-on-demand-updates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
