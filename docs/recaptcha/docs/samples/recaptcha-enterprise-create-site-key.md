---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-create-site-key/
title: Create a reCAPTCHA site key \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:17.296354+00:00
---

# Create a reCAPTCHA site key  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-create-site-key/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  Create a reCAPTCHA site key Stay organized with collections  Save and categorize content based on your preferences. 

Create a reCAPTCHA site key that binds a domain name to a unique key.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.recaptchaenterprise.v1.[CreateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateKeyRequest.html);
    import com.google.recaptchaenterprise.v1.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html);
    import com.google.recaptchaenterprise.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html);
    import com.google.recaptchaenterprise.v1.[WebKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.html);
    import com.google.recaptchaenterprise.v1.[WebKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.html).[IntegrationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.IntegrationType.html);
    import java.io.IOException;
    
    public class CreateSiteKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "your-project-id";
        String domainName = "domain-name";
    
        createSiteKey(projectID, domainName);
      }
    
      /**
       * Create reCAPTCHA Site key which binds a domain name to a unique key.
       *
       * @param projectID : GCloud Project ID.
       * @param domainName : Specify the domain name in which the reCAPTCHA should be activated.
       */
      public static String createSiteKey(String projectID, String domainName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
    
          // Set the type of reCAPTCHA to be displayed.
          // For different types, see: https://cloud.google.com/recaptcha-enterprise/docs/keys
          [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) scoreKey =
              [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html).newBuilder()
                  .[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.Builder.html#com_google_recaptchaenterprise_v1_Key_Builder_setDisplayName_java_lang_String_)("any_descriptive_name_for_the_key")
                  .[setWebSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.Builder.html#com_google_recaptchaenterprise_v1_Key_Builder_setWebSettings_com_google_recaptchaenterprise_v1_WebKeySettings_)(
                      [WebKeySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.html).newBuilder()
                          .addAllowedDomains(domainName)
                          .[setAllowAmpTraffic](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.Builder.html#com_google_recaptchaenterprise_v1_WebKeySettings_Builder_setAllowAmpTraffic_boolean_)(false)
                          .[setIntegrationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.Builder.html#com_google_recaptchaenterprise_v1_WebKeySettings_Builder_setIntegrationType_com_google_recaptchaenterprise_v1_WebKeySettings_IntegrationType_)([IntegrationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.WebKeySettings.IntegrationType.html).SCORE)
                          .build())
                  .build();
    
          [CreateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateKeyRequest.html) createKeyRequest =
              [CreateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateKeyRequest.html).newBuilder()
                  .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html).of(projectID).toString())
                  .setKey(scoreKey)
                  .build();
    
          // Get the name of the created reCAPTCHA site key.
          [Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) response = client.createKey(createKeyRequest);
          String keyName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html#com_google_recaptchaenterprise_v1_Key_getName__)();
          String recaptchaSiteKey = keyName.substring(keyName.lastIndexOf("/") + 1);
          System.out.println("reCAPTCHA Site key created successfully. Site Key: " + recaptchaSiteKey);
          return recaptchaSiteKey;
        }
      }
    }

### PHP

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecaptchaEnterprise\V1\Client\RecaptchaEnterpriseServiceClient;
    use Google\Cloud\RecaptchaEnterprise\V1\CreateKeyRequest;
    use Google\Cloud\RecaptchaEnterprise\V1\Key;
    use Google\Cloud\RecaptchaEnterprise\V1\WebKeySettings;
    use Google\Cloud\RecaptchaEnterprise\V1\WebKeySettings\IntegrationType;
    
    /**
     * Create a site key for reCAPTCHA
     *
     * @param string $projectId Your Google Cloud project ID
     * @param string $keyName The name of the key you wish to create
     */
    function create_key(string $projectId, string $keyName): void
    {
        $client = new RecaptchaEnterpriseServiceClient();
        $formattedProject = $client->projectName($projectId);
    
        // Create the settings for the key.
        // In order to create other keys we'll use AndroidKeySettings or IOSKeySettings
        $settings = new WebKeySettings();
    
        // Allow the key to work for all domains(Not recommended)
        $settings->setAllowAllDomains(true);
        // ...or explicitly set the allowed domains for the key as an array of strings
        // $settings->setAllowedDomains(['']);
    
        // Specify the type of the key
        // - score based key -> IntegrationType::SCORE
        // - checkbox based key -> IntegrationType::CHECKBOX
        // Read https://cloud.google.com/recaptcha-enterprise/docs/choose-key-type
        $settings->setIntegrationType(IntegrationType::CHECKBOX);
    
        $key = new Key();
        $key->setDisplayName($keyName);
        $key->setWebSettings($settings);
    
        try {
            $createKeyRequest = (new CreateKeyRequest())
                ->setParent($formattedProject)
                ->setKey($key);
            $createdKey = $client->createKey($createKeyRequest);
            printf('The key: %s is created.' . PHP_EOL, $createdKey->getName());
        } catch (ApiException $e) {
            print('createKey() call failed with the following error: ');
            print($e);
        }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    
    def create_site_key(project_id: str, domain_name: str) -> str:
        """Create reCAPTCHA Site key which binds a domain name to a unique key.
        Args:
        project_id : GCloud Project ID.
        domain_name: Specify the domain name in which the reCAPTCHA should be activated.
        """
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Set the type of the reCAPTCHA to be displayed.
        # For different types, see: https://cloud.google.com/recaptcha-enterprise/docs/keys
        web_settings = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[WebKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.WebKeySettings.html)()
        web_settings.allowed_domains.append(domain_name)
        web_settings.allow_amp_traffic = False
        web_settings.integration_type = web_settings.[IntegrationType](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.WebKeySettings.IntegrationType.html).SCORE
    
        key = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key.html)()
        key.display_name = "any descriptive name for the key"
        key.web_settings = web_settings
    
        # Create the request.
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[CreateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateKeyRequest.html)()
        request.parent = f"projects/{project_id}"
        request.key = key
    
        # Get the name of the created reCAPTCHA site key.
        response = client.[create_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_key)(request)
        recaptcha_site_key = response.name.rsplit("/", maxsplit=1)[1]
        print("reCAPTCHA Site key created successfully. Site Key: " + recaptcha_site_key)
        return recaptcha_site_key
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # Create a site key by registering a domain/app to use recaptcha services.
    #
    # @param project_id [String] GCloud Project ID.
    # @param domain [String] Domain to register for recaptcha services.
    # @return [void]
    def create_site_key project_id:, domain:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      request = {
        parent: "projects/#{project_id}",
        key: {
          display_name: "any descriptive name for the key",
          web_settings: {
            allowed_domains: [domain],
            allow_amp_traffic: false,
            integration_type: 1
          }
        }
      }
    
      # Get the name of the created reCAPTCHA site key.
      response = client.create_key request
      recaptcha_site_key = response.name.split("/").last
      puts "reCAPTCHA Site key created successfully. Site Key: #{recaptcha_site_key}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
