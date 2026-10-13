---
url: https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases/create/
title: Method: cases.create \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:02.530354+00:00
---

# Method: cases.create  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases/create/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Reference ](https://docs.cloud.google.com/support/docs/reference/rest)



Send feedback 

#  Method: cases.create Stay organized with collections  Save and categorize content based on your preferences. 

Create a new case and associate it with a parent.

It must have the following fields set: `displayName`, `description`, `classification`, and `priority`. If you're just testing the API and don't want to route your case to an agent, set `testCase=true`.

EXAMPLES:

cURL:
    
    
    parent="projects/some-project"
    curl \
      --request POST \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header 'Content-Type: application/json' \
      --data '{
        "displayName": "Test case created by me.",
        "description": "a random test case, feel free to close",
        "classification": {
          "id":
          "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8"
        },
        "timeZone": "-07:00",
        "subscriberEmailAddresses": [
          "foo@domain.com",
          "bar@domain.com"
        ],
        "testCase": true,
        "priority": "P3"
      }' \
      "https://cloudsupport.googleapis.com/v2beta/$parent/cases"
    

Python:
    
    
    import googleapiclient.discovery
    
    apiVersion = "v2beta"
    supportApiService = googleapiclient.discovery.build(
        serviceName="cloudsupport",
        version=apiVersion,
        discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={apiVersion}",
    )
    request = supportApiService.cases().create(
        parent="projects/some-project",
        body={
            "displayName": "A Test Case",
            "description": "This is a test case.",
            "testCase": True,
            "priority": "P2",
            "classification": {
                "id":
                  "100IK2AKCLHMGRJ9CDGMOCGP8DM6UTB4BT262T31BT1M2T31DHNMENPO6KS36CPJ786L2TBFEHGN6NPI64R3CDHN8880G08I1H3MURR7DHII0GRCDTQM8"
            },
        },
    )
    print(request.execute())
    

### HTTP request

`POST https://cloudsupport.googleapis.com/v2beta/{parent=*/*}/cases`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent under which the case should be created.  
  
### Request body

The request body contains an instance of `[Case](https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases#Case)`.

### Response body

If successful, the response body contains a newly created instance of `[Case](https://docs.cloud.google.com/support/docs/reference/rest/v2beta/cases#Case)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsupport`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
