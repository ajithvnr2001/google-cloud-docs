---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instance-recreate/
title: Recreating an Apigee instance with zero downtime \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:40.089421+00:00
---

# Recreating an Apigee instance with zero downtime  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instance-recreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Recreating an Apigee instance with zero downtime Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Important:** This topic only applies to organizations that were created with VPC peering enabled. See also [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

This document explains how to recreate an Apigee [instance](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts#instance) without incurring API management downtime or data loss. 

## Introduction

Apigee instances created before January 25, 2022, do not have sufficient internet protocol (IP) address space to allow Apigee workloads to scale to handle increasing API traffic and/or to allow you to add more than 10 environments to an instance. 

On January 24, 2022, Apigee [introduced an enhancement](https://docs.cloud.google.com/apigee/docs/release-notes#January_24_2022) to address this problem. The enhancement reduces the IP range required to peer your VPC network with Apigee and uses [privately used public IPs](https://cloud.google.com/architecture/configuring-privately-used-public-ips-for-GKE) (PUPI) to allow workloads to scale to higher limits. 

## What you need to do

If you have an Apigee instance that was created before January 25, 2022, Apigee recommends that you replace it with a new instance, as explained in this document. If you do not recreate the older instance, you may experience scaling issues and the number of environments you can add to an instance will continue to be limited to 10. Also, your instance may stop getting regular updates which will impact the API services. 

## Determining an instance's creation date

To determine the creation date of an Apigee instance: 

  1. List details for all of the Apigee instances in your organization: 
         
         **AUTH** ="Authorization: Bearer $(gcloud auth print-access-token)"
         
         curl -i -X GET -H "**$AUTH** " \
         "https://apigee.googleapis.com/v1/organizations/PROJECT_ID/instances"

Where:

     * `AUTH` is the Authentication header with a bearer token. Be sure the default project for `gcloud` is set to the `PROJECT_ID`.
     * `PROJECT_ID` is the Cloud project ID that you created when you provisioned Apigee.

Sample output: 
    
    {
      "instances": [
        {
          "name": "us-west1",
          "location": "us-west1",
          "host": "10.117.200.2",
          "port": "443",
          **"createdAt" : "1642698826000"**,
          "lastModifiedAt": "1655745226000",
          "diskEncryptionKeyName": "projects/myproject/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-key",
          "state": "ACTIVE",
          "peeringCidrRange": "SLASH_22",
          "runtimeVersion": "1-8-0-apigee-33",
          "ipRange": "10.117.200.0/22,10.81.174.192/28",
          "consumerAcceptList": [
            "myproject"
          ],
          "serviceAttachment": "projects/z11f28c6f3104980e-tp/regions/us-west1/serviceAttachments/apigee-us-west1-lbko"
        }
      ]
    }

  2. For each instance, check the value of the `createdAt` field by decoding the Unix timestamp to get the date. 
     * If an instance was created on or after January 25, 2022, then you do not have to do anything further for that instance. 
     * If an instance was created before January 25, 2022, we recommend you replace the instance, as discussed in this document.



## About the recreation procedure

To recreate an instance with zero downtime and no data loss, you need to first create a new instance in a new (expanded) region and direct API traffic to that new instance. Then, you can drain down the existing instance, delete it, and recreate it in the same region as the one you deleted. 

Apigee has provided a set of scripts that perform all of the required steps to recreate and configure an instance. We provide a link to the scripts later in this document. 

## Prerequisites

Before you begin the instance recreation steps: 

  * You must be familiar with how the Apigee instance was created in the first place. The steps for recreating the instance depend on you knowing details about how the original instance was configured. 
  * You must be entitled to provision Apigee in at least two regions. If you aren't sure if you have sufficient entitlement, follow the steps to create an instance in a new region. If you do not have the proper entitlement the attempt will fail with a limit error. In that case, contact Apigee support to get a temporary exception to increase your region limit. If you are already entitled for two or more regions, we recommend you reach out to get the temporary exception to avoid running your production workload with a reduced instance during the recreation process. The process of recreating an instance includes deleting the old instance. If you do not follow the step to create a new instance in an expanded region, you will incur downtime and runtime data loss, including KVMs, cache data, quota data, and KMS data. Therefore, region expansion is mandatory to recreate an instance without downtime or data loss.
  * You must have room in your project for additional IP ranges of **/22** and **/28** blocks to create the new instance. See also [Network sizing](https://cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges#sizing). You can release these ranges when the additional region is deleted after instance recreation is complete. Note that the **/22** block is configurable by you. You can choose which **/28** block Apigee will use, or if you don't choose, it is auto-assigned by Apigee from any available block. 



## Recreating the instance

Apigee has provided a set of scripts that perform all of the required steps to recreate an instance. 

  1. Be sure you have met the prerequisites.
  2. [Download the scripts](https://github.com/apigee/apigee-x-pupi-migration) from GitHub.
  3. Follow the steps in the Git repository's [README](https://github.com/apigee/apigee-x-pupi-migration#readme) file to create the new instance.
  4. Reconfigure the northbound and southbound connections to point to the new Apigee instance. See About northbound changes and About southbound changes.



### About northbound changes

Northbound refers to API traffic from external or internal clients to Apigee through a load balancer. When an instance is deleted and recreated, the northbound IP address and [ Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc) service attachment ID of the instance will change for the new instance. 

The provided scripts reconfigure the load balancer's backend for you. If the instance's [network routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing) was configured with a managed instance group (MIG), a provided script recreates the MIG that proxies traffic to the Apigee endpoint, and attaches the MIG as a backend to the existing backend service. If routing was configured with Private Service Connect, a script recreates the network endpoint group (NEG) to Apigee's service endpoint attachment and attaches the new NEG as a backend to the existing backend service. 

Note that you will not have to change the hostname records in any [environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) associated with the old instance.

### Southbound changes

Southbound refers to API traffic from Apigee to your API proxy target services. 

**Note:** Southbound changes are only needed if you used NAT IPs for Apigee instances, as described in [Provisioning NAT IPs](https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-provisioning).

When an instance is deleted and recreated, any dedicated southbound NAT IP addresses will be released. So, you must reserve and activate new IP addresses for your NAT and reconfigure your firewalls/allowlisting on your target endpoints. One of the provided scripts handles this NAT reconfiguration for you, if needed. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
