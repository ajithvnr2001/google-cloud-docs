---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors/
title: PythonScript policy runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:55.593853+00:00
---

# PythonScript policy runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  PythonScript policy runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/python-script-runtime-errors/).

## ScriptEvaluationFailed

### Error code
    
    
    steps.script.ScriptEvaluationFailed
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Evaluation of script pythonscript_name (py) failed with reason: error_type: error_description"",
            "detail": {
                "errorcode": "steps.script.ScriptEvaluationFailed"
            }
        }
    }

### Possible causes

The [Python Script](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/python-script-policy) policy can throw several different types of `ScriptEvaluationFailed` errors. The sections below describe some of these errors.

## NameError

If there is a variable in the PythonScript code which is referenced or operated on without being defined, then you get the Name error.

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Evaluation of script pythonscript_name (py) failed with reason: "**NameError** : variable_name is not defined"",
            "detail": {
                "errorcode": "steps.script.ScriptEvaluationFailed"
            }
        }
    }

### Example error response body
    
    
    {
        "fault": {
            "faultstring": "Evaluation of script myscript.py (py) failed with reason: "**NameError** : '**num3** ' is not defined"",
            "detail": {
                "errorcode": "steps.script.ScriptEvaluationFailed"
            }
        }
    }

### Diagnosis

  1. Identify the PythonScript policy and the undefined variable name from the faultstring element of the error response. For example, in the following faultstring, the PythonScript name is `myscript.py` and the undefined variable name is **num3** :
         
         "faultstring": "Evaluation of script myscript.py (py) failed with reason: "NameError: '**num3** ' is not defined""

  2. Examine the PythonScript source file identified in step #1 above and verify if the undefined variable identified in step #1 above is being referenced. For example, the following PythonScript code references the undefined variable **num3** , which matches the faultstring:
         
         num1 = 1.5
         num2 = 6.3
         sum = float(num1) + float(num3)
         print('The sum of {0} and {1} is {2}'.format(num1, **num3** sum))

  3. Check if the specific variable is defined within the PythonScript code. If the variable is not defined, then that's the cause for the error.

In the example script shown above, the variable **num3** is undefined. Therefore, you will get the below error:
         
         "faultstring": "Evaluation of script myscript.py (py) failed with reason: "NameError: '**num3** ' is not defined""




### Resolution

Ensure that all the variables referenced in the PythonScript code are properly defined.

To fix the issue with the example PythonScript shown above, define the variable **num3** before using it. For example:
    
    
    num1 = 1.5
    num2 = 6.3
    **num3 = 8.7**
    sum = float(num1) + float(num3)
    print('The sum of {0} and {1} is {2}'.format(num1, num3, sum))

## ZeroDivisionError

This error is raised when the second argument of a division or modulo operation is zero.

### Error response body
    
    
    {
        "fault": {
            "faultstring": "Evaluation of script pythonscript_name (py) failed with reason: "**ZeroDivisionError** : reason_for_error"",
            "detail": {
                "errorcode": "steps.script.ScriptEvaluationFailed"
            }
        }
    }

### Example error response body
    
    
    {
        "fault": {
            "faultstring": "Evaluation of script myscript.py (py) failed with reason: "**ZeroDivisionError** : integer division or modulo by zero"",
            "detail": {
                "errorcode": "steps.script.ScriptEvaluationFailed"
            }
        }
    }

### Diagnosis

  1. Identify the PythonScript policy name and the reason for failure from the faultstring element of the error response. For example, in the following faultstring, the PythonScript name is `myscript.py` and the reason for failure is `integer division or modulo by zero`:
         
         "faultstring": "Evaluation of script myscript.py (py) failed with reason: "**ZeroDivisionError** : integer division or modulo by zero""

  2. Examine the PythonScript source file identified in step #1 above and verify if there's a division or a modulus operation by zero. For example, the following PythonScript code performs division by zero, which matches with what's in the faultstring:
         
         **a = 0**
         b = 5
         c = b/a
         print c

In the example script shown above, because the second argument of the division operation is zero, you get the following error:
         
         "faultstring": "Evaluation of script myscript.py (py) failed with reason: "**ZeroDivisionError** : integer division or modulo by zero""




### Resolution

Ensure that the second argument of a division or modulo operation is non zero in the PythonScript.

To fix the issue with the example PythonScript shown above, use a non zero value as the second argument of a division or modulo operation. For example:
    
    
    **a = 3**
    b = 5
    c = b/a
    print c

## More Information

There are many other possible causes for the error `steps.script.ScriptEvaluationFailed` apart from the ones described above. Please refer to the official [Python documentation](https://docs.python.org/3/library/exceptions.html) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
