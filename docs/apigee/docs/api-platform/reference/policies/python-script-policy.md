---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy/
title: PythonScript policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:03.082560+00:00
---

# PythonScript policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  PythonScript policy Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Python Script policy lets you add customized Python functionality to your API proxy flow, especially when the functionality you need is beyond what the Apigee out-of-the-box policies provide.

This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

Python language support is provided through [Jython version 2.5.2](https://www.jython.org/jython-old-sites/docs/index.html). Third-party libraries you add must be "pure Python" (implemented only in Python). For more on adding libraries, see [Resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files).

**Note:** This feature may not be available in all Apigee plans. To see which pricing plan includes this feature, see [ https://cloud.google.com/apigee/pricing/](https://cloud.google.com/apigee/pricing/).

A Python policy contains no actual code. Instead, a Python policy references a Python resource and defines the Step in the API flow where the Python script executes. You can upload your script through the Apigee UI proxy editor, or you can include it in the `/resources/py` directory in API proxies that you develop locally.

**WARNING:**  
You should limit or disable SSH access to your security resources to prevent this policy from being used to access internal files, current user info, the process list, or CPU/memory utilization. 

### Samples

### Python policy & script

### Python Script policy
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Script name="Python-1">
            <DisplayName>Python-1</DisplayName>
            <ResourceURL>py://myscript.py</ResourceURL>
    </Script>

In this example, the element, ResourceURL specifies the relevant Python script resource.

### Python Script

This shows what you might include in the Python script itself.
    
    
    import base64
    
    username = flow.getVariable("request.formparam.client_id")
    password = flow.getVariable("request.formparam.client_secret")
    
    base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    authorization = "Basic "+base64string
    
    flow.setVariable("authorizationParam",authorization)

## Element reference
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Script name="Python-1">
        <DisplayName>Python-1</DisplayName>
        <ResourceURL>py://myscript.py</ResourceURL>
        <IncludeURL>py://myscript_dependency.py</IncludeURL>
    </Script>

The following table describes attributes that are common to all policy parent elements:

Attribute | Description | Default | Presence  
---|---|---|---  
`name` |  The internal name of the policy. The value of the `name` attribute can contain letters, numbers, spaces, hyphens, underscores, and periods. This value cannot exceed 255 characters. Optionally, use the `<DisplayName>` element to label the policy in the management UI proxy editor with a different, natural-language name. | N/A | Required  
`continueOnError` |  Set to `false` to return an error when a policy fails. This is expected behavior for most policies. Set to `true` to have flow execution continue even after a policy fails. See also:

  * [Fault rules are triggered ONLY in an error state (about continueOnError)](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#multiplefaultrulesandexecutionlogic-faultrulesaretriggeredonlyinanerrorstateaboutcontinueonerror)
  * [Handling faults within the current flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling#continueonerror)

| false | Optional  
`enabled` |  Set to `true` to enforce the policy. Set to `false` to _turn off_ the policy. The policy will not be enforced even if it remains attached to a flow. | true | Optional  
`async` |  This attribute is deprecated. | false | Deprecated  
  
## <DisplayName> element

Use in addition to the `name` attribute to label the policy in the management UI proxy editor with a different, natural-language name.
    
    
    <DisplayName>Policy Display Name</DisplayName>

Default |  N/A If you omit this element, the value of the policy's `name` attribute is used.  
---|---  
Presence | Optional  
Type | String  
  
## <ResourceURL> element

This element specifies the main Python file that will execute in the API flow. You can store this file at the API proxy scope (under `/apiproxy/resources/py` in the API proxy bundle or in the Scripts section of the API proxy editor's Navigator pane), or at the organization or environment scopes for reuse across multiple API proxies, as described in [Resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files). Your code can use the objects, methods, and properties of the [JavaScript object model](https://docs.cloud.google.com/apigee/docs/api-platform/reference/javascript-object-model).
    
    
    <ResourceURL>py://myscript.py</ResourceURL>

**Default:** | None  
---|---  
**Presence:** | Required  
**Type:** | String  
  
## <IncludeURL> element

Specifies a Python file to be loaded as dependency to the main Python file specified with the `<ResourceURL>` element. The scripts will be evaluated in the order in which they are listed in the policy.

Include more than one Python dependency resource with additional `<IncludeURL>` elements.

**Warning:** If your Python files are stored at the proxy or environment level, be sure they were uploaded correctly with cURL using the `-F` option or as a file attachment through a REST client. Content-Type is `multipart/form-data`. For more information, see [Resource files](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files).
    
    
    <IncludeURL>py://myscript_dependency.py</IncludeURL>

**Default:** | None  
---|---  
**Presence:** | Optional  
**Type:** | String  
  
## Error codes

This section describes the fault codes and error messages that are returned and fault variables that are set by Apigee when this policy triggers an error. This information is important to know if you are developing fault rules to handle faults. To learn more, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors) and [Handling faults](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling).

### Runtime errors

These errors can occur when the policy executes.

**Tip:** Need help resolving an error? Click _build_ in the Fix column for detailed troubleshooting information.Fault code | HTTP status | Cause | Fix  
---|---|---|---  
`steps.script.ScriptEvaluationFailed` | `500` | The PythonScript policy can throw several different types of ScriptExecutionFailed errors. Commonly seen types of errors include [NameError](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors#nameerror) and [ZeroDivisionError](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors#zerodivisionerror). | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors#scriptevaluationfailed)  
  
### Deployment errors

These errors can occur when you deploy a proxy containing this policy.

**Tip:** Need help resolving an error? Click _build_ next to the error's cause description to visit the troubleshooting page. Error name | Cause | Fix  
---|---|---  
`InvalidResourceUrlFormat` | If the format of the resource URL specified within the `<ResourceURL>` or the `<IncludeURL>` element of the PythonScript policy is invalid, then the deployment of the API proxy fails. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/python-script-deployment-errors#invalidresourceurlformat)  
`InvalidResourceUrlReference` | If the `<ResourceURL>` or the `<IncludeURL>` elements refer to a PythonScript file that does not exist, then the deployment of the API proxy fails. The referenced source file must exist either the API proxy, environment, or organization level. | [_build_](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/python-script-deployment-errors#invalidresourceurlreference)  
  
### Fault variables

These variables are set when this policy triggers an error at runtime. For more information, see [What you need to know about policy errors](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/what-you-need-know-about-policy-errors).

Variables | Where | Example  
---|---|---  
`fault.name="fault_name"` | fault_name is the name of the fault, as listed in the Runtime errors table above. The fault name is the last part of the fault code. | `fault.name Matches "ScriptExecutionFailed"`  
`pythonscript.policy_name.failed` | policy_name is the user-specified name of the policy that threw the fault. | `pythonscript.PythonScript-1.failed = true`  
  
### Example error response

**Note:** For error handling, the best practice is to trap the `errorcode` part of the error response. Do not rely on the text in the `faultstring`, because it could change.
    
    
    {
      "fault": {
        "faultstring": "Execution of SetResponse failed with error: Pythonscript runtime error: "ReferenceError: "status" is not defined.\"",
        "detail": {
          "errorcode": "steps.script.ScriptExecutionFailed"
        }
      }
    }

### Example fault rule
    
    
    <FaultRule name="PythonScript Policy Faults">
        <Step>
            <Name>AM-CustomErrorResponse</Name>
            <Condition>(fault.name Matches "ScriptExecutionFailed") </Condition>
        </Step>
        <Condition>(pythonscript.PythonScript-1.failed = true) </Condition>
    </FaultRule>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
