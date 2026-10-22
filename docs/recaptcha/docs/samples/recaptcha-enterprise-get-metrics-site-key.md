---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-get-metrics-site-key/
title: Get reCAPTCHA site key metrics \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:00.676943+00:00
---

# Get reCAPTCHA site key metrics  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-get-metrics-site-key/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Get reCAPTCHA site key metrics Stay organized with collections  Save and categorize content based on your preferences. 

Get metrics specific to a reCAPTCHA site key.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[GetMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetMetricsRequest.html);
    import com.google.recaptchaenterprise.v1.[Metrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Metrics.html);
    import com.google.recaptchaenterprise.v1.[MetricsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.MetricsName.html);
    import com.google.recaptchaenterprise.v1.[ScoreMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ScoreMetrics.html);
    import java.io.IOException;
    
    public class GetMetrics {
    
      public static void main(String[] args) throws IOException {
        String projectId = "project-id";
        String recaptchaSiteKey = "recaptcha-site-key";
    
        getMetrics(projectId, recaptchaSiteKey);
      }
    
      /**
       * Get metrics specific to a recaptcha site key. E.g: score bucket count for a key or number of
       * times the checkbox key failed/ passed etc.,
       *
       * @param projectId: Google Cloud Project Id.
       * @param recaptchaSiteKey: Specify the site key to get metrics.
       */
      public static void getMetrics(String projectId, String recaptchaSiteKey) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          [GetMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetMetricsRequest.html) getMetricsRequest =
              [GetMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetMetricsRequest.html).newBuilder()
                  .setName([MetricsName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.MetricsName.html).of(projectId, recaptchaSiteKey).toString())
                  .build();
    
          [Metrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Metrics.html) response = client.getMetrics(getMetricsRequest);
    
          // Retrieve the metrics you want from the key.
          // If the site key is checkbox type: then use response.getChallengeMetricsList() instead of
          // response.getScoreMetricsList()
          for ([ScoreMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ScoreMetrics.html) scoreMetrics : response.[getScoreMetricsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Metrics.html#com_google_recaptchaenterprise_v1_Metrics_getScoreMetricsList__)()) {
            // Each ScoreMetrics is in the granularity of one day.
            int scoreBucketCount = scoreMetrics.getOverallMetrics().getScoreBucketsCount();
            System.out.println(scoreBucketCount);
          }
          System.out.printf("Retrieved the bucket count for score based key: %s", recaptchaSiteKey);
        }
      }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    
    def get_metrics(project_id: str, recaptcha_site_key: str) -> None:
        """Get metrics specific to a recaptcha site key.
            E.g: score bucket count for a key or number of
            times the checkbox key failed/ passed etc.,
        Args:
        project_id: Google Cloud Project ID.
        recaptcha_site_key: Specify the site key to get metrics.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        metrics_name = f"projects/{project_id}/keys/{recaptcha_site_key}/metrics"
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetMetricsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetMetricsRequest.html)()
        request.name = metrics_name
    
        response = client.[get_metrics](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_metrics)(request)
    
        # Retrieve the metrics you want from the key.
        # If the site key is checkbox type: then use response.challenge_metrics
        # instead of response.score_metrics
        for day_metric in response.score_metrics:
            # Each 'day_metric' is in the granularity of one day.
            score_bucket_count = day_metric.overall_metrics.score_buckets
            print(score_bucket_count)
    
        print(f"Retrieved the bucket count for score based key: {recaptcha_site_key}")
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    #  Get metrics specific to a recaptcha site key.
    #  E.g: score bucket count for a key or number of
    #  times the checkbox key failed/ passed etc.,
    #
    # @param project_id [String] GCloud Project ID.
    # @param site_key [String] Site key to be updated.
    # @return [void]
    def get_metrics_site_key project_id:, site_key:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      response = client.get_metrics name: "projects/#{project_id}/keys/#{site_key}/metrics"
    
      # Retrieve the metrics you want from the key.
      # If the site key is checkbox type: then use response.challenge_metrics
      # instead of response.score_metrics
      puts "Retrieved the bucket count for score based key: #{site_key}"
      response.score_metrics.each do |day_metric|
        # Each 'day_metric' is in the granularity of one day.
        score_bucket_count = day_metric.overall_metrics.score_buckets
        puts score_bucket_count.inspect
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
