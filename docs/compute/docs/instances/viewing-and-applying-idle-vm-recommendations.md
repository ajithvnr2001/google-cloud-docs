---
url: https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations/
title: View and apply idle VM recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:05.415526+00:00
---

# View and apply idle VM recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View and apply idle VM recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can use idle VM recommendations to identify and stop idle VM instances to reduce waste of resources and reduce your compute bill on your projects.

  * For more information on how Compute Engine generates idle VM recommendations, see [How detection of idle VM instances works](https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview#how_detection_of_idle_vm_instances_works).
  * For more information on how to configure idle VM Recommender to receive more or fewer recommendations, see [Configure idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/configuring-idle-vm-recommendations).



## Before you begin

  * Review the [limitations](https://docs.cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview#limitations) to check if your VM supports idle VM recommendations.
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




## Pricing

Idle VM recommendations are available free of charge. Using recommendations to reduce your resource usage can result in cost savings.

## Viewing idle VM instance recommendations

To view recommendations about idle VMs, use the gcloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeInstanceIdleResourceRecommendations.list` on the project



###  gcloud 

Use the [`gcloud recommender recommendations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) with `--recommender=google.compute.instance.IdleResourceRecommender`:
    
    
    gcloud recommender recommendations list \
      --project=PROJECT_ID \
      --location=ZONE \
      --recommender=google.compute.instance.IdleResourceRecommender \
      --format=yaml
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `ZONE`: the zone that contains instances to list recommendations for



For example:
    
    
    gcloud recommender recommendations list \
      --project=my-project \
      --location=us-central1-c \
      --recommender=google.compute.instance.IdleResourceRecommender \
      --format=yaml
    

If there are no idle VMs in the location, the response is empty. Otherwise, the response includes the following fields for each recommendation:

  * `operationGroups`: groups of operations that you can perform in serial order to apply the recommendation
  * `description`: a human-readable explanation of the recommendation


    
    
    ---
    content:
    ...
    operationGroups:
    - operations:
      - action: test
        path: /status
        resource: //compute.googleapis.com/projects/my-project/zones/us-central1-c/instances/vm-name
        resourceType: compute.googleapis.com/Instance
        value: RUNNING
      - action: replace
        path: /status
        resource: //compute.googleapis.com/projects/my-project/zones/us-central1-c/instances/vm-name
        resourceType: compute.googleapis.com/Instance
        value: TERMINATED
    description: Save cost by stopping Idle VM 'vm-name'.
    etag: '"83da314c23f634e1"'
    lastRefreshTime: '2020-02-24T07:56:40Z'
    name: projects/141732092341/locations/us-central1-c/recommenders/google.compute.instance.IdleResourceRecommender/recommendations/0e061a3a-f921-4216-b1b4-62e16942cd1a
    primaryImpact:
    category: COST
    costProjection:
      cost:
        currencyCode: USD
        nanos: -91533961
        units: '-262'
      duration: 2592000s
    recommenderSubtype: STOP_VM
    stateInfo:
    state: ACTIVE
    

Learn more about working with recommendations using gcloud in [gcloud examples](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations).

###  REST 

Call the [`recommendations.list` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) and use the following recommendation type:

  * **google.compute.instance.IdleResourceRecommender**



The API call looks like:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.instance.IdleResourceRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: the zone that contains instances to list recommendations for.



The following example shows out to send a request with `curl`, and the associated sample response.
    
    
    PROJECT_ID=my-project
    ZONE=us-central1-c
    RECOMMENDER_ID=google.compute.instance.IdleResourceRecommender
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "x-goog-user-project: $PROJECT_ID" \
      https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$ZONE/recommenders/$RECOMMENDER_ID/recommendations
    

Example JSON response for an idle VM recommendation:
    
    
    {
    "description" : "Save cost by stopping Idle VM `vm-name`",
    "name": "projects/1574864402/locations/us-central1-c/recommenders/"
            "google.compute.instance.IdleResourceRecommender/"
            "recommendations/0fd31b24-cc05-4132-8431-ed54a22dd4f1",
    "lastRefreshTime": {
      "seconds": 1543912652
    },
    "primaryImpact": {
      "category": COST,
      "costProjection": {
        "cost": {"currencyCode": "USD", "units": -50},
        "duration": { "seconds": 2592000 }
      }
    },
    "stateInfo": ACTIVE,
    "content":
      "groups" : [
        {
          "operations" : [
          {
            "action": "test",
            "resourceType": "compute.googleapis.com/Instance",
            "resource": "//compute.googleapis.com/projects/my-project/"
                        "zones/us-central1-c/instances/vm-name",
            "path": "/status",
            "value": "RUNNING"
          },
          {
            "action": "replace",
            "resourceType": "compute.googleapis.com/Instance",
            "resource": "//compute.googleapis.com/projects/my-project/"
                        "zones/us-central1-c/instances/vm-name",
            "path": "/status",
            "value": "TERMINATED"
          }
          ]
        }
      ]
    },
    "etag" : "cb0e6ac2cfc0b591"
    }
    

You can find more details about each field in the [Recommender API documentation](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations).

### Interpreting the recommendation response

Each recommendation that you receive through the gcloud CLI or REST contains an operations group, with operations that you can perform in serial to apply the recommendation. Idle VM recommendation operation groups include two operations:

  1. A test operation to verify the current [`status`](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle) of the VM. For example:
         
         {
            "action": "test",
            "resourceType": "compute.googleapis.com/Instance",
            "resource" : "//compute.googleapis.com/projects/my-project/zones/us-central1-c/instances/vm-name",
            "path": "/status",
            "value": "RUNNING"
          }
         

  2. A replace operation to change the `status` of the VM. For example:
         
         {
            "action": "replace",
            "resourceType": "compute.googleapis.com/Instance",
            "resource" : "//compute.googleapis.com/projects/my-project/zones/us-central1-c/instances/vm-name",
            "path": "/status",
            "value": "TERMINATED"
          }
         




The first operation is a `test`, which means that you should test that the `resource` is still `RUNNING`. You can do this by [checking the VM state](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).

The second operation, `replace`, means that you should replace the resource's `status` with a new value, `TERMINATED`. You can do that by stopping the VM, which is described below.

## Applying idle VM recommendations

After you receive an idle VM recommendation and you decide that you no longer need the instance, use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instances) to stop and optionally delete the instance.

If you stop but do not delete an instance and its disks, you still pay for its disks.

**Warning:** Deleting a VM can cause loss of data. Take precautions to protect any data that you need to keep before you delete a VM, for example, by [creating persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.stop` on the instance to stop it.
  * `compute.instances.delete` on the instance to delete it.



###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the instance that you want to stop.
  3. Click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.



###  gcloud 

Use the [`instances stop`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) command and specify the `VM_NAME` that you want to stop.
    
    
    gcloud compute instances stop VM_NAME --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM instance you want to stop
  * `ZONE`: the zone that contains the instance you want to stop



###  REST 

Construct a `POST` request to stop an instance.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `ZONE`: the zone that contains the instance you want to stop
  * `VM_NAME`: the name of the VM instance you want to stop



If you're sure that the VM instance and its disks can be removed you can [delete the instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

## What's next

  * Learn more about how stopping, resetting, and deleting a VM instance [affects the instance and its resources](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle#comparison_table).
  * Learn how to [configure idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/configuring-idle-vm-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
