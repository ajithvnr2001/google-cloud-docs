---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/remove-api-management/
title: Removing API management \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:46.986454+00:00
---

# Removing API management  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/remove-api-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Removing API management Stay organized with collections  Save and categorize content based on your preferences. 

If you added API management to your application on Google Cloud, and subsequently decide that you don't want the API management features, you can configure Cloud Endpoints Frameworks to stop managing your API.

Removing API management doesn't stop your API from being served. If you want to stop serving your API, you can either disable the application on the **App Engine Settings** page in the Google Cloud console, or you can delete the Google Cloud project. See [Disabling an application and shutting down a project](https://cloud.google.com/appengine/docs/flexible/python/managing-projects-apps-billing#disabling_an_application) for more information.

To remove API management:

  1. Backup your API project's `web.xml` and `appengine-web.xml` files.

  2. In your API project's `web.xml` file, remove the following:

     * The `endpoints-api-configuration` filter.
     * The `endpoints-api-controller` filter.
     * The `endpoints-api-configuration` filter-mapping.
     * The `endpoints-api-controller` filter-mapping.

After deleting the filters and filter mappings, your `web.xml` should be similar to the following:
    
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee
             http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
             version="3.1">
        <!-- Wrap the backend with Endpoints Frameworks v2. -->
        <servlet>
            <servlet-name>EndpointsServlet</servlet-name>
            <servlet-class>com.google.api.server.spi.EndpointsServlet</servlet-class>
            <init-param>
                <param-name>services</param-name>
                <param-value>com.example.skeleton.MyApi</param-value>
            </init-param>
        </servlet>
        <!-- Route API method requests to the backend. -->
        <servlet-mapping>
            <servlet-name>EndpointsServlet</servlet-name>
            <url-pattern>/_ah/api/*</url-pattern>
        </servlet-mapping>
    </web-app>

  3. In your `appengine-web.xml` file, remove the line that defines the `ENDPOINTS_SERVICE_NAME` environment variable. If `ENDPOINTS_SERVICE_NAME` is the only environment variable that you have defined, remove the entire `env-variables` section.

  4. Clean your project and then build your API:

### Maven
         
         mvn clean
             mvn package

### Gradle
         
         gradle clean
             gradle build

  5. Redeploy your application:

### Maven
         
         mvn appengine:deploy

### Gradle
         
         gradle appengineDeploy




After you redeploy your application, Cloud Endpoints Frameworks stops managing your API.

## Verifying API management removal

To verify that Endpoints Frameworks is no longer managing your API:

  1. In the Google Cloud console, go to the **Endpoints** > **Services** page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

  2. Write down the number of requests to one of the methods in your API.

  3. Click the `View logs` link for the method.

  4. In the `Produced API` log, write down the date and time of the most recent log entry.

  5. Send some requests to the method in your API.

  6. In the Google Cloud console, go to the **Endpoints** > **Services** page.

[Go to the Endpoints Services page](https://console.cloud.google.com/endpoints)

The request counter for the method isn't updated.

  7. Click the `View logs` link for the method.

The `Produced API` log doesn't contain log entries for the requests that you sent.




## Removing dependencies in your build configuration

Although not required, you might want to remove dependencies in your build configuration.

To remove dependencies in your build configuration:

  1. Backup your `pom.xml` file or your `build.gradle` file.

  2. Remove the following dependencies:

     * `endpoints-management-control-appengine`
     * `endpoints-management-control-appengine-all`
     * `endpoints-framework-auth`
  3. Clean your project and then build your API:

### Maven
         
         mvn clean
             mvn package

### Gradle
         
         gradle clean
             gradle build

  4. Redeploy your application:

### Maven
         
         mvn appengine:deploy

### Gradle
         
         gradle appengineDeploy

  5. Test your API to make sure it is working as expected.




## Deleting the managed service

Endpoints Frameworks uses Google's Service Management to manage your API. When you deployed the OpenAPI document by using the `gcloud endpoints services deploy` command, the command used Service Management to create a managed service for your API. If you don't need the data on the **Endpoints** > **Services** page and in the **Produced API** log on the **Logs Viewer** page, you can delete the managed service for your API, which removes the data from the Google Cloud console. 

To delete the managed service:

  1. Make sure that the gcloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login
         

  2. Enter the following to display the project IDs for your Google Cloud projects:
         
         gcloud projects list
         

  3. Using the applicable project ID from the previous step, set the default Google Cloud project to the one that your application is in:
         
         gcloud config set project [YOUR_PROJECT_ID]
         

  4. Obtain the name of all managed services in your Google Cloud project:
         
         gcloud endpoints services list
         

  5. Delete the service from Service Management. Replace `SERVICE_NAME` with the name of the service you want to remove.
         
         gcloud endpoints services delete SERVICE_NAME
         

Running `gcloud endpoints services delete` doesn't immediately delete the managed service. Service Management disables the managed service for 30 days, which allows you time to restore it if you need to. After 30 days, Service Management permanently deletes the managed service.




## What's next

  * To restore a managed service, see [Restoring a managed service](https://docs.cloud.google.com/endpoints/docs/frameworks/java/restore-managed-service).

  * For information on the `gcloud` commands used on this page, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference).

  * For information on Service Management, see [Creating and deleting managed services](https://docs.cloud.google.com/service-infrastructure/docs/create-services).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
