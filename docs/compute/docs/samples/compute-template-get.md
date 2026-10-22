---
url: https://docs.cloud.google.com/compute/docs/samples/compute-template-get/
title: Get information about an instance template \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:42.822632+00:00
---

# Get information about an instance template  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-template-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Get information about an instance template Stay organized with collections  Save and categorize content based on your preferences. 

Get the basic information and instance configuration defined in an instance template.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get, List, and Delete Instance Templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // getInstanceTemplate retrieves an instance template, which you can use to create virtual machine
    // (VM) instances and managed instance groups (MIGs).
    func getInstanceTemplate(projectID, templateName string) (*computepb.InstanceTemplate, error) {
    	// projectID := "your_project_id"
    	// templateName := "your_template_name"
    
    	ctx := context.Background()
    	instanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer instanceTemplatesClient.Close()
    
    	req := &computepb.GetInstanceTemplateRequest{
    		Project:          projectID,
    		InstanceTemplate: templateName,
    	}
    
    	return instanceTemplatesClient.Get(ctx, req)
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[GetInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceTemplateRequest.html);
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import java.io.IOException;
    
    public class GetInstanceTemplate {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you use.
        // templateName: name of the template to retrieve.
        String projectId = "your-project-id";
        String templateName = "template-name";
        getInstanceTemplate(projectId, templateName);
      }
    
      //  Retrieve an instance template, which you can use to create virtual machine
      //  (VM) instances and managed instance groups (MIGs).
      public static void getInstanceTemplate(String projectId, String templateName) throws IOException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
    
          [GetInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceTemplateRequest.html) getInstanceTemplateRequest = [GetInstanceTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceTemplateRequest.html)
              .newBuilder()
              .setProject(projectId)
              .setInstanceTemplate(templateName).build();
    
          [InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate = instanceTemplatesClient.get(getInstanceTemplateRequest);
          System.out.println("Instance Template retrieved: " + instanceTemplate.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html#com_google_cloud_compute_v1_InstanceTemplate_getName__)());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const templateName = 'your_template_name';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Retrieve an instance template, which you can use to create
    // virtual machine (VM) instances and managed instance groups (MIGs).
    async function getInstanceTemplate() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instance] = await instanceTemplatesClient.get({
        project: projectId,
        instanceTemplate: templateName,
      });
    
      console.log('Instance template:', instance);
    }
    
    getInstanceTemplate();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import compute_v1
    
    
    def get_instance_template(
        project_id: str, template_name: str
    ) -> compute_v1.InstanceTemplate:
        """
        Retrieve an instance template, which you can use to create virtual machine
        (VM) instances and managed instance groups (MIGs).
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            template_name: name of the template to retrieve.
    
        Returns:
            InstanceTemplate object that represents the retrieved template.
        """
        template_client = compute_v1.InstanceTemplatesClient()
        return template_client.get(project=project_id, instance_template=template_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
