---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime/
title: Upgrade an existing application \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:13.163674+00:00
---

# Upgrade an existing application  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/upgrade-java-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Upgrade an existing application Stay organized with collections  Save and categorize content based on your preferences. 

Upgrade your applications to the [latest supported runtime version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java) to continue receiving security updates and be eligible for technical support.

The process of upgrading an existing application depends on the runtime version that your application uses:

  * **Java 8** : Migrate your application to the [latest supported Java version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java). Java 8 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on January 31, 2024 and will be deprecated on January 31, 2026. After deprecation, you won't be able to deploy Java 8 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing Java 8 applications will continue to run and receive traffic [after their deprecation date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java).

  * **Java 11** : Upgrade your application to the [latest supported Java version](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java). Java 11 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support) on October 31, 2024 and will be deprecated on October 31, 2025. After deprecation, you won't be able to deploy Java 11 applications. Your existing Java 11 applications will continue to run and receive traffic [after their deprecation date](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java).

  * **Supported second-generation runtimes (Java 17 and Java 21)** :

App Engine supports second-generation Java runtime versions, such as Java 17 and Java 21. To upgrade to Java 25, do the following:

    * Update the `app.yaml` file by specifying a version of Java that you want your app to run. For example:
          
          runtime: javaVERSION
          

Where VERSION is the `MAJOR` version number. For example, to use the latest Java version, Java 25, specify `25`. For more information, see the [Java runtime overview](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/runtime).

    * If you use legacy bundled services, upgrade your applications to run on either:

      * Java Enterprise Edition 11 (E11): EE 11 doesn't support `javax.servlet.*` APIs and requires you to update your applications and third-party dependencies to use newer Java artifacts like the `Jakarta` namespace. Java 25 by default runs on EE 11 and doesn't support EE 10.

      * Java Enterprise Edition 8 (EE 8): Java EE 8 lets you use `javax.servlet.*` APIs, but you must make minor configuration changes to your `appengine-web.xml` file.




## Upgrade to a supported Java version for legacy bundled services

**Important:** The `javax.servlet.*` APIs reached the [end of community support](https://github.com/jetty/jetty.project/issues/7958). We recommend that you update your Java on a compatible Enterprise Edition version.

### Java runtime compatibility

By default, App Engine includes an EE embedded web server in your Java project. Starting from Java 25, App Engine the EE web server is installed during deployment. Google periodically publishes a [new version of the JAR](https://repo1.maven.org/maven2/com/google/appengine/runtime-impl). App Engine uses the latest version of the EE embedded web server whenever you redeploy your application.

Refer to the following table to understand which Java versions are compatible with your versions of servlet. For more details on the entry-point features, system property configurations, resulting Jetty support, and compatible EE Versions, see [Entry Point Features](https://github.com/GoogleCloudPlatform/appengine-java-standard?tab=readme-ov-file#entry-point-features).

Enterprise Edition (EE) | Java version | Servlet | Compatibility  
---|---|---|---  
EE7 | 11 | 2.5 or 3.1 | There is no community support for EE7. Java 11 has reached [end of support](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#end_of_support). We recommend that you upgrade your app to use the [latest version of Java](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#java).  
EE7 | 17 | 2.5 or later | There is no community support for EE7. We recommend that you upgrade your app to use EE 8 and later versions.  
EE 8 | 17/21/25 | 2.5 and later | Java EE 8 is backward compatible with Java EE6 and later. For more information, see Upgrade Java on a compatible Enterprise Edition (EE) version.  
EE 10 | 17/21 | 6.0 (default, recommended). Java 21 is configured to run EE 10 by default. | To use Java EE 10, update your application servlets and dependencies to include the `Jakarta` namespace. For more information, see Upgrade Java on a compatible Enterprise Edition (EE) version. You can't use Java 25 on EE10.  
EE 11 | 25 | 6.1 (default, recommended). Java 25 is configured to run EE 11 by default. | To use Java EE 11, update your application servlets and dependencies to include the `Jakarta` namespace. For more information, see Upgrade Java on a compatible Enterprise Edition (EE) version.  
  
## Upgrade Java on a compatible Enterprise Edition (EE) version

To use Java 25 on [Enterprise Edition 11 (EE 11)](https://jakarta.ee/release/11/), or Java 21 on [Enterprise Edition 10 (EE 10)](https://jakarta.ee/release/10/), upgrade your application servlets and dependencies in your Maven and Gradle files to include the `Jakarta` namespace:

###  Java 25 (EE 11) 

To use Java 25 on [Enterprise Edition 11 (EE 11)](https://jakarta.ee/release/11/), follow these steps:

  1. Change the version number in your `web.xml` configuration file to `version=6.1`. For example:
         
         <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_1.xsd"
               version="6.1">
               ...
             </web-app>
         

  2. Rename your application servlets and dependencies from `javax.servlet.*` to `jakarta.servlet.*`:
         
         import jakarta.servlet.ServletException;
             import jakarta.servlet.annotation.WebServlet;
             import jakarta.servlet.http.Cookie;
             import jakarta.servlet.http.HttpServlet;
             import jakarta.servlet.http.HttpServletRequest;
             import jakarta.servlet.http.HttpServletResponse;
         
             @WebServlet(name = "viewer", urlPatterns = {"/view"})
             public class MyServlet extends HttpServlet {
             ......
         

  3. Update your remaining application third-party dependencies to newer Java artifacts, depending on the `Jakarta` namespace.

  4. Add the following system property in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#system_properties) file:
         
         <?xml version="1.0" encoding="utf-8"?>
         <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
             <runtime>java25</runtime>
             <system-properties>
               <property name="appengine.use.EE11" value="true"/>
             </system-properties>
             <app-engine-apis>true</app-engine-apis>
         </appengine-web-app>
         

  5. Optional: Java 25 includes support for virtual threads. To enable virtual threads, add the `appengine.use.virtualthreads` property within the `system-properties` tag in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#system_properties) file.




###  Java 21 (EE 10) 

To use Java 21 on [Enterprise Edition 10 (EE 10)](https://jakarta.ee/release/10/), follow these steps:

  1. Change the version number in your `web.xml` configuration file to `version=6.0`. For example:
         
         <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee https://jakarta.ee/xml/ns/jakartaee/web-app_6_0.xsd"
               version="6.0">
               ...
             </web-app>
         

  2. Rename your application servlets and dependencies from `javax.servlet.*` to `jakarta.servlet.*`:
         
         import jakarta.servlet.ServletException;
             import jakarta.servlet.annotation.WebServlet;
             import jakarta.servlet.http.Cookie;
             import jakarta.servlet.http.HttpServlet;
             import jakarta.servlet.http.HttpServletRequest;
             import jakarta.servlet.http.HttpServletResponse;
         
             @WebServlet(name = "viewer", urlPatterns = {"/view"})
             public class MyServlet extends HttpServlet {
             ......
         

  3. Update your remaining application third-party dependencies to newer Java artifacts, depending on the `Jakarta` namespace.

  4. Add the following system property in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#system_properties) file:
         
         <?xml version="1.0" encoding="utf-8"?>
         <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
             <runtime>java21</runtime> <!-- or java17 -->
             <system-properties>
               <property name="appengine.use.EE10" value="true"/>
             </system-properties>
             <app-engine-apis>true</app-engine-apis>
         </appengine-web-app>
         

  5. Optional: Java 21 includes support for virtual threads. To enable virtual threads, you add the `appengine.use.virtualthreads` property within the `system-properties` tag in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#system_properties) file.




###  Java 17 and later (EE 8) 

Use `javax.servlet.*` APIs on Java EE 8 without major application configuration changes. EE 8 offers backward compatibility for Java EE 6 and later.

To run your applications on Java EE 8, declare a new `system-properties` tag in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#system_properties) file with the non-default `app.engine.use.EE8` configuration:
    
    
      <?xml version="1.0" encoding="utf-8"?>
      <appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
          <runtime>java17</runtime>
          <system-properties>
            <property name="appengine.use.EE8" value="true"/>
          </system-properties>
          <app-engine-apis>true</app-engine-apis>
      </appengine-web-app>
    

Optional: Java version 21 and later includes support for virtual threads. To enable virtual threads, add the `appengine.use.virtualthreads` property within the `system-properties` tag. Example: `<property name="appengine.use.virtualthreads" value="true"/>`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
