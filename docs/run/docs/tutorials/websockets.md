---
url: https://docs.cloud.google.com/run/docs/tutorials/websockets/
title: Building a WebSocket Chat service for Cloud Run tutorial \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:54.341106+00:00
---

# Building a WebSocket Chat service for Cloud Run tutorial  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tutorials/websockets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Building a WebSocket Chat service for Cloud Run tutorial Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to create a multi-room, realtime chat service using WebSockets with a persistent connection for bidirectional communication. With WebSockets, both client and server can push messages to each other without polling the server for updates.

Although you can configure Cloud Run to use [session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity), this provides a _best effort_ affinity, which means that any new request can still be potentially routed to a different instance. As a result, user messages in the chat service need to be synchronized across all instances, not just between the clients connected to one instance.

## Design for a realtime chat service

This sample chat service uses a Memorystore for Redis instance to store and synchronize user messages across all instances. Redis uses a [Pub/Sub](https://redis.io/topics/pubsub) mechanism, not to be confused with the product [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs), to push data to subscribed clients connected to any instance, to eliminate HTTP polling for updates.

However, even with push updates, any instance that is spun up will only receive new messages pushed to the container. To load prior messages, message history would need to be stored and retrieved from a persistent storage solution. This sample uses Redis's conventional functionality of an object store to cache and retrieve message history.

The Redis instance is protected from the internet using private IPs with access controlled and limited to services running on the same Virtual Private Network as the Redis instance. We recommend that you use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

## Limitations

  * This tutorial does not show end user authentication or session caching. To learn more about end user authentication, refer to the Cloud Run tutorial for [end user authentication](https://docs.cloud.google.com/run/docs/tutorials/identity-platform).

  * This tutorial does not implement a database such as Firestore for indefinite storage and retrieval of chat message history.

  * Additional elements are needed for this sample service to be production ready. A [Standard Tier Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers) is recommended to provide [High Availability](https://docs.cloud.google.com/memorystore/docs/redis/high-availability) using replication and automatic failover.




## Objectives

  * Write, build, and deploy a Cloud Run service that uses WebSockets.

  * Connect to a Memorystore for Redis instance to publish and subscribe to new messages across instances.

  * Connect the Cloud Run service with Memorystore using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).




## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Cloud Run](https://cloud.google.com/run)



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

  6. Enable the Cloud Run, Memorystore for Redis, Artifact Registry, and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,redis.googleapis.com,vpcaccess.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com)

  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).



### Required roles

To get the permissions that you need to complete the tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Cloud Memorystore Redis Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/redis#redis.admin) (`roles/redis.admin`)
  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete the tutorial. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Set up gcloud defaults

To configure gcloud with defaults for your Cloud Run service:

  1. Set your default project:
         
         gcloud config set project PROJECT_ID

Replace PROJECT_ID with the name of the project you created for this tutorial.

  2. Configure gcloud for your chosen region:
         
         gcloud config set run/region REGION

Replace REGION with the supported Cloud Run region of your choice.




### Cloud Run locations

Cloud Run is regional, which means the infrastructure that runs your Cloud Run services is located in a specific region and is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).   
  


Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your Cloud Run services are run. You can generally select the region nearest to your users but you should consider the location of the [other Google Cloud products](https://cloud.google.com/about/locations/#locations) that are used by your Cloud Run service. Using Google Cloud products together across multiple locations can affect your service's latency as well as cost.  
  


Cloud Run is available in the following regions:

#### Subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables)

  * `asia-east1` (Taiwan) 
  * `asia-northeast1` (Tokyo) 
  * `asia-northeast2` (Osaka) 
  * `asia-south1` (Mumbai, India) 
  * `asia-southeast3 ` (Bangkok) 
  * `europe-north1` (Finland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-north2` (Stockholm) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-southwest1` (Madrid) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west8` (Milan) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west9` (Paris) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-west1` (Tel Aviv) 
  * `northamerica-south1` (Mexico) 
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-east1` (South Carolina) 
  * `us-east4` (Northern Virginia) 
  * `us-east5` (Columbus) 
  * `us-south1` (Dallas) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west1` (Oregon) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



#### Subject to [Tier 2 pricing](https://cloud.google.com/run/pricing#tables)

  * `africa-south1` (Johannesburg) 
  * `asia-east2` (Hong Kong) 
  * `asia-northeast3` (Seoul, South Korea) 
  * `asia-southeast1` (Singapore) 
  * `asia-southeast2 ` (Jakarta) 
  * `asia-south2` (Delhi, India) 
  * `australia-southeast1` (Sydney) 
  * `australia-southeast2` (Melbourne) 
  * `europe-central2` (Warsaw, Poland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west10` (Berlin) 
  * `europe-west12` (Turin) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west2` (London, UK) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west3` (Frankfurt, Germany) 
  * `europe-west6` (Zurich, Switzerland) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `me-central1` (Doha) 
  * `me-central2` (Dammam) 
  * `northamerica-northeast1` (Montreal) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `northamerica-northeast2` (Toronto) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-east1` (Sao Paulo, Brazil) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `southamerica-west1` (Santiago, Chile) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-west2` (Los Angeles) 
  * `us-west3` (Salt Lake City) 
  * `us-west4` (Las Vegas) 



If you already created a Cloud Run service, you can view the region in the Cloud Run dashboard in the [Google Cloud console](https://console.cloud.google.com/run).

OK

## Retrieve the code sample

To retrieve the code sample for use:

  1. Clone the sample repository to your local machine:

###  Node.js 
         
         git clone https://github.com/GoogleCloudPlatform/nodejs-docs-samples.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the Cloud Run sample code:

###  Node.js 
         
         cd nodejs-docs-samples/run/websockets/




## Understand the WebSockets code

Socket.io is a library that enables real time, bidirectional communication between the browser and server. Although Socket.io is not a WebSocket implementation, it does wrap the functionality to provide a simpler API for multiple communication protocols with additional [features](https://socket.io/docs/v3/#Features) such as improved reliability, [automatic reconnection](https://docs.cloud.google.com/run/docs/triggering/websockets#client-reconnects), and broadcasting to all or a subset of clients.

### Client-side integration
    
    
    <script src="/socket.io/socket.io.js"></script>

The client instantiates a new [Socket instance](https://socket.io/docs/v3/client-socket-instance/) for every connection. Because this sample is server side rendered the server URL does not need to be defined. The socket instance can emit and listen to events.
    
    
    // Initialize Socket.io
    const socket = io('', {
      transports: ['websocket'],
    });
    
    
    // Emit "sendMessage" event with message
    socket.emit('sendMessage', msg, error => {
      if (error) {
        console.error(error);
      } else {
        // Clear message
        $('#msg').val('');
      }
    });
    
    
    // Listen for new messages
    socket.on('message', msg => {
      log(msg.user, msg.text);
    });
    
    // Listen for notifications
    socket.on('notification', msg => {
      log(msg.title, msg.description);
    });
    
    // Listen connect event
    socket.on('connect', () => {
      console.log('connected');
    });

**Note:** For a [multiple instances](https://socket.io/docs/v4/using-multiple-nodes/) architecture without session affinity, Socket.io must only use the Websocket transport. If Socket.io falls back to long polling, it will send multiple HTTP requests during the lifetime of the session. The first request establishes a "[handshake](https://socket.io/docs/v4/how-it-works/#Handshake)" with important information such as the session ID. After the first request, requests might be routed to another instance that will generate an error due to the session ID being unknown to the server.

### Server-side integration

On the server side, the Socket.io server is initialized and attached to the HTTP server. Similar to the client side, once the Socket.io server makes a connection to the client, a socket instance is created for every connection which can be used to emit and listen to messages. Socket.io also provides an interface for creating "rooms" or an arbitrary channel that sockets can join and leave.
    
    
    // Initialize Socket.io
    const server = require('http').Server(app);
    const io = require('socket.io')(server);
    
    const {createAdapter} = require('@socket.io/redis-adapter');
    // Replace in-memory adapter with Redis
    const subClient = redisClient.duplicate();
    io.adapter(createAdapter(redisClient, subClient));
    // Add error handlers
    redisClient.on('error', err => {
      console.error(err.message);
    });
    
    subClient.on('error', err => {
      console.error(err.message);
    });
    
    // Listen for new connection
    io.on('connection', socket => {
      // Add listener for "signin" event
      socket.on('signin', async ({user, room}, callback) => {
        try {
          // Record socket ID to user's name and chat room
          addUser(socket.id, user, room);
          // Call join to subscribe the socket to a given channel
          socket.join(room);
          // Emit notification event
          socket.in(room).emit('notification', {
            title: "Someone's here",
            description: `${user} just entered the room`,
          });
          // Retrieve room's message history or return null
          const messages = await getRoomFromCache(room);
          // Use the callback to respond with the room's message history
          // Callbacks are more commonly used for event listeners than promises
          callback(null, messages);
        } catch (err) {
          callback(err, null);
        }
      });
    
      // Add listener for "updateSocketId" event
      socket.on('updateSocketId', async ({user, room}) => {
        try {
          addUser(socket.id, user, room);
          socket.join(room);
        } catch (err) {
          console.error(err);
        }
      });
    
      // Add listener for "sendMessage" event
      socket.on('sendMessage', (message, callback) => {
        // Retrieve user's name and chat room  from socket ID
        const {user, room} = getUser(socket.id);
        if (room) {
          const msg = {user, text: message};
          // Push message to clients in chat room
          io.in(room).emit('message', msg);
          addMessageToCache(room, msg);
          callback();
        } else {
          callback('User session not found.');
        }
      });
    
      // Add listener for disconnection
      socket.on('disconnect', () => {
        // Remove socket ID from list
        const {user, room} = deleteUser(socket.id);
        if (user) {
          io.in(room).emit('notification', {
            title: 'Someone just left',
            description: `${user} just left the room`,
          });
        }
      });
    });

Socket.io also provides a Redis adapter to broadcast events to all clients regardless of which server is serving the socket. Socket.io only uses Redis's Pub/Sub mechanism and does not store any data.
    
    
    const {createAdapter} = require('@socket.io/redis-adapter');
    // Replace in-memory adapter with Redis
    const subClient = redisClient.duplicate();
    io.adapter(createAdapter(redisClient, subClient));

Socket.io's Redis adapter can reuse the Redis client used to store the room's message history. Each container will create a connection to the Redis instance and Cloud Run can create a large number of instances. This is well under the 65,000 connections that Redis can support.

**Note:** The [Cloud Run container lifecycle](https://cloud.google.com/blog/topics/developers-practitioners/lifecycle-container-cloud-run) does not take into consideration outbound requests such as Redis connections; therefore an active connection to Redis won't prevent the container from scaling in.

### Reconnection

Cloud Run has a maximum timeout of 60 minutes. So you need to add reconnection logic for possible timeouts. In some cases, Socket.io automatically attempts to reconnect after [disconnection or connection error](https://socket.io/docs/v3/client-socket-instance/) events. There is no guarantee that the client will reconnect to the same instance.
    
    
    // Listen for reconnect event
    socket.io.on('reconnect', () => {
      console.log('reconnected');
      // Emit "updateSocketId" event to update the recorded socket ID with user and room
      socket.emit('updateSocketId', {user, room}, error => {
        if (error) {
          console.error(error);
        }
      });
    });
    
    
    // Add listener for "updateSocketId" event
    socket.on('updateSocketId', async ({user, room}) => {
      try {
        addUser(socket.id, user, room);
        socket.join(room);
      } catch (err) {
        console.error(err);
      }
    });

Instances will persist if there is an active connection until all requests close or time out. Even if you use Cloud Run [session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity), it is possible for new requests to be load balanced to active containers, which allows containers to scale in. If you are concerned about large numbers of containers persisting after a spike in traffic, you can lower the maximum timeout value, so that unused sockets are cleaned up more frequently.

## Ship the service

  1. Create a Memorystore for Redis instance:
         
         gcloud redis instances create INSTANCE_ID --size=1 --region=REGION

Replace the following:

     * INSTANCE_ID: the name for the instance—for example, `my-redis-instance`.
     * REGION_ID: the [region](https://docs.cloud.google.com/run/docs/locations) for all your resources and services—for example, `europe-west1`.

Instance will be automatically allocated an IP range from the default service network range. This tutorial uses 1GB of memory for the local cache of messages in the Redis instance. Learn more about [Determining the initial size of a Memorystore instance](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices#determine_the_initial_size_of_a_cloud_memorystore_instance) for your use case.

  2. Define an environment variable with the IP address of your Redis instance's authorized network:
         
         export REDISHOST=$(gcloud redis instances describe INSTANCE_ID --region REGION --format "value(host)")

**Note:** This tutorial uses the default value for the Redis port, `6379`.
  3. Create a service account to serve as the service identity. By default this has no privileges other than project membership.
         
         gcloud iam service-accounts create chat-identity
         gcloud projects add-iam-policy-binding PROJECT_ID \
         --member=serviceAccount:chat-identity@PROJECT_ID.iam.gserviceaccount.com \
         --role=roles/serviceusage.serviceUsageConsumer

  4. Find the name of your Redis instance-authorized VPC network by running the following command:
         
         gcloud redis instances describe INSTANCE_ID --region REGION --format "value(authorizedNetwork)"
         

Replace the following:

     * INSTANCE_ID: the name for the instance—for example, `my-redis-instance`.
     * REGION_ID: the [region](https://docs.cloud.google.com/run/docs/locations) for all your resources and services—for example, `europe-west1`.

Make note of the VPC network name.

  5. Build and deploy the container image to Cloud Run:
         
         gcloud run deploy chat-app --source . \
             --allow-unauthenticated \
             --timeout 3600 \
             --service-account chat-identity \
             --network NETWORK \
             --subnet SUBNET \
             --update-env-vars REDISHOST=$REDISHOST

Replace the following:

     * NETWORK is the name of the authorized VPC network that your Redis instance is attached to.
     * SUBNET is the name of your subnet. The subnet must be `/26` or larger. Direct VPC egress supports IPv4 ranges [RFC 1918](https://tools.ietf.org/html/rfc1918#section-3), [RFC 6598](https://tools.ietf.org/html/rfc6598#section-7), and Class E.

Respond to any prompts to install required APIs by responding `y` when prompted. You only need to do this once for a project. Respond to other prompts by supplying the platform and region, if you haven't set defaults for these as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page. Learn more about [Deploying from source code](https://docs.cloud.google.com/run/docs/deploying-source-code).




## Try the service

To try out the complete service:

  1. Navigate your browser to the URL provided by the deployment step.

  2. Add your name and a chat room to sign in.

  3. Send a message to the room!


**Success:** You built a multi-room, real-time chat service using WebSockets to maintain a persistent connection for bi-directional communication.

If you choose to continue developing these services, remember that they have restricted Identity and Access Management (IAM) access to the rest of Google Cloud and will need to be given additional IAM roles to access many other services.

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
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the service container image](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#deleting_images) named `gcr.io/PROJECT_ID/chat-app` from Artifact Registry
     * [Delete the service account `chat-identity@PROJECT_ID.iam.gserviceaccount.com`](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-delete-gcloud)
     * [Delete the Memorystore for Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/creating-managing-instances#deleting_instances)



## What's next

  * Learn more about [how Socket.io works](https://socket.io/docs/v4/how-it-works/) and more advanced usage.

  * Dive deeper into [Direct VPC egress with a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

  * Review best practices for [Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices) and for [Using WebSockets on Cloud Run](https://docs.cloud.google.com/run/docs/triggering/websockets#client-reconnects).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
