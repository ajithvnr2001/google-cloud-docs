---
url: https://docs.cloud.google.com/cloud-assist/investigations/
title: Troubleshoot issues with Gemini Cloud Assist investigations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:20:37.670364+00:00
---

# Troubleshoot issues with Gemini Cloud Assist investigations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/investigations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Troubleshoot issues with Gemini Cloud Assist investigations Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** As of April 10, 2026, creating, running, and editing investigations are only available to users that have a [Premium Support contract](https://cloud.google.com/support/premium) or who have requested access through their account team. If you ran an investigation prior to April 10, 2026, the results of the investigation continue to be available to you in the Google Cloud console.   
  
Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

Gemini Cloud Assist investigations let you perform root-cause analysis (RCA) to diagnose, troubleshoot, and resolve issues across complex infrastructure and applications. This helps streamline incident response, reduce time to resolution, and improve overall service availability.

## Benefits of Gemini Cloud Assist investigations

  * **Troubleshoot issues in-context.**

Gemini Cloud Assist investigations are integrated into your current workflows.

  * **See what Gemini Cloud Assist sees.**

An investigation produces **Observations** , which are insights about your environment's state that are most relevant to the issue. Observations help you to quickly understand what is happening in your environment and are based on Gemini Cloud Assist's review of data sources such as logs, configurations, and metrics. Analysis across data sources might come from procedural runbooks, broad signal analysis, or tools. Observations are then ranked and filtered to help you focus on the information that is most relevant to your issue. Included in the observations are links to the source data that informs each observation, which lets you further investigate and fact check the observations.

  * **Diagnose issues.**

Investigations synthesizes the observations and uses domain-specific knowledge to identify probable root causes. Public and private knowledge is used to explain the context around the root cause, making it easier to understand. When there is uncertainty, multiple root causes can be provided as hypotheses. You can iterate on the investigation and create new revisions to drill deeper into certain areas.

  * **Resolve issues.**

Investigations recommends the next troubleshooting steps or fixes to help you resolve the issue. References to specific resources or time periods gives you relevant information that would have taken longer to gather on your own, enabling you to get to a resolution faster, with less effort.

  * **Get additional support.**

If you have a [support package](https://docs.cloud.google.com/support), the Google Cloud console lets you seamlessly transfer your investigation into a Google Cloud support case by using the **Request support** button that appears with the investigation details. The details of your investigation can then be reviewed by a support engineer so that they have the context from your troubleshooting, helping you resolve cases faster, with less back and forth.




## Supported Google Cloud products

_Supported products_ are those that investigations support troubleshooting for. Gemini Cloud Assist investigations support the following Google Cloud products:

  * [App Hub](https://docs.cloud.google.com/app-hub)
  * [Cloud SQL](https://docs.cloud.google.com/sql)
  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine)
  * [Cloud Networking](https://cloud.google.com/resources/networking)
  * [Cloud Run](https://docs.cloud.google.com/run)
  * [Managed Service for Apache Spark on Compute Engine](https://docs.cloud.google.com/dataproc/docs/support/troubleshoot-monitor#gemini_cloud_assist-preview)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/guides/monitor-troubleshoot-batches#gemini_cloud_assist-preview)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)
  * [BigQuery](https://docs.cloud.google.com/bigquery)
  * [Bigtable](https://docs.cloud.google.com/bigtable)
  * [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer)
  * [Dataflow](https://docs.cloud.google.com/dataflow)
  * [Spanner](https://docs.cloud.google.com/spanner)
  * [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis)
  * [Identity and Access Management](https://docs.cloud.google.com/iam)
  * [Cloud Quotas](https://docs.cloud.google.com/docs/quotas)



Not all resources within supported products are, themselves, supported. Some tools, such as the Google Cloud console, prevent you from adding an unsupported resource to an investigation or seeing an investigation button associated with an unsupported resource; however, other tools might run an investigation even if it includes unsupported, misspelled, or incorrectly formatted resources. A good practice when reviewing the results of your investigation is to confirm that any resources you specify in your initial investigation are mentioned in the output observations. If a resource isn't mentioned in the output but seems like it should be, it's likely that either the resource is unsupported or there is an issue with the naming of the resource.

### Entry points

You can initiate an investigation in the following places in the Google Cloud console:

  * The [Investigations page](https://console.cloud.google.com/troubleshooting/investigations/list)

Click **Create** to initiative an investigation.

  * The [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)

The **Investigate** button appears on logs for supported resources when the log has a severity level of "Warning" or higher. When initiating an investigation in the Logs Explorer, the log message, start time, and any relevant resources from the log are automatically pre-populate into the investigation creation panel. You can optionally edit or add information before running the investigation.

[Go to logs with severity of "Warning" or higher](https://console.cloud.google.com/logs/query;query=severity%3E%3DWARNING)

  * [Cloud Monitoring alerting](https://docs.cloud.google.com/monitoring/alerts)

The **Investigate** button appears for alerts that have a resource label. When initiating an investigation for an alert, a title, issue description, start time, and relevant resources for the alert are automatically pre-populated into the investigation creation panel. You can optionally edit or add information before running the investigation.

  * The [Gemini Cloud Assist chat panel](https://docs.cloud.google.com/cloud-assist/chat-panel)

The **Create investigation** button appears within a Gemini Cloud Assist chat when Gemini Cloud Assist determines that an investigation could be useful. When initiating an investigation from the chat, fields are automatically pre-populated into the investigation creation panel based on the content from your chat. You can optionally edit or add information before running the investigation.

Alternatively, you can manually begin an investigation within the chat panel by clicking the **More actions** drop-down button and selecting **New investigation**.

  * [Cloud Hub](https://console.cloud.google.com/cloud-hub/home)

The **Create investigation** button appears in the **Health & troubleshooting** page. You can view and initiate investigations scoped to either a project or application.

  * Within specific product pages.

You can initiate investigations from within supported product pages, such as workloads in Google Kubernetes Engine that have alerts, Managed Service for Apache Spark batches that fail, or [failed Airflow tasks](https://docs.cloud.google.com/composer/docs/latest/troubleshooting-dags#investigations) in Managed Service for Apache Airflow.




The [Google Cloud mobile app](https://cloud.google.com/app) is also available for initiating and viewing investigations; investigations are initiated by going to the **Observability** tab and selecting **Investigations**.

## Considerations

  * Each investigation uses an [OAuth 2.0 token](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) as part of its normal operation. The investigation creates a token from an existing grant and, if necessary, requests a new grant that has a scope of `API_CLOUD_PLATFORM`.

    * The access provided by the OAuth 2.0 token is limited to the access available to the user or service account that runs the investigation.

    * The OAuth 2.0 token is never used for mutating data.

  * A Gemini Cloud Assist investigation creates an investigation resource, which includes within it annotations and observations. This information can be stored in any Google Cloud data center. You shouldn't perform investigations on data subject to residency or jurisdictional regulatory compliances. For the support status of other security features, see [Certifications and security for Gemini](https://docs.cloud.google.com/gemini/docs/discover/certifications#security-features).

  * The account that creates an investigation is automatically granted the [Investigation Owner (`roles/geminicloudassist.investigationOwner`)](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationOwner) IAM role for that specific investigation.

  * Investigations are designed for targeted troubleshooting within Google Cloud environments. An investigation is limited to diagnosing issues within a single Google Cloud project or single [App Hub](https://docs.cloud.google.com/app-hub) application.

    * For a project-level investigation, the results of the investigation are stored within the project that created the investigation.

    * For an application-level investigation, the investigation is created within the [App Hub management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) of a folder configured for application management, and the results are stored within the management project. The investigation analyzes resources within the selected application, even if they're spread across different projects.

    * Gemini Cloud Assist doesn't support applications created in a [ host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).
  * Investigations are subject to the [general limitations of AI technology](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

  * Investigation runs are dynamic, which means re-running the same investigation can produce results with small differences. Some of the factors that contribute to differences between runs include the probabilistic nature of output from large-language models such as Gemini and the fact that the overall state of Google Cloud is not static.

  * Timestamps are a key piece of information in effective investigations. For the best results, verify that the time range reported in the investigation is reasonably accurate.




## Feedback

User feedback is an important mechanism for improving the quality and performance of investigations. You can provide feedback in the following ways:

  * [Configure prompt and response sharing](https://docs.cloud.google.com/cloud-assist/configure-prompt-response-sharing) for Gemini Cloud Assist in your project. By default, Google Cloud does not examine either the inputs or outputs associated with your investigations.

  * Provide feedback on investigations by clicking on the **Thumbs Up** or **Thumbs Down** icons in any investigation. This records whether you found that specific investigation to be helpful. This feedback mechanism only records the specific feedback that you provide; it does not record any inputs or generated outputs of the investigation.




## What's next

  * [Create an investigation](https://docs.cloud.google.com/cloud-assist/create-investigation).
  * [View and manage existing investigations](https://docs.cloud.google.com/cloud-assist/manage-investigations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
