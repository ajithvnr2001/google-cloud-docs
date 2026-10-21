---
url: https://docs.cloud.google.com/run/docs/tutorials/autoscale-workerpools-pubsub/
title: Autoscale worker pools based on the Pub/Sub queue volume \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:23.234028+00:00
---

# Autoscale worker pools based on the Pub/Sub queue volume  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/autoscale-workerpools-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Autoscale worker pools based on the Pub/Sub queue volume Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy a Cloud Run worker pool to process Pub/Sub messages, and automatically scale your consumer instances based on queue depth using [Cloud Run External Metrics Autoscaling (CREMA)](https://docs.cloud.google.com/run/docs/configuring/workerpools/crema-autoscaling).

## Objectives

In this tutorial, you will:

  * Create a Pub/Sub topic and subscription to push messages to the topic.
  * Deploy a Cloud Run worker pool that consumes messages from Pub/Sub.
  * Deploy the autoscaler CREMA service to scale your worker pool.
  * Test your autoscaling service by running a python script locally to generate load.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://docs.cloud.google.com/build/docs)
  * [Cloud Run](https://cloud.google.com/run)
  * [Pub/Sub](https://cloud.google.com/pubsub)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Run, Parameter Manager, Artifact Registry, Pub/Sub, and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,parametermanager.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com,pubsub.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Update components: 
         
         gcloud components update

  9. This tutorial uses several environment variables. For improved debugging, run the following command to generate an error when you make references to unset local environment variables: 
         
         set -u

  10. Set the following configuration variables for CREMA used in this tutorial: 
         
         export PROJECT_ID=PROJECT_ID
         export REGION=us-central1
         export TOPIC_ID=crema-pubsub-topic
         export SUBSCRIPTION_ID=crema-subscription
         export CREMA_SA_NAME=crema-service-account
         export CONSUMER_SA_NAME=consumer-service-account
         export CONSUMER_WORKER_POOL_NAME=worker-pool-consumer
         export CREMA_SERVICE_NAME=my-crema-service

Replace PROJECT_ID with the ID of your Google Cloud project.
  11. Set your project ID by running the following command: 
         
         gcloud config set project $PROJECT_ID

  12. You incur charges for your Cloud Run scaling service based on how often you trigger scaling. For more information, estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator).



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Pub/Sub Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)
  * [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Create a Pub/Sub topic and subscription

To autoscale your worker, create a pull subscription for your consumer application using the following steps:

  1. Create a Pub/Sub topic that represents a feed of messages:
         
         gcloud pubsub topics create $TOPIC_ID
         

  2. Create a pull subscription to consume messages from your Pub/Sub topic:
         
         gcloud pubsub subscriptions create $SUBSCRIPTION_ID --topic=$TOPIC_ID
         




## Create custom service accounts

This tutorial requires the following two service accounts with [minimum permissions required](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) to use the provisioned resources:

  * Consumer service account: identity for the consumer worker pool that processes messages. Run the following command to create the consumer service account:
        
        gcloud iam service-accounts create $CONSUMER_SA_NAME \
          --display-name="Pub/Sub consumer service account"
        

  * CREMA service account: identity for the autoscaler. Run the following command to create the CREMA service account:
        
        gcloud iam service-accounts create $CREMA_SA_NAME \
          --display-name="CREMA service account"
        




### Grant additional permissions to your custom service accounts

To scale the worker pool, grant the following permissions on the custom service accounts:

  1. Grant your CREMA service account permission to read from the Parameter Manager:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:$CREMA_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/parametermanager.parameterViewer"
         

  2. Grant your CREMA service account the permission to scale the worker pool:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:$CREMA_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/run.developer"
         

  3. Grant your CREMA service account the service account user role:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:$CREMA_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/iam.serviceAccountUser"
         

  4. Grant your CREMA service account permission to view metrics:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
            --member="serviceAccount:$CREMA_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
            --role="roles/monitoring.viewer"
         

  5. Grant your CREMA service account permission to write metrics:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
            --member="serviceAccount:$CREMA_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
            --role="roles/monitoring.metricWriter"
         

  6. Grant your CREMA service account permission to view Pub/Sub messages:
         
         gcloud pubsub subscriptions add-iam-policy-binding $SUBSCRIPTION_ID \
           --member="serviceAccount:$CREMA_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/pubsub.viewer"
         

  7. Grant your consumer service account permission to pull messages from the subscription:
         
         gcloud pubsub subscriptions add-iam-policy-binding $SUBSCRIPTION_ID \
           --member="serviceAccount:$CONSUMER_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/pubsub.subscriber"
         




## Deploy a Cloud Run worker pool

To deploy a worker pool that consumes messages from Pub/Sub subscriptions, follow these steps:

  1. Create a folder named `consumer` and change the directory into it:
         
         mkdir consumer
         cd consumer
         

  2. Create a file named `worker.py` and add the following code:
         
         import os
         import time
         from google.cloud import pubsub_v1
         from concurrent.futures import TimeoutError
         
         # Configuration
         PROJECT_ID = os.environ.get('PROJECT_ID')
         SUBSCRIPTION_ID = os.environ.get('SUBSCRIPTION_ID')
         
         subscription_path = f"projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}"
         
         print(f"Worker Pool instance starting. Watching {subscription_path}...")
         
         subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
         
         def callback(message):
             try:
                 data = message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data).decode("utf-8")
                 print(f"Processing job: {[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}")
                 time.sleep(5)  # Simulate work
                 print(f"Done {[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}")
                 message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
             except Exception as e:
                 print(f"Error processing message: {e}")
                 message.[nack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_nack)()
         
         streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
         print(f"Listening for messages on {subscription_path}...")
         
         # Wrap subscriber in a 'with' block to automatically call close() when done.
         with subscriber:
             try:
                 # When `timeout` is not set, result() will block indefinitely,
                 # unless an exception is encountered first.
                 streaming_pull_future.result()
             except TimeoutError:
                 streaming_pull_future.cancel()  # Trigger the shutdown.
                 streaming_pull_future.result()  # Block until the shutdown is complete.
             except Exception as e:
                 print(f"Streaming pull failed: {e}")
         

  3. Create a Dockerfile and add the following code:
         
         FROM python:3.12-slim
         RUN pip install google-cloud-pubsub
         COPY worker.py .
         CMD ["python", "-u", "worker.py"]
         

  4. Deploy the consumer worker pool with 0 instances for CREMA to scale up:
         
         gcloud run worker-pools deploy $CONSUMER_WORKER_POOL_NAME \
           --source . \
           --region $REGION \
           --service-account="$CONSUMER_SA_NAME@$PROJECT_ID.iam.gserviceaccount.com" \
           --instances=0 \
           --set-env-vars PROJECT_ID=$PROJECT_ID,SUBSCRIPTION_ID=$SUBSCRIPTION_ID
         




## Deploy the autoscaler CREMA service

Once you deploy the worker pool to consume messages from Pub/Sub, configure the CREMA autoscaler to provision worker instances based on the volume of messages.

### Configure the autoscaler

This tutorial uses the [Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview) to store the YAML configuration file for CREMA.

  1. Create a parameter in the Parameter Manager to store parameter versions for CREMA:
         
         PARAMETER_ID=crema-config
         PARAMETER_REGION=global
         gcloud parametermanager parameters create $PARAMETER_ID --location=$PARAMETER_REGION --parameter-format=YAML
         

  2. Navigate to the root directory of your project by running the following command:
         
         cd
         

  3. In your root directory, create a YAML file, `my-crema-config.yaml` to define the autoscaler configuration:
         
         apiVersion: crema/v1
         kind: CremaConfig
         spec:
           pollingInterval: 30
           triggerAuthentications:
             - metadata:
                 name: adc-trigger-auth
               spec:
                 podIdentity:
                   provider: gcp
           scaledObjects:
             - spec:
                 scaleTargetRef:
                   name: projects/PROJECT_ID/locations/us-central1/workerpools/worker-pool-consumer
                 triggers:
                   - type: gcp-pubsub
                     metadata:
                       subscriptionName: "crema-subscription"
                       # Target number of undelivered messages per worker instance
                       value: "10"
                       mode: "SubscriptionSize"
                     authenticationRef:
                       name: adc-trigger-auth
         

Replace PROJECT_ID with the Google Cloud project ID.

  4. Upload your local YAML file as a new parameter version:
         
         LOCAL_YAML_CONFIG_FILE=my-crema-config.yaml
         PARAMETER_VERSION=1
         
         gcloud parametermanager parameters versions create $PARAMETER_VERSION \
           --location=$PARAMETER_REGION \
           --parameter=$PARAMETER_ID \
           --payload-data-from-file=$LOCAL_YAML_CONFIG_FILE
         

  5. Run the following command to verify your parameter addition is successful:
         
         gcloud parametermanager parameters versions list \
         --parameter=$PARAMETER_ID \
         --location=$PARAMETER_REGION
         

You should see the parameter path, such as `projects/PROJECT_ID/locations/global/parameters/crema-config/versions/1`.




### Deploy the service to scale your workloads

To deploy the service to scale your worker pool, run the following command with a prebuilt container image:
    
    
    CREMA_CONFIG_PARAM_VERSION=projects/$PROJECT_ID/locations/$PARAMETER_REGION/parameters/$PARAMETER_ID/versions/$PARAMETER_VERSION
    IMAGE=us-central1-docker.pkg.dev/cloud-run-oss-images/crema-v1/autoscaler:1.0
    
    gcloud run deploy $CREMA_SERVICE_NAME \
      --image=${IMAGE} \
      --region=${REGION} \
      --service-account="${CREMA_SA_NAME}" \
      --no-allow-unauthenticated \
      --no-cpu-throttling \
      --base-image=us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/java25 \
      --labels=created-by=crema \
      --set-env-vars="CREMA_CONFIG=${CREMA_CONFIG_PARAM_VERSION},OUTPUT_SCALER_METRICS=True"
    

## Test your autoscaling service

Test your CREMA service by creating a script that generates 100 messages and pushes them to the Pub/Sub queue:

  1. In your root directory, create a file named `load-pubsub.sh`, and add the following code:
         
         #!/bin/bash
         
         TOPIC_ID=${TOPIC_ID}
         PROJECT_ID=${PROJECT_ID}
         NUM_MESSAGES=100
         
         echo "Publishing $NUM_MESSAGES messages to topic $TOPIC_ID..."
         
         for i in $(seq 1 $NUM_MESSAGES); do
           gcloud pubsub topics publish $TOPIC_ID --message="job-$i" --project=$PROJECT_ID &
           if (( $i % 10 == 0 )); then
             wait
             echo "Published $i messages..."
           fi
         done
         wait
         echo "Done. All messages published."
         

  2. Run the load test:
         
         chmod +x load-pubsub.sh
         ./load-pubsub.sh
         




This command generates and pushes 100 messages to the Pub/Sub subscription.

### Monitor Scaling

After the `load-pubsub.sh` script completes, wait **three to four minutes** before checking [logs](https://docs.cloud.google.com/run/docs/logging#service-logs) for the service, `my-crema-service`. The CREMA autoscaler service scales up the consumer worker instances from 0.

You should see the following logs:

Each log message is labeled with the component that emitted it.
    
    
    [INFO] [METRIC-PROVIDER] Starting metric collection cycle
    [INFO] [METRIC-PROVIDER] Successfully fetched scaled object metrics ...
    [INFO] [METRIC-PROVIDER] Sending scale request ...
    [INFO] [SCALER] Received ScaleRequest ...
    [INFO] [SCALER] Current instances ...
    [INFO] [SCALER] Recommended instances ...
    

Alternatively, run the following command to verify that the CREMA service recommends instances based on the queue depth:
    
    
    gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=$CREMA_SERVICE_NAME AND textPayload:SCALER" \
      --limit=20 \
      --format="value(textPayload)" \
      --freshness=5m
    

To view the consumer logs consuming messages, run the following command:
    
    
    gcloud run worker-pools logs tail $CONSUMER_WORKER_POOL_NAME --region=$REGION
    

You should see logs that follow the format, `Done job-100`.

## Clean up

To avoid additional charges to your Google Cloud account, delete all the resources you deployed with this tutorial.

### Delete the project

If you created a new project for this tutorial, delete the project. If you used an existing project and need to keep it without the changes you added in this tutorial, delete resources that you created for the tutorial.

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete tutorial resources

  1. Delete the Cloud Run service you deployed in this tutorial. Cloud Run services don't incur costs until they receive requests.

To delete your Cloud Run service, run the following command:
         
         gcloud run services delete SERVICE-NAME

Replace SERVICE-NAME with the name of your service.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove the `gcloud` default region configuration you added during tutorial setup:
         
         gcloud config unset run/region
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete the Pub/Sub resources:
         
         gcloud pubsub subscriptions delete $SUBSCRIPTION_ID
         gcloud pubsub topics delete $TOPIC_ID
         

  5. Delete other Google Cloud resources created in this tutorial:

     * [Delete the Cloud Run worker pool](https://docs.cloud.google.com/run/docs/managing/workerpools#delete)
     * [Delete the worker pool container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images) from Artifact Registry
     * [Delete the CREMA service](https://docs.cloud.google.com/run/docs/managing/services#delete)
     * [Delete the service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete)
     * [Delete the parameters in Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/delete-parameters)



## What's next

  * For a detailed walkthrough of this tutorial, see the codelab [Autoscale Cloud Run worker pools based on the Pub/Sub queue volume using CREMA](https://codelabs.developers.google.com/codelabs/cloud-run/crema-autoscaler-pubsub-workerpool).
  * Learn more about [Cloud Run worker pools](https://docs.cloud.google.com/run/docs/deploy-worker-pools).
  * Explore other [Cloud Run demos, tutorials, and samples](https://docs.cloud.google.com/run/docs).
  * Configure [other KEDA scalers](https://keda.sh/docs/latest/scalers/) with CREMA.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
