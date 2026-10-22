---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/java-callout-runtime-errors/
title: JavaCallout policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:42.862406+00:00
---

# JavaCallout policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/java-callout-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  JavaCallout policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/java-callout-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/java-callout-runtime-errors/).

## ExecutionError

### Error Code
    
    
    steps.javacallout.ExecutionError
    

### Error response body
    
    
    {
      "fault": {
        "faultstring": "Execution returned an error result",
        "detail": {
          "errorcode": "flow.execution.ExecutionReturnedFailure"
        }
      }
    }
    

### Cause

This error occurs if Java code throws an exception or returns _null_ during the execution of a [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy).

### Diagnosis

  1. Start a [trace session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace) to capture the error and identify which [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) has failed.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/java-callout-runtime-error-1.png)

  2. Examine the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) and the resource that is used. In the above example, the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) uses a resource named `hello.jar`, as shown below:
         
         <JavaCallout name="hello-java">
            <ClassName>com.apigeesample.HelloJava</ClassName>
            <ResourceURL>java://hello.jar</ResourceURL>
         </JavaCallout>
         
         

  3. Capture and store the Java exception in a flow variable by modifying the source code, as described in [Handling errors in JavaCallout policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-handle-java-callout-errors).

  4. Compile and replace the affected resource (JAR file) with the updated Java artifact.

  5. Deploy the API Proxy as a new revision and make the API call.

  6. Start another trace session.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/java-callout-runtime-error-2.png)

  7. Notice that a stack trace is available in the `JAVA_STACKTRACE` variable. The stack trace lists the actual exception and the Java source file and line number at which the error is being thrown.

  8. Use this information to fix the issue in the Java code.

  9. In this example, the [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) failed due to an ArithmeticException (division by zero) in the `JavaError.java` file at line #25.




### Resolution

  1. Depending on the exception thrown, fix the issue in the relevant Java source file(s). a. In the example shown above, the issue was caused by an arithmetic error (division by zero). Go to the specific source file and line number indicated by the stack trace.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/java-callout-runtime-error-3.png)

b. Since you cannot perform division by zero, remove the complete else block containing the faulty line of code to resolve the problem.

  2. Replace the relevant JAR file containing the modified files at the appropriate level (API proxy, environment or organization), where it previously existed.

  3. Save and deploy the API proxy as a new revision.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
