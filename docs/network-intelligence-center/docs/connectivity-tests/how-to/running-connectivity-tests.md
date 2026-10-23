---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests/
title: Create and run Connectivity Tests \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:58.034236+00:00
---

# Create and run Connectivity Tests  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Create and run Connectivity Tests Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to run Connectivity Tests by following the steps on this page.

To edit or delete one or more tests, see [Update or delete tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-connectivity-tests).

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



## Run Connectivity Tests

When you run a Connectivity Test, you provide test inputs as a [5-tuple without the source port](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/reachability#endpoints).

The following sections show you how to run a test for source and destination endpoints described in [Common use cases](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/common-use-cases).

From the Google Cloud console, you can run Connectivity Tests by using either of the following:

  * The **Connectivity Tests** page, which is available from the **Networking > Network Intelligence Center** menu.

  * The **Network interface details** page for a network interface of a Compute Engine virtual machine (VM) instance. If you use this page, you must use the current network interface as either the **Source** or **Destination** of the test. This page only lists tests relevant to the current network interface.




Each test that you create runs immediately after you create it and is stored in the Connectivity Tests resource. A test exists until you delete it.

To check the status of a test operation while the operation runs, see [Check a running test operation](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/long-running-ops). Some examples of test operations are `create` and `rerun`.

When you use an IP address for the source or destination endpoint, you might need to specify additional fields.

### Best practices

It takes between 20 and 120 seconds for Connectivity Tests to receive a configuration update and incorporate it into analysis. If you run a test immediately after making a configuration change, you might not see the results that you expect. Make sure that you wait long enough between making the configuration change and running your tests.

This delay does not apply to live data plane analysis. Therefore, you might see a temporary mismatch between the results shown by live data plane analysis and configuration analysis. For example, if you add a firewall rule, it might be reachable for live data plane analysis. However, you might have to wait for some time before the firewall rule is reachable for configuration analysis.

### List all tests for a project

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. At the top of the page, in the drop-down project menu, select a project.
  3. The **Connectivity Tests** page refreshes and shows you the tests for that project.



###  gcloud 

To list all tests owned by a project, enter the following `gcloud` command. This command shows tests in the currently selected project.
    
    
      gcloud network-management connectivity-tests list
    

To list tests in a specific project, specify the `PROJECT_ID`.
    
    
      gcloud network-management connectivity-tests list --project=PROJECT_ID
    

###  API 

To list all existing tests owned by a project, use the [`projects.locations.global.connectivityTests.list` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/list).
    
    
    GET https://networkmanagement.googleapis.com/v1/{parent=projects/PROJECT_ID/locations/global}/connectivityTests
    

  * Replace `PROJECT_ID` with the project ID of the project that contains the tests that you want to list.



###  Python 

The following example code lists all existing tests owned by a project. For more information, see [`list`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#list) in the Google API Client Library for Python.
    
    
    project_id = "PROJECT_ID"
    parent = 'projects/%s/locations/global' % project_id
    request = api.projects().locations().global_().connectivityTests().list(parent=parent)  
    
    print(json.dumps(request.execute(), indent=4))
    

Replace `PROJECT_ID` with the project ID of the project that contains the tests that you want to list.

### Test between private IP addresses in a VPC network

This example assumes that both IP addresses are private IP addresses in the same VPC network.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list?walkthrough_id=network-intelligence--test-private-ip-addresses&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Select **Create Connectivity Test**.

  3. In the **Test name** field, enter a name for the test. 
  4. In the **Protocol** list, select a protocol. 
  5. For **Source** , do the following:

     1. In the **Source endpoint** list, select **IP address**.
     2. In the **Source IP address** field, enter the source IP address.
     3. In the **IP address type** list, select the type of the IP address.
  6. For **Destination** , do the following:

     1. In the **Destination endpoint** list, select **IP address**.
     2. In the **Destination IP address** field, enter the destination IP address.
  7. In the **Destination port** field, enter a valid destination port number. The number must be between 0 and 65535, inclusive. 
  8. Click **Create**. 



After the test finishes, the main Connectivity Tests page loads and shows a list that contains this test and other tests. Continue to [View test results](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#viewing-tests). 

###  gcloud 

Replace variables for the command options with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --source-network=SOURCE_NETWORK \
        --source-network-type=GCP_NETWORK \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.


    
    
    gcloud network-management connectivity-tests create NAME \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --source-network=SOURCE_NETWORK \
        --source-network-type=GCP_NETWORK \
        --destination-instance=DESTINATION_INSTANCE  \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



When you specify a source IP address that is an external IP address outside of Google Cloud, you must set the `networkType` parameter to `INTERNET`. Replace the values in the following command with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --source-network-type=INTERNET \
        --destination-ip-address= DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Terraform 

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_management_connectivity_test) to create a test between two IP addresses in a VPC network.

You do not have to confirm whether your IP address is in Google Cloud or whether the source and destination endpoints are outside the RFC 1918 address space. These parameters are automatically selected based on your source and destination IP addresses.
    
    
    resource "google_network_management_connectivity_test" "default" {
      name = "conn-test-addr"
      source {
        ip_address   = google_compute_address.source_addr.address
        project_id   = google_compute_address.source_addr.project
        network      = google_compute_network.default.id
        network_type = "GCP_NETWORK"
      }
    
      destination {
        ip_address = google_compute_address.dest_addr.address
        project_id = google_compute_address.dest_addr.project
        network    = google_compute_network.default.id
        port       = "80"
      }
    
      protocol = "UDP"
    }
    
    resource "google_compute_network" "default" {
      name                    = "connectivity-vpc"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "default" {
      name          = "connectivity-vpc-subnet"
      ip_cidr_range = "10.0.0.0/8"
      region        = "us-central1"
      network       = google_compute_network.default.id
    }
    
    resource "google_compute_firewall" "default" {
      name    = "allow-incoming-all"
      network = google_compute_network.default.name
    
      allow {
        protocol = "all"
      }
    
      source_ranges = ["0.0.0.0/0"]
    }
    
    resource "google_compute_address" "source_addr" {
      name         = "src-addr"
      subnetwork   = google_compute_subnetwork.default.id
      address_type = "INTERNAL"
      address      = "10.0.0.42"
      region       = "us-central1"
    }
    
    resource "google_compute_address" "dest_addr" {
      name         = "dest-addr"
      subnetwork   = google_compute_subnetwork.default.id
      address_type = "INTERNAL"
      address      = "10.0.0.43"
      region       = "us-central1"
    }
    
    resource "google_compute_instance" "source" {
      name         = "source-vm1"
      machine_type = "e2-medium"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = data.google_compute_image.default.id
        }
      }
    
      network_interface {
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.default.id
        network_ip = "10.0.0.42"
        access_config {
        }
      }
    }
    
    resource "google_compute_instance" "destination" {
      name         = "dest-vm1"
      machine_type = "e2-medium"
      zone         = "us-central1-a"
    
      boot_disk {
        initialize_params {
          image = data.google_compute_image.default.id
        }
      }
    
      network_interface {
        network    = google_compute_network.default.id
        subnetwork = google_compute_subnetwork.default.id
        network_ip = "10.0.0.43"
        access_config {
        }
      }
    }
    
    data "google_compute_image" "default" {
      family  = "debian-13"
      project = "debian-cloud"
    }

###  API 

This example tests the ability to ping from the source IP address to the destination IP address.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
      POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "network": "SOURCE_NETWORK",
          "networkType": "GCP_NETWORK",
        },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
        },
          "protocol": "PROTOCOL".
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.


    
    
      POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?connectivityTestId=TEST_ID'
      {
        "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "networkType": "GCP_NETWORK"
        },
        "destination": {
          "instance": "DESTINATION_INSTANCE",
          "ipAddress": "DESTINATION_IP_ADDRESS"
        },
        "protocol": "PROTOCOL"
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



When you specify a source IP address that is an external IP address outside of Google Cloud, you must set the `networkType` parameter to `INTERNET`. Replace the values in the following command with values for your Google Cloud network.
    
    
      POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "networkType": "INTERNET",
        },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
        },
        "protocol": "PROTOCOL",
      }'
    

###  Python 

The following example code creates a test between two IP addresses. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "network": "SOURCE_NETWORK",
          "networkType": "GCP_NETWORK"
      },
      "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
      },
      "protocol": "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



The following example creates a test between two IP addresses:
    
    
    test_input = {
        "source": {
            "ipAddress": "SOURCE_IP_ADDRESS",
            "network": "SOURCE_NETWORK",
            "networkType": "GCP_NETWORK"
        },
        "destination": {
            "ipAddress": "DESTINATION_IP_ADDRESS",
            "port": "DESTINATION_PORT",
        },
        "protocol": "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
      parent="projects/PROJECT_ID/locations/global",
      testId="TEST_ID",
      body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



When you specify a source IP address that is an external IP address outside of Google Cloud, you must set the `networkType` parameter to `INTERNET`.

### Test between VM instances in a VPC network

These steps assume that both VM instances are in the same Google Cloud project.

###  Console 

#### From the main Connectivity Tests page

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[ Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list?walkthrough_id=network-intelligence--test-vm-connectivity)

school The remaining steps appear automatically in the Google Cloud console. 

  2. Select **Create Connectivity Test**. 
  3. In the **Test name** field, enter a name for the test. 
  4. In the **Protocol** list, select a protocol. 
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **VM instance**.
     2. In the **Source VM instance** menu, select the specific source VM instance.
     3. In the **Source network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface that uniquely identifies the source location.

     4. Optional: Select the **Source IP address** from the list. The default is the IP address of the source VM instance.
  6. For **Destination** , do the following: 
     1. In the **Destination endpoint** menu, select **VM instance**.
     2. In the **Destination VM instance** menu, select the specific destination VM instance.
     3. In the **Destination network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface to identify the destination location uniquely.

     4. Optional: Select the **Destination IP address** from the list. The default is the IP address of the destination VM instance.

**Note:** For a [dual-stack instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), the source and the destination IP address must be of the same type. For example, you cannot test from a VM with an IPv4 address to a VM with an IPv6 address.

  7. In the **Destination port** field, enter a destination port. 
  8. Click **Create**. 

After the test finishes, the main Connectivity Tests page loads and shows a list that contains this test and other tests. Continue to [View test results](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#viewing-tests). 




#### From the Network interface details page

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If it is not already selected, select the project that contains the instance for which you want to run a test.
  3. Click the instance that you want to use to run a test.
  4. For **Network interfaces** , select the network interface that you want to use to run a test.

If the VM instance has multiple network interfaces, select a VM network interface to uniquely identify the destination location.

  5. For **Network analysis** , click **Create Connectivity Test** , and do the following:

     1. In the **Test name** field, enter a name for the test.
     2. In the **Protocol** list, select a protocol.
     3. For **Source** , you can select either **Current network interface** or **Other**.

If you select **Current network interface** , do the following:

        1. In the **Destination endpoint** menu, select **VM instance**.
        2. In the **Destination VM instance** menu, select the instance.
        3. In the **Destination network interface** menu, select the network interface.
        4. Optional: Select the destination IP address. The default is the IP address of the destination VM instance.

If you select **Other** , do the following:

        1. In the **Source endpoint** menu, select **VM instance**.
        2. In the **Source VM instance** menu, select the instance.
        3. In the **Source network interface** menu, select the network interface.
        4. Optional: Select source IP address. The default is the IP address of the source VM instance.
     4. In the **Destination port** field, enter a destination port for your specified destination.

     5. Click **Create**.

  6. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-instance=SOURCE_INSTANCE \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --destination-instance=DESTINATION_INSTANCE \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Terraform 

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_management_connectivity_test) to create a test between two VM instances in a VPC network.
    
    
    resource "google_network_management_connectivity_test" "instance_test" {
      name = "conn-test-instances"
      source {
        instance = google_compute_instance.source.id
      }
    
      destination {
        instance = google_compute_instance.destination.id
        port     = "80"
      }
    
      protocol = "TCP"
    }
    
    resource "google_compute_instance" "source" {
      name         = "source-vm"
      machine_type = "e2-medium"
    
      boot_disk {
        initialize_params {
          image = data.google_compute_image.debian_9.id
        }
      }
    
      network_interface {
        network = "default"
        access_config {
        }
      }
    }
    
    resource "google_compute_instance" "destination" {
      name         = "dest-vm"
      machine_type = "e2-medium"
    
      boot_disk {
        initialize_params {
          image = data.google_compute_image.debian_9.id
        }
      }
    
      network_interface {
        network = "default"
        access_config {
        }
      }
    }
    
    data "google_compute_image" "debian_9" {
      family  = "debian-13"
      project = "debian-cloud"
    }

###  API 

The following sample test determines if the existing network configuration allows VM `instance1`to ping VM `instance2`.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
     POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
       {
         "source": {
           "instance": "SOURCE_INSTANCE",
           "ipAddress": "SOURCE_IP_ADDRESS",
         },
         "destination": {
           "instance": "DESTINATION_INSTANCE",
           "ipAddress": "DESTINATION_IP_ADDRESS",
         },
         "protocol": "PROTOCOL",
       }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between two VM instances. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "instance":
              "SOURCE_INSTANCE",
          "ipAddress":
              "SOURCE_IP_ADDRESS",
          "projectId":
              "SOURCE_INSTANCE_PROJECT_ID"
      },
      "destination": {
          "instance":
              "DESTINATION_INSTANCE",
          "ipAddress":
              "DESTINATION_IP_ADDRESS",
          "projectId":
              "DESTINATION_INSTANCE_PROJECT_ID"
      },
      "protocol":
          "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `SOURCE_INSTANCE_PROJECT_ID`: the project ID of the source VM.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `DESTINATION_INSTANCE_PROJECT_ID`: the project ID of the destination VM.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



### Test to or from a VM with multiple network interfaces

This section describes how to test to or from a VM's non-primary network interface.

###  Console 

If you specify a VM instance with multiple network interfaces as the source or destination of a test, Connectivity Tests prompts you to select a network interface from a list.

Alternatively, you can run a test from the **Network interface details** page for a network interface of a Compute Engine VM instance. If you use this page, you must use the current network interface as either the **Source** or **Destination** of the test.

###  gcloud and API

You must specify the network interface to use for the test in one of the following ways:

  * IP address and network URI
  * IP address and VM URI
  * Network URI and VM URI



Providing only the URI for a VM with multiple interfaces selects only the VM's primary interface.

### Test from a VM to a Google-managed service

This section describes how to test from a VM in your VPC network to a service that runs in a Google-owned VPC network. For example, you can follow the steps in this section to test connectivity to a Cloud SQL instance or a Google Kubernetes Engine cluster [_control plane_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane). You can also run a test by using a Google-managed service endpoint as the source and an endpoint in your VPC network as the destination.

By default, Connectivity Tests attempts to run a test by using the private IP address of the Google-managed service endpoint. If the endpoint does not have a private IP address, Connectivity Tests uses the public IP address. Connectivity Tests analyzes whether the packet can reach the endpoint, which includes analyzing the configuration within the Google-owned VPC network. If configuration issues are detected within your project, the analysis stops before analyzing the Google-owned network configuration.

To test from a VM to a Google-managed service, see the following instructions.

###  Console 

#### From the main Connectivity Tests page

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following:

     1. In the **Source endpoint** menu, select **VM instance**.
     2. In the **Source VM instance** menu, select the specific source VM instance.
     3. In the **Source network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface that uniquely identifies the source location.

     4. Optional: Select the **Source IP address** from the list. The default is the IP address of the source VM instance.

  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select a type of Google-managed service resource such as **GKE cluster control plane**.
     2. In the **Destination GKE cluster control plane** menu, select the cluster for which you want to test connectivity to the GKE control plane.
     3. Optional: Select the **Destination GKE cluster control plane endpoint** from the list. The default is the IP-based endpoint of the GKE cluster.
  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




#### From the Network interface details page

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If it is not already selected, select the project that contains the instance for which you want to run a test.
  3. Click the instance that you want to use to run a test.
  4. For **Network interfaces** , select the network interface that you want to use to run a test.
  5. For **Network analysis** , click **Create Connectivity Test**.
  6. In the **Test name** field, enter a name for the test.
  7. In the **Protocol** list, select a protocol.
  8. For **Source** , select **Current network interface**.
  9. For **Destination** , do the following: 
     1. In the **Destination endpoint** menu, select a type of Google-managed service resource such as **GKE cluster control plane**.
     2. In the **Destination GKE cluster control plane** menu, select the cluster for which you want to test connectivity to the GKE control plane.
     3. Optional: Select the **Destination GKE cluster control plane endpoint** from the list. The default is the IP-based endpoint of the GKE cluster.
  10. In the **Destination port** field, enter a destination port for your specified destination. 
     1. Click **Create**.
     2. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Replace the variables for the command options according to the following guidance:
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-instance=SOURCE_INSTANCE \
        --source-ip-address=SOURCE_IP_ADDRESS \
          DESTINATION_RESOURCE_FLAG=DESTINATION_ENDPOINT \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_RESOURCE_FLAG`: the flag that specifies the type of Google-managed service resource.

For available options, see the following:

    * `--destination-gke-master-cluster`
    * `--destination-cloud-sql-instance`
    * `--destination-redis-instance`
    * `--destination-redis-cluster`

For more information, see the [`gcloud network-management connectivity-tests create` reference](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the flag `--destination-gke-master-cluster`.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.

  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.




###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
     POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
       {
         "source": {
           "instance": "SOURCE_INSTANCE",
           "ipAddress": "SOURCE_IP_ADDRESS",
         },
         "destination": {
           "DESTINATION_RESOURCE_FIELD": "DESTINATION_ENDPOINT",
           "port": DESTINATION_PORT
         },
         "protocol": "PROTOCOL",
       }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_RESOURCE_FIELD`: the field that specifies the type of Google-managed service resource.

For available options, see the following:

    * `gkeMasterCluster`
    * `cloudSqlInstance`
    * `redisInstance`
    * `redisCluster`

For more information, see the [Endpoint reference](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the field `gkeMasterCluster`.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.

  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.




###  Python 

The following example code creates a test between a VM instance and a Google-managed service endpoint. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "instance":
              "SOURCE_INSTANCE",
          "ipAddress":
              "SOURCE_IP_ADDRESS",
          "projectId":
              "SOURCE_INSTANCE_PROJECT_ID"
      },
      "destination": {
          "DESTINATION_RESOURCE_FIELD":
              "DESTINATION_ENDPOINT",
          "port":
              "DESTINATION_PORT"
      },
      "protocol":
          "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `SOURCE_INSTANCE_PROJECT_ID`: the project ID of the source VM.
  * `DESTINATION_RESOURCE_FIELD`: the field that specifies the type of Google-managed service resource.

For available options, see the following:

    * `gkeMasterCluster`
    * `cloudSqlInstance`
    * `redisInstance`
    * `redisCluster`

For more information, see the [Endpoint reference](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the field `gkeMasterCluster`.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.

  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.

  * `PROJECT_ID`: the project ID of the project in which you are creating the test.

  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.




### Test from a VM to Private Service Connect endpoints

This section describes how to test from a VM to a Private Service Connect endpoint.

For example, you can follow the steps in this section to test if a packet could be delivered to a published service that uses Private Service Connect. Connectivity Tests analyzes whether a packet can reach the endpoint, which includes analyzing connected endpoints, published services, and the proxy connection. The analysis ends early if the connection to a published service that uses Private Service Connect is not accepted.

You can test connectivity to the following:

  * [Endpoints for Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis)

  * [Endpoints for published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services)




###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following:

     1. In the **Source endpoint** menu, select **VM instance**.
     2. In the **Source VM instance** menu, select the specific source VM instance.
     3. In the **Source network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface that uniquely identifies the source location.

     4. Optional: Select the **Source IP address** from the list. The default is the IP address of the source VM instance.

  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select **PSC endpoint**.
     2. In the **Destination PSC endpoint** menu, select the PSC endpoint.

If the destination endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**. Then, in the **Destination endpoint project** field, select the project where the endpoint is located.

  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-instance=SOURCE_INSTANCE \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_IP_ADDRESS`: the IP address of the endpoint or backend that you want to test.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

The following sample test determines whether the existing network configuration allows VM `instance1` to ping the IP address of the Private Service Connect endpoint.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
     POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
       {
         "source": {
           "instance": "SOURCE_INSTANCE",
           "ipAddress": "SOURCE_IP_ADDRESS",
         },
        "destination": {
          "forwardingRule": "DESTINATION_FORWARDING_RULE",
          "port": "DESTINATION_PORT",
         },
         "protocol": "PROTOCOL",
       }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_IP_ADDRESS`: the IP address of the endpoint or backend that you want to test.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between a VM instance and a Private Service Connect endpoint. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "instance":
              "SOURCE_INSTANCE",
          "ipAddress":
              "SOURCE_IP_ADDRESS",
          "projectId":
              "SOURCE_INSTANCE_PROJECT_ID"
      },
      "destination": {
          "forwardingRule": "DESTINATION_FORWARDING_RULE",
          "port": "DESTINATION_PORT",
      },
      "protocol":
          "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `SOURCE_INSTANCE_PROJECT_ID`: the project ID of the source VM.
  * `DESTINATION_IP_ADDRESS`: the IP address of the endpoint or backend that you want to test.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



### Test from a VM or an IP address to a load balancer

This section describes how to test connectivity from a VM or an IP address to a Google Cloud load balancer.

Connectivity Tests configuration analysis supports tracing simulated packets to all types of Google Cloud load balancers. The trace path for an external Application Load Balancer also applies to external proxy Network Load Balancers. For more information, see the [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).

You can test connectivity to the following:

  * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
  * [External passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network)
  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [External proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/ssl)



#### Test from a VM to a load balancer

This section analyzes connectivity from the source VM to a [load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following:

     1. In the **Source endpoint** menu, select **VM instance**.
     2. In the **Source VM instance** menu, select the specific source VM instance.
     3. In the **Source network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface that uniquely identifies the source location.

     4. Optional: Select the **Source IP address** from the list. The default is the IP address of the source VM instance.

  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select **Load Balancer**.
     2. In the **Destination Load Balancer** menu, select the load balancer.

If the destination endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**. Then, in the **Destination endpoint project** field, select the project where the endpoint is located.

     3. Select the **Destination Forwarding Rule**.

**Note:** A load balancer can have multiple frontend configurations and each configuration is represented by a forwarding rule. For a general understanding of forwarding rules, see [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).
  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

To test between a VM and a load balancer, enter the following command.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-instance=SOURCE_INSTANCE \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --protocol=PROTOCOL \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing against.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
     POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
       {
         "source": {
           "instance": "SOURCE_INSTANCE",
           "ipAddress": "SOURCE_IP_ADDRESS",
         },
        "destination": {
          "forwardingRule": "DESTINATION_FORWARDING_RULE",
          "port": "DESTINATION_PORT",
         },
         "protocol": "PROTOCOL",
       }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_FORWARDING_RULE`: the destination forwarding rule that represents the endpoint.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between a VM instance and a load balancer endpoint. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "instance":
              "SOURCE_INSTANCE",
          "ipAddress":
              "SOURCE_IP_ADDRESS",
          "projectId":
              "SOURCE_INSTANCE_PROJECT_ID"
      },
      "destination": {
          "forwardingRule": "DESTINATION_FORWARDING_RULE",
          "port": "DESTINATION_PORT",
      },
      "protocol":
          "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `SOURCE_INSTANCE_PROJECT_ID`: the project ID of the source VM.
  * `DESTINATION_FORWARDING_RULE`: the destination forwarding rule that represents the endpoint.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



#### Test from an IP address to a load balancer

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **IP address**.
     2. In the **Source IP address** field, enter the source IP address, and then select the IP address type.
  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select **Load Balancer**.
     2. In the **Destination Load Balancer** menu, select the load balancer endpoint.

If the destination endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**. Then, in the **Destination endpoint project** field, select the project where the endpoint is located.

     3. Select the **Destination Forwarding Rule**.

**Note:** A load balancer can have multiple frontend configurations and each configuration is represented by a forwarding rule. For a general understanding of forwarding rules, see [Forwarding rule concepts](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).
  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-project=SOURCE_PROJECT \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --protocol=PROTOCOL \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_PROJECT`: the project ID of the source endpoint.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.



###  API 

This example tests the ability to ping from the source IP address to a load balancer endpoint.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).

When you specify a source IP address that is an external IP address outside of Google Cloud, you must set the `networkType` parameter to `INTERNET`. Replace the values in the following command with values for your Google Cloud network.
    
    
      POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "networkType": "INTERNET",
        },
        "destination": {
          "forwardingRule": "DESTINATION_FORWARDING_RULE",
          "port": "DESTINATION_PORT",
        },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `DESTINATION_FORWARDING_RULE`: the destination forwarding rule that represents the endpoint.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between an IP address to a load balancer endpoint. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.

When you specify a source IP address that is an external IP address outside of Google Cloud, you must set the `networkType` parameter to `INTERNET`.
    
    
    test_input = {
        "source": {
            "ipAddress": "SOURCE_IP_ADDRESS",
            "networkType": "INTERNET"
        },
        "destination": {
            "forwardingRule": "DESTINATION_FORWARDING_RULE",
            "port": "DESTINATION_PORT",
            "projectId": "DESTINATION_IP_PROJECT_ID"
        },
        "protocol": "PROTOCOL",
    }
    
      request = api.projects().locations().global_().connectivityTests().create(
      parent="projects/PROJECT_ID/locations/global",
      testId="TEST_ID",
      body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `DESTINATION_FORWARDING_RULE`: the destination forwarding rule that represents the endpoint.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `DESTINATION_IP_PROJECT_ID`: the project ID for the destination IP address.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



### Test between GKE Pods

Follow these steps to test connectivity between GKE Pods. Connectivity Tests also supports testing between a Pod and any other [supported endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#supported-configs), such as a VM instance or a load balancer.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.

  3. For **Test name** , enter a name for the test.

  4. In the **Protocol** list, select a protocol.

  5. In the **Source** section, do the following:

     1. For **Source endpoint** , select **GKE pod**.
     2. For **Source cluster** , select the GKE cluster where the Pod is deployed.
     3. If the source Pod isn't in your current project, select **Endpoint is in a project other than [name-of-your-project]** and then select the project of the Pod.
     4. For **Source namespace** , select the namespace of the Pod.
     5. For **Source pod** , select a Pod.
  6. In the **Destination** section, do the following:

     1. For **Destination endpoint** , select **GKE pod**.
     2. For **Destination cluster** , select the GKE cluster where the Pod is deployed.
     3. If the destination Pod isn't in your current project, select **Endpoint is in a project other than [name-of-your-project]** and then select the project of the Pod.
     4. For **Destination namespace** , select the namespace of the Pod.
     5. For **Destination pod** , select a Pod.
     6. For **Destination port** , enter a destination port. This option is displayed only if TCP or UDP is selected for **Protocol**.
  7. Click **Create**.




After the test completes, Connectivity Tests displays your test results.

**Note:** To specify a Pod by its IP address instead of name, select **IP address** as the endpoint type.

###  gcloud 

Use the [gcloud network-management connectivity-tests create command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).
    
    
    gcloud network-management connectivity-tests create NAME \
        --protocol=PROTOCOL \
        --source-gke-pod=SOURCE_POD \
        --destination-gke-pod=DESTINATION_POD \
        --destination-port=DESTINATION_PORT \
        --round-trip
    

Replace the following:

  * `NAME`: a name for your test.
  * `PROTOCOL`: a supported protocol. The default protocol is `TCP`.
  * `SOURCE_POD`: the URI of the source Pod—for example, `projects/my-project/locations/us-central1/clusters/my-cluster/k8s/namespaces/default/pods/my-pod-1`.

To specify the Pod by its IP address, use the `--source-ip-address` flag instead.

  * `DESTINATION_POD`: the URI of the destination Pod—for example, `projects/my-project/locations/us-central1/clusters/my-cluster/k8s/namespaces/default/pods/my-pod-2`.

To specify the Pod by its IP address, use the `--destination-ip-address` flag instead.

  * `DESTINATION_PORT`: a destination port; for example, `80`. Specify only if you are creating a TCP or UDP test.




###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID
        {
            "protocol": "PROTOCOL",
            "source": {
                "gkePod": "SOURCE_POD"
            },
            "destination": {
                "gkePod": "DESTINATION_POD",
                "port": DESTINATION_PORT
            }
        }
      

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the test.
  * `TEST_ID`: a name for the test.
  * `PROTOCOL`: a supported protocol. The default protocol is `TCP`.
  * `SOURCE_POD`: the URI of the source Pod—for example, `projects/my-project/locations/us-central1/clusters/my-cluster/k8s/namespaces/default/pods/my-pod-1`.

To specify the Pod by its IP address, use the `ipAddress` parameter instead.

  * `DESTINATION_POD`: the URI of the destination Pod—for example, `projects/my-project/locations/us-central1/clusters/my-cluster/k8s/namespaces/default/pods/my-pod-2`.

To specify the Pod by its IP address, use the `ipAddress` parameter instead.

  * `DESTINATION_PORT`: a destination port; for example, `80`. Specify only if you are creating a TCP or UDP test.




### Test from an App Engine standard environment version to a destination

This section describes how to test connectivity from an App Engine standard environment version to a VM instance, an IP address, or a Google-managed service.

An App Engine standard environment app is made up of a single application resource that consists of one or more services. Within each service, you deploy versions of that service. You can test reachability from a version of an App Engine standard environment service to a VM instance, an IP address, or a Google-managed service.

A Connectivity Test result might be different for each version of the service, depending on the connectivity type and egress settings as described in [Considerations for serverless endpoints](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#serverless-supported-features). You can test reachability only for UDP or TCP packets.

#### Test connectivity from a version of an App Engine standard environment service to a VM instance

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. Enter a name for the test.
  4. Select a protocol.
  5. In the **Source endpoint** menu, select **App Engine**. 
     1. In the **App Engine service** menu, select the specific App Engine standard environment service from which you want to test connectivity. For example, select `helloworld-service`. 
        1. If the source endpoint is in a project other than the current project, select the **Endpoint is in a project other than "` PROJECT_NAME`"** checkbox.
        2. Select a project where the endpoint exists.
     2. In the **App Engine version** menu, select a version of the App Engine standard environment service from which you want to test connectivity.
  6. For **Destination** , select a **Destination VM instance** from the list.

If the VM instance has multiple network interfaces, select a VM network interface to uniquely identify the destination location.

  7. Optional: Select the **Destination IP address** from the list. The default is the IP address of the destination VM instance.

  8. In the **Destination port** field, enter a destination port for your specified destination.

  9. Click **Create**.

  10. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-app-engine-version=APP_ENGINE_VERSION \
        --destination-instance=DESTINATION_INSTANCE \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `APP_ENGINE_VERSION`: the URI for the source App Engine standard environment version—for example, `apps/myproject/services/service-name/versions/version-name`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
      POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "appEngineVersion": {
            "uri": "APP_ENGINE_VERSION",
            },
        },
        "destination": {
          "instance": "DESTINATION_INSTANCE",
          "ipAddress": "DESTINATION_IP_ADDRESS",
        },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source Cloud Run function.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `APP_ENGINE_VERSION`: the URI for the source App Engine standard environment version—for example, `apps/myproject/services/service-name/versions/version-name`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



#### Test connectivity from a version of an App Engine standard environment service to an IP address

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. Enter a name for the test.
  4. Select a protocol.
  5. In the **Source endpoint** menu, select an **App Engine**. 
     1. In the **App Engine service** menu, select the specific App Engine standard environment service from which you want to test connectivity. For example, select `helloworld-service`. 
        1. If the source endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**.
        2. Select a project where the endpoint exists.
     2. In the **App Engine version** menu, select a version of the App Engine standard environment service from which you want to test connectivity.
  6. For **Destination** , select **IP address** , and then enter an IP address.
  7. Enter a destination port.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-app-engine-version=APP_ENGINE_VERSION \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `APP_ENGINE_VERSION`: the URI for the source App Engine standard environment version—for example, `apps/myproject/services/service-name/versions/version-name`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
      POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "appEngineVersion": {
            "uri": "APP_ENGINE_VERSION",
            },
        },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
        },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source Cloud Run function.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `APP_ENGINE_VERSION`: the URI for the source App Engine standard environment version—for example, `apps/myproject/services/service-name/versions/version-name`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



#### Test connectivity from a version of an App Engine standard environment service to Google-managed service

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. Enter a name for the test.
  4. Select a protocol.
  5. In the **Source endpoint** menu, select an **App Engine**. 
     1. In the **App Engine service** menu, select the specific App Engine standard environment service from which you want to test connectivity. For example, select `helloworld-service`. 
        1. If the source endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**.
        2. Select a project where the endpoint exists.
     2. In the **App Engine version** menu, select a version of the App Engine standard environment service from which you want to test connectivity.
  6. For **Destination** , do the following: 
     1. In the **Destination endpoint** menu, select a type of Google-managed service resource such as **GKE cluster control plane**.
     2. In the **Destination GKE cluster control plane** menu, select the cluster for which you want to test connectivity to the GKE control plane.
     3. Optional: Select the **Destination GKE cluster control plane endpoint** from the list. The default is the IP-based endpoint of the GKE cluster.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-app-engine-version=APP_ENGINE_VERSION \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
          DESTINATION_RESOURCE_FLAG=DESTINATION_ENDPOINT \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `APP_ENGINE_VERSION`: the URI for the source App Engine standard environment version—for example, `apps/myproject/services/servicename/versions/version-number`.
  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.
  * `DESTINATION_RESOURCE_FLAG`: the flag that specifies the type of Google-managed service resource.

For available options, see the following:

    * `--destination-gke-master-cluster`
    * `--destination-cloud-sql-instance`

For more information, see the [`gcloud network-management connectivity-tests create` reference](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the flag `--destination-gke-master-cluster`.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.

  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.




###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
      POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "appEngineVersion": {
            "uri": "APP_ENGINE_VERSION",
            },
        },
        "destination": {
          "DESTINATION_RESOURCE_FIELD": "DESTINATION_ENDPOINT",
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": DESTINATION_PORT,
        },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source Cloud Run function.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `APP_ENGINE_VERSION`: the URI for the source App Engine standard environment version—for example, `apps/myproject/services/servicename/versions/version-number`.
  * `DESTINATION_RESOURCE_FIELD`: the field that specifies the type of Google-managed service resource.

For available options, see the following:

    * `gkeMasterCluster`
    * `cloudSqlInstance`
    * `redisInstance`
    * `redisCluster`

For more information, see the [Endpoint reference](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the field `gkeMasterCluster`.

  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.

  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.




### Test from a Cloud Run function to a destination

This section describes how to test connectivity from a Cloud Run function that is deployed in a specific Google Cloud region to a VM instance, an IP address, or a Google-managed service. For example, you can follow the steps in this section to test connectivity from a Cloud Run function that is deployed in `us-central1` as the source to an endpoint in your VPC network as the destination.

To see a detailed configuration analysis, ensure that your Cloud Run function is active.

If you use a [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) for your Cloud Run function, keep in mind that egress settings for Cloud Run functions control the routing of outbound HTTP requests from a Cloud Run function and control the traffic types routed through the connector to your VPC network. For more information, see [Cloud Run functions egress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#egress_settings).

#### Test connectivity from a Cloud Run function to a VM instance

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **Cloud Function 1st gen**.
     2. In the **Cloud Function** menu, select the specific Cloud Run function from which you want to test connectivity. For example, select `function-1`.
     3. In the **Cloud Function** location menu, select the Google Cloud region where you have deployed the Cloud Run function. You can deploy Cloud Run functions to multiple regions that have different configurations but have the same name.
  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select **VM instance**.
     2. In the **Destination VM instance** menu, select a VM instance.
     3. In the **Destination network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface that uniquely identifies the destination location.

     4. Optional: Select the **Destination IP address** from the list. The default is the IP address of the destination VM instance.

  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-cloud-function=SOURCE_CLOUD_FUNCTION \
        --destination-instance=DESTINATION_INSTANCE \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_CLOUD_FUNCTION`: the URI of the Cloud Run function—for example, `projects/myproject/locations/us-central1/functions/function-1`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
    {
      "source": {
        "cloudFunction": {
          "uri": "SOURCE_CLOUD_FUNCTION",
          },
      },
      "destination": {
        "instance": "DESTINATION_INSTANCE",
        "ipAddress": "DESTINATION_IP_ADDRESS",
      },
      "protocol": "PROTOCOL",
    }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source Cloud Run function.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_CLOUD_FUNCTION`: the URI of the Cloud Run function—for example, `projects/myproject/locations/us-central1/functions/function-1`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



#### Test connectivity from a Cloud Run function to an IP address

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **Cloud Function 1st gen**.
     2. In the **Cloud Function** menu, select the specific Cloud Run function from which you want to test connectivity. For example, select `function-1`.
     3. In the **Cloud Function** location menu, select the Google Cloud region where you have deployed the Cloud Run function. You can deploy Cloud Run functions to multiple regions that have different configurations but have the same name.
  6. For **Destination** , select **IP address** , and then enter an IP address.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to the View test results section later on this page.



###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-cloud-function=SOURCE_CLOUD_FUNCTION \
        --destination-ip-address==DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_CLOUD_FUNCTION`: the URI of the Cloud Run function—for example, `projects/myproject/locations/us-central1/functions/function-1`.
  * `DESTINATION_IP_ADDRESS`: the destination IP address that you are testing to.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
    {
      "source": {
        "cloudFunction": {
          "uri": "SOURCE_CLOUD_FUNCTION",
        },
      },
      "destination": {
        "ipAddress": "DESTINATION_IP_ADDRESS",
      },
      "protocol": "PROTOCOL",
    }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source Cloud Run function.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_CLOUD_FUNCTION`: the URI of the Cloud Run function—for example, `projects/myproject/locations/us-central1/functions/function-1`.
  * `DESTINATION_IP_ADDRESS`: the destination IP address that you are testing to.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



#### Test connectivity from a Cloud Run function to a Google-managed service

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **Cloud Function 1st gen**.
     2. In the **Cloud Function** menu, select the specific Cloud Run function from which you want to test connectivity. For example, select `function-1`.
     3. In the **Cloud Function location** menu, select the Google Cloud region where you have deployed the Cloud Run function. You can deploy Cloud Run functions to multiple regions that have different configurations but have the same name.
  6. For **Destination** , do the following: 
     1. For **Destination endpoint** menu, select a type of Google-managed service resource such as **Cloud SQL instance**.
     2. In the **Destination Cloud SQL instance** menu, select the Cloud SQL instance from which you want to test connectivity.
     3. Optional: Select the **Destination Cloud SQL instance IP address** from the list. The default is the IP address of the source Cloud Run function.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to the View test results section later on this page.



###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-cloud-function=SOURCE_CLOUD_FUNCTION \
          DESTINATION_RESOURCE_FLAG=DESTINATION_ENDPOINT \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_CLOUD_FUNCTION`: the URI of the Cloud Run function—for example, `projects/myproject/locations/us-central1/functions/function-1`.
  * `DESTINATION_RESOURCE_FLAG`: the flag that specifies the type of Google-managed service resource.

For available options, see the following:

    * `--destination-gke-master-cluster`
    * `--destination-cloud-sql-instance`
    * `--destination-redis-instance`
    * `--destination-redis-cluster`

For more information, see the [`gcloud network-management connectivity-tests create` reference](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the flag `--destination-gke-master-cluster`.

  * `DESTINATION_IP_ADDRESS`: the internal or external destination IP address that you are testing to.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.

  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.




### Test from a Cloud Run revision to a destination

This section describes how to test connectivity from a Cloud Run revision to a VM instance, an IP address, or a Google-managed service.

You can deploy multiple [Cloud Run services](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#services) in a single project. Every Cloud Run service has an HTTPS endpoint on a unique subdomain of the `*.run.app` domain. Each deployment of the Cloud Run service creates a new immutable revision. You can test reachability from a revision to a VM instance, an IP address, or a Google-managed service.

To see a detailed configuration analysis, ensure that your revision is active. If your revision is configured to use [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc), ensure that it is receiving traffic. Keep in mind that [egress settings](https://docs.cloud.google.com/run/docs/configuring/networking-best-practices#egress_settings) for Direct VPC egress or [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) control the traffic types routed to your VPC network.

The Connectivity Test results might be different for each revision. For example, a Cloud Run service named `cloud_run_test` has a revision `first-revision` configured to use a Serverless VPC Access connector, a revision `second-revision` configured to use Direct VPC egress, and another revision `third-revision` without VPC access. Each of these revisions might return a different reachability status. For example, the first two revisions might be reachable while the third revision isn't.

When you create a Connectivity Test, you can select from a list of revisions for a Cloud Run service.

#### Test connectivity from a revision of a Cloud Run service to a VM instance

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. Enter a name for the test.
  4. Select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **Cloud Run service**.
     2. In the **Cloud Run service** menu, select the specific Cloud Run service from which you want to test connectivity. For example, select `helloworld-run`. 
        1. If the source endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**.
        2. Select a project where the endpoint exists.
     3. In the **Cloud Run revision** menu, select a Cloud Run revision that you are testing from.
  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select **VM instance**.
     2. In the **Destination VM instance** menu, select the specific destination VM instance.
     3. In the **Destination network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface to uniquely identify the destination location.

     4. Optional: Select the **Destination IP address** from the list. The default is the IP address of the destination VM instance.

  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-cloud-run-revision=CLOUD_RUN_REVISION \
        --destination-instance=DESTINATION_INSTANCE \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `CLOUD_RUN_REVISION`: the URI for the source Cloud Run revision—for example, `projects/myproject/locations/us-central1/revisions/cloudrun-revision`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
    {
      "source": {
        "cloudRunRevision": {
          "uri": "CLOUD_RUN_REVISION",
          },
      },
        "destination": {
          "instance": "DESTINATION_INSTANCE",
          "ipAddress": "DESTINATION_IP_ADDRESS"
          },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `CLOUD_RUN_REVISION`: the URI for the source Cloud Run revision—for example, `projects/myproject/locations/us-central1/revisions/cloudrun-revision`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-2`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address should be one of the IP addresses of the destination VM instance.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



#### Test connectivity from a revision of a Cloud Run service to an IP address

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. Enter a name for the test.
  4. Select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **Cloud Run service**.
     2. In the **Cloud Run service** menu, select the specific Cloud Run service from which you want to test connectivity. For example, select `helloworld-run`. 
        1. If the source endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**.
        2. Select a project where the endpoint exists.
     3. In the **Cloud Run revision** menu, select a Cloud Run revision that you are testing from.
  6. For **Destination** , select **IP address** , and then enter an IP address.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-cloud-run-revision=CLOUD_RUN_REVISION \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `CLOUD_RUN_REVISION`: the URI for the source Cloud Run revision—for example, `projects/myproject/locations/us-central1/revisions/cloudrun-revision`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
    {
      "source": {
        "cloudRunRevision": {
          "uri": "CLOUD_RUN_REVISION",
          },
      },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `CLOUD_RUN_REVISION`: the URI for the source Cloud Run revision—for example, `projects/myproject/locations/us-central1/revisions/cloudrun-revision`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.



#### Test connectivity from a revision of a Cloud Run service to a Google-managed service

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. Enter a name for the test.
  4. Select a protocol.
  5. For **Source** , do the following: 
     1. In the **Source endpoint** menu, select **Cloud Run service**.
     2. In the **Cloud Run service** menu, select the specific Cloud Run service from which you want to test connectivity. For example, select `helloworld-run`. 
        1. If the source endpoint is in a project other than the current project, select **Endpoint is in a project other than "` PROJECT_NAME`"**.
        2. Select a project where the endpoint exists.
     3. In the **Cloud Run revision** menu, select a Cloud Run revision that you are testing from.
  6. For **Destination** , do the following: 
     1. In the **Destination endpoint** menu, select a type of Google-managed service resource such as **GKE cluster control plane**.
     2. In the **Destination GKE cluster control plane** menu, select the cluster for which you want to test connectivity to the GKE control plane.
     3. Optional: Select the **Destination GKE cluster control plane endpoint** from the list. The default is the IP-based endpoint of the GKE cluster.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create). Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-cloud-run-revision=CLOUD_RUN_REVISION \
          DESTINATION_RESOURCE_FLAG=DESTINATION_ENDPOINT \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `CLOUD_RUN_REVISION`: the URI for the source Cloud Run revision—for example, `projects/myproject/locations/us-central1/revisions/cloudrun-revision`.
  * `PROJECT_NAME`: the project name where the endpoint is located—for example, `myproject`.
  * `DESTINATION_RESOURCE_FLAG`: the flag that specifies the type of Google-managed service resource.

For available options, see the following:

    * `--destination-gke-master-cluster`
    * `--destination-cloud-sql-instance`
    * `--destination-redis-instance`
    * `--destination-redis-cluster`

For more information, see the [`gcloud network-management connectivity-tests create` reference](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the flag `--destination-gke-master-cluster`.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.

  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.




###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
    {
      "source": {
        "cloudRunRevision": {
          "uri": "CLOUD_RUN_REVISION",
          },
      },
        "destination": {
          "DESTINATION_RESOURCE_FIELD": "DESTINATION_ENDPOINT",
          "port": DESTINATION_PORT,
        },
        "protocol": "PROTOCOL",
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `CLOUD_RUN_REVISION`: the URI for the source Cloud Run revision—for example, `projects/myproject/locations/us-central1/revisions/cloudrun-revision`.
  * `DESTINATION_RESOURCE_FIELD`: the field that specifies the type of Google-managed service resource.

For available options, see the following:

    * `gkeMasterCluster`
    * `cloudSqlInstance`
    * `redisInstance`
    * `redisCluster`

For more information, see the [Endpoint reference](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint).

  * `DESTINATION_ENDPOINT`: the URI for the destination endpoint—for example, `projects/myproject/locations/us-central1/clusters/cluster-1` for the field `gkeMasterCluster`.

  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols. The default is port `80`.

  * `PROTOCOL`: the networking protocols supported by Serverless VPC Access connectors—`TCP` or `UDP`.




### Test from a Cloud Run job to a destination

Follow these steps to test connectivity from a Cloud Run job to a VM instance.

Connectivity Tests also supports testing from a Cloud Run job to any other [supported endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#supported-configs). To test connectivity to another destination type, select or specify that endpoint as the destination.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.

  3. Enter a name for the test.

  4. In the **Protocol** list, select a protocol.

  5. For **Source** , do the following:

     1. For **Source endpoint** , select **Cloud Run job**.
     2. For **Source endpoint project** , select the project of the job.
     3. For **Cloud Run job** , select the specific job that you want to test.
  6. For **Destination** , do the following:

     1. For **Destination endpoint** , select **VM instance**.
     2. For **Destination VM instance project** , select the project of the VM instance.
     3. For **Destination VM instance** , select the VM instance.
     4. For **Destination network interface** , select the network interface.
     5. Optional: For **Destination IP address** , select an IP address.
     6. For **Destination port** , enter a destination port for your destination. This option is displayed only if TCP or UDP is selected for **Protocol**.
  7. Click **Create**.




After the test completes, Connectivity Tests displays your test results.

###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).
    
    
    gcloud network-management connectivity-tests create NAME \
        --protocol=PROTOCOL \
        --source-cloud-run-job=CLOUD_RUN_JOB \
        --destination-instance=DESTINATION_INSTANCE \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --round-trip
    

Replace the following:

  * `NAME`: a name for your test.
  * `PROTOCOL`: a supported protocol. The default protocol is `TCP`. For Serverless VPC Access connectors, only `TCP` and `UDP` are supported.
  * `CLOUD_RUN_JOB`: the URI for the source Cloud Run job—for example, `projects/my-project/locations/us-central1/jobs/my-cloud-run-job`.
  * `DESTINATION_INSTANCE`: the URI for the destination VM instance—for example, `projects/my-project/zones/us-central1-a/instances/my-instance`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address must be one of the IP addresses of the destination VM instance.
  * `DESTINATION_PORT`: a destination port; for example, `80`. Specify only if you are creating a TCP or UDP test.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID
    {
      "protocol": "PROTOCOL",
      "source": {
        "cloudRunJob": "CLOUD_RUN_JOB"
      },
      "destination": {
        "instance": "DESTINATION_INSTANCE",
        "ipAddress": "DESTINATION_IP_ADDRESS",
        "port": DESTINATION_PORT
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the test.
  * `TEST_ID`: a name for the test.
  * `PROTOCOL`: a supported protocol. The default protocol is `TCP`. For Serverless VPC Access connectors, only `TCP` and `UDP` are supported.
  * `CLOUD_RUN_JOB`: the URI for the source Cloud Run job—for example, `projects/my-project/locations/us-central1/jobs/my-cloud-run-job`.
  * `DESTINATION_INSTANCE`: the URI of the destination VM instance—for example, `projects/my-project/zones/us-central1-a/instances/my-instance`.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM instance that you are testing to. The IP address must be one of the IP addresses of the destination VM instance.
  * `DESTINATION_PORT`: a destination port; for example, `80`. Specify only if you are creating a TCP or UDP test.



### Test from a Database Migration Service private connection to a Cloud SQL instance

You can test connectivity from a [Database Migration Service private connection](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections) to a destination Cloud SQL instance.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page.

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.

  3. In the **Test name** field, enter a name for the test.

  4. In the **Protocol** field, select a protocol.

  5. In the **Source** section, do the following:

     1. For **Source endpoint** , select **Database Migration Service private connection**.
     2. For **Source endpoint project** , select the Google Cloud project of the private connection.
     3. For **Database Migration Service private connection** , select the private connection that you want to test from.
  6. In the **Destination** section, do the following:

     1. For **Destination endpoint** , select **Cloud SQL instance**.
     2. For **Destination endpoint project** , select the Google Cloud project of the Cloud SQL instance.
     3. For **Destination Cloud SQL instance** , select the specific Cloud SQL instance.
     4. For **Destination Cloud SQL instance endpoint** , select the destination IP address that you want to test.
     5. In the **Destination port** field, enter a destination port. This option is displayed only if TCP or UDP is selected for **Protocol**.
  7. Click **Create**.




After the test completes, Connectivity Tests displays your test results.

###  gcloud 

Use the [`gcloud network-management connectivity-tests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create).
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-dms-private-connection=SOURCE_PRIVATE_CONNECTION \
        --destination-cloud-sql-instance=DESTINATION_CLOUD_SQL_INSTANCE \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: a name for your test.
  * `SOURCE_PRIVATE_CONNECTION`: the URI for the source Database Migration Service private connection—for example, `projects/my-project/locations/us-central1/privateConnections/my-private-connection`.
  * `DESTINATION_CLOUD_SQL_INSTANCE`: the URI for the destination Cloud SQL instance—for example, `projects/my-project/instances/my-cloud-sql-instance`.
  * `DESTINATION_IP_ADDRESS`: the destination IP address that you want to test.
  * `DESTINATION_PORT`: a destination port; for example, `80`. Specify only if you are creating a TCP or UDP test.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
    POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID
    {
      "source": {
        "dmsPrivateConnection": "SOURCE_PRIVATE_CONNECTION"
      },
      "destination": {
        "ipAddress": "DESTINATION_IP_ADDRESS",
        "port": DESTINATION_PORT,
        "cloudSqlInstance": "DESTINATION_CLOUD_SQL_INSTANCE"
      },
      "protocol": "PROTOCOL"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the test.
  * `TEST_ID`: a name for the test.
  * `SOURCE_PRIVATE_CONNECTION`: the URI for the source Database Migration Service private connection—for example, `projects/my-project/locations/us-central1/privateConnections/my-private-connection`.
  * `DESTINATION_CLOUD_SQL_INSTANCE`: the URI for the destination Cloud SQL instance—for example, `projects/my-project/instances/my-cloud-sql-instance`.
  * `DESTINATION_IP_ADDRESS`: the destination IP address that you want to test.
  * `DESTINATION_PORT`: a destination port; for example, `80`. Specify only if you are creating a TCP or UDP test.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



### Test from a VPC network to a non-Google Cloud network

To test from a VPC network to a non-Google Cloud network, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , select **IP address** , enter an IP address, and then select the IP address type.
  6. For **Destination** , select **IP address** , and then enter an external IP address.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Enter the following command to test between an internal and external IP addresses. Replace variables for the command options with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --source-network=SOURCE_NETWORK \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

This example tests the ability to ping from the source IP address to the destination IP address.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
      POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "network": "SOURCE_NETWORK"
        },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
        },
          "protocol": "PROTOCOL".
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between two IP addresses. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "projectId": "SOURCE_IP_PROJECT_ID"
      },
      "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
      },
      "protocol": "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_IP_PROJECT_ID`: the project ID for the source IP address.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



The following example creates a test between two IP addresses:
    
    
    test_input = {
        "source": {
            "ipAddress": "SOURCE_IP_ADDRESS",
            "networkType": "GCP_NETWORK"
        },
        "destination": {
            "ipAddress": "DESTINATION_IP_ADDRESS",
            "port": "DESTINATION_PORT",
        },
        "protocol": "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
      parent="projects/PROJECT_ID/locations/global",
      testId="TEST_ID",
      body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination
  * `DESTINATION_PORT`: the destination TCP or UDP port number. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



### Test from a VPC spoke to another VPC spoke connected to the same NCC hub

To test from a VPC spoke in a NCC hub to another VPC spoke connected to the same hub, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , select **IP address** , and then enter the IP address from the source spoke VPC network.
  6. For **Destination** , select **IP address** , and then enter the IP address in another spoke VPC network that you are testing to.
  7. In the **Destination port** field, enter a destination port for your specified destination.
  8. Click **Create**.
  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.



###  gcloud 

Enter the following command to test between two spokes. Replace variables for the command options with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --source-network=SOURCE_NETWORK \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the destination IP address in another spoke VPC network that you are testing to.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

This example tests the ability to ping from the source IP address to the destination IP address.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
      POST https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
      {
        "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "network": "SOURCE_NETWORK"
        },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
        },
          "protocol": "PROTOCOL".
      }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_NETWORK`: the URI for the VPC network where the source IP address is located—for example, `projects/myproject/global/networks/default`.
  * `DESTINATION_IP_ADDRESS`: the destination IP address in another spoke VPC network that you are testing to.
  * `DESTINATION_PORT`: the destination TCP or UDP port number. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between two IP addresses. For more information, see the [`create` method](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "ipAddress": "SOURCE_IP_ADDRESS",
          "projectId": "SOURCE_IP_PROJECT_ID"
      },
      "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
      },
      "protocol": "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `SOURCE_IP_PROJECT_ID`: the project ID for the source IP address
  * `DESTINATION_IP_ADDRESS`: the destination IP address in another spoke VPC network that you are testing to.
  * `DESTINATION_PORT`: the destination TCP or UDP port number. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



The following example creates a test between two IP addresses:
    
    
    test_input = {
        "source": {
            "ipAddress": "SOURCE_IP_ADDRESS",
            "networkType": "GCP_NETWORK"
        },
        "destination": {
            "ipAddress": "DESTINATION_IP_ADDRESS",
            "port": "DESTINATION_PORT",
        },
        "protocol": "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
      parent="projects/PROJECT_ID/locations/global",
      testId="TEST_ID",
      body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_IP_ADDRESS`: the source IP address that you are testing from.
  * `DESTINATION_IP_ADDRESS`: the IP address of the destination VM.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



### Test from a VM to a non-Google Cloud network

This test analyzes connectivity from the source VM to a [Google network edge location](https://docs.cloud.google.com/vpc/docs/edge-locations).

**Note:** If your destination is a Google-owned IP address or an IP address used in Google Cloud, the live data plane analysis results are not displayed because the packet does not leave the Google network. For example, if your destination is a Google-owned IP address such as `8.8.8.8`, the live data plane analysis results are not displayed.

###  Console 

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Click **Create connectivity test**.
  3. In the **Test name** field, enter a name for the test.
  4. In the **Protocol** list, select a protocol.
  5. For **Source** , do the following:

     1. In the **Source endpoint** menu, select **VM instance**.
     2. In the **Source VM instance** menu, select the specific source VM instance.
     3. In the **Source network interface** menu, select the network interface.

If the VM instance has multiple network interfaces, select a VM network interface that uniquely identifies the source location.

     4. Optional: Select the **Source IP address** from the list. The default is the IP address of the source VM instance.

  6. For **Destination** , do the following:

     1. In the **Destination endpoint** menu, select **IP address**.
     2. Enter an external **Destination IP address**.
  7. In the **Destination port** field, enter a destination port for your specified destination.

  8. Click **Create**.

  9. After the test finishes, the main **Connectivity Tests** page loads and shows a list that contains this test and other tests. Continue to View test results.




###  gcloud 

To test between a VM and an external IP address, enter the following command. Replace the sample values with values from your VPC network.
    
    
    gcloud network-management connectivity-tests create NAME \
        --source-instance=SOURCE_INSTANCE \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --destination-ip-address=DESTINATION_IP_ADDRESS \
        --destination-port=DESTINATION_PORT \
        --protocol=PROTOCOL \
        --round-trip
    

Replace the following:

  * `NAME`: the name of the Connectivity Test.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from; the IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  API 

The following sample test determines if the existing network configuration allows VM `instance1`to ping the destination IP address.

Use the [`projects.locations.global.connectivityTests.create` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create).
    
    
     POST https: //networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/connectivityTests?testId=TEST_ID'
       {
         "source": {
           "instance": "SOURCE_INSTANCE",
           "ipAddress": "SOURCE_IP_ADDRESS",
         },
        "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
         },
         "protocol": "PROTOCOL",
       }'
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.
  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.



###  Python 

The following example code creates a test between a VM instance and an external IP address. For more information, see [`create`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#create) in the Google API Client Library for Python.
    
    
    test_input = {
      "source": {
          "instance":
              "SOURCE_INSTANCE",
          "ipAddress":
              "SOURCE_IP_ADDRESS",
          "projectId":
              "SOURCE_INSTANCE_PROJECT_ID"
      },
      "destination": {
          "ipAddress": "DESTINATION_IP_ADDRESS",
          "port": "DESTINATION_PORT",
      },
      "protocol":
          "PROTOCOL",
    }
    
    request = api.projects().locations().global_().connectivityTests().create(
        parent="projects/PROJECT_ID/locations/global",
        testId="TEST_ID",
        body=test_input)
    
    print(json.dumps(request.execute(), indent=4))
    

Replace the following:

  * `SOURCE_INSTANCE`: the URI for the source VM—for example, `projects/myproject/zones/us-east1-b/instances/instance-1`.
  * `SOURCE_IP_ADDRESS`: the IP address of the source VM instance that you are testing from. The IP address should be one of the IP addresses of the source VM instance.
  * `SOURCE_INSTANCE_PROJECT_ID`: the project ID of the source VM.
  * `DESTINATION_IP_ADDRESS`: the external destination IP address that you are testing to.
  * `DESTINATION_PORT`: the IP protocol port of the destination. This option is valid only for TCP or UDP protocols.
  * `PROTOCOL`: a [supported protocol](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#endpoints) for Connectivity Tests. The default protocol is `TCP`.
  * `PROJECT_ID`: the project ID of the project in which you are creating the test.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



### Test from a non-Google Cloud network to a VPC network

This procedure is the same as the Test between private IP addresses in a VPC network.

If you are using the Google Cloud CLI or Network Management API, set the source network type to `NON_GCP_NETWORK` and set the source network to the network of the Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or the router appliance instance.

### Test from a non-Google Cloud network to a non-Google Cloud network

This procedure is the same as the Test between private IP addresses in a VPC network.

If you are using the Google Cloud CLI or Network Management API, set the source network type to `NON_GCP_NETWORK` and set the source network to the network of the Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or the router appliance instance.

## View test results

This section describes how to view the results of a Connectivity Test.

### Console

You can view a test from several different pages.

#### From the main Connectivity Tests page

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. In the **Result details** column, choose a test, and then click **View**.
  3. The info panel for the test appears. You can view the overall result and the result cards for each Google Cloud resource in the testing path. You can click a link to the details page for some Google Cloud resources, such as VM instances or routes. If the test contains multiple traces, you can select a trace from the **Trace result** list.

If the test is [eligible](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#supported-dynamic-configs) for live data plane analysis, you can view packet loss and latency metrics.

  4. To expand or close a results card, click the arrow at the right of the card.

  5. To interpret test results, see [Configuration analysis states](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables).

  6. To close the info panel, at the top right of the page, click **Hide info panel**.




#### From the Connectivity Test details page

Alternatively, from the main Google Cloud console page, click the name of a test and view its results on the **Connectivity Test details** page.

#### From the Network interface details page

You can also view results from the **Network interface details** page for a network interface of a Compute Engine VM instance. This page only lists tests that use the current network interface as a source or destination.

To view results, you can select **View** in the **Result details** column or click the name of the test.

###  gcloud 

To view the results of a test, enter the following command. Use the test ID that you want to view.
    
    
    gcloud network-management connectivity-tests describe NAME
    

Replace `NAME` with the name of the Connectivity Test.

###  API 

Use the [`projects.locations.global.connectivityTests.get` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/get) to view the results of a test.
    
    
      GET https://networkmanagement.googleapis.com/v1/{name=projects/PROJECT_ID/locations/global/connectivityTests/TEST_ID}
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



###  Python 

The following example code prints the results of a test. For more information, see [`get`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#get) in the Google API Client Library for Python.
    
    
    project_id = "PROJECT_ID"
    test_id= "TEST_ID"
    request = api.projects().locations().global_().connectivityTests().get(
          name='projects/%s/locations/global/connectivityTests/%s' %
          (project_id, test_id))  
    
    print(json.dumps(request.execute(), indent=4))

Replace the following:

  * `PROJECT_ID`: the project ID of the project in which the test was created.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



## Rerun one or more tests

You might want to rerun a Connectivity Test if you make configuration changes to the Google Cloud resources in the testing path and want to see results for the latest network configuration. You can rerun one or more tests at the same time.

A Connectivity Test is based on a snapshot of the network configuration at the time of execution. Rerunning a test overwrites the previous test results. If you want to preserve older results, create a new test instead.

To check the status of the `rerun` test operation while it's running, see [Check a running test operation](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/long-running-ops).

### Console

#### From the main Connectivity Tests page

  1. In the Google Cloud console, go to the **Connectivity Tests** page. 

[Go to Connectivity Tests](https://console.cloud.google.com/net-intelligence/connectivity/tests/list)

  2. Select one or more tests from the available Connectivity Tests list.
  3. Click refresh **Rerun**.



#### From the Connectivity Tests details page

  1. From the preceding main **Connectivity Tests** page, click the name of a test.
  2. At the top of the **Connectivity Test details** page, click refresh **Rerun**.



#### From the Network interface details page

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If it is not already selected, select the project that contains the instance for which you want to rerun a test.
  3. Click the instance that you want to use to rerun a test.
  4. For **Network interfaces** , select the network interface that you want to use to rerun a test.
  5. For **Network analysis** , click **Connectivity Tests**.
  6. Select one or more tests from the available Connectivity Tests list.
  7. Click refresh **Rerun**.



###  gcloud 

To rerun a Connectivity Test, enter the following command. Use the test ID that you want to rerun.
    
    
    gcloud network-management connectivity-tests rerun NAME
    

Replace `NAME` with the name of the Connectivity Test.

###  API 

When the Network Management API creates a `connectivityTests` resource, it retains that test resource until you delete it. Because of this, you can rerun tests.

If you don't want to create persistent tests, you can use the API to create a test and delete it after viewing the test result.

Use the [`projects.locations.global.connectivityTests.rerun` method](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/rerun) to rerun a test.
    
    
      POST https://networkmanagement.googleapis.com/v1/{name=projects/*/locations/global/connectivityTests/*}:rerun
        {
          "name": {projects/PROJECT_ID/connectivityTests/{TEST_ID}}
        }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the source VM.
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running.



###  Python 

The following example code reruns a test. For more information, see [`rerun`](http://googleapis.github.io/google-api-python-client/docs/dyn/networkmanagement_v1.projects.locations.global_.connectivityTests.html#rerun) in the Google API Client Library for Python.
    
    
    project_id = "PROJECT_ID"
    test_id = "TEST_ID"
    request = api.projects().locations().global_().connectivityTests().rerun(name='projects/%s/locations/global/connectivityTests/%s' % (project_id, test_id))  
    
    print(json.dumps(request.execute(), indent=4))

Replace the following values:

  * `PROJECT_ID`: the project ID of the project in which the test was created
  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running



## What's next

  * [Configuration analysis states](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
