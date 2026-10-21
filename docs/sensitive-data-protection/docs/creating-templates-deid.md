---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid/
title: Creating Sensitive Data Protection de-identification templates \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:15.091988+00:00
---

# Creating Sensitive Data Protection de-identification templates  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Creating Sensitive Data Protection de-identification templates Stay organized with collections  Save and categorize content based on your preferences. 

You can use _templates_ to create and persist configuration information to use with Sensitive Data Protection. Templates are useful for decoupling configuration such as what you inspect for and how you de-identify it from the implementation of your requests. Templates provide a robust way to re-use configuration and enable consistency across users and data sets.

The Sensitive Data Protection supports two types of templates:

  * _De-identification templates_ : Templates for saving configuration information for de-identification jobs, including both infoType and record (structured dataset) transformations.
  * _Inspection templates_ : Templates for persisting configuration information for inspection scan jobs, including what predefined or custom detectors to use. For more information about inspection templates, see [Creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates).



For conceptual information about templates in Sensitive Data Protection, see [Templates](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates).

The remainder of this topic shows you how to create de-identification templates for use with the Sensitive Data Protection.

## Create a de-identification template

### Console

In the Google Cloud console, go to the **Create template** page.

[Go to Create template](https://console.cloud.google.com/security/sensitive-data-protection/create/template;source=7)

The following sections describe how to fill in the **Create template** page.

### Define template

In the **Define template** section, fill in the fields as follows:

  1. For **Template type** , select **De-identify (remove sensitive data)**.
  2. For **Data transformation type** , select the type of transformation to apply:

     * **InfoType**. Sensitive Data Protection applies each transformation to only the value that was identified as the specific infoType. This transformation type is useful for unstructured text.

     * **Record**. Sensitive Data Protection considers the structured format of the data when it applies a transformation. This transformation type is useful for tabular data.

     * **Image**. Sensitive Data Protection redacts all detected text in an image or only text that matches a specific infoType.

  3. For **Template ID** , enter a unique identifier for the template.

  4. For **Display name** , enter a name for the template.

  5. For **Description** , describe the template.

  6. For **Resource location** , select **Global** or the location of the data that you want to de-identify.

  7. Click **Continue**.




### Configure de-identification

The selection of fields that appear in **Configure de-identification** is based on your chosen data transformation type.

#### InfoType

If you selected **InfoType** as the data transformation type, do the following:

  1. In the **Transformation** field, select a transformation method to apply to findings.

More fields appear according to your selection. Fill in the fields as needed. For more information, see [Transformation reference](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference).

  2. In the **InfoTypes to transform** section, specify whether you want to apply the transformation to all detected infoTypes that are defined in your inspection configuration.

If you select **Specify infoTypes** , select the infoTypes that you want to apply the transformation method to.

  3. If you want to add transformation rules for infoTypes that aren't covered by your transformation rule, click **Add transformation rule**. Then, fill in the fields as needed. Repeat this step until you've configured a transformation rule for all infoTypes that you want to transform.

  4. Click **Create**.




#### Record

If you selected **Record** as the data transformation type, do the following:

  1. For **Field(s) or column(s) to transform** , type the name of the table column containing the data that you want to transform. Then, press `ENTER`. Repeat this step for each column containing data that you want to transform.
  2. Specify the transformation type:

     * **Match on infoType**. Sensitive Data Protection treats each cell as unstructured text and applies the transformation to only the infoTypes that it finds in the cell. Sensitive Data Protection doesn't transform any data surrounding an infoType.

If you select this option, do the following:

       1. Click **Add transformation**. In the **Transformation** field, select a [transformation method](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference) to apply to findings.
       2. Specify whether you want to apply the transformation to all detected infoTypes that are defined in your inspection configuration.

If you select **Specify infoTypes** , select the infoTypes that you want to apply the transformation rule to.

If you want to assign certain transformation rules to certain infoTypes, you can add more transformations as needed.

     * **Primitive field transformation**. Sensitive Data Protection always transforms the entire cell according to a transformation method that you choose. This option is useful if you want to transform entire columns of data, regardless of whether cells in those columns have detected infoTypes.

If you select this option, in the **Transformation** field, select a transformation method to apply to the columns that you specified.

In both cases, more fields appear according to your selected transformation method. Fill in the fields as needed. For more information, see [Transformation reference](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference).

  3. Click **Create**.




#### Image

If you selected **Image** as the data transformation type, do the following:

  1. Optional: To change the color of the box that covers the redacted text, click the black box in the **Redaction color** field, and choose a different color.

  2. In the **InfoTypes to transform** section, specify what you want to redact: all detected text, all infoTypes defined in your inspection configuration, or only specific infoTypes.

If you select **Specify infoTypes** , select the infoTypes that you want to apply the transformation rule to.

  3. If you want to add transformation rules for infoTypes that aren't covered by your transformation rule, click **Add transformation rule**. Then, fill in the fields as needed. Repeat this step until you've configured a transformation rule for all infoTypes that you want to transform.

  4. Click **Create**. 




### Protocol

It's useful to note that a de-identification template is simply a reusable de-identification configuration plus some metadata. In API terms, the [`DeidentifyTemplate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#resource-deidentifytemplate) object is effectively a [`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig) object that includes a few more fields of metadata, such as a display name and a description. Therefore, to create a new de-identification template, the basic steps are:

  1. Start with a [`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig) object.
  2. Call or POST the `create` method of the [`projects.deidentifyTemplates`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates) resource, including in your request a [`DeidentifyTemplate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#resource-deidentifytemplate) object that contains a display name, a description, and that `DeidentifyConfig` object.



The returned `DeidentifyTemplate` will be usable immediately. You can reference it in other calls or jobs by its `name`. You can list the existing templates by calling the `*.deidentifyTemplates.list` method. To view a specific template, call the `*.deidentifyTemplates.get` method. Note that the limit for the number of templates you can create is 1000.

If you've already had some experience de-identifying sensitive data from text, images, or structured content using Sensitive Data Protection, you've already created a [`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig) object. One additional step turns it into a [`DeidentifyTemplate`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#resource-deidentifytemplate) object.

### REST example

The following JSON is an example of what you could send to the [`projects.deidentifyTemplates.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/create) method. This JSON creates a new template with the given display name and description, and scans for matches on the infoTypes `EMAIL_ADDRESS` and `GENERIC_ID`. When it finds content matching those infoTypes, it will mask the first three characters with an asterisk (`*`) character.

**Note:** The following example requires an [OAuth 2.0 access token](https://docs.cloud.google.com/sensitive-data-protection/docs/auth#using_a_service_account).

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/deidentifyTemplates
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

**JSON input**
    
    
    {
      "deidentifyTemplate":{
        "displayName":"Email and id masker",
        "description":"De-identifies emails and ids with a series of asterisks.",
        "deidentifyConfig":{
          "infoTypeTransformations":{
            "transformations":[
              {
                "infoTypes":[
                  {
                    "name":"GENERIC_ID"
                  }
                ],
                "primitiveTransformation":{
                  "replaceWithInfoTypeConfig":{
    
                  }
                }
              },
              {
                "infoTypes":[
                  {
                    "name":"EMAIL_ADDRESS"
                  }
                ],
                "primitiveTransformation":{
                  "characterMaskConfig":{
                    "charactersToIgnore":[
                      {
                        "charactersToSkip":"@"
                      }
                    ],
                    "maskingCharacter":"*"
                  }
                }
              }
            ]
          }
        }
      }
    }
    

**JSON output**
    
    
        {
          "name":"projects/PROJECT_ID/deidentifyTemplates/JOB-ID",
          "displayName":"Email and id masker",
          "description":"De-identifies emails and ids with a series of asterisks.",
          "createTime":"2018-11-30T07:17:59.536022Z",
          "updateTime":"2018-11-30T07:17:59.536022Z",
          "deidentifyConfig":{
            "infoTypeTransformations":{
              "transformations":[
                {
                  "infoTypes":[
                    {
                      "name":"GENERIC_ID"
                    }
                  ],
                  "primitiveTransformation":{
                    "replaceWithInfoTypeConfig":{
    
                    }
                  }
                },
                {
                  "infoTypes":[
                    {
                      "name":"EMAIL_ADDRESS"
                    }
                  ],
                  "primitiveTransformation":{
                    "characterMaskConfig":{
                      "maskingCharacter":"*",
                      "charactersToIgnore":[
                        {
                          "charactersToSkip":"@"
                        }
                      ]
                    }
                  }
                }
              ]
            }
          }
        }

To quickly try this out, you can use the APIs Explorer that's embedded below. For general information about using JSON to send requests to the DLP API, see the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-json).

## Using de-identification templates

Once you've created a new template, you can use its `name` identifier anywhere `deidentifyTemplateName` is accepted, such as:

  * [`projects.content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify): De-identifies potentially sensitive data in content using the template as its configuration. Be aware that this method can use either an inspection template or a de-identification template.



## Listing de-identification templates

To list all de-identification templates that have been created, use one of the `*.*.list` methods:

  * [`projects.deidentifyTemplates.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/list)



This section demonstrates how to use Sensitive Data Protection to list inspection templates. The process is identical to the one for listing de-identification templates.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

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
    
    

## Deleting de-identification templates

To delete a specific de-identification template, use one of the `*.*.delete` methods:

  * [`projects.deidentifyTemplates.delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/delete)



With each `*.*.delete` method, you include the resource name of the template to be deleted.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

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
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
