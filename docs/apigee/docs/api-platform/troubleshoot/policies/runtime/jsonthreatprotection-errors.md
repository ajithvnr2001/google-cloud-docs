---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors/
title: JSON Threat Protection runtime error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:58.090690+00:00
---

# JSON Threat Protection runtime error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  JSON Threat Protection runtime error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors) documentation._

**Note:** Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors/).

## ExecutionFailed

### Error Code
    
    
    steps.jsonthreatprotection.ExecutionFailed
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: JSONThreatProtection[policy_name]: error_description
              at line line_num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Types of Errors and possible causes

The JSONThreatProtection policy can throw many different types of ExecutionFailed errors. The table below lists the different types of errors and their possible causes:

Error type  | Cause   
---|---  
Exceeded object entry name length | The maximum string length allowed in an object's entry name is exceeded.   
Exceeded object entry count | The maximum number of entries allowed in an object is exceeded.   
Exceeded array element count | The maximum number of elements allowed in an array is exceeded.   
Exceeded container depth | The maximum allowed nested depth is exceeded.   
Exceeded string value length | The maximum length allowed for a string value is exceeded.   
[Invalid JSON object](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/runtime/jsonthreatprotection-errors.md?tenant=apigee#not_valid_json_object) | The input JSON Payload is invalid.   
  
## Exceeded object entry name length

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: JSONThreatProtection[policy_name]:
              Exceeded object entry name length at line line_num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Execution failed. reason: JSONThreatProtection[JSON-Threat-Protection-1]:
              Exceeded object entry name length at line 2",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }
    

### Cause

This error occurs if the input message payload specified by the `<Source>` element contains a JSON object with a property name that exceeds the maximum length specified in the `<ObjectEntryNameLength>` element.

For example, if the `<ObjectEntryNameLength>` element is specified as 5 in the policy, but the input message payload has a JSON property whose name exceeds 5 characters, then this error is thrown.

### Diagnosis

  1. Examine the error message to identify the JSONThreatProtection policy name and the line number where the long entry name occurs. For example, in the following error message, the JSONThreatProtection policy name is `JSON-Threat-Protection-1` and line number in the payload is 2.
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded object entry name
         length at line 2
         

  2. Examine the policy you identified in Step 1, and note the value specified in the `<ObjectEntryNameLength>` element.

For example, in the following JSONThreatProtection policy, `<ObjectEntryNameLength>` is set to `5`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>12</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>5</ObjectEntryNameLength>
             <Source>request</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

  3. Examine the specific line number (identified in Step 1) of the input payload and check if the length of the object name is greater than the value specified in the `<ObjectEntryNameLength>` element (identified in Step 2). If the length of the object name exceeds that number, then that is the cause of the error.

Here is an example input payload:
         
         {
            "number" : 500,
            "string" : "text"
         }
         

The JSON payload shown above has a property named `number` at line 2 which has 6 characters (the name length is 6). Since the length of the object name is greater than 5 (the value specified for `<ObjectEntryNameLength>` element) you get the following error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded object entry name
         length at line 2
         




### Resolution

If the JSONThreatProtection policy was meant to protect against payloads with object entry names that exceed the defined value then the error message is expected. In this case, no additional action is required.

However, if you determine that longer object entry names can be specified in the payload without any consequence, then modify the `<ObjectEntryNameLength>` to a suitable value based on your requirements.

For example, if you think you can allow object names up to a length of 10 characters, then modify the JSONThreatProtection policy as follows:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>3</ArrayElementCount>
        <ContainerDepth>12</ContainerDepth>
        <ObjectEntryCount>5</ObjectEntryCount>
        <ObjectEntryNameLength>10</ObjectEntryNameLength>
        <Source>request</Source>
        <StringValueLength>50</StringValueLength>
    </JSONThreatProtection>
    

## Exceeded object entry count

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: JSONThreatProtection[policy_name]:
              Exceeded object entry count at line line_num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Execution failed. reason: JSONThreatProtection[JSON-Threat-Protection-1]:
              Exceeded object entry count at line 7",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }
    

### Cause

This error occurs if the input message payload specified by the `<Source>` element contains a JSON object that contains more entries (properties) than the value specified in the `<ObjectEntryCount>` element of the policy.

For example, if the `<ObjectEntryCount>`element is 5, but the input JSON payload has more than 5 entries, then this error is thrown.

### Diagnosis

  1. Examine the error message to identify the JSONThreatProtection policy name and the line number where the entry count is exceeded. For example, in the following error message, the policy name is `JSON-Threat-Protection-1` and line number in the payload is `7`:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded object entry count
         at line 7
         

  2. Make a note of the value specified in the `<ObjectEntryCount>` element of the policy (identified in Step 1).

In the following policy example, `<ObjectEntryCount>` is set to `5`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>12</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>6</ObjectEntryNameLength>
             <Source>request</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

  3. Examine the specific line number (identified in Step 1) of the input payload and check if the number of entities in the payload is greater than the value specified for `<ObjectEntryCount>` element (identified in Step 2). If the number of objects exceeds the object entry count, then that is the cause of the error.

Here is an example input payload:
         
         {
         "name" : "John",
         "id" : 234687,
         "age" : 31,
         "city" : "New York",
         "country" : "USA",
         "company" : "Google"
         }
         

In the JSON payload shown above, the 6th entry occurs at line #7 (company). Since the count of the object entries in the input JSON payload is greater than 5 (the value specified for `<ObjectEntryCount>` element) you get the following error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded object entry count at
         line 7
         




### Resolution

If the JSONThreatProtection policy was meant to protect against payloads with a number of object entries that exceeds a specific threshold, then the error message is expected. In this case, you don't need to take any additional action.

However, if you determine that more object entries can be included in the payload without any consequence, then modify the `<ObjectEntryCount>` to a suitable value based on your requirements.

For example, If you think you can allow up to 10 object entries, then modify the JSONThreatProtection policy as follows:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>3</ArrayElementCount>
        <ContainerDepth>12</ContainerDepth>
        <ObjectEntryCount>10</ObjectEntryCount>
        <ObjectEntryNameLength>6</ObjectEntryNameLength>
        <Source>request</Source>
        <StringValueLength>50</StringValueLength>
    </JSONThreatProtection>
    

## Exceeded array element count

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: JSONThreatProtection[policy_name]:
              Exceeded array element count at line line-num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Execution failed. reason: JSONThreatProtection[JSON-Threat-Protection-1]:
              Exceeded array element count at line 3",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }
    

### Cause

This error occurs if the input message payload specified by the `<Source>` element contains a JSON array with a number of elements more than the number specified in the `<ArrayElementCount>` element of the policy.

For example, if the `<ArrayElementCount>` element is specified as `3`, but the input payload has a JSON array with more than 3 elements, then this error is thrown.

### Diagnosis

  1. Examine the error message to identify the policy name and the line number where the array length is exceeded. For example, in the following error message, the policy name is `JSON-Threat-Protection-1` and line number in the payload is `3`:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded array element count at line 3
         

  2. Make a note of the value specified for the `<ArrayElementCount>` element of the policy (identified in Step 1).

In the following JSONThreatProtection policy example, `<ArrayElementCount>` is set to `3`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>12</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>6</ObjectEntryNameLength>
             <Source>request</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

  3. Examine the specific line number (identified in Step 1) of the input payload and check if the array specified there has a higher count than the number specified in the `<ArrayElementCount>` element (identified in Step 2). If the number of array elements exceeds the count, then that is the cause of the error.

Here is an example input payload:
         
         {
          "name":"Ford",
          "models":[
             "Mustang",
             "Endeavour",
             "Fiesta",
             "EcoSport",
             "Focus"
          ]
         }
         

The JSON Payload shown above has 5 elements in the array named `models` at line 3. Because the number of array elements is greater than 3 (the value specified for `<ArrayElementCount>` element) you get the following error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded array element count
         at line 3
         




### Resolution

If JSONThreatProtection policy was meant to protect against payloads with a specific array count threshold, then the error message is expected. In this case, there is no additional action required.

However, if you determine that a higher number of elements in an array can be allowed, then modify `<ArrayElementCount>` to a suitable value based on your requirements.

For example, If you think you can allow up to 5 array elements, then modify the policy as follows:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>5</ArrayElementCount>
        <ContainerDepth>12</ContainerDepth>
        <ObjectEntryCount>5</ObjectEntryCount>
        <ObjectEntryNameLength>6</ObjectEntryNameLength>
        <Source>request</Source>
        <StringValueLength>50</StringValueLength>
    </JSONThreatProtection>
    

## Exceeded container depth

### Error response body

Runtime traffic returns a 500 response code with the following error:
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: JSONThreatProtection[policy_name]:
              Exceeded container depth at line line-num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Execution failed. reason: JSONThreatProtection[JSON-Threat-Protection-1]:
              Exceeded container depth at line 5",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }
    

### Cause

This error occurs if the input message payload specified by the `<Source>` element contains a JSON object that contains JSON elements with a container depth that exceeds the maximum container depth specified in the policy's `<ContainerDepth>` element. Container depth is the maximum allowed nested depth for JSON elements. For example, an array containing an object that contains an object would result in a containment depth of 3.

For example, if the `<ContainerDepth>` element is `3`, but the input payload has a container depth that exceeds this limit, then this error is thrown.

### Diagnosis

  1. Examine the error message to identify the JSONThreatProtection policy name and the line number where the container depth is exceeded. For example, in the following error message, the policy name is `JSON-Threat-Protection-1` and the line number in the payload is `5`.
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded container depth at
         line 5
         

  2. Make a note of the value specified for the `<ContainerDepth>` element (identified in Step 1).

In the following JSONThreatProtection policy example, `<ContainerDepth>` is set to `5`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>5</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>20</ObjectEntryNameLength>
             <Source>request</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

  3. Examine the specific line number (identified in Step 1) of the input payload and check if the container depth in the payload is higher than the value specified in the `<ContainerDepth>` element (identified in Step 2). If the container depth exceeds the count, then that is the cause of the error.

Here is an example input payload:
         
         {
          "ContainerDepth2":[ {
                "ContainerDepth4":[
                   {
                      "ContainerDepth6":[
                         "1",
                         "2"
                      ]
                   }
                ]
             }
          ]
         }
         

The JSON payload shown above has a container depth of 6 at line 5. Since depth is greater than 5, the value specified for `<ContainerDepth>` element of JSONThreatProtection policy you get the following error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded container depth at
         line 5
         




### Resolution

If the JSONThreatProtection policy was meant to protect against payloads with container depths that exceed the specified value, then the error message is expected. In this case, there is no additional action required.

However, if you determine that a higher container depths are acceptable, then modify the `<ContainerDepth>` to a suitable value based on your requirements.

For example, If you think you can allow container depths up to 10, then modify the policy as follows:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>3</ArrayElementCount>
        <ContainerDepth>10</ContainerDepth>
        <ObjectEntryCount>5</ObjectEntryCount>
        <ObjectEntryNameLength>20</ObjectEntryNameLength>
        <Source>request</Source>
        <StringValueLength>50</StringValueLength>
    </JSONThreatProtection>
    

## Exceeded string value length

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: JSONThreatProtection[policy_name]:
              Exceeded string value length at line line-num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Execution failed. reason: JSONThreatProtection[JSON-Threat-Protection-1]:
              Exceeded string value length at line 3",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }
    

### Cause

This error occurs if the input message payload specified by the `<Source>` element contains JSON elements that have values with more characters than allowed by the `<StringValueLength>` element.

For example, if the `<StringValueLength>` element is set to `50` in the policy, but the input payload has one or more elements whose values contain more than 50 characters, then this error is thrown.

### Diagnosis

  1. Examine the error message to identify the policy name and the line number where the string length is exceeded. In the following example the policy name is `JSON-Threat-Protection-1 and`line in the payload `3`.
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded string value length at line 3
         

  2. Make a note of the value specified for the `<StringValueLength>` element in the (identified in Step 1).

In the following JSONThreatProtection policy example, `<StringValueLength>` is set to `50`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>5</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>20</ObjectEntryNameLength>
             <Source>request</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

  3. Examine the specific line number (identified in Step 1) of the input payload and check if the length of the value is greater than the number of characters specified for the `<StringValueLength>` element (identified in Step 2). If the length of the value exceeds the limit, then that is the cause of the error.

Here is an example input payload:
         
         {
           "Country": "New Zealand",
           "Place Name": "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu"
         }
         

The JSON Payload shown above has an object named `Place Name` whose value `Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu` has 85 characters at line 3. Since the length of the value is greater than 50, the value specified in the `<StringValueLength>` element, you get the following error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         JSONThreatProtection[JSON-Threat-Protection-1]: Exceeded string value length
         at line 3
         




### Resolution

If the JSONThreatProtection policy was meant to protect against payloads with values that exceed a specific string length, then the error message is expected. In this case, there is no additional action required.

However, if you determine that a longer value length can be specified in the payload, then modify the `<StringValueLength>` to a suitable value based on your requirements.

For example, If you think you can allow a value up to a length of 90, then modify the policy as follows:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>3</ArrayElementCount>
        <ContainerDepth>5</ContainerDepth>
        <ObjectEntryCount>5</ObjectEntryCount>
        <ObjectEntryNameLength>20</ObjectEntryNameLength>
        <Source>request</Source>
        <StringValueLength>90</StringValueLength>
    </JSONThreatProtection>
    

## Not valid JSON object

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Execution failed. reason: string: at line line-num",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Execution failed. reason: Expecting : at line 3",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.ExecutionFailed"
            }
        }
    }
    

### Cause

This error occurs if the input message payload specified by the `<Source>` element in the JSONThreatProtection policy is not a valid JSON object.

### Diagnosis

  1. Examine the error message to identify the policy name and the line number where the error occurred. In the following example the policy name is `JSON-Threat-Protection-1 and`line in the payload `2`.
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason: Expecting : at line 3
         

  2. Examine the specific line number (identified in Step 1) of the input payload and check if the JSON object that was passed in the payload is indeed a valid JSON object.

Here is an example input payload:
         
         {
           "Longitude": 6.11499,
           "Latitude"  50.76891
         }
         

In the JSON payload shown above, the line 3 does not have `":"` (colon). Since it's not a valid JSON object, you get the error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Execution failed. reason:
         Expecting : at line 3
         




### Resolution

Ensure a valid input JSON payload is passed to any API Proxy that includes the JSONThreatProtection policy.

For the example described above, modify the JSON payload as follows:
    
    
    {
        "Longitude": 6.11499,
      "Latitude" : 50.76891
    }
    

## SourceUnavailable

### Error Code
    
    
    steps.jsonthreatprotection.SourceUnavailable
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]::
              Source[var_name] is not available"
            "detail": {
                "errorcode": "steps.jsonthreatprotection.SourceUnavailable"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]::
              Source requests is not available",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.SourceUnavailable"
            }
        }
    }
    

### Cause

This error occurs if the [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message) variable specified in the `<Source>` element of the JSONThreatProtection policy is either:

  * Out of scope (not available in the specific flow where the policy is being executed)
  * Is not one of the valid values `_request_`, `_response_`, or `_message_`



For example, this error occurs if the `<Source>` element in the policy is set to a variable that doesn't exist in the flow where the policy is executed.

### Diagnosis

  1. Identify the policy name, and the name of the Source variable from the error message. For example, in the following error message, the policy name is `JSON-Threat-Protection-1` and the Source variable is `requests`:
         
         JSONThreatProtection[JSON-Threat-Protection-1]:: Source requests is not available
         

  2. Examine the value specified for the `<Source>` element identified in Step 1.

In the following JSONThreatProtection policy example, the `<Source>` element is set to `requests`.
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>5</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>20</ObjectEntryNameLength>
             <Source>requests</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

The valid values for `<Source>` element are `request`, `response`, or `message`. Because requests is not a valid value and doesn't exist in the flow where the policy is being executed, you get the error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]:: Source requests is not available
         




### Resolution

Ensure that the variable set in the `<Source>` element of the failed JSONThreatProtection policy is set to either `request`, `response`, or `message` and exists in the flow where the policy executes.

To correct the example JSONThreatProtection policy shown above, you could modify the `<Source>` element to use the `request` variable, because it exists in the request flow:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>3</ArrayElementCount>
        <ContainerDepth>5</ContainerDepth>
        <ObjectEntryCount>5</ObjectEntryCount>
        <ObjectEntryNameLength>20</ObjectEntryNameLength>
        <Source>request</Source>
        <StringValueLength>50</StringValueLength>
    </JSONThreatProtection>
    

## NonMessageVariable

### Error Code
    
    
    steps.jsonthreatprotection.NonMessageVariable
    

### Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[policy_name]:
              Variable var_name does not resolve to a Message"
            "detail": {
                "errorcode": "steps.jsonthreatprotection.NonMessageVariable"
            }
        }
    }

### Example Error response body
    
    
    {
        "fault": {
            "faultstring": "JSONThreatProtection[JSON-Threat-Protection-1]:
              Variable message.content does not resolve to a Message",
            "detail": {
                "errorcode": "steps.jsonthreatprotection.NonMessageVariable"
            }
        }
    }
    

### Cause

This error occurs if the `<Source>` element in the JSONThreatProtection policy is set to a variable which is not of type [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#message).

Message type variables represent entire HTTP requests and responses. The built-in Apigee flow variables request, response, and message are of type message. To learn more about message variables, see the [Variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables).

### Diagnosis

  1. Identify the JSONThreatProtection policy name and the name of the Source variable from the error message. For example, in the following error message, the policy name is `JSON-Threat-Protection-1`and the Source variable is `message.content`:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Variable message.content does not resolve to a Message
         

  2. Examine `<Source>` element of the JSONThreatProtection policy (identified in Step 1).

In the following JSONThreatProtection policy example, `<Source>` is set to `message.content` instead of `message`:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
             <DisplayName>JSON Threat Protection-1</DisplayName>
             <Properties/>
             <ArrayElementCount>3</ArrayElementCount>
             <ContainerDepth>5</ContainerDepth>
             <ObjectEntryCount>5</ObjectEntryCount>
             <ObjectEntryNameLength>20</ObjectEntryNameLength>
             <Source>message.content</Source>
             <StringValueLength>50</StringValueLength>
         </JSONThreatProtection>
         

Since `message.content` is not of type message, you get the error:
         
         JSONThreatProtection[JSON-Threat-Protection-1]: Variable message.content does
         not resolve to a Message
         




### Resolution

Ensure that the `<Source>` element in the failed JSONThreatProtection policy is set to a [message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#messagevariables) type flow variable that exists in the flow where the policy executes.

To correct the policy, you can modify the `<Source>` element to specify a variable that is of type message. For example, in the failed JSONThreatProtection you could specify the `<Source>` element as `message`:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <JSONThreatProtection async="false" continueOnError="false" enabled="true" name="JSON-Threat-Protection-1">
        <DisplayName>JSON Threat Protection-1</DisplayName>
        <Properties/>
        <ArrayElementCount>3</ArrayElementCount>
        <ContainerDepth>5</ContainerDepth>
        <ObjectEntryCount>5</ObjectEntryCount>
        <ObjectEntryNameLength>20</ObjectEntryNameLength>
        <Source>message</Source>
        <StringValueLength>50</StringValueLength>
    </JSONThreatProtection>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
