---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-use-properties-java-callout/
title: How to use properties in the JavaCallout \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:15.873412+00:00
---

# How to use properties in the JavaCallout  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-use-properties-java-callout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  How to use properties in the JavaCallout Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What is a Java callout?

If you're new to JavaCallouts, we recommend that you start with [How to create a Java callout](https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-create-java-callout).

## Using properties in JavaCallout policies

Properties let you specify name/value pairs in a JavaCallout policy that you can access from your Java code at runtime. You must specify a literal string value for each property; you cannot reference flow variables in this element.

Let's walk through a simple JavaCallout policy example that uses properties. In this example, we create a proxy with that includes a JavaCallout policy. The policy uses the `<Properties>` element to specify a name/value pair. In the Java code, we retrieve the value and use it to set a response header.

### Download the project

To make things simple, you can download this project from the Apigee [api-platform-samples](https://github.com/apigee/api-platform-samples) repository on GitHub.

  1. Download or clone [api-platform-samples](https://github.com/apigee/api-platform-samples) to your system.
  2. In a terminal or code editor of your choice, go to the `api-platform-samples/doc-samples/java-properties` project.



### The JavaCallout policy

The policy uses the `<Properties>` element. This element lets you specify name/value pairs. At runtime, your Java code can access the values of the properties specified in the policy, as we'll see shortly.
    
    
    <JavaCallout name="java-callout">
        <ClassName>com.apigeesample.JavaProperties</ClassName>
        <ResourceURL>java://edge-custom-policy-java-properties.jar</ResourceURL>
        <Properties>
            <Property name="prop">WORLD!</Property>
        </Properties>
    </JavaCallout>

### The sample Java code

The Java code for this sample shows you how to retrieve a property that was specified in the JavaCallout policy. In the sample project, you can find the source code in `java-properties/callout/src/main/java/JavaProperties.java`. We'll walk through the steps for compiling and deploying this code later in this topic.
    
    
    package com.apigeesample;
    
    import com.apigee.flow.execution.ExecutionContext;
    import com.apigee.flow.execution.ExecutionResult;
    import com.apigee.flow.execution.spi.Execution;
    import com.apigee.flow.message.MessageContext;
    
    import java.util.Map;
    
    public class JavaProperties implements Execution {
    
    	private Map <String,String> properties; // read-only
    
    	public JavaProperties(Map <String,String> properties) {
    	        this.properties = properties;
    	}
    
    	public ExecutionResult execute(MessageContext messageContext, ExecutionContext executionContext) {
    
    		try {
    
    		    messageContext.getMessage().setHeader("X-PROPERTY-HELLO", this.properties.get("prop"));
    
                return ExecutionResult.SUCCESS;
    
    		} catch (Exception e) {
    			return ExecutionResult.ABORT;
    		}
    	}
    }

**Note:** To retrieve the properties specified in the policy, all you need to do is implement the Execution class constructor as shown above. Then, in the Java code, you can get the property value you want by name.

### Compile your code with Maven

The project is set up so that you can compile with Maven. If you want to use `javac`, we'll include an example as well.

**Note:** The POM file and configuration for the Maven compile should work, but are offered in the Git repository as an example only. You may need to make adjustments for your environment. If you make changes to the sample code, you may also need to adjust the Maven configuration. 

  1. Be sure that you have Maven installed: 
         
         mvn -version

  2. Execute the script `java-properties/buildsetup.sh`. This script installs the required JAR dependencies in your local Maven repo.
  3. cd to the `java-properties/callout` directory.
  4. Execute Maven: 
         
         mvn clean package

**Note:** If you get a Maven error, be sure that you are in the `java-properties/callout` directory.
  5. If you wish, verify that the JAR file `edge-custom-policy-java-properties.jar` was copied to `java-properties/apiproxy/resources/java`. This is the required location for JAR files that you wish to deploy with a proxy.



### Compile with javac (optional)

If you want to use `javac` to compile the code, you can do something similar to the following (from the `java-properties` directory). The required JAR files are provided for you in the `java-properties/lib` directory.

  1. cd to `api-platform-samples/doc-samples/java-properties`.
  2. Be sure you have javac in your path.  
  

         
         javac -version

  3. Execute the following javac command:  
  

         
         javac -d . -classpath ./lib/expressions-1.0.0.jar:./lib/message-flow-1.0.0.jar:. callout/src/main/java/JavaProperties.java

  4. Create a JAR file:  
  
`jar -cvf edge-custom-policy-java-properties.jar ./com/apigeesample/JavaProperties.class`  

  5. Copy the JAR file to the apiproxy/resources/java directory. This is the required location for JAR files that you wish to deploy with a proxy.  

         
         cp edge-custom-policy-java-properties.jar apiproxy/resources/java




### Deploy and call the proxy

A deploy script is provided in the `./java-properties` directory. But before you run it, you need to do a quick setup.

  1. cd to `api-platform-samples/doc-samples/java-properties`
  2. The simplest way to deploy the proxy is to bundle it in a zip file and upload the proxy bundle to an environment in your Apigee organization. See [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy). Be sure to use the **Upload Proxy Bundle** option. See also [ Tips and tricks for uploading API proxy in a proxy bundle](https://discuss.google.dev/t/tips-and-tricks-for-uploading-api-proxy-in-proxy-bundle/12956.html) in the Apigee community. 
  3. When the proxy is deployed, try calling it:  

         
         curl  https://$HOSTNAME/java-properties

The proxy returns the header: `X-PROPERTY-HELLO: WORLD!`. Remember that in the policy, we added a property name/value pair `"prop/WORLD!"`. The JavaCallout policy retrieves the value `"WORLD!"` and sets it in a header called `X-PROPERTY-HELLO`:
         
         messageContext.getMessage().setHeader("X-PROPERTY-HELLO", this.properties.get("prop"));




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
