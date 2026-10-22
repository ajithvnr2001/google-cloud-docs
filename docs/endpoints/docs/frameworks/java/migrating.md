---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating/
title: Migrating to Cloud Endpoints Frameworks version 2.0 for App Engine \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:59.990038+00:00
---

# Migrating to Cloud Endpoints Frameworks version 2.0 for App Engine  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Migrating to Cloud Endpoints Frameworks version 2.0 for App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes migrating an existing Cloud Endpoints version 1.0 application to [Endpoints Frameworks for App Engine](https://docs.cloud.google.com/endpoints/docs/frameworks/java) in Java.

**Note:** This page refers to Endpoints 1.0 as Endpoints Frameworks version 1.0 and new Endpoints Frameworks for App Engine as Endpoints Frameworks version 2.0.

## Benefits

The new framework brings a number of benefits, including:

  * Reduced request latency.
  * Better integration with App Engine features, such as custom domains.
  * Official support for Guice configurations.
  * Optionally, new API management features.



Endpoints Frameworks version 2.0 doesn't affect the interfaces to your API. Existing clients continue to work after migration without any client-side code changes.

## Currently excluded features and tools

The following features aren't currently available. If you require any of these, please submit a [feature request](https://github.com/cloudendpoints/endpoints-java/issues).

  * JSON-RPC protocol, which is required for legacy iOS clients. To create iOS clients for your Endpoints Frameworks version 2.0 API, we recommend that you use [Google APIs Objective-C client library for REST APIs](https://github.com/google/google-api-objectivec-client-for-rest/wiki).
  * Automatic ETags
  * Automatic kind fields
  * IDE integration
  * `fields` partial responses
  * Automatic PATCH API method creation



In addition, Android Studio support for Endpoints version 1.0 isn't currently supported for version 2.0.

## Migrating to Endpoints Frameworks version 2.0

Endpoints Frameworks version 2.0 has moved to Maven artifacts in group `com.google.endpoints`. The base required JAR is in the `endpoints-framework` artifact. If you wish to use Guice configuration, add the `endpoints-framework-guice` artifact.

The following instructions provide an example of how to migrate from Endpoints Frameworks version 1.0 to Endpoints Frameworks version 2.0 by using a **Discovery Document** :

  1. [Download and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). 
  2. Run the following commands: 
     1. Make sure that the gcloud CLI is authorized to access your data and services on Google Cloud: 
            
            gcloud auth login

     2. Use application default credentials: 
            
            gcloud auth application-default login

     3. Install the Google Cloud SDK `app-engine-java` component: 
            
            gcloud components install app-engine-java

     4. Update to the latest version of the Google Cloud SDK and all components: 
            
            gcloud components update




### Migrate using Maven or Gradle

### Maven

  1. Remove the legacy dependency, which is the `appengine-endpoints` artifact: 
         
         <dependency>
               <groupId>com.google.appengine</groupId>
               <artifactId>appengine-endpoints</artifactId>
               <version>1.9.53</version>
         </dependency>

  2. Add the new Endpoints Frameworks dependency: 
         
         <dependency>
             <groupId>com.google.endpoints</groupId>
             <artifactId>endpoints-framework</artifactId>
             <version>2.2.1</version>
         </dependency>

  3. Add the new Endpoints Frameworks plugin and define the hostname for a generated discovery document: 
         
         <plugin>
             <groupId>com.google.cloud.tools</groupId>
             <artifactId>endpoints-framework-maven-plugin</artifactId>
             <version>1.0.2</version>
             <configuration>
                 <!-- plugin configuration -->
                 <hostname>YOUR-PROJECT-ID.appspot.com</hostname>
             </configuration>
         </plugin>

  4. Add the new App Engine Maven plugin: 
         
         <plugin>
             <groupId>com.google.cloud.tools</groupId>
             <artifactId>appengine-maven-plugin</artifactId>
             <version>1.3.2</version>
             <configuration>
                 <!-- deploy configuration -->
             </configuration>
         </plugin>

**Note** : The old App Engine Maven plugin, with group `com.google.appengine`, is incompatible with the Endpoints Frameworks plugin. You must use the new version.
  5. Update the API entry point in your project `web.xml` file: 
     * Rename all occurrences of `SystemServiceServlet` to `EndpointsServlet`
     * Replace all occurrences of the path `/_ah/spi/__`to the new required path`/_ah/api/`  


The following shows the contents of the `web.xml` before and after migration: 

### Before migration

Endpoints Frameworks version 1.0 `web.xml`: 
    
    <servlet>
        <servlet-name>SystemServiceServlet</servlet-name>
        <servlet-class>com.google.api.server.spi.SystemServiceServlet</servlet-class>
        <init-param>
            <param-name>services</param-name>
            <param-value>com.example.helloendpoints.Greetings</param-value>
        </init-param>
        <init-param>
            <param-name>restricted</param-name>
            <param-value>false</param-value>
        </init-param>
    </servlet>
    <servlet-mapping>
        <servlet-name>SystemServiceServlet</servlet-name>
        <url-pattern>/_ah/spi/*</url-pattern>
    </servlet-mapping>

### After migration

Endpoints Frameworks version 2.0 `web.xml`: 
    
    <servlet>
        <servlet-name>EndpointsServlet</servlet-name>
        <servlet-class>com.google.api.server.spi.EndpointsServlet</servlet-class>
        <init-param>
            <param-name>services</param-name>
            <param-value>com.example.helloendpoints.Greetings</param-value>
        </init-param>
        <init-param>
            <param-name>restricted</param-name>
            <param-value>false</param-value>
        </init-param>
    </servlet>
    <servlet-mapping>
        <servlet-name>EndpointsServlet</servlet-name>
        <url-pattern>/_ah/api/*</url-pattern>
    </servlet-mapping>

  6. After modifying dependencies clean the projec: 
         
         mvn clean

  7. You can generate a discovery document: 
         
         mvn endpoints-framework:discoveryDocs

Learn more about the Maven Endpoints Frameworks [plugin goals](https://docs.cloud.google.com/endpoints/docs/frameworks/java/maven-endpoints-frameworks-plugin). 
  8. You can deploy a project: 
         
         mvn appengine:deploy

Learn more about the Maven App Engine [plugin goals](https://docs.cloud.google.com/appengine/docs/standard/java/maven-reference). 

**Note** : When migrating, you must deploy to a new App Engine version. This is done automatically if you don't specify a version. See [Known issues](https://docs.cloud.google.com/endpoints/docs/frameworks/java/about-cloud-endpoints-frameworks).




### Gradle

  1. Remove the legacy dependency, which is the `appengine-endpoints` artifact: 
         
         compile group: 'com.google.appengine', name: 'appengine-endpoints', version: '+'

  2. Add the new Endpoints Frameworks dependency: 
         
         compile group: 'com.google.endpoints', name: 'endpoints-framework', version: '2.0.8'

  3. Add the new App Engine and Endpoints Frameworks plugins: 
         
         buildscript {    // Configuration for building
           repositories {
             mavenCentral()
             jcenter()    // Bintray's repository - a fast Maven Central mirror & more
           }
           dependencies {
             // App Engine Gradle plugin
             classpath 'com.google.cloud.tools:appengine-gradle-plugin:1.3.3'
         
             // Endpoints Frameworks Gradle plugin
             classpath 'com.google.cloud.tools:endpoints-framework-gradle-plugin:1.0.2'
           }
         }

  4. Apply the new App Engine and Endpoints Frameworks plugins: 
         
         apply plugin: 'com.google.cloud.tools.appengine'
         apply plugin: 'com.google.cloud.tools.endpoints-framework-server'

  5. Define the hostname endpoint for generated discovery documents: 
         
         endpointsServer {
           // Endpoints Framework Plugin server-side configuration
           hostname = "YOUR-PROJECT-ID.appspot.com"
         }

  6. Update the API entry point in your project `web.xml` file: 
     * Rename all occurrences of `SystemServiceServlet` to `EndpointsServlet`
     * Replace all occurrences of the path `/_ah/spi/__`to the new required path`/_ah/api/`  


The following shows the contents of the `web.xml` before and after migration: 

### Before migration

Endpoints Frameworks version 1.0 `web.xml`: 
    
    <servlet>
        <servlet-name>SystemServiceServlet</servlet-name>
        <servlet-class>com.google.api.server.spi.SystemServiceServlet</servlet-class>
        <init-param>
            <param-name>services</param-name>
            <param-value>com.example.helloendpoints.Greetings</param-value>
        </init-param>
        <init-param>
            <param-name>restricted</param-name>
            <param-value>false</param-value>
        </init-param>
    </servlet>
    <servlet-mapping>
        <servlet-name>SystemServiceServlet</servlet-name>
        <url-pattern>/_ah/spi/*</url-pattern>
    </servlet-mapping>

### After migration

Endpoints Frameworks version 2.0 `web.xml`: 
    
    <servlet>
        <servlet-name>EndpointsServlet</servlet-name>
        <servlet-class>com.google.api.server.spi.EndpointsServlet</servlet-class>
        <init-param>
            <param-name>services</param-name>
            <param-value>com.example.helloendpoints.Greetings</param-value>
        </init-param>
        <init-param>
            <param-name>restricted</param-name>
            <param-value>false</param-value>
        </init-param>
    </servlet>
    <servlet-mapping>
        <servlet-name>EndpointsServlet</servlet-name>
        <url-pattern>/_ah/api/*</url-pattern>
    </servlet-mapping>

  7. After modifying dependencies clean the project using: 
         
         gradle clean

  8. You can generate a discovery document by using: 
         
         gradle endpointsDiscoveryDocs

Learn more about the Gradle Endpoints Frameworks [plugin tasks](https://docs.cloud.google.com/endpoints/docs/frameworks/java/gradle-endpoints-frameworks-plugin)
  9. You can deploy a project by using: 
         
         gradle appengineDeploy

Learn more about the Gradle App Engine [plugin tasks](https://docs.cloud.google.com/appengine/docs/standard/java/gradle-reference). 

**Note** : When migrating, you must deploy to a new App Engine version. This is done automatically if you don't specify a version. See [Known issues](https://docs.cloud.google.com/endpoints/docs/frameworks/java/about-cloud-endpoints-frameworks).




### Using Guice to configure Endpoints Frameworks for Java

If you wish to use Guice:

  1. Add the new Endpoints Frameworks Guice dependency: 

### Maven
         
         <dependency>
             <groupId>com.google.endpoints</groupId>
             <artifactId>endpoints-framework-guice</artifactId>
             <version>2.2.1</version>
         </dependency>

### Gradle
         
         compile 'com.google.endpoints:endpoints-framework-guice:2.0.9'

  2. Declare a new module that extends `EndpointsModule`, and configure it, as follows: 
         
         public class EchoEndpointModule extends EndpointsModule {
           @Override
           public void configureServlets() {
             super.configureServlets();
         
             bind(ServiceManagementConfigFilter.class).in(Singleton.class);
             filter("/_ah/api/*").through(ServiceManagementConfigFilter.class);
         
             Map<String, String> apiController = new HashMap<String, String>();
             apiController.put("endpoints.projectId", "YOUR-PROJECT-ID");
             apiController.put("endpoints.serviceName", "YOUR-PROJECT-ID.appspot.com");
         
             bind(GoogleAppEngineControlFilter.class).in(Singleton.class);
             filter("/_ah/api/*").through(GoogleAppEngineControlFilter.class, apiController);
         
             bind(Echo.class).toInstance(new Echo());
             configureEndpoints("/_ah/api/*", ImmutableList.of(Echo.class));
           }
         }




## Verifying a new deployment

You can verify that the new framework is serving traffic:

  1. Send some requests to the new deployment.
  2. In the Google Cloud console, go to the **Logging** > **Logs Explorer** page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  3. If requests are shown with paths beginning with `/_ah/api`, then Endpoints Frameworks version 2.0 is now serving your API. The logs shouldn't show any requests with paths beginning with `/_ah/spi`. These requests indicate that the Endpoints Frameworks version 1.0 proxy is still serving requests.




## Adding Endpoints API management

Endpoints Frameworks version 2.0 also lets you turn on API management features, including:

  * API key management
  * API sharing
  * User authentication
  * API metrics
  * API logs



To get started using these features, see [Adding API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).

## Troubleshooting

This section describes common erratic behaviors when migrating to Endpoints Frameworks version 2.0 and suggested solutions.

### API returns `404` errors, but API Explorer still lists APIs correctly

You are required to remove the old Endpoints Frameworks version 1.0 configuration when migrating to Endpoints Frameworks version 2.0. If the old configuration is still present in the application configuration, the Endpoints service continues to treat the app as a version 1.0 app. You may see requests in your App Engine logs sent to `/_ah/spi`, which result in `HTTP 404` errors sent to the client.

  1. Remove the following lines from your `web.xml` file, if they are present:
         
         <servlet>
             <servlet-name>SystemServiceServlet</servlet-name>
             <servlet-class>com.google.api.server.spi.SystemServiceServlet</servlet-class>
             <init-param>
                 <param-name>services</param-name>
                 <param-value>...</param-value>
             </init-param>
         </servlet>
         <servlet-mapping>
             <servlet-name>SystemServiceServlet</servlet-name>
             <url-pattern>/_ah/spi/*</url-pattern>
         </servlet-mapping>
         

  2. Make sure your `web.xml` file contains the following:
         
         <servlet-mapping>
             <servlet-name>EndpointsServlet</servlet-name>
             <url-pattern>/_ah/api/*</url-pattern>
         </servlet-mapping>
         




### API is throwing reflection errors

You must package only the `endpoints-framework` artifact into your application, not the old `appengine-endpoints` JAR. If you deploy an application with both JARs, you might run into reflection errors or runtime type errors, such as `NoClassDefFoundError`, `NoSuchMethodError`, and `ClassCastException`. Remove the following lines from your build file, if they are present:

### Maven
    
    
    <dependency>
          <groupId>com.google.appengine</groupId>
          <artifactId>appengine-endpoints</artifactId>
          <version>1.9.53</version>
    </dependency>

### Gradle
    
    
    compile group: 'com.google.appengine', name: 'appengine-endpoints', version: '+'

In addition, if any of your other dependencies depend on older versions of Guava, this can also manifest as a missing `TypeToken` method. You must ensure that you use Guava v19 or use the `endpoints-framework-all` artifact, which shadows dependencies.

### Client library sources don't compile

If you see an error such as, `method does not override or implement a method from a supertype`, or `cannot find symbol method setBatchPath(String)`, then your client application likely depends on an old version of the Google Java client library. You must ensure that your `google-api-client` artifact is `1.23.0` or higher.

### Maven
    
    
    <dependency>
        <groupId>com.google.api-client</groupId>
        <artifactId>google-api-client</artifactId>
        <version>1.23.0</version>
    </dependency>

### Gradle
    
    
    compile group: 'com.google.api-client', name: 'google-api-client', version: '1.23.0'

### Issues with JPA/JDO Datanucleus enhancement

### Maven

The new Google Cloud CLI-based App Engine Maven plugin doesn't support Datanucleus enhancement of any type. If your project uses the Datanucleus JDO or JPA enhancement support from the old plugin, you must configure the third-party Datanucleus Maven plugin separately when you migrate. See the following for more information: 

  * [ JDO instructions](https://docs.cloud.google.com/appengine/docs/standard/java/datastore/jdo/overview-dn2)
  * [ JPA instructions](https://docs.cloud.google.com/appengine/docs/standard/java/datastore/jpa/overview-dn2)



### Gradle

If your project uses the `gradle-appengine-plugin` JPA/JDO Datanucleus enhancement, you must manually configure Datanucleus enhancement after switching to the new gcloud CLI-based Gradle plugin. See an [ example from Stackoverflow](https://stackoverflow.com/questions/29279503/how-can-i-run-datanucleus-enhancer-from-gradle). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
