---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/psc/
title: Apigee connectivity issue with northbound Private Service Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:23.814442+00:00
---

# Apigee connectivity issue with northbound Private Service Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Apigee connectivity issue with northbound Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

When you attempt to set up a northbound Private Service Connect endpoint for your customer consumer project to an Apigee instance, the network endpoint group status remains in `Pending` and does not progress to `Accepted`.

## Symptom

The status of the Private Service Connect endpoint is `Pending` in the customer consumer project.

## Error messages

No error message. 

The configured Private Service Connect endpoint is stuck in the `Pending` status. 

## Possible causes

Cause | Description  
---|---  
The project with the configured Private Service Connect endpoint is not included in the consumer accept list for the Apigee instance. | The project where the Private Service Connect endpoint resides needs to be added to the Apigee instance.  
  
### Cause 1: Missing Private Service Connect Endpoint Project

The project with the configured Private Service Connect endpoint is not included in the consumer accept list for the Apigee instance. 

#### Diagnosis

  1. Find the Apigee service attachment information from the endpoint configuration in the customer consumer project. 
  2. Check if the consumer project is added to the consumer accept list for the Apigee instance. This can be done through the management API or the Console UI. 



#### API Example

The following output does not include the consumer project in the `consumerAcceptList`.

Sample command:
    
    
    curl -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/instances"
    

Where ORG_NAME is the ID of your Apigee organization. 

Sample output:
    
    
    {
      "instances": [
        {
          "name": "apigee-dev-us-central1-instance",
          "location": "us-central1",
          "host": "10.71.132.2",
          "port": "443",
          "createdAt": "1746546423661",
          "lastModifiedAt": "1747937301425",
          "state": "ACTIVE",
          "peeringCidrRange": "SLASH_22",
          "runtimeVersion": "1-15-0-apigee-4",
          "ipRange": "10.71.132.0/22,10.71.136.0/28",
          "consumerAcceptList": [
            "prj-example-dev"
          ],
          "serviceAttachment": "projects/a1b2c3d4e5f6g7h8ip-tp/regions/us-central1/serviceAttachments/apigee-us-central1-7xxw",
          "accessLoggingConfig": {
            "enabled": true
          }
        }
      ]
    }
    
    

#### Resolution

Follow the [Northbound networking with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc#updating-the-consumer-accept-list-for-an-apigee-instance) documentation and use either the Apigee UI or the Management API to update the Apigee instance's `consumerAcceptList` with the new endpoint group project. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
