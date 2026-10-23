---
url: https://docs.cloud.google.com/workstations/docs/startup-scripts/
title: Run custom startup scripts on the host VM \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:44.853730+00:00
---

# Run custom startup scripts on the host VM  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/startup-scripts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Run custom startup scripts on the host VM Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Workstations lets you run custom startup scripts on the host workstation VM before your workstation container starts. This is useful for performing VM-level configuration or installing additional software that needs to run outside the workstation container. 

Running custom startup scripts on the host VM is an advanced feature. Instead of using startup scripts, we recommend that you [customize your container image](https://docs.cloud.google.com/workstations/docs/customize-container-images).

If you choose to use startup scripts, ensure that your script remains compatible with Container-Optimized OS (COS) image changes because the host VM receives regular operating system updates based on COS.

## Before you begin

Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

## Prepare your startup script

Create the startup script that you want to run on the host workstation VM. When writing your script, adhere to the following guidelines:

  1. Cloud Workstations runs your specified workstation container as well as several system containers on the host workstation VM to ensure your workstation functions properly. All containers run using the `containerd` runtime and the `crictl` client.
  2. Run any additional containers launched by your startup script using `containerd`. Docker is disabled on the host VM to prevent interference with the Docker daemon running inside your workstation container.
  3. Host-level containers launched by your startup script can't interact with the main workstation container. These direct interactions are unsupported because they bypass Identity and Access Management (IAM) checks.



## Store your startup script in Cloud Storage

Upload your script to a Cloud Storage bucket and ensure the script is accessible by the service account associated with your workstation.

  1. Upload your script to a bucket:
         
         gcloud storage cp LOCAL_SCRIPT_PATH gs://BUCKET_NAME/SCRIPT_NAME
         

Replace the following:

     * `LOCAL_SCRIPT_PATH`: the local path to your startup script file.
     * `BUCKET_NAME`: the name of your Cloud Storage bucket.
     * `SCRIPT_NAME`: the name you want to give the script file in the bucket.
  2. Ensure the service account used by your workstation configuration has [permissions to access the bucket and script file](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions). Alternatively, the script can be publicly accessible.




## Create a workstation configuration

To use a custom startup script, create a workstation configuration and specify the Cloud Storage URI of your script.

###  Console 

To configure a custom startup script when you create a workstation configuration:

  1. In the Google Cloud console, go to the **Workstation configurations** page.

[Go to Workstation configurations](https://console.cloud.google.com/workstations/configurations)

  2. Click add **Create**.

  3. On the **Basic information** page, enter a name for the configuration, select a workstation cluster, and click **Continue**.

  4. On the **Machine settings** page, configure your machine settings, and click **Continue**.

  5. On the **Environment settings** page, expand the **Advanced container options** section.

  6. In the **Custom startup script** field, enter the Cloud Storage path to your startup script (for example, `gs://BUCKET_NAME/SCRIPT_NAME`).

  7. Complete the remaining steps, and click **Create**.




###  REST 

To configure a custom startup script using the REST API, create the workstation configuration and set the `startupScriptUri` field in a `host.gceInstance` message to the Cloud Storage URI of your script:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
           "host": {
             "gceInstance": {
               "poolSize": 1,
               "startupScriptUri": "gs://BUCKET_NAME/SCRIPT_NAME",
               "serviceAccount": "SERVICE_ACCOUNT"
             }
           }
         }' \
         https://workstations.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/workstationClusters/CLUSTER_ID/workstationConfigs?workstation_config_id=CONFIG_ID
    

Replace the following:

  * `SERVICE_ACCOUNT`: the email address of the service account associated with the workstation configuration.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the region where your workstation cluster is located.
  * `CLUSTER_ID`: the ID of your workstation cluster.
  * `CONFIG_ID`: the ID you want to assign to the new workstation configuration.



## Verify script execution

To verify that your script ran correctly, use one of the following methods:

  * **Serial port 3 output logs** : output logs generated by your script are automatically sent to [serial port 3 output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output). To find the name of the VM assigned to your workstation, see the [platform logs](https://docs.cloud.google.com/workstations/docs/platform-logging).
  * **SSH into your VM** : you can [SSH into your workstation VM](https://docs.cloud.google.com/workstations/docs/ssh-support) to further debug your script if needed.
  * **Readiness checks** : startup scripts are best-effort and don't block your workstation from starting. If your script takes a long time to run or fails, the workstation might still be marked as ready. To ensure the workstation is not marked ready until your script completes, consider implementing [readiness checks](https://docs.cloud.google.com/workstations/docs/create-configuration#customize_environment).



## What's next

  * Learn more about [platform logging](https://docs.cloud.google.com/workstations/docs/platform-logging).
  * [Customize your development environment](https://docs.cloud.google.com/workstations/docs/customize-development-environment).
  * [Troubleshoot](https://docs.cloud.google.com/workstations/docs/troubleshoot) workstation issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
