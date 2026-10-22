---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-delete-site-key/
title: Delete a reCAPTCHA Enterprise site key \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:55.236531+00:00
---

# Delete a reCAPTCHA Enterprise site key  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-delete-site-key/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Delete a reCAPTCHA Enterprise site key Stay organized with collections  Save and categorize content based on your preferences. 

Delete the given reCAPTCHA site key for the given project ID.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[DeleteKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.DeleteKeyRequest.html);
    import com.google.recaptchaenterprise.v1.[KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteSiteKey {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "your-project-id";
        String recaptchaSiteKey = "recaptcha-site-key";
    
        deleteSiteKey(projectID, recaptchaSiteKey);
      }
    
      /**
       * Delete the given reCAPTCHA site key present under the project ID.
       *
       * @param projectID: GCloud Project ID.
       * @param recaptchaSiteKey: Specify the site key to be deleted.
       */
      public static void deleteSiteKey(String projectID, String recaptchaSiteKey)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the project ID and reCAPTCHA site key.
          [DeleteKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.DeleteKeyRequest.html) deleteKeyRequest =
              [DeleteKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.DeleteKeyRequest.html).newBuilder()
                  .setName([KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html).of(projectID, recaptchaSiteKey).toString())
                  .build();
    
          client.[deleteKeyCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html#com_google_cloud_recaptchaenterprise_v1_RecaptchaEnterpriseServiceClient_deleteKeyCallable__)().futureCall(deleteKeyRequest).get(5, TimeUnit.SECONDS);
          System.out.println("reCAPTCHA Site key successfully deleted !");
        }
      }
    }

### PHP

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecaptchaEnterprise\V1\Client\RecaptchaEnterpriseServiceClient;
    use Google\Cloud\RecaptchaEnterprise\V1\DeleteKeyRequest;
    
    /**
     * Delete an existing reCAPTCHA key from your Google Cloud project
     *
     * @param string $projectId Your Google Cloud project ID
     * @param string $keyId The 40 char long key ID you wish to delete
     */
    function delete_key(string $projectId, string $keyId): void
    {
        $client = new RecaptchaEnterpriseServiceClient();
        $formattedKeyName = $client->keyName($projectId, $keyId);
    
        try {
            $deleteKeyRequest = (new DeleteKeyRequest())
                ->setName($formattedKeyName);
            $client->deleteKey($deleteKeyRequest);
            printf('The key: %s is deleted.' . PHP_EOL, $keyId);
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('The key with Key ID: %s doesn\'t exist.' . PHP_EOL, $keyId);
            } else {
                print('deleteKey() call failed with the following error: ');
                print($e->getBasicMessage() . PHP_EOL);
            }
        }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    
    def delete_site_key(project_id: str, recaptcha_site_key: str) -> None:
        """Delete the given reCAPTCHA site key present under the project ID.
    
        Args:
        project_id : GCloud Project ID.
        recaptcha_site_key: Specify the key ID to be deleted.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Construct the key details.
        key_name = f"projects/{project_id}/keys/{recaptcha_site_key}"
    
        # Set the project ID and reCAPTCHA site key.
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[DeleteKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteKeyRequest.html)()
        request.name = key_name
    
        client.[delete_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_delete_key)(request)
        print("reCAPTCHA Site key deleted successfully ! ")
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Delete site key registered to use recaptcha services.
    #
    # @param project_id [String] GCloud Project ID.
    # @param site_key [String] Site key to be updated.
    # @return [void]
    def delete_site_key project_id:, site_key:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      client.delete_key name: "projects/#{project_id}/keys/#{site_key}"
      puts "reCAPTCHA Site key deleted successfully !"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
