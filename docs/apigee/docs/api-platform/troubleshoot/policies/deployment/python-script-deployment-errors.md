---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/python-script-deployment-errors/
title: PythonScript policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:44.991388+00:00
---

# PythonScript policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/python-script-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  PythonScript policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/python-script-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/python-script-deployment-errors/).

## InvalidResourceUrlFormat

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid resource url format. Resource url is invalid_URL.

### Example error message
    
    
    Error Deploying Revision 2 to prod
    Invalid resource url format. Resource url is py:myscript.py.

### Example screenshot

![Error deploying revision 2 to prod.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/python-InvalidResourceUrlFormat.png)

### Cause

If the format of the resource URL specified within the `<ResourceURL>` or the `<IncludeURL>` element of the [PythonScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy) is invalid, then the deployment of the API proxy fails.

The correct format is as shown below:
    
    
    <ResourceURL>py://file_name.py</ResourceURL>
    <IncludeURL>py://file_name.py</IncludeURL>

For example, if the `<ResourceURL>` element is specified as shown below, then the deployment of the API proxy fails because it does not follow the required pattern:
    
    
    <ResourceURL>py:myscript.py</ResourceURL>

### Diagnosis

  1. Identify the invalid resource URL format used in the PythonScript policy. You can find this information from the error message. For example, in the following error, the invalid resource URL format is `py:myscript.py`:
         
         Invalid resource url format. Resource url is py:myscript.py.

  2. Examine all the PythonScript policies in the specific API Proxy where the failure has occurred. If there is any PythonScript policy in which the resource URL specified in the `<ResourceURL>` or the `<IncludeURL>` element matches the invalid entry identified in step #1 above, then that's the cause of the error.

For example, the following policy specifies the resource URL as `py:myscript.py`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <Script async="false" continueOnError="false" enabled="true" timeLimit="200" name="py-TotalVariable">
             <DisplayName>py-TotalVariable</DisplayName>
             <Properties/>
             <ResourceURL>py:myscript.py</ResourceURL>
         </Script>

Since the resource URL is specified as `py:myscript.py`, which is invalid, the deployment of the API Proxy fails with the error:
         
         Invalid resource url format. Resource url is py:myscript.py.




### Resolution

Ensure that the resource URL format specified in the `<ResourceURL>` element of the PythonScript policy is valid. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Script async="false" continueOnError="false" enabled="true" timeLimit="200" name="py-TotalVariable">
        <DisplayName>py-TotalVariable</DisplayName>
        <Properties/>
        <ResourceURL>py://myscript.py</ResourceURL>
    </Script>

## InvalidResourceUrlReference

### Error message

Deployment of an API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Deploying Revision revision_number to environment
    Invalid resource url ref invalid_reference in policy policy_name in org_name

### Example error message
    
    
    Error Deploying Revision 2 to prod
    Invalid resource url ref py://myscript.py in policy Python_script in myorg

### Example screenshot

![Error deploying revision 2 to prod.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/python-InvalidResourceUrlRef.png)

### Cause

If the `<ResourceURL>` and `<IncludeURL>` elements refer to a PythonScript file that does not exist, then the deployment of the API proxy fails. If you are deploying a proxy bundle from your local machine, then the PythonScript source files must be stored under `/apiproxy/resources/py`(at the API proxy scope).

In the Apigee UI, the PythonScript source files appear under **py** in the Scripts section of the API proxy editor's Navigator pane as shown below:

![API Proxy Editor Navigation pane Scripts section.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/python-deployment-py.png)

You can also store resource files in [environment level repositories](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) (to make PythonScript code available to all proxies in an env, for example). If any resource files specified in the policy cannot be found, then this error occurs.

### Diagnosis

  1. Identify the PythonScript policy where the error occurred and the invalid resource URL reference. You can find this information from the error message. For example, in the following error, the policy name is `Python_script` and the invalid resource URL reference is `py://myscript.py`:
         
         Invalid resource url ref py://myscript.py in policy Python_script in myorg

  2. Verify that the resource URL reference specified in the failed PythonScript policy matches with the value identified in the error message (step #1 above). For example, the following policy specifies the resource URL reference as `py://myscript.py`, which matches what's in the error message:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <Script async="false" continueOnError="false" enabled="true" name="Python_script">
             <DisplayName>Python-1</DisplayName>
             <Properties/>
             <ResourceURL>py://myscript.py</ResourceURL>
         </Script>

  3. Check if the file identified in step #1 file is part of the specific API Proxy bundle, or exists at the environment scope.

     1. To check if the file is part of the specific API Proxy bundle, follow one of the below steps: 
        1. In the Apigee UI, check if this file is in the Scripts section of the API proxy.
        2. Download the API Proxy bundle and search if the file exists.
     2. If the file is not part of the specific API Proxy bundle, then check if it exists at the environment level. You can use the [Resource Files API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.resourcefiles) for this investigation.

If the file does not exist at the API Proxy or environment level, then that's the cause of the error.

In the example above, the invalid PythonScript filename is myscript.py. In the screenshot below, notice that the file specified as a resource URL in the policy does not appear in the Scripts section. Also the file does not exist at the environment level. Therefore, the deployment of the API Proxy fails with the error:
    
    Invalid resource url ref py://myscript.py in policy Python_script in myorg




![Invalid resource URL.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/python-deployment-error.png)

### Resolution

Ensure that the PythonScript files specified in `<ResourceURL>` and `<IncludeURL>` elements refer to a valid file that exists at the API Proxy or environment level.

To correct the example PythonScript policy shown above, add the file myscript.py to the API Proxy bundle. In the screenshot below you can see that the PythonScript files specified in `<ResourceURL>` and `<IncludeURL>` elements are visible in the Scripts section of the API Proxy bundle:

![Scripts section of API Proxy bundle.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/python-deployment-py.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
