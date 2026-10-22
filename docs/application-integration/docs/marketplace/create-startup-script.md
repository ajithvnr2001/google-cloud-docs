---
url: https://docs.cloud.google.com/application-integration/docs/marketplace/create-startup-script/
title: Create a startup script \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:24.597993+00:00
---

# Create a startup script  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/marketplace/create-startup-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a startup script

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to create a startup script for the web service and then validate the script.

To ensure that bringing up the web service does not require manual intervention, you must create a startup script.The startup script does the following tasks:

  * Reads the virtual machine (VM) metadata and sets the environment variable for metadata with the `CONNECTOR_ENV` prefix. Any data required by consumers is taken during VM creation from Marketplace and is set as environment variables in docker. These environment variables can then be read and processed accordingly in the application.
  * Starts the docker container containing the web service with the appropriate environment variables.



The following code is a sample startup script:
    
    
    #!/bin/bash
    
    # 1. Fetch Metadata Keys
    metadata_keys_url="http://metadata.google.internal/computeMetadata/v1/instance/attributes/"
    metadata_keys=$(curl -H "Metadata-Flavor: Google" "$metadata_keys_url")
    
    # 2. Set Environment Variables for CONNECTOR_ENV Keys (with error handling)
    for key in $metadata_keys; do
      if [[ $key == CONNECTOR_ENV_* ]]; then
        metadata_value_url="http://metadata.google.internal/computeMetadata/v1/instance/attributes/$key"
    
        # Fetch value with error handling
        value=$(curl -H "Metadata-Flavor: Google" "$metadata_value_url" 2>/dev/null)
        if [[ -z "$value" ]]; then
          echo "Warning: No value found for key '$key'. Skipping." >&2 # Log the warning to stderr
          continue  # Skip to the next iteration
        fi
        export "$key=$value"
      fi
    done
    
    # 3. Run Docker with Environment Variables
    sudo docker stop connector-service || true
    sudo docker run \
      --name connector-service \
     $(env | grep CONNECTOR_ENV_ | sed 's/=/="/;s/$/"/' | sed 's/^/-e /') \
     -d -p $CONNECTOR_ENV_PORT:$CONNECTOR_ENV_PORT \
     --restart=unless-stopped \
      connector-container

### Validate the startup script

  1. In the VM instance, add the metadata for the port and all other parameters which are required during VM creation. 
         
         gcloud compute instances add-metadata VM_NAME \                                                   
             --zone=VM_ZONE \
             --project=PROJECT_NAME \
             --metadata=CONNECTOR_ENV_PORT=8081

  2. Edit the VM from UI and add the startup script mentioned in the automation section. 

You can also use the following gcloud command: 
         
         gcloud compute instances add-metadata VM_NAME \                                                   
             --zone=VM_ZONE \
             --project=PROJECT_NAME \
             --metadata-from-file startup-script=gcp-start.sh

  3. After adding the startup script, ssh to the VM and run the following command: 
         
         sudo google_metadata_script_runner startup

  4. Run the following command to ensure that the docker container is running on the mentioned port. 
         
         sudo docker ps

  5. Run the following command to stop and remove the docker service. After testing, the service must not be running on the VM. 
         
         sudo docker rm -f connector-service

## What's next

     * Learn how to [create a VM deployment script](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-vm-deploy-tf).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
