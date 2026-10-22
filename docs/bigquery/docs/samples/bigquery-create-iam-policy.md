---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-iam-policy/
title: Create IAM policy \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:10.960268+00:00
---

# Create IAM policy  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-create-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create IAM policy Stay organized with collections  Save and categorize content based on your preferences. 

Create an IAM policy for a table.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.[Role](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Role.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.cloud.bigquery.[TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html);
    
    // Sample to create iam policy for table
    public class CreateIamPolicy {
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) {
        // TODO(developer): Replace these variables before running the sample.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) datasetName = "MY_DATASET_NAME";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tableName = "MY_TABLE_NAME";
        createIamPolicy(datasetName, tableName);
      }
    
      public static void createIamPolicy([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) datasetName, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) tableName) {
        try {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigquery = [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).getDefaultInstance().getService();
    
          [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html) tableId = [TableId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.TableId.html).of(datasetName, tableName);
    
          [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) policy = bigquery.[getIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_getIamPolicy_com_google_cloud_bigquery_TableId_com_google_cloud_bigquery_BigQuery_IAMOption____)(tableId);
          policy
              .toBuilder()
              .[addIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Policy.Builder.html#com_google_cloud_Policy_Builder_addIdentity_com_google_cloud_Role_com_google_cloud_Identity_com_google_cloud_Identity____)(
                  [Role](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Role.html).of("roles/bigquery.dataViewer"),
                  [Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.html).[user](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.html#com_google_cloud_Identity_user_java_lang_String_)("example-analyst-group@google.com"))
              .build();
          bigquery.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html#com_google_cloud_bigquery_BigQuery_setIamPolicy_com_google_cloud_bigquery_TableId_com_google_cloud_Policy_com_google_cloud_bigquery_BigQuery_IAMOption____)(tableId, policy);
          System.out.println("Iam policy created successfully");
        } catch ([BigQueryException](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryException.html) e) {
          System.out.println("Iam policy was not created. \n" + e.toString());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    bqclient = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    
    policy = bqclient.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_get_iam_policy)(
        your_table_id,  # e.g. "project.dataset.table"
    )
    
    analyst_email = "example-analyst-group@google.com"
    binding = {
        "role": "roles/bigquery.dataViewer",
        "members": {f"group:{analyst_email}"},
    }
    policy.bindings.append(binding)
    
    updated_policy = bqclient.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_set_iam_policy)(
        your_table_id,  # e.g. "project.dataset.table"
        policy,
    )
    
    for binding in updated_policy.bindings:
        print(repr(binding))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
