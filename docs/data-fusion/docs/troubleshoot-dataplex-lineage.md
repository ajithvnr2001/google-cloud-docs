---
url: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-dataplex-lineage/
title: Troubleshoot Knowledge Catalog asset lineage integrations \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:39.229583+00:00
---

# Troubleshoot Knowledge Catalog asset lineage integrations  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/troubleshoot-dataplex-lineage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Troubleshoot Knowledge Catalog asset lineage integrations Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud Data Fusion Knowledge Catalog asset lineage integrations.

## Runtime errors

To find relevant logs for your data pipelines, go to your instance in the Cloud Data Fusion web interface and click **System Admin** > **Management** > **Metadata Service**.

### The Data Lineage API isn't enabled or role isn't granted

The following issue occurs when the Data Lineage API hasn't been enabled in the project or the Cloud Data Fusion service account hasn't been granted the Data Lineage Events Producer role: 
    
    
    Error calling the metadata consumer data-catalog-consumer:
    io.grpc.StatusRuntimeException: PERMISSION_DENIED: Data Lineage API has not been
    used in project <project_id> before or it is disabled. Enable it by visiting
    https://console.developers.google.com/apis/api/datalineage.googleapis.com/overview?project=<project_id>
    then retry. If you enabled this API recently, wait a few minutes for the action
    to propagate to our systems and retry.
    

To resolve this issue, enable the Data Lineage API and grant the Data Lineage Events Producer role to the Cloud Data Fusion Service Agent. For more information, see [View lineage in Knowledge Catalog](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex#before_you_begin).

### Pipeline runs in an unsupported Cloud Data Fusion version

The following issue occurs when the Cloud Data Fusion instance is upgraded to a version greater than 6.8.0, but the pipeline hasn't been upgraded:
    
    
    Error calling the metadata consumer data-catalog-consumer:
    java.lang.IllegalArgumentException: FQN for the asset is null.
    

To resolve this issue, [upgrade the pipeline](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading) to the latest version.

### No messages in logs and no lineage in Knowledge Catalog

The following issue occurs when one of the plugins used in the pipeline doesn't support lineage egress to Knowledge Catalog:

There aren't error or success messages in the logs and there's no lineage in Knowledge Catalog.

To resolve this issue, your pipeline must contain only the [plugins that support data lineage in Knowledge Catalog](https://docs.cloud.google.com/data-fusion/docs/how-to/view-lineage-in-dataplex#supported_plugins).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
