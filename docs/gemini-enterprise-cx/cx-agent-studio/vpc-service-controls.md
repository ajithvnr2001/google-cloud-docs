---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/vpc-service-controls/
title: Configure VPC Service Controls for CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:23.256134+00:00
---

# Configure VPC Service Controls for CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Configure VPC Service Controls for CX Agent Studio Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) can help you mitigate the risk of data exfiltration from CX Agent Studio. Use VPC Service Controls to create a _service perimeter_ that protects the resources and data that you specify. For example, when you use VPC Service Controls to protect CX Agent Studio, the following artifacts cannot leave your service perimeter:

  * Agent application data
  * [runSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/runSession) requests and responses



CX Agent Studio allows interacting with other Google Cloud resources such as DLP redaction templates, BigQuery for conversation exporting, and Data Stores. These resources are in your control and must be available under the same VPC-SC perimeter as the agent application.

## Limitations

The following limitations apply:

  * Tools and callbacks are not able to send requests to arbitrary HTTP endpoints when VPC Service Controls is enabled, as this may risk exfiltrating data outside the VPC Service Controls perimeter. You have to configure Service Directory for private network access. 
  * Audio recordings cannot be written to Cloud Storage buckets outside the perimeter.
  * Conversations cannot be written to BigQuery datasets outside the perimeter.
  * Sensitive Data Protection redaction templates outside the perimeter cause failures in redacting conversation contents. 
  * OpenAPI tools cannot reference authentication keys using secrets that are outside the perimeter.
  * Datastore tools that specify a data store outside the perimeter fail to execute.
  * Flow-based agents that specify an agent resource outside the perimeter fail when called.
  * Attempting to import an agent application from a Cloud Storage bucket outside the perimeter fails.
  * Attempting to export an agent application to a Cloud Storage bucket outside the perimeter fails.



## Service perimeter creation

When you create a service perimeter, include both CX Agent Studio (`ces.googleapis.com`) and CX Insights (`contactcenterinsights.googleapis.com`) as protected services. Include any services that you want to restrict (for example, `storage.googleapis.com`, `bigquery.googleapis.com`) under the **Restricted services** pane.

For more information about creating a service perimeter, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) in the VPC Service Controls documentation.

VPC Service Controls documentation for optional dependencies:

  * [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/vpcsc-connectors)



## Using Service Directory for private network access

**Note:** If you are using load balancing within the perimeter, be sure to read the details about load balancing in [Private network access overview](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview).

CX Agent Studio integrates with [Service Directory private network access](https://docs.cloud.google.com/service-directory/docs/private-network-access-overview), so it can connect to OpenAPI tools targets inside your VPC network. This keeps the traffic within the Google Cloud network and enforces [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview) and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

To set up a tool targeting a private network:

  1. Follow [Service Directory private network configuration](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access) to configure your VPC network and Service Directory endpoint.

  2. The **Customer Engagement Suite Service Agent** [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) with the following address must exist for your agent project: 
         
         service-agent-project-number@gcp-sa-ces.iam.gserviceaccount.com

Grant the following roles to **Customer Engagement Suite Service Agent** service account in the project where your Service Directory is located:

     * `servicedirectory.viewer`
     * `servicedirectory.pscAuthorizedService`

Additionally, if your Service Directory is in a different project than your agent application, you also need to grant the `servicedirectory.viewer` role to the Customer Engagement Suite Service Agent account in the project that hosts your agent application.

  3. Provide Service Directory service along with the URL and optional authentication information when creating the tool. This field is available in the advanced settings for the tool.




To troubleshoot issues, you can set up a [private uptime check](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks) to check that your Service Directory is correctly configured.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
