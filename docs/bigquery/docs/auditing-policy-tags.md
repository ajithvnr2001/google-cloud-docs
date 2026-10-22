---
url: https://docs.cloud.google.com/bigquery/docs/auditing-policy-tags/
title: Audit policy tags \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:45.872341+00:00
---

# Audit policy tags  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/auditing-policy-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Audit policy tags

This document describes how to use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to audit activities related to policy tags. For example, you can determine:

  * The email address for the principal that grants or removes access on a policy tag

  * The email address for whom the access was granted or removed

  * The policy tag whose access was changed




## Access to logs

For information about the permission you need to view logs, see the [Cloud Logging access control guide](https://docs.cloud.google.com/logging/docs/access-control).

## Viewing logs for policy tag events

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the resources drop-down list, click **Audited Resource** , click **Audited Resources** again, and then click **datacatalog.googleapis.com**. You will see recent audit log entries of Data Catalog resources.

  3. To view the log entries, select the Data Catalog `SetIamPolicy` method.

  4. Click the log entry to see details about the call to the `SetIamPolicy` method.

  5. Click the log entry fields to see details for the `SetIamPolicy` entry.

     * Click `protoPayload`, then click `authenticationInfo` to see the `principalEmail` for the entity that set the IAM policy.

     * Click `protoPayload`, click `request`, click `policy`, and then click `bindings` to see the bindings, including principals and roles, that were changed.




## What's next

Learn about [best practices for policy tags](https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
