---
url: https://docs.cloud.google.com/composer/docs/composer-3/manage-dags/
title: Add and update DAGs \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:13.802854+00:00
---

# Add and update DAGs  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/manage-dags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Add and update DAGs Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to manage DAGs in your Managed Airflow environment.

Managed Airflow uses a [Cloud Storage](https://docs.cloud.google.com/storage) bucket to store DAGs of your Managed Airflow environment. Your environment synchronizes DAGs from this bucket to [Airflow components](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture) such as Airflow workers and schedulers.

## Before you begin

  * Because Apache Airflow does not provide strong DAG isolation, we recommend that you maintain separate production and test environments to prevent DAG interference. For more information, see [Testing DAGs](https://docs.cloud.google.com/composer/docs/composer-3/test-dags).
  * Make sure that your account [has enough permissions](https://docs.cloud.google.com/composer/docs/composer-3/access-control) to manage DAGs.
  * Changes to DAG propagate to Airflow within 3-5 minutes. You can see task status in the [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).



## Access the bucket of your environment

To access the bucket associated with your environment:

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, find a row with the name of your environment and in the **DAGs folder** column click the **DAGs** link. The **Bucket details** page opens. It shows contents of the `/dags` folder in your environment's bucket.




###  gcloud 

gcloud CLI has separate commands to add and delete DAGs in your environment's bucket.

If you want to interact with your environment's bucket, you can also use the [Google Cloud CLI](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud). To get the address of your environment's bucket run the following gcloud CLI command:
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
        --location LOCATION \
        --format="get(config.dagGcsPrefix)"
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud beta composer environments describe example-environment \
        --location us-central1 \
        --format="get(config.dagGcsPrefix)"
    

###  API 

Construct an [`environments.get`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/get) API request. In the [Environment](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#Environment) resource, in the [EnvironmentConfig](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments#EnvironmentConfig) resource, in the `dagGcsPrefix` resource is the address of your environment's bucket.

Example:
    
    
    GET https://composer.googleapis.com/v1/projects/example-project/
    locations/us-central1/environments/example-environment
    

###  Python 

Use the [google-auth](https://googleapis.dev/python/google-auth/latest/) library to get credentials and use the [requests](https://requests.readthedocs.io/en/latest/) library to call the REST API. 
    
    
    import google.auth
    import google.auth.transport.requests
    
    # Authenticate with Google Cloud.
    # See: https://cloud.google.com/docs/authentication/getting-started
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'us-central1'
    # composer_environment = 'YOUR_COMPOSER_ENVIRONMENT_NAME'
    
    environment_url = (
        "https://composer.googleapis.com/v1beta1/projects/{}/locations/{}"
        "/environments/{}"
    ).format(project_id, location, composer_environment)
    response = authed_session.request("GET", environment_url)
    environment_data = response.json()
    
    # Print the bucket name from the response body.
    print(environment_data["config"]["dagGcsPrefix"])

## Add or update a DAG

To add or update a DAG, move the Python `.py` file for the DAG to the `/dags` folder in the environment's bucket.

**Important:** Managed Airflow automatically synchronizes the environment's bucket contents to Airflow components of your environment. The synchronization and the following re-parsing of DAGs happen **with a delay of approximately 1-2 minutes**. This delay depends on the number of files in the `/dags` folder and on the amount of resources available to Airflow components of your environment.

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, find a row with the name of your environment and in the **DAGs folder** column click the **DAGs** link. The **Bucket details** page opens. It shows contents of the `/dags` folder in your environment's bucket.

  3. Click **Upload files**. Then select the Python `.py` file for the DAG using the browser's dialog and confirm.




###  gcloud 
    
    
    gcloud composer environments storage dags import \
        --environment ENVIRONMENT_NAME \
        --location LOCATION \
        --source="LOCAL_FILE_TO_UPLOAD"
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `LOCAL_FILE_TO_UPLOAD` is the Python `.py` file for the DAG.



Example:
    
    
    gcloud composer environments storage dags import \
        --environment example-environment \
        --location us-central1 \
        --source="example_dag.py"
    

### Update a DAG that has active DAG runs

If you update a DAG that has active DAG runs:

  * All currently executing tasks finish using the original DAG file.
  * All tasks that are scheduled but are not currently running use the updated DAG file.
  * All tasks that are no longer present in the updated DAG file are marked as removed.



### Update DAGs that run on a frequent schedule

After you upload a DAG file, it takes some time for Airflow to load this file and update the DAG. If your DAG runs on a frequent schedule, you might want to ensure that the DAG uses the updated version of the DAG file. To do so:

  1. Pause the DAG [in the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).

  2. Upload an updated DAG file.

  3. Wait until you see the updates in the Airflow UI. This means that the DAG was correctly parsed by the scheduler and updated in the Airflow database.

If the Airflow UI displays the updated DAGs, this does not guarantee that Airflow workers have the updated version of the DAG file. This happens because DAG files are synced independently for schedulers and workers.

  4. You might want to extend the waiting time to make sure that the DAG file is synced with all workers in your environment. The synchronization happens several times per minute. In a healthy environment, waiting for about 20-30 seconds is enough for all workers to sync.

  5. (Optional) If you want to be completely sure that all workers have the new version of the DAG file, inspect logs for each individual worker. To do so:

     1. Open the **Logs** tab for your environment in Google Cloud console.

     2. Go to **Composer logs** > **Infrastructure** > **Cloud Storage sync** item and inspect logs for every worker in your environment. Look for the most recent `Syncing dags directory` log item that has a timestamp after you uploaded the new DAG file. If you see a `Finished syncing` item that follows it, then the DAGs are synchronized successfully on this worker.

  6. Un-pause the DAG.




### Re-parse a DAG

**Important:** DAG parsing in Managed Airflow **happens automatically** shortly after the DAG is synchronized to the DAG processor.

Because DAGs are stored in the environment's bucket, each DAG is synchronized to the DAG processor first, and then the DAG processor parses it with a short delay. If you re-parse a DAG manually, for example, through Airflow UI, then the DAG processor **re-parses the current version of the DAG available to it** , which might not be the latest version of the DAG that you uploaded to the environment's bucket.

We recommend to use on-demand re-parsing only if you encounter long parsing times. For example, this might happen if your environment has a large number of files, or if a [long DAG parsing interval](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#min-file-process-interval) is configured in Airflow configuration options.

## Delete a DAG in your environment

To delete a DAG, remove the Python `.py` file for the DAG from the environment's `/dags` folder in your environment's bucket.

**Note:** Deleting a DAG does not remove the DAG metadata from the Airflow UI.

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, find a row with the name of your environment and in the **DAGs folder** column click the **DAGs** link. The **Bucket details** page opens. It shows contents of the `/dags` folder in your environment's bucket.

  3. Select the DAG file, click **Delete** , and confirm the operation.




###  gcloud 
    
    
    gcloud composer environments storage dags delete \
        --environment ENVIRONMENT_NAME \
        --location LOCATION \
        DAG_FILE
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `DAG_FILE` with the Python `.py` file for the DAG.



Example:
    
    
    gcloud composer environments storage dags delete \
        --environment example-environment \
        --location us-central1 \
        example_dag.py
    

## Remove a DAG from the Airflow UI

To remove the metadata for a DAG from the Airflow UI:

###  Airflow UI 

  1. [Go to the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) for your environment.
  2. For the DAG, click **Delete DAG**.



###  gcloud 

Run the following command in gcloud CLI:
    
    
      gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        dags delete -- DAG_NAME
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `DAG_NAME` is the name of the DAG to delete.



## What's next

  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-3/write-dags)
  * [Test, synchronize, and deploy your DAGs from GitHub](https://docs.cloud.google.com/composer/docs/composer-3/dag-cicd-github)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
