---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-imageproc-controller/
title: Pub/Sub handler to process Cloud Storage events \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:27.451233+00:00
---

# Pub/Sub handler to process Cloud Storage events  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-imageproc-controller/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Pub/Sub handler to process Cloud Storage events Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates using Cloud Run, Cloud Vision API, and ImageMagick to detect and blur offensive images uploaded to a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Process images from Cloud Storage tutorial](https://docs.cloud.google.com/run/docs/tutorials/image-processing)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample image-processing is a Cloud Run service which performs asynchronous processing on images.
    package main
    
    import (
    	"encoding/json"
    	"io"
    	"log"
    	"net/http"
    	"os"
    
    	"github.com/GoogleCloudPlatform/golang-samples/run/image-processing/imagemagick"
    )
    
    func main() {
    	http.HandleFunc("/", HelloPubSub)
    	// Determine port for HTTP service.
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    	}
    	// Start HTTP server.
    	log.Printf("Listening on port %s", port)
    	if err := http.ListenAndServe(":"+port, nil); err != nil {
    		log.Fatal(err)
    	}
    }
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Message struct {
    		Data []byte `json:"data,omitempty"`
    		ID   string `json:"id"`
    	} `json:"message"`
    	Subscription string `json:"subscription"`
    }
    
    // HelloPubSub receives and processes a Pub/Sub push message.
    func HelloPubSub(w http.ResponseWriter, r *http.Request) {
    	var m PubSubMessage
    	body, err := io.ReadAll(r.Body)
    	if err != nil {
    		log.Printf("ioutil.ReadAll: %v", err)
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    	if err := json.Unmarshal(body, &m); err != nil {
    		log.Printf("json.Unmarshal: %v", err)
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    
    	var e imagemagick.GCSEvent
    	if err := json.Unmarshal(m.Message.Data, &e); err != nil {
    		log.Printf("json.Unmarshal: %v", err)
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    
    	if e.Name == "" || e.Bucket == "" {
    		log.Printf("invalid GCSEvent: expected name and bucket")
    		http.Error(w, "Bad Request", http.StatusBadRequest)
    		return
    	}
    
    	if err := imagemagick.BlurOffensiveImages(r.Context(), e); err != nil {
    		log.Printf("imagemagick.BlurOffensiveImages: %v", err)
    		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
    	}
    }
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.gson.JsonObject;
    import com.google.gson.JsonParser;
    import java.util.Base64;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    import org.springframework.web.bind.annotation.RestController;
    
    // PubsubController consumes a Pub/Sub message.
    @RestController
    public class PubSubController {
      @RequestMapping(value = "/", method = RequestMethod.POST)
      public ResponseEntity<String> receiveMessage(@RequestBody Body body) {
        // Get PubSub message from request body.
        Body.Message message = body.getMessage();
        if (message == null) {
          String msg = "Bad Request: invalid Pub/Sub message format";
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.BAD_REQUEST);
        }
    
        // Decode the Pub/Sub message.
        String pubSubMessage = message.getData();
        JsonObject data;
        try {
          String decodedMessage = new String(Base64.getDecoder().decode(pubSubMessage));
          data = JsonParser.parseString(decodedMessage).getAsJsonObject();
        } catch (Exception e) {
          String msg = "Error: Invalid Pub/Sub message: data property is not valid base64 encoded JSON";
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.BAD_REQUEST);
        }
    
        // Validate the message is a Cloud Storage event.
        if (data.get("name") == null || data.get("bucket") == null) {
          String msg = "Error: Invalid Cloud Storage notification: expected name and bucket properties";
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.BAD_REQUEST);
        }
    
        try {
          ImageMagick.blurOffensiveImages(data);
        } catch (Exception e) {
          String msg = String.format("Error: Blurring image: %s", e.getMessage());
          System.out.println(msg);
          return new ResponseEntity<>(msg, HttpStatus.INTERNAL_SERVER_ERROR);
        }
        return new ResponseEntity<>(HttpStatus.OK);
      }
    }

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const express = require('express');
    const app = express();
    
    // This middleware is available in Express v4.16.0 onwards
    app.use(express.json());
    
    const image = require('./image');
    
    app.post('/', async (req, res) => {
      if (!req.body) {
        const msg = 'no Pub/Sub message received';
        console.error(`error: ${msg}`);
        res.status(400).send(`Bad Request: ${msg}`);
        return;
      }
      if (!req.body.message || !req.body.message.data) {
        const msg = 'invalid Pub/Sub message format';
        console.error(`error: ${msg}`);
        res.status(400).send(`Bad Request: ${msg}`);
        return;
      }
    
      // Decode the Pub/Sub message.
      const pubSubMessage = req.body.message;
      let data;
      try {
        data = Buffer.from(pubSubMessage.data, 'base64').toString().trim();
        data = JSON.parse(data);
      } catch (err) {
        const msg =
          'Invalid Pub/Sub message: data property is not valid base64 encoded JSON';
        console.error(`error: ${msg}: ${err}`);
        res.status(400).send(`Bad Request: ${msg}`);
        return;
      }
    
      // Validate the message is a Cloud Storage event.
      if (!data.name || !data.bucket) {
        const msg =
          'invalid Cloud Storage notification: expected name and bucket properties';
        console.error(`error: ${msg}`);
        res.status(400).send(`Bad Request: ${msg}`);
        return;
      }
    
      try {
        await image.blurOffensiveImages(data);
        res.status(204).send();
      } catch (err) {
        console.error(`error: Blurring image: ${err}`);
        res.status(500).send();
      }
    });

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import json
    import os
    
    from flask import Flask, request
    
    import image
    
    
    app = Flask(__name__)
    
    
    @app.route("/", methods=["POST"])
    def index():
        """Receive and parse Pub/Sub messages containing Cloud Storage event data."""
        envelope = request.get_json()
        if not envelope:
            msg = "no Pub/Sub message received"
            print(f"error: {msg}")
            return f"Bad Request: {msg}", 400
    
        if not isinstance(envelope, dict) or "message" not in envelope:
            msg = "invalid Pub/Sub message format"
            print(f"error: {msg}")
            return f"Bad Request: {msg}", 400
    
        # Decode the Pub/Sub message.
        pubsub_message = envelope["message"]
    
        if isinstance(pubsub_message, dict) and "data" in pubsub_message:
            try:
                data = json.loads(base64.b64decode(pubsub_message["data"]).decode())
    
            except Exception as e:
                msg = (
                    "Invalid Pub/Sub message: "
                    "data property is not valid base64 encoded JSON"
                )
                print(f"error: {e}")
                return f"Bad Request: {msg}", 400
    
            # Validate the message is a Cloud Storage event.
            if not data["name"] or not data["bucket"]:
                msg = (
                    "Invalid Cloud Storage notification: "
                    "expected name and bucket properties"
                )
                print(f"error: {msg}")
                return f"Bad Request: {msg}", 400
    
            try:
                image.blur_offensive_images(data)
                return ("", 204)
    
            except Exception as e:
                print(f"error: {e}")
                return ("", 500)
    
        return ("", 500)
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
