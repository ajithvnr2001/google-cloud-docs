---
url: https://docs.cloud.google.com/mainframe-connector/docs/deploy-mainframe-connector/
title: Deploy Mainframe Connector on Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:43.446506+00:00
---

# Deploy Mainframe Connector on Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/deploy-mainframe-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Deploy Mainframe Connector on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses how you can deploy Mainframe Connector on Cloud Run as a remote service using [Terraform](https://www.terraform.io/). You can then use the Mainframe Connector remote service to transcode, store, and export mainframe data on Google Cloud. You can trigger this service from your mainframe to [perform remote transcoding](https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding), or as a [standalone instance that is integrated with an existing extract, transfer, and load (ETL) workflow](https://docs.cloud.google.com/mainframe-connector/docs/standalone-mode).

You can also deploy multiple instances of the Mainframe Connector remote service. For more information, see Deploy multiple instances of the Mainframe Connector.

To deploy Mainframe Connector on Cloud Run using [Terraform](https://www.terraform.io/), use the following steps:

  1. Download the [Mainframe Connector deployment tar file](https://docs.cloud.google.com/mainframe-connector/docs/deploy-mainframe-connector/).

### Important

Be aware that Mainframe Connector uses Google Analytics to collect usage data. This helps us improve the software and provide a better user experience. By default, Google Analytics is enabled. However, you can opt out by configuring an [environment variable](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#disable_analytics) when running Mainframe Connector.   
  
The use of Google Analytics is subject to the Google Analytics [Terms of Service and Privacy Policy](https://www.google.com/analytics/terms). By downloading Mainframe Connector, you acknowledge that you have read, understood, and accepted the terms and conditions.

[Download](https://storage.googleapis.com/mainframe-connector-release/latest/deployment.tar) Cancel

  2. Extract the files in the deployment tar file.
         
         tar -xvf ./deployment.tar
         

The `main.tf` and `vars.tf` files are extracted from deployment tar file.

  3. Review and edit the variables in the `vars.tf` file. Most of the variables already have default values. The only mandatory variables you need to set are `project` and `connector_service_account_email`.

     * **`project`:** The Google Cloud project in which you want to install Mainframe Connector.
     * **`connector_service_account_email`:** The service account that has all the permissions for the operations you want to perform using Mainframe Connector.

You can also set the network configuration using the `connector_service_ingress` and `connector_service_vpc_access` variables.

  4. Run the [`terraform init`](https://developer.hashicorp.com/terraform/cli/commands/init) command with a Cloud Storage _bucket_ and _prefix_ as arguments. Using a Cloud Storage bucket and prefix helps you save the deployment state in the bucket. You can also reuse the same bucket and prefix when you upgrade Mainframe Connector.
         
         terraform init \
         -backend-config bucket=DEPLOYMENT_STATE_BUCKET \
         -backend-config prefix=BUCKET_PREFIX
         

Replace the following:

     * DEPLOYMENT_STATE_BUCKET: The name of the Cloud Storage bucket.
     * BUCKET_PREFIX: The prefix that you want to use in the Cloud Storage bucket.
  5. Create a `.tfvars` file to define variables that you want Terraform to use during the Mainframe Connector deployment.

  6. Open the `.tfvars` file and define the following variables as key-value pairs.

     * **`instance_id`:** Define an `instance_id` to separate different workloads when you want to have multiple instances of Mainframe Connector, or to use different service accounts.
     * **`project`:** The project in which you want to deploy Mainframe Connector.
     * **`connector_service_ingress`:** The ingress type.
     * **`additional_labels`:** Additional labels if you want to test the deployment.
     * **`connector_service_account_email`:** The service account email ID of Mainframe Connector.

Save your changes and close the file.

  7. Deploy Mainframe Connector.
         
         terraform apply -var-file=VARIABLE_FILE_NAME
         

Replace VARIABLE_FILE_NAME with the variables file you created in the previous step.

  8. (Optional) To check if Mainframe Connector is deployed and running, go to the Cloud Run page, and select the **Services** tab. You should see your deployment listed in the table.

[Go to Cloud Run](https://console.cloud.google.com/run?enableapi=true)




## Deploy multiple instances of the Mainframe Connector

To limit access for specific jobs, you might need to deploy multiple instances of the Mainframe Connector. You can do this by deploying the Mainframe Connector multiple times with different variables and service accounts. Since the Mainframe Connector remote service is based on Cloud Run, you will only be billed when each service is actually running. You also don't need to set up high availability (HA) as each instance is already load balanced and highly available.

## What's next

  * [Transcode mainframe data remotely on Google Cloud](https://docs.cloud.google.com/mainframe-connector/docs/remote-transcoding)
  * [Transcode mainframe data moved to Google Cloud using a virtual tape library](https://docs.cloud.google.com/mainframe-connector/docs/vtl-transcoding)
  * [Run Mainframe Connector as a standalone job](https://docs.cloud.google.com/mainframe-connector/docs/standalone-mode)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
