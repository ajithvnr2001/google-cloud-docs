---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-your-first-confidential-space-environment/
title: Create your first Confidential Space environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:46:45.744239+00:00
---

# Create your first Confidential Space environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-your-first-confidential-space-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)



Send feedback 

#  Create your first Confidential Space environment Stay organized with collections  Save and categorize content based on your preferences. 

[ Data collaborators ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles) [ Workload author ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles) [ Workload operator ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles)

In this guide, Alex and Bola want to find out who has the highest salary without revealing numbers to each other. They decide to use Confidential Space to keep their data confidential, and agree to take on the following [roles](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles):

  * **Alex:** Data collaborator, workload author

  * **Bola:** Data collaborator, workload operator




This arrangement is designed to keep things as straightforward as possible for this guide. However, it's possible for the workload author and operator to be entirely independent from the data collaborators, and you can have as many collaborators as you want.

## Before you begin

This guide demonstrates a Confidential Space scenario using a single account in a single organization with access to multiple projects, so you can experience the whole process. In a production deployment, collaborators, workload authors, and workload operators have separate accounts and their own projects contained in discrete organizations, inaccessible to each other and keeping their confidential data separate.

Confidential Space can interact with many of Google Cloud's services to produce its results, including but not limited to:

  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry)

  * [Cloud Storage](https://docs.cloud.google.com/storage)

  * [Cloud Key Management Service](https://docs.cloud.google.com/kms)

  * [Compute Engine](https://docs.cloud.google.com/compute)

  * [Cloud Logging](https://docs.cloud.google.com/logging)

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)

  * [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation)




This guide makes use of and assumes a basic understanding of all of these features.

### Required roles

To get the permissions that you need to complete this guide, ask your administrator to grant you the following IAM roles on the project: 

  * Cloud KMS Admin (`roles/cloudkms.admin`) for the data collaborators (Alex and Bola). 
  * IAM Workload Identity Pool Admin (`roles/iam.workloadIdentityPoolAdmin`) for the data collaborators (Alex and Bola). 
  * Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) for the data collaborators (Alex and Bola). 
  * Storage Admin (`roles/storage.admin`) for the data collaborators (Alex and Bola) and the workload operator (Bola). 
  * Service Account Admin (`roles/iam.serviceAccountAdmin`) for the workload operator (Bola). 
  * Compute Admin (`roles/compute.admin`) for the workload operator (Bola). 
  * Security Admin (`roles/securityAdmin`) for the workload operator (Bola). 
  * Artifact Registry Administrator (`roles/artifactregistry.admin`) for the workload author (Alex). 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up data collaborator resources

Both Alex and Bola need independent projects that contain the following resources:

  * The confidential data itself.

  * An encryption key to encrypt that data and keep it confidential.

  * A Cloud Storage bucket to store the encrypted data in.

  * A [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation). The workload processing the confidential data uses the pool to access the private data and decrypt it.




To get started, go to the Google Cloud console:

[Go to Google Cloud console](https://console.cloud.google.com/)

### Set up Alex's resources

To set up the resources for Alex, complete the following instructions.

  1. Click terminal **Activate Cloud Shell**.
  2. In Cloud Shell, enter the following command to create a project for Alex, replacing ALEX_PROJECT_ID with a name of your choice:
         
         gcloud projects create ALEX_PROJECT_ID

  3. Switch to the newly created project:
         
         gcloud config set project ALEX_PROJECT_ID

  4. Enable the APIs that Alex requires as a data collaborator and workload author:
         
         gcloud services enable \
             artifactregistry.googleapis.com \
             cloudkms.googleapis.com \
             iamcredentials.googleapis.com

  5. Create a key ring and encryption key with Cloud Key Management Service:
         
         gcloud kms keyrings create ALEX_KEYRING_NAME \
             --location=global
         
         gcloud kms keys create ALEX_KEY_NAME \
             --location=global \
             --keyring=ALEX_KEYRING_NAME \
             --purpose=encryption

  6. Grant Alex the `cloudkms.cryptoKeyEncrypter` role so they can use the newly created encryption key to encrypt data:
         
         gcloud kms keys add-iam-policy-binding \
             "projects/ALEX_PROJECT_ID/locations/global/\
         keyRings/ALEX_KEYRING_NAME/\
         cryptoKeys/ALEX_KEY_NAME" \
             --member=user:$(gcloud config get-value account) \
             --role=roles/cloudkms.cryptoKeyEncrypter

  7. Create Alex's workload identity pool:
         
         gcloud iam workload-identity-pools create ALEX_POOL_NAME \
             --location=global

  8. Create a Cloud Storage bucket for the input data, and another to store the results in:
         
         gcloud storage buckets create gs://ALEX_INPUT_BUCKET_NAME \
             gs://ALEX_OUTPUT_BUCKET_NAME

  9. Create a file that contains only Alex's salary as a number:
         
         echo 123456 > ALEX_SALARY.txt

  10. Encrypt the file, and then upload it to Alex's bucket:
         
         gcloud kms encrypt \
             --ciphertext-file="ALEX_ENCRYPTED_SALARY_FILE" \
             --plaintext-file="ALEX_SALARY.txt" \
             --key="projects/ALEX_PROJECT_ID/locations/global/\
         keyRings/ALEX_KEYRING_NAME/\
         cryptoKeys/ALEX_KEY_NAME"
         
         gcloud storage cp ALEX_ENCRYPTED_SALARY_FILE gs://ALEX_INPUT_BUCKET_NAME




### Set up Bola's resources

To set up the resources for Bola, complete the following instructions.

  1. In Cloud Shell, enter the following command to create a project for Bola, replacing BOLA_PROJECT_ID with a name of your choice:
         
         gcloud projects create BOLA_PROJECT_ID

  2. Switch to the newly created project:
         
         gcloud config set project BOLA_PROJECT_ID

  3. Enable the APIs that Bola requires as a data collaborator and workload operator:
         
         gcloud services enable \
             cloudkms.googleapis.com \
             compute.googleapis.com \
             confidentialcomputing.googleapis.com \
             iamcredentials.googleapis.com

  4. Create a key ring and encryption key with Cloud Key Management Service:
         
         gcloud kms keyrings create BOLA_KEYRING_NAME \
             --location=global
         
         gcloud kms keys create BOLA_KEY_NAME \
             --location=global \
             --keyring=BOLA_KEYRING_NAME \
             --purpose=encryption

  5. Grant Bola the `cloudkms.cryptoKeyEncrypter` role so they can use the newly created encryption key to encrypt data:
         
         gcloud kms keys add-iam-policy-binding \
             "projects/BOLA_PROJECT_ID/locations/global/\
         keyRings/BOLA_KEYRING_NAME/\
         cryptoKeys/BOLA_KEY_NAME" \
             --member=user:$(gcloud config get-value account) \
             --role=roles/cloudkms.cryptoKeyEncrypter

  6. Create Bola's workload identity pool:
         
         gcloud iam workload-identity-pools create BOLA_POOL_NAME \
             --location=global

  7. Create a Cloud Storage bucket for the input data, and another to store the results in:
         
         gcloud storage buckets create gs://BOLA_INPUT_BUCKET_NAME \
             gs://BOLA_OUTPUT_BUCKET_NAME

  8. Create a file that contains only Bola's salary as a number:
         
         echo 111111 > BOLA_SALARY.txt

  9. Encrypt the file, and then upload it to Bola's bucket:
         
         gcloud kms encrypt \
             --ciphertext-file="BOLA_ENCRYPTED_SALARY_FILE" \
             --plaintext-file="BOLA_SALARY.txt" \
             --key="projects/BOLA_PROJECT_ID/locations/global/\
         keyRings/BOLA_KEYRING_NAME/\
         cryptoKeys/BOLA_KEY_NAME"
         
         gcloud storage cp BOLA_ENCRYPTED_SALARY_FILE gs://BOLA_INPUT_BUCKET_NAME




## Create a service account for the workload

In this guide, Bola operates and runs the workload, but anyone can take on these roles, including a third party. The VM instance Bola creates to run the workload has a service account attached, which has permission to generate attestation tokens, write logs, read Alex and Bola's encrypted data, and write results to specific Cloud Storage buckets.

Complete the following steps in Bola's project to set up the service account:

  1. Create a service account to run the workload:
         
         gcloud iam service-accounts create WORKLOAD_SERVICE_ACCOUNT_NAME
         

  2. Grant Bola the `iam.serviceAccountUser` role, so they can attach the service account to the workload VM later:
         
         gcloud iam service-accounts add-iam-policy-binding \
             WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --member=user:$(gcloud config get-value account) \
             --role=roles/iam.serviceAccountUser
         

  3. Grant the service account the `confidentialcomputing.workloadUser` role so it can request an attestation token:
         
         gcloud projects add-iam-policy-binding BOLA_PROJECT_ID \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/confidentialcomputing.workloadUser
         

  4. Grant the service account the `logging.logWriter` role to write logs to Cloud Logging, so you can check the progress of the workload:
         
         gcloud projects add-iam-policy-binding BOLA_PROJECT_ID \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/logging.logWriter
         

  5. Give the service account read access to both Alex and Bola's buckets that contain their encrypted data, and write access to each of their results buckets:
         
         gcloud storage buckets add-iam-policy-binding gs://ALEX_INPUT_BUCKET_NAME \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/storage.objectViewer
         
         gcloud storage buckets add-iam-policy-binding gs://ALEX_OUTPUT_BUCKET_NAME \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/storage.objectAdmin
         
         gcloud storage buckets add-iam-policy-binding gs://BOLA_INPUT_BUCKET_NAME \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/storage.objectViewer
         
         gcloud storage buckets add-iam-policy-binding gs://BOLA_OUTPUT_BUCKET_NAME \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/storage.objectAdmin
         

This assumes the user granting the access has the Storage Admin (`roles/storage.admin`) role for the project that contains the Cloud Storage bucket that's being operated on.




## Create the workload

In this guide, Alex provides the code for the workload and builds a Docker image to contain it, but anyone can take on these roles, including a third party.

Alex needs to create the following resources for the workload:

  * The code that performs the workload.

  * A Docker repository in Artifact Registry, that the service account running the workload has access to.

  * A Docker image that contains and runs the workload code.




To create and set up the resources, complete the following steps in Alex's project:

  1. Switch to Alex's project:
         
         gcloud config set project ALEX_PROJECT_ID
         

  2. Click **Open editor** to open the Cloud Shell Editor, and then create a new file called `salary.go`. Copy the following code into the file, and then save it:
         
         package main
         
         import (
           "context"
           "fmt"
           "io"
           "os"
           "strconv"
           "strings"
           "time"
         
           kms "cloud.google.com/go/kms/apiv1"
           kmspb "cloud.google.com/go/kms/apiv1/kmspb"
           "cloud.google.com/go/storage"
           "google.golang.org/api/option"
         )
         
         type collaborator struct {
           name         string
           wipName      string
           keyName      string
           inputBucket  string
           inputFile    string
           outputBucket string
         }
         
         // The following values are pulled from environment variables
         
         // Alex's values
         var collaborator1Name string = os.Getenv("COLLAB_1_NAME") // Alex's name
         var collaborator1EncryptedSalaryFileName string = os.Getenv("COLLAB_1_ENCRYPTED_SALARY") // The name of Alex's encrypted salary file.
         var collaborator1BucketInputName string = os.Getenv("COLLAB_1_INPUT_BUCKET") // The name of the storage bucket that contains Alex's encrypted salary file.
         var collaborator1BucketOutputName string = os.Getenv("COLLAB_1_OUTPUT_BUCKET") // The name of the storage bucket to store Alex's results in.
         var collaborator1KMSKeyringName string = os.Getenv("COLLAB_1_KEYRING_NAME") // Alex's Key Management Service key ring.
         var collaborator1KMSKeyName string = os.Getenv("COLLAB_1_KEY_NAME") // Alex's Key Management Service key.
         var collaborator1ProjectName string = os.Getenv("COLLAB_1_PROJECT_ID") // Alex's project ID.
         var collaborator1ProjectNumber string = os.Getenv("COLLAB_1_PROJECT_NUMBER") // Alex's project number.
         var collaborator1PoolName string = os.Getenv("COLLAB_1_POOL_NAME") // Alex's workload identity pool name.
         
         // Bola's values
         var collaborator2Name string = os.Getenv("COLLAB_2_NAME") // Bola's name
         var collaborator2EncryptedSalaryFileName string = os.Getenv("COLLAB_2_ENCRYPTED_SALARY") // The name of Bola's encrypted salary file.
         var collaborator2BucketInputName string = os.Getenv("COLLAB_2_INPUT_BUCKET") // The name of the storage bucket that contains Bola's encrypted salary file.
         var collaborator2BucketOutputName string = os.Getenv("COLLAB_2_OUTPUT_BUCKET") // The name of the storage bucket to store Bola's results in.
         var collaborator2KMSKeyringName string = os.Getenv("COLLAB_2_KEYRING_NAME") // Bola's Key Management Service key ring.
         var collaborator2KMSKeyName string = os.Getenv("COLLAB_2_KEY_NAME") // Bola's Key Management Service key.
         var collaborator2ProjectName string = os.Getenv("COLLAB_2_PROJECT_ID") // Bola's project ID.
         var collaborator2ProjectNumber string = os.Getenv("COLLAB_2_PROJECT_NUMBER") // Bola's project number.
         var collaborator2PoolName string = os.Getenv("COLLAB_2_POOL_NAME") // Bola's workload identity pool name.
         
         var collaborators = [2]collaborator{
           {
             collaborator1Name,
             "projects/" + collaborator1ProjectNumber + "/locations/global/workloadIdentityPools/" + collaborator1PoolName + "/providers/attestation-verifier",
             "projects/" + collaborator1ProjectName + "/locations/global/keyRings/" + collaborator1KMSKeyringName + "/cryptoKeys/" + collaborator1KMSKeyName,
             collaborator1BucketInputName,
             collaborator1EncryptedSalaryFileName,
             collaborator1BucketOutputName,
           },
           {
             collaborator2Name,
             "projects/" + collaborator2ProjectNumber + "/locations/global/workloadIdentityPools/" + collaborator2PoolName + "/providers/attestation-verifier",
             "projects/" + collaborator2ProjectName + "/locations/global/keyRings/" + collaborator2KMSKeyringName + "/cryptoKeys/" + collaborator2KMSKeyName,
             collaborator2BucketInputName,
             collaborator2EncryptedSalaryFileName,
             collaborator2BucketOutputName,
           },
         }
         
         const credentialConfig = `{
                 "type": "external_account",
                 "audience": "//iam.googleapis.com/%s",
                 "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
                 "token_url": "https://sts.googleapis.com/v1/token",
                 "credential_source": {
                   "file": "/run/container_launcher/attestation_verifier_claims_token"
                 }
                 }`
         
         func main() {
           fmt.Println("workload started")
           ctx := context.Background()
         
           storageClient, err := storage.NewClient(ctx) // Using the default credential on the Compute Engine VM
           if err != nil {
             panic(err)
           }
         
           // Get and decrypt
           s0, err := getSalary(ctx, storageClient, collaborators[0])
           if err != nil {
             panic(err)
           }
         
           s1, err := getSalary(ctx, storageClient, collaborators[1])
           if err != nil {
             panic(err)
           }
         
           res := ""
           if s0 > s1 {
             res = fmt.Sprintf("%s earns more!\n", collaborators[0].name)
           } else if s1 > s0 {
             res = fmt.Sprintf("%s earns more!\n", collaborators[1].name)
           } else {
             res = "You earn the same!\n"
           }
         
           now := time.Now()
           for _, cw := range collaborators {
             outputWriter := storageClient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(cw.outputBucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(fmt.Sprintf("comparison-result-%d", now.Unix())).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
         
             _, err = output[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)r.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte(res))
             if err != nil {
               fmt.Printf("Could not write: %v", err)
               panic(err)
             }
             if err = outputWriter.Close(); err != nil {
               fmt.Printf("Could not close: %v", err)
               panic(err)
             }
           }
         }
         
         func getSalary(ctx context.Context, storageClient *storage.Client, cw collaborator) (float64, error) {
           encryptedBytes, err := getFile(ctx, storageClient, cw.inputBucket, cw.inputFile)
           if err != nil {
             return 0.0, err
           }
           decryptedByte, err := decryptByte(ctx, cw.keyName, cw.wipName, encryptedBytes)
           if err != nil {
             return 0.0, err
           }
           decryptedNumber := strings.TrimSpace(string(decryptedByte))
           num, err := strconv.ParseFloat(decryptedNumber, 64)
           if err != nil {
             return 0.0, err
           }
           return num, nil
         }
         
         func decryptByte(ctx context.Context, keyName, wippro string, encryptedData []byte) ([]byte, error) {
           cc := fmt.Sprintf(credentialConfig, wippro)
           kmsClient, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx, option.WithCredentialsJSON([]byte(cc)))
           if err != nil {
             return nil, fmt.Errorf("creating a new KMS client with federated credentials: %w", err)
           }
         
           decryptRequest := &kmspb.DecryptRequest{
             Name:       keyName,
             Ciphertext: encryptedData,
           }
           decryptResponse, err := kmsClient.Decrypt(ctx, decryptRequest)
           if err != nil {
             return nil, fmt.Errorf("could not decrypt ciphertext: %w", err)
           }
         
           return decryptResponse.Plaintext, nil
         }
         
         func getFile(ctx context.Context, c *storage.Client, bucketName string, objPath string) ([]byte, error) {
           bucketHandle := c.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
           objectHandle := bucketHandle.[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(objPath)
         
           objectReader, err := objectHandle.[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
           if err != nil {
             return nil, err
           }
           defer objectReader.Close()
         
           s, err := io.ReadAll(objectReader)
           if err != nil {
             return nil, err
           }
         
           return s, nil
         }
         

  3. Make sure that all parties read and audit the source code.

  4. Create a file named `Dockerfile` in Cloud Shell Editor containing the following contents:
         
         # Compile the provided Go code to a statically linked binary
         FROM golang:latest AS build
         WORKDIR /build
         COPY salary.go .
         RUN go mod init salary
         RUN go get cloud.google.com/go/kms/apiv1 cloud.google.com/go/storage google.golang.org/api/option google.golang.org/genproto/googleapis/cloud/kms/v1
         RUN CGO_ENABLED=0 go build -trimpath
         
         # Build the workload container image
         FROM alpine:latest AS run
         WORKDIR /test
         COPY --from=build /build/salary /test/salary
         ENTRYPOINT ["/test/salary"]
         CMD []
         
         # Allow the workload to access the following environment variables
         LABEL "tee.launch_policy.allow_env_override"="\
         COLLAB_1_NAME,\
         COLLAB_2_NAME,\
         COLLAB_1_ENCRYPTED_SALARY,\
         COLLAB_2_ENCRYPTED_SALARY,\
         COLLAB_1_INPUT_BUCKET,\
         COLLAB_2_INPUT_BUCKET,\
         COLLAB_1_OUTPUT_BUCKET,\
         COLLAB_2_OUTPUT_BUCKET,\
         COLLAB_1_KEYRING_NAME,\
         COLLAB_2_KEYRING_NAME,\
         COLLAB_1_KEY_NAME,\
         COLLAB_2_KEY_NAME,\
         COLLAB_1_PROJECT_ID,\
         COLLAB_2_PROJECT_ID,\
         COLLAB_1_PROJECT_NUMBER,\
         COLLAB_2_PROJECT_NUMBER,\
         COLLAB_1_POOL_NAME,\
         COLLAB_2_POOL_NAME"
         

This `Dockerfile` uses a multi-stage build to first compile the Go code, and then copies the compiled version of that code to the final workload container. It also [allows specific environment variables](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/launch-policies#allow-env-override) to be used in that workload container. Values for these environment variables are mapped later to the specific resources that the workload needs to operate on.

  5. Click **Open Terminal** to switch back to Cloud Shell, or invoke the terminal built into Cloud Shell Editor from the **View** menu.

  6. Create a Docker repository in Artifact Registry:
         
         gcloud artifacts repositories create REPOSITORY_NAME \
             --repository-format=docker \
             --location=us
         

  7. Grant the service account that's going to run the workload the Artifact Registry Reader (`roles/artifactregistry.reader`) role so it can read from the repository:
         
         gcloud artifacts repositories add-iam-policy-binding REPOSITORY_NAME \
             --location=us \
             --member=serviceAccount:WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/artifactregistry.reader
         

  8. Update your Docker credentials to include the `us-docker.pkg.dev` domain name:
         
         gcloud auth configure-docker us-docker.pkg.dev
         

  9. Create a Docker image from `Dockerfile` by entering the following command in the terminal:
         
         docker build -t \
             "us-docker.pkg.dev/ALEX_PROJECT_ID/\
         REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest" .
         

  10. Push the Docker image to Artifact Registry:
         
         docker push \
             us-docker.pkg.dev/ALEX_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME
         

  11. The Docker push response lists the image's SHA256 digest, which is needed later to authorize the workload. The digest looks similar to the following example:
         
         sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
         

Copy the image digest (including the `sha256:` prefix) somewhere you can reference it. You can also enter the digest in the following code sample to prefill the rest of the code samples in this guide that need the value:
         
         WORKLOAD_CONTAINER_IMAGE_DIGEST
         

  12. Make sure all parties audit the Docker image and verify that it's trustworthy before authorizing its use.




## Authorize the workload

With the workload approved by both parties, Alex and Bola need to add Google Cloud Attestation as a [provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation#providers) to their workload identity pools. The provider specifies the attestation service to use, and the properties the workload must match for it to be allowed to operate on Alex's or Bola's data. If a malicious actor changes the Docker image, or alters another measured property, the workload is denied access.

This guide uses [attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) to provide direct resource access to the workload based on the image digest. However, for other situations you may prefer to use service account impersonation to access the resources. See [External workload access](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources#external-access-methods) to learn more.

To set up the providers for Alex and Bola with the required conditions, complete the following steps:

  1. Enter the following command to create the provider for Alex:
         
         gcloud iam workload-identity-pools providers create-oidc attestation-verifier \
             --location=global \
             --workload-identity-pool=ALEX_POOL_NAME \
             --issuer-uri="https://confidentialcomputing.googleapis.com/" \
             --allowed-audiences="https://sts.googleapis.com" \
             --attribute-mapping="google.subject=\"gcpcs\
         ::\"+assertion.submods.container.image_digest+\"\
         ::\"+assertion.submods.gce.project_number+\"\
         ::\"+assertion.submods.gce.instance_id,\
         attribute.image_digest=assertion.submods.container.image_digest" \
             --attribute-condition="assertion.swname == 'CONFIDENTIAL_SPACE'"
         

  2. Get Alex's project number for the next command:
         
         gcloud projects describe ALEX_PROJECT_ID --format="value(projectNumber)"
         

  3. Grant the federated identity defined by Alex's provider the `cloudkms.cryptoKeyDecrypter` role, specifying the `image_digest` attribute so only workload containers with the specified digest can decrypt their KMS keys:
         
         gcloud kms keys add-iam-policy-binding \
             "projects/ALEX_PROJECT_ID/locations/global/\
         keyRings/ALEX_KEYRING_NAME/\
         cryptoKeys/ALEX_KEY_NAME" \
             --member="principalSet://iam.googleapis.com/\
         projects/ALEX_PROJECT_NUMBER/locations/global/\
         workloadIdentityPools/ALEX_POOL_NAME/\
         attribute.image_digest/WORKLOAD_CONTAINER_IMAGE_DIGEST" \
             --role=roles/cloudkms.cryptoKeyDecrypter
         

  4. Switch to Bola's project:
         
         gcloud config set project BOLA_PROJECT_ID
         

  5. Enter the following command to create the provider for Bola:
         
         gcloud iam workload-identity-pools providers create-oidc attestation-verifier \
             --location=global \
             --workload-identity-pool=BOLA_POOL_NAME \
             --issuer-uri="https://confidentialcomputing.googleapis.com/" \
             --allowed-audiences="https://sts.googleapis.com" \
             --attribute-mapping="google.subject=\"gcpcs\
         ::\"+assertion.submods.container.image_digest+\"\
         ::\"+assertion.submods.gce.project_number+\"\
         ::\"+assertion.submods.gce.instance_id,\
         attribute.image_digest=assertion.submods.container.image_digest" \
             --attribute-condition="assertion.swname == 'CONFIDENTIAL_SPACE'"
         

  6. Get Bola's project number for the next command:
         
         gcloud projects describe BOLA_PROJECT_ID --format="value(projectNumber)"
         

  7. Grant the federated identity defined by Bola's provider the `cloudkms.cryptoKeyDecrypter` role, specifying the `image_digest` attribute so only workload containers with the specified digest can decrypt their KMS keys:
         
         gcloud kms keys add-iam-policy-binding \
             "projects/BOLA_PROJECT_ID/locations/global/\
         keyRings/BOLA_KEYRING_NAME/\
         cryptoKeys/BOLA_KEY_NAME" \
             --member="principalSet://iam.googleapis.com/\
         projects/BOLA_PROJECT_NUMBER/locations/global/\
         workloadIdentityPools/BOLA_POOL_NAME/\
         attribute.image_digest/WORKLOAD_CONTAINER_IMAGE_DIGEST" \
             --role=roles/cloudkms.cryptoKeyDecrypter
         




## Test the workload

With providers added to both Alex and Bola's workload identity pools and the required resources in place, it's time for the workload operator to test the workload.

To test the workload, you create a new Confidential VM instance in Bola's project that has the following properties:

  * A [supported configuration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations) with AMD SEV, Intel TDX, or Intel TDX with NVIDIA Confidential Computing.

  * Secure Boot enabled.

  * An OS based on the [Confidential Space debug image](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images), to make troubleshooting easier.

  * A reference to the Docker image that Alex created earlier. This is loaded on top of the Confidential Space image.

  * An attached service account that Bola created earlier, that runs the workload.

  * `STDOUT` and `STDERR` redirected to both Cloud Logging and the serial console.

  * The resource details the workload needs set as environment variables.




Enter the following command in Bola's Cloud Shell to test the workload:
    
    
    gcloud compute instances create WORKLOAD_VM_2_NAME \
        --confidential-compute-type=SEV \
        --shielded-secure-boot \
        --scopes=cloud-platform \
        --zone=us-west1-b \
        --maintenance-policy=MIGRATE \
        --min-cpu-platform="AMD Milan" \
        --image-project=confidential-space-images \
        --image-family=confidential-space-debug \
        --service-account=WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
        --metadata="^~^tee-image-reference=us-docker.pkg.dev/\
    ALEX_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest\
    ~tee-container-log-redirect=true\
    ~tee-env-COLLAB_1_NAME=Alex\
    ~tee-env-COLLAB_2_NAME=Bola\
    ~tee-env-COLLAB_1_ENCRYPTED_SALARY=ALEX_ENCRYPTED_SALARY_FILE\
    ~tee-env-COLLAB_2_ENCRYPTED_SALARY=BOLA_ENCRYPTED_SALARY_FILE\
    ~tee-env-COLLAB_1_INPUT_BUCKET=ALEX_INPUT_BUCKET_NAME\
    ~tee-env-COLLAB_2_INPUT_BUCKET=BOLA_INPUT_BUCKET_NAME\
    ~tee-env-COLLAB_1_OUTPUT_BUCKET=ALEX_OUTPUT_BUCKET_NAME\
    ~tee-env-COLLAB_2_OUTPUT_BUCKET=BOLA_OUTPUT_BUCKET_NAME\
    ~tee-env-COLLAB_1_KEYRING_NAME=ALEX_KEYRING_NAME\
    ~tee-env-COLLAB_2_KEYRING_NAME=BOLA_KEYRING_NAME\
    ~tee-env-COLLAB_1_KEY_NAME=ALEX_KEY_NAME\
    ~tee-env-COLLAB_2_KEY_NAME=BOLA_KEY_NAME\
    ~tee-env-COLLAB_1_PROJECT_ID=ALEX_PROJECT_ID\
    ~tee-env-COLLAB_2_PROJECT_ID=BOLA_PROJECT_ID\
    ~tee-env-COLLAB_1_PROJECT_NUMBER=ALEX_PROJECT_NUMBER\
    ~tee-env-COLLAB_2_PROJECT_NUMBER=BOLA_PROJECT_NUMBER\
    ~tee-env-COLLAB_1_POOL_NAME=ALEX_POOL_NAME\
    ~tee-env-COLLAB_2_POOL_NAME=BOLA_POOL_NAME"
    

**Note:** For more sensitive data or to make managing environment variables easier, instead of using `~tee-env-` as part of the VM instance metadata you can store the needed values somewhere like [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

### View progress

You can view the progress of the workload in Bola's project by going to **Logs explorer**.

[Go to Logs explorer](https://console.cloud.google.com/logs/)

To only show Confidential Space log entries, filter by the following **Log fields** , if they're available:

  * **Resource type:** VM Instance

  * **Instance ID:** The instance ID of the VM

  * **Log name:** confidential-space-launcher




To refresh the log, click keyboard_tab **Jump to now**. You can also scroll to earlier results, and then scroll to the end of the log again to load the latest entries.

### View the results

If the workload task ends and returns `0`, this means no errors have occurred and it's time to check the output in Alex's and Bola's output buckets:

  1. Switch to Alex's project:
         
         gcloud config set project ALEX_PROJECT_ID
         

  2. List all the files in their results bucket:
         
         gcloud storage ls gs://ALEX_OUTPUT_BUCKET_NAME
         

  3. Read the latest file that is listed, replacing `ALEX_OUTPUT_CLOUD_STORAGE_PATH` with the path of the file, including the `gs://`:
         
         gcloud storage cat ALEX_OUTPUT_CLOUD_STORAGE_PATH
         

If no file is present, then you need to debug your workload.

  4. Switch to Bola's project:
         
         gcloud config set project BOLA_PROJECT_ID
         

  5. List all the files in their results bucket:
         
         gcloud storage ls gs://BOLA_OUTPUT_BUCKET_NAME
         

  6. Read the latest file that is listed, replacing `BOLA_RESULTS_CLOUD_STORAGE_PATH` with the path of the file, including the `gs://`:
         
         gcloud storage cat BOLA_RESULTS_CLOUD_STORAGE_PATH
         

If no file is present, then you need to debug your workload.

  7. After you've successfully read the results, stop the VM instance:
         
         gcloud compute instances stop WORKLOAD_VM_2_NAME --zone=us-west1-b
         




By reading the files, Alex and Bola each discover who earns more without ever revealing their salaries to each other.

### Debug and restart the workload

A Confidential Space environment has many parts, and it's possible that something has been configured incorrectly that causes the workload to fail.

Unlike the production Confidential Space image, the debug image keeps the VM instance running after the workload has finished. This means that, if the logs don't reveal enough to solve your problem, the next step is to connect to your VM instance over SSH and [continue debugging](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/monitor-debug).

After you've finished debugging, stop the VM instance:
    
    
    gcloud compute instances stop WORKLOAD_VM_2_NAME --zone=us-west1-b
    

To run the workload against the debugged environment, start the VM again:
    
    
    gcloud compute instances start WORKLOAD_VM_2_NAME --zone=us-west1-b
    

## Harden the environment for production

After you've successfully tested the workload, it's time to harden the Confidential Space environment for production deployment. Alex and Bola need to add a [`support_attributes` assertion](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/attestation-assertions#support_attributes) to their providers to verify that the production Confidential Space image is used for the workload:

  1. Switch to Alex's project:
         
         gcloud config set project ALEX_PROJECT_ID
         

  2. Enter the following command to update the provider for Alex:
         
         gcloud iam workload-identity-pools providers update-oidc attestation-verifier \
             --location=global \
             --workload-identity-pool=ALEX_POOL_NAME \
             --issuer-uri="https://confidentialcomputing.googleapis.com/" \
             --allowed-audiences="https://sts.googleapis.com" \
             --attribute-mapping="google.subject=\"gcpcs\
         ::\"+assertion.submods.container.image_digest+\"\
         ::\"+assertion.submods.gce.project_number+\"\
         ::\"+assertion.submods.gce.instance_id,\
         attribute.image_digest=assertion.submods.container.image_digest" \
             --attribute-condition="assertion.swname == 'CONFIDENTIAL_SPACE' \
                 **& & 'STABLE' in assertion.submods.confidential_space.support_attributes**"
         

  3. Switch to Bola's project:
         
         gcloud config set project BOLA_PROJECT_ID
         

  4. Enter the following command to update the provider for Bola:
         
         gcloud iam workload-identity-pools providers update-oidc attestation-verifier \
             --location=global \
             --workload-identity-pool=BOLA_POOL_NAME \
             --issuer-uri="https://confidentialcomputing.googleapis.com/" \
             --allowed-audiences="https://sts.googleapis.com" \
             --attribute-mapping="google.subject=\"gcpcs\
         ::\"+assertion.submods.container.image_digest+\"\
         ::\"+assertion.submods.gce.project_number+\"\
         ::\"+assertion.submods.gce.instance_id,\
         attribute.image_digest=assertion.submods.container.image_digest" \
             --attribute-condition="assertion.swname == 'CONFIDENTIAL_SPACE' \
                 **& & 'STABLE' in assertion.submods.confidential_space.support_attributes**"
         




## Deploy the production workload

Bola needs to create a separate VM instance to run the production workload. The following things are different compared to the test workload:

  * The OS is based on the production Confidential Space image. This has SSH disabled, and the VM instance stops after the workload finishes.

  * Logging redirection is removed. Only basic logs that expose no sensitive information are shown in Cloud Logging.




Enter the following command in Bola's Cloud Shell to deploy the production workload:
    
    
    gcloud compute instances create WORKLOAD_VM_NAME \
        --confidential-compute-type=SEV \
        --shielded-secure-boot \
        --scopes=cloud-platform \
        --zone=us-west1-b \
        --maintenance-policy=MIGRATE \
        --image-project=confidential-space-images \
        --image-family=confidential-space \
        --service-account=WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com \
        --metadata="^~^tee-image-reference=us-docker.pkg.dev/\
    ALEX_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest\
    ~tee-env-COLLAB_1_NAME=Alex\
    ~tee-env-COLLAB_2_NAME=Bola\
    ~tee-env-COLLAB_1_ENCRYPTED_SALARY=ALEX_ENCRYPTED_SALARY_FILE\
    ~tee-env-COLLAB_2_ENCRYPTED_SALARY=BOLA_ENCRYPTED_SALARY_FILE\
    ~tee-env-COLLAB_1_INPUT_BUCKET=ALEX_INPUT_BUCKET_NAME\
    ~tee-env-COLLAB_2_INPUT_BUCKET=BOLA_INPUT_BUCKET_NAME\
    ~tee-env-COLLAB_1_OUTPUT_BUCKET=ALEX_OUTPUT_BUCKET_NAME\
    ~tee-env-COLLAB_2_OUTPUT_BUCKET=BOLA_OUTPUT_BUCKET_NAME\
    ~tee-env-COLLAB_1_KEYRING_NAME=ALEX_KEYRING_NAME\
    ~tee-env-COLLAB_2_KEYRING_NAME=BOLA_KEYRING_NAME\
    ~tee-env-COLLAB_1_KEY_NAME=ALEX_KEY_NAME\
    ~tee-env-COLLAB_2_KEY_NAME=BOLA_KEY_NAME\
    ~tee-env-COLLAB_1_PROJECT_ID=ALEX_PROJECT_ID\
    ~tee-env-COLLAB_2_PROJECT_ID=BOLA_PROJECT_ID\
    ~tee-env-COLLAB_1_PROJECT_NUMBER=ALEX_PROJECT_NUMBER\
    ~tee-env-COLLAB_2_PROJECT_NUMBER=BOLA_PROJECT_NUMBER\
    ~tee-env-COLLAB_1_POOL_NAME=ALEX_POOL_NAME\
    ~tee-env-COLLAB_2_POOL_NAME=BOLA_POOL_NAME"
    

The way that you view progress and view the results is the same as when you tested the workload.

When the production workload is finished, the VM instance stops. To see different results, you can change the salaries, re-encrypt them, reupload them to the respective Cloud Storage buckets, and then restart the VM instance to run the workload again:
    
    
    gcloud compute instances start WORKLOAD_VM_NAME --zone=us-west1-b
    

## Cleanup

To remove the resources created in this guide, complete the following instructions.

### Clean up Alex's resources

  1. Switch to Alex's project:
         
         gcloud config set project ALEX_PROJECT_ID
         

  2. Delete Alex's workload identity pool:
         
         gcloud iam workload-identity-pools delete ALEX_POOL_NAME \
             --location=global
         

  3. Delete Alex's Cloud Storage buckets:
         
         gcloud storage rm gs://ALEX_INPUT_BUCKET_NAME \
             gs://ALEX_OUTPUT_BUCKET_NAME --recursive
         

  4. Delete Alex's salary files, the Go code, and the `Dockerfile`:
         
         rm ALEX_SALARY.txt \
             ALEX_ENCRYPTED_SALARY_FILE \
             salary.go \
             Dockerfile
         

  5. Optional: [Disable](https://docs.cloud.google.com/kms/docs/enable-disable) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore) Alex's Cloud Key Management Service key.

  6. Optional: [Shut down Alex's project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).




### Clean up Bola's resources

  1. Switch to Bola's project:
         
         gcloud config set project BOLA_PROJECT_ID
         

  2. Delete the VM that ran the test workflow:
         
         gcloud compute instances delete WORKLOAD_VM_2_NAME --zone=us-west1-b
         

  3. Delete the VM that ran the production workflow:
         
         gcloud compute instances delete WORKLOAD_VM_NAME --zone=us-west1-b
         

  4. Delete the service account that ran the workload:
         
         gcloud iam service-accounts delete \
             WORKLOAD_SERVICE_ACCOUNT_NAME@BOLA_PROJECT_ID.iam.gserviceaccount.com
         

  5. Delete Bola's workload identity pool:
         
         gcloud iam workload-identity-pools delete BOLA_POOL_NAME \
             --location=global
         

  6. Delete Bola's Cloud Storage buckets:
         
         gcloud storage rm gs://BOLA_INPUT_BUCKET_NAME \
             gs://BOLA_OUTPUT_BUCKET_NAME --recursive
         

  7. Delete Bola's salary files:
         
         rm BOLA_SALARY.txt \
             BOLA_ENCRYPTED_SALARY_FILE
         

  8. Optional: [Disable](https://docs.cloud.google.com/kms/docs/enable-disable) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore) Bola's Cloud Key Management Service key.

  9. Optional: [Shut down Bola's project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
