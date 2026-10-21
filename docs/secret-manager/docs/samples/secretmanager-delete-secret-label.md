---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-delete-secret-label/
title: Delete secret label \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:10.002975+00:00
---

# Delete secret label  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-delete-secret-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Delete secret label Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a label of a secret

## Code sample

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // deleteSecret updates the metadata about an existing secret and remove an existing label.
    func deleteSecretLabel(w io.Writer, name string) error {
    	// name := "projects/my-project/secrets/my-secret"
    
    	labelKey := "labelkey"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request to get the secret.
    	req := &secretmanagerpb.GetSecretRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetSecret(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get secret: %w", err)
    	}
    
    	labels := result.Labels
    
    	delete(labels, labelKey)
    
    	// Build the request to update the secret.
    	updateReq := &secretmanagerpb.UpdateSecretRequest{
    		Secret: &secretmanagerpb.Secret{
    			Name:   name,
    			Labels: labels,
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"labels"},
    		},
    	}
    
    	// Call the API.
    	updateResult, err := client.UpdateSecret(ctx, updateReq)
    	if err != nil {
    		return fmt.Errorf("failed to update secret: %w", err)
    	}
    	fmt.Fprintf(w, "Updated secret: %s\n", updateResult.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.[FieldMaskOrBuilder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class DeleteSecretLabel {
    
      public static void deleteSecretLabel() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // This is the id of the GCP project
        String projectId = "your-project-id";
        // This is the id of the secret to act on
        String secretId = "your-secret-id";
        // This is the key of the label to be deleted
        String labelKey = "your-label-key";
        deleteSecretLabel(projectId, secretId, labelKey);
      }
    
      // Update an existing secret, by deleting a label.
      public static [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) deleteSecretLabel(
                         String projectId, String secretId, String labelKey) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).of(projectId, secretId);
    
          // Get the existing secret
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) existingSecret = client.getSecret(secretName);
    
          Map<String, String> existingLabelsMap = 
                  new HashMap<String, String>(existingSecret.[getLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getLabels__)());
          existingLabelsMap.remove(labelKey);
    
          // Build the updated secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                  .setName(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)())
                  .[putAllLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_putAllLabels_java_util_Map_java_lang_String_java_lang_String__)(existingLabelsMap)
                  .build();
    
          // Build the field mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("labels");
    
          // Update the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) updatedSecret = client.updateSecret(secret, fieldMask);
          System.out.printf("Updated secret %s\n", updatedSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)());
    
          return updatedSecret;
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const name = 'projects/my-project/secrets/my-secret';
    // const labelKey = 'secretmanager';
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    async function getSecret() {
      const [secret] = await client.getSecret({
        name: name,
      });
    
      return secret;
    }
    
    async function deleteSecretLabel() {
      const oldSecret = await getSecret();
      delete oldSecret.labels[labelKey];
      const [secret] = await client.updateSecret({
        secret: {
          name: name,
          labels: oldSecret.labels,
        },
        updateMask: {
          paths: ['labels'],
        },
      });
    
      console.info(`Updated secret ${secret.name}`);
    }
    
    deleteSecretLabel();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\GetSecretRequest;
    use Google\Cloud\SecretManager\V1\Secret;
    use Google\Cloud\SecretManager\V1\UpdateSecretRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     * @param string $labelKey  Your label key (e.g. 'label-key')
     */
    function delete_secret_label(string $projectId, string $secretId, string $labelKey): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the parent project.
        $name = $client->secretName($projectId, $secretId);
    
        // Build the request.
        $request = GetSecretRequest::build($name);
    
        // get the secret.
        $getSecret = $client->getSecret($request);
    
        // get the secret labels
        $labels = $getSecret->getLabels();
    
        // delete the label
        unset($labels[$labelKey]);
    
        // set the field mask
        $fieldMask = new FieldMask();
        $fieldMask->setPaths(['labels']);
    
        // build the secret
        $secret = new Secret();
        $secret->setLabels($labels);
        $secret->setName($getSecret->getName());
    
        // build the request
        $request = new UpdateSecretRequest();
        $request->setSecret($getSecret);
        $request->setUpdateMask($fieldMask);
    
        // update the secret
        $updateSecret = $client->updateSecret($request);
    
        // print the secret name
        printf('Updated secret %s' . PHP_EOL, $updateSecret->getName());
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    
    
    def delete_secret_label(
        project_id: str, secret_id: str, label_key: str
    ) -> secretmanager.UpdateSecretRequest:
        """
        Delete a label on an existing secret.
        """
    
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Build the resource name of the secret.
        name = client.[secret_path](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_secret_path)(project_id, secret_id)
    
        # Get the secret.
        response = client.[get_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_get_secret)(request={"name": name})
    
        labels = response.labels
    
        # Delete the label
        labels.pop(label_key, None)
    
        # Update the secret.
        secret = {"name": name, "labels": labels}
        update_mask = {"paths": ["labels"]}
        response = client.[update_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_update_secret)(
            request={"secret": secret, "update_mask": update_mask}
        )
    
        # Print the new secret name.
        print(f"Updated secret: {response.name}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
