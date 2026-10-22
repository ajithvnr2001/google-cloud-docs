---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/war-packaging/
title: Re-packaging a WAR file into a JAR file \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:29.552695+00:00
---

# Re-packaging a WAR file into a JAR file  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/war-packaging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Re-packaging a WAR file into a JAR file Stay organized with collections  Save and categorize content based on your preferences. 

If you are migrating to the latest supported Java version and your app does not use legacy bundled services, you must re-package your App Engine web application into an executable JAR file.

Your application must have a `Main` class that starts a web server that responds to HTTP requests on port 8080, which might be specified by the `PORT` environment variable.

For example: 
    
    
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

## WAR migration example (Java 21)

The following instructions demonstrate how to repackage an App Engine `hello-world` WAR application as a JAR to run on the Java 21 runtime.

The migration uses the `appengine-simple-jetty-main` artifact. This provides a `Main` class with a simple Jetty web server that loads a WAR file and packages your app into an executable JAR file:

  1. Clone the Embedded Jetty Server artifact to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/java-docs-samples
         

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/java-docs-samples/archive/master.zip) as a zip file and extract it.

  2. Change to the directory that contains the sample code:
         
         cd java-docs-samples/flexible/repacking-legacy-applications/appengine-simple-jetty-main/
         

  3. Build the Jetty runner JAR:
         
         mvn install
         

This generates `jetty-jar-with-dependencies.jar` in your `target/` directory.

  4. Configure the `pom.xml` build file for the Jetty server:

     * Compiler properties (Java 21): 
           
           <properties>
             <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
             <maven.compiler.source>21</maven.compiler.source>
             <maven.compiler.target>21</maven.compiler.target>
             <jetty.version>9.4.57.v20241219</jetty.version>
           </properties>

     * Embedded Jetty dependencies: 
           
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

     * `maven-assembly-plugin` configuration: 
           
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
           

  5. Place the generated `jetty-jar-with-dependencies.jar` and your application WAR file. For example, `helloworld.war` in the same directory.

  6. Create an `app.yaml` file in your application directory to specify the Java 21 runtime and an `entrypoint` element to call the `jetty-jar-with-dependencies.jar` file and pass your WAR file as an argument:
         
         runtime: java21
         entrypoint: 'java -jar jetty-jar-with-dependencies.jar helloworld.war'
         

  7. To run your application locally:

     1. Start the server with your WAR file as an argument:
            
            java -jar jetty-jar-with-dependencies.jar helloworld.war
            

     2. In your web browser, enter the following address:

<http://localhost:8080>

  8. To deploy your application:

### gcloud tooling
         
         gcloud app deploy

### Maven plugin
         
         mvn package appengine:deploy -Dapp.deploy.projectId=PROJECT_ID

Replace PROJECT_ID with the ID of your Google Cloud project. If your `pom.xml` file already [specifies your project ID](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/maven-reference#appenginedeploy) , you don't need to include the `-Dapp.deploy.projectId` property in the command you run. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
