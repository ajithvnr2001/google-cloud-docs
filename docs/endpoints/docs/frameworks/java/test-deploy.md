---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy/
title: Deploying and testing an API \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:30.550004+00:00
---

# Deploying and testing an API  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Deploying and testing an API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy your API.

## Before you begin

  * [Set up your programming environment](https://docs.cloud.google.com/endpoints/docs/frameworks/java/set-up-environment).
  * [Create an API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code) and annotate it.



## Deploying an API

You can deploy your API using the App Engine [Apache Maven](https://docs.cloud.google.com/appengine/docs/standard/java/using-maven) or [Gradle](https://docs.cloud.google.com/appengine/docs/standard/java/using-gradle) plugins. To deploy your API to a production App Engine standard environment, use the command for your plugin:

  1. Use the command for your plugin: 

### Maven
         
         mvn appengine:deploy

### Gradle
         
         gradle appengineDeploy

  2. Wait for the deployment to finish.
  3. Send a test request to your deployed API. For example, using `curl`:
         
         curl \
             -H "Content-Type: application/json" \
             -X POST \
             -d '{"message": "echo"}' \
             "https://YOUR-PROJECT-ID.appspot.com/_ah/api/echo/v1/echo?n=2"
         

Your response is similar to the following:
         
         {
           "message": "echo echo"
         }
         




If you didn't get a successful response, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/frameworks/troubleshoot-response-errors).

## Deploying to multiple application versions

For information on how to do API versioning, and how to deploy to versions, see [Handling API versioning](https://docs.cloud.google.com/endpoints/docs/frameworks/java/handling-api-versioning)

## Running and testing API backends locally

To test your API locally:

  1. Build the project in the root directory of the project. For example:

### Maven
         
         mvn clean package

### Gradle
         
         gradle clean build

  2. Start the App Engine development server. For example:

### Maven
         
         mvn appengine:run

### Gradle
         
         gradle appengineRun

  3. Make an API request to test your API. For example, using `curl`:
         
         curl \
             -H "Content-Type: application/json" \
             -X POST \
             -d '{"message": "echo"}' \
             "${HOST}/_ah/api/echo/v1/echo?n=2"
         




## Serving your API from a different path

To serve your API from a different path, in your `web.xml` file, change the `url-pattern` in the `EndpointsServlet` section and redeploy your API. For example:
    
    
    <servlet-mapping>
        <servlet-name>EndpointsServlet</servlet-name>
        <url-pattern>/example-api/*</url-pattern>
    </servlet-mapping>
    

## Adding API management

Endpoints Frameworks provides API management features such as:

  * [Monitoring](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api)
  * [Logging](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api#logs)
  * [Quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview)
  * [Developer portal](https://docs.cloud.google.com/endpoints/docs/openapi/dev-portal-overview)



For your API to be managed by Endpoints Frameworks, you must generate and deploy an OpenAPI document that describes your API, as described in [Adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
