---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments/
title: Purchase software commitments for OS licenses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:34.859257+00:00
---

# Purchase software commitments for OS licenses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Purchase software commitments for OS licenses Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine provides resource-based committed use discounts (CUDs) for your predictable workloads that use applicable premium operating system (OS) licenses. You can purchase commitments for licenses to run VM instances that use applicable SLES, SLES for SAP, or RHEL images. 

This document explains how to purchase resource-based commitments for OS licenses by using the Google Cloud console, the gcloud CLI, or REST.

To learn more about license commitments, including the qualifying images and discount rates, see [Software license commitments](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#software-license-commitments).

## Before you begin

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

To get the permission that you need to purchase commitments for licenses, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.commitments.create` permission, which is required to purchase commitments for licenses. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

By default, project owners have permission to purchase resource-based commitments. However, it's possible for owners to create custom roles that include or exclude certain users. To make sure that you have permission to purchase a resource-based commitment, see [Access control](https://docs.cloud.google.com/compute/docs/access).

## Purchase an OS license commitment

Purchase software resource-based commitments for OS licenses using the Google Cloud console, the gcloud CLI, or REST.

After you purchase a commitment, your commitment becomes active on the following day at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time). Compute Engine [ maintains a lien on your project](https://docs.cloud.google.com/resource-manager/docs/project-liens) for each region in your project where you purchase a commitment. When you purchase a new commitment for any region in your project, Compute Engine associates the lien for that region with the newly created commitment. 

Between the time of your commitment purchase and its activation time, the status of your commitment remains as `NOT_YET_ACTIVE` (or as `PENDING` on the Google Cloud console). After activation, the status of your commitment changes to `ACTIVE`. For example, suppose that you purchase your commitment on January 20, 2024, at 10:00 PM US and Canadian Pacific Time (UTC-8 or UTC-7). Compute Engine creates your commitment immediately with its status as `NOT_YET_ACTIVE`. Your commitment becomes `ACTIVE` on January 21, 2024, at 12:00 AM US and Canadian Pacific Time (UTC-8 or UTC-7). 

**Important:** After you purchase a commitment, you can't cancel it. If you move the project that is associated with the commitment to a different Cloud Billing account, then the project inherits the attribution and CUD sharing settings that apply to the destination account. For more information, see [Impact of changing a project's Cloud Billing account](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#moving-project-billing-account).

###  Console 

Before you purchase a commitment using the Google Cloud console, select the project where you want to use the resources and apply your CUDs. If you enabled [CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) for your project's Cloud Billing account, then you can purchase the commitment for any project from that Cloud Billing account.

After you select the project, perform the following steps:

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

The **Commitment list** page appears and displays the **Hardware commitments** tab.

  2. Click **Software license commitments**.

  3. Click **Purchase commitment**.

The **Purchase a committed use discount** page appears.

  4. In the **Name** field, enter a name for your commitment.

  5. In the **Region** field, select the region where you want to use resources at committed-use-discounted prices.

  6. For **Duration** , select either **1 year** or **3 years** as the _[plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan)_ for your commitment. The plan determines the CUD rate and preset term duration of your commitment.

  7. In the **License family** field, select the OS license for which you want to purchase the commitment.

  8. In the **License type and quantity** section, do the following:

     1. For **Type** , select the number of vCPUs that applies.
     2. For **Number of licenses** , enter the number of OS licenses that you want to commit to purchasing.
  9. In the **Summary** pane, review your commitment timeline and details.

  10. To purchase your commitment, do the following:

     1. Click **Purchase**. The **Purchase a committed use discount** dialog appears.

     2. In the dialog, review the acceptance disclosures regarding monthly fees, commitment terms, and the [service specific terms](https://cloud.google.com/terms/service-terms).

     3. To confirm your commitment purchase, click **Purchase**.




###  gcloud 

To purchase a license commitment by using the gcloud CLI, run the [`gcloud compute commitments create-license` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license):
    
    
    gcloud compute commitments create-license COMMITMENT_NAME \
        --license LICENSE_URI \
        --amount NUMBER_OF_LICENSES \
        --cores-per-license CORES_PER_LICENSE \
        --plan PLAN \
        --region REGION
    

Replace the following:

  * `COMMITMENT_NAME`: the name for your commitment.
  * `LICENSE_URI`: the license URI. For example: `https://www.googleapis.com/compute/v1/projects/myproject/global/licenses/sles-sap-12`
  * `NUMBER_OF_LICENSES`: the number of licenses that you plan to purchase.
  * `CORES_PER_LICENSE`: the number of cores per license. Enter `1-2`, `3-4`, or `5+`.
  * `PLAN`: enter the plan length: `12-month` or `36-month`.
  * `REGION`: the region where this commitment applies.



For example, to purchase a 3-year commitment for 4 SLES licenses with 3-4 cores per license in the `us-central1` region, run the following command:
    
    
    gcloud compute commitments create-license commitment-1 \
        --license=https://www.googleapis.com/compute/v1/projects/myproject/global/licenses/sles-12 \
        --amount=4 \
        --cores-per-license=3-4 \
        --plan=36-month \
        --region=us-central1
    

For example, to purchase a 1-year commitment for 2 SLES for SAP licenses with 1-2 cores per license in the `us-central1` region, run the following command:
    
    
    gcloud compute commitments create-license commitment-2 \
        --license=https://www.googleapis.com/compute/v1/projects/myproject/global/licenses/sles-sap-12 \
        --amount=2 \
        --cores-per-license=1-2 \
        --plan=12-month \
        --region=us-central1
    

###  REST 

Use the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert) and include the `licenseResource` field to define the license commitment's properties.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments?requestId=OPTIONAL_UNIQUE_ID
    
    {
        "name": "COMMITMENT_NAME",
        "plan": "PLAN",
        "category": "LICENSE",
        "licenseResource": {
          "coresPerLicense": "CORES_PER_LICENSE",
          "amount": "NUMBER_OF_LICENSES",
          "license": "LICENSE_URI"
        }
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment.
  * `OPTIONAL_UNIQUE_ID`: Optional. A unique request ID to help prevent unintended duplicate requests.
  * `COMMITMENT_NAME`: the name for your commitment.
  * `LICENSE_URI`: the license URI. For example: `https://www.googleapis.com/compute/v1/projects/myproject/global/licenses/sles-sap-12`
  * `NUMBER_OF_LICENSES`: the number of licenses that you plan to purchase.
  * `CORES_PER_LICENSE`: the number of cores per license. Enter `1-2`, `3-4`, or `5+`.
  * `PLAN`: enter the plan length: `TWELVE_MONTH` or `THIRTY_SIX_MONTH`.
  * `REGION`: the region where this commitment applies.



For example, to purchase a 3-year commitment for 4 SLES for SAP licenses with 3-4 cores per license in the `us-central1` region, make the following POST request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/commitments
    
    {
        "name": "commitment-3",
        "plan": "THIRTY_SIX_MONTH",
        "category": "LICENSE",
        "licenseResource": {
          "coresPerLicense": "3-4",
          "amount": "4",
          "license": "https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12"
          }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
