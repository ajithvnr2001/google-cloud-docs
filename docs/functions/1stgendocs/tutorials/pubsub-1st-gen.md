---
url: https://docs.cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen/
title: Cloud Pub/Sub Tutorial (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:43.461251+00:00
---

# Cloud Pub/Sub Tutorial (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback 

#  Cloud Pub/Sub Tutorial (1st gen) Stay organized with collections  Save and categorize content based on your preferences. 

This simple tutorial demonstrates writing, deploying, and triggering an [Event-Driven Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions) with a [Pub/Sub trigger](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub).

If you are new to Pub/Sub and want to learn more, see the Pub/Sub [documentation](https://docs.cloud.google.com/pubsub/docs), particularly [managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin). See [Pub/Sub Triggers](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) for an overview of working with Pub/Sub topics and subscriptions in Cloud Run functions.

If you're looking for code samples for using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs) itself, please visit the [sample browser](https://docs.cloud.google.com/docs/samples?p=pubsub).

**Note:** You can also use [HTTP-triggered functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) to listen to [Pub/Sub push subscriptions](https://docs.cloud.google.com/pubsub/docs/subscriber#push-subscription). Using an HTTP function enables a single function to subscribe to multiple Pub/Sub topics.

## Objectives

  * Write and deploy an [Event-Driven Cloud Run function](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions).
  * Trigger the function by publishing a message to a [Pub/Sub](https://docs.cloud.google.com/pubsub) topic.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Run functions
  * Pub/Sub



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

  4. Enable the Cloud Functions and Cloud Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,pubsub&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Functions and Cloud Pub/Sub APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudfunctions,pubsub&redirect=https%3A//cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

If you already have the gcloud CLI installed, update it by running the following command:
    
    gcloud components update

  14. Prepare your development environment. 

###  Node.js 

[ Go to the Node.js setup guide ](https://docs.cloud.google.com/nodejs/docs/setup)

###  Python 

[ Go to the Python setup guide ](https://docs.cloud.google.com/python/docs/setup)

###  Go 

[ Go to the Go setup guide ](https://docs.cloud.google.com/go/docs/setup)

###  Java 

[ Go to the Java setup guide ](https://docs.cloud.google.com/java/docs/setup)

###  Ruby 

[ Go to the Ruby setup guide ](https://docs.cloud.google.com/ruby/docs/setup)




## Preparing the application

  1. Clone the sample app repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Python 
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Go 
         
         git clone https://github.com/GoogleCloudPlatform/golang-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/golang-samples/archive/main.zip) as a zip file and extract it. 

###  Java 
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/main.zip) as a zip file and extract it. 

###  Ruby 
         
         git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/ruby-docs-samples/archive/main.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run functions sample code for accessing Pub/Sub:

###  Node.js 
         
         cd nodejs-docs-samples/functions/helloworld/

###  Python 
         
         cd python-docs-samples/functions/helloworld/

###  Go 
         
         cd golang-samples/functions/helloworld/

###  Java 
         
         cd java-docs-samples/functions/helloworld/hello-pubsub/

###  Ruby 
         
         cd ruby-docs-samples/functions/helloworld/pubsub/

  3. Take a look at the sample code:

###  Node.js 
         
         /**
          * Background Cloud Function to be triggered by Pub/Sub.
          * This function is exported by index.js, and executed when
          * the trigger topic receives a message.
          *
          * @param {object} message The Pub/Sub message.
          * @param {object} context The event metadata.
          */
         exports.helloPubSub = (message, context) => {
           const name = message.data
             ? Buffer.from(message.data, 'base64').toString()
             : 'World';
         
           console.log(`Hello, ${name}!`);
         };

###  Python 
         
         def hello_pubsub(event, context):
             """Background Cloud Function to be triggered by Pub/Sub.
             Args:
                  event (dict):  The dictionary with data specific to this type of
                                 event. The `@type` field maps to
                                  `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
                                 The `data` field maps to the PubsubMessage data
                                 in a base64-encoded string. The `attributes` field maps
                                 to the PubsubMessage attributes if any is present.
                  context (google.cloud.functions.Context): Metadata of triggering event
                                 including `event_id` which maps to the PubsubMessage
                                 messageId, `timestamp` which maps to the PubsubMessage
                                 publishTime, `event_type` which maps to
                                 `google.pubsub.topic.publish`, and `resource` which is
                                 a dictionary that describes the service API endpoint
                                 pubsub.googleapis.com, the triggering topic's name, and
                                 the triggering event type
                                 `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
             Returns:
                 None. The output is written to Cloud Logging.
             """
             import base64
         
             print(
                 """This Function was triggered by messageId {} published at {} to {}
             """.format(
                     context.event_id, context.timestamp, context.resource["name"]
                 )
             )
         
             if "data" in event:
                 name = base64.b64decode(event["data"]).decode("utf-8")
             else:
                 name = "World"
             print(f"Hello {name}!")
         
         

###  Go 
         
         // Package helloworld provides a set of Cloud Functions samples.
         package helloworld
         
         import (
         	"context"
         	"log"
         )
         
         // PubSubMessage is the payload of a Pub/Sub event.
         // See the documentation for more details:
         // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
         type PubSubMessage struct {
         	Data []byte `json:"data"`
         }
         
         // HelloPubSub consumes a Pub/Sub message.
         func HelloPubSub(ctx context.Context, m PubSubMessage) error {
         	name := string(m.Data) // Automatically decoded from base64.
         	if name == "" {
         		name = "World"
         	}
         	log.Printf("Hello, %s!", name)
         	return nil
         }
         

###  Java 
         
         import com.google.cloud.functions.BackgroundFunction;
         import com.google.cloud.functions.Context;
         import functions.eventpojos.PubsubMessage;
         import java.nio.charset.StandardCharsets;
         import java.util.Base64;
         import java.util.logging.Level;
         import java.util.logging.Logger;
         
         public class HelloPubSub implements BackgroundFunction<PubsubMessage> {
           private static final Logger logger = Logger.getLogger(HelloPubSub.class.getName());
         
           @Override
           public void accept(PubsubMessage message, Context context) {
             String name = "world";
             if (message != null && message.getData() != null) {
               name = new String(
                   Base64.getDecoder().decode(message.getData().getBytes(StandardCharsets.UTF_8)),
                   StandardCharsets.UTF_8);
             }
             logger.info(String.format("Hello %s!", name));
             return;
           }
         }

###  Ruby 
         
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

**Note:** The Pub/Sub message's data is stored as a `base64`-encoded string in the `data` property of the [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) object. To extract this data, you may need to decode it as shown in the examples above. The `context` parameter is described [here](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions).



## Deploying the function

To deploy the function with a Pub/Sub trigger, run the following command in the directory that contains the sample code (or in the case of Java, the `pom.xml` file):

###  Node.js 
    
    
    gcloud functions deploy helloPubSub \
    --runtime nodejs22 \  
    --trigger-topic YOUR_TOPIC_NAME

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy hello_pubsub \
    --runtime python312 \  
    --trigger-topic YOUR_TOPIC_NAME

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy HelloPubSub \
    --runtime go121 \  
    --trigger-topic YOUR_TOPIC_NAME

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-pubsub-function \
    --entry-point functions.HelloPubSub \
    --runtime java17 \
    --memory 512MB \  
    --trigger-topic YOUR_TOPIC_NAME

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

###  Ruby 
    
    
    gcloud functions deploy hello_pubsub --runtime ruby33 \  
    --trigger-topic YOUR_TOPIC_NAME

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Ruby version](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) to run your function. 

where `YOUR_TOPIC_NAME` is the name of the Pub/Sub topic to which the function will be subscribed.

If `YOUR_TOPIC_NAME` doesn't already exist, this command creates it for you. You can also create a topic before you run the `deploy` command, using either the [Google Cloud console](https://docs.cloud.google.com/pubsub/docs/create-topic-console) or the following `gcloud` command:
    
    
    gcloud pubsub topics create YOUR_TOPIC_NAME

**Note:** Cloud Run functions automatically creates [push subscriptions](https://docs.cloud.google.com/pubsub/docs/subscriber#push-subscription) that forward messages from the specified topic to your function.

## Triggering the function

  1. Publish a message to your Pub/Sub topic. In this example, the message is a name that the function will include in a greeting:
         
         gcloud pubsub topics publish YOUR_TOPIC_NAME --message YOUR_NAME

Replace `YOUR_TOPIC_NAME` with the name of your Pub/Sub topic, and `YOUR_NAME` with an arbitrary string.

  2. Check the logs to be sure the executions have completed:
         
         gcloud functions logs read --limit 50

**Note:** Logs might take a few moments to appear. If you don't see them immediately, check again in a minute or two.



You can also publish a message to a Pub/Sub topic [from within a function](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub#publishing_a_message_from_within_a_function).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Deleting the project

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



### Deleting the function

Deleting Cloud Run functions does not remove any resources stored in Cloud Storage.

To delete the function you created in this tutorial, run the following command:

###  Node.js 
    
    
    gcloud functions delete helloPubSub 

###  Python 
    
    
    gcloud functions delete hello_pubsub 

###  Go 
    
    
    gcloud functions delete HelloPubSub 

###  Java 
    
    
    gcloud functions delete java-pubsub-function 

###  Ruby 
    
    
    gcloud functions delete hello_pubsub 

You can also delete Cloud Run functions from the [Google Cloud console](https://console.cloud.google.com/functions/list).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
