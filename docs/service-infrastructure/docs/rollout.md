---
url: https://docs.cloud.google.com/service-infrastructure/docs/rollout/
title: Managing Service Rollouts \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:22.011006+00:00
---

# Managing Service Rollouts  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/rollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Managing Service Rollouts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Service Infrastructure to perform a gradual [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config) [rollouts](https://docs.cloud.google.com/service-infrastructure/docs/glossary#rollout).

Updating the service configuration for a production service is risky and can potentially cause an outage. The Service Management API allows you to gradually roll out configuration changes, thus mitigating the impact caused by bad service configurations.

You can deploy multiple service configuration versions and define how these versions will be used at runtime, all through calling the [`services.rollouts.create`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/create) method to initiate a [Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts). At most **5** service configurations can be rolled out at a time.

## Before you begin

To run the examples in this guide, make sure you first follow the instructions to complete the initial setup in [Getting Started with the Service Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started).

## Performing rollout

Assuming you have a [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) `endpointsapis.appspot.com` built on the Service Management API, you can perform the following steps to roll out a service configuration change in a staged and controlled manner.

For example, `endpointsapis.appspot.com` is currently using service configuration `old`, and you want to change it to use service configuration `new`. Instead of having the new service configuration instantaneously used by all production traffic, you can create a rollout to test the new service configuration with 10% of the total traffic:
    
    
    # Create rollout to test the new configuration with 10% traffic.
    $ gcurl -d '{
      "rolloutId": "canary-rollout",
      "serviceName": "endpointsapis.appspot.com",
      "trafficPercentStrategy": {
        "percentages": {
          "new": 10,
          "old": 90
        }
      }
    }' https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/rollouts
    {
      "name": "operations/rollouts.endpointsapis.appspot.com:canary-rollout"
      "metadata": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
        "resourceNames": [
          "services/endpointsapis.appspot.com/rollouts/canary-rollout"
        ],
        "startTime": ...
      },
      "response": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.Rollout",
        "rolloutId": "canary-rollout",
        "createTime": ...
        "trafficPercentStrategy": {
          "percentages": {
            "old": 90,
            "new": 10,
          }
        },
        "serviceName": "endpointsapis.appspot.com"
      }
    }
    

After the rollout is created, you can then get the status of the rollout by running the following command, substituting your own rollout ID:
    
    
    # Get rollout status of `operations/rollouts.endpointsapis.appspot.com:canary-rollout`.
    $ gcurl https://servicemanagement.googleapis.com/v1/operations/rollouts.endpointsapis.appspot.com:canary-rollout
    {
      "name": "operations/rollouts.endpointsapis.appspot.com:canary-rollout",
      "metadata": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
        "resourceNames": [
          "services/endpointsapis.appspot.com/rollouts/canary-rollout"
        ],
        "steps": [
          {
            "description": "update Service Controller",
            "status": "DONE"
          }
        ],
        "progressPercentage": 100,
        "startTime": ...
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.Rollout",
        "rolloutId": "canary-rollout",
        "createTime": ...
        "status": "SUCCESS",
        "trafficPercentStrategy": {
          "percentages": {
            "old": 90,
            "new": 10,
          }
        },
        "serviceName": "endpointsapis.appspot.com"
      }
    }
    

After making sure the canary rollout has completed and the new service configuration is good, you can then create a rollout to let it serve 100% of the traffic:
    
    
    # Create rollout to let new configuration serve 100% traffic.
    $ gcurl -d '{
      "rolloutId": "full-rollout",
      "serviceName": "endpointsapis.appspot.com",
      "trafficPercentStrategy": {
        "percentages": {
          "new": 100,
        }
      }
    }' https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/rollouts
    {
      "name": "operations/rollouts.endpointsapis.appspot.com:full-rollout",
      "metadata": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
        "resourceNames": [
          "services/endpointsapis.appspot.com/rollouts/full-rollout"
        ],
        "startTime": ...
      },
      "response": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.Rollout",
        "rolloutId": "full-rollout",
        "createTime": ...
        "trafficPercentStrategy": {
          "percentages": {
            "new": 100,
          }
        },
        "serviceName": "endpointsapis.appspot.com"
      }
    }
    

In case problems are observed during the test stage, you can roll back to the old configuration by doing:
    
    
    # Rollback to the old configuration.
    $ gcurl -d '{
      "rolloutId": "rollout-to-old",
      "serviceName": "endpointsapis.appspot.com",
      "trafficPercentStrategy": {
        "percentages": {
          "old": 100,
        }
      }
    }' https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/rollouts
    {
     "name": "operations/rollouts.endpointsapis.appspot.com:rollout-to-old",
     "metadata": {
       "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
       "resourceNames": [
         "services/endpointsapis.appspot.com/rollouts/rollout-to-old"
       ],
       "startTime": ...
     },
     "response": {
       "@type": "type.googleapis.com/google.api.servicemanagement.v1.Rollout",
       "rolloutId": "rollout-to-old",
       "createTime": ...
       "trafficPercentStrategy": {
         "percentages": {
           "old": 100,
         }
       },
       "serviceName": "endpointsapis.appspot.com"
     }
    

}

## Viewing rollout history

The Service Management API keeps a history of rollouts. To view the rollout history for `endpointsapis.appspot.com`, you can do:
    
    
    # List rollout history for `endpointsapis.appspot.com`.
    $ gcurl https://servicemanagement.googleapis.com/v1/services/endpointsapis.appspot.com/rollouts
    {
      "rollouts": [
        {
          "rolloutId": "canary-rollout",
          "createTime": ...
          "status": "IN_PROGRESS",
          "trafficPercentStrategy": {
            "percentages": {
              "old": 90,
              "new": 10
             }
          },
          "serviceName": "endpointsapis.appspot.com"
        },
        {
          "rolloutId": "old-rollout",
          "createTime": ...
          "status": "SUCCESS",
          "trafficPercentStrategy": {
            "percentages": {
              "old": 100
             }
          },
          "serviceName": "endpointsapis.appspot.com"
        },
        ...
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
