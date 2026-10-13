---
url: https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases.attachments/get/
title: Method: cases.attachments.get \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:41.137503+00:00
---

# Method: cases.attachments.get  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases.attachments/get/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Reference ](https://docs.cloud.google.com/support/docs/reference/rest)



Send feedback 

#  Method: cases.attachments.get Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve an attachment associated with a support case.

EXAMPLES:

cURL:
    
    
    attachment="projects/some-project/cases/23598314/attachments/0684M00000P3h1fQAB"
    curl \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://cloudsupport.googleapis.com/v2beta/$attachment"
    

Python:
    
    
    import googleapiclient.discovery
    
    apiVersion = "v2beta"
    supportApiService = googleapiclient.discovery.build(
        serviceName="cloudsupport",
        version=apiVersion,
        discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={apiVersion}",
    )
    request = (
        supportApiService.cases()
        .attachments()
        .get(name="projects/some-project/cases/43595344/attachments/0684M00000P3h1fQAB")
    )
    print(request.execute())
    

### HTTP request

`GET https://cloudsupport.googleapis.com/v2beta/{name=*/*/cases/*/attachments/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the attachment to get.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Attachment](https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases.attachments#Attachment)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsupport`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
