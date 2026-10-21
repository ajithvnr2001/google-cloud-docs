---
url: https://docs.cloud.google.com/compute/docs/samples/compute-regional-disk-attach-read-only/
title: Attach a regional disk to a Compute Engine VM instance in read-only mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:48:21.142286+00:00
---

# Attach a regional disk to a Compute Engine VM instance in read-only mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-regional-disk-attach-read-only/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Attach a regional disk to a Compute Engine VM instance in read-only mode Stay organized with collections  Save and categorize content based on your preferences. 

Attach a regional disk to a Compute Engine VM instance in read-write mode Attach a regional disk to a single virtual machine running in Google Compute Engine. The disk also needs to be mounted by the operating system before it can be used. The disk is attached in read-only mode. The disk can be attached to multiple VM instances simultaneously.

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
    )
    
    // Attaches the provided regional disk in read-only mode to the given VM.
    // Read-only disks can be attached to multiple VMs at once.
    func attachRegionalDiskReadOnly(w io.Writer, projectID, zone, instanceName, diskUrl string) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-a" // refers to the instance, not the disk
    	// instanceName := "your_instance_name"
    	// diskUrl := "projects/your_project/regions/europe-west3/disks/your_disk"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return err
    	}
    	defer instancesClient.Close()
    
    	mode := "READ_ONLY"
    
    	req := &computepb.AttachDiskInstanceRequest{
    		AttachedDiskResource: &computepb.AttachedDisk{
    			Source: &diskUrl,
    			Mode:   &mode,
    		},
    		Instance: instanceName,
    		Project:  projectID,
    		Zone:     zone,
    	}
    
    	op, err := instancesClient.AttachDisk(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to attach disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk attached\n")
    
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
