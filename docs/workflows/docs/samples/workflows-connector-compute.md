---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-compute/
title: Connector for Compute Engine \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:32.784599+00:00
---

# Connector for Compute Engine  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Compute Engine within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Compute Engine API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Compute Engine connector:
    # Create and start a Compute Engine VM instance, then stop and delete the VM
    # Each step waits until the long-running operation of stopping or starting the VM completes
    # After each step, the machine status is verified
    # Expected output: "SUCCESS"
    main:
      params: []
      steps:
        - init:
            assign:
              - project: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
              - zone: "us-central1-a"
              - instance: "INSTANCE_NAME"  # replace INSTANCE_NAME placeholder
              - machineType: "e2-micro"
        - insert_machine:
            call: googleapis.compute.v1.instances.insert
            args:
              project: ${project}
              zone: ${zone}
              body:
                name: ${instance}
                machineType: ${"zones/" + zone + "/machineTypes/" + machineType}
                disks:
                  - initializeParams:
                      sourceImage: "projects/debian-cloud/global/images/debian-10-buster-v20201112"
                    boot: true
                    autoDelete: true
                networkInterfaces:
                  - network: "global/networks/default"
        - start_machine:
            call: googleapis.compute.v1.instances.start
            args:
              instance: ${instance}
              project: ${project}
              zone: ${zone}
        - assert_running:
            call: assert_machine_status
            args:
              expected_status: "RUNNING"
              project: ${project}
              zone: ${zone}
              instance: ${instance}
        - stop_machine:
            call: googleapis.compute.v1.instances.stop
            args:
              instance: ${instance}
              project: ${project}
              zone: ${zone}
        - assert_terminated:
            call: assert_machine_status
            args:
              expected_status: "TERMINATED"
              project: ${project}
              zone: ${zone}
              instance: ${instance}
        - delete_machine:
            call: googleapis.compute.v1.instances.delete
            args:
              instance: ${instance}
              project: ${project}
              zone: ${zone}
        - the_end:
            return: "SUCCESS"
    
    assert_machine_status:
      params: [expected_status, project, zone, instance]
      steps:
        - get_instance:
            call: googleapis.compute.v1.instances.get
            args:
              instance: ${instance}
              project: ${project}
              zone: ${zone}
            result: instance
        - compare:
            switch:
              - condition: ${instance.status == expected_status}
                next: end
        - fail:
            raise: ${"Expected VM status is " + expected_status + ". Received " + instance.status + " instead."}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
