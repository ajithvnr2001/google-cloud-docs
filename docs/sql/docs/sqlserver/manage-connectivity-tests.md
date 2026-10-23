---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-connectivity-tests/
title: Manage connectivity tests \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:41.840567+00:00
---

# Manage connectivity tests  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-connectivity-tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage connectivity tests Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/manage-connectivity-tests "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/manage-connectivity-tests "View this page for the PostgreSQL database engine") | SQL Server

[Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) is a diagnostics tool that lets you check connectivity between network endpoints. It analyzes your configuration and, in some cases, performs [live data plane analysis](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#live-data-plane) between the endpoints. An endpoint is a source or destination of network traffic, such as a Cloud SQL instance. 

Use the Connectivity Tests tool for any of the following purposes:

  * To verify connectivity between a Cloud SQL instance and another resource, such as a Virtual Machine (VM), or between a [read replica](https://docs.cloud.google.com/sql/docs/sqlserver/replication#read-replicas) instance and a primary instance.
  * To troubleshoot any connectivity issues associated with different types of source and destination settings.
  * To determine whether there's an issue in your VPC network that's used for the Cloud SQL-related resources.



Configuration errors that the tool can diagnose include connectivity to a Cloud SQL instance blocked by:

  * VPC firewall rules, hierarchical firewall policies, and global network firewall policies
  * A routing issue (for example, an incorrect route to a destination network is used or no dynamic routes are available)
  * An issue associated with VPC peering between your VPC network and the Google-managed service network
  * The instance not running
  * An incorrect port or protocol being used by the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy#how-works) to access the instance 
  * A failure occurring with [authorized networks](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks) set up for the instance



For more information about the Connectivity Tests tool, see [Connectivity Tests overview](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview). 

**Note:** The procedures on this page explain how to use the Google Cloud console to manage connectivity tests. You can also manage these tests by using [](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the [Cloud SQL Admin API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/enable-api). You must enable this API so that you can run connectivity tests.
  7. Make sure you assign the [Network Management Admin](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control#networkmanagement-roles) role and associated permissions to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)




## Create a connectivity test

To create a connectivity test, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the Cloud SQL instance for which you want to create a connectivity test.

If no instances appear on the page, [create an instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

  3. From the side navigation menu, click **Connections**.
  4. Click the **Connectivity tests** tab, and then click **Create**.
  5. In the **Test name** field, enter a name for the test.

The test name can contain lowercase letters, numbers, and hyphens only.

  6. From the **Protocol** list, select a protocol for the test.
  7. If this Cloud SQL instance is the source for the test, do the following: 
     1. In the **Source** region, click the **Current Cloud SQL instance** option.
     2. In the **Destination** region, click **Other** , and then specify information about the endpoint for the destination.
  8. If the instance is the destination for the test, do the following: 
     1. In the **Source** region, click **Other** , and then specify information about the source's endpoint.
     2. In the **Destination** region, click the **Current Cloud SQL instance** option.
  9. In the **Destination port** field, enter a port for the destination.
  10. Click **Create**.



After the test finishes, the **Connectivity tests** tab loads and displays a list of configured tests.

## View information about a connectivity test

High-level information about a connectivity test that you can view includes the following information:

  * Name, protocol, source, and destination for the test.
  * Google Cloud projects associated with the source and destination.
  * Port reserved for the destination.
  * Last date and time that the test was run.
  * Result of the data plane analysis check that signifies how many packets of data were transmitted from the source to the destination.
  * Result of the configuration analysis check that signifies whether a connection can be established between the source and destination so that packets of data can be transferred to the destination.
  * Details about the test.



In addition to viewing high-level information about a connectivity test, you can click a test to see additional information about the results of the test, including the following information:

  * One-way latency values associated with the [live data plane analysis](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#live-data-plane) check.
  * Detailed information about the configuration analysis check. This information includes the status of the check, Cloud SQL instance, and so on.
  * REST API response for the connectivity test being run.



### View high-level and detailed information

To view high-level and detailed information a connectivity test, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the Cloud SQL instance for which you want to view information about a connectivity test.

  3. From the side navigation menu, click **Connections**.
  4. Click the **Connectivity tests** tab. High-level information about all tests associated with the instance appears.
  5. Click a test about which you want to view detailed information.

The **Connectivity test details** page appears. On this page, you can view the overall result and result cards for each Google Cloud resource in the testing path. You can click a link to the details page for some Google Cloud resources, such as VM instances or routes. If the test contains multiple traces, you can select a trace from the Trace result list.

If the test is [eligible](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#supported-dynamic-configs) for data plane analysis, you can view the packet loss and latency metrics.

To interpret the test results, see [Configuration analysis states](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/state-tables).

  6. To view detailed information about the configuration analysis check, in the **Last configuration analysis result** section, click **View**.
  7. To view the REST API response for the test, scroll to the bottom of the page, and then click **Equivalent REST**.



## Modify a connectivity test

To modify a connectivity test, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the Cloud SQL instance for which you want to modify a connectivity test.
  3. From the side navigation menu, click **Connections**.
  4. Click the **Connectivity tests** tab.
  5. Click the test that you want to modify.
  6. On the **Connectivity test details** page, click **Edit**.
  7. Modify the test. You can modify the protocol, source and destination endpoints, and destination port.
  8. Click **Save**.



## Test connectivity

You can test connectivity to a Cloud SQL instance with [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) enabled. To test inbound connectivity to the instance, set the IP address of the Private Service Connect endpoint that's used to connect to the instance to be the destination IP address.

### gcloud

Use the [`gcloud network-management connectivity-tests create`](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/connectivity-tests/create) command to create a connectivity test for a Cloud SQL instance with Private Service Connect enabled.
    
    
    gcloud network-management connectivity-tests create CONNECTIVITY_TEST_NAME \
    --source-instance=SOURCE_INSTANCE \
    --destination-cloud-sql-instance=DESTINATION_CLOUD_SQL_INSTANCE \
    --destination-network=DESTINATION_NETWORK \
    --destination-port=DESTINATION_PORT \
    --protocol=tcp \
    --round-trip

Make the following replacements:

  * CONNECTIVITY_TEST_NAME: the name of the connectivity test.
  * SOURCE_INSTANCE: the URI for the Compute Engine instance where the source IP address is located (for example, `projects/myproject/zones/myzone/instances/myinstance`).
  * DESTINATION_CLOUD_SQL_INSTANCE: the URL for the Cloud SQL instance (for example, `projects/myproject/instances/myinstance`).
  * DESTINATION_NETWORK: the URI for the VPC network where the destination IP address is located (for example, `projects/myproject/global/networks/mynetwork`).
  * DESTINATION_PORT: the port number reserved for the instance. For Cloud SQL for SQL Server instances, the port number is `1433`.



## Run connectivity tests again

If you change the network configuration of resources associated with a connectivity test and want to see the results for the latest configuration, you can run a test again. You can rerun one or more tests at the same time.

A connectivity test is based on a snapshot of the network configuration at the time that the test is run. Running a test again overwrites the previous test's results. If you want to keep older results, create a new test.

To run one or more connectivity tests again, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the Cloud SQL instance for which you want to run connectivity tests again.
  3. From the side navigation menu, click **Connections**.
  4. Click the **Connectivity tests** tab.
  5. Select the check box next to each test that you want to run again.
  6. Click **Rerun**.
  7. In the dialog box, click **Rerun**.



## Delete connectivity tests

If you no longer need a connectivity test, delete it. You can delete one or more tests at the same time.

To delete connectivity tests, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the Cloud SQL instance for which you want to delete connectivity tests.
  3. From the side navigation menu, click **Connections**.
  4. Click the **Connectivity tests** tab.
  5. Select the check box next to each test that you want to delete.
  6. Click **Delete**.
  7. In the dialog box, click **Delete**.

By deleting a connectivity test, it won't take up quota and you won't be billed for it in the future. 

## Troubleshoot

For more information about troubleshooting common issues with connectivity tests, see [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting).

## What's next

  * [Connectivity Tests overview](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)
  * [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)
  * [Network Analyzer overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
