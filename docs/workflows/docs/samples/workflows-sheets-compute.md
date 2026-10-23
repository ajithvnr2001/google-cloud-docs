---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-sheets-compute/
title: Create a Compute Engine VM instance using the Compute Engine API connector \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:22.768701+00:00
---

# Create a Compute Engine VM instance using the Compute Engine API connector  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-sheets-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Create a Compute Engine VM instance using the Compute Engine API connector Stay organized with collections  Save and categorize content based on your preferences. 

Calls the Compute Engine API connector to create a Compute Engine VM instance based on specifications collected through Google Forms.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Trigger a workflow from Google Sheets](https://docs.cloud.google.com/workflows/docs/tutorials/trigger-workflow-from-sheets)



## Code sample

### YAML
    
    
    main:
       params: [input]
       steps:
       - init:
           assign:
                - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                - zone: ${input.zone}
                - machineType: ${input.machineType}
                - diskSize: ${input.diskSize}
                - imageProject: ${input.imageProject}
                - imageFamily: ${input.imageFamily}
                - vmName: ${input.vmName}
                - email: ${input.email}
       - createResource:
           call: googleapis.compute.v1.instances.insert
           args:
               project: ${projectId}
               zone: ${zone}
               body:
                   name: ${vmName}
                   machineType: ${"projects/" + projectId + "/zones/" + zone + "/machineTypes/" + machineType}
                   disks:
                    - initializeParams:
                        diskSizeGb: ${diskSize}
                        sourceImage: ${"projects/" + imageProject + "/global/images/family/" + imageFamily}
                      type: PERSISTENT
                      boot: true
                      autoDelete: true
                   networkInterfaces:
                    - network: "global/networks/default"
           result: insertResult
       - retStep:
           return: ${insertResult}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
