---
url: https://docs.cloud.google.com/storage/docs/samples/storage-s3-sdk-list-objects/
title: Amazon S3 SDK: List objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:44.271773+00:00
---

# Amazon S3 SDK: List objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-s3-sdk-list-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Amazon S3 SDK: List objects Stay organized with collections  Save and categorize content based on your preferences. 

Shows an example of listing objects to help developers overcome an issue with interoperability until it's fixed.

## Code sample

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"github.com/aws/aws-sdk-go/aws"
    	"github.com/aws/aws-sdk-go/aws/credentials"
    	"github.com/aws/aws-sdk-go/aws/session"
    	"github.com/aws/aws-sdk-go/service/s3"
    )
    
    func listGCSObjects(w io.Writer, bucketName string, googleAccessKeyID string, googleAccessKeySecret string) error {
    	// bucketName := "your-gcs-bucket-name"
    	// googleAccessKeyID := "Your Google Access Key ID"
    	// googleAccessKeySecret := "Your Google Access Key Secret"
    
    	// Create a new client and do the following:
    	// 1. Change the endpoint URL to use the Google Cloud Storage XML API endpoint.
    	// 2. Use Cloud Storage HMAC Credentials.
    	sess := session.Must(session.NewSession(&aws.Config{
    		Region:      aws.String("auto"),
    		Endpoint:    aws.String("https://storage.googleapis.com"),
    		Credentials: credentials.NewStaticCredentials(googleAccessKeyID, googleAccessKeySecret, ""),
    	}))
    
    	client := s3.New(sess)
    	ctx := context.Background()
    
    	result, err := client.ListObjectsWithContext(ctx, &s3.ListObjectsInput{
    		Bucket: aws.String(bucketName),
    	})
    	if err != nil {
    		return fmt.Errorf("ListObjectsWithContext: %w", err)
    	}
    
    	fmt.Fprintf(w, "Objects:")
    	for _, o := range result.Contents {
    		fmt.Fprintf(w, "%s\n", aws.StringValue(o.Key))
    	}
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.amazonaws.auth.AWSStaticCredentialsProvider;
    import com.amazonaws.auth.BasicAWSCredentials;
    import com.amazonaws.client.builder.AwsClientBuilder;
    import com.amazonaws.services.s3.AmazonS3;
    import com.amazonaws.services.s3.AmazonS3ClientBuilder;
    import com.amazonaws.services.s3.model.ObjectListing;
    import com.amazonaws.services.s3.model.S3ObjectSummary;
    
    public class ListGcsObjects {
      public static void listGcsObjects(
          String googleAccessKeyId, String googleAccessKeySecret, String bucketName) {
    
        // String googleAccessKeyId = "your-google-access-key-id";
        // String googleAccessKeySecret = "your-google-access-key-secret";
        // String bucketName = "bucket-name";
    
        // Create a BasicAWSCredentials using Cloud Storage HMAC credentials.
        BasicAWSCredentials googleCreds =
            new BasicAWSCredentials(googleAccessKeyId, googleAccessKeySecret);
    
        // Create a new client and do the following:
        // 1. Change the endpoint URL to use the Google Cloud Storage XML API endpoint.
        // 2. Use Cloud Storage HMAC Credentials.
        AmazonS3 interopClient =
            AmazonS3ClientBuilder.standard()
                .withEndpointConfiguration(
                    new AwsClientBuilder.EndpointConfiguration(
                        "https://storage.googleapis.com", "auto"))
                .withCredentials(new AWSStaticCredentialsProvider(googleCreds))
                .build();
    
        // Call GCS to list current objects
        ObjectListing objects = interopClient.listObjects(bucketName);
    
        // Print objects names
        System.out.println("Objects:");
        for (S3ObjectSummary object : objects.getObjectSummaries()) {
          System.out.println(object.getKey());
        }
    
        // Explicitly clean up client resources.
        interopClient.shutdown();
      }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import boto3  # type: ignore
    
    
    def list_gcs_objects(
        google_access_key_id: str, google_access_key_secret: str, bucket_name: str
    ) -> List[str]:
        """Lists all Cloud Storage objects using AWS SDK for Python (boto3)
        Positional arguments:
            google_access_key_id: hash-based message authentication code (HMAC) access ID
            google_access_key_secret: HMAC access secret
            bucket_name: name of Cloud Storage bucket
    
        Returned value is a list of strings, one for each object in the bucket.
    
        To use this sample:
        1. Create a Cloud Storage HMAC key: https://cloud.google.com/storage/docs/authentication/managing-hmackeys#create
        2. Change endpoint_url to a Google Cloud Storage XML API endpoint.
    
        To learn more about HMAC: https://cloud.google.com/storage/docs/authentication/hmackeys#overview
        """
        client = boto3.client(
            "s3",
            region_name="auto",
            endpoint_url="https://storage.googleapis.com",
            aws_access_key_id=google_access_key_id,
            aws_secret_access_key=google_access_key_secret,
        )
    
        # Call GCS to list objects in bucket_name
        response = client.list_objects(Bucket=bucket_name)
    
        # Return list of object names in bucket
        results = []
        for blob in response["Contents"]:
            results.append(blob["Key"])
            print(blob["Key"])  # Can remove if not needed after development
        return results
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
