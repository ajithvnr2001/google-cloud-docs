---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location/
title: Specifying processing locations \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:47.432043+00:00
---

# Specifying processing locations  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Specifying processing locations Stay organized with collections  Save and categorize content based on your preferences. 

With the ability to specify a region in which to perform your Sensitive Data Protection operations, you can control where your potentially sensitive data is processed. This document explains the concept of Sensitive Data Protection processing location and shows you how to specify a region.

To see a list of supported regions and multi-regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).

## About regions and multi-regions

A _region_ is a specific geographic place, such as the western United States or northeast Asia. A _multi-region location_ (or just _multi-region_) is a large geographic area, such as the European Union, that contains two or more geographic regions.

## Location considerations

A good location balances latency, availability, and bandwidth costs.

  * Use a region to help optimize latency and network bandwidth.

  * Use a multi-region when you want to process data from outside of the Google network and distributed across large geographic areas, or when you want the higher availability that comes with being redundant across regions.

  * Generally, you should process your data in a location that is convenient or contains the majority of the users of your data.

  * If your organization is required to keep in-transit data within a specified location, then use only the regions or multi-regions that [support regional endpoints](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#regional-endpoints). In this case, you need to use the Cloud Data Loss Prevention API, because the regional endpoints for Sensitive Data Protection aren't available for use with the Google Cloud console.




## Specify a region

How you specify the processing region depends on the type of endpoint you are sending the request to—the _global endpoint_ or a _regional endpoint_. The type of endpoint you choose depends on whether you're required to keep in-transit data within a specified region. For more information, see [Global and regional endpoints for Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints).

### Specify a region in a request to the global endpoint

### Console

Choose a region when setting up your Sensitive Data Protection operation.

For example, when [creating a job trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers), choose a location from the **Resource location** menu, as shown here:

![](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/specifying-location-trigger.png)

If the processing location is not a concern, use the **Global** region and Google chooses the location where processing should take place. **Global** is the default region choice.

### REST

Insert region information into the request endpoint URL. If the processing location is not a concern, use the `global` region and Google chooses the location where processing should take place. Note that any resources created by a request that specifies the `global` region are stored under the `global` region.

The following are some example requests to the global endpoint.

#### Using the global region

The following two requests have the same effect. Not including a region is the same as specifying `locations/global/`.
    
    
    POST https://www.googleapis.com/dlp/v2/projects/PROJECT_ID/locations/global/content:inspect
    
    
    POST https://www.googleapis.com/dlp/v2/projects/PROJECT_ID/content:inspect

#### Using a specific region

To specify a region for processing, within the resource URL, insert `locations/` and then the [region name](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).
    
    
    POST https://www.googleapis.com/dlp/v2/projects/PROJECT_ID/locations/us-west2/content:inspect

### Specify a region in a request to a regional endpoint

### Console

For Sensitive Data Protection, regional endpoints aren't available for use with the Google Cloud console.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.InspectConfig.Types;
    
    public class InspectStringRep
    {
        public static InspectContentResponse Inspect(
            string projectId,
            string repLocation,
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
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, repLocation).ToString(),
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
                {
                    Value = dataValue
                },
                InspectConfig = inspectConfig
            };
    
            var dlp = new [DlpServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClientBuilder.html)
            {
                Endpoint = $"dlp.{repLocation}.rep.googleapis.com"
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClientBuilder.html#Google_Cloud_Dlp_V2_DlpServiceClientBuilder_Build)();
    
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
    	"google.golang.org/api/option"
    )
    
    // inspectString inspects the a given string, and prints results.
    func inspectStringRep(w io.Writer, projectID, repLocation, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "My name is Gary and my email is gary@example.com"
    	ctx := context.Background()
    
    	// Assemble the regional endpoint url using provided rep location
    	repEndpoint := fmt.Sprintf("dlp.%s.rep.googleapis.com:443", repLocation)
    
    	// Initialize client.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx, option.WithEndpoint(repEndpoint))
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	// Create and send the request.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, repLocation),
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
    import com.google.cloud.dlp.v2.[DlpServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceSettings.html);
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
    
    public class InspectStringRep {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String repLocation = "regional-endpoint-location-to-use";
        String textToInspect = "My name is Gary and my email is gary@example.com";
        inspectString(projectId, repLocation, textToInspect);
      }
    
      // Inspects the provided text.
      public static void inspectString(String projectId, String repLocation, String textToInspect)
          throws IOException {
        // Assemble the regional endpoint url using provided rep location
        String repEndpoint = String.format("dlp.%s.rep.googleapis.com:443", repLocation);
        [DlpServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceSettings.html) settings = [DlpServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceSettings.html).newBuilder()
            .setEndpoint(repEndpoint)
            .build();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create(settings)) {
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
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, repLocation).toString())
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

### REST

The following example sends a `content.inspect` request to a regional endpoint. Any data attached to this request remains in the specified region while in transit, in use, and at rest.

Before using any of the request data, make the following replacements: 

  * `REGION`: a region where a regional endpoint for Sensitive Data Protection is available—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: your Google Cloud project ID. Project IDs are alphanumeric strings, like `example-project`. 



HTTP method and URL: 
    
    
    POST https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/content:inspect

Request JSON body: 
    
    
    {
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ]
      },
      "item": {
        "value": "hi, my ccn is 4111111111111111"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `inspect-request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @inspect-request.json \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/content:inspect"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `inspect-request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile inspect-request.json `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/content:inspect" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "result": {
        "findings": [
          {
            "infoType": {
              "name": "CREDIT_CARD_NUMBER",
              "sensitivityScore": {
                "score": "SENSITIVITY_HIGH"
              }
            },
            "likelihood": "LIKELY",
            "location": {
              "byteRange": {
                "start": "14",
                "end": "30"
              },
              "codepointRange": {
                "start": "14",
                "end": "30"
              }
            },
            "createTime": "2024-08-09T19:54:13.348Z",
            "findingId": "2024-08-09T19:54:13.352163Z4747901452516738787"
          }
        ]
      }
    }

## Co-location considerations

When you scan a storage repository such as Cloud Storage or BigQuery, you should specify the same location in your Sensitive Data Protection request as the location of the repository you're scanning. For example, if the BigQuery dataset is in the European Union multi-region location, specify the European Union multi-region (`europe`) when configuring the Sensitive Data Protection job.

If you do not co-locate your Sensitive Data Protection request with the storage repository you're scanning, processing of your request may be split between the location of the data and the location specified in the request.

**Note:** Sensitive Data Protection templates, stored infoTypes, and Cloud KMS keys can only be used by Sensitive Data Protection jobs, job triggers, and the [`content` methods](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types) in the same region.

## What's next

  * Learn more about [geography and zones](https://docs.cloud.google.com/docs/geography-and-regions).
  * See a list of [supported regions and multi-regions](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).
  * Learn more about [Global and regional endpoints for Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
