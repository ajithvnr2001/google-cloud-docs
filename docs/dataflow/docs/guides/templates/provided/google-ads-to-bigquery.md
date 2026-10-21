---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/google-ads-to-bigquery/
title: Google Ads to BigQuery template \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:06:11.799373+00:00
---

# Google Ads to BigQuery template  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/google-ads-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Google Ads to BigQuery template Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Google Ads to BigQuery template is a batch pipeline that reads Google Ads reports and writes to BigQuery.

## Pipeline requirements

  * The Google Ads account IDs to be used.
  * The Google Ads Query Language query to obtain the data.
  * OAuth credentials for the Google Ads API.



## Template parameters

### Required parameters

  * **customerIds** : A list of Google Ads account IDs to use to execute the query. For example, `12345,67890`.
  * **query** : The query to use to get the data. See Google Ads Query Language (<https://developers.google.com/google-ads/api/docs/query/overview>). For example, `SELECT campaign.id, campaign.name FROM campaign`.
  * **qpsPerWorker** : The rate of query requests per second (QPS) to submit to Google Ads. Divide the desired per pipeline QPS by the maximum number of workers. Avoid exceeding per-account or developer token limits. See Rate Limits (<https://developers.google.com/google-ads/api/docs/best-practices/rate-limits>).
  * **googleAdsClientId** : The OAuth 2.0 client ID that identifies the application. See Create a client ID and client secret (<https://developers.google.com/google-ads/api/docs/oauth/cloud-project#create_a_client_id_and_client_secret>).
  * **googleAdsClientSecret** : The OAuth 2.0 client secret that corresponds to the specified client ID. See Create a client ID and client secret (<https://developers.google.com/google-ads/api/docs/oauth/cloud-project#create_a_client_id_and_client_secret>).
  * **googleAdsRefreshToken** : The OAuth 2.0 refresh token to use to connect to the Google Ads API. See 2-Step Verification (<https://developers.google.com/google-ads/api/docs/oauth/2sv>).
  * **googleAdsDeveloperToken** : The Google Ads developer token to use to connect to the Google Ads API. See Obtain a developer token (<https://developers.google.com/google-ads/api/docs/get-started/dev-token>).
  * **outputTableSpec** : The BigQuery output table location to write the output to. For example, `<PROJECT_ID>:<DATASET_NAME>.<TABLE_NAME>`.Depending on the `createDisposition` specified, the output table might be created automatically using the user provided Avro schema.



### Optional parameters

  * **loginCustomerId** : A Google Ads manager account ID to use to access the account IDs. For example, `12345`.
  * **bigQueryTableSchemaPath** : The Cloud Storage path to the BigQuery schema JSON file. If this value is not set, then the schema is inferred from the Proto schema. For example, `gs://MyBucket/bq_schema.json`.
  * **writeDisposition** : The BigQuery WriteDisposition (<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload>) value. For example, `WRITE_APPEND`, `WRITE_EMPTY`, or `WRITE_TRUNCATE`. Defaults to `WRITE_APPEND`.
  * **createDisposition** : The BigQuery CreateDisposition (<https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#jobconfigurationload>). For example, `CREATE_IF_NEEDED` and `CREATE_NEVER`. Defaults to `CREATE_IF_NEEDED`.



## Run the template

### Console

  1. Go to the Dataflow **Create job from template** page.
[Go to Create job from template](https://console.cloud.google.com/dataflow/createjob)
  2. In the **Job name** field, enter a unique job name. 
  3. Optional: For **Regional endpoint** , select a value from the drop-down menu. The default region is `us-central1`. 

For a list of regions where you can run a Dataflow job, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). 

  4. From the **Dataflow template** drop-down menu, select the **Google Ads to BigQuery** template.
  5. In the provided parameter fields, enter your parameter values.
  6. Click **Run job**.



### gcloud

**Note:** To use the Google Cloud CLI to run flex templates, you must have [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install) version 284.0.0 or later. 

In your shell or terminal, run the template:
    
    
    gcloud dataflow flex-template run JOB_NAME \
        --template-file-gcs-location=gs://dataflow-templates/VERSION/flex/Google_Ads_to_BigQuery \
        --project=PROJECT_ID \
        --region=REGION_NAME \
        --parameters \
           customerIds=CUSTOMER_IDS,\
           query=QUERY,\
           qpsPerWorker=QPS_PER_WORKER,\
           googleAdsClientId=GOOGLE_ADS_CLIENT_ID,\
           googleAdsClientSecret=GOOGLE_ADS_CLIENT_SECRET,\
           googleAdsRefreshToken=GOOGLE_ADS_REFRESH_TOKEN,\
           googleAdsDeveloperToken=GOOGLE_ADS_DEVELOPER_TOKEN,\
           outputTableSpec=OUTPUT_TABLE_SPEC,\

Replace the following:

  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `REGION_NAME`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `CUSTOMER_IDS`: the Google Ads account IDs
  * `QUERY`: the Google Ads Query Language query
  * `QPS_PER_WORKER`: the required Google Ads request rate per worker
  * `GOOGLE_ADS_CLIENT_ID`: the OAuth 2.0 client ID that identifies the application
  * `GOOGLE_ADS_CLIENT_SECRET`: the OAuth 2.0 client secret that corresponds with the specified client ID
  * `GOOGLE_ADS_REFRESH_TOKEN`: the OAuth 2.0 refresh token to use to connect to the Google Ads API
  * `GOOGLE_ADS_DEVELOPER_TOKEN`: the Google Ads developer token to use to connect to the Google Ads API
  * `OUTPUT_TABLE_SPEC`: the BigQuery output table



### API

To run the template using the REST API, send an HTTP POST request. For more information on the API and its authorization scopes, see [`projects.templates.launch`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.templates/launch).
    
    
    POST https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/LOCATION/flexTemplates:launch
    {
       "launchParameter": {
         "jobName": "JOB_NAME",
         "parameters": {
           "customerIds": "CUSTOMER_IDS",
           "query": "QUERY",
           "qpsPerWorker": "QPS_PER_WORKER",
           "googleAdsClientId": "GOOGLE_ADS_CLIENT_ID",
           "googleAdsClientSecret": "GOOGLE_ADS_CLIENT_SECRET",
           "googleAdsRefreshToken": "GOOGLE_ADS_REFRESH_TOKEN",
           "googleAdsDeveloperToken": "GOOGLE_ADS_DEVELOPER_TOKEN",
           "outputTableSpec": "OUTPUT_TABLE_SPEC",
         },
         "containerSpecGcsPath": "gs://dataflow-templates/VERSION/flex/Google_Ads_to_BigQuery",
         "environment": { "maxWorkers": "10" }
      }
    }

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID where you want to run the Dataflow job 
  * `JOB_NAME`: a unique job name of your choice 
  * `VERSION`: the version of the template that you want to use 

You can use the following values:

    * `latest` to use the latest version of the template, which is available in the **non-dated** parent folder in the bucket— [gs://dataflow-templates/latest/](https://console.cloud.google.com/storage/browser/dataflow-templates/latest)
    * the version name, like `2023-09-12-00_RC00`, to use a specific version of the template, which can be found nested in the respective dated parent folder in the bucket— [gs://dataflow-templates/](https://console.cloud.google.com/storage/browser/dataflow-templates)
**Caution:** The **latest** version of templates might update with breaking changes. Your production environments should use templates kept in the most recent **dated** parent folder to prevent these breaking changes from affecting your production workflows. 
  * `LOCATION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy your Dataflow job—for example, `us-central1`
  * `CUSTOMER_IDS`: the Google Ads account IDs
  * `QUERY`: the Google Ads Query Language query
  * `QPS_PER_WORKER`: the required Google Ads request rate per worker
  * `GOOGLE_ADS_CLIENT_ID`: the OAuth 2.0 client ID that identifies the application
  * `GOOGLE_ADS_CLIENT_SECRET`: the OAuth 2.0 client secret that corresponds with the specified client ID
  * `GOOGLE_ADS_REFRESH_TOKEN`: the OAuth 2.0 refresh token to use to connect to the Google Ads API
  * `GOOGLE_ADS_DEVELOPER_TOKEN`: the Google Ads developer token to use to connect to the Google Ads API
  * `OUTPUT_TABLE_SPEC`: the BigQuery output table



## Template source code

### Java
    
    
    /*
     * Copyright (C) 2023 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License"); you may not
     * use this file except in compliance with the License. You may obtain a copy of
     * the License at
     *
     *   http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
     * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
     * License for the specific language governing permissions and limitations under
     * the License.
     */
    package com.google.cloud.teleport.v2.templates;
    
    import com.google.ads.googleads.v23.services.GoogleAdsRow;
    import com.google.cloud.teleport.metadata.Template;
    import com.google.cloud.teleport.metadata.TemplateCategory;
    import com.google.cloud.teleport.metadata.TemplateParameter;
    import com.google.cloud.teleport.v2.options.BigQueryCommonOptions.WriteOptions;
    import com.google.cloud.teleport.v2.transforms.BigQueryConverters;
    import com.google.cloud.teleport.v2.transforms.GoogleAdsRowToReportRowJsonFn;
    import com.google.cloud.teleport.v2.utils.GCSUtils;
    import com.google.cloud.teleport.v2.utils.GoogleAdsRateLimitPolicyFactory;
    import com.google.cloud.teleport.v2.utils.GoogleAdsUtils;
    import com.google.common.collect.ImmutableList;
    import java.util.List;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.PipelineResult;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.CreateDisposition;
    import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO.Write.WriteDisposition;
    import org.apache.beam.sdk.io.googleads.GoogleAdsIO;
    import org.apache.beam.sdk.io.googleads.GoogleAdsOptions;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.options.Validation;
    import org.apache.beam.sdk.transforms.Create;
    import org.apache.beam.sdk.transforms.ParDo;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.vendor.guava.v32_1_2_jre.com.google.common.base.Strings;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    
    /**
     * A template for writing <a href=
     * "https://developers.google.com/google-ads/api/docs/reporting/overview">Google Ads reports</a> to
     * BigQuery.
     *
     * <p>Nested fields are lifted to top-level fields by replacing the dots in field paths with
     * underscores.
     *
     * <p>Check out <a
     * href="https://github.com/GoogleCloudPlatform/DataflowTemplates/blob/main/v2/README_Google_Ads_to_BigQuery.md">README</a>
     * for instructions on how to use or modify this template.
     */
    @Template(
        name = "Google_Ads_to_BigQuery",
        category = TemplateCategory.BATCH,
        displayName = "Google Ads to BigQuery",
        description =
            "The Google Ads to BigQuery template is a batch pipeline that reads Google Ads reports and writes to BigQuery.",
        optionsClass = GoogleAdsToBigQuery.GoogleAdsToBigQueryOptions.class,
        flexContainerName = "google-ads-to-bigquery",
        contactInformation = "https://cloud.google.com/support",
        documentation =
            "https://cloud.google.com/dataflow/docs/guides/templates/provided/google-ads-to-bigquery",
        requirements = {
          "The Google Ads account IDs to use.",
          "The Google Ads Query Language query to obtain information.",
          "OAuth credentials for the Google Ads API."
        },
        preview = true)
    public final class GoogleAdsToBigQuery {
      public interface GoogleAdsToBigQueryOptions extends WriteOptions, GoogleAdsOptions {
        @TemplateParameter.Long(
            order = 1,
            optional = true,
            description = "Google Ads manager account ID",
            helpText = "A Google Ads manager account ID to use to access the account IDs.",
            example = "12345")
        Long getLoginCustomerId();
    
        void setLoginCustomerId(Long loginCustomerId);
    
        @TemplateParameter.Text(
            order = 2,
            regexes = {"^[0-9]+(,[0-9]+)*$"},
            description = "Google Ads account IDs",
            helpText = "A list of Google Ads account IDs to use to execute the query.",
            example = "12345,67890")
        @Validation.Required
        List<Long> getCustomerIds();
    
        void setCustomerIds(List<Long> customerIds);
    
        @TemplateParameter.Text(
            order = 3,
            description = "Google Ads Query Language query",
            helpText =
                "The query to use to get the data. See Google Ads Query Language (https://developers.google.com/google-ads/api/docs/query/overview).",
            example = "SELECT campaign.id, campaign.name FROM campaign")
        @Validation.Required
        String getQuery();
    
        void setQuery(String query);
    
        @TemplateParameter.Double(
            order = 4,
            description = "Required Google Ads request rate per worker",
            helpText =
                "The rate of query requests per second (QPS) to submit to Google Ads.  "
                    + "Divide the desired per pipeline QPS by the maximum number of workers. "
                    + "Avoid exceeding per-account or developer token limits. "
                    + "See Rate Limits (https://developers.google.com/google-ads/api/docs/best-practices/rate-limits).")
        Double getQpsPerWorker();
    
        void setQpsPerWorker(Double qpsPerWorker);
    
        @TemplateParameter.GcsReadFile(
            order = 5,
            optional = true,
            description = "BigQuery Table Schema Path",
            helpText =
                "The Cloud Storage path to the BigQuery schema JSON file. "
                    + "If this value is not set, then the schema is inferred "
                    + "from the Proto schema.",
            example = "gs://MyBucket/bq_schema.json")
        String getBigQueryTableSchemaPath();
    
        void setBigQueryTableSchemaPath(String value);
    
        @TemplateParameter.Text(
            order = 6,
            description = "OAuth 2.0 Client ID identifying the application",
            helpText =
                "The OAuth 2.0 client ID that identifies the application. See Create a client ID and client secret (https://developers.google.com/google-ads/api/docs/oauth/cloud-project#create_a_client_id_and_client_secret).")
        String getGoogleAdsClientId();
    
        void setGoogleAdsClientId(String clientId);
    
        @TemplateParameter.Password(
            order = 7,
            groupName = "Source",
            description = "OAuth 2.0 Client Secret for the specified Client ID",
            helpText =
                "The OAuth 2.0 client secret that corresponds to the specified client ID. See Create a client ID and client secret (https://developers.google.com/google-ads/api/docs/oauth/cloud-project#create_a_client_id_and_client_secret).")
        String getGoogleAdsClientSecret();
    
        void setGoogleAdsClientSecret(String clientSecret);
    
        @TemplateParameter.Password(
            order = 8,
            description = "OAuth 2.0 Refresh Token for the user connecting to the Google Ads API",
            helpText =
                "The OAuth 2.0 refresh token to use to connect to the Google Ads API. See 2-Step Verification (https://developers.google.com/google-ads/api/docs/oauth/2sv).")
        String getGoogleAdsRefreshToken();
    
        void setGoogleAdsRefreshToken(String refreshToken);
    
        @TemplateParameter.Password(
            order = 9,
            description = "Google Ads developer token for the user connecting to the Google Ads API",
            helpText =
                "The Google Ads developer token to use to connect to the Google Ads API. See Obtain a developer token (https://developers.google.com/google-ads/api/docs/get-started/dev-token).")
        String getGoogleAdsDeveloperToken();
    
        void setGoogleAdsDeveloperToken(String developerToken);
      }
    
      private static final Logger LOG = LoggerFactory.getLogger(GoogleAdsToBigQuery.class);
    
      public static void main(String[] args) {
        run(
            PipelineOptionsFactory.fromArgs(args)
                .withValidation()
                .as(GoogleAdsToBigQueryOptions.class));
      }
    
      public static PipelineResult run(GoogleAdsToBigQueryOptions options) {
        Pipeline pipeline = Pipeline.create(options);
        double qps = options.getQpsPerWorker();
        String query = options.getQuery();
    
        PCollection<GoogleAdsRow> googleAdsRows =
            pipeline
                .apply(
                    Create.of(
                        options.getCustomerIds().stream()
                            .map(Object::toString)
                            .collect(ImmutableList.toImmutableList())))
                .apply(
                    GoogleAdsIO.current()
                        .read()
                        .withDeveloperToken(options.getGoogleAdsDeveloperToken())
                        .withLoginCustomerId(options.getLoginCustomerId())
                        .withQuery(options.getQuery())
                        .withRateLimitPolicy(new GoogleAdsRateLimitPolicyFactory(qps)));
    
        PCollection<String> reportRows =
            googleAdsRows.apply(ParDo.of(new GoogleAdsRowToReportRowJsonFn(query)));
    
        Write<String> write =
            BigQueryIO.<String>write()
                .withoutValidation()
                .withWriteDisposition(WriteDisposition.valueOf(options.getWriteDisposition()))
                .withCreateDisposition(CreateDisposition.valueOf(options.getCreateDisposition()))
                .withFormatFunction(BigQueryConverters::convertJsonToTableRow)
                .to(options.getOutputTableSpec());
    
        String schemaPath = options.getBigQueryTableSchemaPath();
    
        if (Strings.isNullOrEmpty(schemaPath)) {
          write = write.withSchema(GoogleAdsUtils.createBigQuerySchema(query));
        } else {
          write = write.withJsonSchema(GCSUtils.getGcsFileAsString(schemaPath));
        }
    
        reportRows.apply("WriteToBigQuery", write);
    
        return pipeline.run();
      }
    }
    

## What's next

  * Learn about [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
