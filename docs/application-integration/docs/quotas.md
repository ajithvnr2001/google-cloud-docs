---
url: https://docs.cloud.google.com/application-integration/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:16.396431+00:00
---

# Quotas and limits  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document lists the quotas and system limits that apply to Application Integration.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Application Integration resources. System limits can't be changed. 

By default, Application Integration quotas and limits apply on a [per-project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) basis. Quotas and limits that apply on a different basis are indicated as such; for example, the default concurrent executions for each project, or the maximum numbers of integrations per project. 

##  Resource quotas 

The following quotas apply to Application Integration resources for each Google Cloud project. You can increase or decrease the quota by requesting for a quota change.

Resource | Quota | Value  
---|---|---  
Integration execution | Default concurrent executions per project | 50  
Number of integration execution requests per minute | 24000  
[Integration Connectors](https://docs.cloud.google.com/application-integration/docs/using-integration-connectors) | See [Integration Connectors limits](https://docs.cloud.google.com/integration-connectors/docs/quotas) |   
Integration [execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs) and [monitoring](https://docs.cloud.google.com/application-integration/docs/monitoring-overview) | Number of read executions requests per minute | 18000  
Integrations page  (This page lists all the available integrations in your project)  | Number of read integration requests per minute | 12000  
[Integration editor](https://docs.cloud.google.com/application-integration/docs/integration-designer-layout) page  (This page loads a whole integration including all the integration versions and configured task entities)  | Number of read task entity requests per minute | 12000  
Number of read integration version requests per minute | 12000  
Number of write integration version requests per minute | 12000  
[Authentication profiles](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles) page  (This page lists all the available authentication profiles in your project)  | Number of read requests per minute | 12000  
Number of write requests per minute | 12000  
[Salesforce trigger](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger) | Number of read Salesforce channel requests per minute | 12000  
Number of write Salesforce channel requests per minute | 12000  
Number of read Salesforce instance requests per minute | 12000  
Number of write Salesforce instance requests per minute | 12000  
  
###  Request a quota increase 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

##  Usage limits 

Application Integration enforces the following usage limits. Your are responsible for tracking and ensuring that the values stay within the prescribed limits. Exceeding the limits might lead to reduced throughput, task failures, and increased latencies when running the integration. Resource | Limit | Value  
---|---|---  
Applicable to the entire Application Integration | Maximum characters in the integration name | 64 characters  
Maximum cumulative size of all the integration data (including input and output variables) **Note:** Similar to integrations, each sub-integration also has a limit of 30 MB. However, when a private trigger is triggered from an integration, the size of both the integration and the private trigger is counted towards the limit, since they are in the same execution. | 30 MB **Caution:** If the data size exceeds **10 MB** , Application Integration runs the integration, but disables [local logging](https://docs.cloud.google.com/application-integration/docs/local-logging). As a result, you can't view the full execution logs, apply retry strategy, or monitor integrations in the [monitoring dashboard](https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard).  
Maximum cumulative size of all the integration data (including input and output variables) sent and received from connections | 8 MB  
Timeout for synchronous (SYNC) integration executions The timeout duration includes any external system calls or sub-integration tasks of the integration during its execution. After the timeout duration, the execution status is set to `CANCELED`. Examples of external system calls include, calling external endpoints, calling Salesforce using connectors, and calling Google Cloud functions | 2 minutes  
Timeout for asynchronous (ASYNC) integration executions If your sub-integration takes longer than 2 minutes to run, consider executing your integration in ASYNC mode | 10 minutes  
Maximum time till which an older version of the integration can run after publishing the new version (system consistency) This is because Application Integration is a distributed system that provides _eventual consistency_. It uses caches throughout the system that may take time to clear and refresh | 10 minutes  
Maximum numbers of integrations per project | 1000  
Maximum number of tasks in an integration If there is a need for more tasks, it is recommended that you split your integration into multiple integrations | 100  
Maximum versions allowed for an integration | 100  
Number of days an integration execution can last, including the pause during the approval task | 31 days  
[API trigger](https://docs.cloud.google.com/application-integration/docs/configure-apps-script-task) | Maximum characters for _TRIGGER_NAME_ in Trigger ID Trigger ID format: `api_trigger/TRIGGER_NAME` | 64 characters  
[Apps Script task](https://docs.cloud.google.com/application-integration/docs/configure-apps-script-task) | Maximum active deployments for an Apps Script | 50  
Queries per second (QPS) for API executables | 5000 per minute  
Queries per second (QPS) for Webapp deployments | 5000 per minute  
Latency for API executables | 1.5 seconds  
Latency for Webapp | 2.5 seconds  
Maximum cumulative size of all the integration variables in an Apps Script | 15 MB  
[Call REST Endpoint task](https://docs.cloud.google.com/application-integration/docs/configure-call-rest-endpoint-task) | Maximum number of concurrent REST calls | 100  
Maximum size of the request body sent to the REST endpoint | 20 MB  
Maximum size of the response received from the REST endpoint | 34 MB (34,000,000 bytes)  
[Call Integration task](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task) | Maximum number of sub-integrations that can run from the main integration | 10000  
[Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) | Timeout for Connector task execution | 3 minutes  
Maximum size of the response from the connector | 20 MB  
Execute Custom Query: Maximum timeout | 180 seconds  
Execute Custom Query: Maximum number of rows | 50,000  
[While Loop task](https://docs.cloud.google.com/application-integration/docs/configure-while-loop-task) and [For Each Loop task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-loop-task) | Maximum cumulative size of data processed | 20 MB  
Maximum number of iterations | 8000  
Maximum cumulative size of data collected from each sub-integration call | 50 MB  
[For Each Parallel task](https://docs.cloud.google.com/application-integration/docs/configure-for-each-parallel-task) | Maximum cumulative size of data processed | 20 MB  
Maximum number of iterations | 10000  
Maximum number of parallel executions To increase this limit, you must request an increase for the Default concurrent executions per project quota. | 50  
[Data Mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task) | Maximum size of an array data type variable | 100000 elements  
Maximum size of a JSON data type variable | 20 MB  
Maximum size of a string data type variable | 20 MB  
[Data Transformer task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) | Maximum memory available for script evaluation | 300 MB  
[JavaScript task](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task) | Maximum request size for the script | 25 MB  
[Send Email task](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task) | Maximum recipient count for the task | 30  
  
### Data processing limits

We don't recommend using integrations in the following scenarios:

  * Integration requires movement of bulk data or focus on extract, transform, and load (ETL) processes
  * Cumulative size of all the integration data is **greater than** `10 MB` during execution 

When calculating the cumulative data size, add the size of all types of data such as input variables, output variables, and other intermediate task variables 

**Caution:** If the data size exceeds 10 MB, Application Integration runs the integration, but disables [local logging](https://docs.cloud.google.com/application-integration/docs/local-logging). As a result, you can't view the full execution logs, apply retry strategy, or monitor integrations in the [monitoring dashboard](https://docs.cloud.google.com/application-integration/docs/monitoring-dashboard).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
