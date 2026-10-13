---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-handle-java-callout-errors/
title: How to handle JavaCallout policy errors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:45.935379+00:00
---

# How to handle JavaCallout policy errors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-handle-java-callout-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  How to handle JavaCallout policy errors Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What is a Java Callout?

If you're new to JavaCallout, we recommend that you start with [How to create a Java callout](https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-create-java-callout).

## Handling errors in JavaCallout policies

When you write a JavaCallout policy, you may want to do custom error handling in your Java code. For example, you may wish to return custom error messages and headers and/or set flow variables with error information in the proxy flow on Apigee.

Let's walk through a simple JavaCallout policy example that illustrates basic custom error handling patterns. The sample returns a custom error message when an exception occurs. It also places the error stacktrace into a flow variable, which can be a handy debugging technique.

**Tip:** See also [this community post](https://discuss.google.dev/t/how-to-continue-on-error-in-a-java-callout/10400) about handling errors in Java callout code. 

### Download the project

To make things simple, you can download this project from the Apigee [api-platform-samples](https://github.com/apigee/api-platform-samples) repository on GitHub.

  1. Download or clone [api-platform-samples](https://github.com/apigee/api-platform-samples) to your system.
  2. In a terminal or code editor of your choice, go to the `api-platform-samples/doc-samples/java-error` project.



### The sample Java code

The error handling patterns are straightforward. You can set flow variables in the current Apigee flow context with the `messageContext.setVariable()` method. To return custom error information, construct an `ExecutionResult` instance and call methods on it to set the error response and headers.
    
    
    package com.apigeesample;
    
    import com.apigee.flow.execution.ExecutionContext;
    import com.apigee.flow.execution.ExecutionResult;
    import com.apigee.flow.execution.spi.Execution;
    import com.apigee.flow.message.MessageContext;
    import com.apigee.flow.execution.Action;
    
    import org.apache.commons.lang.exception.ExceptionUtils;
    
    
    public class JavaError implements Execution {
        public ExecutionResult execute(MessageContext messageContext, ExecutionContext executionContext) {
    
            try {
    
                    String name = messageContext.getMessage().getHeader("username");
    
                    if (name != null && name.length()>0) {
                            messageContext.getMessage().setContent("Hello, " + name + "!");
                            messageContext.getMessage().removeHeader("username");
    
                    } else {
                            throw new RuntimeException("Please specify a name parameter!");
                    }
    
                    return ExecutionResult.SUCCESS;
    
            } catch (RuntimeException ex) {
    
                ExecutionResult executionResult = new ExecutionResult(false, Action.ABORT);
    
                //--Returns custom error message and header
                executionResult.setErrorResponse(ex.getMessage());
                executionResult.addErrorResponseHeader("ExceptionClass", ex.getClass().getName());
    
                //--Set flow variables -- may be useful for debugging.
                messageContext.setVariable("JAVA_ERROR", ex.getMessage());
                messageContext.setVariable("JAVA_STACKTRACE", ExceptionUtils.getStackTrace(ex));
                return executionResult;
            }
        }
    }

###   
Compile your code with Maven

The project is set up so that you can compile with Maven. If you want to use `javac`, we'll include an example as well.

**Note:** The POM file and configuration for the Maven compile should work, but are offered in the Git repository as an example only. You may need to make adjustments for your environment. If you make changes to the sample code, you may also need to adjust the Maven configuration. 

  1. Be sure that you have Maven installed: 
         
         mvn -version

  2. Execute the script `java-error/buildsetup.sh`. This script installs the required JAR dependencies in your local Maven repo.
  3. cd to the `java-error/callout` directory.
  4. Execute Maven: 
         
         mvn clean package

**Note:** If you get a Maven error, be sure that you are in the `java-error/callout` directory.
  5. If you wish, verify that the JAR file `edge-custom-policy-java-error.jar` was copied to `java-error/apiproxy/resources/java`. This is the required location for JAR files that you wish to deploy with a proxy.



### Deploy and call the proxy

A deploy script is provided in the `./java-error` directory. But before you run it, you need to do a quick setup.

  1. cd to `api-platform-samples/doc-samples/java-error`
  2. The simplest way to deploy the proxy is to bundle it in a zip file and upload the proxy bundle to an environment in your Apigee organization. See [Creating an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-create-proxy). Be sure to use the **Upload Proxy Bundle** option. See also [ Tips and tricks for uploading API proxy in a proxy bundle](https://discuss.google.dev/t/tips-and-tricks-for-uploading-api-proxy-in-proxy-bundle/12956) in the Apigee community. 
  3. When the proxy is deployed, try calling it:  

         
         curl  https://$HOSTNAME/java-error

Because the call does not include a "name" query parameter, the Java code throws a runtime error. The proxy returns this message and header:



  * Error message: `Please specify a name parameter!`
  * Header: `ExceptionClass: java.lang.RuntimeException`

**Note:** If you look at the Debug Tool in the Apigee UI, you'll see that a flow variable is set called JAVA_STACKTRACE. This is a useful technique for debugging, rather than returning a stacktrace to the client.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
