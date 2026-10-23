---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-inspect-templates/
title: List templates \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:13.566457+00:00
---

# List templates  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-list-inspect-templates/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  List templates Stay organized with collections  Save and categorize content based on your preferences. 

List inspection or de-identification templates.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating Sensitive Data Protection de-identification templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid)
  * [Creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    
    public class InspectTemplateList
    {
        public static PagedEnumerable<ListInspectTemplatesResponse, InspectTemplate> List(string projectId)
        {
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var response = client.ListInspectTemplates(
                new [ListInspectTemplatesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ListInspectTemplatesRequest.html)
                {
                    Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                }
            );
    
            // Uncomment to list templates
            //PrintTemplates(response);
    
            return response;
        }
    
        public static void PrintTemplates(PagedEnumerable<ListInspectTemplatesResponse, [InspectTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectTemplate.html)> response)
        {
            foreach (var template in response)
            {
                Console.WriteLine($"Template {template.Name}:");
                Console.WriteLine($"\tDisplay Name: {template.DisplayName}");
                Console.WriteLine($"\tDescription: {template.Description}");
                Console.WriteLine($"\tCreated: {template.CreateTime}");
                Console.WriteLine($"\tUpdated: {template.UpdateTime}");
                Console.WriteLine("Configuration:");
                Console.WriteLine($"\tMin Likelihood: {template.[InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)?.MinLikelihood}");
                Console.WriteLine($"\tInclude quotes: {template.[InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)?.IncludeQuote}");
                Console.WriteLine($"\tMax findings per request: {template.[InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)?.Limits.[MaxFindingsPerRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.Types.FindingLimits.html#Google_Cloud_Dlp_V2_InspectConfig_Types_FindingLimits_MaxFindingsPerRequest)}");
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
    	"time"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    	"github.com/golang/protobuf/ptypes"
    	"google.golang.org/api/iterator"
    )
    
    // listInspectTemplates lists the inspect templates in the project.
    func listInspectTemplates(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Create a configured request.
    	req := &dlppb.ListInspectTemplatesRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    	}
    
    	// Send the request and iterate over the results.
    	it := client.ListInspectTemplates(ctx, req)
    	for {
    		t, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    		fmt.Fprintf(w, "Inspect template %v\n", t.GetName())
    		c, err := ptypes.Timestamp(t.GetCreateTime())
    		if err != nil {
    			return fmt.Errorf("CreateTime Timestamp: %w", err)
    		}
    		fmt.Fprintf(w, "  Created: %v\n", c.Format(time.RFC1123))
    		u, err := ptypes.Timestamp(t.GetUpdateTime())
    		if err != nil {
    			return fmt.Errorf("UpdateTime Timestamp: %w", err)
    		}
    		fmt.Fprintf(w, "  Updated: %v\n", u.Format(time.RFC1123))
    		fmt.Fprintf(w, "  Display Name: %q\n", t.GetDisplayName())
    		fmt.Fprintf(w, "  Description: %q\n", t.GetDescription())
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).[ListInspectTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.ListInspectTemplatesPagedResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html);
    import com.google.privacy.dlp.v2.[ListInspectTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInspectTemplatesRequest.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import java.io.IOException;
    
    class TemplatesList {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        listInspectTemplates(projectId);
      }
    
      // Lists all templates associated with a given project
      public static void listInspectTemplates(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Create the request to be sent by the client
          [ListInspectTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInspectTemplatesRequest.html) request =
              [ListInspectTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ListInspectTemplatesRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setPageSize(1)
                  .build();
    
          // Send the request
          [ListInspectTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.ListInspectTemplatesPagedResponse.html) response = dlpServiceClient.listInspectTemplates(request);
    
          // Parse through and process the response
          System.out.println("Templates found:");
          for ([InspectTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectTemplate.html) template : response.getPage().getResponse().getInspectTemplatesList()) {
            System.out.printf("Template name: %s\n", template.getName());
            if (template.getDisplayName() != null) {
              System.out.printf("\tDisplay name: %s \n", template.getDisplayName());
              System.out.printf("\tCreate time: %s \n", template.getCreateTime());
              System.out.printf("\tUpdate time: %s \n", template.getUpdateTime());
    
              // print inspection config
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = template.getInspectConfig();
              for ([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType : inspectConfig.[getInfoTypesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html#com_google_privacy_dlp_v2_InspectConfig_getInfoTypesList__)()) {
                System.out.printf("\tInfoType: %s\n", infoType.getName());
              }
              System.out.printf("\tMin likelihood: %s\n", inspectConfig.[getMinLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html#com_google_privacy_dlp_v2_InspectConfig_getMinLikelihood__)());
              System.out.printf("\tLimits: %s\n", inspectConfig.[getLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html#com_google_privacy_dlp_v2_InspectConfig_getLimits__)().getMaxFindingsPerRequest());
            }
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
    
    // Helper function to pretty-print dates
    const formatDate = date => {
      const msSinceEpoch = parseInt(date.seconds, 10) * 1000;
      return new [Date](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.type.date.html)(msSinceEpoch).toLocaleString('en-US');
    };
    
    async function listInspectTemplates() {
      // Construct template-listing request
      const request = {
        parent: `projects/${projectId}/locations/global`,
      };
    
      // Run template-deletion request
      const [templates] = await dlp.listInspectTemplates(request);
    
      templates.forEach(template => {
        console.log(`Template ${template.name}`);
        if (template.displayName) {
          console.log(`  Display name: ${template.displayName}`);
        }
    
        console.log(`  Created: ${formatDate(template.createTime)}`);
        console.log(`  Updated: ${formatDate(template.updateTime)}`);
    
        const inspectConfig = template.inspectConfig;
        const infoTypes = inspectConfig.infoTypes.map(x => x.name);
        console.log('  InfoTypes:', infoTypes.join(' '));
        console.log('  Minimum likelihood:', inspectConfig.minLikelihood);
        console.log('  Include quotes:', inspectConfig.includeQuote);
    
        const limits = inspectConfig.limits;
        console.log('  Max findings per request:', limits.maxFindingsPerRequest);
      });
    }
    
    listInspectTemplates();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ListInspectTemplatesRequest;
    
    /**
     * List DLP inspection configuration templates.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     */
    function list_inspect_templates(string $callingProjectId): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $listInspectTemplatesRequest = (new ListInspectTemplatesRequest())
            ->setParent($parent);
        $response = $dlp->listInspectTemplates($listInspectTemplatesRequest);
    
        // Print results
        $templates = $response->iterateAllElements();
    
        foreach ($templates as $template) {
            printf('Template %s' . PHP_EOL, $template->getName());
            printf('  Created: %s' . PHP_EOL, $template->getCreateTime()->getSeconds());
            printf('  Updated: %s' . PHP_EOL, $template->getUpdateTime()->getSeconds());
            printf('  Display Name: %s' . PHP_EOL, $template->getDisplayName());
            printf('  Description: %s' . PHP_EOL, $template->getDescription());
    
            $inspectConfig = $template->getInspectConfig();
            if ($inspectConfig === null) {
                print('  No inspect config.' . PHP_EOL);
            } else {
                printf('  Minimum likelihood: %s' . PHP_EOL, $inspectConfig->getMinLikelihood());
                printf('  Include quotes: %s' . PHP_EOL, $inspectConfig->getIncludeQuote());
                $limits = $inspectConfig->getLimits();
                printf('  Max findings per request: %s' . PHP_EOL, $limits->getMaxFindingsPerRequest());
            }
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def list_inspect_templates(project: str) -> None:
        """Lists all Data Loss Prevention API inspect templates.
        Args:
            project: The Google Cloud project id to use as a parent resource.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[list_inspect_templates](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_list_inspect_templates)(request={"parent": parent})
    
        for template in response:
            print(f"Template {template.name}:")
            if template.display_name:
                print(f"  Display Name: {template.display_name}")
            print(f"  Created: {template.create_time}")
            print(f"  Updated: {template.update_time}")
    
            config = template.inspect_config
            print(
                "  InfoTypes: {}".format(", ".join([it.name for it in config.info_types]))
            )
            print(f"  Minimum likelihood: {config.min_likelihood}")
            print(f"  Include quotes: {config.include_quote}")
            print(
                "  Max findings per request: {}".format(
                    config.limits.max_findings_per_request
                )
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
