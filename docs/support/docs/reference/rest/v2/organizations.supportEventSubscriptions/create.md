---
url: https://docs.cloud.google.com/support/docs/reference/rest/v2/organizations.supportEventSubscriptions/create/
title: Method: organizations.supportEventSubscriptions.create \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:54.159337+00:00
---

# Method: organizations.supportEventSubscriptions.create  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/reference/rest/v2/organizations.supportEventSubscriptions/create/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Reference ](https://docs.cloud.google.com/support/docs/reference/rest)



Send feedback 

#  Method: organizations.supportEventSubscriptions.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a support event subscription for an organization.

EXAMPLES:

cURL:
    
    
    parent="organizations/123456789"
    curl \
      --request POST \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header 'Content-Type: application/json' \
      --data '{
        "pubSubTopic": "projects/my-project/topics/my-topic"
      }' \
      "https://cloudsupport.googleapis.com/v2/$parent/supportEventSubscriptions"
    

Python:
    
    
    import googleapiclient.discovery
    
    apiVersion = "v2"
    supportApiService = googleapiclient.discovery.build(
        serviceName="cloudsupport",
        version=apiVersion,
        discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={apiVersion}",
    )
    request = supportApiService.supportEventSubscriptions().create(
        parent="organizations/123456789",
        body={
            "pubSubTopic": "projects/my-project/topics/my-topic"
        },
    )
    print(request.execute())
    

### HTTP request

`POST https://cloudsupport.googleapis.com/v2/{parent=organizations/*}/supportEventSubscriptions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name where the support event subscription will be created. Format: organizations/{organizationId}  
  
### Request body

The request body contains an instance of `[SupportEventSubscription](https://docs.cloud.google.com/support/docs/reference/rest/v2/organizations.supportEventSubscriptions#SupportEventSubscription)`.

### Response body

If successful, the response body contains a newly created instance of `[SupportEventSubscription](https://docs.cloud.google.com/support/docs/reference/rest/v2/organizations.supportEventSubscriptions#SupportEventSubscription)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsupport`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
