---
url: https://docs.cloud.google.com/appengine/docs/flexible/java/war-packaging/
title: Re-package a WAR file into a JAR file \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:44.884642+00:00
---

# Re-package a WAR file into a JAR file  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/java/war-packaging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Re-package a WAR file into a JAR file Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** Java 8 has reached end of support. We recommend that you migrate your application to use a [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) of Java.

This document describes how to re-package a Java 8 application as a JAR file to run on a [supported Java](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) runtime. To use a supported Java runtime, you can either embed a server like Jetty or containerize your application with Docker for a custom runtime without completely rewriting your application. You can run your existing WAR applications on modern Java platforms or flexible cloud environments. Choose from the following methods that best suits your deployment strategy and infrastructure:

  * Use Dockerfiles to deploy your application (recommended)
  * Use an embedded Java runtime (Jetty)



## Prepare your Java 8 web application (WAR file)

Before you re-package your Java 8 application as a supported JAR file, you must build a WAR file. This section provides a sample Java 8 application that builds a WAR file. Follow the instructions to create a Java 8 `hello-world` application:

  1. Create a `HelloServlet.java` file in your source directory:
         
         import java.io.IOException;
         import javax.servlet.ServletException;
         import javax.servlet.annotation.WebServlet;
         import javax.servlet.http.HttpServlet;
         import javax.servlet.http.HttpServletRequest;
         import javax.servlet.http.HttpServletResponse;
         
         @WebServlet("/hello")
         public final class HelloServlet extends HttpServlet {
           /**
            * This method handles GET requests to the /hello endpoint.
            *
            * <p>Subclasses should not override this method.
            *
            * @param request the HttpServletRequest object
            * @param response the HttpServletResponse object
            * @throws ServletException if a servlet-specific error occurs
            * @throws IOException if an I/O error occurs
            */
           @Override
           protected void doGet(
               final HttpServletRequest request, final HttpServletResponse response)
               throws ServletException, IOException {
             response.setContentType("text/html");
             response.getWriter().println("<h1>Hello, World!</h1>");
           }
         }

  2. Create a `web.xml` deployment descriptor file to configure your web application:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
                  version="4.0">
         
             <welcome-file-list>
                 <welcome-file>index.jsp</welcome-file>
             </welcome-file-list>
         
         </web-app>

  3. Create a landing page `index.jsp`:
         
         <%@ page contentType="text/html;charset=UTF-8" language="java" %>
         <html>
         <head>
             <title>Hello App Engine</title>
         </head>
         <body>
             <h1>Welcome to Google App Engine!</h1>
             <p><a href="hello">Say Hello</a></p>
         </body>
         </html>
         

  4. Add the following code in the `pom.xml` file to define the build for your Java 8 application:

     * WAR packing configuration:
           
           <groupId>com.example</groupId>
           <artifactId>HelloWorldApp</artifactId>
           <version>1.0</version>
           <packaging>war</packaging>
           

     * `maven-war-plugin` plugin with the `maven.compiler` source and target set to version `1.8`:
           
           <properties>
               <maven.compiler.source>1.8</maven.compiler.source>
               <maven.compiler.target>1.8</maven.compiler.target>
               <java.version>8</java.version>
           </properties>
           

     * `javax.servlet-api` dependency:
           
           <dependencies>
               <dependency>
                   <groupId>javax.servlet</groupId>
                   <artifactId>javax.servlet-api</artifactId>
                   <version>3.1.0</version>
                   <scope>provided</scope>
               </dependency>
           </dependencies>
           

     * Maven configuration:
           
           <build>
                 <plugins>
                     <plugin>
                         <groupId>org.apache.maven.plugins</groupId>
                         <artifactId>maven-compiler-plugin</artifactId>
                         <version>3.8.1</version> <configuration>
                             <source>${maven.compiler.source}</source>
                             <target>${maven.compiler.target}</target>
                         </configuration>
                     </plugin>
           
                     <plugin>
                         <groupId>org.apache.maven.plugins</groupId>
                         <artifactId>maven-war-plugin</artifactId>
                         <version>3.3.2</version>
                     </plugin>
           
                 </plugins>
             </build>
           

Your project directory should be similar to the following structure:
    
    ├── pom.xml
    └── src
        └── main
            ├── java
            │   └── com
            │       └── example
            │           └── HelloServlet.java
            └── webapp
                ├── WEB-INF
                │   └── web.xml
                └── index.jsp
    
    

  5. Run `mvn install` in your application's project directory to generate the WAR file `HelloWorldApp-1.0.war` in the target directory.




## Use Dockerfiles to deploy your application (recommended)

Custom runtimes are suitable for platforms supporting custom containers, such as [App Engine custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes). Custom runtimes provide flexibility by allowing you to configure the runtime environment. For an example walkthrough of deploying custom runtimes, see [Create a custom runtime app in the App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/create-app).

The following instructions describe how to containerize your Java 8 application using a Dockerfile:

  1. Prepare your Java 8 web application (WAR file)
  2. Build the container image and push it to Artifact Registry
  3. Deploy your application



### Build the container image and push it to Artifact Registry

This section describes how to build a Docker image using Cloud Build and push it to an Artifact Registry repository. Follow these steps to create a container image of your application:

  1. Create a `cloudbuild.yaml` file in your source directory to build the Docker image and push to Artifact Registry:
         
         steps:
         # Step 1: Build the Docker image
         - name: "gcr.io/cloud-builders/docker"
             args:
             - "build"
             - "-t"
             - "$LOCATION-docker.pkg.dev/$PROJECT/$REPOSITORY/SERVICE:VERSION"
             - "."
         
         # Step 2: Push the Docker image to Artifact Registry
         - name: "gcr.io/cloud-builders/docker"
             args:
             - "push"
             - "$LOCATION-docker.pkg.dev/$PROJECT/$REPOSITORY/SERVICE:VERSION"
         
         images:
         - "$LOCATION-docker.pkg.dev/$PROJECT/$REPOSITORY/SERVICE:VERSION"
         

Replace:

     * LOCATION with the Google Cloud region where you deploy your app.
     * PROJECT with your Google Cloud project ID.
     * REPOSITORY with the name of your Artifact Registry repository.
     * IMAGE with your container image URL.
     * TAG with your container image tag.
  2. Create a Dockerfile with the following configuration:
         
         # Use Maven to build the project with JDK 8
         FROM maven:3.8.6-openjdk-8 AS build
         
         # Set working directory
         WORKDIR /app
         
         # Copy the application source code
         COPY . .
         
         # Build the application
         RUN mvn clean package
         
         # Use Jetty as the runtime
         FROM jetty:9.4-jdk8
         
         # Set Jetty working directory
         WORKDIR /var/lib/jetty/webapps
         
         # Copy the built WAR file
         COPY --from=build /app/target/*.war ./ROOT.war
         
         # Expose the default Jetty port
         EXPOSE 8080
         
         # Start Jetty correctly
         CMD ["java", "-Djetty.base=/var/lib/jetty", "-jar", "/usr/local/jetty/start.jar"]

  3. [Download and install Docker](https://docs.docker.com/engine/installation/) to test your sample app, and run the Hello World container on your local machine.

  4. Build the container image and push it to Artifact Registry:
         
         gcloud builds submit .
         




### Deploy your application

To deploy your App Engine application:

  1. Configure your `app.yaml` file to use a custom runtime in the source directory:
         
         runtime: custom
         env: flex
         instance_class: F1
         
         handlers:
           - url: /.*
             script: auto

Your project directory should be similar to the following structure:
         
         ├── Dockerfile
         ├── README.md
         ├── app.yaml
         ├── cloudbuild.yaml
         ├── pom.xml
         └── src
             └── main
                 ├── java
                 │   └── com
                 │       └── example
                 │           └── HelloServlet.java
                 └── webapp
                     ├── WEB-INF
                     │   └── web.xml
                     └── index.jsp
         

  2. Deploy your application using the [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command:
         
         gcloud app deploy --image-url=REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:tag
         

Replace:

     * LOCATION with the Google Cloud region where you deploy your app.
     * PROJECT with your Google Cloud project ID.
     * REPOSITORY with the name of your Artifact Registry repository.
     * IMAGE with your container image URL.
     * TAG with your container image tag.



## Use an embedded Java runtime

The following instructions demonstrate how to re-package an App Engine Java 8 application with an embedded server (Jetty) to run as a standalone JAR on a [supported Java](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) runtime:

  1. Create an embedded Jetty server
  2. Prepare your Java 8 web application (WAR file)
  3. Run the WAR file with embedded Jetty and deploy your application



### Create an Embedded Jetty server

To bundle your application WAR file with an embedded Jetty server, follow these steps:

  1. Create a `Main` class to initialize and configure the Jetty server to run your WAR file. The `Main` class sets up the server port that defaults to `8080`. You can also modify the source code to use a port specified in the `PORT` environment variable. The `Main` class configures the `WebAppContext` handler to serve your WAR file:
         
         import org.eclipse.jetty.server.Server;
         import org.eclipse.jetty.webapp.Configuration.ClassList;
         import org.eclipse.jetty.webapp.WebAppContext;
         
         /** Simple Jetty Main that can execute a WAR file when passed as an argument. */
         public class Main {
         
           public static void main(String[] args) throws Exception {
             if (args.length != 1) {
               System.err.println("Usage: need a relative path to the war file to execute");
               System.exit(1);
             }
             System.setProperty("org.eclipse.jetty.util.log.class", "org.eclipse.jetty.util.log.StrErrLog");
             System.setProperty("org.eclipse.jetty.LEVEL", "INFO");
         
             // Create a basic Jetty server object that will listen on port defined by
             // the PORT environment variable when present, otherwise on 8080.
             int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
             Server server = new Server(port);
         
             // The WebAppContext is the interface to provide configuration for a web
             // application. In this example, the context path is being set to "/" so
             // it is suitable for serving root context requests.
             WebAppContext webapp = new WebAppContext();
             webapp.setContextPath("/");
             webapp.setWar(args[0]);
             ClassList classlist = ClassList.setServerDefault(server);
         
             // Enable Annotation Scanning.
             classlist.addBefore(
                 "org.eclipse.jetty.webapp.JettyWebXmlConfiguration",
                 "org.eclipse.jetty.annotations.AnnotationConfiguration");
         
             // Set the the WebAppContext as the ContextHandler for the server.
             server.setHandler(webapp);
         
             // Start the server! By using the server.join() the server thread will
             // join with the current thread. See
             // "http://docs.oracle.com/javase/1.5.0/docs/api/java/lang/Thread.html#join()"
             // for more details.
             server.start();
             server.join();
           }
         }

  2. Create the Maven project file `pom.xml` and add the following configuration:

     1. Set the `maven.compiler.source` and `maven.compiler.target` properties to a [supported Java](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) runtime:
            
            <properties>
              <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
              <maven.compiler.source>21</maven.compiler.source>
              <maven.compiler.target>21</maven.compiler.target>
              <jetty.version>9.4.57.v20241219</jetty.version>
            </properties>

     2. Add dependencies for Jetty:
            
            <dependencies>
              <!-- Embedded Jetty dependencies -->
              <dependency>
                <groupId>org.eclipse.jetty</groupId>
                <artifactId>jetty-server</artifactId>
                <version>${jetty.version}</version>
              </dependency>
              <dependency>
                <groupId>org.eclipse.jetty</groupId>
                <artifactId>jetty-webapp</artifactId>
                <version>${jetty.version}</version>
                <type>jar</type>
              </dependency>
              <dependency>
                <groupId>org.eclipse.jetty</groupId>
                <artifactId>jetty-util</artifactId>
                <version>${jetty.version}</version>
              </dependency>
              <dependency>
                <groupId>org.eclipse.jetty</groupId>
                <artifactId>jetty-annotations</artifactId>
                <version>${jetty.version}</version>
              </dependency>
              <!-- extra explicit dependency needed because there is a JSP in the sample-->
              <dependency>
                <groupId>org.eclipse.jetty</groupId>
                <artifactId>apache-jsp</artifactId>
                <version>${jetty.version}</version>
              </dependency>
            </dependencies>

     3. Configure the `maven-assembly-plugin` property to package dependencies:
            
            <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-assembly-plugin</artifactId>
              <version>3.0.0</version>
              <configuration>
                <finalName>jetty</finalName>
                <descriptorRefs>
                  <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>
                <archive>
                  <manifest>
                    <mainClass>com.example.appengine.jetty.Main</mainClass>
                  </manifest>
                </archive>
              </configuration>
              <executions>
                <execution>
                  <id>make-assembly</id>
                  <phase>package</phase>
                  <goals>
                    <goal>single</goal>
                  </goals>
                </execution>
              </executions>
            </plugin>
            

Your project directory should be similar to the following structure:
    
    ├─src
    │  └─main
    │      └─java
    │          └─jetty
    │              └─Main.java
    └─pom.xml
    

  3. Run the `mvn install` command in the Jetty runner project directory. This generates the `jetty-jar-with-dependencies.jar` in your target directory.

  4. Follow the instructions in the Prepare your Java 8 web application (WAR file) section to create a WAR file.




### Run the WAR file with embedded Jetty and deploy your application

This section provides steps for packaging your application into an executable JAR file. Follow these instructions to package and deploy your application:

  1. Place the generated Jetty runner JAR `jetty-jar-with-dependencies.jar` and your application WAR file `HelloWorldApp-1.0.war` in the same directory.

  2. Run the application using a [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#java) Java runtime:
         
         java -jar jetty-jar-with-dependencies.jar HelloWorldApp-1.0.war
         

     1. In your web browser, navigate to <http://localhost:8080>. You should see your application's welcome page.
  3. Create an `entrypoint` element in your `app.yaml` file to call the `jetty-jar-with-dependencies` file, and pass your WAR file as an argument. The version you specify in the WAR file must be the same version as the `pom.xml` file:
         
         runtime: java
         env: flex
         runtime_config:
           operating_system: ubuntu22
           runtime_version: 21
         entrypoint: "java -jar jetty-jar-with-dependencies.jar sample.war"
         handlers:
           - url: /.*
             script: this field is required, but ignored
         
         manual_scaling:
           instances: 1

  4. Deploy your application using the [`gcloud app deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
