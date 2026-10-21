---
url: https://docs.cloud.google.com/functions/docs/tutorials/pubsub/
title: Trigger functions from Pub/Sub using Eventarc \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:34:10.041010+00:00
---

# Trigger functions from Pub/Sub using Eventarc  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/tutorials/pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Trigger functions from Pub/Sub using Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to write and trigger an event-driven Cloud Run functions with a [Pub/Sub trigger](https://docs.cloud.google.com/run/docs/tutorials/pubsub).

You can configure the routing of events, including the event source and the event target, by specifying filters for an Eventarc trigger. For the example in this tutorial, publishing a message to a Pub/Sub topic triggers the event, and a request is sent to your function in the form of an HTTP request.

If you are new to Pub/Sub and want to learn more, see the [Pub/Sub documentation](https://docs.cloud.google.com/pubsub/docs) for quickstarts and key references.

**Note:** You can also use [HTTP-triggered functions](https://docs.cloud.google.com/run/docs/triggering/https-request) to listen to [Pub/Sub push subscriptions](https://docs.cloud.google.com/pubsub/docs/push). Using an HTTP function enables a single function to subscribe to multiple Pub/Sub topics.

## Objectives

In this tutorial, you will:

  1. Deploy an event-driven function.
  2. Create an Eventarc trigger.
  3. Trigger the function by publishing a message to a Pub/Sub topic.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Cloud Run](https://docs.cloud.google.com/run)
  * [Cloud Logging](https://docs.cloud.google.com/logging)
  * [Eventarc](https://docs.cloud.google.com/eventarc)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. If you are not using Cloud Shell, update the Google Cloud CLI components and log in using your account: 
         
         gcloud components update
         gcloud auth login

  13. Enable the APIs: 
         
         gcloud services enable artifactregistry.googleapis.com \
             cloudbuild.googleapis.com \
             eventarc.googleapis.com \
             run.googleapis.com \
             logging.googleapis.com \
             pubsub.googleapis.com

  14. Set the configuration variables used in this tutorial: 
         
         export REGION=us-central1
         gcloud config set run/region ${REGION}
         gcloud config set run/platform managed
         gcloud config set eventarc/location ${REGION}

  15. Create a service account: 
         
         SERVICE_ACCOUNT=eventarc-trigger-sa
         
         gcloud iam service-accounts create $SERVICE_ACCOUNT

  16. If you are under a domain restriction organization policy [restricting](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) unauthenticated invocations for your project, you will need to access your deployed service as described under [Testing private services](https://docs.cloud.google.com/run/docs/triggering/https-request#testing-private).




### Required roles

You or your administrator must grant the deployer account, the trigger identity, and optionally, the Pub/Sub service agent and the Cloud Storage service agent the following IAM roles.

#### Required roles for the deployer account

  1. If you are the project creator, you are granted the [basic Owner role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`). By default, this Identity and Access Management (IAM) role includes the permissions necessary for full access to most Google Cloud resources and you can skip this step.

If you are not the project creator, required permissions must be granted on the project to the appropriate _principal_. For example, a principal can be a Google Account (for end users) or a service account (for applications and compute workloads). For more information, see the [Roles and permissions](https://docs.cloud.google.com/eventarc/docs/all-roles-permissions) page for your event destination.

To get the permissions that you need to complete this tutorial, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Run Source Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Note that by default, [Cloud Build permissions include permissions to upload and download Artifact Registry artifacts](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp).




#### Required roles for the trigger identity

  1. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) as you will attach it to an Eventarc trigger to represent the identity of the trigger for testing purposes. This service account is automatically created after enabling or using a Google Cloud service that uses Compute Engine, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
         
         gcloud projects describe PROJECT_ID --format='value(projectNumber)'

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. By default, Cloud Run services are only callable by Project Owners, Project Editors, and Cloud Run Admins and Invokers. You can [control access on a per-service basis](https://docs.cloud.google.com/run/docs/securing/managing-access#control-service-or-job-access); however, for testing purposes, grant the [Cloud Run Invoker role](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`run.invoker`) on the Google Cloud project to the Compute Engine service account. This grants the role on all Cloud Run services and jobs in a project. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/run.invoker

Note that if you create a trigger for an authenticated Cloud Run service without granting the Cloud Run Invoker role, the trigger is created successfully and is active. However, the trigger will not work as expected and a message similar to the following appears in the logs:

`The request was not authenticated. Either allow public access or set the proper Authorization header.`
  3. Grant the [Eventarc Event Receiver role](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver) (`roles/eventarc.eventReceiver`) on the project to the Compute Engine default service account so that the Eventarc trigger can receive events from event providers. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
             --role=roles/eventarc.eventReceiver




#### Optional role for the Cloud Storage service agent

  * Before creating a trigger for direct events from Cloud Storage, grant the [Pub/Sub Publisher role](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) to the Cloud Storage service agent: 
        
        SERVICE_ACCOUNT="$(gcloud storage service-agent --project=PROJECT_ID)"
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member="serviceAccount:${SERVICE_ACCOUNT}" \
            --role='roles/pubsub.publisher'




#### Optional role for the Pub/Sub service agent

  * If you enabled the Cloud Pub/Sub service agent on or before April 8, 2021, to support authenticated Pub/Sub push requests, grant the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) to the service agent. Otherwise, this role is granted by default: 
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
            --role=roles/iam.serviceAccountTokenCreator




## Create a Pub/Sub topic

In Cloud Run, Pub/Sub topics are not automatically created when you deploy a function. Before deploying your function, publish a message to this Pub/Sub topic to trigger the function:
    
    
    gcloud pubsub topics create YOUR_TOPIC_NAME

## Prepare the application

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git
         

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git
         

### Java
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git
         

### .NET
         
         git clone https://github.com/GoogleCloudPlatform/dotnet-docs-samples.git
         

###  Ruby 
         
         git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples.git
         

###  PHP 
         
         git clone https://github.com/GoogleCloudPlatform/php-docs-samples.git
         

  2. Change to the directory that contains the sample code for accessing Pub/Sub:

###  Node.js 
         
         cd nodejs-docs-samples/functions/v2/helloPubSub/
         

###  Python 
         
         cd python-docs-samples/functions/v2/pubsub/
         

###  Go 
         
         cd golang-samples/functions/functionsv2/hellopubsub/
         

### Java
         
         cd java-docs-samples/functions/v2/pubsub/
         

### .NET
         
         cd dotnet-docs-samples/functions/helloworld/HelloPubSub/
         

###  Ruby 
         
         cd ruby-docs-samples/functions/helloworld/pubsub/
         

###  PHP 
         
         cd php-docs-samples/functions/helloworld_pubsub/
         

  3. Take a look at the sample code:

### Node.js
         
         const functions = require('@google-cloud/functions-framework');
         
         // Register a CloudEvent callback with the Functions Framework that will
         // be executed when the Pub/Sub trigger topic receives a message.
         functions.cloudEvent('helloPubSub', cloudEvent => {
           // The Pub/Sub message is passed as the CloudEvent's data payload.
           const base64name = cloudEvent.data.message.data;
         
           const name = base64name
             ? Buffer.from(base64name, 'base64').toString()
             : 'World';
         
           console.log(`Hello, ${name}!`);
         });

### Python
         
         import base64
         
         from cloudevents.http import CloudEvent
         import functions_framework
         
         
         # Triggered from a message on a Cloud Pub/Sub topic.
         @functions_framework.cloud_event
         def subscribe(cloud_event: CloudEvent) -> None:
             # Print out the data from Pub/Sub, to prove that it worked
             print(
                 "Hello, " + base64.b64decode(cloud_event.data["message"]["data"]).decode() + "!"
             )
         
         

### Go
         
         // Package helloworld provides a set of Cloud Functions samples.
         package helloworld
         
         import (
         	"context"
         	"fmt"
         	"log"
         
         	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
         	"github.com/cloudevents/sdk-go/v2/event"
         )
         
         func init() {
         	functions.CloudEvent("HelloPubSub", helloPubSub)
         }
         
         // MessagePublishedData contains the full Pub/Sub message
         // See the documentation for more details:
         // https://cloud.google.com/eventarc/docs/cloudevents#pubsub
         type MessagePublishedData struct {
         	Message PubSubMessage
         }
         
         // PubSubMessage is the payload of a Pub/Sub event.
         // See the documentation for more details:
         // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
         type PubSubMessage struct {
         	Data []byte `json:"data"`
         }
         
         // helloPubSub consumes a CloudEvent message and extracts the Pub/Sub message.
         func helloPubSub(ctx context.Context, e event.Event) error {
         	var msg MessagePublishedData
         	if err := e.DataAs(&msg); err != nil {
         		return fmt.Errorf("event.DataAs: %w", err)
         	}
         
         	name := string(msg.Message.Data) // Automatically decoded from base64.
         	if name == "" {
         		name = "World"
         	}
         	log.Printf("Hello, %s!", name)
         	return nil
         }
         

### Java
         
         import com.google.cloud.functions.CloudEventsFunction;
         import com.google.gson.Gson;
         import functions.eventpojos.PubSubBody;
         import io.cloudevents.CloudEvent;
         import java.nio.charset.StandardCharsets;
         import java.util.Base64;
         import java.util.logging.Logger;
         
         public class SubscribeToTopic implements CloudEventsFunction {
           private static final Logger logger = Logger.getLogger(SubscribeToTopic.class.getName());
         
           @Override
           public void accept(CloudEvent event) {
             // The Pub/Sub message is passed as the CloudEvent's data payload.
             if (event.getData() != null) {
               // Extract Cloud Event data and convert to PubSubBody
               String cloudEventData = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
               Gson gson = new Gson();
               PubSubBody body = gson.fromJson(cloudEventData, PubSubBody.class);
               // Retrieve and decode PubSub message data
               String encodedData = body.getMessage().getData();
               String decodedData =
                   new String(Base64.getDecoder().decode(encodedData), StandardCharsets.UTF_8);
               logger.info("Hello, " + decodedData + "!");
             }
           }
         }

### .NET
         
         using CloudNative.CloudEvents;
         using Google.Cloud.Functions.Framework;
         using Google.Events.Protobuf.Cloud.PubSub.V1;
         using Microsoft.Extensions.Logging;
         using System.Threading;
         using System.Threading.Tasks;
         
         namespace HelloPubSub;
         
         public class Function : ICloudEventFunction<MessagePublishedData>
         {
             private readonly ILogger _logger;
         
             public Function(ILogger<Function> logger) =>
                 _logger = logger;
         
             public Task HandleAsync(CloudEvent cloudEvent, MessagePublishedData data, CancellationToken cancellationToken)
             {
                 string nameFromMessage = data.Message?.TextData;
                 string name = string.IsNullOrEmpty(nameFromMessage) ? "world" : nameFromMessage;
                 _logger.LogInformation("Hello {name}", name);
                 return Task.CompletedTask;
             }
         }

### Ruby
         
         require "functions_framework"
         require "base64"
         
         FunctionsFramework.cloud_event "hello_pubsub" do |event|
           # The event parameter is a CloudEvents::Event::V1 object.
           # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
           name = Base64.decode64 event.data["message"]["data"] rescue "World"
         
           # A cloud_event function does not return a response, but you can log messages
           # or cause side effects such as sending additional events.
           logger.info "Hello, #{name}!"
         end

### PHP
         
         use CloudEvents\V1\CloudEventInterface;
         use Google\CloudFunctions\FunctionsFramework;
         
         // Register the function with Functions Framework.
         // This enables omitting the `FUNCTIONS_SIGNATURE_TYPE=cloudevent` environment
         // variable when deploying. The `FUNCTION_TARGET` environment variable should
         // match the first parameter.
         FunctionsFramework::cloudEvent('helloworldPubsub', 'helloworldPubsub');
         
         function helloworldPubsub(CloudEventInterface $event): void
         {
             $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
         
             $cloudEventData = $event->getData();
             $pubSubData = base64_decode($cloudEventData['message']['data']);
         
             $name = $pubSubData ? htmlspecialchars($pubSubData) : 'World';
             fwrite($log, "Hello, $name!" . PHP_EOL);
         }


**Note:** The Pub/Sub message's data is stored as a `base64`-encoded string in the `data` property of the [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) object. To extract this data, you may need to decode it as shown in the preceding sample code.

## Deploy an event-driven function

To deploy the function, run the following command in the directory that contains the sample code:

###  Node.js 
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function helloPubSub \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `nodejs24`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



###  Python 
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function subscribe \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `python314`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



###  Go 
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function HelloPubSub \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `go127`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



### Java
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function functions.SubscribeToTopic \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `java25`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



### .NET
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function HelloPubSub.Function \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `dotnet10`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



###  Ruby 
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function hello_pubsub \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `ruby40`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



###  PHP 
    
    
      gcloud run deploy FUNCTION \
            --source . \
            --function helloworldPubsub \
            --base-image BASE_IMAGE \
    

Replace:

  * FUNCTION with the name of the function you are deploying. If you omit this parameter, you will be prompted to enter a name when you run the command. 
  * BASE_IMAGE with the base image environment for your function, for example, `php85`. For more details about base images and the packages included in each image, see [Supported language runtimes and base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).



If you are prompted to create a repository in the specified region, respond by pressing `y`. When the deployment is complete, the Google Cloud CLI displays a URL where the service is running.

## Create an Eventarc trigger

To deploy the function with a Pub/Sub trigger, run the following command in the directory that contains the sample code:

  1. Create an Eventarc Pub/Sub trigger:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=${REGION} \
             --destination-run-service=FUNCTION \
             --destination-run-region=${REGION} \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace:

     * TRIGGER_NAME with the name for your trigger.
     * FUNCTION with the name of your function.
     * PROJECT_NUMBER with your Google Cloud project number.

Note that when creating an Eventarc trigger for the first time in a Google Cloud project, there might be a delay in provisioning the Eventarc service agent. This issue can usually be resolved by attempting to create the trigger again. For more information, see [Permission denied errors](https://docs.cloud.google.com/eventarc/docs/troubleshooting#trigger-error).

  2. Confirm that the trigger was successfully created. Note that although your trigger is created immediately, it can take up to two minutes for a trigger to be fully functional.
         
         gcloud eventarc triggers list --location=${REGION}

The output should be similar to the following:
         
         NAME: helloworld-events
         TYPE: google.cloud.pubsub.topic.v1.messagePublished
         DESTINATION: Cloud Run service: helloworld-events
         ACTIVE: Yes
         LOCATION: us-central1
         




## Trigger the function

To test the Pub/Sub function:

  1. Assign the topic to a variable:
         
         TOPIC_ID=$(gcloud eventarc triggers describe TRIGGER_NAME --location $REGION --format='value(transport.pubsub.topic)')
         

  2. Publish a message to the topic:
         
         gcloud pubsub topics publish $TOPIC_ID --message="Hello World"
         




The Cloud Run service logs the body of the incoming message. You can view this in the Logs section of your Cloud Run instance:

  1. Navigate to the [Google Cloud console](https://console.cloud.google.com/run).
  2. Click the function.
  3. Select the **Logs** tab.

Logs might take a few moments to appear. If you don't see them immediately, check again after a few moments.

  4. Look for the "Hello World!" message.


**Success:** You created and triggered an event-driven Cloud Run function with a [Pub/Sub trigger](https://docs.cloud.google.com/run/docs/tutorials/pubsub).

## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and want to keep it without the changes added in this tutorial, delete the resources created for the tutorial.

### Delete the project

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

  1. Delete the Cloud Run service you deployed in this tutorial:
         
         gcloud run services delete SERVICE_NAME

Where `SERVICE_NAME` is your chosen service name.

You can also delete Cloud Run services from the [Google Cloud console](https://console.cloud.google.com/run).

  2. Remove any gcloud CLI default configurations you added during the tutorial setup.

For example:

`gcloud config unset run/region`

or

`gcloud config unset project`

  3. Delete other Google Cloud resources created in this tutorial:

     * Delete the Eventarc trigger: 
           
           gcloud eventarc triggers delete TRIGGER_NAME
           

Replace `TRIGGER_NAME` with the name of your trigger.



## What's next

  * [Create Eventarc triggers for other event types](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events)
  * [Manage functions](https://docs.cloud.google.com/run/docs/managing/services)
  * [Configure retries](https://docs.cloud.google.com/run/docs/tips/function-retries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
