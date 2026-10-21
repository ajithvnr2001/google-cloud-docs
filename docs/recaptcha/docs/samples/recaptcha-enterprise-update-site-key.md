---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-update-site-key/
title: Update a site key \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:25:36.583140+00:00
---

# Update a site key  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-update-site-key/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Update a site key Stay organized with collections  Save and categorize content based on your preferences. 

Update the properties of the given site key for the given the project id.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest.html);
    import com.google.recaptchaenterprise.v1.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html);
    import com.google.recaptchaenterprise.v1.[KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html);
    import com.google.recaptchaenterprise.v1.[UpdateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UpdateKeyRequest.html);
    import com.google.recaptchaenterprise.v1.[WebKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateSiteKey {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "your-project-id";
        String recaptchaSiteKeyID = "recaptcha-site-key-id";
        String domainName = "domain-name";
    
        updateSiteKey(projectID, recaptchaSiteKeyID, domainName);
      }
    
      /**
       * Update the properties of the given site key present under the project id.
       *
       * @param projectID: GCloud Project ID.
       * @param recaptchaSiteKeyID: Specify the site key.
       * @param domainName: Specify the domain name for which the settings should be updated.
       */
      public static void updateSiteKey(String projectID, String recaptchaSiteKeyID, String domainName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the name and the new settings for the key.
          [UpdateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UpdateKeyRequest.html) updateKeyRequest =
              [UpdateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UpdateKeyRequest.html).newBuilder()
                  .setKey(
                      [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html).newBuilder()
                          .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.Builder.html#com_google_recaptchaenterprise_v1_Key_Builder_setDisplayName_java_lang_String_)("any descriptive name for the key")
                          .setName([KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html).of(projectID, recaptchaSiteKeyID).toString())
                          .[setWebSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.Builder.html#com_google_recaptchaenterprise_v1_Key_Builder_setWebSettings_com_google_recaptchaenterprise_v1_WebKeySettings_)(
                              [WebKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.html).newBuilder()
                                  .[setAllowAmpTraffic](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.Builder.html#com_google_recaptchaenterprise_v1_WebKeySettings_Builder_setAllowAmpTraffic_boolean_)(true)
                                  .addAllowedDomains(domainName)
                                  .build())
                          .build())
                  .build();
    
          client.[updateKeyCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html#com_google_cloud_recaptchaenterprise_v1_RecaptchaEnterpriseServiceClient_updateKeyCallable__)().futureCall(updateKeyRequest).get();
    
          // Check if the key has been updated.
          [GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest.html) getKeyRequest =
              [GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest.html).newBuilder()
                  .setName([KeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.KeyName.html).of(projectID, recaptchaSiteKeyID).toString())
                  .build();
          [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) response = client.getKey(getKeyRequest);
    
          // Get the changed property.
          boolean allowedAmpTraffic = response.[getWebSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html#com_google_recaptchaenterprise_v1_Key_getWebSettings__)().getAllowAmpTraffic();
          if (!allowedAmpTraffic) {
            System.out.println(
                "Error! reCAPTCHA Site key property hasn't been updated. Please try again !");
            return;
          }
          System.out.println("reCAPTCHA Site key successfully updated !");
        }
      }
    }

### PHP

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecaptchaEnterprise\V1\Client\RecaptchaEnterpriseServiceClient;
    use Google\Cloud\RecaptchaEnterprise\V1\Key;
    use Google\Cloud\RecaptchaEnterprise\V1\UpdateKeyRequest;
    use Google\Cloud\RecaptchaEnterprise\V1\WebKeySettings;
    use Google\Cloud\RecaptchaEnterprise\V1\WebKeySettings\ChallengeSecurityPreference;
    use Google\Cloud\RecaptchaEnterprise\V1\WebKeySettings\IntegrationType;
    use Google\Protobuf\FieldMask;
    
    /**
     * Update an existing reCAPTCHA site key
     *
     * @param string $projectId Your Google Cloud project ID
     * @param string $keyId The 40 char long key ID you wish to update
     * @param string $updatedName The updated display name of the reCAPTCHA key
     */
    function update_key(
        string $projectId,
        string $keyId,
        string $updatedName
    ): void {
        $client = new RecaptchaEnterpriseServiceClient();
        $formattedKeyName = $client->keyName($projectId, $keyId);
    
        // Create the settings for the key.
        // In order to create other keys we'll use AndroidKeySettings or IOSKeySettings
        $settings = new WebKeySettings();
    
        // Allow the key to work for all domains(Not recommended)
        // $settings->setAllowAllDomains(false);
        // ...or explicitly set the allowed domains for the key as an array of strings
        $settings->setAllowedDomains(['google.com']);
    
        // Specify the type of the key
        // - score based key -> IntegrationType::SCORE
        // - checkbox based key -> IntegrationType::CHECKBOX
        // Read https://cloud.google.com/recaptcha-enterprise/docs/choose-key-type
        $settings->setIntegrationType(IntegrationType::CHECKBOX);
    
        // Specify the possible challenge frequency and difficulty
        // Read https://cloud.google.com/recaptcha-enterprise/docs/reference/rest/v1/projects.keys#challengesecuritypreference
        $settings->setChallengeSecurityPreference(ChallengeSecurityPreference::SECURITY);
    
        $key = new Key();
        $key->setName($formattedKeyName);
        $key->setDisplayName($updatedName);
        $key->setWebSettings($settings);
    
        $updateMask = new FieldMask([
            'paths' => ['display_name', 'web_settings']
        ]);
    
        try {
            $updateKeyRequest = (new UpdateKeyRequest())
                ->setKey($key)
                ->setUpdateMask($updateMask);
            $updatedKey = $client->updateKey($updateKeyRequest);
    
            printf('The key: %s is updated.' . PHP_EOL, $updatedKey->getDisplayName());
        } catch (ApiException $e) {
            if ($e->getStatus() === 'NOT_FOUND') {
                printf('The key with Key ID: %s doesn\'t exist.' . PHP_EOL, $keyId);
            } else {
                print('updateKey() call failed with the following error: ');
                print($e);
            }
        }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    
    def update_site_key(project_id: str, recaptcha_site_key: str, domain_name: str) -> None:
        """
        Update the properties of the given site key present under the project id.
    
        Args:
        project_id: GCloud Project ID.
        recaptcha_site_key: Specify the site key.
        domain_name: Specify the domain name for which the settings should be updated.
        """
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Construct the key details.
        key_name = f"projects/{project_id}/keys/{recaptcha_site_key}"
    
        # Set the name and the new settings for the key.
        web_settings = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[WebKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.WebKeySettings.html)()
        web_settings.allow_amp_traffic = True
        web_settings.allowed_domains.append(domain_name)
    
        key = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key.html)()
        key.display_name = "any descriptive name for the key"
        key.name = key_name
        key.web_settings = web_settings
    
        update_key_request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[UpdateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateKeyRequest.html)()
        update_key_request.key = key
        client.[update_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_key)(update_key_request)
    
        time.sleep(5)
    
        # Retrieve the key and check if the property is updated.
        get_key_request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetKeyRequest.html)()
        get_key_request.name = key_name
        response = client.[get_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_key)(get_key_request)
        web_settings = response.web_settings
    
        # Get the changed property.
        if not web_settings.allow_amp_traffic:
            print(
                "Error! reCAPTCHA Site key property hasn't been updated. Please try again !"
            )
        else:
            print("reCAPTCHA Site key successfully updated ! ")
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Update a site key registered for a domain/app to use recaptcha services.
    #
    # @param project_id [String] GCloud Project ID.
    # @param site_key [String] Site key to be updated.
    # @param domain [String] Domain to register for recaptcha services.
    # @return [void]
    def update_site_key project_id:, site_key:, domain:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      request_key = client.get_key name: "projects/#{project_id}/keys/#{site_key}"
      request_key.web_settings.allowed_domains.push domain
      request_key.web_settings.allow_amp_traffic = true
    
      client.update_key key: request_key
    
      # Retrieve the key and check if the property is updated.
      response = client.get_key name: "projects/#{project_id}/keys/#{site_key}"
      web_settings = response.web_settings
    
      puts "reCAPTCHA Site key successfully updated with allow_amp_traffic to #{web_settings.allow_amp_traffic}!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
