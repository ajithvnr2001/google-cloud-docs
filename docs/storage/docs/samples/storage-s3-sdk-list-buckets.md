---
url: https://docs.cloud.google.com/storage/docs/samples/storage-s3-sdk-list-buckets/
title: List buckets using Amazon S3 SDKs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:53.460215+00:00
---

# List buckets using Amazon S3 SDKs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-s3-sdk-list-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  List buckets using Amazon S3 SDKs Stay organized with collections  Save and categorize content based on your preferences. 

List Cloud Storage buckets that use Amazon Simple Storage Service (Amazon S3) SDKs by using the Cloud Storage XML API with HMAC credentials.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Simple migration from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/aws-simple-migration)



## Code sample

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"github.com/aws/aws-sdk-go/aws"
    	"github.com/aws/aws-sdk-go/aws/credentials"
    	"github.com/aws/aws-sdk-go/aws/session"
    	"github.com/aws/aws-sdk-go/service/s3"
    )
    
    func listGCSBuckets(w io.Writer, googleAccessKeyID string, googleAccessKeySecret string) error {
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
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    	result, err := client.ListBucketsWithContext(ctx, &s3.ListBucketsInput{})
    	if err != nil {
    		return fmt.Errorf("ListBucketsWithContext: %w", err)
    	}
    
    	fmt.Fprintf(w, "Buckets:")
    	for _, b := range result.Buckets {
    		fmt.Fprintf(w, "%s\n", aws.StringValue(b.Name))
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
    import com.amazonaws.services.s3.model.Bucket;
    import java.util.List;
    
    public class ListGcsBuckets {
      public static void listGcsBuckets(String googleAccessKeyId, String googleAccessKeySecret) {
    
        // String googleAccessKeyId = "your-google-access-key-id";
        // String googleAccessKeySecret = "your-google-access-key-secret";
    
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
    
        // Call GCS to list current buckets
        List<Bucket> buckets = interopClient.listBuckets();
    
        // Print bucket names
        System.out.println("Buckets:");
        for (Bucket bucket : buckets) {
          System.out.println(bucket.getName());
        }
    
        // Explicitly clean up client resources.
        interopClient.shutdown();
      }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import boto3  # type: ignore
    
    
    def list_gcs_buckets(
        google_access_key_id: str, google_access_key_secret: str
    ) -> List[str]:
        """Lists all Cloud Storage buckets using AWS SDK for Python (boto3)
        Positional arguments:
            google_access_key_id: hash-based message authentication code (HMAC) access ID
            google_access_key_secret: HMAC access secret
    
        Returned value is a list of strings, one for each bucket name.
    
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
    
        # Call GCS to list current buckets
        response = client.list_buckets()
    
        # Return list of bucket names
        results = []
        for bucket in response["Buckets"]:
            results.append(bucket["Name"])
            print(bucket["Name"])  # Can remove if not needed after development
        return results
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
