---
url: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-generic-handler/
title: Create a generic event handler \u00a0|\u00a0 Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:36.066735+00:00
---

# Create a generic event handler  |  Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/samples/eventarc-generic-handler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Samples ](https://docs.cloud.google.com/eventarc/docs/samples)



#  Create a generic event handler Stay organized with collections  Save and categorize content based on your preferences. 

Creates an event handler that receives an incoming event as a CloudEvent.

## Code sample

### Go

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample generic is a Cloud Run service which logs and echos received requests.
    package main
    
    import (
    	"encoding/json"
    	"fmt"
    	"io"
    	"log"
    	"net/http"
    	"os"
    	"strings"
    )
    
    // GenericHandler receives and echos a HTTP request's headers and body.
    func GenericHandler(w http.ResponseWriter, r *http.Request) {
    	log.Println("Event received!")
    
    	// Log all headers besides authorization header
    	log.Println("HEADERS:")
    	headerMap := make(map[string]string)
    	for k, v := range r.Header {
    		if k != "Authorization" {
    			val := strings.Join(v, ",")
    			headerMap[k] = val
    			log.Println(fmt.Sprintf("%q: %q\n", k, val))
    		}
    	}
    
    	// Log body
    	log.Println("BODY:")
    	bodyBytes, err := io.ReadAll(r.Body)
    	if err != nil {
    		log.Printf("error parsing body: %v", err)
    	}
    	body := string(bodyBytes)
    	log.Println(body)
    
    	// Format and print full output
    	type result struct {
    		Headers map[string]string `json:"headers"`
    		Body    string            `json:"body"`
    	}
    	res := &result{
    		Headers: headerMap,
    		Body:    body,
    	}
    	if err := json.NewEncoder(w).Encode(res); err != nil {
    		log.Printf("error encoding response: %v", err)
    		http.Error(w, "Could not marshal JSON output", 500)
    		return
    	}
    	fmt.Fprintln(w)
    }
    

### Java

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import java.util.Map;
    import org.json.JSONObject;
    import org.springframework.http.HttpStatus;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.RequestBody;
    import org.springframework.web.bind.annotation.RequestHeader;
    import org.springframework.web.bind.annotation.RequestMapping;
    import org.springframework.web.bind.annotation.RequestMethod;
    import org.springframework.web.bind.annotation.RestController;
    
    @RestController
    public class EventController {
      @RequestMapping(value = "/", method = RequestMethod.POST)
      public ResponseEntity<String> receiveMessage(
          @RequestBody String body, @RequestHeader Map<String, String> headers) {
        System.out.println("Event received!");
    
        // Log headers
        System.out.println("HEADERS:");
        headers.forEach((k, v) -> {
          if (!k.equals("Authorization")) {
            System.out.printf("%s: %s\n", k, v);
          }
        });
        System.out.println("");
    
        // Log body
        System.out.println("BODY:");
        JSONObject jsonBody = new JSONObject(body);
        String jsonString = jsonBody.toString(2);
        System.out.println(jsonString);
    
        // Return headers and body
        JSONObject json = new JSONObject();
        JSONObject jsonHeaders = new JSONObject();
        json.put("headers", jsonHeaders);
        json.put("body", jsonBody);
    
        return new ResponseEntity<>(json.toString(), HttpStatus.OK);
      }
    }

### Node.js

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const express = require('express');
    const app = express();
    
    app.use(express.json());
    app.post('/', (req, res) => {
      console.log('Event received!');
    
      console.log('HEADERS:');
      delete req.headers.authorization; // do not log authorization header
      console.log(JSON.stringify(req.headers));
    
      console.log('BODY:');
      console.log(JSON.stringify(req.body));
    
      res.send({
        headers: req.headers,
        body: req.body,
      });
    });
    
    module.exports = app;

### PHP

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $msg = "Event received!\n";
    
    $msg .= "\nHEADERS:\n";
    $headers = getallheaders();
    unset($headers['Authorization']); // do not log authorization header
    foreach ($headers as $name => $value) {
        $msg .= "$name: $value\n";
    }
    
    $msg .= "\nBODY:\n";
    $body = file_get_contents('php://input');
    $msg .= $body . "\n";
    
    // Write to stderr for logging
    $log = fopen('php://stderr', 'wb');
    fwrite($log, $msg);
    // Echo to return in request body
    echo $msg;

### Python

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    @app.route("/", methods=["POST"])
    def index():
        print("Event received!")
    
        print("HEADERS:")
        headers = dict(request.headers)
        headers.pop("Authorization", None)  # do not log authorization header if exists
        print(headers)
    
        print("BODY:")
        body = dict(request.json)
        print(body)
    
        resp = {"headers": headers, "body": body}
        return (resp, 200)
    
    

### Ruby

To authenticate to Eventarc, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    post "/" do
      request.body.rewind # in case someone already read it
    
      puts "Event received!"
    
      puts "\nHEADERS:"
      headers = request.env.select { |k, _v| k.start_with? "HTTP_" }
      headers = headers.collect { |key, val| [key.sub(/^HTTP_/, ""), val] }
      headers = headers.collect { |key, val| "#{key}: #{val}" }.sort
      headers.each do |key, value|
        if key != "Authorization"
          puts "#{key}: #{value}<br>"
        end
      end
      headers_json = headers
    
      puts "\nBODY:"
      body_json = JSON.parse request.body.read
      puts body_json
    
      result = {
        "headers" => headers_json,
        "body"    => body_json
      }
      result.to_json
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=eventarc). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
