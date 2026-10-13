---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/instances/getSerialPortOutput/
title: Method: googleapis.compute.v1.instances.getSerialPortOutput \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:18.120310+00:00
---

# Method: googleapis.compute.v1.instances.getSerialPortOutput  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/instances/getSerialPortOutput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.compute.v1.instances.getSerialPortOutput Stay organized with collections  Save and categorize content based on your preferences. 

Returns the last 1 MB of serial port output from the specified instance.

## Arguments

Parameters  
---  
`instance` |  `string` Required. Name of the instance for this request.  
`project` |  `string` Required. Project ID for this request.  
`zone` |  `string` Required. The name of the zone for this request.  
`port` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Specifies which COM or serial port to retrieve data from.  
`start` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Specifies the starting byte position of the output to return. To start with the first byte of output to the specified port, omit this field or set it to `0`. If the output for that byte position is available, this field matches the `start` parameter sent with the request. If the amount of serial console output exceeds the size of the buffer (1 MB), the oldest output is discarded and is no longer available. If the requested start position refers to discarded output, the start position is adjusted to the oldest output still available, and the adjusted start position is returned as the `start` property value. You can also provide a negative start position, which translates to the most recent number of bytes written to the serial port. For example, -3 is interpreted as the most recent 3 bytes written to the serial console.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`SerialPortOutput`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/Overview#SerialPortOutput).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/instances/getSerialPortOutput).

### YAML
    
    
    - getSerialPortOutput:
        call: googleapis.compute.v1.instances.getSerialPortOutput
        args:
            instance: ...
            project: ...
            zone: ...
            port: ...
            start: ...
        result: getSerialPortOutputResult

### JSON
    
    
    [
      {
        "getSerialPortOutput": {
          "call": "googleapis.compute.v1.instances.getSerialPortOutput",
          "args": {
            "instance": "...",
            "project": "...",
            "zone": "...",
            "port": "...",
            "start": "..."
          },
          "result": "getSerialPortOutputResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
