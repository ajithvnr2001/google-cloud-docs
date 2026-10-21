---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-migrate-site-key/
title: Migrate a site key \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:15.336086+00:00
---

# Migrate a site key  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-migrate-site-key/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Migrate a site key Stay organized with collections  Save and categorize content based on your preferences. 

Migrate a site key from reCAPTCHA (non-Enterprise) to reCAPTCHA Enterprise.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html);
    import com.google.recaptchaenterprise.v1.[KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html);
    import com.google.recaptchaenterprise.v1.[MigrateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.MigrateKeyRequest.html);
    import java.io.IOException;
    
    public class MigrateKey {
    
      public static void main(String[] args) throws IOException {
        String projectId = "project-id";
        String recaptchaSiteKey = "recaptcha-site-key";
    
        migrateKey(projectId, recaptchaSiteKey);
      }
    
      /**
       * Migrate a key from reCAPTCHA (non-Enterprise) to reCAPTCHA Enterprise. If you created the key
       * using Admin console: https://www.google.com/recaptcha/admin/site, then use this API to migrate
       * to reCAPTCHA Enterprise. For more info, see:
       * https://cloud.google.com/recaptcha-enterprise/docs/migrate-recaptcha
       *
       * @param projectId: Google Cloud Project Id.
       * @param recaptchaSiteKey: Specify the site key to migrate.
       */
      public static void migrateKey(String projectId, String recaptchaSiteKey) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Specify the key name to migrate.
          [MigrateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.MigrateKeyRequest.html) migrateKeyRequest =
              [MigrateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.MigrateKeyRequest.html).newBuilder()
                  .setName([KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html).of(projectId, recaptchaSiteKey).toString())
                  .build();
    
          [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) response = client.migrateKey(migrateKeyRequest);
    
          // To verify if the site key has been migrated, use 'ListSiteKeys' and check if the
          // key is present.
          for ([Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) key : recaptcha.ListSiteKeys.listSiteKeys(projectId).iterateAll()) {
            if (key.equals(response)) {
              System.out.printf("Key migrated successfully: %s", recaptchaSiteKey);
            }
          }
        }
      }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    from list_site_keys import list_site_keys
    
    
    def migrate_site_key(project_id: str, recaptcha_site_key: str) -> None:
        """Migrate a key from reCAPTCHA (non-Enterprise) to reCAPTCHA Enterprise.
            If you created the key using Admin console: https://www.google.com/recaptcha/admin/site,
            then use this API to migrate to reCAPTCHA Enterprise.
            For more info, see: https://cloud.google.com/recaptcha-enterprise/docs/migrate-recaptcha
        Args:
        project_id: Google Cloud Project ID.
        recaptcha_site_key: Specify the site key to migrate.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Specify the key name to migrate.
        name = f"projects/{project_id}/keys/{recaptcha_site_key}"
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[MigrateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.MigrateKeyRequest.html)()
        request.name = name
    
        response = client.[migrate_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_migrate_key)(request)
        # To verify if the site key has been migrated, use 'list_site_keys' to check if the
        # key is present.
        for key in list_site_keys(project_id):
            if key.name == response.name:
                print(f"Key migrated successfully: {recaptcha_site_key}")
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Migrate a key from reCAPTCHA (non-Enterprise) to reCAPTCHA Enterprise.
    #
    # @param project_id [String] GCloud Project ID.
    # @param site_key [String] Site key to be updated.
    # @return [void]
    def migrate_site_key project_id:, site_key:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      response = client.migrate_key name: "projects/#{project_id}/keys/#{site_key}"
    
      # To verify if the site key has been migrated, use 'list_keys' to check if the
      # key is present.
      keys = client.list_keys parent: "projects/#{project_id}"
      keys.each do |key|
        puts "Key migrated successfully: #{site_key}" if key.name == response.name
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
