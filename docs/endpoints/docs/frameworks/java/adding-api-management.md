---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management/
title: Adding API management \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:19.690575+00:00
---

# Adding API management  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Adding API management Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints Frameworks provides API management features that are comparable to the features that the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/frameworks/glossary#extensible_service_proxy) provides for Cloud Endpoints. Endpoints Frameworks includes a built-in [API gateway](https://en.wikipedia.org/wiki/API_management) that intercepts all requests and performs any necessary checks, such as authentication, before forwarding the request to the API backend. When the backend responds, Endpoints Frameworks gathers and reports telemetry. You can view metrics for your API on the **Endpoints** > **Services** page in the Google Cloud console.

The API management features available in Endpoints Frameworks include:

  * [Monitoring](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api)
  * [Logging](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api#logs)
  * [Quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview)
  * [Developer portal](https://docs.cloud.google.com/endpoints/docs/openapi/dev-portal-overview)



For your API to be managed by Endpoints, you must deploy an OpenAPI document that describes your API using version 2.0 of the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md). This page describes how to generate and deploy an OpenAPI document that enables Endpoints to manage your API.

If you don't add API management, your API still serves requests, but your API doesn't appear on the **Endpoints** > **Services** page in the Google Cloud console, and the functionality provided by Endpoints, such as logging, monitoring, and setting quotas, isn't available.

To add API management to your API:

  1. Set up your Maven `pom.xml` file or your Gradle `build.gradle` file as described in [Configuring the build files](https://docs.cloud.google.com/endpoints/docs/frameworks/java/set-up-environment#configuring_the_build_files).

  2. Make sure that you set the Google Cloud project ID in the build files.

### Maven

Search for `<endpoints.project.id>`, and replace `YOUR_PROJECT_ID` with your Google Cloud project ID. For example:

`<endpoints.project.id>example-project-12345</endpoints.project.id>`
         
         <endpoints.project.id>YOUR_PROJECT_ID</endpoints.project.id>

### Gradle

     1. Search for `def projectId`, and replace `YOUR_PROJECT_ID` with your Google Cloud project ID. For example: 

`def projectId = 'example-project-12345'`

     2. Make sure your `build.gradle` file contains the `replaceProjectId` task, which sets the project ID in the `appengine-web.xml` and `web.xml` files. 
            
            task replaceProjectId(type: Copy) {
                from 'src/main/webapp/WEB-INF/'
                include '*.xml'
                into "build/exploded-${archivesBaseName}/WEB-INF"
                expand(endpoints:[project:[id:projectId]])
                filteringCharset = 'UTF-8'
            }

  3. In your API project's `web.xml` file, add the API management servlet filter configuration:
         
         <!-- Add a filter that fetches the service config from service management. -->
         <filter>
             <filter-name>endpoints-api-configuration</filter-name>
             <filter-class>com.google.api.control.ServiceManagementConfigFilter</filter-class>
         </filter>
         
         <!-- Add a filter that performs Endpoints logging and monitoring. -->
         <filter>
             <filter-name>endpoints-api-controller</filter-name>
             <filter-class>com.google.api.control.extensions.appengine.GoogleAppEngineControlFilter</filter-class>
             <init-param>
                 <param-name>endpoints.projectId</param-name>
                 <param-value>${endpoints.project.id}</param-value>
             </init-param>
             <init-param>
                 <param-name>endpoints.serviceName</param-name>
                 <param-value>${endpoints.project.id}.appspot.com</param-value>
             </init-param>
         </filter>
         
         <filter-mapping>
             <filter-name>endpoints-api-configuration</filter-name>
             <servlet-name>EndpointsServlet</servlet-name>
         </filter-mapping>
         
         <filter-mapping>
             <filter-name>endpoints-api-controller</filter-name>
             <servlet-name>EndpointsServlet</servlet-name>
         </filter-mapping>

  4. Modify your API project's build configuration:

### Maven

     1. Add the API management dependencies:
            
            <dependency>
              <groupId>com.google.endpoints</groupId>
              <artifactId>endpoints-management-control-appengine-all</artifactId>
              <version>1.0.14</version>
            </dependency>

     2. Include the plugin that you can use to generate client libraries and the OpenAPI document, `openapi.json`:
            
            <plugin>
              <groupId>com.google.cloud.tools</groupId>
              <artifactId>endpoints-framework-maven-plugin</artifactId>
              <version>2.1.0</version>
              <configuration>
                <!-- plugin configuration -->
                <hostname>${endpoints.project.id}.appspot.com</hostname>
              </configuration>
            </plugin>

### Gradle

     1. Add the API management dependencies:
            
            compile 'com.google.endpoints:endpoints-management-control-appengine:1.0.14'
            compile 'com.google.endpoints:endpoints-framework-auth:1.0.14'

     2. Declare the external dependency so that the plugin is retrieved from Maven Central:
            
            classpath 'com.google.cloud.tools:endpoints-framework-gradle-plugin:2.1.0'

     3. Use the server-side Endpoints Frameworks Gradle plugin, which generates the OpenAPI document:
            
            apply plugin: 'com.google.cloud.tools.endpoints-framework-server'

     4. Configure the name of your Endpoints service:
            
            endpointsServer {
              // Endpoints Framework Plugin server-side configuration
              hostname = "${projectId}.appspot.com"
            }

  5. After modifying dependencies, clean your project and then build your API:

### Maven
         
         mvn clean
             mvn package

### Gradle
         
         gradle clean
             gradle build

  6. Generate the OpenAPI document, `openapi.json`:

### Maven
         
         mvn endpoints-framework:openApiDocs

### Gradle
         
         gradle endpointsOpenApiDocs

  7. Deploy the OpenAPI document:
         
         gcloud endpoints services deploy openapi.json
         

The first time you deploy `openapi.json`, a new Endpoints service is created with the name `YOUR_PROJECT_ID.appspot.com`. On successful completion, a line similar to the following displays the service configuration ID and the service name:
         
         Service Configuration 2017-02-13r0 uploaded for service example-project-12345.appspot.com
         

In the preceding example, `2017-02-13r0` is the service configuration ID. The service configuration ID consists of a date stamp followed by a revision number. If you deploy `openapi.json` again, the revision number is incremented in the service configuration ID.

If you need to display the service configuration ID again, run the following command, but replace `YOUR_PROJECT_ID` with the project ID of your Google Cloud project:
         
         gcloud endpoints configs list --service=YOUR_PROJECT_ID.appspot.com
         

You can create your own OpenAPI document and deploy it, rather than using a generated one. Simply replace `openapi.json` above with the path to your OpenAPI document. For more information on writing an OpenAPI document, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).

  8. Edit your `appengine-web.xml` file to set the value for an environment variable:
         
         <env-variables>
             <env-var name="ENDPOINTS_SERVICE_NAME" value="${endpoints.project.id}.appspot.com" />
         </env-variables>

Replace `${endpoints.project.id}` with your Google Cloud project ID. For example:
         
         <env-var name="ENDPOINTS_SERVICE_NAME" value="example-project-12345.appspot.com" />
         

  9. Redeploy your application.

### Maven
         
         mvn appengine:deploy

### Gradle
         
         gradle appengineDeploy

  10. Test your API by making some requests to it.

  11. To [view your API metrics](https://docs.cloud.google.com/endpoints/docs/frameworks/monitoring-your-api), open the **Endpoints** > **Services** page in the Google Cloud console for your project:  


[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
