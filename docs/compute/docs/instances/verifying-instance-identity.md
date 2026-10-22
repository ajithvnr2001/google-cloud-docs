---
url: https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity/
title: Verify VM identity \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:36.876556+00:00
---

# Verify VM identity  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Verify VM identity Stay organized with collections  Save and categorize content based on your preferences. 

Before an application sends sensitive information to a virtual machine (VM) instance, the application can verify the identity of the instance by using instance identity tokens signed by Google. Each instance has a unique JSON Web Token (JWT) that includes details about the instance as well as Google's [RS256 signature](https://tools.ietf.org/html/rfc7518#section-3.3). Your applications can verify the signature against Google's [public Oauth2 certificates](https://www.googleapis.com/oauth2/v3/certs) to confirm the identity of the instance with which they have established a connection.

Compute Engine generates signed instance tokens only when an instance requests them from instance metadata. Instances are able to access only their own unique token and not the tokens for any other instances.

You might want to verify the identities of your instances in the following scenarios:

  * When you start an instance for the first time, your applications might need to ensure that the instance they connected to has a valid identity before they transmit sensitive information to the instance.
  * When your policies require you to store credentials outside of the Compute Engine environment and you regularly send those credentials to your instances for temporary use. Your applications can confirm the identities of instances each time they need to transmit credentials.



Google's instance authentication methods have the following benefits:

  * Compute Engine creates a unique token each time an instance requests it, and each token expires within one hour. You can configure your applications to accept an instance's identity token only once, which reduces the risk that the token can be reused by an unauthorized system.
  * Signed metadata tokens use the [RFC 7519](https://tools.ietf.org/html/rfc7518#section-3.3) open industry standard and the [OpenID Connect 1.0](http://openid.net/specs/openid-connect-core-1_0.html), identity layer, so existing tooling and libraries will work seamlessly with the identity tokens.



## Before you begin

  * Understand how to [retrieve instance metadata values](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata). 
  * Understand the [basics of JSON Web Tokens](https://jwt.io/introduction/) so that you know how to use them in your applications. 
  * Understand how to [create and enable service accounts](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) on your instances. Your instances must have a service account associated with them so that they can retrieve their identity tokens. The service account does not require any IAM permissions to retrieve these identity tokens.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * If you're using a local shell, then create local authentication credentials for your user account: 
        
        gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Verifying the identity of an instance

In some scenarios your applications must verify the identity of an instance running on Compute Engine before transmitting sensitive data to that instance. In one typical example, there is one system running outside of Compute Engine called "Host1" and a Compute Engine instance called "VM1". VM1 can connect to Host1 and validate the identity of that instance with the following process:

  1. VM1 establishes a secure connection to Host1 over a secure connection protocol of your choice, such as HTTPS.

  2. VM1 requests its unique identity token from the metadata server and specifies the audience of the token. In this example, the audience value is the URI for Host1. The request to the metadata server includes the audience URI so that Host1 can check the value later during the token verification step.

  3. Google generates a new unique instance identity token in JWT format and provides it to VM1. The payload of the token includes several details about the instance and also includes the audience URI. Read Token Contents for a complete description of the token contents.

  4. VM1 sends the identity token to Host1 over the existing secure connection.

  5. Host1 decodes the identity token to obtain the token header and payload values.

  6. Host1 verifies that the token is signed by Google by checking the audience value and verifying the certificate signature against the [public Google certificate](https://www.googleapis.com/oauth2/v3/certs).

  7. If the token is valid, Host1 proceeds with the transmission and closes the connection when it is finished. Host1 and any other systems should request a new token for any subsequent connections to VM1.




### Obtaining the instance identity token

When your virtual machine instance receives a request to provide its identity token, the instance requests that token from the metadata server using the normal process for [getting instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#querying). For example, you might use one of the following methods:

###  cURL 

Create a `curl` request and include a value in the `audience` parameter. Optionally, you can include the `format` parameter to specify whether or not you want to include project and instance details in the payload. If using the `full` format, you can include the `licenses` parameter to specify whether or not you want to include license codes in the payload.
    
    
    curl -H "Metadata-Flavor: Google" \
    'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience=AUDIENCE&format=FORMAT&licenses=LICENSES'

Replace the following:

  * `AUDIENCE`: the unique URI agreed upon by both the instance and the system verifying the instance's identity. For example, the audience could be a URL for the connection between the two systems.
  * `FORMAT`: the optional parameter that specifies whether or not the project and instance details are included in the payload. Specify `full` to include this information in the payload or `standard` to omit the information from the payload. The default value is `standard`. For more information, see Identity token format.
  * `LICENSES`: an optional parameter that specifies whether [license codes](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/get#body.Image.FIELDS.license_code) for images associated with this instance are included in the payload. Specify `TRUE` to include this information or `FALSE` to omit this information from the payload. The default value is `FALSE`. Has no effect unless `format` is `full`



The metadata server responds to this request with a JSON Web Token signed using the [RS256 algorithm](https://tools.ietf.org/html/rfc7518#section-3.3). The token includes a Google signature and additional information in the payload. You can send this token to other systems and applications so that they can verify the token and confirm that the identity of your instance.

###  Python 

You can submit a simple request from your instance to the metadata server using methods in the Python `requests` library. The following example requests and then prints an instance identity token. The token is unique to the instance that makes this request.
    
    
    import requests
    
    AUDIENCE_URL = "http://www.example.com"
    METADATA_HEADERS = {"Metadata-Flavor": "Google"}
    METADATA_VM_IDENTITY_URL = (
        "http://metadata.google.internal/computeMetadata/v1/"
        "instance/service-accounts/default/identity?"
        "audience={audience}&format={format}&licenses={licenses}"
    )
    FORMAT = "full"
    LICENSES = "TRUE"
    
    
    def acquire_token(
        audience: str = AUDIENCE_URL, format: str = "standard", licenses: bool = True
    ) -> str:
        """
        Requests identity information from the metadata server.
    
        Args:
            audience: the unique URI agreed upon by both the instance and the
                system verifying the instance's identity. For example, the audience
                could be a URL for the connection between the two systems.
            format: the optional parameter that specifies whether the project and
                instance details are included in the payload. Specify `full` to
                include this information in the payload or standard to omit the
                information from the payload. The default value is `standard`.
            licenses: an optional parameter that specifies whether license
                codes for images associated with this instance are included in the
                payload. Specify TRUE to include this information or FALSE to omit
                this information from the payload. The default value is FALSE.
                Has no effect unless format is `full`.
    
        Returns:
            A JSON Web Token signed using the RS256 algorithm. The token includes a
            Google signature and additional information in the payload. You can send
            this token to other systems and applications so that they can verify the
            token and confirm that the identity of your instance.
        """
        # Construct a URL with the audience and format.
        url = METADATA_VM_IDENTITY_URL.format(
            audience=audience, format=format, licenses=licenses
        )
    
        # Request a token from the metadata server.
        r = requests.get(url, headers=METADATA_HEADERS)
        # Extract and return the token from the response.
        r.raise_for_status()
        return r.text

The metadata server responds to this request with a JSON Web Token signed using the [RS256 algorithm](https://tools.ietf.org/html/rfc7518#section-3.3). The token includes a Google signature and additional information in the payload. You can send this token to other systems and applications so that they can verify the token and confirm that the identity of your instance.

### Verifying the token

After your application receives an instance identity token from a Compute Engine instance, it can verify the token using the following process.

  1. Receive the token from the virtual machine instance, decode the token using an RS256 JWT decoder, and read the header contents to obtain the `kid` value.

  2. Verify that the token is signed by checking the token against the [public Google certificate](https://www.googleapis.com/oauth2/v3/certs). Each public certificate has a `kid` value that corresponds to the `kid` value in the token header.

**Caution:** Only tokens signed using the Google certificate can be trusted to assert properties of the Compute Engine workload.
  3. If the token is valid, compare the payload contents against the expected values. If the token payload includes details about the instance and the project, your application can check the `instance_id`, `project_id`, and `zone` values. Those values are a globally unique tuple that confirms your application is communicating with the correct instance in the desired project.




You can decode and verify the token using any tool that you like, but a common method is to use the libraries for your language of choice. For example, you can use the `verify_token` method from the [Google OAuth 2.0 library](https://developers.google.com/api-client-library/python/guide/aaa_oauth) for Python. The `verify_token` method matches the `kid` value to the appropriate certificate, verifies the signature, checks the audience claim, and returns the payload contents from the token.
    
    
    import google.auth.transport.requests
    from google.oauth2 import id_token
    def verify_token(token: str, audience: str) -> dict:
        """Verify token signature and return the token payload.
    
        Args:
            token: the JSON Web Token received from the metadata server to
                be verified.
            audience: the unique URI agreed upon by both the instance and the
                system verifying the instance's identity.
    
        Returns:
            Dictionary containing the token payload.
        """
        request = google.auth.transport.requests.Request()
        payload = id_token.verify_token(token, request=request, audience=audience)
        return payload

After your application verifies the token and its contents, it can proceed to communicate with that instance over a secure connection and then close the connection when it is finished. For subsequent connections, request a new token from the instance and re-verify the identity of the instance.

## Token contents

The instance identity token contains three primary parts:

  * Header
  * Payload
  * Signature



#### Header

The header includes the `kid` value to identify which [public Oauth2 certificates](https://www.googleapis.com/oauth2/v3/certs) you must use to verify the signature. The header also includes the `alg` value to confirm that the signature is generated using the [RS256 algorithm](https://tools.ietf.org/html/rfc7518#section-3.3).
    
    
    {
      "alg": "RS256",
      "kid": "511a3e85d2452aee960ed557e2666a8c5cedd8ae",
    }
    

#### Payload

The payload contains the `aud` audience claim. If the instance specified `format=full` when it requested the token, the payload also includes claims about the virtual machine instance and its project. When requesting a full format token, specifying `licenses=TRUE` will also include claims about the licenses associated with the instance.
    
    
    {
       "iss": "[TOKEN_ISSUER]",
       "iat": [ISSUED_TIME],
       "exp": [EXPIRED_TIME],
       "aud": "[AUDIENCE]",
       "sub": "[SUBJECT]",
       "azp": "[AUTHORIZED_PARTY]",
       "email": "[EMAIL]",
       "email_verified": "[EMAIL_VERIFIED]",
       "google": {
        "compute_engine": {
          "project_id": "[PROJECT_ID]",
          "project_number": [PROJECT_NUMBER],
          "zone": "[ZONE]",
          "instance_id": "[INSTANCE_ID]",
          "instance_name": "[INSTANCE_NAME]",
          "instance_creation_timestamp": [CREATION_TIMESTAMP],
          "instance_confidentiality": [INSTANCE_CONFIDENTIALITY],
          "license_id": [
            "[LICENSE_1]",
              ...
            "[LICENSE_N]"
          ]
        }
      }
    }
    

Where:

  * `[TOKEN_ISSUER]`: a URL identifying who issued the token. For Compute Engine, this value is `https://accounts.google.com`.
  * `[ISSUED_TIME]`: a unix timestamp indicating when the token was issued. This value updates each time the instance requests a token from the metadata server.
  * `[EXPIRED_TIME]`: a unix timestamp indicating when the token expires.
  * `[AUDIENCE]`: the unique URI agreed upon by both the instance and the system verifying the instance's identity. For example, the audience could be a URL for the connection between the two systems.
  * `[SUBJECT]`: the subject of the token, which is the unique ID for the service account that you associated with your instance.
  * `[AUTHORIZED_PARTY]`: the party to which the ID Token was issued which is the unique ID for the service account that you associated with your instance.
  * `[EMAIL]`: The email address of the service account associated with the instance.
  * `[EMAIL_VERIFIED]`: `true` if email of the service account has been verified.
  * `[PROJECT_ID]`: the ID for the project where you created the instance.
  * `[PROJECT_NUMBER]`: the unique number for the project where you created the instance.
  * `[ZONE]`: the zone where the instance is located.
  * `[INSTANCE_ID]`: the unique ID for the instance to which this token belongs. This ID is unique within the project and zone.
  * `[INSTANCE_NAME]`: the name of the instance to which this token belongs. If your project uses [zonal DNS](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names), this name can be reused across zones, so use a combination of the `project_id`, `zone`, and the `instance_id` values to identify a unique instance ID. Projects with global DNS enabled have unique instance name across the project.
  * `[CREATION_TIMESTAMP]`: a Unix timestamp indicating when you created the instance.
  * `[INSTANCE_CONFIDENTIALITY]`: `1` if the instance is a [confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm).
  * `[LICENSE_1]` through `[LICENSE_N]`: the [license codes](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/get#body.Image.FIELDS.license_code) for images associated with this instance.



Your payload might look similar to the following example:
    
    
    {
      "iss": "https://accounts.google.com",
      "iat": 1496953245,
      "exp": 1496956845,
      "aud": "https://www.example.com",
      "sub": "107517467455664443765",
      "azp": "107517467455664443765",
      "email": "739419398126-compute@developer.gserviceaccount.com",
      "email_verified": true,
      "google": {
        "compute_engine": {
          "project_id": "my-project",
          "project_number": 739419398126,
          "zone": "us-west1-a",
          "instance_id": "152986662232938449",
          "instance_name": "example",
          "instance_creation_timestamp": 1496952205,
          "instance_confidentiality": 1,
          "license_id": [
            "1000204"
          ]
        }
      }
    }
    

#### Signature

Google generates the signature by base64url encoding the header and the payload and concatenating the two values. You can check this value against the [public Oauth2 certificates](https://www.googleapis.com/oauth2/v3/certs) to verify the token.

## What's next

  * Review the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
  * [Authenticate workloads to other workloads over mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
