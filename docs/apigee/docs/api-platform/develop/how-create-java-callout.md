---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-create-java-callout/
title: How to create Java Callout \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:17.625093+00:00
---

# How to create Java Callout  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-create-java-callout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  How to create Java Callout Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What is a Java Callout?

Apigee provides a range of policies that address common API management requirements such as security, data transformation, traffic management, and others.

However, there are some cases where your API requires custom behavior that is not implemented in a standard policy. In these cases, Apigee provides several options that enable you to script or code customized API behavior. One approach is to implement the desired behavior in Java.

Supported Java versions include: Oracle JDK 11 and OpenJDK 11.

**Note:** **Important:** If you are developing JavaCallout policies, you need to know which permission policies are in effect in the Apigee JVM and how they will affect your code. See [Java permission reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/java-permission-reference). .

## How do I use Java code in a proxy?

The JavaCallout policy lets you call Java code from within an executing proxy flow. Your Java code needs to implement certain Apigee-specific Java interfaces that allow the code to interact with the executing proxy. For example, Java methods exist for getting and setting headers, query parameters, flow variables, and other entities within the current flow context of the proxy.

## When should I use the JavaCallout policy?

Let's look at situations where the JavaCallout policy is useful, and situations where you should consider other approaches.

### First, consider alternative approaches

Before using the JavaCallout policy, note that there may be alternative approaches that you can use instead. For example:

  * For lightweight operations, such as HTTP API calls to remote services, consider using the ServiceCallout policy. See [Service Callout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy).
  * For relatively simple interactions with message content, such as modifying or extracting HTTP headers, parameters, or message content, you can use [JavaScript](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy) or [PythonScript](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy) policies.



### What you can do in Java code

The JavaCallout policy supports these basic operations:

  * Examining or manipulating request or response messages
  * Getting and setting flow variables. You can use Java methods to access Apigee flow variables. If you want to access Key Value Map (KVM) information, use a KVM policy, assign KVM values to flow variables, and then you can access the flow variables from within the JavaCallout policy. 
  * Calling external services
  * Raising faults
  * Manipulating error messages and status codes



### What you cannot do in Java code

Most system calls are disallowed. You **cannot** :

  * Make internal file system reads or writes. This means that you cannot use any of the Java packages to read/write into internal file systems; however, you can make external remote calls.
  * Get information about the current process, the process list, or CPU/memory utilization on the machine.
  * Access the source code in `expressions-1.0.0.jar` and `message-flow-1.0.0.jar`.



Although some such calls may work, they are unsupported and liable to be actively disabled at any time. Avoid making such calls in your code.

Do not use or rely on Java libraries that are included with Apigee. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release. If you use such libraries, use them in non-production demonstrations only.

## Hello JavaCallout

Let's go through a basic hello world a JavaCallout policy example. In this example, we create a simple proxy with JavaCallout that returns a "hello world" response. The proxy can return one of two possible responses:

  * If you pass in a "username" header with a "name" value, the proxy returns:  
  

        
        Hello, <name>!

  * If you omit the header, the proxy just returns:  
  

        
        "Hello, Guest!"




### Download the starter project

To make things simple, we have a basic project prepared for you on GitHub in the Apigee [api-platform-samples](https://github.com/apigee/api-platform-samples) repository.

  1. Download or clone [api-platform-samples](https://github.com/apigee/api-platform-samples) to your system. If you already have `api-platform-samples` on your system, do a `pull` to make sure you have the latest version.
  2. In a terminal or code editor of your choice, go to the `api-platform-samples/doc-samples/java-hello` project.



### Write the Java code

  1. Open the Java source file: `java-hello/callout/src/main/java/HelloJava.java`. This file is a skeleton version of the main Java class that we will implement. The imported packages are required for Apigee JavaCallout code. These classes provide methods that allow you to access the proxy execution context. We'll walk through the steps for compiling and deploying this code shortly.  

         
         package com.apigeesample;
         
         import com.apigee.flow.execution.ExecutionContext;
         import com.apigee.flow.execution.ExecutionResult;
         import com.apigee.flow.execution.spi.Execution;
         import com.apigee.flow.message.MessageContext;
         
         
         public class HelloJava implements Execution {
         
                 public ExecutionResult execute(MessageContext messageContext, ExecutionContext executionContext) {
         
                         try {
         
                                 // Your code here.
         
                     return ExecutionResult.SUCCESS;
         
                         } catch (Exception e) {
                                 return ExecutionResult.ABORT;
                         }
                 }
         
         }

  2. Replace the commented line `// Your code here` with the following code:  
  

         
         String name = messageContext.getMessage().getHeader("username");
         
         if (name != null && name.length()>0) {
                 messageContext.getMessage().setContent("Hello, " + name + "!");
                 messageContext.getMessage().removeHeader("username");
         } else {
                 messageContext.getMessage().setContent("Hello, Guest!");
         }

**Note:** **Note:** The **MessageContext** object lets you access entities inside the flow where the JavaCallout policy executes. Let's say the JavaCallout policy is attached to the Proxy Endpoint Response flow. The code listed above gets the HTTP Message object for that flow context. The **Message** object, in turn, gives you access to headers, query parameters, body content, and flow variables.
  3. Save the file.



###   
Compile your code with Maven

**Note:** The POM file and configuration for the Maven compile should work, but are offered in the Git repository as an example only. You may need to make adjustments for your environment. If you make changes to the sample code, you may also need to adjust the Maven configuration. 

  1. Be sure that you have Maven installed:  
  

         
         mvn -version

  2. Install the required JAR dependencies in your local Maven repo using one of the following methods: 
     * Add the following snippet to the `pom.xml` file to downoad the required JAR dependencies from [ Artifact Registry](https://cloud.google.com/artifact-registry): 
           
           <repositories>
             <repository>
               <id>artifact-registry</id>
               <url>https://us-maven.pkg.dev/apigee-release/apigee-java-callout-dependencies</url>
             </repository>
           </repositories>
           
           <dependencies>
             <dependency>
               <groupId>com.apigee.gateway.libraries</groupId>
               <artifactId>message-flow</artifactId>
               <version>1.0.0</version>
               <scope>compile</scope>
               <type>jar</type>
             </dependency>
             <dependency>
               <groupId>com.apigee.infra.libraries</groupId>
               <artifactId>expressions</artifactId>
               <version>1.0.0</version>
               <scope>compile</scope>
               <type>jar</type>
             </dependency>
           </dependencies>

     * Use the following `curl` calls to download the required JAR dependencies from [ Artifact Registry](https://cloud.google.com/artifact-registry): 
           
           curl "https://us-maven.pkg.dev/apigee-release/apigee-java-callout-dependencies/com/apigee/gateway/libraries/message-flow/1.0.0/message-flow-1.0.0.jar" -v -L -o message-flow-1.0-0.jar
                   
           
           curl "https://us-maven.pkg.dev/apigee-release/apigee-java-callout-dependencies/com/apigee/infra/libraries/expressions/1.0.0/expressions-1.0.0.jar" -v -L -o expressions-1.0.0.jar
                   

     * Execute the script `java-hello/buildsetup.sh`. This script downloads the required JAR dependencies from the [Apigee GitHub repository](https://github.com/apigee/api-platform-samples).
  3. cd to the `java-hello/callout` directory.
  4. Execute Maven:  
  

         
         mvn clean package

**Note:** If you get a Maven error, be sure that you are in the `java-hello/callout` directory.
  5. If you wish, verify that the JAR file `edge-custom-policy-java-hello.jar` was copied to `java-hello/apiproxy/resources/java`. This is the required location for JAR files that you wish to deploy with a proxy.



### Deploy and call the proxy

Follow these steps to deploy and test the API proxy:

  1. Change to the `java-hello` directory. 
  2. Zip the API proxy bundle: 
         
         zip apiproxy-bundle.zip -r apiproxy -x \*.\*~

  3. The simplest way to deploy the proxy is to bundle it in a zip file and upload the proxy bundle to an environment in your Apigee organization. See [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy). Be sure to use the **Upload Proxy Bundle** option. See also [ Tips and tricks for uploading API proxy in a proxy bundle](https://discuss.google.dev/t/tips-and-tricks-for-uploading-api-proxy-in-proxy-bundle/12956.html) in the Apigee community. 
  4. When the proxy is deployed, try calling it:  

         
         curl  https://$HOSTNAME/java-hello -H "username:Will"

Which returns "Hello, Will!




### About the proxy

Let's quickly examine the policies used in this proxy. Pay attention to where the policies are positioned in the proxy flow and why.

**The Assign message policy**

An Assign message policy is attached to the ProxyEndpoint **request flow**. It copies the username header from the request and assigns it to the response. This operation allows the JavaCallout policy, which is attached to the response flow, to access the username header and build a custom response body using the value of that header.
    
    
    <AssignMessage async="false" continueOnError="false" enabled="true" name="CopyHeader">
        <DisplayName>CopyHeader</DisplayName>
        <Copy source="request">
            <Headers>
              <Header name="username"/>
            </Headers>
        </Copy>
        <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
        <AssignTo createNew="false" transport="http" type="response"/>
    </AssignMessage>

**The JavaCallout policy**

The JavaCallout policy is attached to the **response flow**. This is because the custom Java code makes changes to the response headers and message. The policy's ClassName element specifies the main class that is executed by the policy. The ResourceURL element is the name of the JAR file that you built and added to the `resources/java` directory of the proxy.
    
    
    <JavaCallout name="hello-java">
        <ClassName>com.apigeesample.HelloJava</ClassName>
        <ResourceURL>java://edge-custom-policy-java-hello.jar</ResourceURL>
    </JavaCallout>

## What you need to know about the JavaCallout policy

Important things to note about implementing the JavaCallout policy are:

  * Imports classes from the `com.apigee.flow.execution` and `com.apigee.flow.message` packages. These packages must be included in the JAR file that is packaged and deployed. You can upload your Java JAR through the Management UI proxy editor, or you can include it in the `/resources/java` directory in API proxies that you develop locally.
  * Implements the Execution interface. Any Java code that is executed within an API proxy must implement Execution. 
  * JavaCallout policy contains no actual code. Instead, the policy references a Java 'resource', which you must package in a JAR.
  * Package names to avoid: Do not use **io.apigee** or **com.apigee** as package names in JavaCallout policies. Those are reserved and used by other Apigee modules.
  * If your JavaCallout policy relies on additional third-party libraries packaged as independent JAR files, then place those JAR files in the `/resources/java` directory as well to ensure that they are loaded correctly at runtime.
  * If there are multiple JARs, simply add them as additional resources. You do not need to modify the policy configuration to refer to additional JAR files. Putting them in `/resources/java` is sufficient.
  * For additional information on uploading Java JARs, see [Resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
