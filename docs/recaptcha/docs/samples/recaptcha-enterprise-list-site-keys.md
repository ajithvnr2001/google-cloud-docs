---
url: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-list-site-keys/
title: List reCAPTCHA Enterprise site keys \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:15.114677+00:00
---

# List reCAPTCHA Enterprise site keys  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-list-site-keys/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Samples ](https://docs.cloud.google.com/recaptcha/docs/samples)



#  List reCAPTCHA Enterprise site keys Stay organized with collections  Save and categorize content based on your preferences. 

List all keys present for the given project ID.

## Code sample

### Java

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html);
    import com.google.cloud.recaptchaenterprise.v1.[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).[ListKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListKeysPagedResponse.html);
    import com.google.recaptchaenterprise.v1.[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html);
    import com.google.recaptchaenterprise.v1.[ListKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListKeysRequest.html);
    import com.google.recaptchaenterprise.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html);
    import java.io.IOException;
    
    public class ListSiteKeys {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectID = "your-project-id";
    
        listSiteKeys(projectID);
      }
    
      /**
       * List all keys present under the given project ID.
       *
       * @param projectID : GCloud Project ID.
       */
      public static [ListKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListKeysPagedResponse.html) listSiteKeys(String projectID) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `client.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html) client = [RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.html).create()) {
          // Set the project ID to list the keys present in it.
          [ListKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListKeysRequest.html) listKeysRequest =
              [ListKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListKeysRequest.html).newBuilder().setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ProjectName.html).of(projectID).toString()).build();
    
          [ListKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListKeysPagedResponse.html) response = client.listKeys(listKeysRequest);
          System.out.println("Listing reCAPTCHA site keys: ");
          for ([Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key.html) key : response.iterateAll()) {
            System.out.println(key.getName());
          }
          return response;
        }
      }
    }

### PHP

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\RecaptchaEnterprise\V1\Client\RecaptchaEnterpriseServiceClient;
    use Google\Cloud\RecaptchaEnterprise\V1\ListKeysRequest;
    
    /**
     * List all the reCAPTCHA keys associate to a Google Cloud project
     *
     * @param string $projectId Your Google Cloud project ID
     */
    function list_keys(string $projectId): void
    {
        $client = new RecaptchaEnterpriseServiceClient();
        $formattedProject = $client->projectName($projectId);
    
        try {
            $listKeysRequest = (new ListKeysRequest())
                ->setParent($formattedProject)
                ->setPageSize(2);
            $response = $client->listKeys($listKeysRequest);
    
            print('Keys fetched' . PHP_EOL);
    
            // Either iterate over all the keys and let the library handle the paging
            foreach ($response->iterateAllElements() as $key) {
                print($key->getDisplayName() . PHP_EOL);
            }
    
            // Or fetch each page and process the keys as needed
            // foreach ($response->iteratePages() as $page) {
            //     foreach ($page as $key) {
            //         print($key->getDisplayName() . PHP_EOL);
            //     }
            // }
        } catch (ApiException $e) {
            print('listKeys() call failed with the following error: ');
            print($e);
        }
    }

### Python

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    from google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers import (
        [ListKeysPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager.html),
    )
    
    
    def list_site_keys(project_id: str) -> ListKeysPager:
        """List all keys present under the given project ID.
    
        Args:
        project_id: GCloud Project ID.
        """
    
        project_name = f"projects/{project_id}"
    
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Set the project id to list the keys present in it.
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ListKeysRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListKeysRequest.html)()
        request.parent = project_name
    
        response = client.[list_keys](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_keys)(request)
        print("Listing reCAPTCHA site keys: ")
        for i, key in enumerate(response):
            print(f"{str(i)}. {key.name}")
    
        return response
    
    

### Ruby

To authenticate to Fraud Defense, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/recaptcha_enterprise"
    
    # List all site keys registered to use recaptcha services.
    #
    # @param project_id [String] GCloud Project ID.
    # @return [void]
    def list_site_keys project_id:
      # Create the reCAPTCHA client.
      client = ::Google::Cloud::RecaptchaEnterprise.recaptcha_enterprise_service
    
      response = client.list_keys parent: "projects/#{project_id}"
      puts "Listing reCAPTCHA site keys: "
      response.each do |key|
        puts key.name
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=recaptcha_enterprise). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
