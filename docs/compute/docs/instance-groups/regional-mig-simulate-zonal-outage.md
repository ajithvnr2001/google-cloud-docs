---
url: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage/
title: Simulate a zone outage for a regional MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:41.931404+00:00
---

# Simulate a zone outage for a regional MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Simulate a zone outage for a regional MIG Stay organized with collections  Save and categorize content based on your preferences. 

To test that your [regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) is overprovisioned enough and can survive a zone outage, you can use the following example to simulate a zonal failure.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
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




## Use a script to simulate a zone outage

This script stops and starts Apache as the default scenario. If this doesn't apply to your application, replace the commands that stop and start Apache with your own failure and recovery scenario.

  1. Deploy and run this script continuously in every VM in the group. You can do this by adding the script to the instance template or by including the script in a [custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) and using the image in the instance template.
         
         #!/usr/bin/env bash
         
         # Copyright 2016 Google Inc. All Rights Reserved.
         #
         # Licensed under the Apache License, Version 2.0 (the "License");
         # you may not use this file except in compliance with the License.
         # You may obtain a copy of the License at
         #
         #     http://www.apache.org/licenses/LICENSE-2.0
         #
         # Unless required by applicable law or agreed to in writing, software
         # distributed under the License is distributed on an "AS IS" BASIS,
         # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         # See the License for the specific language governing permissions and
         # limitations under the License.
         
         set -o nounset
         set -o errexit
         set -o pipefail
         
         function GetMetadata() {
           curl -s "$1" -H "Metadata-Flavor: Google"
         }
         
         PROJECT_METADATA_URL="http://metadata.google.internal/computeMetadata/v1/project/attributes"
         INSTANCE_METADATA_URL="http://metadata.google.internal/computeMetadata/v1/instance"
         ZONE=$(GetMetadata "$INSTANCE_METADATA_URL/zone" | cut -d '/' -f 4)
         INSTANCE_NAME=$(hostname)
         
         # We keep track of the state to make sure failure and recovery is triggered only once.
         STATE="healthy"
         while true; do
           if [[ "$ZONE" = "$(GetMetadata $PROJECT_METADATA_URL/failed_zone)" ]] && \
              [[ "$INSTANCE_NAME" = *"$(GetMetadata $PROJECT_METADATA_URL/failed_instance_names)"* ]]; then
             if [[ "$STATE" = "healthy" ]]; then
               STATE="failure"
               # Do something to simulate failure here.
               echo "STARTING A FAILURE"
               /etc/init.d/apache2 stop
             fi
           else
             if [[ "$STATE" = "failure" ]] ; then
               STATE="healthy"
               # Do something to recover here.
               echo "RECOVERING FROM FAILURE"
               /etc/init.d/apache2 start
             fi
           fi
           sleep 5
         done
         
         

  2. Simulate a zone failure by setting these two project metadata fields:

     * `failed_zone`: Sets the zone where you want to simulate the outage (limit the failure to just one zone).
     * `failed_instance_names`: Choose the VMs to take offline by name (to limit the failure to only VM names containing this string).

You can set this metadata using the gcloud CLI. For example, the following command sets the zone outage to the `europe-west1-b` zone and affects VMs that have names starting with `base-instance-name`:
    
    gcloud compute project-info add-metadata --metadata failed_zone='europe-west1-b',failed_instance_names='base-instance-name-'

  3. After you are done simulating the outage, recover from the failure by removing the metadata keys:
         
         gcloud compute project-info remove-metadata --keys failed_zone,failed_instance_names




Here are some ideas for failure scenarios you can run using this script:

  * Stop your application completely to see how the MIG responds.
  * Make your VMs return as "unhealthy" on load balancing health checks.
  * Modify iptables to block some of the traffic to and from the VM.
  * Shutdown the VMs. By default, it will be recreated by the regional MIG shortly after but the new incarnation will immediately shutdown itself as soon as the script runs and as long as the metadata values are set. This will result in a crash loop.



## What's next

  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution) to observe how capacity shifts across zones during and after a simulated outage.
  * Learn how to build [scalable and resilient web applications](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps).
  * Learn about [disaster recovery on Google Cloud Platform](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
