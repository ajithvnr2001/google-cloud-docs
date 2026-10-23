---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-inspect-template/
title: Create an inspection template \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:24.286869+00:00
---

# Create an inspection template  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-create-inspect-template/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create an inspection template Stay organized with collections  Save and categorize content based on your preferences. 

Use templates to create and persist configuration information for use with Cloud DLP. Templates are useful for decoupling configuration information—such as what you inspect for and how you de-identify it—from the implementation of your requests. Templates provide a way to re-use configuration and enable consistency across users and datasets. In addition, whenever you update a template, it's updated for any job trigger that uses it.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    
    public class InspectTemplateCreate
    {
        public static InspectTemplate Create(
            string projectId,
            string templateId,
            string displayName,
            string description,
            [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html) likelihood,
            int maxFindings,
            bool includeQuote)
        {
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var request = new [CreateInspectTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CreateInspectTemplateRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                InspectTemplate = new [InspectTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectTemplate.html)
                {
                    DisplayName = displayName,
                    Description = description,
                    InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                    {
                        MinLikelihood = likelihood,
                        Limits = new InspectConfig.Types.FindingLimits
                        {
                            MaxFindingsPerRequest = maxFindings
                        },
                        IncludeQuote = includeQuote
                    },
                },
                TemplateId = templateId
            };
    
            var response = client.CreateInspectTemplate(request);
    
            Console.WriteLine($"Successfully created template {response.Name}.");
    
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
    
    // createInspectTemplate creates a template with the given configuration.
    func createInspectTemplate(w io.Writer, projectID string, templateID, displayName, description string, infoTypeNames []string) error {
    	// projectID := "my-project-id"
    	// templateID := "my-template"
    	// displayName := "My Template"
    	// description := "My template description"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    
    	// Create a configured request.
    	req := &dlppb.CreateInspectTemplateRequest{
    		Parent:     fmt.Sprintf("projects/%s/locations/global", projectID),
    		TemplateId: templateID,
    		InspectTemplate: &dlppb.InspectTemplate{
    			DisplayName: displayName,
    			Description: description,
    			InspectConfig: &dlppb.InspectConfig{
    				InfoTypes:     infoTypes,
    				MinLikelihood: dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    				Limits: &dlppb.InspectConfig_FindingLimits{
    					MaxFindingsPerRequest: 10,
    				},
    			},
    		},
    	}
    	// Send the request.
    	resp, err := client.CreateInspectTemplate(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateInspectTemplate: %w", err)
    	}
    	// Print the result.
    	fmt.Fprintf(w, "Successfully created inspect template: %v", resp.GetName())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[CreateInspectTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateInspectTemplateRequest.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    class TemplatesCreate {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        createInspectTemplate(projectId);
      }
    
      // Creates a template to persist configuration information
      public static void createInspectTemplate(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // Construct the inspection configuration for the template
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).build();
    
          // Optionally set a display name and a description for the template
          String displayName = "Inspection Config Template";
          String description = "Save configuration for future inspection jobs";
    
          // Build the template
          [InspectTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html) inspectTemplate =
              [InspectTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html).newBuilder()
                  .setInspectConfig(inspectConfig)
                  .setDisplayName(displayName)
                  .setDescription(description)
                  .build();
    
          // Create the request to be sent by the client
          [CreateInspectTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateInspectTemplateRequest.html) createInspectTemplateRequest =
              [CreateInspectTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CreateInspectTemplateRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectTemplate(inspectTemplate)
                  .build();
    
          // Send the request to the API and process the response
          [InspectTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html) response =
              dlpServiceClient.createInspectTemplate(createInspectTemplateRequest);
          System.out.printf("Template created: %s", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html#com_google_privacy_dlp_v2_InspectTemplate_getName__)());
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
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'PHONE_NUMBER' }, { name: 'EMAIL_ADDRESS' }, { name: 'CREDIT_CARD_NUMBER' }];
    
    // Whether to include the matching string
    // const includeQuote = true;
    
    // (Optional) The name of the template to be created.
    // const templateId = 'my-template';
    
    // (Optional) The human-readable name to give the template
    // const displayName = 'My template';
    
    async function createInspectTemplate() {
      // Construct the inspection configuration for the template
      const inspectConfig = {
        infoTypes: infoTypes,
        minLikelihood: minLikelihood,
        includeQuote: includeQuote,
        limits: {
          maxFindingsPerRequest: maxFindings,
        },
      };
    
      // Construct template-creation request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectTemplate: {
          inspectConfig: inspectConfig,
          displayName: displayName,
        },
        templateId: templateId,
      };
    
      const [response] = await dlp.createInspectTemplate(request);
      const templateName = response.name;
      console.log(`Successfully created template ${templateName}.`);
    }
    createInspectTemplate();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\CreateInspectTemplateRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectTemplate;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    /**
     * Create a new DLP inspection configuration template.
     *
     * @param string $callingProjectId project ID to run the API call under
     * @param string $templateId       name of the template to be created
     * @param string $displayName      (Optional) The human-readable name to give the template
     * @param string $description      (Optional) A description for the trigger to be created
     * @param int    $maxFindings      (Optional) The maximum number of findings to report per request (0 = server maximum)
     */
    function create_inspect_template(
        string $callingProjectId,
        string $templateId,
        string $displayName = '',
        string $description = '',
        int $maxFindings = 0
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // ----- Construct inspection config -----
        // The infoTypes of information to match
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infoTypes = [$personNameInfoType, $phoneNumberInfoType];
    
        // Whether to include the matching string in the response
        $includeQuote = true;
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Specify finding limits
        $limits = (new FindingLimits())
            ->setMaxFindingsPerRequest($maxFindings);
    
        // Create the configuration object
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setLimits($limits)
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote($includeQuote);
    
        // Construct inspection template
        $inspectTemplate = (new InspectTemplate())
            ->setInspectConfig($inspectConfig)
            ->setDisplayName($displayName)
            ->setDescription($description);
    
        // Run request
        $parent = "projects/$callingProjectId/locations/global";
        $createInspectTemplateRequest = (new CreateInspectTemplateRequest())
            ->setParent($parent)
            ->setInspectTemplate($inspectTemplate)
            ->setTemplateId($templateId);
        $template = $dlp->createInspectTemplate($createInspectTemplateRequest);
    
        // Print results
        printf('Successfully created template %s' . PHP_EOL, $template->getName());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    from typing import Optional
    
    import google.cloud.dlp
    
    
    def create_inspect_template(
        project: str,
        info_types: List[str],
        template_id: Optional[str] = None,
        display_name: Optional[str] = None,
        min_likelihood: Optional[int] = None,
        max_findings: Optional[int] = None,
        include_quote: Optional[bool] = None,
    ) -> None:
        """Creates a Data Loss Prevention API inspect template.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            template_id: The id of the template. If omitted, an id will be randomly
                generated.
            display_name: The optional display name of the template.
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
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "info_types": info_types,
            "min_likelihood": min_likelihood,
            "include_quote": include_quote,
            "limits": {"max_findings_per_request": max_findings},
        }
    
        inspect_template = {
            "inspect_config": inspect_config,
            "display_name": display_name,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[create_inspect_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_create_inspect_template)(
            request={
                "parent": parent,
                "inspect_template": inspect_template,
                "template_id": template_id,
            }
        )
    
        print(f"Successfully created template {response.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
