---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/cloud-run/
title: Deploy a Cloud Run service \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:18.800252+00:00
---

# Deploy a Cloud Run service  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy a Cloud Run service Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the `cloud-run` module to deploy a Cloud Run service within Cluster Toolkit blueprints. Use this module to rapidly deploy and manage scalable, containerized applications without provisioning or managing servers.

For the complete list of inputs and outputs for this module, see the [`cloud-run` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/modules/compute/cloud-run/README.md#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you have completed the following tasks:

  * Enable the [Cloud Run API (`run.googleapis.com`)](https://console.cloud.google.com/run).
  * Install the required dependencies to prepare your environment. For instructions, see [Install dependencies](https://docs.cloud.google.com/cluster-toolkit/docs/setup/install-dependencies).



### Required roles

To get the permissions that you need to deploy the Cloud Run service, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** To set the `allow_unauthenticated` variable to `true`, you must have the Project IAM Admin role. The module uses this role to modify IAM policies and grant public access to the service. For more information, see Manage your configuration.

## Deploy Cloud Run

The following example demonstrates how to configure a basic Cloud Run service. This configuration deploys a sample container image, sets an environment variable, and configures the service to allow unauthenticated, public traffic.
    
    
      - id: cloud_run
        source: modules/compute/cloud-run
        settings:
          project_id: $(vars.project_id)
          region: us-central1
          service_name: my-service
          image: us-docker.pkg.dev/cloudrun/container/hello
          container_port: 8080
          env_vars:
            KEY: "VALUE"
          allow_unauthenticated: true
    

After the deployment successfully completes, the module outputs the `service_url`. You can use this URL to directly access your running container.

## Manage your configuration

The `cloud-run` module provides several settings to help you manage your deployment:

  * **Deletion protection:** By default, the `deletion_protection` variable is set to `true`. This prevents Terraform from accidentally deleting the service. To let the service be destroyed during a [`gcluster destroy` operation](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy), you must explicitly set this variable to `false`.
  * **Ingress traffic:** You can restrict the type of network traffic that's allowed to reach your service by setting the `ingress` variable. By default, the value of this variable is set to `INGRESS_TRAFFIC_ALL`. If you're deploying internal tools or APIs, then you can restrict access by setting this value to `INGRESS_TRAFFIC_INTERNAL_ONLY` or `INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER`.
  * **Public access:** Set the `allow_unauthenticated` variable to `true` to make the service publicly accessible. If you leave this variable as `false` (the default value), then users and services must provide valid authentication credentials to invoke the endpoint.



## What's next

  * For the complete list of inputs and outputs for this module, see the [`cloud-run` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/modules/compute/cloud-run/README.md#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
