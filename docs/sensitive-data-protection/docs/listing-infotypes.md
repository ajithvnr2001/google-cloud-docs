---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/listing-infotypes/
title: Listing built-in infoType detectors \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:49.563285+00:00
---

# Listing built-in infoType detectors  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/listing-infotypes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Listing built-in infoType detectors Stay organized with collections  Save and categorize content based on your preferences. 

InfoTypes are types of sensitive data. Sensitive Data Protection supports both built-in and custom infoTypes. You can view all built-in infoTypes in the [infoTypes reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference), or you can use the DLP API to list all built-in infoTypes programmatically.

The [`infoTypes.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/infoTypes/list) method lists all built-in infoTypes that are currently supported in Sensitive Data Protection. Each infoType includes the following information:

  * The infoType identifier (ID), the internal name of the infoType.
  * The infoType display name, a human readable infoType name.
  * Whether the infoType is supported by [inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text) or [risk analysis](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) operations.



## Code examples

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

To list all built-in infoType detectors:

### Console

  1. In the Google Cloud console, open Sensitive Data Protection.

[Go to Sensitive Data Protection UI](https://console.cloud.google.com/security/sensitive-data-protection;source=7)

  2. Click the **Configuration** tab, and then click **InfoTypes**.

  3. A table containing all built-in infoType detectors appears.




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
    
    

### REST

**JSON input:**
    
    
    GET https://dlp.googleapis.com/v2/infoTypes?key={YOUR_API_KEY}
    

The preceding request, when sent to the indicated endpoint, returns a list of all predefined detectors in the following format, where:

  * `[INFOTYPE-NAME]` represents the name of the infoType detector.
  * `[INFOTYPE-DISPLAY-NAME]` represents the display name for the detector
  * `"supportedBy"` is set to `"INSPECT"`, `"RISK_ANALYSIS"`, or both, depending on whether the detector is supported by [inspection](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text) or [risk analysis](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis) operations
  * `[INFOTYPE-DESCRIPTION]` represents the detector's description.



**JSON output:**
    
    
    {
      "infoTypes":[
        {
          "name":"[INFOTYPE-NAME]",
          "displayName":"[INFOTYPE-DISPLAY-NAME]",
          "supportedBy":[
            "INSPECT"
          ],
          "description":"[INFOTYPE-DESCRIPTION]"
        },
        ...
      ]
    }
    

## APIs Explorer

You can list infoType detectors using APIs Explorer:

  1. Go to the APIs Explorer on the API reference page for `infoTypes.list` by clicking the following button:

[Open APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/infoTypes/list?apix=true)

  2. Uncheck **Google OAuth 2.0**.

**Note:** Authenticating with just an API key is only recommended for testing Sensitive Data Protection with non-sensitive data.
  3. Click **Execute**.




APIs Explorer sends a request to Sensitive Data Protection, which sends back a JSON object containing all supported infoType detectors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
