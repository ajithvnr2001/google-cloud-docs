---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision/
title: gcloud alpha apigee organizations provision \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:51.760521+00:00
---

# gcloud alpha apigee organizations provision  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/organizations/provision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apigee organizations provision Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apigee organizations provision - provision an Apigee SaaS organization 
SYNOPSIS
    

`gcloud alpha apigee organizations provision` `--authorized-network`=`AUTHORIZED_NETWORK` [`--analytics-region`=`ANALYTICS_REGION`] [`--async`] [`--runtime-location`=`RUNTIME_LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Provision an Apigee SaaS organization. 

`gcloud alpha apigee organizations provision` creates an Apigee organization and populates it with the necessary child resources to be immediately useable. 

This is a long running operation and could take anywhere from 10 minutes to 1 hour to complete. 

At the moment, only trial organizations are supported. 

EXAMPLES
     To provision an organization for the active Cloud Platform project, attached to a network named ``default`` run: 
    
    
    gcloud alpha apigee organizations provision --authorized-network=default

To provision an organization asynchronously and print only the name of the launched operation, run: 
    
    
    gcloud alpha apigee organizations provision --authorized-network=default --async --format="value(name)"

To provision an organization for the project named ``my-proj``, with analytics and runtimes located in ``us-central1``, run: 
    
    
    gcloud alpha apigee organizations provision --authorized-network=default --project=my-proj --analytics-region=us-central1 --runtime-location=us-central1-a

REQUIRED FLAGS
    

`--authorized-network`=`AUTHORIZED_NETWORK`
     Name of the network to which the provisioned organization should be attached. This must be a VPC network peered through Service Networking. To get a list of existing networks, run: 
    
    
    [gcloud compute networks list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list)

To check whether a network is peered through Service Networking, run: 
    
    
    [gcloud services vpc-peerings list](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list) --network=NETWORK_NAME --service=servicenetworking.googleapis.com

To create a new network suitable for Apigee provisioning, choose a name for the network and address range, and run: 
    
    
    [gcloud compute networks create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) NETWORK_NAME --bgp-routing-mode=global --description='network for an Apigee trial'
    [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) ADDRESS_RANGE_NAME --global --prefix-length=16 --description="peering range for an Apigee trial" --network=NETWORK_NAME --purpose=vpc_peering
    [gcloud services vpc-peerings connect](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect) --service=servicenetworking.googleapis.com --network=NETWORK_NAME --ranges=ADDRESS_RANGE_NAME

OPTIONAL FLAGS
    

`--analytics-region`=`ANALYTICS_REGION`
     Primary Cloud Platform region for analytics data storage. For valid values, see: <https://docs.apigee.com/hybrid/latest/precog-provision>. 

If unspecified, the default is ``us-west1``

`--async`
     If set, returns immediately and outputs a description of the long running operation that was launched. Else, `gcloud alpha apigee organizations provision` will block until the organization has been provisioned. 

To monitor the operation once it's been launched, run `gcloud alpha apigee operations describe OPERATION_NAME`. 

`--runtime-location`=`RUNTIME_LOCATION`
     Cloud Platform location for the runtime instance. For trial organizations, this is a compute zone. To get a list of valid zones, run `[gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)`. If unspecified, the default is ``us-west1-a``. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
