---
url: https://docs.cloud.google.com/composer/docs/composer-3/triggering-gcf-pubsub/
title: Trigger DAGs with Cloud Functions and Pub/Sub Messages \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:41.508320+00:00
---

# Trigger DAGs with Cloud Functions and Pub/Sub Messages  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/triggering-gcf-pubsub/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Trigger DAGs with Cloud Functions and Pub/Sub Messages Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/triggering-gcf-pubsub "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

**Note:** This page is **not yet revised for Managed Airflow (Gen 3)** and displays content for Managed Airflow (Gen 2).

This page guides you through creating an event-based push architecture by triggering Managed Airflow DAGs in response to Pub/Sub topic changes. Examples in this tutorial demonstrate handling the full cycle of Pub/Sub management, including subscription management, as a part of the DAG process. It is suitable for some of the common use cases when you need to trigger DAGs but don't want to set up extra access permissions.

For example, messages sent through Pub/Sub can be used as a solution if you don't want to provide direct access to a Managed Airflow environment for security reasons. You can configure a Cloud Run function that creates Pub/Sub messages and publishes them on a Pub/Sub topic. You can then create a DAG that pulls Pub/Sub messages and then handles these messages.

**Note:** As an alternative approach, you can trigger DAGs using [only the Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-api), or you might want to trigger DAGs using Cloud Run functions [when a specific event occurs](https://docs.cloud.google.com/composer/docs/composer-2/triggering-with-gcf).

In this specific example, you create a Cloud Run function and deploy two DAGs. The first DAG pulls Pub/Sub messages and triggers the second DAG according to the Pub/Sub message content.

This tutorial assumes you are familiar with Python and the Google Cloud console.

## Objectives

**Objective:**

  * Create related resources and prepare your environment.
  * [Upload a DAG](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags) that subscribes to a Pub/Sub topic.
  * Configure and deploy a Cloud Run function that pushes Pub/Sub messages to a Pub/Sub topic.
  * Test your function.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Managed Airflow](https://docs.cloud.google.com/composer/pricing) (also see [additional costs](https://docs.cloud.google.com/composer/pricing#additional-costs))
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/pricing)
  * [Cloud Run functions](https://docs.cloud.google.com/functions/pricing)



After you finish this tutorial, you can avoid continued billing by deleting the resources you created. See Clean up for more detail.

## Before you begin

For this tutorial, you need a Google Cloud [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). Configure the project in the following way:

  1. In the Google Cloud console, [select or create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):

[Go to Project Selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. [Learn how to check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Make sure that your Google Cloud project user has the following [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to create the necessary resources:

     * **Service Account User** (`roles/iam.serviceAccountUser`) 
     * **Pub/Sub Editor** (`roles/pubsub.editor`)
     * **Environment and Storage Object Administrator** (`roles/composer.environmentAndStorageObjectAdmin`)
     * **Cloud Run functions Admin** (`roles/cloudfunctions.admin`)
     * **Logs Viewer** (`roles/logging.viewer`) 
  4. Make sure that the [service account that runs your Cloud Run function](https://docs.cloud.google.com/functions/docs/concepts/iam#access_control_for_service_accounts) has sufficient permissions in your project to access Pub/Sub. By default, Cloud Run functions use the [App Engine default service account](https://docs.cloud.google.com/appengine/docs/legacy/standard/python/service-account). This service account has the **Editor** role, which has sufficient permissions for this tutorial.




## Enable APIs for your project

###  Console 

Enable the Managed Airflow, Cloud Run functions, and Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=composer.googleapis.com,cloudfunctions.googleapis.com,pubsub.googleapis.com)

###  gcloud 

Enable the Managed Airflow, Cloud Run functions, and Pub/Sub APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable composer.googleapis.com cloudfunctions.googleapis.com pubsub.googleapis.com

###  Terraform 

Enable the Cloud Composer API in your project by adding the following resource definitions to your Terraform script:
    
    
    resource "google_project_service" "composer_api" {
      project = "<PROJECT_ID>"
      service = "composer.googleapis.com"
      // Disabling Cloud Composer API might irreversibly break all other
      // environments in your project.
      // This parameter prevents automatic disabling
      // of the API when the resource is destroyed.
      // We recommend to disable the API only after all environments are deleted.
      disable_on_destroy = false
    // this flag is introduced in 5.39.0 version of Terraform. If set to true it will
    //prevent you from disabling composer_api through Terraform if any environment was
    //there in the last 30 days
      check_if_service_has_usage_on_destroy = true
    }
    
    resource "google_project_service" "pubsub_api" {
      project = "<PROJECT_ID>"
      service = "pubsub.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service" "functions_api" {
      project = "<PROJECT_ID>"
      service = "cloudfunctions.googleapis.com"
      disable_on_destroy = false
    }
    

Replace `<PROJECT_ID>` with [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your project. For example, `example-project`.

## Create your Managed Airflow environment

[Create a Managed Airflow (Gen 2) environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#basic-setup).

[As a part of this procedure](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#grant-permissions), you grant the **Cloud Composer v2 API Service Agent Extension** (`roles/composer.ServiceAgentV2Ext`) role to the Composer Service Agent account. Managed Airflow uses this account to perform operations in your Google Cloud project.

## Create a Pub/Sub topic

This example triggers a DAG in response to a message pushed to a Pub/Sub topic. Create a Pub/Sub topic to use in this example:

###  Console 

  1. In the Google Cloud console, go to the **Pub/Sub Topics** page.

[Go to Pub/Sub Topics](https://console.cloud.google.com/cloudpubsub/topicList)

  2. Click **Create Topic**.

  3. In the **Topic ID** field, enter `dag-topic-trigger` as an ID for your topic.

  4. Leave other options at their defaults.

  5. Click **Create Topic**.




###  gcloud 

To create a topic, run the [gcloud pubsub topics create](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command in Google Cloud CLI:
    
    
    gcloud pubsub topics create dag-topic-trigger
    

###  Terraform 

Add the following resource definitions to your Terraform script:
    
    
    resource "google_pubsub_topic" "trigger" {
      project                    = "<PROJECT_ID>"
      name                       = "dag-topic-trigger"
      message_retention_duration = "86600s"
    }
    

Replace `<PROJECT_ID>` with [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your project. For example, `example-project`.

## Upload your DAGs

Upload DAGs to your environment:

  1. Save the following DAG file on your local computer.
  2. Replace `<PROJECT_ID>` with [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your project. For example, `example-project`.
  3. [Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the edited DAG file to your environment.


    
    
    from __future__ import annotations
    
    from datetime import datetime
    import time
    
    from airflow import DAG
    from airflow import XComArg
    from airflow.operators.python import PythonOperator
    from airflow.operators.trigger_dagrun import TriggerDagRunOperator
    from airflow.providers.google.cloud.operators.pubsub import (
        PubSubCreateSubscriptionOperator,
        PubSubPullOperator,
    )
    
    PROJECT_ID = "<PROJECT_ID>"
    TOPIC_ID = "dag-topic-trigger"
    SUBSCRIPTION = "trigger_dag_subscription"
    
    
    def handle_messages(pulled_messages, context):
        dag_ids = list()
        for idx, m in enumerate(pulled_messages):
            data = m.message.data.decode("utf-8")
            print(f"message {idx} data is {data}")
            dag_ids.append(data)
        return dag_ids
    
    
    # This DAG will run minutely and handle pub/sub messages by triggering target DAG
    with DAG(
        "trigger_dag",
        start_date=datetime(2021, 1, 1),
        schedule_interval="* * * * *",
        max_active_runs=1,
        catchup=False,
    ) as trigger_dag:
        # If subscription exists, we will use it. If not - create new one
        subscribe_task = PubSubCreateSubscriptionOperator(
            task_id="subscribe_task",
            project_id=PROJECT_ID,
            topic=TOPIC_ID,
            subscription=SUBSCRIPTION,
        )
    
        subscription = subscribe_task.output
    
        # Proceed maximum 50 messages in callback function handle_messages
        # Here we acknowledge messages automatically. You can use PubSubHook.acknowledge to acknowledge in downstream tasks
        # https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/hooks/pubsub/index.html#airflow.providers.google.cloud.hooks.pubsub.PubSubHook.acknowledge
        pull_messages_operator = PubSubPullOperator(
            task_id="pull_messages_operator",
            project_id=PROJECT_ID,
            ack_messages=True,
            messages_callback=handle_messages,
            subscription=subscription,
            max_messages=50,
        )
    
        # Here we use Dynamic Task Mapping to trigger DAGs according to messages content
        # https://airflow.apache.org/docs/apache-airflow/2.3.0/concepts/dynamic-task-mapping.html
        trigger_target_dag = TriggerDagRunOperator.partial(task_id="trigger_target").expand(
            trigger_dag_id=XComArg(pull_messages_operator)
        )
    
        (subscribe_task >> pull_messages_operator >> trigger_target_dag)
    
    
    def _some_heavy_task():
        print("Do some operation...")
        time.sleep(1)
        print("Done!")
    
    
    # Simple target DAG
    with DAG(
        "target_dag",
        start_date=datetime(2022, 1, 1),
        # Not scheduled, trigger only
        schedule_interval=None,
        catchup=False,
    ) as target_dag:
        some_heavy_task = PythonOperator(
            task_id="some_heavy_task", python_callable=_some_heavy_task
        )
    
        (some_heavy_task)

The sample code contains two DAGs: `trigger_dag` and `target_dag`.

The `trigger_dag` DAG subscribes to a Pub/Sub topic, pulls Pub/Sub messages, and triggers another DAG specified in the DAG ID of the Pub/Sub message data. In this example, `trigger_dag` triggers the `target_dag` DAG, which outputs messages to the task logs.

The `trigger_dag` DAG contains the following tasks:

  * `subscribe_task`: Subscribe to a Pub/Sub topic.
  * `pull_messages_operator`: Read a Pub/Sub message data with `PubSubPullOperator`.
  * `trigger_target_dag`: Trigger another DAG (in this example, `target_dag`) according to the data in the messages pulled from the Pub/Sub topic.



The `target_dag` DAG contains just one task: `output_to_logs`. This task prints messages to the task log with one second delay.

**Note:** If you want to pass more parameters to the DAG run, such as `conf` or `execution_date`, then you can modify the Cloud Run function and the DAG example. Pass the values in the Pub/Sub message, then handle them in the `trigger_target_dag` task. For more information about parameters that you can pass, see documentation for [`TriggerDagRunOperator`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/trigger_dagrun/index.html).

## Deploy a Cloud Run function that publishes messages on a Pub/Sub topic

In this section, you deploy a Cloud Run function that publishes messages on a Pub/Sub topic.

### Create a Cloud Run function and specify its configuration

###  Console 

  1. In the Google Cloud console, go to the **Cloud Run functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

  2. Click **Create function**.

  3. In the **Environment** field, select **1st gen**.

  4. In the **Function name** field, enter the name for your function: `pubsub-publisher`.

  5. In the **Trigger type** field, select **HTTP**.

  6. In the **Authentication** section, select **Allow unauthenticated invocations**. This option grants [unauthenticated users](https://docs.cloud.google.com/functions/docs/securing/managing-access-iam#allowing_unauthenticated_http_function_invocation) the ability to invoke an HTTP function.

**Caution:** For production use, consider using functions that require authentication. See [Authenticating for invocations](https://docs.cloud.google.com/functions/docs/securing/authenticating) for more information.
  7. Click Save.

  8. Click **Next** to move to the **Code** step.




###  Terraform 

Consider using the Google Cloud console for this step, because there is no straightforward way to manage the function's source code from Terraform.

This example demonstrates how you can upload a Cloud Run function from a local zip archive file by creating a Cloud Storage bucket, storing the file in this bucket, then using the file from the bucket as a source for the Cloud Run function. If you use this approach, Terraform doesn't automatically update the source code of your function, even if you create a new archive file. To re-upload the function code, you can change the file name of the archive.

  1. Donwload the [`pubsub_publisher.py`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/functions/pubsub_publisher.py) and the [`requirements.txt`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/functions/requirements.txt) files.
  2. In the `pubsub_publisher.py` file, replace `<PROJECT_ID>` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your project. For example, `example-project`.
  3. Create a zip archive named `pubsub_function.zip` with the `pbusub_publisner.py` and the `requirements.txt` file.
  4. Save the zip archive to a directory where your Terraform script is stored.
  5. Add the following resource definitions to your Terraform script and replace `<PROJECT_ID>` with the Project ID of your project.


    
    
    resource "google_storage_bucket" "cloud_function_bucket" {
      project        = <PROJECT_ID>
      name           = "<PROJECT_ID>-cloud-function-source-code"
      location       = "US"
      force_destroy  = true
      uniform_bucket_level_access = true
    }
    
    resource "google_storage_bucket_object" "cloud_function_source" {
      name   = "pubsub_function.zip"
      bucket = google_storage_bucket.cloud_function_bucket.name
      source = "./pubsub_function.zip"
    }
    
    resource "google_cloudfunctions_function" "pubsub_function" {
      project = <PROJECT_ID>
      name    = "pubsub-publisher"
      runtime = "python310"
      region  = "us-central1"
    
      available_memory_mb   = 128
      source_archive_bucket = google_storage_bucket.cloud_function_bucket.name
      source_archive_object = "pubsub_function.zip"
      timeout               = 60
      entry_point           = "pubsub_publisher"
      trigger_http          = true
    }
    

### Specify Cloud Run function code parameters

###  Console 

  1. In the **Code** step, In the **Runtime** field, select the language runtime your function uses. In this example, select **Python 3.10**.

  2. In the **Entry point** field, enter `pubsub_publisher`. This is the code that is executed when your Cloud Run function runs. The value of this flag must be a function name or a fully-qualified class name that exists in your source code.




###  Terraform 

Skip this step. Cloud Run function parameters are already defined in the `google_cloudfunctions_function` resource.

### Upload your Cloud Run function code

###  Console 

In the **Source code** field, select the appropriate option for how you [supply the function source code](https://docs.cloud.google.com/functions/docs/create-deploy-gcloud-1st-gen#get_the_sample_code). In this tutorial, add your function code using the Cloud Run functions **Inline Editor**. As an alternative, you can upload a ZIP file, or use Cloud Source Repositories.

  1. Put the following code example into the **main.py** file.
  2. Replace `<PROJECT_ID>` with [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your project. For example, `example-project`.


    
    
    from google.cloud import pubsub_v1
    
    project = "<PROJECT_ID>"
    topic = "dag-topic-trigger"
    
    
    def pubsub_publisher(request):
        """Publish message from HTTP request to Pub/Sub topic.
        Args:
            request (flask.Request): HTTP request object.
        Returns:
            The response text with message published into Pub/Sub topic
            Response object using
            `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
        """
        request_json = request.get_json()
        print(request_json)
        if request.args and "message" in request.args:
            data_str = request.args.get("message")
        elif request_json and "message" in request_json:
            data_str = request_json["message"]
        else:
            return "Message content not found! Use 'message' key to specify"
    
        publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
        # The `topic_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/topics/{topic_id}`
        topic_path = publisher.topic_path(project, topic)
    
        # The required data format is a bytestring
        data = data_str.encode("utf-8")
        # When you publish a message, the client returns a future.
        message_length = len(data_str)
        future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data, message_length=str(message_length))
        print(future.result())
    
        return f"Message {[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)} with message_length {message_length} published to {topic_path}."
    
    

###  Terraform 

Skip this step. Cloud Run function parameters are already defined in the `google_cloudfunctions_function` resource.

### Specify your Cloud Run function dependencies

###  Console 

Specify the function dependencies in the **requirements.txt** metadata file:
    
    
    requests-toolbelt==1.0.0
    google-auth==2.38.0
    google-cloud-pubsub==2.28.0
    

When you deploy your function, Cloud Run functions downloads and installs dependencies declared in the **requirements.txt** file, one line per package. This file must be in the same directory as the **main.py** file that contains your function code. For more details, see [Requirements Files](https://pip.pypa.io/en/stable/user_guide/#requirements-files) in `pip` documentation.

###  Terraform 

Skip this step. Cloud Run function dependencies are defined in the `requirements.txt` file in the `pubsub_function.zip` archive.

### Deploy your Cloud Run function

###  Console 

Click **Deploy**. When deployment finishes successfully, the function appears with a green check mark on the **Cloud Run functions** page in the Google Cloud console.

Make sure that the service account that runs your Cloud Run function has enough permissions in your project to access Pub/Sub.

###  Terraform 

  1. Initialize Terraform:
         
         terraform init
         

  2. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations:
         
         terraform plan
         

  3. To check whether your configuration is valid, run the following command:
         
         terraform validate
         

  4. Apply the Terraform configuration by running the following command and entering yes at the prompt:
         
         terraform apply
         




Wait until Terraform displays the "Apply complete!" message.

In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them.

## Test your Cloud Run function

To check that your function publishes a message on a Pub/Sub topic and that the example DAGs work as intended:

  1. Check that the DAGs are active:

     1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     2. In the list of environments, click the name of your environment. The **Environment details** page opens.

     3. Go to the **DAGs** tab.

     4. Check values in the **State** column for DAGs named `trigger_dag` and `target_dag`. Both DAGs must be in the `Active` state.

  2. Push a test Pub/Sub message. You can do it in Cloud Shell:

     1. In the Google Cloud console, go to the **Functions** page.

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

     2. Click the name of your function, `pubsub-publisher`.

     3. Go to the **Testing** tab.

     4. In **Configure triggering event** section, enter the following JSON key-value: `{"message": "target_dag"}`. Don't modify the key-value pair, because this message triggers the test DAG later.

     5. In the **Test Command** section, click **Test in Cloud Shell**.

     6. In **Cloud Shell Terminal** , wait until a command appears automatically. Run this command by pressing `Enter`.

     7. If the **Authorize Cloud Shell** message appears, click **Authorize**.

     8. Check that the message content corresponds to the Pub/Sub message. In this example, the output message must start with `Message b'target_dag' with message_length 10 published to` as a response from your function.

  3. Check that `target_dag` was triggered:

     1. Wait at least one minute, so that a new DAG run of `trigger_dag` completes.

     2. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     3. In the list of environments, click the name of your environment. The **Environment details** page opens.

     4. Go to the **DAGs** tab.

     5. Click `trigger_dag` to go to the **DAG details** page. On the **Runs** tab, a list of DAG runs for the `trigger_dag` DAG is displayed.

This DAG runs every minute and processes all Pub/Sub messages sent from the function. If no messages were sent, then the `trigger_target` task is marked as `Skipped` in the DAG run logs. If DAGs were triggered, then the `trigger_target` task is marked as `Success`.

     6. Look through several recent DAG runs to locate a DAG run where all three tasks (`subscribe_task`, `pull_messages_operator`, and `trigger_target`) are in `Success` statuses.

     7. Go back to the **DAGs** tab and check that the **Successful runs** column for the `target_dag` DAG lists one successful run.




## Summary

In this tutorial, you learned how to use Cloud Run functions to publish messages on a Pub/Sub topic and deploy a DAG that subscribes to a Pub/Sub topic, pulls Pub/Sub messages, and triggers another DAG specified in the DAG ID of the message data.

There are also alternative ways of [creating and managing Pub/Sub subscriptions](https://docs.cloud.google.com/pubsub/docs/create-subscription#create_subscriptions) and [triggering DAGs](https://docs.cloud.google.com/composer/docs/composer-2/schedule-and-trigger-dags) that are outside of the scope of this tutorial. For example, you can [use Cloud Run functions to trigger Airflow DAGs](https://docs.cloud.google.com/composer/docs/composer-2/triggering-with-gcf) when a specified event occurs. [Have a look at our tutorials](https://docs.cloud.google.com/docs/tutorials) to try out the other Google Cloud features for yourself.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

###  Console 

  1. [Delete the Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments). You also delete the environment's bucket during this procedure.
  2. [Delete the Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic#delete_a_topic), `dag-topic-trigger`.
  3. Delete the Cloud Run function.

     1. In the Google Cloud console, go to Cloud Run functions.

[Go to Cloud Run functions](https://console.cloud.google.com/functions/list)

     2. Click the checkbox for the function that you want to delete, `pubsub-publisher`.

     3. Click **Delete** , and then follow the instructions.




###  Terraform 

  1. Make sure that your Terraform script doesn't contain entries for resources that are still required by your project. For example, you might want to keep some APIs enabled and IAM permissions still assigned (if you added such definitions to your Terraform script).
  2. Run `terraform destroy`.
  3. Manually delete the environment's bucket. Managed Airflow doesn't delete it automatically. You can do it from the Google Cloud console or Google Cloud CLI.



## What's next

  * [Testing DAGs](https://docs.cloud.google.com/composer/docs/composer-2/test-dags)
  * [Testing HTTP Functions](https://docs.cloud.google.com/functions/docs/testing/test-http)
  * [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy)
  * Try out other Google Cloud features for yourself. Have a look at [our tutorials](https://docs.cloud.google.com/docs/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
