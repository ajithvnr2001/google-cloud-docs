---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/troubleshoot/
title: Troubleshoot queries \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:43.988712+00:00
---

# Troubleshoot queries  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Troubleshoot queries Stay organized with collections  Save and categorize content based on your preferences. 

Use the information in this document to help you to identify and resolve issues with queries that return no results or seem to be missing data.

## Verify requirements

Review the requirements to view topologies and the underlying data.

  * [Requirements for the Gemini Enterprise Agent Platform **Topology** page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/view-project-topology#requirements)
  * [Requirements for topologies in Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology/view-agent-registry-topology#requirements)



You can also review App Topology [limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology#limitations) for additional considerations.

## Query does not return data

If a query does not return data, try starting from a predefined query or broadening your query. Make one change at a time so that you can track which changes improve your query results.

  1. Try a suggested query. The predefined query suggestions are designed to return results that are relevant for most environments. If a suggested query works, try modifying it to better meet your needs.

  2. Test a broader query. For example, if the query filters a node with a `Where` clause, remove the `Where` clause and run the query again. If the broader query works, the original query might be too specific for the available data.

  3. Check the query logic. Avoid combining too many constraints that might unintentionally exclude all results. For example, if a test project has no active deployments, looking for `Critical` vulnerabilities in active deployments will produce no results.




## Data is missing or looks old

If some data seems to be missing or appears outdated, try the following steps:

  1. Wait a few minutes for data synchronization to occur. Recently created or updated resources might take a few minutes to appear in query results. For example, if a user just deployed a new workload or updated an IAM policy, there might be a delay before these changes are reflected in the query results.
  2. Some types of data are not supported or might have longer latency for data synchronization. See the list of [limitations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology#limitations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
