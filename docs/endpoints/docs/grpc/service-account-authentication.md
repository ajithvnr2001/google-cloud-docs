---
url: https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication/
title: Authentication between services \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:17.697206+00:00
---

# Authentication between services  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Authentication between services Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/service-account-authentication "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

You can implement authentication between services by using a service account in a gRPC service. This page demonstrates service-to-service authentication by walking you through a complete example, including how to configure the [Extensible Service Proxy](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#extensible_service_proxy) (ESP) in a gRPC service to support authenticated requests and how to call the service from a gRPC client.

In order for any service to make authenticated calls into an Cloud Endpoints API, the calling service must have a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#serviceaccount) and it must send an auth token in the call. The caller must use a [Google ID token](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#google_id_token) or a custom [JSON Web Token](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#jwt) (JWT) that is signed only by the service account of the caller. ESP validates that the `iss` claim in the JWT matches the `issuer` setting in the service configuration. ESP doesn't check for [Identity and Access Management](https://cloud.google.com/iam/docs/) permissions that have been granted on the service account.

In our example, you set up and use the simplest form of service-to-service authentication, where the client uses their Google Cloud service account to generate authenticating JWTs. The approach for other authentication methods is similar, though the client-side process for getting valid authentication tokens depends on the authentication method used.

## Before you begin

This guide uses the Bookstore example used in our [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials).

  1. Clone the git repo where the gRPC example code is hosted:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

  2. Change your working directory:
         
         cd python-docs-samples/endpoints/bookstore-grpc/
         

  3. Follow the instructions in the [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) to set up a project if you don't have one already.




In this example, you use [deployment to Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine), though the authentication setup is the same for Compute Engine.

In the example, there are two Google Cloud Platform projects that are referenced:

  * The service _producer project_ , which is the project that owns the Cloud Endpoints for gRPC service.
  * The service _consumer project_ , which is the project that owns the gRPC client.



## Creating the consumer service account and key

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To create the service account and key for the _consumer project_ :

  1. In the Google Cloud console, go to APIs & services. 

[APIs & services](https://console.cloud.google.com/apis)

Make sure you are in your _consumer project_.
  2. On the **Credentials** page, in the **Create Credentials** drop-down list, select **Service Account Key**.
  3. On the **Create service account key** page, if you have an existing service account that you'd like to use, select it. Otherwise, in the **Service account** drop-down list, select **New service account** and type an account name.

A corresponding **Service account ID** is created for you. Make note of the ID, as it is needed in the following sections. For example:
         
         service-account-name@YOUR_PROJECT_ID.iam.gserviceaccount.com
         

  4. Click the **Role** drop-down list and select the following roles:

     * **Service Accounts** > **Service Account User**
     * **Service Accounts** > **Service Account Token Creator**
  5. Ensure the **JSON** key type is selected.

  6. Click **Create**. Your service account JSON key file is downloaded to your local machine. Note the location and make sure it's stored securely because it is used later to generate tokens.




## Configuring authentication for the service

Use the _producer project_ for all steps in this section.

### Set up authentication in the gRPC API configuration

Authentication for ESP is configured in the `authentication` section of your gRPC API configuration YAML file. The configuration with authentication for this example service is in [`api_config_auth.yaml`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/api_config_auth.yaml).
    
    
    authentication:
      providers:
      - id: google_service_account
        # Replace SERVICE-ACCOUNT-ID with your service account's email address.
        issuer: SERVICE-ACCOUNT-ID
        jwks_uri: https://www.googleapis.com/robot/v1/metadata/x509/SERVICE-ACCOUNT-ID
      rules:
      # This auth rule will apply to all methods.
      - selector: "*"
        requirements:
          - provider_id: google_service_account

The `providers` section specifies the authentication provider(s) you want to use - in this case, that you want to use a Google service account as an authentication provider. The `rules` section specifies that you require tokens from this provider for access to all your service's methods.

In your own copy of this file from the cloned repo:

  * Change `MY_PROJECT_ID` to your _producer project_ ID.
  * Change `SERVICE-ACCOUNT-ID` in the `authentication` section (in both the `issuer` and `jwks_uri` values) to the consumer service account ID you noted in the previous section. This tells ESP that you want to grant access to your service to users who provide valid tokens from this particular service account.
  * Optionally, add `jwt_locations` under the `providers` element. You can use this value to define a custom JWT location. The default JWT locations are the `Authorization` metadata (prefixed by "Bearer ") and the `X-Goog-Iap-Jwt-Assertion` metadata.

**Note:** \- If you specify the `jwt_locations`, Endpoints then ignores all default locations. \- The customized `jwt_locations` are only supported by ESPv2 so far.

Save the file for the next step.

### Deploy the configuration and service

These steps are the same as in [Getting started with gRPC on GKE](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine):

  1. [Deploy your service configuration to Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine#deploy_configuration): you need to do this even if you did so for the tutorial, as this is a different configuration. Note the returned service name:
         
         gcloud endpoints services deploy api_descriptor.pb api_config_auth.yaml --project PRODUCER_PROJECT
         

  2. [Create a container cluster](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine#creating_a_container_cluster) and [authenticate `kubectl` to the cluster](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine#authenticating_kubectl_to_the_container_cluster), if you haven't already done so.

  3. [Deploy the sample API and ESP to the cluster](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine#deploying_the_sample_api_and_esp_to_the_cluster). If you are using separate producer and consumer projects, first make sure that you have set the appropriate project within the `gcloud` command-line tool:
         
         gcloud config set project PRODUCER_PROJECT
         




## Calling authenticated methods from a gRPC client

Finally, on the client side, you can use the service account key to generate a JWT token and then use the token to call an authenticated Bookstore method. First install the appropriate Python requirements to both generate the token and run the example client. Ensure that you are in the `python-docs-samples/endpoints/bookstore-grpc` folder of your cloned client, then:
    
    
    virtualenv bookstore-env
    source bookstore-env/bin/activate
    pip install -r requirements.txt
    

### Generate a JWT token

In this example, the Bookstore is using service-to-service authentication where the calling service is purely authenticated by its service account, so creating an appropriate token to send with our requests is simple. Note that you can also require more stringent service-to-service authentication where the generated token must be further authenticated by Google (using a [Google Id token](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#google_id_token)).

For this example, the provided Python script can generate a token from the JSON key file downloaded earlier, using a dummy user ID and email.
    
    
    #!/usr/bin/env python
    
    # Copyright 2016 Google Inc.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Example of generating a JWT signed from a service account file."""
    
    import argparse
    import json
    import time
    
    import google.auth.crypt
    import google.auth.jwt
    
    """Max lifetime of the token (one hour, in seconds)."""
    MAX_TOKEN_LIFETIME_SECS = 3600
    
    
    def generate_jwt(service_account_file, issuer, audiences):
        """Generates a signed JSON Web Token using a Google API Service Account."""
        with open(service_account_file) as fh:
            service_account_info = json.load(fh)
    
        signer = google.auth.crypt.RSASigner.from_string(
            service_account_info["private_key"], service_account_info["private_key_id"]
        )
    
        now = int(time.time())
    
        payload = {
            "iat": now,
            "exp": now + MAX_TOKEN_LIFETIME_SECS,
            # aud must match 'audience' in the security configuration in your
            # swagger spec. It can be any string.
            "aud": audiences,
            # iss must match 'issuer' in the security configuration in your
            # swagger spec. It can be any string.
            "iss": issuer,
            # sub and email are mapped to the user id and email respectively.
            "sub": issuer,
            "email": "user@example.com",
        }
    
        signed_jwt = google.auth.jwt.encode(signer, payload)
        return signed_jwt
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument("--file", help="The path to your service account json file.")
        parser.add_argument("--issuer", default="", help="issuer")
        parser.add_argument("--audiences", default="", help="audiences")
    
        args = parser.parse_args()
    
        signed_jwt = generate_jwt(args.file, args.issuer, args.audiences)
        print(signed_jwt.decode("utf-8"))
    

To generate a token using the script:

  * Generate a JWT token and assign it to the variable `$JWT_TOKEN`:
        
        JWT_TOKEN=$(python jwt_token_gen.py \
            --file=[SERVICE_ACCOUNT_FILE] \
            --audiences=[SERVICE_NAME] \
            --issuer=[SERVICE-ACCOUNT-ID])
        

where:

    * `[SERVICE_ACCOUNT_FILE]` is the downloaded consumer service account JSON key file.
    * `[SERVICE_NAME]` is the name of the Bookstore service that was returned when you deployed its updated service configuration to Endpoints.
    * `[SERVICE-ACCOUNT-ID]` is the full consumer service account ID when you generated your service account.

**Note:** The JWT token expires in one hour. You need to regenerate the token if you want to use it after that.

### Make an authenticated gRPC call

This last step uses [`bookstore_client.py`](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/bookstore-grpc/bookstore_client.py), which is the same client used in the [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials). To make an authenticated call, the client passes the JWT as [metadata](http://www.grpc.io/docs/guides/concepts.html#metadata) with their method call.
    
    
    def run(
        host, port, api_key, auth_token, timeout, use_tls, servername_override, ca_path

To run the example:

  1. Use `kubectl get services` to get the external IP address for the deployed Bookstore:
         
         #kubectl get services
         NAME                 CLUSTER-IP      EXTERNAL-IP      PORT(S)           AGE
         echo                 10.11.246.240   104.196.186.92   80/TCP            10d
         endpoints            10.11.243.168   104.196.210.50   80/TCP,8090/TCP   10d
         esp-grpc-bookstore   10.11.254.34    104.196.60.37    80/TCP            1d
         kubernetes           10.11.240.1     <none>           443/TCP           10d
         

In this case, it's the `esp-grpc-bookstore` service and its external IP is `104.196.60.37`.

  2. Assign the IP address to the variable `EXTERNAL_IP`
         
         EXTERNAL_IP=104.196.60.37
         

  3. List all the shelves from the Bookstore service:
         
         python bookstore_client.py --port=80 --host=$EXTERNAL_IP --auth_token=$JWT_TOKEN
         

The service returns all the shelves in the current Bookstore. You can double check it by not providing a token, or by specifying the wrong service account ID when generating the JWT. The command should fail.




## What's next

  * [Troubleshooting JWT validation](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-jwt)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
