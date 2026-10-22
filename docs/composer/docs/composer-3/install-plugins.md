---
url: https://docs.cloud.google.com/composer/docs/composer-3/install-plugins/
title: Install custom plugins \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:25.875162+00:00
---

# Install custom plugins  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/install-plugins/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Install custom plugins Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/install-plugins "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/install-plugins "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to install custom plugins in your Managed Service for Apache Airflow environment.

Apache Airflow's plugin manager allows you to write custom in-house Apache Airflow operators, hooks, sensors, or interfaces. For more information, see [custom plugins](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html) in the Airflow documentation.

## About custom plugins

When you create an environment, Managed Airflow [creates a Cloud Storage bucket](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage) and associates this bucket with your environment. You use the `plugins` folder in your environment's bucket to install custom plugins.

## Before you begin

  * Your account [must have a role](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account) that allows viewing and modifying your environment's bucket contents.
  * This installation method applies only to [Airflow plugins](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html). For example, you cannot use this method to install common Python modules or other libraries.
  * Plugins must conform to the [Airflow plugins template](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html#example) guidelines.

  * Managed Airflow (Gen 3) doesn't support custom plugins for the Airflow scheduler and the Airflow triggerer. Plugins aren't synchronized to these components of your environment. This includes features of Airflow that rely on plugins, such as [custom TimeTables](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html) and DAG-level [listeners](https://airflow.apache.org/docs/apache-airflow/2.10.5/administration-and-deployment/listeners.html). Task-level listeners and built-in TimeTables are supported.




## Install a plugin

To install a custom plugin into your Managed Airflow environment, copy the plugin code to the `plugins` folder in your environment's bucket.

**Note:** After the plugins are loaded, they are never reloaded, except the UI plugins in the web server. You might need to restart the web server or the scheduler processes manually. Otherwise, a scheduler only restarts after the [`[scheduler]num_runs`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#num-runs), which is set to 5000 by default.

To install a plugin:

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Find your environment and follow the **DAGs** link.

  3. Go one folder level up, then navigate to the `plugins/` folder.

  4. Upload your plugin files. For more information about uploading objects, see [Uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).




###  gcloud 

Use the following `gcloud` command:
    
    
    gcloud composer environments storage plugins import \
        --environment ENVIRONMENT_NAME \
        --location LOCATION \
        --source PATH_TO_LOCAL_FILE \
        --destination PATH_IN_SUBFOLDER
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `PATH_TO_LOCAL_FILE` with the path of the file to upload.
  * (Optional) `PATH_IN_SUBFOLDER` with the subfolder path. Use the `--destination` argument to upload a plugin to a subfolder in the `plugins` folder. Otherwise, omit the `--destination` argument.



## View the list of plugins

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Find your environment and follow the **DAGs** link.

  3. Go one folder level up, then navigate to the `plugins/` folder.

  4. View the plugin files.




###  gcloud 

Use the following `gcloud` command:
    
    
    gcloud composer environments storage plugins list \
        --environment ENVIRONMENT_NAME \
        --location LOCATION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



## Delete a plugin

To delete a plugin from your Managed Airflow environment, delete the plugin code from the `plugins` folder in the environment's bucket.

**Note:** You can disable web server plugins without deleting them.

To delete a plugin:

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Find your environment and follow the **DAGs** link.

  3. Go one folder level up, then navigate to the `plugins/` folder.

  4. Delete the plugin files. For more information about deleting objects, see [Deleting objects](https://docs.cloud.google.com/storage/docs/deleting-objects).




###  gcloud 

Use the following `gcloud` command:
    
    
    gcloud composer environments storage plugins delete \
        --environment ENVIRONMENT_NAME \
        --location LOCATION \
        PLUGIN_TO_DELETE
    

## Download plugins

To download plugins, choose an option:

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Find your environment and follow the **DAGs** link.

  3. Go one folder level up, then navigate to the `plugins/` folder.

  4. Download the plugin files. For more information about deleting objects, see [Downloading objects](https://docs.cloud.google.com/storage/docs/downloading-objects).




###  gcloud 

Use the following `gcloud` command:
    
    
    gcloud composer environments storage plugins export \
      --environment ENVIRONMENT_NAME \
      --location LOCATION \
      --destination PATH_TO_LOCAL_DESTINATION \
      --source PATH_IN_FOLDER
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `PATH_TO_LOCAL_DESTINATION` with the destination for downloaded file.
  * (Optional) `--source` is an option to download only one plugin. `PATH_IN_FOLDER` is the folder path.



## Disable web server plugins

In Managed Airflow (Gen 3), if you experience problems with Airflow UI, you can disable web server plugins without having to remove them from the environment's bucket.

**Note:** You can also disable web server plugins when you [create an environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments).

###  gcloud 

The following Google Cloud CLI arguments disable and enable web server plugins:

  * `--no-support-web-server-plugins`: disable web server plugins
  * `--support-web-server-plugins`: enable web server plugins



To disable web server plugins, run the following Google Cloud CLI command:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --no-support-web-server-plugins
    

To enable web server plugins, run the following Google Cloud CLI command:
    
    
    gcloud beta composer environments update ENVIRONMENT_NAME \
      --location LOCATION \
      --support-web-server-plugins
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of the environment
  * `LOCATION`: the region where the environment is located



###  API 

  1. Create an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1beta1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.software_config.web_server_plugins_mode` mask.

     2. In the request body, in the `web_server_plugins_mode` field:

        * Specify `PLUGINS_DISABLED` to disable web server plugins.
        * Specify `PLUGINS_ENABLED` to enable web server plugins.



Example (disable plugins):
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.software_config.web_server_plugins_mode
    
    "config": {
      "softwareConfig": {
        "web_server_plugins_mode": "PLUGINS_DISABLED"
       }
    }
    

Example (enable plugins):
    
    
    // PATCH https://composer.googleapis.com/v1beta1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.software_config.web_server_plugins_mode
    
    "config": {
      "softwareConfig": {
        "web_server_plugins_mode": "PLUGINS_ENABLED"
       }
    }
    

## Troubleshoot plugin issues

### Plugins cause problems with Airflow UI

You can disable web server plugins without deleting them. For more information, see Disable web server plugins.

### A newly-uploaded plugin is not visible in Airflow UI

If you use [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac) then the newly uploaded plugin might not be visible in Airflow UI. To address this issue, ask Airflow UI Administrator to configure access to the newly uploaded plugin or assign yourself the `Admin` role in Airflow UI.

## What's next

  * [Data stored in Cloud Storage](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage)
  * [Manage DAGs](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
