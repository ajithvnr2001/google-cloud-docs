---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-get-site-key/
title: Get a reCAPTCHA site key \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:10:46.854771+00:00
---

# Get a reCAPTCHA site key  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-get-site-key/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Get a reCAPTCHA site key Stay organized with collections  Save and categorize content based on your preferences. 

Get reCAPTCHA site keys for the given the project ID.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest.html);
    import com.google.recaptchaenterprise.v1.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html);
    import com.google.recaptchaenterprise.v1.[KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class GetSiteKey {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "your-project-id";
        String recaptchaSiteKey = "recaptcha-site-key";
    
        getSiteKey(projectID, recaptchaSiteKey);
      }
    
      /**
       * Get the reCAPTCHA site key present under the project ID.
       *
       * @param projectID: GCloud Project ID.
       * @param recaptchaSiteKey: Specify the site key to get the details.
       */
      public static void getSiteKey(String projectID, String recaptchaSiteKey)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Construct the "GetSiteKey" request.
          [GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest.html) getKeyRequest =
              [GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest.html).newBuilder()
                  .setName([KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html).of(projectID, recaptchaSiteKey).toString())
                  .build();
    
          // Wait for the operation to complete.
          ApiFuture<Key> futureCall = client.[getKeyCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html#com_google_cloud_recaptchaenterprise_v1_RecaptchaEnterpriseServiceClient_getKeyCallable__)().futureCall(getKeyRequest);
          [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) key = futureCall.get(5, TimeUnit.SECONDS);
    
          System.out.println("Successfully obtained the key !" + key.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html#com_google_recaptchaenterprise_v1_Key_getName__)());
        }
      }
    }

### PHP

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecaptchaEnterprise\V1\Client\RecaptchaEnterpriseServiceClient;
    use Google\Cloud\RecaptchaEnterprise\V1\GetKeyRequest;
    use Google\Cloud\RecaptchaEnterprise\V1\WebKeySettings\IntegrationType;
    
    /**
     * Get a reCAPTCHA key from a google cloud project
     *
     * @param string $projectId Your Google Cloud project ID
     * @param string $keyId The 40 char long key ID you wish to fetch
     */
    function get_key(string $projectId, string $keyId): void
    {
        $client = new RecaptchaEnterpriseServiceClient();
        $formattedKeyName = $client->keyName($projectId, $keyId);
    
        try {
            // Returns a 'Google\Cloud\RecaptchaEnterprise\V1\Key' object
            $getKeyRequest = (new GetKeyRequest())
                ->setName($formattedKeyName);
            $key = $client->getKey($getKeyRequest);
            $webSettings = $key->getWebSettings();
    
            print('Key fetched' . PHP_EOL);
            printf('Display name: %s' . PHP_EOL, $key->getDisplayName());
            // $key->getCreateTime() returns a Google\Protobuf\Timestamp object
            printf('Create time: %d' . PHP_EOL, $key->getCreateTime()->getSeconds());
            printf('Web platform settings: %s' . PHP_EOL, $key->hasWebSettings() ? 'Yes' : 'No');
            printf('Allowed all domains: %s' . PHP_EOL, $key->hasWebSettings() && $webSettings->getAllowAllDomains() ? 'Yes' : 'No');
            printf('Integration Type: %s' . PHP_EOL, $key->hasWebSettings() ? IntegrationType::name($webSettings->getIntegrationType()) : 'N/A');
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('The key with Key ID: %s doesn\'t exist.' . PHP_EOL, $keyId);
            } else {
                print('getKey() call failed with the following error: ');
                print($e);
            }
        }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    
    def get_site_key(project_id: str, recaptcha_site_key: str) -> None:
        """
        Get the reCAPTCHA site key present under the project ID.
    
        Args:
        project_id: GCloud Project ID.
        recaptcha_site_key: Specify the site key to get the details.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Construct the key details.
        key_name = f"projects/{project_id}/keys/{recaptcha_site_key}"
    
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetKeyRequest.html)()
        request.name = key_name
    
        key = client.[get_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_key)(request)
        print("Successfully obtained the key !" + key.name)
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Get details of site key registered to use recaptcha services.
    #
    # @param project_id [String] GCloud Project ID.
    # @param site_key [String] Site key to be updated.
    # @return [void]
    def get_site_key project_id:, site_key:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      key = client.get_key name: "projects/#{project_id}/keys/#{site_key}"
      puts "Successfully obtained the key ! #{key.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
