---
url: https://docs.cloud.google.com/iam/docs/samples/iam-workload-identity-aws-credential/
title: Create a token for Workload Identity Federation with AWS \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:03.312184+00:00
---

# Create a token for Workload Identity Federation with AWS  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-workload-identity-aws-credential/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Create a token for Workload Identity Federation with AWS Stay organized with collections  Save and categorize content based on your preferences. 

Creates a token that IAM Workload Identity Federation can verify without revealing the AWS secret access key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Workload Identity Federation with AWS or Azure VMs](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds)



## Code sample

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import json
    import urllib
    
    import boto3
    from botocore.auth import SigV4Auth
    from botocore.awsrequest import AWSRequest
    
    
    def create_token_aws(project_number: str, pool_id: str, provider_id: str) -> None:
        # Prepare a GetCallerIdentity request.
        request = AWSRequest(
            method="POST",
            url="https://sts.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15",
            headers={
                "Host": "sts.amazonaws.com",
                "x-goog-cloud-target-resource": f"//iam.googleapis.com/projects/{project_number}/locations/global/workloadIdentityPools/{pool_id}/providers/{provider_id}",
            },
        )
    
        # Set the session credentials and Sign the request.
        # get_credentials loads the required credentials as environment variables.
        # Refer:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
        SigV4Auth(boto3.Session().get_credentials(), "sts", "us-east-1").add_auth(request)
    
        # Create token from signed request.
        token = {"url": request.url, "method": request.method, "headers": []}
        for key, value in request.headers.items():
            token["headers"].append({"key": key, "value": value})
    
        # The token lets workload identity federation verify the identity without revealing the AWS secret access key.
        print("Token:\n%s" % json.dumps(token, indent=2, sort_keys=True))
        print("URL encoded token:\n%s" % urllib.parse.quote(json.dumps(token)))
    
    
    def main() -> None:
        # TODO(Developer): Replace the below credentials.
        # project_number: Google Project number (not the project id)
        project_number = "my-project-number"
        pool_id = "my-pool-id"
        provider_id = "my-provider-id"
    
        create_token_aws(project_number, pool_id, provider_id)
    
    
    if __name__ == "__main__":
        main()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
