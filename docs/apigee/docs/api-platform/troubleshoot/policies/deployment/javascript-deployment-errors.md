---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/javascript-deployment-errors/
title: JavaScript policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:27.557399+00:00
---

# JavaScript policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/javascript-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  JavaScript policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/javascript-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/javascript-deployment-errors/).

## InvalidResourceUrlFormat

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid resource url format. Resource url is invalid_URL.
    

### Example error message
    
    
    Error Deploying Revision 1 to test
    Invalid resource url format. Resource url is jsc:add_variables.js.
    

### Example screenshot

![Error deploying revision 1 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/javascript-deploy-error-5.png)

### Cause

If the format of the resource URL specified within the `<ResourceURL>` or the `<IncludeURL>` element of the JavaScript policy is invalid, then the deployment of the API proxy fails.

The correct format to specify the resource URL is as shown below:
    
    
    <ResourceURL>jsc://<file_name>.js</ResourceURL>
    <IncludeURL>jsc://<file_name>.js</IncludeURL>
    

For example, if the `<ResourceURL>` element is specified as shown below, then the deployment of the API proxy fails because it does not follow the prescribed pattern:
    
    
    <ResourceURL>jsc:add_variables.js</ResourceURL>
    

### Diagnosis

  1. Identify the invalid resource URL format used in the JavaScript policy. You can find this information from the error message. For example, in the following error, the invalid resource URL format is `jsc:add_variables.js`.
         
         Error Deploying Revision 1 to test
             Invalid resource url format. Resource url is jsc:add_variables.js.
         

  2. Examine all the JavaScript policies in the specific API Proxy where the failure has occurred. If there is any JavaScript policy in which the resource URL specified in the `<ResourceURL>` or the `<IncludeURL>` element matches the invalid entry identified in step #1 above, then that's the cause of the error.

For example, the following policy specifies the resource URL as `jsc:add_variables.js`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-TotalVariable">
             <DisplayName>js-TotalVariable</DisplayName>
             <Properties/>
             <ResourceURL>jsc:add_variables.js</ResourceURL>
         </Javascript>
         

Because the resource URL is specified as `jsc:add_variables.js`, which is invalid, the deployment of the API Proxy fails with the error:
         
         Invalid resource url format. Resource url is jsc:add_variables.js.
         




### Resolution

Ensure that the resource URL format specified in the `<ResourceURL>` or `<IncludeURL>` element of the JavaScript policy is valid. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-TotalVariable">
        <DisplayName>js-TotalVariable</DisplayName>
        <Properties/>
        <ResourceURL>jsc://add_variables.js</ResourceURL>
    </Javascript>
    

## InvalidResourceUrlReference

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid resource url ref invalid_reference in policy policy_name in org_name
    

### Example error message
    
    
    Error Deploying Revision 8 to test
    Invalid resource url ref jsc://dependent_js.js in policy js-TotalVariable in aprabhashankar-eval
    

### Example screenshot

![Error deploying revision 8 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/javascript-deploy-error-1.png)

### Cause

If the `<ResourceURL>` and `<IncludeURL>` elements refer to a JavaScript file that does not exist, then the deployment of the API proxy fails.

If you are deploying a proxy bundle from your local machine, then the JavaScript source files must be stored under `/apiproxy/resources/jsc`. In this case, the source files are scoped to the API proxy.

In the Apigee UI, the JavaScript source files appear under **jsc** in the Scripts section of the API proxy editor's Navigator pane. You can also store resource files in [environment level repositories](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) (to make JavaScript code available to all proxies in an org or env, for example).

If any resource files specified in the policy cannot be found in any of the available scopes (proxy or environment), then this error occurs.

### Diagnosis

  1. Identify the JavaScript policy where the error occurred and that contains the invalid resource URL reference. You can find this information from the error message. For example, in the following error, the policy name is `js-TotalVariable` and the invalid resource URL reference is `jsc://dependent_js.js`.
         
         Invalid resource url ref jsc://dependent_js.js in policy js-TotalVariable in aprabhashankar-eval
         

  2. Verify that the resource URL reference specified in the failed JavaScript policy matches with the value identified in the error message (step #1 above). For example, the following policy specifies the resource URL reference as `jsc://dependent_js.js`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-TotalVariable">
           <DisplayName>js-TotalVariable</DisplayName>
           <Properties/>
           <ResourceURL>jsc://add_variables.js</ResourceURL>
           <IncludeURL>jsc://dependent_js.js</IncludeURL>
         </Javascript>
         

  3. Check if the source file identified in step #1 file is part of the specific API Proxy bundle, or exists at the environment scope.

     1. To check if the file is part of the specific API Proxy bundle, follow one of the below steps: 
        1. In the Apigee UI, check if this file is in the Scripts section of the API proxy.
        2. Download the API Proxy bundle and search if the file exists.
     2. If the file is not part of the specific API Proxy bundle, then check if it exists at the environment level. You can use the [Resource Files API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles) for this investigation.

If the file does not exist at the API Proxy or environment level, then that's the cause of the error.

In the example described above, recall that the invalid JavaScript file name is `dependent_js.js`. In the below screenshot, notice that the file specified as a resource URL in the policy does not appear in the Scripts section. Therefore, it is not part of the API Proxy. If it is also the case that the file does not exist at the environment level, the deployment of the API Proxy fails with the error:
    
    Invalid resource url ref jsc://dependent_js.js in policy js-TotalVariable in aprabhashankar-eval
    

![Invalid resource URL error.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/javascript-deploy-error-3.png)




### Resolution

Ensure that the JavaScript files specified in the `<ResourceURL>` and `<IncludeURL>` elements refer to a valid file that exists at the API Proxy or environment level.

To correct the example JavaScript policy shown above, add the file `dependent_js.js` to the API Proxy bundle. In the below screenshot you can see that the JavaScript files specified in `<ResourceURL>` and `<IncludeURL>` elements are visible in the Scripts section of the API Proxy bundle.

![Corrected example.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/javascript-deploy-error-4.png)

## WrongResourceType

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Resource JavaScript_file is the wrong type. It is invalid_type: but JavaScript steps use type jsc:.
    

### Example error message
    
    
    Error Deploying Revision 2 to test
    Resource js_checkType.js is the wrong type. It is node: but JavaScript steps use type jsc:.
    

### Example screenshot

![Error deploying revision 2 to test.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/javascript-deploy-error-2.png)

### Cause

This error occurs during deployment if the `<ResourceURL>` and `<IncludeURL>` elements of the JavaScript policy refer to any resource type other than **jsc** (JavaScript file).

**Note:** The JavaScript policy supports only the **jsc** resource type.

For example, if the `<IncludeURL>` element is declared as shown below, the deployment of the API proxy fails:
    
    
    <IncludeURL>node://javascript-dependency.js</IncludeURL>
    

This is because it's referring to a `node` resource type which is incorrect.

### Diagnosis

  1. Identify the invalid resource type used in the JavaScript policy. You can find this information from the error message. For example, in the following error, the invalid resource type is `node`.
         
         Resource js_checkType.js is the wrong type. It is node: but JavaScript steps use type jsc:.
         

  2. Examine all the JavaScript policies in the specific API Proxy where the failure has occurred. If there is any JavaScript policy in which the resource specified in the `<ResourceURL>` or the `<IncludeURL>`element the matches the invalid resource type identified in Step #1 above, then that's the cause of the error.

For example, the following policy specifies the resource type as `node`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
             <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-TotalVariable">
             <DisplayName>js-TotalVariable</DisplayName>
             <Properties/>
             <ResourceURL>node://js_checkType.js</ResourceURL>
             <IncludeURL>jsc://javascript-dependency.js</IncludeURL>
         </Javascript>
         

Because the resource type is specified as `node`, which is invalid, the deployment of the API Proxy fails with the error:
         
         Resource js_checkType.js is the wrong type. It is node: but JavaScript steps use type jsc:.
         




### Resolution

Ensure that the `<ResourceURL>` and `<IncludeURL>` elements in the JavaScript policy always refer to `jsc` resource type.

To correct the example shown above, modify the `<ResourceURL>` element to have the `jsc` resource type.
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-TotalVariable">
        <DisplayName>js-TotalVariable</DisplayName>
        <Properties/>
        <ResourceURL>jsc://js_checkType.js</ResourceURL>
        <IncludeURL>jsc://javascript-dependency.js</IncludeURL>
    </Javascript>
    

## NoResourceURLOrSource

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision revision_number
    Bundle is invalid. Errors:[Entity : Policy-policy_name, No ResourceURL or Source;].
    

### Example error message
    
    
    Error Saving Revision 10
    Bundle is invalid. Errors:[Entity : Policy-js-example, No ResourceURL or Source;].
    

### Example screenshot

![Error saving revision 10.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/javascript-deploy-error-6.png)

### Cause

The deployment of the JavaScript policy can fail with this error under the following scenarios:

  1. If the `<ResourceURL>` element is not declared or if the resource URL is not defined within this element. `<ResourceURL>` element is a mandatory element.
  2. The `<IncludeURL>` element is declared but the resource URL is not defined within this element. `<IncludeURL>` element is optional but if declared, the resource URL must be specified within the `<IncludeURL>`element.



For example, if the `<IncludeURL>` element is declared as shown below, the deployment of the API proxy fails:
    
    
    <IncludeURL></IncludeURL>
    

### Diagnosis

  1. Identify the JavaScript policy where the error occurred. You can find this information from the error message. For example, in the following error, the policy name is `Policy-js-example`:
         
         Bundle is invalid. Errors:[Entity : Policy-js-example, No ResourceURL or Source;].
         

  2. In the failed JavaScript policy XML file, perform the following checks:

     1. The `<ResourceURL>` element must be declared and the element must have the resource URL defined.
     2. If the `<IncludeURL>`element is declared, you must specify a resource URL within. Declaring the `<IncludeURL>` element is optional.

If any of the above checks fail, then that's the cause of the error.

**Example 1:** The following policy doesn't have the `<ResourceURL>` element declared:
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-example">
        <DisplayName>js-example</DisplayName>
        <Properties/>
    </Javascript>
    

Because the `<ResourceURL>` element is not declared, the deployment of the API Proxy fails with the error:
    
    Bundle is invalid. Errors:[Entity : Policy-js-example, No ResourceURL or Source;].
    

**Example 2:** The following policy has an empty `<IncludeURL>` element.



    
    
      <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
      <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-example">
          <DisplayName>js-example</DisplayName>
          <Properties/>
          <ResourceURL>jsc://check_var.js</ResourceURL>
          <IncludeURL></IncludeURL>
      </Javascript>
    

Because the `<IncludeURL>` element does not have the resource URL, the deployment of the API Proxy fails with the error:
    
    
      Bundle is invalid. Errors:[Entity : Policy-js-example, No ResourceURL or Source;].
    

### Resolution

Ensure the following in the JavaScript policy:

  1. The `<ResourceURL>` element is declared and the resource URL is defined within this element. `<ResourceURL>` element is a mandatory element.
  2. If the `<IncludeURL>`element is declared, the include resource URL must be defined within this element. `<IncludeURL>`element is optional but if declared, the resource URL must be specified within the `<IncludeURL>`element.

To correct the Example 1 shown above, include the `<ResourceURL>` element with a valid JavaScript file:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-example">
             <DisplayName>js-example</DisplayName>
             <Properties/>
             <ResourceURL>jsc://check_var.js</ResourceURL>
         </Javascript>
         

To correct the Example 2 shown above, include a valid JavaScript file in the `<IncludeURL>` element
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <Javascript async="false" continueOnError="false" enabled="true" timeLimit="200" name="js-example">
             <DisplayName>js-example</DisplayName>
             <Properties/>
             <ResourceURL>jsc://check_var.js</ResourceURL>
             <IncludeURL>jsc://js_dependency.js</IncludeURL>
         </Javascript>
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
