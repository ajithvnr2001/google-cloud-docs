---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/long-running-ops/
title: Check a running test operation \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:49.122410+00:00
---

# Check a running test operation  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/long-running-ops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Check a running test operation Stay organized with collections  Save and categorize content based on your preferences. 

Connectivity Tests supports periodically checking the status of a running test operation, such as `create`, `update`, or `delete`. You can still review the final test results when the test completes.

###  Console 

The Google Cloud console uses a spinner icon to show a running test. Behind the scenes, Connectivity Tests continuously polls for the status of the test operation. When the test completes, you can check the final results in the **Result details** panel.

For more information about Google Cloud console pages, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

###  gcloud 

To use the gcloud CLI to check a running test operation, specify the `--async` option. If you don't specify this option, you see only the final test results.

  1. For example, creating the following test by using the `--async` option immediately returns an _operation resource ID_ to the command line. You can then use this ID in a subsequent `describe` command to check test status while the test is still running.
         
         gcloud network-management connectivity-tests create NAME \
           --destination-project=DESTINATION_PROJECT \
           --source-ip-address=SOURCE_IP_ADDRESS \
           --destination-ip-address=DESTINATION_IP_ADDRESS \
           --protocol=PROTOCOL \
           --source-project=SOURCE_PROJECT \
           --round-trip \
           --async
         

Replace the following values:

     * `NAME`: the name of the Connectivity Tests
     * `DESTINATION_PROJECT`: the project ID of the destination endpoint
     * `SOURCE_IP_ADDRESS`: the internal or external source IP address that you are testing from; an IPv6 address is only allowed when the test's destination is a global load balancer VIP
     * `DESTINATION_IP_ADDRESS`: the internal or external source IP address that you are testing to; an IPv6 address is only allowed when the test's destination is a global load balancer VIP
     * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests
     * `SOURCE_PROJECT`: the project ID of the source endpoint

The output is the following:
    
    Create request issued for: [gcloud-example]
    Check operation [projects/reachability-e2e-test/locations/global/operations/operation-1580411210002-59d6028c56f71-85ef2899-54d8bc13] for status
    

  2. Use the operation resource ID with the `describe` command to check on the test's status:
         
         gcloud network-management operations describe \
         projects/SOURCE_PROJECT/locations/global/operations/OPERATION_RESOURCE_ID
         

Replace the following values:

     * `SOURCE_PROJECT`: the project ID of the source endpoint
     * `OPERATION_RESOURCE_ID`: the resource ID for the in-progress operation that you are checking (for example, `operation-1580411210002-59d6028c56f71-85ef2899-54d8bc13`)

The following sample output for the previous command shows `done: false`. When the test completes, this field changes to `done: true`.
    
    **done: false**
    metadata:
     '@type': type.googleapis.com/google.cloud.networkmanagement.v1.OperationMetadata
     apiVersion: v1
     cancelRequested: false
     createTime: '2020-01-30T19:06:50.055838110Z'
     endTime: '2020-01-30T19:06:57.637200039Z'
     target: projects/reachability-e2e-test/locations/global/connectivityTests/gcloud-example
     verb: create
    name:
     projects/reachability-e2e-test/locations/global/operations/operation-1580411210002-59d6028c56f71-85ef2899-54d8bc13
    response:
     '@type': type.googleapis.com/google.cloud.networkmanagement.v1beta1.ConnectivityTest
     createTime: '2020-01-30T19:06:50.050012906Z'
     ...  // Full resource metadata displayed here.
    

  3. Repeat the previous `describe` command until the output shows `done: true`.




###  API 

The Network Management API is always in `async` mode. When you issue a command to the API, you immediately receive an operation ID. You can use this ID to periodically check test status.

###  Python 

The Network Management API is always in `async` mode. When you use the API Python client to issue a request, you immediately receive an operation ID. You can use this ID to periodically check test status.

See the following example:
    
    
    project_id = 'PROJECT_ID'
    operation_id = 'OPERATION_ID'
    
    request = api.projects().locations().global_().operations().get(
            name='projects/%s/locations/global/operations/%s' % (project_id, operation_id))
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following values:

  * `PROJECT_ID`: the project ID for the project in which you created the test
  * `OPERATION_ID`: the resource ID for the in-progress operation that you are checking (for example, `operation-1580411210002-59d6028c56f71-85ef2899-54d8bc13`)



## What's next

  * [Learn about Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
