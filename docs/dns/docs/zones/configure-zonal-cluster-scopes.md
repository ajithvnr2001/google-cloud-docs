---
url: https://docs.cloud.google.com/dns/docs/zones/configure-zonal-cluster-scopes/
title: Configure a zonal GKE cluster-scoped zone \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:07.783113+00:00
---

# Configure a zonal GKE cluster-scoped zone  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/configure-zonal-cluster-scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Configure a zonal GKE cluster-scoped zone Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud DNS to configure a zonal Google Kubernetes Engine (GKE) cluster-scope zone.

To configure a zonal GKE cluster-scoped DNS zone using Cloud DNS, first choose an existing private DNS zone or create a new private DNS zone to which to attach a specific GKE cluster. Next, configure the DNS zone to reference the GKE cluster's name.

For an overview of zonal Cloud DNS zones, see [Zonal Cloud DNS zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#zonal_zones). To learn more about scopes, see [Scopes and hierarchies](https://docs.cloud.google.com/dns/docs/scopes).

## Create a zonal private zone for the zonal GKE cluster

To create a new managed zonal private zone using Cloud DNS for the zonal GKE cluster, follow this step.

###  gcloud 

Run the [`gcloud dns managed-zones create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create):
    
    
    gcloud dns managed-zones create NAME \
        --description=DESCRIPTION \
        --visibility=private \
        --gkeclusters=GKE_CLUSTER \
        --location=LOCATION
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1-b/clusters/my-cluster`
  * `LOCATION`: the location of the GKE cluster, specifically the [Google Cloud zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster is located, such as `us-east1-b`



###  API 

Send a `POST` request by using the [`managedZones.create`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones
    {
    
    "name": "NAME",
    "description": "DESCRIPTION",
    "dnsName": "DNS_NAME",
    "visibility": "private"
    "privateVisibilityConfig": {
        "kind": "dns#managedZonePrivateVisibilityConfig",
        "gkeClusters": [{
                "kind": "dns#managedZonePrivateVisibilityConfigGKEClusters",
                "gkeClusterName": GKE_CLUSTER_NAME_1
            },
            {
                "kind": "dns#managedZonePrivateVisibilityConfigGKEClusters",
                "gkeClusterName": GKE_CLUSTER_NAME_2
            },
            ....
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you have created the managed zone
  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_NAME`: the DNS suffix for your zone, such as `example.private`
  * `GKE_CLUSTER_NAME_1` and `GKE_CLUSTER_NAME_2`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1-b/clusters/my-cluster`



## Authorize the zonal GKE cluster to query a Cloud DNS private zone

To authorize the zonal GKE cluster to query an existing Cloud DNS private zone, follow this step.

###  gcloud 

Run the [`gcloud dns managed-zones update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update):
    
    
    gcloud dns managed-zones update NAME \
        --gkeclusters=GKE_CLUSTER  \
        --location=LOCATION
    

Replace the following:

  * `NAME`: the name of your zone, such as `my-zone`
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1-b/clusters/my-cluster`
  * `LOCATION`: the location of the GKE cluster, specifically the [Google Cloud zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster is located, such as `us-east1-b`. The managed zone is only visible in this Google Cloud zone.



###  API 

Send a `PATCH` request by using the [`managedZones.patch`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/patch) method:
    
    
    PATCH https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones/NAME
    {
    "privateVisibilityConfig": {
        "gkeClusters": [{
                "kind": "dns#managedZonePrivateVisibilityConfigGKEClusters",
                "gkeClusterName": GKE_CLUSTER_NAME_1
            },
            {
                "kind": "dns#managedZonePrivateVisibilityConfigGKEClusters",
                "gkeClusterName": GKE_CLUSTER_NAME_2
            },
            ....
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you have created the managed zone
  * `NAME`: the name of your zone, such as `my-zone`
  * `GKE_CLUSTER_NAME_1` and `GKE_CLUSTER_NAME_2`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1-b/clusters/my-cluster`



## Configure the zonal GKE cluster to query a zonal response policy

To configure the zonal GKE cluster to query a zonal response policy, follow this step.

###  gcloud 

Run the [`gcloud dns response-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create):
    
    
    gcloud dns response-policies create NAME \
        --description=DESCRIPTION \
        --gkeclusters=GKE_CLUSTER  \
        --location=LOCATION
    

Replace the following:

  * `NAME`: a name for your response policy, such as `my-response-policy`
  * `DESCRIPTION`: a description for your response policy, such as `my-response-policy-for-gke-5`
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1-b/clusters/my-cluster`
  * `LOCATION`: the location of the GKE cluster, specifically the [Google Cloud zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the cluster is located, such as `us-east1-b`. The managed zone is only visible in this Google Cloud zone.



###  API 

Send a `POST` request by using the [`responsePolicies.create`](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/create) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/responsePolicies
    {
      "responsePolicyName": "NAME",
      "description": "DESCRIPTION",
      "gkeClusters": [
        {
          "kind": "dns#responsePolicyGKECluster",
          "gkeClusterName": "GKE_CLUSTER"
        },
      ]
    }
    

Replace the following:

  * `NAME`: a name for your response policy, such as `my-response-policy`
  * `DESCRIPTION`: a description for your response policy, such as `my-response-policy-for-gke-5`
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1-b/clusters/my-cluster`



## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To learn more about Cloud DNS response policies and rules, see [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).
  * To display an audit log of operations, see [View operations on managed zones](https://docs.cloud.google.com/dns/docs/zones/operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
