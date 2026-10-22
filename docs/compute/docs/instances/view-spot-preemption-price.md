---
url: https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price/
title: View the preemption rate and pricing for Spot VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:13.768823+00:00
---

# View the preemption rate and pricing for Spot VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View the preemption rate and pricing for Spot VMs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to view the preemption rate and pricing for Spot VMs.

Before you create [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), you can view the historical and current preemption rates and pricing for the machine type that you want your Spot VMs to use. Viewing this data helps you compare the stability and cost of different machine types and locations to find the best fit for your workload and budget.

If you want to view real-time data about Spot VMs, then see the following instead:

  * To view the current cost of Spot VMs, see [Spot VMs pricing](https://cloud.google.com/spot-vms/pricing).

  * To view if capacity is available in the zone where you want to create Spot VMs, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).




## Limitations

You can't view the preemption rate and pricing trend for N1 machine types that have GPUs attached, custom machine types, or TPUs.

## Understand preemption rate and pricing for Spot VMs

When you send a request to the `advice.capacityHistory` API, the output shows the following metrics. By understanding these metrics, you can view and compare the preemption rate trend and pricing trend across machine types and zones, and then use this data to inform your decisions when you create Spot VMs.

  * Historical preemption rate

  * Historical pricing




### Historical preemption rate

The historical preemption rate (`preemptionHistory`) shows the daily preemption rates for your specified machine type and zone over the past 30 days. Compute Engine sets the data boundaries for this rate at midnight Pacific Time (PT). The preemption rate for the current day might change throughout the day.

Compute Engine calculates the preemption rate by dividing the number of Spot VMs preempted in a day across Google Cloud by the number of Spot VMs that stopped running that same day, as shown in the following formula. These stops include when users or programmatic actions (such as limited runtimes) suspend, stop, or delete Spot VMs, or when Compute Engine preempts them.

$${preemptionHistory}=\frac{\text{Total preempted Spot VMs in a day}}{\text{Total Spot VMs that stopped running in a day}}$$ 

The preemption rate ranges from `0.00` to `1.00`. For example, a rate of `0.50` indicates that, among the Spot VMs with a specific machine type and in a specific zone that stopped running that day across Google Cloud, Compute Engine preempted 50% of them.

### Historical pricing

The historical pricing (`priceHistory`) shows the price changes in USD for your specified machine type and region over the past year. Each entry indicates the hourly price for the time interval when that price was active. Compute Engine sets price changes at midnight (00:00 AM) PT. If data is unavailable, then the time intervals have gaps.

## Before you begin

  * The `advice.capacityHistory` API includes [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) by default in its output. To help ensure that you can create Spot VMs in AI zones if the API recommends that you create VMs in one of these zones, [ verify that AI zones are enabled for your project](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#check-ai-zone-status).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to view the preemption rate and pricing of Spot VMs, ask your administrator to grant you the [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view the preemption rate and pricing of Spot VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view the preemption rate and pricing of Spot VMs:

  * To view the preemption rate and pricing of Spot VMs: `compute.advice.capacityHistory` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View the preemption rate and pricing for Spot VMs

To view the historical preemption rate and pricing for Spot VMs, you must specify the machine type, and the region or zone, where you want to create VMs. Based on the results, you can either create the Spot VMs, or view the preemption rate and pricing in another location or for a different machine.

To view the preemption rate and pricing for Spot VMs, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Capacity advisor** page.

[Go to Capacity advisor](https://console.cloud.google.com/compute/capacityAdvisor)

  2. In the **Filters** pane, complete the following steps:

     1. In **Location** section, in the **Region** list, select the regions where you want to create Spot VMs.

     2. In the **Machine specifications** section, specify the machine configuration and number of Spot VMs that you want to create:

        1. In the **Machine family** list, select a [machine family](https://docs.cloud.google.com/compute/docs/machine-resource).

        2. In the **Series** list, select up to three machine series.

        3. In the **Machine type** list, select up to five machine types.

        4. In the **Number of VMs** field, enter the number of Spot VMs.

        5. Optional: By default, zones that have limited resources available are hidden. To view these zones, clear the **Hide regions with limited availability** checkbox.

     3. Click search **Search**.

  3. Based on your use case, select one of the following options:

     * To view pricing, availability, and preemption rates for a specific location, complete the following steps:

       1. In the **Results for provisioning model** pane, click the **Map** tab.

       2. On the map, click a region. A pane that shows the pricing and zonal preemption rates for that region appears.

     * To compare historical pricing and preemption rates across different machine types, complete the following steps:

       1. In the **Results for provisioning model** pane, click the **List** tab.

       2. Select two or more rows containing the machine types that you want to compare.

       3. Click compare_arrows **Compare prices**. The **Machine type comparison** pane appears.

       4. To view pricing data or preemption rates, click the **Price** or **Preemption** tab.

       5. Optional: To change the machine types to compare, do one of the following:

          * To add a machine type, click **Add machine type** , and then select the machine type that you want to add.

          * To remove a machine type, in the **Actions** column for the machine type that you want to remove, click close **Remove row**.




###  gcloud 

To view the preemption rate and pricing for Spot VMs, use the [`gcloud beta compute advice capacity-history` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/advice/capacity-history).

Based on your use case, include the following flags:

  * To view preemption rate and pricing in a region, include the `--types=PREEMPTION,PRICE` and `--region` flags:
        
        gcloud beta compute advice capacity-history \
            --provisioning-model=SPOT \
            --machine-type=MACHINE_TYPE \
            **--types=PREEMPTION,PRICE** \
            **--region= REGION**
        

  * To view preemption rate in a zone, include the `--types=PREEMPTION` and `--zone` flags:
        
        gcloud beta compute advice capacity-history \
            --provisioning-model=SPOT \
            --machine-type=MACHINE_TYPE \
            **--types=PREEMPTION** \
            **--zone= ZONE**
        




Replace the following:

  * `MACHINE_TYPE`: the machine type that you want your Spot VMs to use.

  * `REGION`: the region where you want to create Spot VMs.

  * `ZONE`: the zone where you want to create Spot VMs.




The output is similar to the following:
    
    
    location: https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-a
    machineType: n2-standard-32
    preemptionHistory:
    - interval:
        endTime: "2026-04-21T07:00:00Z"
        startTime: "2026-04-20T07:00:00Z"
      preemptionRate: 0.52
    - interval:
        endTime: "2026-04-22T07:00:00Z"
        startTime: "2026-04-21T07:00:00Z"
      preemptionRate: 0.64
    ...
    priceHistory:
    - interval:
        endTime: "2026-05-11T07:00:00Z"
        startTime: "2026-04-27T07:00:00Z"
      listPrice:
        currencyCode: "USD"
        nanos: "478720000"
    - interval:
        endTime: "2026-05-12T07:00:00Z"
        startTime: "2026-05-11T07:00:00Z"
      listPrice:
        currencyCode: "USD"
        nanos: "502720000"
    ...
    

###  REST 

To view the preemption rate and pricing for Spot VMs, make a `POST` request to the [beta `advice.capacityHistory` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/advice/capacityHistory).

Based on your use case, make one of the following requests:

  * To view preemption rate and pricing in a region, make the following request:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/advice/capacityHistory
        
        {
          "types": [
            "PREEMPTION",
            "PRICE"
          ],
          "instanceProperties": {
            "scheduling": {
              "provisioningModel": "SPOT"
            },
            "machineType": "MACHINE_TYPE"
          }
        }
        

  * To view preemption rate in a zone, make the following request:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/advice/capacityHistory
        
        {
          "types": [
            "PREEMPTION"
          ],
          "instanceProperties": {
            "scheduling": {
              "provisioningModel": "SPOT"
            },
            "machineType": "MACHINE_TYPE"
          },
          "locationPolicy": {
            "location": "zones/ZONE"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `REGION`: the region where you want to create Spot VMs.

  * `MACHINE_TYPE`: the machine type that you want your Spot VMs to use.

  * `ZONE`: the zone, which must be within `REGION`, where you want to create Spot VMs.




The output is similar to the following:
    
    
    {
      "machineType": "n2-standard-32",
      "location": "https://compute.googleapis.com/compute/beta/projects/example-project/regions/us-central1",
      "preemptionHistory": [
        {
          "interval": {
            "startTime": "2026-04-20T07:00:00Z",
            "endTime": "2026-04-21T07:00:00Z"
          },
          "preemptionRate": 0.52
        },
        {
          "interval": {
            "startTime": "2026-04-21T07:00:00Z",
            "endTime": "2026-04-22T07:00:00Z"
          },
          "preemptionRate": 0.64
        },
        ...
      ],
      "priceHistory": [
        {
          "interval": {
            "startTime": "2026-04-27T07:00:00Z",
            "endTime": "2026-05-11T07:00:00Z"
          },
          "listPrice": {
            "currencyCode": "USD",
            "nanos": "478720000"
          }
        },
        {
          "interval": {
            "startTime": "2026-05-11T07:00:00Z",
            "endTime": "2026-05-12T07:00:00Z"
          },
          "listPrice": {
            "currencyCode": "USD",
            "nanos": "502720000"
          }
        },
        ...
      ]
    }
    

## What's next

  * Learn how to [create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot).

  * Learn more about the [best practices for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
