---
url: https://docs.cloud.google.com/functions/1stgendocs/concepts/jvm-langs/
title: JVM Languages \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:30.381408+00:00
---

# JVM Languages  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/concepts/jvm-langs/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# JVM Languages

It's possible to write your function in using different JVM languages (such as [Kotlin](https://kotlinlang.org/), [Groovy](https://groovy-lang.org/), or [Scala](https://www.scala-lang.org/)) as long as they conform to the following rules:

  * The function is a public class that implements one of the function interfaces ([`HttpFunction`](https://javadoc.io/static/com.google.cloud.functions/functions-framework-api/1.0.1/com/google/cloud/functions/HttpFunction.html), [`BackgroundFunction`](https://javadoc.io/static/com.google.cloud.functions/functions-framework-api/1.0.1/com/google/cloud/functions/BackgroundFunction.html), or [`RawBackgroundFunction`](https://javadoc.io/static/com.google.cloud.functions/functions-framework-api/1.0.1/com/google/cloud/functions/RawBackgroundFunction.html)) and has a public no-argument constructor.

  * If you are deploying from source:

    * It can be built from Maven.
    * The build file contains all the plugins to produce compiled classes.
  * If you are deploying from a pre-built JAR:

    * You can use any build tools to produce this JAR.
    * The pre-built JAR must be a Fat JAR with all of its dependency classes, or its manifest must contain a [`Class-Path`](https://docs.oracle.com/javase/tutorial/deployment/jar/downman.html) entry with the relative locations of jars containing those dependency classes.



## HTTP function examples

You use [HTTP functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-http-functions) when you want to invoke your function via an HTTP(S) request. The following examples output the message `"Hello World!"`

### Kotlin
    
    
    import com.google.cloud.functions.HttpFunction
    import com.google.cloud.functions.HttpRequest
    import com.google.cloud.functions.HttpResponse
    import java.io.IOException
    import java.util.logging.Logger
    
    class HelloWorld : HttpFunction {
        // Simple function to return "Hello World"
        @Throws(IOException::class)
        override fun service(request: HttpRequest, response: HttpResponse) {
            response.writer.write("Hello World!")
        }
    }

### Groovy
    
    
    import com.google.cloud.functions.HttpFunction
    import com.google.cloud.functions.HttpRequest
    import com.google.cloud.functions.HttpResponse
    
    class GroovyHelloWorld implements HttpFunction {
        @Override
        void service(HttpRequest request, HttpResponse response) {
            response.writer.write("Hello World!")
        }
    }

### Scala
    
    
    class ScalaHelloWorld extends HttpFunction {
      override def service(httpRequest: HttpRequest, httpResponse: HttpResponse): Unit = {
        httpResponse.getWriter.write("Hello World!")
      }
    }

### `pom.xml` file for HTTP examples

Here are the `pom.xml` files for the above samples:

### Kotlin
    
    
    <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
    
      <groupId>com.example.functions</groupId>
      <artifactId>functions-kotlin-hello-world</artifactId>
    
    
      <properties>
        <maven.compiler.target>11</maven.compiler.target>
        <maven.compiler.source>11</maven.compiler.source>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <kotlin.version>1.9.22</kotlin.version>
      </properties>
    
      <dependencies>
        <!-- Required for Function primitives -->
        <dependency>
          <groupId>com.google.cloud.functions</groupId>
          <artifactId>functions-framework-api</artifactId>
          <version>1.1.0</version>
          <scope>provided</scope>
        </dependency>
    
        <dependency>
          <groupId>org.jetbrains.kotlin</groupId>
          <artifactId>kotlin-stdlib-jdk8</artifactId>
          <version>${kotlin.version}</version>
        </dependency>
        <dependency>
          <groupId>org.jetbrains.kotlin</groupId>
          <artifactId>kotlin-test</artifactId>
          <version>${kotlin.version}</version>
          <scope>test</scope>
        </dependency>
      </dependencies>
    
      <build>
        <plugins>
          <plugin>
            <!--
              Google Cloud Functions Framework Maven plugin
    
              This plugin allows you to run Cloud Functions Java code
              locally. Use the following terminal command to run a
              given function locally:
    
              mvn function:run -Drun.functionTarget=your.package.yourFunction
            -->
            <groupId>com.google.cloud.functions</groupId>
            <artifactId>function-maven-plugin</artifactId>
            <version>0.11.0</version>
            <configuration>
              <functionTarget>functions.HelloWorld</functionTarget>
            </configuration>
          </plugin>
          <plugin>
            <groupId>org.jetbrains.kotlin</groupId>
            <artifactId>kotlin-maven-plugin</artifactId>
            <version>${kotlin.version}</version>
            <executions>
              <execution>
                <id>compile</id>
                <phase>compile</phase>
                <goals>
                  <goal>compile</goal>
                </goals>
                <configuration>
                  <sourceDirs>
                    <source>src/main/kotlin</source>
                  </sourceDirs>
                </configuration>
              </execution>
              <execution>
                <id>test-compile</id>
                <phase>test-compile</phase>
                <goals>
                  <goal>test-compile</goal>
                </goals>
              </execution>
            </executions>
            <configuration>
              <jvmTarget>1.8</jvmTarget>
            </configuration>
          </plugin>
        </plugins>
      </build>
    </project>

### Groovy
    
    
    <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
    
      <groupId>com.example.functions</groupId>
      <artifactId>functions-groovy-hello-world</artifactId>
    
      <properties>
        <maven.compiler.target>11</maven.compiler.target>
        <maven.compiler.source>11</maven.compiler.source>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <groovy.version>3.0.20</groovy.version>
      </properties>
    
      <dependencyManagement>
        <dependencies>
          <dependency>
            <artifactId>libraries-bom</artifactId>
            <groupId>com.google.cloud</groupId>
            <scope>import</scope>
            <type>pom</type>
            <version>26.32.0</version>
          </dependency>
        </dependencies>
      </dependencyManagement>
    
      <dependencies>
        <!-- Required for Function primitives -->
        <dependency>
          <groupId>com.google.cloud.functions</groupId>
          <artifactId>functions-framework-api</artifactId>
          <version>1.1.0</version>
          <scope>provided</scope>
        </dependency>
    
        <!-- Required for groovy samples -->
        <dependency>
          <groupId>org.codehaus.groovy</groupId>
          <artifactId>groovy-all</artifactId>
          <version>${groovy.version}</version>
          <type>pom</type>
        </dependency>
      </dependencies>
    
      <build>
        <plugins>
          <plugin>
            <!--
              Google Cloud Functions Framework Maven plugin
    
              This plugin allows you to run Cloud Functions Java code
              locally. Use the following terminal command to run a
              given function locally:
    
              mvn function:run -Drun.functionTarget=your.package.yourFunction
            -->
            <groupId>com.google.cloud.functions</groupId>
            <artifactId>function-maven-plugin</artifactId>
            <version>0.11.0</version>
            <configuration>
              <functionTarget>functions.GroovyHelloWorld</functionTarget>
            </configuration>
          </plugin>
          <plugin>
            <groupId>org.codehaus.gmavenplus</groupId>
            <artifactId>gmavenplus-plugin</artifactId>
            <version>3.0.2</version>
            <executions>
              <execution>
                <id>groovy-compile</id>
                <phase>process-resources</phase>
                <goals>
                  <goal>addSources</goal>
                  <goal>compile</goal>
                </goals>
              </execution>
            </executions>
            <dependencies>
              <dependency>
                <groupId>org.codehaus.groovy</groupId>
                <artifactId>groovy-all</artifactId>
                <!-- any version of Groovy \>= 1.5.0 should work here -->
                <version>${groovy.version}</version>
                <scope>runtime</scope>
                <type>pom</type>
              </dependency>
            </dependencies>
          </plugin>
        </plugins>
      </build>
    </project>

### Scala
    
    
    <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
      <modelVersion>4.0.0</modelVersion>
    
      <groupId>com.example.functions</groupId>
      <artifactId>functions-scala-hello-world</artifactId>
    
      <properties>
        <maven.compiler.target>11</maven.compiler.target>
        <maven.compiler.source>11</maven.compiler.source>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
      </properties>
    
      <dependencyManagement>
        <dependencies>
          <dependency>
            <artifactId>libraries-bom</artifactId>
            <groupId>com.google.cloud</groupId>
            <scope>import</scope>
            <type>pom</type>
            <version>26.32.0</version>
          </dependency>
        </dependencies>
      </dependencyManagement>
    
      <dependencies>
        <!-- Required for scala samples -->
        <dependency>
          <groupId>org.scala-lang</groupId>
          <artifactId>scala-library</artifactId>
          <version>2.13.5</version>
        </dependency>
    
        <!-- Required for Function primitives -->
        <dependency>
          <groupId>com.google.cloud.functions</groupId>
          <artifactId>functions-framework-api</artifactId>
          <version>1.1.0</version>
          <scope>provided</scope>
        </dependency>
      </dependencies>
    
      <build>
        <plugins>
          <plugin>
            <!--
              Google Cloud Functions Framework Maven plugin
    
              This plugin allows you to run Cloud Functions Java code
              locally. Use the following terminal command to run a
              given function locally:
    
              mvn function:run -Drun.functionTarget=your.package.yourFunction
            -->
            <groupId>com.google.cloud.functions</groupId>
            <artifactId>function-maven-plugin</artifactId>
            <version>0.11.0</version>
            <configuration>
              <functionTarget>functions.ScalaHelloWorld</functionTarget>
            </configuration>
          </plugin>
          <plugin>
            <groupId>net.alchim31.maven</groupId>
            <artifactId>scala-maven-plugin</artifactId>
            <version>4.4.1</version>
            <executions>
              <execution>
                <id>scala-compile</id>
                <phase>process-resources</phase>
                <goals>
                  <goal>add-source</goal>
                  <goal>compile</goal>
                </goals>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </project>

### Deploying the HTTP functions

### Kotlin
    
    
    gcloud functions deploy kotlin-helloworld --entry-point functions.KotlinHelloWorld --no-gen2 --runtime java17 --trigger-http --allow-unauthenticated --memory 512MB
    

### Groovy
    
    
    gcloud functions deploy groovy-helloworld --entry-point functions.GroovyHelloWorld --no-gen2 --runtime java17 --trigger-http --allow-unauthenticated --memory 512MB
    

### Scala
    
    
    gcloud functions deploy scala-helloworld --entry-point functions.ScalaHelloWorld --no-gen2 --runtime java17 --trigger-http --allow-unauthenticated --memory 512MB
    

## Event-driven function examples

You use event-driven functions when you want to have your Cloud Run function invoked indirectly in response to an asynchronous event, such as a message on a Pub/Sub topic, a change in a Cloud Storage bucket, or a Firebase event.

There are two types of [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing#event-driven_functions): background functions and CloudEvent functions. The JVM languages only support [background functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions#background-functions).

### Kotlin
    
    
    import com.google.cloud.functions.BackgroundFunction
    import com.google.cloud.functions.Context
    import functions.eventpojos.PubsubMessage
    import java.nio.charset.StandardCharsets
    import java.util.Base64
    import java.util.logging.Logger
    
    
    class KotlinHelloPubSub : BackgroundFunction<PubsubMessage> {
        override fun accept(message: PubsubMessage, context: Context) {
            // name's default value is "world"
            var name = "world"
            if (message?.data != null) {
                name = String(
                        Base64.getDecoder().decode(message.data!!.toByteArray(StandardCharsets.UTF_8)),
                        StandardCharsets.UTF_8)
            }
            LOGGER.info(String.format("Hello %s!", name))
            return;
        }
    
        companion object {
            private val LOGGER = Logger.getLogger(KotlinHelloPubSub::class.java.name)
        }
    }

When developing background functions, you define classes for the events triggering your functions. However, GSON marshalling may not work out of the box for Kotlin, if your event class doesn't follow [certain guidelines](https://medium.com/@programmerr47/gson-unsafe-problem-d1ff29d4696f).

In your Kotlin event class, properties must conform to these guidelines:

  * They are able to be set to `null`.
  * They don't have a default value assigned to them.
  * They are not delegate properties.



Another approach is to create your event classes in Java, and use them from your Kotlin function class.

### Groovy
    
    
    import com.google.cloud.functions.BackgroundFunction
    import com.google.cloud.functions.Context
    import functions.eventpojos.PubsubMessage
    import java.nio.charset.StandardCharsets
    import java.util.logging.Logger
    
    class GroovyHelloPubSub implements BackgroundFunction<PubsubMessage> {
        private static final Logger LOGGER = Logger.getLogger(GroovyHelloPubSub.class.name)
    
        @Override
        void accept(PubsubMessage message, Context context) {
            // name's default value is "world"
            String name = "world"
    
            if (message?.data) {
                 name = new String(Base64.decoder.decode(message.data), StandardCharsets.UTF_8)
            }
    
            LOGGER.info("Hello ${name}!")
            return
        }
    }

### Scala
    
    
    import java.nio.charset.StandardCharsets
    import java.util.Base64
    import java.util.logging.Logger
    
    import com.google.cloud.functions.{BackgroundFunction, Context}
    import functions.eventpojos.PubsubMessage
    
    class ScalaHelloPubSub extends BackgroundFunction[PubsubMessage] {
    
      val LOGGER = Logger.getLogger(this.getClass.getName)
    
      override def accept(message: PubsubMessage, context: Context): Unit = {
        // name's default value is "world"
        var name = "world"
        if (message != null && message.getData != null) {
          name = new String(Base64.getDecoder.decode(
            message.getData.getBytes(StandardCharsets.UTF_8)), StandardCharsets.UTF_8)
        }
        LOGGER.info(String.format("Hello %s!", name))
      }
    }

### Deploying the background functions

### Kotlin
    
    
    gcloud functions deploy kotlin-hello-pubsub --entry-point functions.KotlinHelloPubSub --no-gen2 --runtime java17 --trigger-topic my-topic --allow-unauthenticated --memory 512MB
    

### Groovy
    
    
    gcloud functions deploy groovy-hello-pubsub --entry-point functions.GroovyHelloPubSub --no-gen2 --runtime java17 --trigger-topic my-topic --allow-unauthenticated --memory 512MB
    

### Scala
    
    
    gcloud functions deploy scala-hello-pubsub --entry-point functions.ScalaHelloPubSub --no-gen2 --runtime java17 --trigger-topic my-topic --allow-unauthenticated --memory 512MB
    

### Test the background examples

You can test the background examples as follows:

  1. Publish a message to your Pub/Sub Topic to trigger your function:
         
         gcloud pubsub topics publish my-topic --message Flurry

  2. Look at the logs:
         
         gcloud functions logs read --limit 10




You should see something like this, with a message that includes the name you published to the Pub/Sub topic:
    
    
    D      my-function  ...  Function execution started
    I      my-function  ...  Hello Flurry!
    D      my-function  ...  Function execution took 39 ms, finished with status: 'ok'
    

**Note:** log messages may be delayed by a few minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
