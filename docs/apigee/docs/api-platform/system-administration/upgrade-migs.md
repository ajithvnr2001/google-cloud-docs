---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/upgrade-migs/
title: Upgrade Apigee managed instance groups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:02:52.257525+00:00
---

# Upgrade Apigee managed instance groups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/upgrade-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Upgrade Apigee managed instance groups Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes how to inspect and upgrade Compute Engine managed instance groups that route northbound traffic to Apigee. 

## Overview

Some Apigee deployments route proxy traffic from a load balancer through Compute Engine MIGs that run in your project and forward requests to the Apigee runtime endpoint, including [northbound load balancing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing) and [active health checks with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-health-check-using-mig). Apigee does not manage these MIGs. As a security and reliability best practice, you must track, manage, and upgrade these MIGs and their VMs yourself to stay current with the [Compute Engine operating system lifecycle](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle). 

When an OS reaches end of life, Compute Engine removes the image family alias for new VMs. Existing VMs in the MIG continue to run and survive live host maintenance events. However, if the MIG attempts to create a new VM during autoscaling, autohealing, or a rolling replacement, VM creation fails because the source image family is no longer found. If healthy proxy VMs become unavailable, the load balancer returns `HTTP 502 Bad Gateway` errors and API traffic stops. 

**Note:** To eliminate MIG maintenance for northbound routing, see [Migrate northbound routing to Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/migrate-from-mig-to-psc). 

## Before you begin

The commands in this document are examples. Your deployment might use different network tags, machine types, disk sizes, metadata, or VM counts. Inspect your existing configuration first and adjust the command flags to match your environment. 

Replace the following placeholders in the example commands with values from your environment: 

  * `PROJECT_ID`: the Google Cloud project ID where your MIGs and instance templates are deployed. 
  * `REGION`: the Compute Engine region of your MIG. 
  * `EXISTING_MIG_NAME`: the name of your existing MIG. 
  * `OLD_TEMPLATE_NAME`: the name of the instance template attached to `EXISTING_MIG_NAME`. 
  * `NEW_TEMPLATE_NAME`: the name of the new instance template that you create. 
  * `VPC_NAME`: the name of the VPC network used by your MIG. 
  * `VPC_SUBNET`: the name of the VPC subnet in `REGION` used by your MIG. 
  * `IMAGE_FAMILY`: a supported OS image family from the [Compute Engine operating system details](https://docs.cloud.google.com/compute/docs/images/os-details). 
  * `IMAGE_PROJECT`: the image project that contains `IMAGE_FAMILY`. 
  * `APIGEE_ENDPOINT`: the target IP address configured in the `ENDPOINT` metadata of your existing instance template. 
  * `STARTUP_SCRIPT_URL`: the Cloud Storage URL configured in the `startup-script-url` metadata of your existing instance template. 

**Note:** If you manage MIGs using Terraform or other Infrastructure as Code automation, update the image in your configuration files to prevent subsequent deployments from overwriting manual updates with legacy templates. 

## Inspect your MIGs and instance templates

Apigee routing MIGs typically use the `apigee-mig-proxy` tag and `ENDPOINT` metadata. Complete the following steps to inspect your MIGs and instance templates: 

  1. List the MIGs in your project and identify the attached instance templates: 
         
         gcloud compute instance-groups managed list --project=PROJECT_ID \
           --format="table(name,region.basename(),zone.basename(),instanceTemplate.basename())"
         

  2. Check the source OS image of your existing instance template. Add `--region=REGION` if the template is regional: 
         
         gcloud compute instance-templates describe OLD_TEMPLATE_NAME \
           --project=PROJECT_ID \
           --format="value(properties.disks[0].initializeParams.sourceImage)"
         

  3. Inspect the machine type, disk configuration, network, subnet, tags, and metadata of `OLD_TEMPLATE_NAME` so that you can match these settings when creating the new template. Add `--region=REGION` if the template is regional: 
         
         gcloud compute instance-templates describe OLD_TEMPLATE_NAME \
           --project=PROJECT_ID \
           --format="yaml(properties.machineType,properties.disks,properties.networkInterfaces,properties.tags,properties.metadata)"
         




## Create a new instance template and execute a rolling update

Create a new instance template with a supported OS image family and start a rolling update on the MIG. Using `--max-surge` with `--max-unavailable=0` provisions and verifies new VMs before draining and removing old instances, which prevents traffic disruption even if new VMs fail to start due to a resource stockout or configuration error. 

  1. Create a new instance template. The following command is an example; adjust the network, subnet, tags, machine type, disk size, and metadata to match your existing template configuration: 
         
         gcloud compute instance-templates create NEW_TEMPLATE_NAME \
           --project=PROJECT_ID \
           --region=REGION \
           --network=VPC_NAME \
           --subnet=VPC_SUBNET \
           --tags=https-server,apigee-mig-proxy,gke-apigee-proxy \
           --machine-type=e2-medium \
           --image-family=IMAGE_FAMILY \
           --image-project=IMAGE_PROJECT \
           --boot-disk-size=20GB \
           --no-address \
           --metadata=ENDPOINT=APIGEE_ENDPOINT,startup-script-url=STARTUP_SCRIPT_URL
         

This command creates a global instance template at `projects/PROJECT_ID/global/instanceTemplates/NEW_TEMPLATE_NAME`. If you prefer to create a regional instance template, add `--instance-template-region=REGION` and use `projects/PROJECT_ID/regions/REGION/instanceTemplates/NEW_TEMPLATE_NAME` in the next step. 

  2. Start a rolling update on the MIG. Adjust `--max-surge` if needed based on the size and quota of your MIG: 
         
         gcloud compute instance-groups managed rolling-action start-update EXISTING_MIG_NAME \
           --project=PROJECT_ID \
           --region=REGION \
           --version=template=projects/PROJECT_ID/global/instanceTemplates/NEW_TEMPLATE_NAME \
           --max-surge=3 \
           --max-unavailable=0
         

  3. Verify that all VMs in the MIG run `NEW_TEMPLATE_NAME` and report a `RUNNING` status: 
         
         gcloud compute instance-groups managed list-instances EXISTING_MIG_NAME \
           --project=PROJECT_ID \
           --region=REGION
         




## What's next

  * [Migrate northbound routing to Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/migrate-from-mig-to-psc)
  * [Configure active health check for regional failover with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-health-check-using-mig)
  * [Roll out updates to MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)
  * [Compute Engine operating systems lifecycle](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle)
  * [Compute Engine operating system details](https://docs.cloud.google.com/compute/docs/images/os-details)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
