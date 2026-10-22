---
url: https://docs.cloud.google.com/compute/docs/committed-use-discounts/view-resource-based-commitments/
title: View resource-based commitments \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:35.314484+00:00
---

# View resource-based commitments  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/committed-use-discounts/view-resource-based-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View resource-based commitments Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine lets you view a list of all your purchased resource-based commitments or retrieve the detailed properties of a specific commitment. 

You can view these commitments using the Google Cloud console, the gcloud CLI, or REST.

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

To get the permission that you need to view resource-based commitments, ask your administrator to grant you the Compute Viewer (`roles/compute.viewer`) or Compute Admin (`roles/compute.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.commitments.get` and `compute.commitments.list` permission, which is required to view resource-based commitments. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View a list of commitments

You can view a list of all commitments in your project by using the Google Cloud console, the gcloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Committed use discounts** page. [Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. To view a list of commitments for a specific category, select one of the following tabs:

     * **Hardware commitments** : Select this tab to view commitments for hardware resources, such as vCPUs, memory, GPUs, Local SSD disks, and sole-tenant nodes.
     * **Software license commitments** : Select this tab to view commitments for OS licenses.
     * **Block storage commitments** : Select this tab to view commitments for Exapool capacity.



###  gcloud 

To list all commitments in a specific region, use the [`gcloud compute commitments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/list):
    
    
    gcloud compute commitments list \
        --regions=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `REGION`: the region for which you want to view the commitments.
  * `PROJECT_ID`: the project ID.



#### Examples

For example, to list the commitments within the `us-central1` region using the `project-list-example` project, run the following command:
    
    
    gcloud compute commitments list \
        --regions=us-central1 \
        --project=project-list-example
    

###  REST 

To list commitments in a specific region, make a `GET` request to the [`regionCommitments.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments
    

To list commitments across all regions in your project, make a `GET` request to the [`regionCommitments.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/aggregatedList):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/commitments
    

Replace the following:

  * `PROJECT_ID`: the project ID for the project for which you want to view commitments.
  * `REGION`: the region from which you want to view commitments.



## View details of a specific commitment

You can view the detailed properties of a commitment, such as the following:

  * Status
  * Commitment plan
  * Commitment start and end times
  * Auto-renewal settings
  * Committed resource types and amounts



You can view your commitments by using the Google Cloud console, the gcloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Committed use discounts** page. [Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. Select the tab for the category of commitment that you want to view:

     * To view commitments for hardware resources, click the **Hardware commitments** tab. Hardware commitments cover vCPUs, memory, GPUs, Local SSD disks, and sole-tenant nodes.
     * To view commitments for premium software licenses, select the **Software license commitments** tab. License commitments cover operating system (OS) licenses, such as SUSE Linux Enterprise Server (SLES), SLES for SAP, or Red Hat Enterprise Linux (RHEL).
     * To view commitments for network-attached storage pools, select the **Block storage commitments** tab. Block storage commitments cover Exapool capacity.
  3. To view the details page for a commitment, click the name of the commitment.




###  gcloud 

To describe a specific commitment, use the [`gcloud compute commitments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/describe):
    
    
    gcloud compute commitments describe COMMITMENT_NAME \
        --region=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `COMMITMENT_NAME`: the name of your commitment.
  * `REGION`: the region where the commitment is located.
  * `PROJECT_ID`: the project ID.



#### Examples

The following examples describe commitments in the `myproject` project and the `us-central1` region.

**Example 1: Describe a hardware commitment**

To describe an existing hardware commitment (`example-hardware-commitment`), run the following command:
    
    
    gcloud compute commitments describe example-hardware-commitment \
        --region=us-central1 \
        --project=myproject
    

The command returns the properties of your commitment, similar to the following:
    
    
    autoRenew: true
    category: MACHINE
    creationTimestamp: '2025-05-15T09:30:00.000-07:00'
    endTimestamp: '2026-05-15T09:30:00.000-07:00'
    kind: compute#commitment
    name: example-hardware-commitment
    plan: TWELVE_MONTH
    region: https://www.googleapis.com/compute/v1/projects/myproject/regions/us-central1
    resources:
    - amount: '4'
      type: VCPU
    - amount: '16384'
      type: MEMORY
    status: ACTIVE
    type: GENERAL_PURPOSE
    

**Example 2: Describe a block storage commitment**

To describe an existing block storage commitment (`example-block-storage-commitment`), run the [`gcloud beta compute commitments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/commitments/describe):
    
    
    gcloud beta compute commitments describe example-block-storage-commitment \
        --region=us-central1 \
        --project=myproject
    

The command returns the properties of your commitment, establishing the commitment's relationship to Exapools, similar to the following:
    
    
    autoRenew: true
    category: PERSISTENT_DISK
    creationTimestamp: '2025-08-20T14:45:00.000-07:00'
    endTimestamp: '2026-08-20T14:45:00.000-07:00'
    kind: compute#commitment
    name: example-block-storage-commitment
    persistentDiskResources:
    - amount: '102400'
      dimensionType: CAPACITY_OPTIMIZED
      productType: HYPERDISK_EXAPOOL_BALANCED
    plan: TWELVE_MONTH
    region: https://www.googleapis.com/compute/beta/projects/myproject/regions/us-central1
    status: ACTIVE
    

###  REST 

Make a `GET` request to the [`regionCommitments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/commitments/COMMITMENT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID of your project.
  * `REGION`: the region where the commitment was purchased.
  * `COMMITMENT_NAME`: the name of your commitment.



#### Examples

The following examples retrieve the details of a commitment in the `myproject` project and the `us-central1` region.

**Example 1: Describe a hardware commitment**

To retrieve the properties of a hardware commitment (`example-hardware-commitment`), make the following `GET` request:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/commitments/example-hardware-commitment
    

The response contains the properties of your hardware commitment, similar to the following output:
    
    
    {
      "autoRenew": true,
      "category": "MACHINE",
      "creationTimestamp": "2025-05-15T09:30:00.000-07:00",
      "endTimestamp": "2026-05-15T09:30:00.000-07:00",
      "kind": "compute#commitment",
      "name": "example-hardware-commitment",
      "plan": "TWELVE_MONTH",
      "region": "https://www.googleapis.com/compute/v1/projects/myproject/regions/us-central1",
      "resources": [
        {
          "amount": "4",
          "type": "VCPU"
        },
        {
          "amount": "16384",
          "type": "MEMORY"
        }
      ],
      "status": "ACTIVE",
      "type": "GENERAL_PURPOSE"
    }
    

**Example 2: Describe a block storage commitment**

To retrieve the properties of a block storage commitment (`example-block-storage-commitment`), make the following `GET` request to the [`beta` `regionCommitments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionCommitments/get):
    
    
    GET https://compute.googleapis.com/compute/beta/projects/myproject/regions/us-central1/commitments/example-block-storage-commitment
    

The response contains the properties representing your block storage commitment capacity, similar to the following JSON output:
    
    
    {
      "autoRenew": true,
      "category": "PERSISTENT_DISK",
      "creationTimestamp": "2025-08-20T14:45:00.000-07:00",
      "endTimestamp": "2026-08-20T14:45:00.000-07:00",
      "kind": "compute#commitment",
      "name": "example-block-storage-commitment",
      "persistentDiskResources": [
        {
          "amount": "102400",
          "dimensionType": "CAPACITY_OPTIMIZED",
          "productType": "HYPERDISK_EXAPOOL_BALANCED"
        }
      ],
      "plan": "TWELVE_MONTH",
      "region": "https://www.googleapis.com/compute/beta/projects/myproject/regions/us-central1",
      "status": "ACTIVE"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
