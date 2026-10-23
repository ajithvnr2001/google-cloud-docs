---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-d-presence/
title: Computing \u03b4-presence for a dataset \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:23.741153+00:00
---

# Computing δ-presence for a dataset  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/compute-d-presence/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Computing δ-presence for a dataset Stay organized with collections  Save and categorize content based on your preferences. 

Delta-presence (_δ_ -presence) is a metric that quantifies the probability that an individual belongs to an analyzed dataset. Like _k_ -map, you can estimate _δ_ -presence values using Sensitive Data Protection, which uses a statistical model to estimate the attack dataset.

_δ_ -presence contrasts with the other risk analysis methods, in which the attack dataset is explicitly known. Depending on the type of data, Sensitive Data Protection uses publicly available datasets (for example, from the US Census) or a custom statistical model (for example, one or more BigQuery tables that you specify), or it extrapolates from the distribution of values in your input dataset.

This topic demonstrates how to compute _δ_ -presence values for a dataset using Sensitive Data Protection. For more information about _δ_ -presence or risk analysis in general, see the [risk analysis concept topic](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) before continuing on.

**Note:** At this time, you can only compute _δ_ -presence values using the DLP API or Sensitive Data Protection-supported [client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). Sensitive Data Protection in the Google Cloud console doesn't support computing _δ_ -presence values.

**Note:** Prematurely canceling an operation midway through a job still incurs costs for the portion of the job that was completed. For more information about billing, see [Sensitive Data Protection pricing](https://cloud.google.com/sensitive-data-protection/pricing).

##  Before you begin 

Before continuing, be sure you've done the following: 

  1. [Sign in](https://accounts.google.com/Login) to your Google Account.
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.
[Go to the project selector](https://console.cloud.google.com/projectselector2/home/dashboard)
  3. Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm billing is enabled for your project.](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  4. Enable Sensitive Data Protection.
[Enable Sensitive Data Protection](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  5. Select a BigQuery dataset to analyze. Sensitive Data Protection estimates the _δ_ -presence metric by scanning a BigQuery table.
  6. Determine the types of datasets you want to use to model the attack dataset. For more information, see the reference page for the [`DeltaPresenceEstimationConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#deltapresenceestimationconfig) object, as well as [Risk analysis terms and techniques](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#risk_analysis_terms_and_techniques).



## Compute _δ_ -presence metrics

To compute a _δ_ -presence estimate using Sensitive Data Protection, send a request to the following URL, where PROJECT_ID indicates your [project identifier](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects):
    
    
    https://dlp.googleapis.com/v2/projects/PROJECT_ID/dlpJobs

The request contains a [`RiskAnalysisJobConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.RiskAnalysisJobConfig) object, which is composed of the following:

  * A [`PrivacyMetric`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#privacymetric) object. This is where you specify that you want to calculate _δ_ -presence by specifying a [`DeltaPresenceEstimationConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#deltapresenceestimationconfig) object containing the following:

    * `quasiIds[]`: Required. Fields ([`QuasiId`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#quasiid) objects) considered to be quasi-identifiers to scan and use to compute _δ_ -presence. No two columns can have the same tag. These can be any of the following:

      * An [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType): This causes Sensitive Data Protection to use the relevant public dataset as a statistical model of population, including US ZIP codes, region codes, ages, and genders.
      * A custom infoType: A custom tag wherein you indicate an auxiliary table (an [`AuxiliaryTable`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.AuxiliaryTable) object) that contains statistical information about the possible values of this column.
      * The `inferred` tag: If no semantic tag is indicated, specify `inferred`. Sensitive Data Protection infers the statistical model from the distribution of values in the input data.
    * `regionCode`: An [ISO 3166-1 alpha-2 region code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) for Sensitive Data Protection to use in statistical modeling. This value is required if no column is tagged with a region-specific infoType (for example, a US ZIP code) or a region code.

    * `auxiliaryTables[]`: Auxiliary tables ([`StatisticalTable`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#statisticaltable) objects) to use in the analysis. Each custom tag used to tag a quasi-identifier column (from `quasiIds[]`) must appear in exactly one column of one auxiliary table.

  * A [`BigQueryTable`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable) object. Specify the BigQuery table to scan by including all of the following:

    * `projectId`: The project ID of the project containing the table.
    * `datasetId`: The dataset ID of the table.
    * `tableId`: The name of the table.
  * A set of one or more [`Action`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action) objects, which represent actions to run, in the order given, at the completion of the job. Each `Action` object can contain one of the following actions:

    * [`SaveFindings`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#SaveFindings) object: Saves the results of the risk analysis scan to a BigQuery table.
    * [`PublishToPubSub`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishToPubSub) object: [Publishes a notification to a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publisher).
**Note:** If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 
    * [`PublishSummaryToCscc`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#PublishSummaryToCscc) object: Saves a results summary to Security Command Center.
    * [`JobNotificationEmails`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#JobNotificationEmails) object: Sends you an email with results.
    * [`PublishToStackdriver`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#PublishToStackdriver) object: Saves results to Google Cloud Observability.



## Viewing _δ_ -presence job results

To retrieve the results of the _δ_ -presence risk analysis job using the REST API, send the following GET request to the [`projects.dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get) resource. Replace PROJECT_ID with your project ID and JOB_ID with the identifier of the job you want to obtain results for. The job ID was returned when you started the job, and can also be retrieved by listing all jobs.
    
    
    GET https://dlp.googleapis.com/v2/projects/PROJECT_ID/dlpJobs/JOB_ID

The request returns a JSON object containing an instance of the job. The results of the analysis are inside the `"riskDetails"` key, in an [`AnalyzeDataSourceRiskDetails`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob.AnalyzeDataSourceRiskDetails) object. For more information, see the API reference for the [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob) resource.

## What's next

  * Learn how to calculate the [_k_ -anonymity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity) value for a dataset.
  * Learn how to calculate the [_l_ -diversity](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity) value for a dataset.
  * Learn how to calculate the [_k_ -map](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-map) value for a dataset.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
