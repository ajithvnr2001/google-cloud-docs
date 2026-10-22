---
url: https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations/
title: View and apply idle resources recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:15.557523+00:00
---

# View and apply idle resources recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View and apply idle resources recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view and apply idle resources recommendations for Persistent Disk volumes, IP addresses, and custom disk images.

Compute Engine helps you identify idle Persistent Disk volumes, IP addresses, and custom disk images, and provides recommendations to help you minimize waste and avoid unnecessary charges.

If you're interested in recommendations for idle virtual machine (VM) instances, then see [View and apply idle VM recommendations](https://docs.cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations).

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




## Pricing

There are no costs associated with using idle resources recommendations.

## Recommendation generation

If a resource has not been attached to a VM or other resource for 15 days, then the Recommender classifies that resource as idle. For more information about the conditions to classify a resource as idle and the recommended actions, see the following table:

Resource | Condition for resource to be classified as idle | Recommended action | Savings  
---|---|---|---  
Persistent Disk | All of the following must be true:  


  * The Persistent Disk was created at least 15 days ago.
  * The Persistent Disk was never attached to a VM.
  * The Persistent Disk is blank.
  * The Persistent Disk isn't bound to GKE Pods.

| Delete | Save 100% of the cost of that disk. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing).  
Persistent Disk | All of the following must be true:  


  * The Persistent Disk was detached for at least 15 days.
  * The Persistent Disk isn't bound to GKE Pods.

| Create a snapshot of the Persistent Disk, and then delete it.  
**Note:** Depending on the location, the cost of the snapshot might be higher than the Persistent Disk. In such cases, the recommendation to create a snapshot doesn't appear, as it wouldn't generate any savings.  | Reduce the maintenance cost of that disk from 35% to 92%. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing).  
  
Custom image | All of the following must be true:  


  * The image wasn't used to create a disk for at least 15 days.
  * The image isn't used in any instance template.

| Delete | Save 100% of the cost of that image. For more information, see [Disk and image pricing](https://cloud.google.com/compute/disks-image-pricing).  
External IP address | The IP address hasn't been attached to any resource for at least 15 days. | Delete  
**Note:** In some cases, you might receive recommendations to delete [Bring your own IP addresses (BYOIP)](https://docs.cloud.google.com/vpc/docs/byoip-planning). You can ignore such recommendations, since you're not charged for idle BYOIP addresses.  | Save 100% of the cost of that IP address. For more information, see [External IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).   
  
## Recommendation frequency

Idle resource recommendations begin 15 days after resource creation, and they are updated once every 24 hours.

## Viewing recommendations

To view recommendations about idle resources, use the gcloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeDiskIdleResourceRecommendations.list` on the project for idle Persistent Disk volumes
  * `recommender.computeAddressIdleResourceRecommendations.list` on the project for idle IPs
  * `recommender.computeImageIdleResourceRecommendations.list` on the project for idle custom images



### Console

In the Google Cloud console, go to the **All recommendations** page.

[Go to Recommendations](https://console.cloud.google.com/active-assist/list/all/recommendations)

All idle resources are listed under **Unused Compute Engine resources**.

### gcloud

Use the [`gcloud recommender recommendations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) with the `--recommender=`[`RECOMMENDER_ID`](https://docs.cloud.google.com/recommender/docs/recommenders) flag:
    
    
    gcloud recommender recommendations list \
        --project=PROJECT_ID \
        --location=LOCATION \
        --recommender=RECOMMENDER_ID \
        --format=yaml
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the location that contains the resources for which you want recommendations. 
    * For Persistent Disk volumes specify a zone or region; for example, `us-central1-c`.
    * For IPs: 
      * To list regional IPs, you must specify a region.
      * To list global IPs, specify `global`. For more information about regional and global IP address resources, see [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress).
    * For custom images specify `global`.
  * `RECOMMENDER_ID`: the ID of [recommender](https://docs.cloud.google.com/recommender/docs/recommenders)
    * For disks, specify `google.compute.disk.IdleResourceRecommender`.
    * For images, specify `google.compute.image.IdleResourceRecommender`.
    * For IPs, specify `google.compute.address.IdleResourceRecommender`.



For example, the following command lists idle Persistent Disk recommendations in `us-central1-c` for `test-project`:
    
    
    gcloud recommender recommendations list \
        --project=test-project \
        --location=us-central1-c \
        --recommender=google.compute.disk.IdleResourceRecommender \
        --format=yaml
    
    
    ---
    content:
        operationGroups:
        - operations:
          - action: add
            resource: //compute.googleapis.com/projects/test-project/global/snapshots/$snapshot-name
            resourceType: compute.googleapis.com/Disk
            path: /
            value:
            - name: $snapshot-name
              sourceDisk: projects/test-project/locations/us-central1-c/disks/pd-name
              storageLocations: us-central1
          - action: remove
            resource: //compute.googleapis.com/projects/test-project/zones/us-central1-c/disks/pd-name
            resourceType: compute.googleapis.com/Disk
            path: /
    description: Save cost by snapshotting and then deleting idle persistent disk 'pd-name'
    name: projects/test-project/locations/us-central1-c/recommenders/google.compute.disk.IdleResourceRecommender/recommendations/0fd31b24-cc05-4132-8431-ed54a22dd4f1
    recommenderSubtype: SNAPSHOT_AND_DELETE_DISK
    lastRefreshTime:
      seconds: 1543912652
    primaryImpact:
      category: COST
      costProjection:
        cost:
          currencyCode: USD
          units: '-50'
        duration:
          seconds: 2592000
    stateInfo: ACTIVE
    etag: "cb0e6ac2cfc0b591"
    

Learn more about using gcloud CLI to work with [recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

###  REST 

Call the [`recommendations.list` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) and specify the [recommender id](https://docs.cloud.google.com/recommender/docs/recommenders), for example `google.compute.disk.IdleResourceRecommender`:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/RECOMMENDER_ID/recommendations
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the location that contains the resources for which you want recommendations. 
    * For Persistent Disk volumes specify a zone or region; for example, `us-central1-c`.
    * For IPs: 
      * To list regional IPs, you must specify a region.
      * To list global IPs, specify `global`. For more information about regional and global IP address resources, see [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress).
    * For custom images specify `global`.
  * `RECOMMENDER_ID`: the ID of [recommender](https://docs.cloud.google.com/recommender/docs/recommenders)
    * For disks, specify `google.compute.disk.IdleResourceRecommender`.
    * For images, specify `google.compute.image.IdleResourceRecommender`.
    * For IPs, specify `google.compute.address.IdleResourceRecommender`.



The following example shows out to send a request with `curl`, and the associated sample response.
    
    
    PROJECT_ID=test-project
    LOCATION=us-central1-c
    RECOMMENDER_ID=google.compute.disk.IdleResourceRecommender
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$LOCATION/recommenders/$RECOMMENDER_ID/recommendations
    

Example JSON response for idle Persistent Disk recommendation: 
    
    
    {
     "description" : "Save cost by deleting idle persistent disk 'pd-name'",
     "name": "projects/test-project/locations/us-central1-c/recommenders/"
             "google.compute.disk.IdleResourceRecommender/"
             "recommendations/0fd31b24-cc05-4132-8431-ed54a22dd4f1",
     "recommenderSubtype" : "SNAPSHOT_AND_DELETE_DISK",
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
     "content": {
       "operationGroups" : [
        {
          "operations" : [
           {
             "action": "add",
             "resourceType": "compute.googleapis.com/Disk",
             "resource" : "//compute.googleapis.com/projects/test-project/global/snapshots/$snapshot-name",
             "value": {
               "name": "$snapshot-name",
               "sourceDisk": "projects/test-project/zones/us-central1-c/disks/pd-name",
               "storageLocations": ["us-central1"],
             }
           },
           {
             "action": "remove",
             "resourceType": "compute.googleapis/Disk",
             "resource": "//compute.googleapis.com/projects/test-project/"
                         "zones/us-central1-c/disks/pd-name"
           }
          ]
        }
       ]
     },
     "associatedInsights": [
        {
          "insight": "projects/test-project/locations/us-central1-c/insightTypes/google.compute.disk.IdleResourceInsight/insights/31326443-bcc3-4776-9b86-48879fddb656"
        }
      ],
     "etag": "cb0e6ac2cfc0b591"
    }
    

### Interpreting the recommendation response

Each recommendation that you receive through the gcloud CLI or REST contains operation groups, with operations that you can perform in serial to apply the recommendation. For example, idle Persistent Disk recommendation operation groups include one or two operations:

  * If your idle Persistent Disk has data on it, then the recommendation includes an `add` operation to create a snapshot to back up the Persistent Disk. For example:
        
        {
             "action": "add",
             "resourceType": "compute.googleapis.com/Disk",
             "resource" : "//compute.googleapis.com/projects/test-project/global/snapshots/$snapshot-name",
             "path": "/",
             "value": {
               "name": "$snapshot-name",
               "sourceDisk": "projects/test-project/zones/us-central1-c/disks/pd-name",
               "storageLocations": ["us-central1"]
             }
           }
        

  * A `remove` operation to permanently delete the idle Persistent Disk. For example:
        
        {
             "action": "remove",
             "resourceType": "compute.googleapis.com/Disk",
             "resource" : "//compute.googleapis.com/projects/test-project/zones/us-central1-c/disks/pd-name",
             "path": "/"
           }
        




### Viewing insights for idle resource recommendations

The Recommender generates recommendations based on resource [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights). By viewing insights on resources you can learn more about those resources, such as how long a resource has been detached from a VM or whether a Persistent Disk is blank.

If you want to view the [insight](https://docs.cloud.google.com/recommender/docs/insights/using-insights) that generated the recommendation, you can use the gcloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeDiskIdleResourceInsights.list` on the project for idle PDs
  * `recommender.computeAddressIdleResourceInsights.list` on the project for idle IPs
  * `recommender.computeImageIdleResourceInsights.list` on the project for idle images



###  gcloud 

Use the [`insights list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/insights/list)
    
    
    gcloud beta recommender insights list --project=PROJECT_NAME \
      --location=LOCATION --insight-type=INSIGHT_TYPE
    

Replace the following:

  * `LOCATION`: the location that contains the resources for which you want insights. 
    * For PDs specify a zone or region, for example, `us-central1-c`.
    * For IPs: 
      * To list regional IPs, you must specify a region.
      * To list global IPs, specify `global`. For more information about regional and global IP address resources, see [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress).
    * For custom images specify `global`.
  * `INSIGHT_TYPE`: the ID of the [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types)
    * For disks, specify `google.compute.disk.IdleResourceInsight`.
    * For images, specify `google.compute.image.IdleResourceInsight`.
    * For IPs, specify `google.compute.address.IdleResourceInsight`.



###  REST 

Use the [`insights.list` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list).
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE/insights
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `LOCATION`: the location that contains the resources for which you want insights. 
    * For Persistent Disk volumes specify a zone or region; for example, `us-central1-c`.
    * For IPs: 
      * To list regional IPs, you must specify a region.
      * To list global IPs, specify `global`. For more information about regional and global IP address resources, see [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress).
    * For custom images specify `global`.
  * `INSIGHT_TYPE`: the ID of the [insight type](https://docs.cloud.google.com/recommender/docs/insights/insight-types)
    * For disks, specify `google.compute.disk.IdleResourceInsight`.
    * For images, specify `google.compute.image.IdleResourceInsight`.
    * For IPs, specify `google.compute.address.IdleResourceInsight`.



Here is an example response of an insight on an idle Persistent Disk resource:
    
    
    {
      "name": "projects/test-project/locations/us-central1-c/insightTypes/google.compute.disk.IdleResourceInsight/insights/0ec21a13-bb04-3121-7321-dc43a11cc3e2",
      "description": "Disk 'pd-name' in zone 'us-central1-c' was last used 17 days ago. Consider taking snapshot and delete it.",
      "targetResources": [
        "//compute.googleapis.com/projects/test-project/zones/us-central1-c/disks/pd-name"
      ],
      "insightSubtype": "IDLE_DISK",
      "content": {
        "diskLastUseTime": "2019-10-01 13:00:00",
        "isBlank": false,
      },
      "lastRefreshTime": "2019-10-10 13:00:00",
      "observationPeriod": "15 days",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "COST",
      "etag": "fds421j2349",
      "associatedRecommendations": [
        {
          "projects/test-project/locations/us-central1-c/recommenders/"
          "google.compute.disk.IdleResourceRecommender/"
          "recommendations/0fd31b24-cc05-4132-8431-ed54a22dd4f1"
        }
      ]
    }
    

The example response includes the following fields:

  * `diskLastUseTime`: The last time when the disk was attached to a VM. If the disk was never attached to a VM this is set to the disk's creation time.
  * `isBlank`: This field is set to `true` if disk is blank and was never attached to VM. Otherwise it is `false`.



For more information about insights, see the [reference docs](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights).

## Applying idle resource recommendations

If you receive a recommendation about an idle resource and you decide that you want to apply the recommendation, then follow the instructions in the next sections.

### Deleting idle IP address

See the [`addresses.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/delete), [`gcloud compute addresses delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/delete), or the [Releasing a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) documentation.

### Deleting idle custom images

See the [`images.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/delete), [`gcloud compute images delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/delete), or the [Deleting an image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#deleting_an_image) documentation.

### Applying idle Persistent Disk recommendations

If you need to create a snapshot of a Persistent Disk prior to deleting it, then see [Creating persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

To delete an idle Persistent Disk, see the [`gcloud compute disks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete).

For information about how to recover data from a snapshot and recreate your Persistent Disk, see [Restoring snapshots](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
