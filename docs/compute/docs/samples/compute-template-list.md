---
url: https://docs.cloud.google.com/compute/docs/samples/compute-template-list/
title: List instance templates in a project \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:02.214750+00:00
---

# List instance templates in a project  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-template-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  List instance templates in a project Stay organized with collections  Save and categorize content based on your preferences. 

Get a list of instance templates defined in a project.

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
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    )
    
    // listInstanceTemplates prints a list of InstanceTemplate objects available in a project.
    func listInstanceTemplates(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	instanceTemplatesClient, err := compute.[NewInstanceTemplatesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstanceTemplatesClient_NewInstanceTemplatesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstanceTemplatesRESTClient: %w", err)
    	}
    	defer instanceTemplatesClient.Close()
    
    	req := &computepb.ListInstanceTemplatesRequest{
    		Project: projectID,
    	}
    
    	it := instanceTemplatesClient.List(ctx, req)
    	for {
    		instance, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s %s\n", instance.GetName(), instance.GetProperties().GetMachineType())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html);
    import com.google.cloud.compute.v1.[InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).ListPagedResponse;
    import java.io.IOException;
    
    public class ListInstanceTemplates {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // projectId: project ID or project number of the Cloud project you use.
        String projectId = "your-project-id";
        listInstanceTemplates(projectId);
      }
    
      // Get a list of InstanceTemplate objects available in a project.
      public static ListPagedResponse listInstanceTemplates(String projectId) throws IOException {
        try ([InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html) instanceTemplatesClient = [InstanceTemplatesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplatesClient.html).create()) {
          int count = 0;
          System.out.println("Listing instance templates...");
          ListPagedResponse templates = instanceTemplatesClient.list(projectId);
          for ([InstanceTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceTemplate.html) instanceTemplate : templates.iterateAll()) {
            System.out.printf("%s. %s%n", ++count, instanceTemplate.getName());
          }
          return templates;
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
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Print a list of instance template objects available in a project.
    async function listInstanceTemplates() {
      const instanceTemplatesClient = new compute.[InstanceTemplatesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const instanceTemplates = instanceTemplatesClient.listAsync({
        project: projectId,
      });
    
      for await (const instanceTemplate of instanceTemplates) {
        console.log(` - ${instanceTemplate.name}`);
      }
    }
    
    listInstanceTemplates();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    
    from google.cloud import compute_v1
    
    
    def list_instance_templates(project_id: str) -> Iterable[compute_v1.InstanceTemplate]:
        """
        Get a list of InstanceTemplate objects available in a project.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
    
        Returns:
            Iterable list of InstanceTemplate objects.
        """
        template_client = compute_v1.InstanceTemplatesClient()
        return template_client.list(project=project_id)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
