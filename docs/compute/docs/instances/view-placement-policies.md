---
url: https://docs.cloud.google.com/compute/docs/instances/view-placement-policies/
title: View placement policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:58:05.116592+00:00
---

# View placement policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-placement-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View placement policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view placement policies.

Viewing [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) is useful to see all the existing placement policies in a project, or verify the configuration details of a specific placement policy.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

To get the permissions that you need to view placement policies, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view placement policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view placement policies:

  * To view a list of your placement policies: `compute.resourcePolicies.list` on the project 
  * To view the details of a placement policy: `compute.resourcePolicies.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View your placement policies

To view the placement policies that are available in a project, select one of the following methods described in this document:

  * To see all the existing placement policies in a project, view a list of your placement policies.

  * To see the configuration details of a placement policy, view the details of a placement policy.




### View a list of your placement policies

To view a list of all the placement policies in your project, select one of the following options:

###  gcloud 

To view a list of placement policies, use the [`gcloud compute resource-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list) with the `--filter` flag set to `groupPlacementPolicy:*`.
    
    
    gcloud compute resource-policies list \
        --filter="groupPlacementPolicy:*"
    

The output is similar to the following:
    
    
    NAME: example-compact-policy
    DESCRIPTION:
    REGION: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
    CREATION_TIMESTAMP: 2024-05-09T02:09:24.588-07:00
    
    NAME: example-spread-policy
    DESCRIPTION:
    REGION: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
    CREATION_TIMESTAMP: 2024-05-09T02:08:13.404-07:00
    

For more information about using filter expressions to narrow down a list of Compute Engine resources, see the [`gcloud topic filters` command](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

###  REST 

To view a list of placement policies that are located in a specific region, make a `GET` request to the [`resourcePolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/list). In the request URL, include the `filter` query parameter and set it to `groupPlacementPolicy%3A*`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies?filter=groupPlacementPolicy%3A*
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which you want to view a list of placement policies.

  * `REGION`: the region where one or more placement policies are located.




The output is similar to the following:
    
    
    {
      "kind": "compute#resourcePolicyList",
      "id": "projects/example-project/regions/us-central1/resourcePolicies",
      "items": [
        {
          "kind": "compute#resourcePolicy",
          "id": "5587673659722509355",
          "creationTimestamp": "2024-05-09T02:09:24.588-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/example-compact-policy",
          "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
          "name": "example-compact-policy",
          "groupPlacementPolicy": {
            "collocation": "COLLOCATED"
          },
          "status": "READY"
        },
        {
          "kind": "compute#resourcePolicy",
          "id": "5970772604948130963",
          "creationTimestamp": "2024-05-09T02:08:13.404-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/example-spread-policy",
          "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
          "name": "example-spread-policy",
          "groupPlacementPolicy": {
            "availabilityDomainCount": 5
          },
          "status": "READY"
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies",
      "etag": "-L7XCupTQ5V9__TOJ8G5RDcR2cY=/g_xt0udkOM_tU7jSL0z9I2Sivis="
    }
    

For more information about using filter expressions to narrow down a list of resource policies using [URL-encoding](https://en.wikipedia.org/wiki/URL_encoding), see the [`filter` query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/list#body.QUERY_PARAMETERS.filter).

### View the details of a placement policy

To view the details of a placement policy, select one of the following options:

###  gcloud 

To view the details of a placement policy, use the [`gcloud compute resource-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/describe).

**Note:** If you want to view the `maxDistance` field in a compact placement policy, use the [`gcloud beta compute resource-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/resource-policies/describe) instead.
    
    
    gcloud compute resource-policies describe POLICY_NAME \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of an existing placement policy.

  * `REGION`: the region where the placement policy is located.




The output is similar to the following:

  * If you're viewing the details of a compact placement policy:
        
        creationTimestamp: '2024-05-09T02:09:24.588-07:00'
        groupPlacementPolicy:
          collocation: COLLOCATED
        id: '5587673659722509355'
        kind: compute#resourcePolicy
        name: example-compact-policy
        region: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
        selfLink: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/example-compact-policy
        status: READY
        

  * If you're viewing the details of a spread placement policy:
        
        creationTimestamp: '2024-05-09T02:08:13.404-07:00'
        groupPlacementPolicy:
          availabilityDomainCount: 5
        id: '5970772604948130963'
        kind: compute#resourcePolicy
        name: example-spread-policy
        region: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
        selfLink: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/example-spread-policy
        status: READY
        




###  REST 

To view the details of a placement policy, make a `GET` request to the [`resourcePolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/get).

**Note:** If you want to view the `maxDistance` field in a compact placement policy, make a `GET` request to the [`beta.resourcePolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/resourcePolicies/get) instead.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the placement policy you want to view the details of is located.

  * `REGION`: the region where the placement policy is located.

  * `POLICY_NAME`: the name of an existing placement policy.




The output is similar to the following:

  * If you're viewing the details of a compact placement policy:
        
        {
          "kind": "compute#resourcePolicy",
          "id": "5587673659722509355",
          "creationTimestamp": "2024-05-09T02:09:24.588-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/example-compact-policy",
          "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
          "name": "example-compact-policy",
          "groupPlacementPolicy": {
            "collocation": "COLLOCATED"
          },
          "status": "READY"
        }
        

  * If you're viewing the details of a spread placement policy:
        
        {
          "kind": "compute#resourcePolicy",
          "id": "5970772604948130963",
          "creationTimestamp": "2024-05-09T02:08:13.404-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/example-spread-policy",
          "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
          "name": "example-spread-policy",
          "groupPlacementPolicy": {
            "availabilityDomainCount": 5
          },
          "status": "READY"
        }
        




## What's next?

  * Learn how to [replace, remove, or delete placement policies](https://docs.cloud.google.com/compute/docs/instances/manage-placement-policies).

  * Learn how to apply a placement policy:

    * [Apply compact placement policies to VMs](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#apply-policy).

    * [Apply spread placement policies to VMs](https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies#apply-policy).

  * Learn how to [verify the physical location of your VMs](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
