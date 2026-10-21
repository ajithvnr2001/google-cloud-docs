---
url: https://docs.cloud.google.com/compute/docs/instances/view-references-between-resources/
title: Viewing referrers to VM instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:17:33.158006+00:00
---

# Viewing referrers to VM instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-references-between-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Viewing referrers to VM instances Stay organized with collections  Save and categorize content based on your preferences. 

If you want to view the relationships between VM instances and other Compute Engine resources, use the [`listReferrers` REST API method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/listReferrers).

When you use REST, Compute Engine returns a list of references that describe:

  * The source resource: the resource that is pointing to the target resource
  * The target resource: the resource in question
  * The reference type: the relationship between the two resources



For example, you can use REST to conveniently view a list of instance groups that a VM instance belongs to.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations

  * You can only list relationships between VM instances and instance groups (both managed and unmanaged).
  * You can only list referrers by using REST.



## Listing a single referrer

A referrer is a resource that refers to another resource. For VM instances, a common referrer is an instance group.

For example, assume that you have a VM instance named `example-ig-a1` in zone `us-central1-a`. The VM instance is a member of an instance group called `example-ig` in the same zone, as shown in the diagram below:

[ ![A virtual machine instance is a member of an instance group in the
            same zone.](https://docs.cloud.google.com/static/compute/images/instance-group-referrers-diagram.svg)](https://docs.cloud.google.com/static/compute/images/instance-group-referrers-diagram.svg)

To see this relationship, call the [`listReferrers` method](https://docs.cloud.google.com/compute/docs/reference/v1/instances/listReferrers) on `example-ig-a1` with the following HTTP request:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-ig-a1/referrers
    

The server returns standard list response containing the following items:
    
    
    "items": [
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-ig-a1,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-ig
      }
    ]
    

In this case, the `target` is `example-ig-a1`, which is a `MEMBER_OF` the `referrer`, the `example-ig instance` group.

## Listing multiple referrers

If a resource has more than one referrer, the response returns a list of all referrers for the target resource. If an instance belongs to two instance groups, the response contains both instance groups.

[ ![If a virtual machine instance is a member of two instance groups,
            the response contains both instance groups.](https://docs.cloud.google.com/static/compute/images/instance-group-referrers-multiple-diagram.svg)](https://docs.cloud.google.com/static/compute/images/instance-group-referrers-multiple-diagram.svg)

For example, the following response indicates that the instance named `example-instance-a2` belongs to two instance groups, `example-ig` and `example-ig-2`:
    
    
    "items": [
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-instance-a2,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-ig
      },
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-instance-a2,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-ig-2
      }
    ]
    

## Listing cross-scope referrers

The `listReferrers` method also returns information about referrers that exist inside other scopes, such as other regions or zones. For example, assume that you have a VM instance that belongs to a regional managed instance group (regional MIG):

[ ![In region us-central1, instance new-instance-a3 in
            zone us-central1-a is a member of
            the example-rmig regional instance group.](https://docs.cloud.google.com/static/compute/images/instance-group-referrers-cross-scope-diagram.svg)](https://docs.cloud.google.com/static/compute/images/instance-group-referrers-cross-scope-diagram.svg)

You call the `listReferrers` method targeting this instance with the following HTTP request:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/new-instance-a3/referrers
    

The server returns a standard list response containing the following items:
    
    
    "items": [
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/new-instance-a3,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/instanceGroups/example-rmig
      }
    ]
    

The response shows the regional instance group in the list of referrers.

## Listing referrers to all resources within a collection

By using the wildcard character (`-`), you can request a list of all referrers to all VM instances within a specific zone. The request can be made with an HTTP request that is similar to the following:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/-/referrers
    

The server returns a response containing a list of VM instances in the zone and references to the instance. For example:
    
    
    "items": [
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-ig-a1,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-ig
      },
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-ig-a2,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-ig
      },
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/example-ig-a2,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instanceGroups/example-ig-2
      },
      {
        "target": https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances/new-instance-a3,
        "referenceType": MEMBER_OF,
        "referrer": https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-central1/instanceGroups/example-rmig
      }
    ]
    

## What's next

  * Learn more about [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).
  * See a list of applicable [zones and regions](https://docs.cloud.google.com/compute/docs/regions-zones).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
