---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-connectivity-tests/
title: Update or delete tests \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:19.719745+00:00
---

# Update or delete tests  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-connectivity-tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Update or delete tests Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Connectivity Tests performs a [static analysis](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#no-data-plane-testing) of the resource configurations in your VPC network. This analysis does not represent the actual condition of the network data plane.

Learn how to edit or delete tests by following the steps on this page. You can edit or delete tests created by you and by others.

To create, view, or rerun tests, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

To learn about Connectivity Tests, see the [overview](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview).

## Before you begin

Before you can use Connectivity Tests, set up the following items in Google Cloud:

  1. In the Google Cloud console, go to the project selector page.

[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

Select or create a Google Cloud project.

  2. Ensure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project) for your Google Cloud project.
  3. Install the Google Cloud CLI, which is part of the Google Cloud CLI. To install the latest version of the gcloud CLI, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/docs).

For a list of all commands, see the [`gcloud` command reference](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/gcloud-sdk).

  4. [Enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/reference/enable-api). Enabling the API provides you with the following:

     * Example API calls that use the [Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/apis)

You can test Network Management API commands by using the API Explorer. In the Network Management API reference document, use the `Try this API` column to explore API fields and [run a test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create). 

     * Sample code that uses the API Python client

The example code assumes that you have constructed a resource named `api` to interact with the Network Management API. To construct a resource, use the [`build`](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html#build) function. See the following example:
           
           from googleapiclient.discovery import build
           api = build('networkmanagement', 'v1')
           

For more information about the API Python client, see the following:

       * [Google API Client Library for Python Docs](https://github.com/googleapis/google-api-python-client/tree/master/docs#google-api-client-library-for-python-docs) in GitHub, which includes installation and authentication instructions.
       * The [Network Management API](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.html) reference documentation for the API Python client.
  5. Obtain the permissions that you need to run and view tests. For details, see [Assign access](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control).



## Update a test

Follow the steps in this section to update a test. You can change any field except the `name` of the test.

To check the status of the `update` test operation while it's running, see [Check a running test operation](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/long-running-ops).

### Console

#### From the main Connectivity Tests page

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. To update a test, click its name.

  3. On the **Connectivity Test details** page, click **Edit** edit at the top of the page.

  4. Modify the test options.

  5. Click **Save**.

The test reruns automatically.




#### From the Network interface details page

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If it is not already selected, select the project that contains the instance for which you want to update a test.

  3. Click the instance for which you want to update a test.

  4. Under **Network interfaces** , select the network interface for which you want to update a test.

  5. Under **Network analysis** , click **Connectivity Tests**.

  6. Click the name of a test to update.

  7. On the **Connectivity Test details** page, click **Edit** edit at the top of the page.

  8. Modify the test options.

  9. Click **Save**.

The test reruns automatically.




###  gcloud 

To update a test, enter the following command using the test ID that you want to update and the command options that you want to change. The following example changes the destination IP address.
    
    
      gcloud network-management connectivity-tests update NAME \
        --destination-ip-address= DESTINATION_IP_ADDRESS \
        --round-trip
    

Replace the following values:

  * `NAME`: the name of the Connectivity Test
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to; an IPv6 address is only allowed when the test's destination is a global load balancer VIP



###  API 

Use the [`networkmanagement.connectivitytests.patch`](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/patch) method to update (edit) a test.
    
    
      PATCH https: //networkmanagement.googleapis.com/v1/{resource.name=projects/PROJECT_ID/locations/global/connectivityTests/TEST_ID}
        {
          "source": {
            "ipAddress": "SOURCE_IP_ADDRESS",
            "projectId": "SOURCE_PROJECT",
          },
        }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the source VM
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running
  * `SOURCE_IP_ADDRESS`: the internal or external source IP address that you are testing from; an IPv6 address is only allowed when the test's destination is a global load balancer VIP
  * `SOURCE_PROJECT`: the project ID of the source endpoint



###  Python 

The following example code updates the source IP address for a test. For more information, see [`patch`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#patch) in the API Python client reference documentation.
    
    
    project_id = "PROJECT_ID"
    test_id = "TEST_ID"
    test_input = {
      "source": {
        "ipAddress": "SOURCE_IP_ADDRESS"
      },
    }
    
    request = api.projects().locations().global_().connectivityTests().patch(
      name='projects/%s/locations/global/connectivityTests/%s' % (project_id, test_id),
      body=test_input,
      updateMask="source")
      
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project in which the test was created
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running
  * `SOURCE_IP_ADDRESS`: the internal or external source IP address that you are testing from; an IPv6 address is only allowed when the test's destination is a global load balancer VIP



`updateMask` is a required parameter that specifies the fields that your patch updates. This example updates the `source` field.

## Delete one or more tests

Follow the steps in this section to delete a test.

To check the status of the `delete` test operation while it's running, see [Check a running test operation](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/long-running-ops).

### Console

#### From the main Connectivity Tests page

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click the checkbox to the left of one or more tests to delete.

  3. At the top of the Google Cloud console page, click **Delete** delete.




#### From the Connectivity Test details page

  1. From the main **Connectivity Tests** page, click the name of a test.
  2. At the top of the **Connectivity Test details** page, click **Delete** delete.



#### From the Network interface details page

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If it is not already selected, select the project that contains the instance from which you want to delete a test.

  3. Click the instance from which you want to delete a test.

  4. Under **Network interfaces** , select the network interface from which you want to delete a test.

  5. Under **Network analysis** , click **Connectivity Tests**.

  6. Select the checkbox to the left of one or more tests that you want to delete.

  7. At the top of the list of tests, click **Delete** delete.




###  gcloud 

To delete a test, enter the following command. Use the test ID for the test that you want to delete.
    
    
      gcloud beta network-management connectivity-tests delete NAME
    

Replace `NAME` with the name of the Connectivity Test.

###  API 

Use the [`networkmanagement.connectivitytests.delete`](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/delete) method to delete a test.
    
    
    DELETE https://networkmanagement.googleapis.com/v1/{name=projects/PROJECT_ID/locations/global/connectivityTests/{TEST_ID}
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the source VM
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running



###  Python 

The following example code deletes a test. For more information, see [`delete`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#delete) in the API Python client reference documentation.
    
    
    project_id = "PROJECT_ID"
    test_id = "TEST_ID"
    request = api.projects().locations().global_().connectivityTests().delete(
              name='projects/%s/locations/global/connectivityTests/%s' % (project_id, test_id))
      
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project in which the test was created
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are deleting



## What's next

  * [Configuration analysis states](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
