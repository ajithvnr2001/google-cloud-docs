---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/run-connectivity-tests/
title: Run Connectivity Tests \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:07.898044+00:00
---

# Run Connectivity Tests  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/run-connectivity-tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Run Connectivity Tests Stay organized with collections  Save and categorize content based on your preferences. 

You can run Connectivity Tests directly from Flow Analyzer to validate the connectivity between two endpoints. You can also run these tests to understand the path between two resources. When you run Connectivity Tests, note that the tests uses the existing configuration. So, if you run the tests two weeks after the actual log event, Connectivity Tests does not use the historical configuration.

While running a test, the following attributes are used in the test definition:

  * Source IP
  * Source Project
  * Source Network (for internal IP addresses)
  * Destination IP (for internal IP addresses)
  * Destination Project (for internal IP addresses)
  * Destination Network (for internal IP addresses)
  * Destination Port
  * Protocol



If these parameters are not available in the traffic information, the Connectivity Test fails. For example, if you group traffic in Flow Analyzer only by Source VPC and Destination VPC, this information is not sufficient to run Connectivity Tests.

**Note:** The existing resource configuration is used to perform the analysis.

Connectivity Tests can fail due to the following reasons:

  * If the resources shown in VPC Flow Logs no longer exist.
  * If the test is executed from server to client and traffic in that direction (other than return traffic) cannot be initiated.



## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Enable the Network Management API](https://docs.cloud.google.com/network-intelligence-center/docs/reference/enable-api).

  3. Make sure the user role has the following permissions: `compute.networks.list`

Because the tests are run through internal API, the results are ephemeral and users are not billed for running the tests. The results are not stored and are not accessible after closing the results panel.




## Run Connectivity Tests

To run Connectivity Tests from Flow Analyzer, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Flow Analyzer** page.

[Go to Flow Analyzer](https://console.cloud.google.com/net-intelligence/flow-analyzer)

  2. Select a log bucket. By default, flow logs are stored in the **_Default** log bucket and accessible in the **_Default** log view.

  3. Select the time range for which you want to run the query.

  4. In the **Traffic** menu, select one of the following options:

     * **Source - Destination:** Aggregate the traffic from the source to the destination.
     * **Client - Server:** Aggregate the traffic in both directions by considering the resources with lower port numbers and service definitions as servers.
  5. Optional: In the **Filter** lists, select one or more filters.

  6. Organize the query results by using the **Organize flows by** lists. The following fields are required:

     * Source IP address
     * Source VPC network or VPC network project ID
     * Destination IP address
  7. Click **Run new query**.

  8. In the **All data flows** table, click **Run** for any flow.




## What's next

  * [Analyze your traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows)
  * [Monitor your traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/monitor-traffic-flows)
  * [Troubleshoot data issues in Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/manage-flow-analyzer)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
