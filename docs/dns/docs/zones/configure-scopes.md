---
url: https://docs.cloud.google.com/dns/docs/zones/configure-scopes/
title: Configure a GKE cluster scope \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.493746+00:00
---

# Configure a GKE cluster scope  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/configure-scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Configure a GKE cluster scope Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud DNS to configure a Google Kubernetes Engine cluster scope. This helps you to manage custom DNS for internal services and applications within your clusters to improve service discovery and network management.

To configure a GKE cluster-scoped DNS zone using Cloud DNS, create or choose a private DNS zone in the same project as the GKE cluster that will use the DNS zone and then configure the DNS zone to reference the cluster's name.

To learn more about scopes, see [Scopes and hierarchies](https://docs.cloud.google.com/dns/docs/scopes).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.managedZones.create` to create a managed zone
  * `dns.managedZones.list` to list managed zones
  * `dns.gkeClusters.bindPrivateDNSZone` to configure a GKE cluster scope
  * `dns.managedZones.update` to update a managed zone
  * `dns.managedZones.list` to list managed zones
  * `dns.managedZones.patch` to update a managed zone



**Roles**

  * `roles/dns.admin`



## Create a private zone for the GKE cluster

To create a new managed private zone using Cloud DNS for the GKE cluster, complete the following step.

###  gcloud 

Run the [`gcloud dns managed-zones create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create):
    
    
    gcloud dns managed-zones create NAME \
        --dns-name=DNS_NAME \
        --visibility=private \
        --gkeclusters=GKE_CLUSTER
    

Replace the following:

  * `NAME`: a name for your zone
  * `DNS_NAME`: the DNS suffix for your zone, such as `example.private.`
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1a/clusters/my-cluster`



###  API 

Send a `POST` request by using the [`managedZones.create` method](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create):
    
    
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
  * `DNS_NAME`: the DNS suffix for your zone, such as `example.private.`
  * `GKE_CLUSTER_NAME_1` and `GKE_CLUSTER_NAME_2`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1a/clusters/my-cluster`



## Authorize the GKE cluster to query a Cloud DNS private zone

To authorize the GKE cluster to query an existing Cloud DNS private zone, complete the following step.

###  gcloud 

Run the [`gcloud dns managed-zones update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/managed-zones/update):
    
    
    gcloud dns managed-zones update NAME \
        --gkeclusters=GKE_CLUSTER
    

Replace the following:

  * `NAME`: the name of your zone, such as `my-zone`
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1a/clusters/my-cluster`



###  API 

Send a `PATCH` request by using the [`managedZones.patch` method](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/patch):
    
    
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
  * `GKE_CLUSTER_NAME_1` and `GKE_CLUSTER_NAME_2`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1a/clusters/my-cluster`



## Configure the GKE cluster to query a response policy

To configure the GKE cluster to query a response policy, complete the following step.

**Note:** DNS queries that reach response policies get billed at the usual Cloud DNS query billing rate. For pricing details, see [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

###  gcloud 

Run the [`gcloud dns response-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create):
    
    
    gcloud dns response-policies create NAME \
        --description=DESCRIPTION \
        --gkeclusters=GKE_CLUSTER
    

Replace the following:

  * `NAME`: a name for your response policy, such as `my-response-policy`
  * `DESCRIPTION`: a description for your response policy, such as `"my-response-policy-for-gke-5"`
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1a/clusters/my-cluster`



###  API 

Send a `POST` request by using the [`responsePolicies.create` method](https://docs.cloud.google.com/dns/docs/reference/v1/responsePolicies/create):
    
    
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
  * `GKE_CLUSTER`: the fully qualified resource path of a GKE cluster, such as `projects/my-project/locations/us-east1a/clusters/my-cluster`



## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To learn more about Cloud DNS response policies and rules, see [Manage response policies and rules](https://docs.cloud.google.com/dns/docs/zones/manage-response-policies).
  * To display an audit log of operations, see [View operations on managed zones](https://docs.cloud.google.com/dns/docs/zones/operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
