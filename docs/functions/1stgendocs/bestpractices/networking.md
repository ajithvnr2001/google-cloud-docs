---
url: https://docs.cloud.google.com/functions/1stgendocs/bestpractices/networking/
title: Optimize networking (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.209238+00:00
---

# Optimize networking (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/bestpractices/networking/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Optimize networking (1st gen)

**Note:** This content applies only to Cloud Run functions (1st gen)—formerly Cloud Functions (1st gen). 

For the Cloud Run version of this document, see [Optimize networking](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices). 

The simplicity of Cloud Run functions lets you quickly develop code and run it in a serverless environment. At moderate scale, the cost of running functions is low, and optimizing your code might not seem like a high priority. As your deployment scales up, however, optimizing your code becomes increasingly important.

This document describes how to optimize networking for your functions. Some of the benefits of optimizing networking are as follows:

  * Reduce CPU time spent in establishing new connections at each function call.
  * Reduce the likelihood of running out of connection or DNS [quotas](https://docs.cloud.google.com/functions/quotas).



## Maintain Persistent Connections

This section gives examples of how to maintain persistent connections in a function. Failure to do so can result in quickly exhausting connection quotas.

The following scenarios are covered in this section:

  * HTTP/S
  * Google APIs



### HTTP/S Requests

The following optimized code snippet shows how to maintain persistent connections instead of creating a new connection upon every function invocation:

###  Node.js 
    
    
    const fetch = require('node-fetch');
    
    const http = require('http');
    const https = require('https');
    
    const functions = require('@google-cloud/functions-framework');
    
    const httpAgent = new http.Agent({keepAlive: true});
    const httpsAgent = new https.Agent({keepAlive: true});
    
    /**
     * HTTP Cloud Function that caches an HTTP agent to pool HTTP connections.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('connectionPooling', async (req, res) => {
      try {
        // TODO(optional): replace this with your own URL.
        const url = 'https://www.example.com/';
    
        // Select the appropriate agent to use based on the URL.
        const agent = url.includes('https') ? httpsAgent : httpAgent;
    
        const fetchResponse = await fetch(url, {agent});
        const text = await fetchResponse.text();
    
        res.status(200).send(`Data: ${text}`);
      } catch (err) {
        res.status(500).send(`Error: ${err.message}`);
      }
    });

###  Python 
    
    
    import functions_framework
    import requests
    
    # Create a global HTTP session (which provides connection pooling)
    session = requests.Session()
    
    
    @functions_framework.http
    def connection_pooling(request):
        """
        HTTP Cloud Function that uses a connection pool to make HTTP requests.
        Args:
            request (flask.Request): The request object.
            <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
    
        # The URL to send the request to
        url = "http://example.com"
    
        # Process the request
        response = session.get(url)
        response.raise_for_status()
        return "Success!"
    
    

###  Go 
    
    
    // Package http provides a set of HTTP Cloud Functions samples.
    package http
    
    import (
    	"fmt"
    	"net/http"
    	"time"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    var urlString = "https://example.com"
    
    // client is used to make HTTP requests with a 10 second timeout.
    // http.Clients should be reused instead of created as needed.
    var client = &http.Client{
    	Timeout: 10 * time.Second,
    }
    
    func init() {
    	functions.HTTP("MakeRequest", MakeRequest)
    }
    
    // MakeRequest is an example of making an HTTP request. MakeRequest uses a
    // single http.Client for all requests to take advantage of connection
    // pooling and caching. See https://godoc.org/net/http#Client.
    func MakeRequest(w http.ResponseWriter, r *http.Request) {
    	resp, err := client.Get(urlString)
    	if err != nil {
    		http.Error(w, "Error making request", http.StatusInternalServerError)
    		return
    	}
    	if resp.StatusCode != http.StatusOK {
    		msg := fmt.Sprintf("Bad StatusCode: %d", resp.StatusCode)
    		http.Error(w, msg, http.StatusInternalServerError)
    		return
    	}
    	fmt.Fprintf(w, "ok")
    }
    

###  PHP 

We recommend using the [Guzzle PHP HTTP Framework](https://docs.guzzlephp.org/en/stable/) to send HTTP requests, as it handles persistent connections [automatically](https://docs.guzzlephp.org/en/5.3/faq.html#why-should-i-use-guzzle). 

### Accessing Google APIs

The following example uses [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub/docs/reference/libraries), but this approach also works for other client libraries; for example, [Cloud Natural Language](https://docs.cloud.google.com/natural-language/docs/reference/libraries) or [Cloud Spanner](https://docs.cloud.google.com/spanner/docs/reference/libraries). Note that performance improvements may depend on the current implementation of particular client libraries.

Creating a Pub/Sub client object results in one connection and two DNS queries per invocation. To avoid unnecessary connections and DNS queries, create the Pub/Sub client object in global scope as shown in the following sample:

###  Node.js 
    
    
    const functions = require('@google-cloud/functions-framework');
    const {PubSub} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    const pubsub = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    /**
     * HTTP Cloud Function that uses a cached client library instance to
     * reduce the number of connections required per function invocation.
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} req.body Cloud Function request context body.
     * @param {String} req.body.topic The Cloud Pub/Sub topic to publish to.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('gcpApiCall', (req, res) => {
      const topic = pubsub.topic(req.body.topic);
    
      const data = Buffer.from('Test message');
      topic.publishMessage({data}, err => {
        if (err) {
          res.status(500).send(`Error publishing the message: ${err}`);
        } else {
          res.status(200).send('1 message published');
        }
      });
    });

###  Python 
    
    
    import os
    
    import functions_framework
    from google.cloud import pubsub_v1
    
    
    # Create a global Pub/Sub client to avoid unneeded network activity
    pubsub = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    
    
    @functions_framework.http
    def gcp_api_call(request):
        """
        HTTP Cloud Function that uses a cached client library instance to
        reduce the number of connections required per function invocation.
        Args:
            request (flask.Request): The request object.
        Returns:
            The response text, or any set of values that can be turned into a
            Response object using `make_response`
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
        """
    
        """
        The `GCP_PROJECT` environment variable is set automatically in the Python 3.7 runtime.
        In later runtimes, it must be specified by the user upon function deployment.
        See this page for more information:
            https://cloud.google.com/functions/docs/configuring/env-var#python_37_and_go_111
        """
        project = os.getenv("GCP_PROJECT")
        request_json = request.get_json()
    
        topic_name = request_json["topic"]
        topic_path = pubsub.topic_path(project, topic_name)
    
        # Process the request
        data = b"Test message"
        pubsub.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data=data)
    
        return "1 message published"
    
    

###  Go 
    
    
    // Package contexttip is an example of how to use Pub/Sub and context.Context in
    // a Cloud Function.
    package contexttip
    import (
        "context"
        "encoding/json"
        "fmt"
        "log"
        "net/http"
        "os"
        "sync"
        "cloud.google.com/go/pubsub"
        "github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    // client is a global Pub/Sub client, initialized once per instance.
    var client *pubsub.[Client](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client)
    var once sync.Once
    // createClient creates the global pubsub Client
    func createClient() {
        // GOOGLE_CLOUD_PROJECT is a user-set environment variable.
        var projectID = os.Getenv("GOOGLE_CLOUD_PROJECT")
        // err is pre-declared to avoid shadowing client.
        var err error
        // client is initialized with context.Background() because it should
        // persist between function invocations.
        client, err = pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(context.Background(), projectID)
        if err != nil {
            log.Fatalf("pubsub.NewClient: %v", err)
        }
    }
    func init() {
        // register http function
        functions.HTTP("PublishMessage", PublishMessage)
    }
    type publishRequest struct {
        Topic   string json:"topic"
        Message string json:"message"
    }
    // PublishMessage publishes a message to Pub/Sub. PublishMessage only works
    // with topics that already exist.
    func PublishMessage(w http.ResponseWriter, r *http.Request) {
        // use of sync.Once ensures client is only created once.
        once.Do(createClient)
        // Parse the request body to get the topic name and message.
        p := publishRequest{}
        if err := json.NewDecoder(r.Body).Decode(&p); err != nil {
            log.Printf("json.NewDecoder: %v", err)
            http.Error(w, "Error parsing request", http.StatusBadRequest)
            return
        }
        if p.Topic == "" || p.Message == "" {
            s := "missing 'topic' or 'message' parameter"
            log.Println(s)
            http.Error(w, s, http.StatusBadRequest)
            return
        }
        m := &pubsub.Message{
            Data: []byte(p.Message),
        }
        // Publish and Get use r.Context() because they are only needed for this
        // function invocation. If this were a background function, they would use
        // the ctx passed as an argument.
        id, err := client.Topic(p.Topic).Publish(r.Context(), m).Get(r.Context())
        if err != nil {
            log.Printf("topic(%s).Publish.Get: %v", p.Topic, err)
            http.Error(w, "Error publishing message", http.StatusInternalServerError)
            return
        }
        fmt.Fprintf(w, "Message published: %v", id)
    }

### Outbound connection resets

Connection streams from your function to both [VPC](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc) and internet can be occasionally terminated and replaced when underlying infrastructure is restarted or updated. If your application reuses long-lived connections, we recommend that you configure your application to re-establish connections to avoid the reuse of a dead connection.

### Outbound request timeouts

Outbound sockets may be reclaimed after 10 minutes of inactivity. Any socket operation keeps the socket alive for a further 10 minutes.

## Load test your function

To measure how many connections your function performs on average, deploy it as a HTTP function and use a performance-testing framework to invoke it at certain QPS. One possible choice is [Artillery](https://artillery.io/), which you can invoke with a single line:
    
    
    $ artillery quick -d 300 -r 30 URL

This command fetches the given URL at 30 QPS for 300 seconds.

After performing the test, check the usage of your connection quota on the [Cloud Run functions API quota page](https://console.cloud.google.com/apis/api/cloudfunctions.googleapis.com/quotas) in Google Cloud console. If the usage is consistently around 30 (or its multiple), you are establishing one (or several) connections in every invocation. After you optimize your code, you should see a few (10-30) connections occur only at the beginning of the test.

You can also compare the CPU cost before and after the optimization on the CPU quota plot on the same page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
