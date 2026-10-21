---
url: https://docs.cloud.google.com/appengine/docs/managed-vms/php/writing-and-responding-to-pub-sub-messages/
title: Writing and responding to Pub/Sub messages \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:46:31.238933+00:00
---

# Writing and responding to Pub/Sub messages  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/managed-vms/php/writing-and-responding-to-pub-sub-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Writing and responding to Pub/Sub messages Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed#region-id). 

OK

[Pub/Sub](https://docs.cloud.google.com/pubsub/docs) provides reliable, many-to-many, asynchronous messaging between applications. Publisher applications can send messages to a _topic_ , and other applications can subscribe to that topic to receive the messages.

This document describes how to use the [Cloud Client Libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries) to send and receive Pub/Sub messages in an App Engine app. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) version of Python by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) file. 

## Prerequisites

  * Follow the instructions to [build an app for your selected runtime](https://docs.cloud.google.com/appengine/docs/flexible) to set up your environment and project, and to understand how App Engine apps are structured.
  * Write down and save your project ID, because you will need it to run the sample application described in this document.
  * [Create a service account and service account key](https://docs.cloud.google.com/appengine/docs/flexible/access-control#service_account) to use with your application.
  * Enable the Google Cloud Pub/Sub API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub)




## Cloning the sample app

Copy the sample apps to your local machine, and navigate to the `pubsub` directory:

### Go
    
    
    git clone https://github.com/GoogleCloudPlatform/golang-samples.git
    cd golang-samples/appengine_flexible/pubsub
    

### Java
    
    
    git clone https://github.com/GoogleCloudPlatform/java-docs-samples
    cd java-docs-samples/flexible/java-11/pubsub/
    

### Node.js
    
    
    git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples
    cd nodejs-docs-samples/appengine/pubsub
    

### PHP
    
    
    git clone https://github.com/GoogleCloudPlatform/php-docs-samples.git
    cd php-docs-samples/pubsub
    

### Python
    
    
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
    cd python-docs-samples/appengine/flexible/pubsub
    

### Ruby
    
    
    git clone https://github.com/GoogleCloudPlatform/ruby-docs-samples
    cd ruby-docs-samples/appengine/flexible/pubsub/
    

### .NET
    
    
    git clone  https://github.com/GoogleCloudPlatform/dotnet-docs-samples
    cd dotnet-docs-samples/appengine/flexible/Pubsub/Pubsub.Sample
    

## Create a topic and subscription

Create a topic and subscription, which includes specifying the endpoint to which the Pub/Sub server should send requests:

### Go
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### Java
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### Node.js
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### PHP
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### Python
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### Ruby
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### .NET
    
    
    # Configure the topic
    gcloud pubsub topics create YOUR_TOPIC_NAME
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10

Replace `YOUR_TOKEN` with a secret random token. The push endpoint uses this to verify requests. 

To use Pub/Sub with authentication, create another subscription:
    
    
    # Configure the push subscription
    gcloud pubsub subscriptions create YOUR_SUBSCRIPTION_NAME \
        --topic=YOUR_TOPIC_NAME \
        --push-auth-service-account=YOUR-SERVICE-ACCOUNT-EMAIL\
        --push-auth-token-audience=OPTIONAL_AUDIENCE_OVERRIDE\
        --push-endpoint=https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com/push-handlers/receive_messages?token=YOUR_TOKEN \
        --ack-deadline=10
    
    # Your service agent
    # `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com` needs to have the
    # `iam.serviceAccountTokenCreator` role.
    PUBSUB_SERVICE_ACCOUNT="service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com"
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
        --member="serviceAccount:${PUBSUB_SERVICE_ACCOUNT}"\
        --role='roles/iam.serviceAccountTokenCreator'

Replace `YOUR-SERVICE-ACCOUNT-EMAIL` with your [service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts) email.

### Setting environment variables

### Go

Edit the `app.yaml` file to set the environment variables for your topic and verification token:
    
    
    env_variables:
      PUBSUB_TOPIC: your-topic
      # This token is used to verify that requests originate from your
      # application. It can be any sufficiently random string.
      PUBSUB_VERIFICATION_TOKEN: your-token

### Java

Edit the `app.yaml` file to set the environment variables for your topic and verification token:
    
    
    env_variables:
      PUBSUB_TOPIC: <your-topic-name>
      # This token is used to verify that requests originate from your
      # application. It can be any sufficiently random string.
      PUBSUB_VERIFICATION_TOKEN: <your-verification-token>

### Node.js

Edit your `app.yaml` file to set the environment variables for your topic and verification token:
    
    
    env_variables:
      PUBSUB_TOPIC: YOUR_TOPIC_NAME
      # This token is used to verify that requests originate from your
      # application. It can be any sufficiently random string.
      PUBSUB_VERIFICATION_TOKEN: YOUR_VERIFICATION_TOKEN

### PHP

Edit your `index.php` file to set the environment variables for your topic and subscription:
    
    
    $container->set('topic', 'php-example-topic');
    $container->set('subscription', 'php-example-subscription');

### Python

Edit the `app.yaml` file to set the environment variables for your project ID, topic, and verification token:
    
    
    env_variables:
        PUBSUB_TOPIC: your-topic
        # This token is used to verify that requests originate from your
        # application. It can be any sufficiently random string.
        PUBSUB_VERIFICATION_TOKEN: 1234abc

### Ruby

Edit the `app.yaml` file to set the environment variables for your project ID, topic, and verification token:
    
    
    env_variables:
        PUBSUB_TOPIC: <pubsub-topic-name>
        # This token is used to verify that requests originate from your
        # application. It can be any sufficiently random string.
        PUBSUB_VERIFICATION_TOKEN: <verification-token>

### .NET

Edit the `app.yaml` file to set the environment variables for your topic and verification token:
    
    
    runtime: aspnetcore
    env: flex
    
    runtime_config:
      operating_system: ubuntu22
    
    env_variables:
      TEST_PROJECT_ID: your-project-id
      TEST_VERIFICATION_TOKEN: your-token
      TEST_TOPIC_ID: your-topic
      TEST_SUBSCRIPTION_ID: your-sub
      TEST_AUTH_SUBSCRIPTION_ID: your-auth-sub
      TEST_SERVICE_ACCOUNT_EMAIL: your-service-account-email
    

## Code review

The sample app uses the [Pub/Sub Client Library](https://docs.cloud.google.com/pubsub/docs/reference/libraries).

### Go

The sample app uses the environment variables you set in the `app.yaml` file (`PUBSUB_TOPIC` and `PUBSUB_VERIFICATION_TOKEN`) for configuration.

The messages received by this instance are stored in a slice:
    
    
    messages   []string
    

**Note:** This tutorial is using an instance level global variable, `messages`, to store messages received from Pub/Sub. In production, that should be converted to an external storage solution, such as Firestore.

The `pushHandler` function [receives pushed messages](https://docs.cloud.google.com/pubsub/docs/push), verifies the token, and adds the message to the `messages` slice:
    
    
    func pushHandler(w http.ResponseWriter, r *http.Request) {
    	// Verify the token.
    	if r.URL.Query().Get("token") != token {
    		http.Error(w, "Bad token", http.StatusBadRequest)
    		return
    	}
    	msg := &pushRequest{}
    	if err := json.NewDecoder(r.Body).Decode(msg); err != nil {
    		http.Error(w, fmt.Sprintf("Could not decode body: %v", err), http.StatusBadRequest)
    		return
    	}
    
    	messagesMu.Lock()
    	defer messagesMu.Unlock()
    	// Limit to ten.
    	messages = append(messages, string(msg.Message.Data))
    	if len(messages) > maxMessages {
    		messages = messages[len(messages)-maxMessages:]
    	}
    }

The `publishHandler` function publishes new messages to the topic.
    
    
    func publishHandler(w http.ResponseWriter, r *http.Request) {
    	ctx := context.Background()
    
    	msg := &pubsub.Message{
    		Data: []byte(r.FormValue("payload")),
    	}
    
    	if _, err := topic.Publish(ctx, msg).Get(ctx); err != nil {
    		http.Error(w, fmt.Sprintf("Could not publish message: %v", err), 500)
    		return
    	}
    
    	fmt.Fprint(w, "Message published.")
    }

### Java

The sample app uses the values you set in the `app.yaml` file to configure environment variables. The push request handler uses these values to confirm that the request came from Pub/Sub and originated from a trusted source:
    
    
    String pubsubVerificationToken = System.getenv("PUBSUB_VERIFICATION_TOKEN");
    

The sample app maintains a Cloud Datastore database instance to store messages. The `PubSubPush` servlet receives pushed messages and adds them to the `messageRepository` database instance:

###  version 11/17 
    
    
    @WebServlet(value = "/pubsub/push")
    @MultipartConfig()
    public class PubSubPush extends HttpServlet {
    
      @Override
      public void doPost(HttpServletRequest req, HttpServletResponse resp)
          throws IOException, ServletException {
        String pubsubVerificationToken = System.getenv("PUBSUB_VERIFICATION_TOKEN");
        // Do not process message if request token does not match pubsubVerificationToken
        if (pubsubVerificationToken == null
            || pubsubVerificationToken.compareTo(req.getParameter("token")) != 0) {
          resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
          return;
        }
        // parse message object from "message" field in the request body json
        // decode message data from base64
        Message message = getMessage(req);
        try {
          messageRepository.save(message);
          // 200, 201, 204, 102 status codes are interpreted as success by the Pub/Sub system
          resp.setStatus(HttpServletResponse.SC_OK);
        } catch (Exception e) {
          System.out.println(e);
          resp.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
      }

###  version 8 
    
    
    @WebServlet(value = "/pubsub/push")
    public class PubSubPush extends HttpServlet {
    
      @Override
      public void doPost(HttpServletRequest req, HttpServletResponse resp)
          throws IOException, ServletException {
        String pubsubVerificationToken = System.getenv("PUBSUB_VERIFICATION_TOKEN");
        // Do not process message if request token does not match pubsubVerificationToken
        if (req.getParameter("token").compareTo(pubsubVerificationToken) != 0) {
          resp.setStatus(HttpServletResponse.SC_BAD_REQUEST);
          return;
        }
        // parse message object from "message" field in the request body json
        // decode message data from base64
        Message message = getMessage(req);
        try {
          messageRepository.save(message);
          // 200, 201, 204, 102 status codes are interpreted as success by the Pub/Sub system
          resp.setStatus(HttpServletResponse.SC_OK);
        } catch (Exception e) {
          resp.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
      }

The `PubSubPublish` servlet interacts with the App Engine web app to publish new messages and display received messages:
    
    
    @WebServlet(name = "Publish with PubSub", value = "/pubsub/publish")
    public class PubSubPublish extends HttpServlet {
    
      @Override
      public void doPost(HttpServletRequest req, HttpServletResponse resp)
          throws IOException, ServletException {
        Publisher publisher = this.publisher;
        try {
          String topicId = System.getenv("PUBSUB_TOPIC");
          // create a publisher on the topic
          if (publisher == null) {
            publisher = Publisher.newBuilder(
                ProjectTopicName.of(ServiceOptions.getDefaultProjectId(), topicId))
                .build();
          }
          // construct a pubsub message from the payload
          final String payload = req.getParameter("payload");
          PubsubMessage pubsubMessage =
              PubsubMessage.newBuilder().setData(ByteString.copyFromUtf8(payload)).build();
    
          publisher.publish(pubsubMessage);
          // redirect to home page
          resp.sendRedirect("/");
        } catch (Exception e) {
          resp.sendError(HttpStatus.SC_INTERNAL_SERVER_ERROR, e.getMessage());
        }
      }

### Node.js

The sample app uses the values you set in your `app.yaml` file to configure environment variables. The push request handler uses these values to confirm that the request came from Pub/Sub and originated from a trusted source:
    
    
    // The following environment variables are set by the `app.yaml` file when
    // running on App Engine, but will need to be manually set when running locally.
    var PUBSUB_VERIFICATION_TOKEN = process.env.PUBSUB_VERIFICATION_TOKEN;
    var pubsub = gcloud.pubsub({
        projectId: process.env.GOOGLE_CLOUD_PROJECT
    });
    var topic = pubsub.topic(process.env.PUBSUB_TOPIC);
    

The sample app maintains a global list to store messages received by this instance:
    
    
    // List of all messages received by this instance
    var messages = [];
    

**Note:** This tutorial is using an instance level global variable, `messages`, to store messages received from Pub/Sub. In production, that should be converted to an external storage solution, such as Firestore.

This method [receives pushed messages](https://docs.cloud.google.com/pubsub/docs/push) and adds them to the `messages` global list:
    
    
    app.post('/pubsub/push', jsonBodyParser, (req, res) => {
      if (req.query.token !== PUBSUB_VERIFICATION_TOKEN) {
        res.status(400).send();
        return;
      }
    
      // The message is a unicode string encoded in base64.
      const message = Buffer.from(req.body.message.data, 'base64').toString(
        'utf-8'
      );
    
      messages.push(message);
    
      res.status(200).send();
    });

This method interacts with the App Engine web app to publish new messages and display received messages:
    
    
    app.get('/', (req, res) => {
      res.render('index', {messages, tokens, claims});
    });
    
    app.post('/', formBodyParser, async (req, res, next) => {
      if (!req.body.payload) {
        res.status(400).send('Missing payload');
        return;
      }
    
      const data = Buffer.from(req.body.payload);
      try {
        const messageId = await topic.publishMessage({data});
        res.status(200).send(`Message ${messageId} sent.`);
      } catch (error) {
        next(error);
      }
    });

### PHP

The sample app uses the values you set in the `app.yaml` file to configure environment variables. The push request handler uses these values to confirm that the request came from Pub/Sub and originated from a trusted source:
    
    
    runtime: php
    env: flex
    

The sample app maintains a global list to store messages received by this instance:
    
    
    $messages = [];
    

**Note:** This tutorial is using an instance level global variable, `$messages`, to store messages received from Pub/Sub. In production, that should be converted to an external storage solution, such as Firestore.

The `pull` method retrieves messages from the topic you created and adds them to the messages list:
    
    
    // get PULL pubsub messages
    $pubsub = new PubSubClient([
        'projectId' => $projectId,
    ]);
    $subscription = $pubsub->subscription($subscriptionName);
    $pullMessages = [];
    foreach ($subscription->pull(['returnImmediately' => true]) as $pullMessage) {
        $pullMessages[] = $pullMessage;
        $messages[] = $pullMessage->data();
    }
    // acknowledge PULL messages
    if ($pullMessages) {
        $subscription->acknowledgeBatch($pullMessages);
    }

The `publish` method publishes new messages to the topic:
    
    
    if ($message = (string) $request->getBody()) {
        // Publish the pubsub message to the topic
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $topic = $pubsub->topic($topicName);
        $topic->publish(['data' => $message]);
        return $response->withStatus(204);
    }

### Python

The sample app uses the values you set in the `app.yaml` file to configure environment variables. The push request handler uses these values to confirm that the request came from Pub/Sub and originated from a trusted source:
    
    
    app.config['PUBSUB_VERIFICATION_TOKEN'] = \
        os.environ['PUBSUB_VERIFICATION_TOKEN']
    app.config['PUBSUB_TOPIC'] = os.environ['PUBSUB_TOPIC']
    

The sample app maintains a global list to store messages received by this instance:
    
    
    MESSAGES = []
    

**Note:** This tutorial is using an instance level global variable, `MESSAGES`, to store messages received from Pub/Sub. In production, that should be converted to an external storage solution, such as Firestore.

The `pubsub_push()` method [receives pushed messages](https://docs.cloud.google.com/pubsub/docs/push) and adds them to the `MESSAGES` global list:
    
    
    @app.route("/pubsub/push", methods=["POST"])
    def pubsub_push():
        if request.args.get("token", "") != current_app.config["PUBSUB_VERIFICATION_TOKEN"]:
            return "Invalid request", 400
    
        envelope = json.loads(request.data.decode("utf-8"))
        payload = base64.b64decode(envelope["message"]["data"])
    
        MESSAGES.append(payload)
    
        # Returning any 2xx status indicates successful receipt of the message.
        return "OK", 200
    
    

The `index()` method interacts with the App Engine web app to publish new messages and display received messages:
    
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            return render_template("index.html", messages=MESSAGES)
    
        data = request.form.get("payload", "Example payload").encode("utf-8")
    
        # publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(
            current_app.config["PROJECT"], current_app.config["PUBSUB_TOPIC"]
        )
    
        publisher.publish(topic_path, data=data)
    
        return "OK", 200
    
    

### Ruby

The sample app uses the values you set in the `app.yaml` file to configure environment variables. The push request handler uses these values to confirm that the request came from Pub/Sub and originated from a trusted source:
    
    
    publisher = pubsub.publisher ENV["PUBSUB_TOPIC"]
    PUBSUB_VERIFICATION_TOKEN = ENV["PUBSUB_VERIFICATION_TOKEN"]

The sample app maintains a global list to store messages received by this instance:
    
    
    # List of all messages received by this instance
    messages = []

This method [receives pushed messages](https://docs.cloud.google.com/pubsub/docs/push) and adds them to the `messages` global list:

**Note:** This tutorial is using an instance level global variable, `messages`, to store messages received from Pub/Sub. In production, that should be converted to an external storage solution, such as Firestore.
    
    
    post "/pubsub/push" do
      halt 400 if params[:token] != PUBSUB_VERIFICATION_TOKEN
    
      message = JSON.parse request.body.read
      payload = Base64.decode64 message["message"]["data"]
    
      messages.push payload
    end

This method interacts with the App Engine web app to publish new messages and display received messages:
    
    
    get "/" do
      @claims = claims
      @messages = messages
    
      slim :index
    end
    
    post "/publish" do
      publisher.publish params[:payload]
    
      redirect "/", 303
    end

### .NET

**Note:** This tutorial is using an instance level global variable, `s_receivedMessages`, to store messages received from Pub/Sub. In production, that should be converted to an external storage solution such as Firestore.
    
    
    [HttpGet]
    [HttpPost]
    public async Task<IActionResult> IndexAsync(MessageForm messageForm)
    {
        var model = new MessageList();
        if (!_options.HasGoodProjectId())
        {
            model.MissingProjectId = true;
            return View(model);
        }
        if (!string.IsNullOrEmpty(messageForm.Message))
        {
            // Publish the message.
            var pubsubMessage = new PubsubMessage()
            {
                Data = ByteString.CopyFromUtf8(messageForm.Message)
            };
            pubsubMessage.Attributes["token"] = _options.VerificationToken;
            await _publisher.PublishAsync(pubsubMessage);
            model.PublishedMessage = messageForm.Message;
        }
        // Render the current list of messages.
        model.Messages = s_receivedMessages.ToArray();
        model.AuthMessages = s_authenticatedMessages.ToArray();
        return View(model);
    }
    

## Running the sample locally

When running locally, you can use the Google Cloud CLI to provide authentication to use Google Cloud APIs. Assuming you set up your environment as described in Prerequisites, you have already run the `gcloud init` command, which provides this authentication.

### Go

Set environment variables before starting your application:
    
    
    export GOOGLE_CLOUD_PROJECT=[your-project-id]
    export PUBSUB_VERIFICATION_TOKEN=[your-token]
    export PUBSUB_TOPIC=[your-topic]
    go run pubsub.go
    

### Java
    
    
    mvn clean package
    

Set environment variables before starting your application:
    
    
    export PUBSUB_VERIFICATION_TOKEN=[your-verification-token]
    export PUBSUB_TOPIC=[your-topic]
    mvn jetty:run
    

### Node.js

Set environment variables before starting your application:
    
    
    export GOOGLE_CLOUD_PROJECT=[your-project-id]
    export PUBSUB_VERIFICATION_TOKEN=[your-verification-token]
    export PUBSUB_TOPIC=[your-topic]
    npm install
    npm start
    

### PHP

Install dependencies using Composer:
    
    
    composer install
    

Then set environment variables before starting your application:
    
    
    export GOOGLE_CLOUD_PROJECT=[your-project-id]
    export PUBSUB_VERIFICATION_TOKEN=[your-verification-token]
    export PUBSUB_TOPIC=[your-topic]
    php -S localhost:8080
    

### Python

Install dependencies, preferably in a virtual environment.

### Mac OS / Linux

Note: These instructions describe how to set up a virtual environment in Python 3. For Python 2 apps, use [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv) to set up a virtual environment.

  1. Create an [isolated Python environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv): 
         
         python3 -m venv env
         source env/bin/activate

  2. If you're not in the directory that contains the sample code, navigate to the directory that contains the `hello_world` sample code. Then install dependencies: 
         
         cd YOUR_SAMPLE_CODE_DIR
         pip install -r requirements.txt




### Windows

Note: These instructions describe how to set up a virtual environment in Python 3. For Python 2 apps, use [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv) to set up a virtual environment.

Use PowerShell to run your Python packages.

  1. Locate your installation of [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows). 
  2. Right-click on the shortcut to PowerShell and start it as an administrator.
  3. Create an [isolated Python environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv). 
         
         python -m venv env
         .\env\Scripts\activate

  4. Navigate to your project directory and install dependencies. If you're not in the directory that contains the sample code, navigate to the directory that contains the `hello_world` sample code. Then, install dependencies: 
         
         cd YOUR_SAMPLE_CODE_DIR
         pip install -r requirements.txt




Then set environment variables before starting your application:
    
    
    export GOOGLE_CLOUD_PROJECT=[your-project-id]
    export PUBSUB_VERIFICATION_TOKEN=[your-verification-token]
    export PUBSUB_TOPIC=[your-topic]
    python main.py
    

### Ruby

Install dependencies:
    
    
    bundle install
    

Then set environment variables before starting your application:
    
    
    export GOOGLE_CLOUD_PROJECT=[your-project-id]
    export PUBSUB_VERIFICATION_TOKEN=[your-verification-token]
    export PUBSUB_TOPIC=[your-topic]
    bundle exec ruby app.rb -p 8080
    

### .NET

Run the following commands from the root directory of your application:
    
    
        dotnet restore
        dotnet run
    

In your web browser, enter http://localhost:5000/. To exit the web server, press Ctrl+C in your terminal window.

### Simulating push notifications

The application can send messages locally, but it is not able to receive push messages locally. You can, however, simulate a push message by making an HTTP request to the local push notification endpoint. The sample includes the file `sample_message.json`.

### Go

You can use `curl` or a [`httpie`](https://github.com/jkbrzt/httpie) client to send an HTTP `POST` request:
    
    
    curl -H "Content-Type: application/json" -i --data @sample_message.json "localhost:8080/push-handlers/receive_messages?token=[your-token]"
    

Or
    
    
    http POST ":8080/push-handlers/receive_messages?token=[your-token]" < sample_message.json
    

Response:
    
    
    HTTP/1.1 200 OK
    Date: Tue, 13 Nov 2018 16:04:18 GMT
    Content-Length: 0
    

After the request completes, you can refresh `localhost:8080` and see the message in the list of received messages.

### Java

You can use `curl` or a [`httpie`](https://github.com/jkbrzt/httpie) client to send an HTTP `POST` request:
    
    
    curl -H "Content-Type: application/json" -i --data @sample_message.json "localhost:8080/push-handlers/receive_messages?token=[your-token]"
    

Or
    
    
    http POST ":8080/push-handlers/receive_messages?token=[your-token]" < sample_message.json
    

Response:
    
    
    HTTP/1.1 200 OK
    Date: Wed, 26 Apr 2017 00:03:28 GMT
    Content-Length: 0
    Server: Jetty(9.3.8.v20160314)
    

After the request completes, you can refresh `localhost:8080` and see the message in the list of received messages.

### Node.js

You can use `curl` or a [`httpie`](https://github.com/jkbrzt/httpie) client to send an HTTP `POST` request:
    
    
    curl -H "Content-Type: application/json" -i --data @sample_message.json "localhost:8080/push-handlers/receive_messages?token=[your-token]"
    

Or
    
    
    http POST ":8080/push-handlers/receive_messages?token=[your-token]" < sample_message.json
    

Response:
    
    
    HTTP/1.1 200 OK
    Connection: keep-alive
    Date: Mon, 31 Aug 2015 22:19:50 GMT
    Transfer-Encoding: chunked
    X-Powered-By: Express
    

After the request completes, you can refresh `localhost:8080` and see the message in the list of received messages.

### PHP

You can use `curl` or a [`httpie`](https://github.com/jkbrzt/httpie) client to send an HTTP `POST` request:
    
    
    curl -i --data @sample_message.json "localhost:4567/push-handlers/receive_messages?token=[your-token]"
    

Or
    
    
    http POST ":4567/push-handlers/receive_messages?token=[your-token]" < sample_message.json
    

After the request completes, you can refresh `localhost:8080` and see the message in the list of received messages.

### Python

You can use `curl` or a [`httpie`](https://github.com/jkbrzt/httpie) client to send an HTTP `POST` request:
    
    
    curl -H "Content-Type: application/json" -i --data @sample_message.json "localhost:8080/pubsub/push?token=[your-token]"
    

Or
    
    
    http POST ":8080/pubsub/push?token=[your-token]" < sample_message.json
    

Response:
    
    
    HTTP/1.0 200 OK
    Content-Length: 2
    Content-Type: text/html; charset=utf-8
    Date: Mon, 10 Aug 2015 17:52:03 GMT
    Server: Werkzeug/0.10.4 Python/2.7.10
    
    OK
    

After the request completes, you can refresh `localhost:8080` and see the message in the list of received messages.

### Ruby

You can use `curl` or a [`httpie`](https://github.com/jkbrzt/httpie) client to send an HTTP `POST` request:
    
    
    curl -i --data @sample_message.json "localhost:4567/push-handlers/receive_messages?token=[your-token]"
    

Or
    
    
    http POST ":4567/push-handlers/receive_messages?token=[your-token]" < sample_message.json
    

Response:
    
    
    HTTP/1.1 200 OK
    Content-Type: text/html;charset=utf-8
    Content-Length: 13
    X-Xss-Protection: 1; mode=block
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN
    Server: WEBrick/1.3.1 (Ruby/2.3.0/2015-12-25)
    Date: Wed, 20 Apr 2016 20:56:23 GMT
    Connection: Keep-Alive
    
    Hello, World!
    

After the request completes, you can refresh `localhost:8080` and see the message in the list of received messages.

### .NET

To send an HTTP `POST` request:
    
    
    Get-Content -Raw .\sample_message.json | Invoke-WebRequest -Uri
    http://localhost:5000/Push?token=your-secret-token -Method POST -ContentType
    'text/json' -OutFile out.txt
    

After the request completes, you can refresh `localhost:5000` and see the message in the list of received messages.

## Running on App Engine

To deploy the demo app to App Engine using the `gcloud` command-line tool:

### Go

Run the following command from the directory where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

### Java

To deploy your app using Maven, run the following:
    
    
    mvn package appengine:deploy -Dapp.deploy.projectId=PROJECT_ID

Replace PROJECT_ID with the ID of your Google Cloud project. If your `pom.xml` file already [specifies your project ID](https://docs.cloud.google.com/appengine/docs/flexible/java/maven-reference#appenginedeploy), you don't need to include the `-Dapp.deploy.projectId` property in the command you run. 

### Node.js

Run the following command from the directory where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

### PHP

Run the following command from the directory where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

### Python

Run the following command from the directory where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

### Ruby

Run the following command from the directory where your `app.yaml` file is located:
    
    
    gcloud app deploy app.yaml
    

### .NET

Run the following command from the directory where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

You can now access the application at `https://PROJECT_ID.REGION_ID.r.appspot.com`. You can use the form to submit messages, but there's no guarantee of which instance of your application will receive the notification. You can send multiple messages and refresh the page to see the received message.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
