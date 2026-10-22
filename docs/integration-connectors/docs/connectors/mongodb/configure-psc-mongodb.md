---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb/
title: Example: Private connectivity for a MongoDB Atlas cluster \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:29.134971+00:00
---

# Example: Private connectivity for a MongoDB Atlas cluster  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Example: Private connectivity for a MongoDB Atlas cluster

This page explains how to enable connectivity from Integration Connectors to your MongoDB Atlas cluster running on a private network within Google Cloud. 

## Configure private connectivity for an Atlas cluster

To configure private connectivity for an Atlas cluster, do the following:

  1. Login to your Atlas management console.
  2. Open the Atlas project for which you need to establish the network connectivity.
  3. Open the **Network access** page for the project, and then select **Private endpoint**.
  4. Select **Dedicated Cluster** , and then click **Add private endpoint**. 

This opens the dialog to choose a cloud provider.

**Note:** By default, you can create only one endpoint in each region or multiple endpoints in a single region. You can't create multiple endpoints in multiple regions. To override this behaviour, you must enable [multiple regionalized private endpoints](https://www.mongodb.com/docs/atlas/security-private-endpoint/#-optional--regionalized-private-endpoints-for-multi-region-sharded-clusters).
  5. Select **Google Cloud** , and then click **Next**.
  6. Select an **Atlas region** , and then click **Next**. 

This is the Google Cloud region where your Atlas cluster is created, and it should be the same region as that of the Google Cloud project where you create your connections. For the list of all the supported Integration Connector regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

**Note:** The endpoint that you are creating now, provides access to all the Atlas clusters in the specified region.
  7. Enter the **Google Cloud project ID**. This is the project ID of the service directory from the Integration Connectors runtime. For more information, see Get the project ID of the service directory.
  8. In the **VPC name** field, enter `default`.
  9. In the **Subnet name** field, enter `default`.
  10. In the **Private service connect endpoint prefix** field, enter a prefix. 

This text is prefixed to all the endpoint names and can be used to identify the private endpoints you have created.

  11. Install the `gcloud` CLI (command line interface). For more information, see [Install the gcloud CLI](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb/).
  12. Copy and save the following shell script as `setup_psc.sh` on your local system. 

Set appropriate values for the following variables in the script:

     * PROJECT_ID
     * REGION
     * PREFIX
     * SERVICE_ATTACHMENT_ID_PREFIX
    
    #!/bin/bash
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)"'
    
    # Set PROJECT_ID to the ID of the Google Cloud project where you create your connections.
    export PROJECT_ID=PROJECT_ID
    
    # Set REGION to the Google Cloud region where Atlas cluster is installed.
    export REGION=REGION
    
    export HOSTNAME=https://connectors.googleapis.com/v1
    
    # Set ENDPOINT_PREFIX to the prefix value that you entered for the
    # "Private service connect endpoint prefix" field (in step 10).
    export PREFIX=ENDPOINT_PREFIX
    
    # Set SERVICE_ATTACHMENT_ID_PREFIX to the prefix of the service attachments
    # created by Atlas. The service attachments are present in the script
    # displayed on the Atlas UI and have the following naming format:
    # projects/{google-cloud-project-id-of-atlas-cluster}/regions/{region}/serviceAttachment/{prefix}-{index}
    # For example, if the service attachment is
    # "projects/p-ditnerelrvndieqhe3kh9pop/regions/us-west1/serviceAttachments/sa-us-west1-37204mg5wr0j6-$i",
    # you must set the value of SERVICE_ATTACHMENT_ID_PREFIX to
    # "projects/p-ditnerelrvndieqhe3kh9pop/regions/us-west1/serviceAttachments/sa-us-west1-37204mg5wr0j6"
    export SERVICE_ATTACHMENT_ID_PREFIX=SERVICE_ATTACHMENT_ID_PREFIX
    
    # Set ENDPOINT_GLOBAL_ACCESS to true if you want to enable global access for the endpoint, else false.
    export ENDPOINT_GLOBAL_ACCESS=ENDPOINT_GLOBAL_ACCESS
    
    if [ "$ENDPOINT_GLOBAL_ACCESS" != "true" ] && [ "$ENDPOINT_GLOBAL_ACCESS" != "false" ]; then
        echo "Error: Variable ENDPOINT_GLOBAL_ACCESS must be either 'true' or 'false'."
        exit 1
    fi
    
    function poll_operation() {
      OPERATION_ID="$1"
      INDEX="$2"
      RESULT=''
    
      while [[ "$RESULT" != *"true"* ]];
      do
        RESULT=$(gcurl -s -X GET "${HOSTNAME}/${OPERATION_ID}" | grep '"done"')
        sleep 5
      done
    
      echo "${PREFIX}-${INDEX} created"
    }
    
    echo "Creating Endpoint Attachments..."
    for i in {0..49}
    do
      export ENDPOINT=${HOSTNAME}/projects/${PROJECT_ID}/locations/${REGION}/endpointAttachments?endpointAttachmentId=${PREFIX}-$i
      OPERATION_ID=$(gcurl -s -X POST -H "Content-Type: application/json" -d '{"name": "'"projects/${PROJECT_ID}/locations/${REGION}/endpointAttachments/${PREFIX}-$i"'","serviceAttachment": "'"${SERVICE_ATTACHMENT_ID_PREFIX}-$i"'", "endpointGlobalAccess":'${ENDPOINT_GLOBAL_ACCESS}'}' "${ENDPOINT}" | sed 's/  //' | grep -E '"name"' | sed -E 's/"name": "//' | sed 's/",//')
      poll_operation "$OPERATION_ID" "$i" &
    done
    
    wait
    echo "All endpoint attachments created."
    
    echo "[" > atlasEndpoints-${PREFIX}.json
    
    echo "Fetching IP Addresses..."
    for i in {0..49}
    do
      ENDPOINT=${HOSTNAME}/projects/${PROJECT_ID}/locations/${REGION}/endpointAttachments/${PREFIX}-$i
      response=$(gcurl -s -X GET "${ENDPOINT}" | sed 's/  //g' | grep -E 'name|endpointIp' | sed 's/"endpointIp"/"IPAddress"/g' | sed -E 's/"name": "projects\/.+\/locations\/.+\/endpointAttachments\//"name": "/g' | sed '1 s/"/{"/1')
      if [ "$ENDPOINT_GLOBAL_ACCESS" = "true" ]; then
        echo "${response}" | sed '2 s/"/"}/4' >> atlasEndpoints-${PREFIX}.json
      else
        echo "${response}" | sed '2 s/"/"},/4' >> atlasEndpoints-${PREFIX}.json
      fi
    done
    
    sed -i '$s/,/]/' atlasEndpoints-${PREFIX}.json
    
    echo "Created atlasEndpoints-${PREFIX}.json"

  13. Run the shell script. To run the shell script, go to the directory in which you saved the script, and then run the following command: 
         
         sh setup_psc.sh

This script, generates a JSON file that has the list of IP addresses and their corresponding PSC endpoint names. The JSON file is saved in the directory where the shell script is run.

  14. Click **Next** in the Atlas management console.
  15. Click **Upload JSON file** , and then upload the JSON file that got created in step 13.
  16. Click **Create**. 

The endpoint setup process might take up to 25 minutes to complete, and if the setup is successful, the endpoint will be in the `Available` state.

  17. Verify your private connectivity. For more information, see Verify private connectivity.



## Get the project ID of the service directory

To get the project ID of the service directory, you can use the [List Connections API](https://docs.cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections/list) as shown in the following example.

### Syntax
    
    
    curl -X GET \
        -H "authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://connectors.googleapis.com/v1/projects/CONNECTORS_PROJECT_ID/locations/-/connections"

Replace the following: 

  * CONNECTORS_PROJECT_ID: The ID of your Google Cloud project where you created your connection.



### Example

This example gets the project ID of the service directory for the `connectors-test` Google Cloud project.
    
    
    curl -X GET \
        -H "authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://connectors.googleapis.com/v1/projects/connectors-test/locations/-/connections"

Running this command on the terminal displays an output similar to the following:
    
    
    .....
    {
      "connections": [
        {
          "name": "projects/connectors-test/locations/asia-northeast1/connections/big-query-iam-invalid-sa",
          "createTime": "2022-10-07T09:02:31.905048520Z",
          "updateTime": "2022-10-07T09:22:39.993778690Z",
          "connectorVersion": "projects/connectors-test/locations/global/providers/gcp/connectors/bigquery/versions/1",
          "status": {
            "state": "ACTIVE"
          },
          "configVariables": [
            {
              "key": "project_id",
              "stringValue": "**connectors-test** "
            },
            {
              "key": "dataset_id",
              "stringValue": "testDataset"
            }
          ],
          "authConfig": {},
          "serviceAccount": "564332356444-compute@developer.gserviceaccount.com",
          "serviceDirectory": "projects/**abcdefghijk-tp** /locations/asia-northeast1/namespaces/connectors/services/runtime",
          "nodeConfig": {
            "minNodeCount": 2,
            "maxNodeCount": 50
          }
        },
    ....
    

In the sample output, for the `connectors-test` Google Cloud project, the project ID of the service directory is `abcdefghijk-tp`.

## Verify private connectivity

To verify private connectivity to your Atlas cluster(s) do the following:

  1. In the Atlas management console, open the **Database Deployments** page.
  2. Scroll to the required cluster, and then click **Connect**. This opens the **Connect to <CLUSTER_NAME>** dialog.
  3. Click **Private Endpoint** for connection type.
  4. Select the private endpoint prefix that you had entered in the Atlas UI from the **Choose a private endpoint** drop-down.
  5. Click **Choose a connection method**.
  6. Click **Drivers** in the **Connect to your application** section. This step is to get the `srv` connection string.
  7. Copy the `srv` connection string from the **Add your connection string into your application code** section. 

Format of the `srv` string: `mongodb+srv://{cluster-name}-pl-{index}.{unique-pin}.mongodb.net`.

  8. Create a MongoDB connection by using this `srv` string as the hostname. For more information, see [Configure a MongoDB connector](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/v2/configure#configure-the-connector). 

The connection should be successfully created.

**Note:** When configuring the connection, instead of a `srv` string, you can also enter private hostnames.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
