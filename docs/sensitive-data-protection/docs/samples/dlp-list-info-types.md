---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-info-types/
title: List information types for a category \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:54.269933+00:00
---

# List information types for a category  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-info-types/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  List information types for a category Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates listing information types for a category.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Listing built-in infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/listing-infotypes)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InfoTypesList
    {
        public static ListInfoTypesResponse ListInfoTypes(string languageCode, string filter)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var response = dlp.ListInfoTypes(
                new [ListInfoTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListInfoTypesRequest.html)
                {
                    LanguageCode = languageCode,
                    Filter = filter
                });
    
            // Uncomment to print infotypes
            // Console.WriteLine("Info Types:");
            // foreach (var InfoType in response.InfoTypes)
            // {
            //     Console.WriteLine($"\t{InfoType.Name} ({InfoType.DisplayName})");
            // }
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // infoTypes returns the info types in the given language and matching the given filter.
    func infoTypes(w io.Writer, languageCode, filter string) error {
    	// languageCode := "en-US"
    	// filter := "supported_by=INSPECT"
    	ctx := context.Background()
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	req := &dlppb.ListInfoTypesRequest{
    		LanguageCode: languageCode,
    		Filter:       filter,
    	}
    	resp, err := client.ListInfoTypes(ctx, req)
    	if err != nil {
    		return fmt.Errorf("ListInfoTypes: %w", err)
    	}
    	for _, it := range resp.GetInfoTypes() {
    		fmt.Fprintln(w, it.GetName())
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[InfoTypeDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeDescription.html);
    import com.google.privacy.dlp.v2.[ListInfoTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesRequest.html);
    import com.google.privacy.dlp.v2.[ListInfoTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesResponse.html);
    import java.io.IOException;
    
    public class InfoTypesList {
    
      public static void main(String[] args) throws IOException {
        listInfoTypes();
      }
    
      // Lists the types of sensitive information the DLP API supports.
      public static void listInfoTypes() throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Construct the request to be sent by the client
          [ListInfoTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesRequest.html) listInfoTypesRequest =
              [ListInfoTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesRequest.html).newBuilder()
                  // Only return infoTypes supported by certain parts of the API.
                  // Supported filters are "supported_by=INSPECT" and "supported_by=RISK_ANALYSIS"
                  // Defaults to "supported_by=INSPECT"
                  .setFilter("supported_by=INSPECT")
                  // BCP-47 language code for localized infoType friendly names.
                  // Defaults to "en_US"
                  .[setLanguageCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesRequest.Builder.html#com_google_privacy_dlp_v2_ListInfoTypesRequest_Builder_setLanguageCode_java_lang_String_)("en-US")
                  .build();
    
          // Use the client to send the API request.
          [ListInfoTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesResponse.html) response = dlpClient.listInfoTypes(listInfoTypesRequest);
    
          // Parse the response and process the results
          System.out.println("Infotypes found:");
          for ([InfoTypeDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeDescription.html) infoTypeDescription : response.[getInfoTypesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInfoTypesResponse.html#com_google_privacy_dlp_v2_ListInfoTypesResponse_getInfoTypesList__)()) {
            System.out.println("Name : " + infoTypeDescription.getName());
            System.out.println("Display name : " + infoTypeDescription.getDisplayName());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The BCP-47 language code to use, e.g. 'en-US'
    // const languageCode = 'en-US';
    
    // The filter to use
    // const filter = 'supported_by=INSPECT'
    
    async function listInfoTypes() {
      const [response] = await dlp.listInfoTypes({
        languageCode: languageCode,
        filter: filter,
      });
      const infoTypes = response.infoTypes;
      console.log('Info types:');
      infoTypes.forEach(infoType => {
        console.log(`\t${infoType.name} (${infoType.displayName})`);
      });
    }
    
    listInfoTypes();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ListInfoTypesRequest;
    
    /**
     * Lists all Info Types for the Data Loss Prevention (DLP) API.
     *
     * @param string $filter        (Optional) filter to use
     * @param string $languageCode  (Optional) language code, empty for 'en-US'
     */
    function list_info_types(string $filter = '', string $languageCode = ''): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Run request
        $listInfoTypesRequest = (new ListInfoTypesRequest())
            ->setLanguageCode($languageCode)
            ->setFilter($filter);
        $response = $dlp->listInfoTypes($listInfoTypesRequest);
    
        // Print the results
        print('Info Types:' . PHP_EOL);
        foreach ($response->getInfoTypes() as $infoType) {
            printf(
                '  %s (%s)' . PHP_EOL,
                $infoType->getDisplayName(),
                $infoType->getName()
            );
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional
    
    import google.cloud.dlp
    
    
    def list_info_types(
        language_code: Optional[str] = None, result_filter: Optional[str] = None
    ) -> None:
        """List types of sensitive information within a category.
        Args:
            language_code: The BCP-47 language code to use, e.g. 'en-US'.
            result_filter: An optional filter to only return info types supported by
                    certain parts of the API. Defaults to "supported_by=INSPECT".
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Make the API call.
        response = dlp.[list_info_types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_list_info_types)(
            request={"parent": language_code, "filter": result_filter}
        )
    
        # Print the results to the console.
        print("Info types:")
        for info_type in response.info_types:
            print(
                "{name}: {display_name}".format(
                    name=info_type.name, display_name=info_type.display_name
                )
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
