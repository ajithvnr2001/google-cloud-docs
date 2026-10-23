---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-string/
title: Inspect a string \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:01.303527+00:00
---

# Inspect a string  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-string/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Inspect a string Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates finding sensitive data in a string.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Inspecting text for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectString
    {
        public static InspectContentResponse Inspect(
            string projectId,
            string dataValue,
            string minLikelihood,
            int maxFindings,
            bool includeQuote,
            IEnumerable<InfoType> infoTypes,
            IEnumerable<CustomInfoType> customInfoTypes)
        {
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                MinLikelihood = ([Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html))Enum.Parse(typeof([Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html)), minLikelihood, true),
                Limits = new [FindingLimits](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html)
                {
                    MaxFindingsPerRequest = maxFindings
                },
                IncludeQuote = includeQuote,
                InfoTypes = { infoTypes },
                CustomInfoTypes = { customInfoTypes }
            };
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
                {
                    Value = dataValue
                },
                InspectConfig = inspectConfig
            };
    
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var response = dlp.InspectContent(request);
    
            PrintResponse(includeQuote, response);
    
            return response;
        }
    
        private static void PrintResponse(bool includeQuote, [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html) response)
        {
            var findings = response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result).Findings;
            if (findings.Any())
            {
                Console.WriteLine("Findings:");
                foreach (var finding in findings)
                {
                    if (includeQuote)
                    {
                        Console.WriteLine($"  Quote: {finding.Quote}");
                    }
                    Console.WriteLine($"  InfoType: {finding.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)}");
                    Console.WriteLine($"  Likelihood: {finding.[Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html)}");
                }
            }
            else
            {
                Console.WriteLine("No findings.");
            }
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
    
    // inspectString inspects the a given string, and prints results.
    func inspectString(w io.Writer, projectID, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "My name is Gary and my email is gary@example.com"
    	ctx := context.Background()
    
    	// Initialize client.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	// Create and send the request.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item: &dlppb.ContentItem{
    			DataItem: &dlppb.ContentItem_Value{
    				Value: textToInspect,
    			},
    		},
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes: []*dlppb.InfoType{
    				{Name: "PHONE_NUMBER"},
    				{Name: "EMAIL_ADDRESS"},
    				{Name: "CREDIT_CARD_NUMBER"},
    			},
    			IncludeQuote: true,
    		},
    	}
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	result := resp.Result
    	fmt.Fprintf(w, "Findings: %d\n", len(result.Findings))
    	for _, f := range result.Findings {
    		fmt.Fprintf(w, "\tQuote: %s\n", f.Quote)
    		fmt.Fprintf(w, "\tInfo type: %s\n", f.InfoType.Name)
    		fmt.Fprintf(w, "\tLikelihood: %s\n", f.Likelihood)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).[BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class InspectString {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "My name is Gary and my email is gary@example.com";
        inspectString(projectId, textToInspect);
      }
    
      // Inspects the provided text.
      public static void inspectString(String projectId, String textToInspect) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          List<InfoType> infoTypes = new ArrayList<>();
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          for (String typeName : new String[] {"PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true).build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
                  .build();
    
          // Use the client to send the API request.
          [InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html) response = dlp.inspectContent(request);
    
          // Parse the response and process results
          System.out.println("Findings: " + response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsCount());
          for ([Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html) f : response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsList()) {
            System.out.println("\tQuote: " + f.getQuote());
            System.out.println("\tInfo type: " + f.getInfoType().getName());
            System.out.println("\tLikelihood: " + f.getLikelihood());
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
    
    // The string to inspect
    // const string = 'My name is Gary and my email is gary@example.com';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // Whether to include the matching string
    // const includeQuote = true;
    
    async function inspectString() {
      // Construct item to inspect
      const item = {value: string};
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: {
          infoTypes: infoTypes,
          customInfoTypes: customInfoTypes,
          minLikelihood: minLikelihood,
          includeQuote: includeQuote,
          limits: {
            maxFindingsPerRequest: maxFindings,
          },
        },
        item: item,
      };
    
      // Run request
      const [response] = await dlp.inspectContent(request);
      const findings = response.result.findings;
      if (findings.length > 0) {
        console.log('Findings:');
        findings.forEach(finding => {
          if (includeQuote) {
            console.log(`\tQuote: ${finding.quote}`);
          }
          console.log(`\tInfo type: ${finding.infoType.name}`);
          console.log(`\tLikelihood: ${finding.likelihood}`);
        });
      } else {
        console.log('No findings.');
      }
    }
    inspectString();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    /**
     * @param string $projectId
     * @param string $textToInspect
     */
    function inspect_string(string $projectId, string $textToInspect): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Construct request
        $parent = "projects/$projectId/locations/global";
        $item = (new ContentItem())
            ->setValue($textToInspect);
        $inspectConfig = (new InspectConfig())
            // The infoTypes of information to match
            ->setInfoTypes([
                (new InfoType())->setName('PHONE_NUMBER'),
                (new InfoType())->setName('EMAIL_ADDRESS'),
                (new InfoType())->setName('CREDIT_CARD_NUMBER')
            ])
            // Whether to include the matching string
            ->setIncludeQuote(true);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
        $findings = $response->getResult()->getFindings();
        if (count($findings) == 0) {
            print('No findings.' . PHP_EOL);
        } else {
            print('Findings:' . PHP_EOL);
            foreach ($findings as $finding) {
                print('  Quote: ' . $finding->getQuote() . PHP_EOL);
                print('  Info type: ' . $finding->getInfoType()->getName() . PHP_EOL);
                $likelihoodString = Likelihood::name($finding->getLikelihood());
                print('  Likelihood: ' . $likelihoodString . PHP_EOL);
            }
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def inspect_string(
        project: str,
        content_string: str,
        info_types: List[str],
        custom_dictionaries: List[str] = None,
        custom_regexes: List[str] = None,
        min_likelihood: str = None,
        max_findings: str = None,
        include_quote: bool = True,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze strings for protected data.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            max_findings: The maximum number of findings to report; 0 = no maximum.
            include_quote: Boolean for whether to display a quote of the detected
                information in the results.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Prepare custom_info_types by parsing the dictionary word lists and
        # regex patterns.
        if custom_dictionaries is None:
            custom_dictionaries = []
        dictionaries = [
            {
                "info_type": {"name": f"CUSTOM_DICTIONARY_{i}"},
                "dictionary": {"word_list": {"words": custom_dict.split(",")}},
            }
            for i, custom_dict in enumerate(custom_dictionaries)
        ]
        if custom_regexes is None:
            custom_regexes = []
        regexes = [
            {
                "info_type": {"name": f"CUSTOM_REGEX_{i}"},
                "regex": {"pattern": custom_regex},
            }
            for i, custom_regex in enumerate(custom_regexes)
        ]
        custom_info_types = dictionaries + regexes
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "custom_info_types": custom_info_types,
            "min_likelihood": min_likelihood,
            "include_quote": include_quote,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                try:
                    if finding.quote:
                        print(f"Quote: {finding.quote}")
                except AttributeError:
                    pass
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### Ruby

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id   = "Your Google Cloud project ID"
    # content      = "The text to inspect"
    # max_findings = "Maximum number of findings to report per request (0 = server maximum)"
    
    require "google/cloud/dlp"
    
    dlp = Google::Cloud::[Dlp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp.html).[dlp_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp/latest/Google-Cloud-Dlp.html)
    inspect_config = {
      # The types of information to match
      info_types:     [{ name: "PERSON_NAME" }, { name: "US_STATE" }],
    
      # Only return results above a likelihood threshold (0 for all)
      min_likelihood: :POSSIBLE,
    
      # Limit the number of findings (0 for no limit)
      limits:         { max_findings_per_request: max_findings },
    
      # Whether to include the matching string in the response
      include_quote:  true
    }
    
    # The item to inspect
    item_to_inspect = { value: content }
    
    # Run request
    parent = "projects/#{project_id}/locations/global"
    response = dlp.inspect_content parent:         parent,
                                   inspect_config: inspect_config,
                                   item:           item_to_inspect
    
    # Print the results
    if response.result.findings.empty?
      puts "No findings"
    else
      response.result.findings.each do |finding|
        puts "Quote:      #{finding.quote}"
        puts "Info type:  #{finding.info_type.name}"
        puts "Likelihood: #{finding.likelihood}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
