---
url: https://docs.cloud.google.com/compute/docs/instance-groups/view-workload-policies/
title: View workload policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:24.817741+00:00
---

# View workload policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/view-workload-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View workload policies Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view workload policies.

After you create and apply workload policies to managed instance groups (MIGs), you can view the configuration details of those policies. Viewing workload policies helps you gain an overview of all the workload policies in your project, or verify the configuration details of a specific policy.

To learn more about the requirements and limitations that you apply when you create workload policies, see [About workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).

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

To get the permissions that you need to view workload policies, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view workload policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view workload policies:

  * To view a list of your workload policies: `compute.resourcePolicies.list` on the project 
  * To view the details of a workload policy: `compute.resourcePolicies.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View your workload policies

To view the workload policies that exist in your project, use one of the following methods:

  * To see all the existing workload policies in a project, view a list of your workload policies.

  * To see the configuration details of a specific workload policy, view the details of a workload policy.




### View a list of your workload policies

To view a list of all the workload policies in your project, select one of the following options:

###  gcloud 

To view a list of workload policies, use the [`gcloud compute resource-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list) with the `--filter` flag set to `workloadPolicy:*`.
    
    
    gcloud compute resource-policies list \
        --filter="workloadPolicy:*"
    

The output is similar to the following:
    
    
    NAME: workload-policy-01
    DESCRIPTION:
    REGION: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
    CREATION_TIMESTAMP: 2026-03-18T02:20:11.010-07:00
    
    NAME: workload-policy-02
    DESCRIPTION:
    REGION: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
    CREATION_TIMESTAMP: 2026-03-18T09:24:58.281-07:00
    

For more information about using filter expressions to narrow down a list of Compute Engine resources, see the [`gcloud topic filters` command](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

###  REST 

To view a list of workload policies in a specific region, make a `GET` request to the [`resourcePolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/list). In the request URL, include the `filter` query parameter and set it to `workloadPolicy%3A*`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies?filter=workloadPolicy%3A*
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which you want to view a list of workload policies.

  * `REGION`: the region where one or more workload policies exist.




The output is similar to the following:
    
    
    {
      "kind": "compute#resourcePolicyList",
      "id": "projects/example-project/regions/us-central1/resourcePolicies",
      "items": [
        {
          "workloadPolicy": {
            "type": "HIGH_THROUGHPUT"
          },
          "kind": "compute#resourcePolicy",
          "id": "7592369487854686373",
          "creationTimestamp": "2026-03-18T02:20:11.010-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/workload-policy-01",
          "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
          "name": "workload-policy-01",
          "status": "READY"
        },
        {
          "workloadPolicy": {
            "type": "HIGH_THROUGHPUT",
            "maxTopologyDistance": "BLOCK"
          },
          "kind": "compute#resourcePolicy",
          "id": "5947350722329145141",
          "creationTimestamp": "2026-03-18T09:24:58.281-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/workload-policy-02",
          "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
          "name": "workload-policy-02",
          "status": "READY"
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies",
      "etag": "ntWQ-oLKD9MWsxuxLOpT5pDF0To=/2MdxB9oc-_-zK6Z7g0OIqrUQ0BI="
    }
    

For more information about using filter expressions to narrow down a list of resource policies using [URL-encoding](https://en.wikipedia.org/wiki/URL_encoding), see the [`filter` query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/list#body.QUERY_PARAMETERS.filter).

### View the details of a workload policy

To view the details of a workload policy, select one of the following options:

###  gcloud 

To view the details of a workload policy, use the [`gcloud compute resource-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/describe).
    
    
    gcloud compute resource-policies describe POLICY_NAME \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of an existing workload policy.

  * `REGION`: the region where the workload policy exists.




The output is similar to the following:
    
    
    creationTimestamp: '2026-03-18T02:20:11.010-07:00'
    id: '7592369487854686373'
    kind: compute#resourcePolicy
    name: workload-policy-01
    region: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/workload-policy-01
    status: READY
    workloadPolicy:
      type: HIGH_THROUGHPUT
    

###  REST 

To view the details of a workload policy, make a `GET` request to the [`resourcePolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the workload policy you want to view the details of exists.

  * `REGION`: the region where the workload policy exists.

  * `POLICY_NAME`: the name of an existing workload policy.




The output is similar to the following:
    
    
    {
      "workloadPolicy": {
        "type": "HIGH_THROUGHPUT"
      },
      "kind": "compute#resourcePolicy",
      "id": "7592369487854686373",
      "creationTimestamp": "2026-03-18T02:20:11.010-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/resourcePolicies/workload-policy-01",
      "region": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1",
      "name": "workload-policy-01",
      "status": "READY"
    }
    

## What's next

  * Learn how to [replace, remove, or delete workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/manage-workload-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
