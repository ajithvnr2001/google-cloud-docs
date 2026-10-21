---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install/
title: Integrate backend modules with your system \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:23.245162+00:00
---

# Integrate backend modules with your system  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Integrate backend modules with your system Stay organized with collections  Save and categorize content based on your preferences. 

Backend modules provide an infrastructure to process large volumes of feature-related messages and interact with the agent desktop UI. This tutorial walks you through the process of integrating backend modules with your agent system.

For more information about background modules concepts and structure, see the [backend modules basics](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-basics) documentation.

## Prerequisites

  1. If you haven't configured it, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).
  2. Create a [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic) topic for each kind of event notification you need from Dialogflow. Note the topic ID and topic name for later backend deployment.
  3. [Configure your conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) using [Agent Assist console](https://agentassist.cloud.google.com/) with Pub/Sub topics.



## Automated Deployment

The deployment can be automated by a Google Cloud automation script or terraform.

### Automation Script

You can check [./deploy.sh](https://github.com/GoogleCloudPlatform/agent-assist-integrations/blob/d3a0d3a7a05de204f37ca6e7e5b13a7a3453ee37/aa-integration-backend/deploy.sh) for more details.

### Apply terraform changes

You can automate the deployment with a gcloud CLI automation script or terraform. Before applying terraform changes complete the following steps.

  1. Grant the following IAM roles to your account: 
     * `Project IAM Admin` (roles/resourcemanager.projectIamAdmin)
     * `Service Usage Admin` (roles/serviceusage.serviceUsageAdmin)
     * `Service Account Admin` (roles/iam.serviceAccountAdmin)
     * `Service Account User` (roles/iam.serviceAccountUser)
     * `Pub/Sub Admin` (roles/pubsub.admin)
     * `Secret Manager Admin` (roles/secretmanager.admin)
     * `Cloud Build Editor` (roles/cloudbuild.builds.editor)
     * `Artifact Registry Administrator` (roles/artifactregistry.admin)
     * `Storage Admin` (roles/storage.admin)
     * `Cloud Run Admin` (roles/run.admin)
     * `Cloud Memorystore Redis Admin` (roles/redis.admin)
     * `Serverless VPC Access Admin` (roles/vpcaccess.admin)
  2. Build images for UI Connector and for Cloud Pub/Sub Interceptor and note the image name. 
     * For UI Connector, run the following command under `./ui-connector` folder. 
           
           $ gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/aa-integration-backend/ui-connector

     * For Cloud Pub/Sub Interceptor, run the following command under `./cloud-pubsub-interceptor` folder. 
           
           $ gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/aa-integration-backend/cloud-pubsub-interceptor

  3. Create a Cloud Storage bucket to store terraform state and update the backend bucket value at `/terraform/backend.tf` using the following command. 
         
         GCP_PROJECT_ID=$(gcloud config get-value project)
         # Create the Cloud storage bucket
         gcloud storage buckets create gs://${GCP_PROJECT_ID}-tfstate
         # Enable Object Versioning to keep the history of your deployments
         gcloud storage buckets update gs://${GCP_PROJECT_ID}-tfstate --versioning

  4. Export the value of required terraform variables `gcp_project_id`, `ui_connector_docker_image` and `cloud_pubsub_interceptor_docker_image`. Example: export TF_VAR_gcp_project_id='you-gcp-project-id'. Alternatively, you can fill their values at `/terraform/variables.tf` directly.
  5. Customize the authentication method by modifying `auth.check_auth()` method at `/ui-connector/auth.py`.



If you want to automate these steps by using Cloud Build, follow this [instruction](https://docs.cloud.google.com/build/docs/automate-builds) and use the build configuration file [./terraform_cloudbuild.yaml](https://github.com/GoogleCloudPlatform/agent-assist-integrations/blob/d3a0d3a7a05de204f37ca6e7e5b13a7a3453ee37/aa-integration-backend/terraform_cloudbuild.yaml). To allow Cloud Build to deploy the services, you need to grant Cloud Build Service Account the IAM roles listed at Step 1.

## Manual deployment

Following steps explains how to deploy backend modules manually.

### Set up environment variables

To make the commands for deployment simpler, we recommend that you set the following useful environment variables in your shell. You can set the variables using the following example command:
    
    
    $ export GCP_PROJECT_ID='aa-integration-service'

Set the following environment variables:

  * `GCP_PROJECT_ID`: The project ID of your Cloud Platform project that hosts related resources. Example: `my-project`.
  * `SERVICE_REGION`: The location or region of your services and related Google Cloud resources. Platform resources. Example: `us-central1`.



### Set up an administrative account

We recommend using separate Google Cloud accounts for service administration and runtime identity. Service administration is mainly performed by humans with [Google accounts](https://docs.cloud.google.com/iam/docs/overview#google_account), while runtime identity grants Cloud Run services permissions using [service accounts](https://docs.cloud.google.com/iam/docs/overview#service_account) to enable access to necessary resources.

#### Prepare the human administrative account

If you plan to use an account that already has Editor or Owner permissions in your project, you can skip ahead to the [next section](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install#set_the_human_administrative_account_in_gcloud).

To manage the backend infrastructure, establish an administrator account and grant it the following Identity and Access Management (IAM) roles. Their permissions are all included in the [Editor and Owner basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

  * `roles/secretmanager.admin` (Secret Manager Admin): Manage secrets stored in Secret Manager for JWT generation and verification.
  * `roles/run.admin` (Cloud Run Admin): Deploy and manage Cloud Run services.
  * `roles/iam.serviceAccountUser` (Service Account User): Grant Cloud Run runtime service accounts `iam.serviceAccounts.actAs` permissions.
  * `roles/cloudbuild.builds.editor` (Cloud Build Editor): Build Docker images for the integration services using Cloud Build.
  * Artifact Registry Administrator: Store and manage built Docker images for the integration services.
  * `roles/pubsub.editor` (Cloud Pub/Sub Editor): Create and manage Cloud Pub/Sub topics and subscriptions.
  * `roles/redis.admin` (Redis Admin): Create and manage Memorystore for Redis' resources.



To grant IAM roles to a human account, use the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) Google Cloud CLI command. The following is an example command:
    
    
    $ gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
     --member='user:test-user@gmail.com' \
     --role='roles/pubsub.editor'

#### Set the human administrative account in gcloud

Replace `$ADMIN_ACCOUNT` with the administrator account you would like to use (for example: `myaccount@gmail.com`) in the following sample:
    
    
    $ gcloud config set account $ADMIN_ACCOUNT

### Set up service accounts

By default, Cloud Run services or jobs run as the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). Rather than leave the default, we recommend giving every Cloud Run service a dedicated identity by assigning it a user-managed service account with the minimum required set of permissions. If you plan to keep the default service account, you can skip ahead to [set environment variables](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install#set_environment_variables).

#### Create two service accounts for each Cloud Run runtime

**Note:** You can also perform all of the actions in this section using the [Cloud Console UI](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).

  1. To create the service accounts, replace the value of `$CONNECTOR_SERVICE_ACCOUNT_ID` and `$INTERCEPTOR_SERVICE_ACCOUNT_ID` if and run the following commands:
         
         $ export CONNECTOR_SERVICE_ACCOUNT_ID='aa-ui-connector' && gcloud iam service-accounts create $CONNECTOR_SERVICE_ACCOUNT_ID \
         --description='Agent Assist integration - UI connector service account' \
         --display-name='Agent Assist integration - UI connector'
         $ export INTERCEPTOR_SERVICE_ACCOUNT_ID='aa-pubsub-interceptor' && gcloud iam service-accounts create $INTERCEPTOR_SERVICE_ACCOUNT_ID \
         --description='Agent Assist integration - Pubsub interceptor service account' \
         --display-name='Agent Assist integration - Pubsub interceptor'

  2. Use the following sample command to assign the following roles to the UI connector and Cloud Pub/Sub connector service accounts:
         
         $ gcloud projects add-iam-policy-binding $GCP_PROJECT_ID \
         --member='serviceAccount:$CONNECTOR_SERVICE_ACCOUNT_ID@$GCP_PROJECT_ID.iam.gserviceaccount.com' \
         --role='roles/pubsub.editor'




Grant the following IAM roles to the UI connector service account:

  * `roles/redis.editor`
  * `roles/vpcaccess.user`
  * `roles/compute.viewer`
  * `roles/secretmanager.secretAccessor`
  * `roles/dialogflow.agentAssistClient`



Grant the following roles to the Cloud Pub/Sub connector service account:

  * `roles/redis.editor`
  * `roles/vpcaccess.user`
  * `roles/compute.viewer`



#### Set environment variables

Set the values of the following environment variables to be the service accounts you just created or the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) in your project.

  1. `CONNECTOR_SERVICE_ACCOUNT`: The service account for UI connector runtime. Example: `aa-ui-connector@my-project-id.iam.gserviceaccount.com`.
  2. `INTERCEPTOR_SERVICE_ACCOUNT`: The service account for Cloud Pub/Sub Interceptor runtime. Example: `aa-pubsub-interceptor@my-project-id.iam.gserviceaccount.com`.



### Customize the user authentication method

The [code repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend) supports both backend users and users of the frontend module for Genesys Cloud and Twilio.

  1. Within the code repository, open the `ui_connector/auth.py` file.
  2. Specify the supported identity provider by setting the environment variable `AUTH_OPTION` or implement your authentication method with `auth.check_auth`.

By default, `AUTH_OPTION` is empty and no users are allowed to register JWT with the UI Connector service. Supported values:

     * **`Salesforce`** : Verify the auth token using Salesforce OpenID Connect. Required environment variable: SALESFORCE_ORGANIZATION_ID.
     * **`SalesforceLWC`** : Verify a Salesforce OAuth Client Credentials auth token using the `oauth2/userinfo` REST endpoint. Required environment variables: SALESFORCE_ORGANIZATION_ID, SALESFORCE_DOMAIN.
     * **`GenesysCloud`** : Verify the auth token using Genesys SDK UsersAPI.
     * **`Twilio`** : Verify the auth token for Twilio. Required environment variable: TWILIO_FLEX_ENVIRONMENT.
     * **`Skip`** : Skip auth token verification. It shouldn't be used in production.

Example: 
    
    $ export AUTH_OPTION='Salesforce'

Each token type might have a different means of validation. You decide how the token is validated. Without any changes, `auth.check_auth` returns `false` for every request.




### Customize allowed origins (recommended)

To limit the origins that can access your service, change the value of `config.CORS_ALLOWED_ORIGINS` variable. The default value `*` will allow any origin to visit your service.

### Generate and store a JWT secret key

In order for the UI connector service to send secure authentication tokens back to the client, it must encrypt them using a JWT secret key. The key's value can be any arbitrary string, although it should be unique and difficult to guess. 

This secret key will be stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs).

#### Set environment variable

  * `JWT_SECRET_NAME`: The name for the secret key in Secret Manager. It can be any arbitrary name. Recommended value: `aa-integration-jwt-secret`.



#### Generate the key

We recommend generating a random hash as the JWT secret key so that it cannot be guessed by attackers. To do so, you can use [python secrets](https://docs.python.org/3/library/secrets.html) to generate secure random numbers for it.
    
    
    # generate_secret_key.py
    import secrets
    jwt_secret_key = secrets.token_bytes(16)
    print(jwt_secret_key) # Output example: b'L\x9b\xd6i4\xc3\x1d\x95\xe3\xf78z\xdda\x97\xec'

#### Store the key in Secret Manager

In the following example command, replace `my_key` with the secret key you plan to use.
    
    
    $ python generate_secret_key.py | gcloud secrets create $JWT_SECRET_NAME --data-file=- \
    --replication-policy=user-managed --locations=$SERVICE_REGION

### Set up Memorystore for Redis

To set up Redis, you need the following environment variables:

  * `VPC_CONNECTOR_NAME`: The name of your [Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#create-connector) for connecting Cloud Run services to [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview). Recommended value: `aa-integration-vpc`.
  * `VPC_NETWORK`: The VPC network to attach your Serverless VPC Access connector to. The value should be `default` if you don't set up VPC for your Google Cloud project.
  * `VPC_SUBNET`: The name of the authorized VPC network that your Redis instance is attached to. The value should be `default` if you haven't customized VPC network settings.
  * `REDIS_IP_RANGE`: An unreserved internal IP network for your Serverless VPC Access connector. A `/28` of unallocated space is required. Recommended value: `10.8.0.0/28` (this value should work for most new projects).
  * `REDIS_INSTANCE_ID`: A name for your Redis instance. Recommended value: `aa-integration-redis`.



#### Create a Redis instance in the region of your Cloud Run services

Run the following command:
    
    
    $ gcloud redis instances create $REDIS_INSTANCE_ID --size=5 --region=$SERVICE_REGION

You can connect to a Redis instance from Cloud Run by using [Direct Egress or Serverless VPC Access](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run).

#### Create a Serverless VPC Access connector {:#create-svpca-connector} (Optional)

This is optional now if customers choose Direct Egress. If you choose Serverless VPC Access, you'll need to create a Serverless VPC Access connector. For more details about this step, see the [Cloud Run tutorial](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#create-connector).

Verify that the Serverless VPC Access API is enabled for your project:
    
    
    $ gcloud services enable vpcaccess.googleapis.com

Create a Serverless VPC Access connector with a custom IP range:
    
    
    $ gcloud compute networks vpc-access connectors create $VPC_CONNECTOR_NAME \
      --network $VPC_NETWORK \
      --region $SERVICE_REGION \
      --range $REDIS_IP_RANGE

#### Save the Redis host and Redis port as environment variables

  * Set the IP Address of your Redis instance to environment variable `REDIS_HOST`.
  * Set the port number of your Redis instance to environment variable `REDIS_PORT`.



### Deploy the UI connector service

For the UI connector service, you need the following environment variables:

  * `CONNECTOR_SERVICE_NAME`: The Cloud Run service name of your UI Connector. Recommended value: `ui-connector`.
  * `CONNECTOR_IMAGE_NAME`: The image name of your UI Connector service. It can be the same as `CONNECTOR_SERVICE_NAME`. Recommended value: `ui-connector`.



#### Build the Docker image

Under the `/ui-connector` folder, run the following command:
    
    
    $ gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/$CONNECTOR_IMAGE_NAME

#### Deploy UI connector to Cloud Run

Under the [`/ui-connector` folder](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/main/aa-integration-backend/ui-connector), run the following command:

  * If using Direct Egress to connect for Redis connection.


    
    
    $ gcloud run deploy $CONNECTOR_IMAGE_NAME \
    --image gcr.io/$GCP_PROJECT_ID/$CONNECTOR_IMAGE_NAME \
    --platform managed \
    --service-account=$CONNECTOR_SERVICE_ACCOUNT_NAME \
    --allow-unauthenticated \
    --timeout 3600 \
    --region $SERVICE_REGION \
    --network $VPC_NETWORK \
    --subnet $VPC_SUBNET \
    --clear-vpc-connector \
    --min-instances=1 \
    --set-env-vars REDISHOST=$REDIS_HOST,REDISPORT=$REDIS_PORT,GCP_PROJECT_ID=$GCP_PROJECT_ID,AUTH_OPTION=$AUTH_OPTION \
    --update-secrets=/secret/jwt_secret_key=${JWT_SECRET_NAME}:latest

  * If using a created Serverless VPC Access connector for Redis connection.


    
    
    $ gcloud run deploy $CONNECTOR_IMAGE_NAME \
    --image gcr.io/$GCP_PROJECT_ID/$CONNECTOR_IMAGE_NAME \
    --platform managed \
    --service-account=$CONNECTOR_SERVICE_ACCOUNT_NAME \
    --allow-unauthenticated \
    --timeout 3600 \
    --region $SERVICE_REGION \
    --vpc-connector $VPC_CONNECTOR_NAME \
    --clear-network \
    --min-instances=1 \
    --no-cpu-throttling \
    --set-env-vars REDISHOST=$REDIS_HOST,REDISPORT=$REDIS_PORT,GCP_PROJECT_ID=$GCP_PROJECT_ID,AUTH_OPTION=$AUTH_OPTION \
    --update-secrets=/secret/jwt_secret_key=${JWT_SECRET_NAME}:latest

Make a note of the service URL for the deployed UI Connector, which will be used by clients (agent desktops).

### Deploy Cloud Pub/Sub interceptor service

For the Pub/Sub interceptor service, you need the following environment variables:

  * `INTERCEPTOR_SERVICE_NAME`: The Cloud Run service name of your Cloud Pub/Sub interceptor. Recommended value: `cloud-pubsub-interceptor`.
  * `INTERCEPTOR_IMAGE_NAME`: The image name of your Cloud Pub/Sub interceptor service. It can be the same as `INTERCEPTOR_SERVICE_NAME`. Recommended value: `cloud-pubsub-interceptor`.
  * `INTERCEPTOR_SERVICE_ACCOUNT_NAME`: The service account for Cloud Pub/Sub interceptor runtime.



#### Build the Docker image

Under the `/cloud-pubsub-interceptor` folder, run the following command: 
    
    
    $ gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/$INTERCEPTOR_IMAGE_NAME

#### Deploy Pub/Sub interceptor to Cloud Run

Under the `/cloud-pubsub-interceptor` folder, run the following command:

  * If using Direct Egress to connect for Redis connection.


    
    
    $ gcloud run deploy $INTERCEPTOR_SERVICE_NAME \
    --image gcr.io/$GCP_PROJECT_ID/$INTERCEPTOR_IMAGE_NAME \
    --platform managed \
    --service-account=$INTERCEPTOR_SERVICE_ACCOUNT_NAME \
    --region $SERVICE_REGION \
    --network $VPC_NETWORK \
    --subnet $VPC_SUBNET \
    --clear-vpc-connector \
    --ingress=internal \
    --min-instances=1 \
    --no-cpu-throttling \
    # You can also add LOGGING_FILE here to specify the logging file path on Cloud Run.
    --set-env-vars REDISHOST=$REDIS_HOST,REDISPORT=$REDIS_PORT

  * If using a created Serverless VPC Access connector for Redis connection.


    
    
    $ gcloud run deploy $INTERCEPTOR_SERVICE_NAME \
    --image gcr.io/$GCP_PROJECT_ID/$INTERCEPTOR_IMAGE_NAME \
    --platform managed \
    --service-account=$INTERCEPTOR_SERVICE_ACCOUNT_NAME \
    --region $SERVICE_REGION \
    --vpc-connector $VPC_CONNECTOR_NAME \
    --clear-network \
    --ingress=internal \
    --min-instances=1 \
    # You can also add LOGGING_FILE here to specify the logging file path on Cloud Run.
    --set-env-vars REDISHOST=$REDIS_HOST,REDISPORT=$REDIS_PORT

#### Save the deployed URL

Set the deployed URL as the `INTERCEPTOR_SERVICE_URL` environment variable.

### Configure Cloud Pub/Sub subscriptions

Cloud Pub/Sub subscriptions use the following:

  * Topics
  * Conversation profile
  * Service account
  * Service account permission for interceptor service



#### Create Cloud Pub/Sub topics

[Create a Cloud Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#create_a_topic) for each kind of event notification you need from Dialogflow. The available event notification types are:

  * **New suggestion events** : Events sent when new Agent Assist suggestions are available (for example, new Smart Reply suggestions in response to a customer utterance).
  * **New message events** : Events sent whenever a new utterance is recognized from an agent or customer (for example, customer says `Hi`).
  * **New conversation lifecycle events** : Events sent for certain conversation lifecycle changes (for example, when a conversation is started, or when it is completed).
  * **New recognition result-notification events** : Events sent when intermediate transcript is recognized from an agent or customer (for example, customer says `Hi, how can I help you?`, an intermediate transcript is `Hi how can` while customer is speaking).



Make a note of the topic ID and topic name for later backend deployment.

#### Configure a conversation profile

[Configure a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) with the Cloud Pub/Sub topics that you created in the previous step.

  * When you create a new conversation profile, select **Pub/Sub notifications** and then **Enable Pub/Sub notifications**. Once enabled, you can check the boxes next to the types of notifications you'd like to enable and enter the topic ID for the notification's associated Cloud Pub/Sub topic. 
  * Select `JSON` as the message format for each topic.



#### Create service account for Pub/Sub subscription identity

Create a service account representing the Pub/Sub subscription identity using the following command:
    
    
    $ gcloud iam service-accounts create cloud-run-pubsub-invoker \
         --display-name "Cloud Run Pub/Sub Invoker"

#### Give the service account permission to invoke your interceptor service

Run the following command:
    
    
    $ gcloud run services add-iam-policy-binding $INTERCEPTOR_SERVICE_NAME \ 
      --member=serviceAccount:cloud-run-pubsub-invoker@$GCP_PROJECT_ID.iam.gserviceaccount.com \
       --role=roles/run.invoker

#### Create Cloud Pub/Sub subscriptions for topics

For each topic that you created, you must create a corresponding Cloud Pub/Sub subscription.

##### New suggestion events

Replace `your-new-suggestion-topic-id` with the Cloud Pub/Sub topic you configured for new suggestions:
    
    
    $ export TOPIC_ID='your-new-suggestion-topic-id' && gcloud pubsub subscriptions create $SUBSCRIPTION_NAME --topic $TOPIC_ID \
       --push-endpoint=$INTERCEPTOR_SERVICE_URL/human-agent-assistant-event \
       --push-auth-service-account=cloud-run-pubsub-invoker@$GCP_PROJECT_ID.iam.gserviceaccount.com

##### New message events

Replace `your-new-message-event-topic-id` with the Cloud Pub/Sub topic you configured for new message events:
    
    
    $ export TOPIC_ID='your-new-message-event-topic-id' && gcloud pubsub subscriptions create $SUBSCRIPTION_NAME --topic $TOPIC_ID \
       --push-endpoint=$INTERCEPTOR_SERVICE_URL/new-message-event \
       --push-auth-service-account=cloud-run-pubsub-invoker@$GCP_PROJECT_ID.iam.gserviceaccount.com

##### Conversation lifecycle events

Replace `your-conversation-lifecycle-event-topic` with the Cloud Pub/Sub topic you configured for new conversation lifecycle events:
    
    
    $ export TOPIC_ID='your-conversation-lifecycle-event-topic' && gcloud pubsub subscriptions create $SUBSCRIPTION_NAME --topic $TOPIC_ID \
       --push-endpoint=$INTERCEPTOR_SERVICE_URL/conversation-lifecycle-event \
       --push-auth-service-account=cloud-run-pubsub-invoker@$GCP_PROJECT_ID.iam.gserviceaccount.com

##### New recognition-result notification events
    
    
    $ export TOPIC_ID='your-new-recognition-result-notification-event-topic' && gcloud pubsub subscriptions create $SUBSCRIPTION_NAME --topic $TOPIC_ID \
       --push-endpoint=$INTERCEPTOR_SERVICE_URL/new-recognition-result-notification-event \
       --push-auth-service-account=cloud-run-pubsub-invoker@$GCP_PROJECT_ID.iam.gserviceaccount.com

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
