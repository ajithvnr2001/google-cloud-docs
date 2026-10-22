---
url: https://docs.cloud.google.com/appengine/docs/flexible/using-websockets-and-session-affinity/
title: Creating persistent connections with WebSockets \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:25.878742+00:00
---

# Creating persistent connections with WebSockets  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/using-websockets-and-session-affinity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Creating persistent connections with WebSockets Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

You can use WebSockets to create a persistent connection from a client (such as a mobile device or a computer) to an App Engine instance. The open connection allows two-way data exchange between the client and the server at any time, resulting in lower latency and better use of resources.

## WebSockets

The WebSockets protocol, defined in [RFC 6455](https://tools.ietf.org/html/rfc6455), provides a full-duplex communication channel between a client and a server. The channel is initiated from an HTTP(S) request with an "upgrade" header.

Typical use cases for WebSockets include:

  * Real time event updates, such as social media feeds, sports scores, news, or stock market prices
  * User notifications, such as software or content updates
  * Chatting applications
  * Collaborative editing tools
  * Multiplayer games



WebSockets are always available to your application without any additional setup. Once a WebSockets connection is established, it will time out after one hour. Usage of the WebSocket is [billed by connection usage](https://cloud.google.com/appengine/pricing#managing) until timeout or socket termination.

## Running a sample application with WebSockets

The code samples in this document describe how to run a sample application with Websockets. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) version of Python by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) file. 

### Prerequisites and setup

Follow the instructions in [Setting Up Your Development Environment ](https://docs.cloud.google.com/appengine/docs/flexible/setting-up-environment) to set up your environment and project, and to understand how apps are structured.

### Clone the sample app

Copy the sample apps to your local machine, and navigate to the `websockets` directory:
    
    
    git clone https://github.com/GoogleCloudPlatform/python-docs-samples
    cd python-docs-samples/appengine/flexible/websockets/
    

### Run the sample locally

To run locally, you need to use [Gunicorn](http://gunicorn.org/) with the `flask_socket` worker:
    
    
    $ gunicorn -b 127.0.0.1:8080 -k flask_sockets.worker main:app
    

### Deploy and run the sample on App Engine

To deploy your application to the App Engine flexible environment, run the following command from the directory where your `app.yaml` is located:
    
    
    gcloud app deploy
    

You can then direct your browser to `https://PROJECT_ID.REGION_ID.r.appspot.com`

## Session affinity

Not all clients support WebSockets. To work around this, many applications use libraries such as [socket.io](http://socket.io/) that fall back on http long polling with clients that don't support WebSockets.

App Engine typically distributes requests evenly among available instances. However, when using http long polling, multiple sequential requests from a given user need to reach the same instance.

To allow App Engine to send requests by the same user to the same instance, you can enable session affinity. App Engine then identifies which requests are sent by the same users by inspecting a cookie and routes those requests to the same instance.

**Important:** App Engine applications must always be tolerant of session affinity interruptions, particularly because all App Engine instances are periodically restarted. Enabling session affinity can also limit the effectiveness of App Engine's load balancing algorithms and can cause your instance to become overloaded.

Session affinity in App Engine is implemented on a best-effort basis. When developing your app, you should always assume that session affinity is not guaranteed. A client can lose affinity with the target instance in the following scenarios:

  * The App Engine autoscaler can add or remove instances that serve your application. The application might reallocate the load, and the target instance might move. To minimize this risk, ensure that you have set the minimum number of instances to handle the expected load.
  * If the target instance fails health checks, App Engine moves the session to a healthy instance. For more information about health checks and their customization options, see [Split health checks](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#updated_health_checks).
  * Session affinity is lost when an instance is rebooted for maintenance or software updates. App Engine flexible environment VM instances are restarted on a weekly basis.



Because session affinity isn't guaranteed, you should only use it to take advantage of the ability of `socket.io` and other libraries to fall back on HTTP long polling in cases where the connection is broken. You should never use session affinity to build stateful applications.

## Enabling and disabling session affinity

**Important:** To take advantage of session affinity, cookies must be enabled for all clients that are accessing your application, such as end-user web browsers and API clients. Clients without cookie support cannot take advantage of session affinity.

By default, session affinity is disabled for all App Engine applications. Session affinity is set at the version level of your application and can be enabled or disabled on deployment.

To enable session affinity for your App Engine version, add the following entry to your `app.yaml` file:
    
    
    network:
      session_affinity: true
    

Once the version is deployed with the updated app.yaml, new requests will start serving from the same instance as long as that instance is available.

To turn off session affinity, remove the entry from your [`app.yaml` file](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#network_settings), or set the value to false:
    
    
    network:
      session_affinity: false
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
