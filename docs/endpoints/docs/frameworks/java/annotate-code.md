---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code/
title: Writing and annotating the code \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:18.371455+00:00
---

# Writing and annotating the code  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotate-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Writing and annotating the code Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to structure and annotate your Cloud Endpoints Frameworks code. For a complete list of all supported annotations, see [Annotations](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations).

## Before you begin

  1. [Set up your development environment](https://docs.cloud.google.com/endpoints/docs/frameworks/java/set-up-environment).
  2. Clone the skeleton Endpoints Frameworks example:
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples.git
         

  3. The skeleton Endpoints Frameworks example is located in:
         
         cd appengine-java8/endpoints-v2-skeleton/
         




To help explain how annotations work, this document uses the `endpoints-v2-backend` sample to show the annotations and other code that you must add to the `endpoints-v2-skeleton` sample to get it to build. In the end, the modified `endpoints-v2-skeleton` sample behaves the same as the `endpoints-v2-backend` sample, which is used in [Getting started with Endpoints Frameworks on App Engine](https://docs.cloud.google.com/endpoints/docs/frameworks/java/get-started-frameworks-java).

## Creating and annotating code

To annotate your code:

  1. Change directories to the project's Java source directory, for example: `src/main/java/com/example/skeleton`. 
  2. Create a [JavaBean](https://wikipedia.org/wiki/JavaBeans) class file named `Message.java` that contains the following code: 
         
         public class Message {
         
           private String message;
         
           public String getMessage() {
             return this.message;
           }
         
           public void setMessage(String message) {
             this.message = message;
           }
         }

  3. Edit the `MyApi.java` file contained in the skeleton example. Change the `@Api` definition annotation with the following: 
         
         @Api(
             name = "echo",
             version = "v1",
             namespace =
             @ApiNamespace(
                 ownerDomain = "echo.example.com",
                 ownerName = "echo.example.com",
                 packagePath = ""
             ),
             // ...
         )

The `version = "v1"` attribute specifies the version of the sample API. The value that you enter becomes part of the path in the URL to your API. For more information on versions, see [Handling API versioning](https://docs.cloud.google.com/endpoints/docs/frameworks/java/handling-api-versioning).

  4. Add the following `echo` method as your first API endpoint and the `doEcho` helper method to your `MyApi.java`. 
         
         @ApiMethod(name = "echo")
         public Message echo(Message message, @Named("n") @Nullable Integer n) {
           return doEcho(message, n);
         }
         
         private Message doEcho(Message request, Integer n) {
           Message response = new Message();
           if (n != null && n >= 0) {
             StringBuilder sb = new StringBuilder();
             for (int i = 0; i < n; i++) {
               if (i > 0) {
                 sb.append(' ');
               }
               sb.append(request.getMessage());
             }
             response.setMessage(sb.toString());
           }
           return response;
         }

  5. Copy all of the imports from [ `Echo.java`](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/appengine-java8/endpoints-v2-backend/src/main/java/com/example/echo/Echo.java), and paste them in your `MyApi.java`. 
  6. ### Maven

Build the project:
         
         mvn clean package

### Gradle

Build the project:
         
         gradle clean build




## Annotation basics

There are three annotations commonly used in backend APIs:

  * [`@Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#api_api-scoped_annotations) contains the configuration details of the backend API.
  * [`@ApiMethod`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#apimethod_method-scoped_annotations) marks a class method that is part of the backend API. Methods that aren't marked with`@ApiMethod` aren't included when you generate client libraries and discovery docs. The `@ApiMethod` annotation can also be used to override the API configuration for a specific method.
  * [`@Named`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#named) must be added to all parameters passed to server-side methods, unless the parameter is an entity type.



For a complete list of all Endpoints Frameworks annotations, see [Annotations and syntax](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations).

## What's next

  * [Learn about adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).
  * [Learn about the supported parameter and return types](https://docs.cloud.google.com/endpoints/docs/frameworks/java/parameter-and-return-types).
  * [Learn about exceptions and status codes](https://docs.cloud.google.com/endpoints/docs/frameworks/java/exceptions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
