---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-delete-inspect-template/
title: Delete an inspection template \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:54.444946+00:00
---

# Delete an inspection template  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-delete-inspect-template/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Delete an inspection template Stay organized with collections  Save and categorize content based on your preferences. 

Delete an inspection template from Cloud DLP.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating Sensitive Data Protection de-identification templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid)
  * [Creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    
    public class InspectTemplateDelete
    {
        public static object Delete(string projectId, string templateName)
        {
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var request = new [DeleteInspectTemplateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeleteInspectTemplateRequest.html)
            {
                Name = templateName
            };
    
            client.DeleteInspectTemplate(request);
            Console.WriteLine($"Successfully deleted template {templateName}.");
    
            return templateName;
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
    
    // deleteInspectTemplate deletes the given template.
    func deleteInspectTemplate(w io.Writer, templateID string) error {
    	// projectID := "my-project-id"
    	// templateID := "my-template"
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	req := &dlppb.DeleteInspectTemplateRequest{
    		Name: templateID,
    	}
    
    	if err := client.DeleteInspectTemplate(ctx, req); err != nil {
    		return fmt.Errorf("DeleteInspectTemplate: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully deleted inspect template %v", templateID)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[DeleteInspectTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeleteInspectTemplateRequest.html);
    import java.io.IOException;
    
    class TemplatesDelete {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String templateId = "your-template-id";
        deleteInspectTemplate(projectId, templateId);
      }
    
      // Delete an existing template
      public static void deleteInspectTemplate(String projectId, String templateId) throws IOException {
        // Construct the template name to be deleted
        String templateName = String.format("projects/%s/inspectTemplates/%s", projectId, templateId);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Create delete template request to be sent by the client
          [DeleteInspectTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeleteInspectTemplateRequest.html) request =
              [DeleteInspectTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeleteInspectTemplateRequest.html).newBuilder().setName(templateName).build();
    
          // Send the request with the client
          dlpServiceClient.deleteInspectTemplate(request);
          System.out.printf("Deleted template: %s\n", templateName);
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
    
    // The name of the template to delete
    // Parent project ID is automatically extracted from this parameter
    // const templateName = 'projects/YOUR_PROJECT_ID/inspectTemplates/#####'
    async function deleteInspectTemplate() {
      // Construct template-deletion request
      const request = {
        name: templateName,
      };
    
      // Run template-deletion request
      await dlp.deleteInspectTemplate(request);
      console.log(`Successfully deleted template ${templateName}.`);
    }
    
    deleteInspectTemplate();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\DeleteInspectTemplateRequest;
    
    /**
     * Delete a DLP inspection configuration template.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $templateId        The name of the template to delete
     */
    function delete_inspect_template(
        string $callingProjectId,
        string $templateId
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Run template deletion request
        $templateName = "projects/$callingProjectId/locations/global/inspectTemplates/$templateId";
        $deleteInspectTemplateRequest = (new DeleteInspectTemplateRequest())
            ->setName($templateName);
        $dlp->deleteInspectTemplate($deleteInspectTemplateRequest);
    
        // Print results
        printf('Successfully deleted template %s' . PHP_EOL, $templateName);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def delete_inspect_template(project: str, template_id: str) -> None:
        """Deletes a Data Loss Prevention API template.
        Args:
            project: The id of the Google Cloud project which owns the template.
            template_id: The id of the template to delete.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Combine the template id with the parent id.
        template_resource = f"{parent}/inspectTemplates/{template_id}"
    
        # Call the API.
        dlp.[delete_inspect_template](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_delete_inspect_template)(request={"name": template_resource})
    
        print(f"Template {template_resource} successfully deleted.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
