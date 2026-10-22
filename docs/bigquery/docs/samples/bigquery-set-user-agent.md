---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-set-user-agent/
title: Set user agent \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:48.243440+00:00
---

# Set user agent  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-set-user-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Set user agent Stay organized with collections  Save and categorize content based on your preferences. 

Set a custom user agent on a BigQuery client.

## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.rpc.[FixedHeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedHeaderProvider.html);
    import com.google.api.gax.rpc.[HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.cloud.bigquery.[BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html);
    import com.google.cloud.bigquery.[BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html);
    import com.google.common.collect.ImmutableMap;
    import java.io.IOException;
    
    public class SetUserAgent {
    
      private static final String USER_AGENT_HEADER = "user-agent";
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String customUserAgentValue = "my-custom-user-agent-value";
        setUserAgent(projectId, customUserAgentValue);
      }
    
      public static void setUserAgent(String projectId, String customUserAgentValue)
          throws IOException {
        // Setup the credentials
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) googleCredentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
    
        // Initialize the HeaderProvider object with custom user agent value
        [HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider.html) headerProvider =
            [FixedHeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedHeaderProvider.html).create(ImmutableMap.of(USER_AGENT_HEADER, customUserAgentValue));
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        [BigQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQuery.html) bigQuery =
            [BigQueryOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryOptions.html).newBuilder()
                .setProjectId(projectId)
                .[setCredentials](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder.html#com_google_api_gax_rpc_ClientContext_Builder_setCredentials_com_google_auth_Credentials_)(googleCredentials)
                .setHeaderProvider(headerProvider)
                .build()
                .getService();
    
        System.out.println(bigQuery.getOptions().[getUserAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-jdbc/latest/com.google.cloud.bigquery.jdbc.DataSource.html#com_google_cloud_bigquery_jdbc_DataSource_getUserAgent__)());
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
