---
url: https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api/
title: Access the Airflow REST API \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:27:49.863974+00:00
---

# Access the Airflow REST API  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Access the Airflow REST API Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Composer 3](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api "View this page for Cloud Composer 3") | [Cloud Composer 2](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-api "View this page for Cloud Composer 2") | **Cloud Composer 1**

Apache Airflow has a REST API interface that you can use to perform tasks such as getting information about DAG runs and tasks, updating DAGs, getting Airflow configuration, adding and deleting connections, and listing users.

For an example of using Airflow REST API with Cloud Run functions, see [Triggering DAGs with Cloud Run functions](https://docs.cloud.google.com/composer/docs/composer-1/triggering-with-gcf).

## Airflow REST API versions

  * Airflow 1 uses the [experimental REST API](https://airflow.apache.org/docs/apache-airflow/stable/deprecated-rest-api-ref.html).
  * Airflow 2 uses the [stable REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html). The experimental REST API is deprecated by Airflow.
  * You can still use the experimental REST API in Airflow 2 if you enable it through an Airflow configuration override, as described further.



## Configure the stable Airflow REST API

###  Airflow 2 

The stable REST API is enabled by default in Airflow 2. Cloud Composer uses its own [API authentication backend](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html#roll-your-own-api-authentication), which is integrated with Identity-Aware Proxy. 

Authorization works in the standard way provided by Airflow. When a new user authorizes through the API, the user's account gets the `Op` role by default.

You can enable or disable the stable REST API, or change the default user role by [overriding](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value | Notes  
---|---|---|---  
`api` |  (Airflow 2.2.5 and earlier) `auth_backend`   
(Airflow 2.3.0 and later) `auth_backends` |  `airflow.composer.api.backend.composer_auth` |  To disable the stable REST API, change to `airflow.api.auth.backend.deny_all`  
`api` |  `composer_auth_user_registration_role` |  `Op` |  You can specify [any other role](https://airflow.apache.org/docs/apache-airflow/stable/security/access-control.html#default-roles).  
  
###  Airflow 1 

The stable REST API is not available in Airflow 1. You can use the experimental REST API instead.

## Configure the experimental Airflow REST API

###  Airflow 2 

By default, the API authentication feature is disabled in the experimental API. The Airflow web server denies all requests to it. To enable the API authentication feature and the Airflow 2 experimental API, [override](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value | Notes  
---|---|---|---  
`api` |  (Airflow 2.2.5 and earlier) `auth_backend`   
(Airflow 2.3.0 and later) `auth_backends` |  `airflow.api.auth.backend.default` |  The default is `airflow.composer.api.backend.composer_auth`.  
`api` |  `enable_experimental_api` |  `True` |  The default is `False`.  
  
###  Airflow 1 

**Note:** This section applies to Cloud Composer versions that use **Airflow 1.10.12 and later**. If your environment uses Airflow 1.10.10 and earlier versions, the experimental REST API is enabled by default.

By default, the API authentication feature is disabled in Airflow 1.10.11 and later versions. The Airflow web server denies all requests that you make. You use requests to trigger DAGs, so enable this feature.

To enable the API authentication feature in Airflow 1, [override](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value | Notes  
---|---|---|---  
`api` | `auth_backend` | `airflow.api.auth.backend.default` | The default is `airflow.api.auth.backend.deny_all`  
  
After you set this configuration option to `airflow.api.auth.backend.default`, the Airflow web server accepts all API requests without authentication.

Even though the Airflow web server itself doesn't require authentication, Cloud Composer uses its own authentication layer to protect it, which is integrated with Identity-Aware Proxy.

## Allow API calls to Airflow REST API using web server access control

Depending on the method used to call Airflow REST API, the caller method can use either **IPv4 or IPv6 address**. Remember to unblock the IP traffic to Airflow REST API using [web server access control](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface#network-access-controls).

Use the default configuration option which is `All IP addresses have access (default)` if you are not sure from which IP addresses your calls to Airflow REST API will be sent.

## Make calls to Airflow REST API

### Get the client_id of the IAM proxy

To make a request to the Airflow REST API endpoint, the function requires the client ID of the IAM proxy that protects the Airflow web server.

Cloud Composer does not provide this information directly. Instead, make an unauthenticated request to the Airflow web server and capture the client ID from the redirect URL:

###  cURL 
    
    
    curl -v AIRFLOW_URL 2>&1 >/dev/null | grep -o "client_id\=[A-Za-z0-9-]*\.apps\.googleusercontent\.com"
    

Replace `AIRFLOW_URL` with the URL of the Airflow web interface.

In the output, search for the string following `client_id`. For example:
    
    
    client_id=**836436932391-16q2c5f5dcsfnel77va9bvf4j280t35c.apps.googleusercontent.com**
    

###  Python 

Save the following code in a file called `get_client_id.py`. Fill in your values for `project_id`, `location`, and `composer_environment`, then run the code in Cloud Shell or your local environment.
    
    
    # This script is intended to be used with Composer 1 environments
    # In Composer 2, the Airflow Webserver is not in the tenant project
    # so there is no tenant client ID
    # See https://cloud.google.com/composer/docs/composer-2/environment-architecture
    # for more details
    import google.auth
    import google.auth.transport.requests
    import requests
    import six.moves.urllib.parse
    
    # Authenticate with Google Cloud.
    # See: https://cloud.google.com/docs/authentication/getting-started
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'us-central1'
    # composer_environment = 'YOUR_COMPOSER_ENVIRONMENT_NAME'
    
    environment_url = (
        "https://composer.googleapis.com/v1beta1/projects/{}/locations/{}"
        "/environments/{}"
    ).format(project_id, location, composer_environment)
    composer_response = authed_session.request("GET", environment_url)
    environment_data = composer_response.json()
    composer_version = environment_data["config"]["softwareConfig"]["imageVersion"]
    if "composer-1" not in composer_version:
        version_error = (
            "This script is intended to be used with Composer 1 environments. "
            "In Composer 2, the Airflow Webserver is not in the tenant project, "
            "so there is no tenant client ID. "
            "See https://cloud.google.com/composer/docs/composer-2/environment-architecture for more details."
        )
        raise (RuntimeError(version_error))
    airflow_uri = environment_data["config"]["airflowUri"]
    
    # The Composer environment response does not include the IAP client ID.
    # Make a second, unauthenticated HTTP request to the web server to get the
    # redirect URI.
    redirect_response = requests.get(airflow_uri, allow_redirects=False)
    redirect_location = redirect_response.headers["location"]
    
    # Extract the client_id query parameter from the redirect.
    parsed = six.moves.urllib.parse.urlparse(redirect_location)
    query_string = six.moves.urllib.parse.parse_qs(parsed.query)
    print(query_string["client_id"][0])

### Call Airflow REST API using client_id

Make the following replacements:

  * Replace the value of the `client_id` variable with the `client_id` value obtained in the previous step.
  * Replace the value of the `webserver_id` variable with your tenant project ID, which is a part of the Airflow web interface URL before `.appspot.com`. You obtained the Airflow web interface URL on a previous step.
  * Specify the Airflow REST API version that you use:

    * If you use the stable Airflow REST API, set the `USE_EXPERIMENTAL_API` variable to `False`.
    * If you use the experimental Airflow REST API, no changes are needed. The `USE_EXPERIMENTAL_API` variable is already set to `True`.


    
    
    from google.auth.transport.requests import Request
    from google.oauth2 import id_token
    import requests
    
    
    IAM_SCOPE = "https://www.googleapis.com/auth/iam"
    OAUTH_TOKEN_URI = "https://www.googleapis.com/oauth2/v4/token"
    # If you are using the stable API, set this value to False
    # For more info about Airflow APIs see https://cloud.google.com/composer/docs/access-airflow-api
    USE_EXPERIMENTAL_API = True
    
    
    def trigger_dag(data, context=None):
        """Makes a POST request to the Composer DAG Trigger API
    
        When called via Google Cloud Functions (GCF),
        data and context are Background function parameters.
    
        For more info, refer to
        https://cloud.google.com/functions/docs/writing/background#functions_background_parameters-python
    
        To call this function from a Python script, omit the ``context`` argument
        and pass in a non-null value for the ``data`` argument.
    
        This function is currently only compatible with Composer v1 environments.
        """
    
        # Fill in with your Composer info here
        # Navigate to your webserver's login page and get this from the URL
        # Or use the script found at
        # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/rest/get_client_id.py
        client_id = "YOUR-CLIENT-ID"
        # This should be part of your webserver's URL:
        # {tenant-project-id}.appspot.com
        webserver_id = "YOUR-TENANT-PROJECT"
        # The name of the DAG you wish to trigger
        dag_name = "composer_sample_trigger_response_dag"
    
        if USE_EXPERIMENTAL_API:
            endpoint = f"api/experimental/dags/{dag_name}/dag_runs"
            json_data = {"conf": data, "replace_microseconds": "false"}
        else:
            endpoint = f"api/v1/dags/{dag_name}/dagRuns"
            json_data = {"conf": data}
        webserver_url = "https://" + webserver_id + ".appspot.com/" + endpoint
        # Make a POST request to IAP which then Triggers the DAG
        make_iap_request(webserver_url, client_id, method="POST", json=json_data)
    
    
    # This code is copied from
    # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/iap/make_iap_request.py
    # START COPIED IAP CODE
    def make_iap_request(url, client_id, method="GET", **kwargs):
        """Makes a request to an application protected by Identity-Aware Proxy.
        Args:
          url: The Identity-Aware Proxy-protected URL to fetch.
          client_id: The client ID used by Identity-Aware Proxy.
          method: The request method to use
                  ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                    If no timeout is provided, it is set to 90 by default.
        Returns:
          The page body, or raises an exception if the page couldn't be retrieved.
        """
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        # Obtain an OpenID Connect (OIDC) token from metadata server or using service
        # account.
        google_open_id_connect_token = id_token.fetch_id_token(Request(), client_id)
    
        # Fetch the Identity-Aware Proxy-protected URL, including an
        # Authorization header containing "Bearer " followed by a
        # Google-issued OpenID Connect token for the service account.
        resp = requests.request(
            method,
            url,
            headers={"Authorization": "Bearer {}".format(google_open_id_connect_token)},
            **kwargs,
        )
        if resp.status_code == 403:
            raise Exception(
                "Service account does not have permission to "
                "access the IAP-protected application."
            )
        elif resp.status_code != 200:
            raise Exception(
                "Bad response from application: {!r} / {!r} / {!r}".format(
                    resp.status_code, resp.headers, resp.text
                )
            )
        else:
            return resp.text
    
    
    # END COPIED IAP CODE
    

## Access Airflow REST API using a service account

**Note:** If your environment uses Airflow 1, then this section only applies if [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-1/airflow-rbac) is enabled in your environment. Otherwise, Airflow does not perform its own user management.

The Airflow database in Airflow versions before 2.3.0 limits the length of the email field to 64 characters. Service accounts sometimes have email addresses that are longer than 64 characters. It is not possible to create Airflow users for such service accounts in the usual way. If there is no Airflow user for such a service account, then accessing the Airflow REST API results in HTTP errors 401 and 403.

**Note:** Errors 401 (Unauthorized) and 403 (Forbidden) are generic HTTP errors. If you still get these errors after using the described workaround, then check for other possible causes. For example, IAM roles might be missing on the service account. To allow a service account to access the Airflow REST API, grant an IAM role that [allows accessing the web interface](https://docs.cloud.google.com/composer/docs/composer-1/access-control#role-view-environments).

As a workaround, you can preregister an Airflow user for a service account. To do so, use `accounts.google.com:NUMERIC_USER_ID` as the username, and any unique string as the email.

  1. To get `NUMERIC_USER_ID` for a service account, run:
         
         gcloud iam service-accounts describe \
           SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
           --format="value(oauth2ClientId)"
         

Replace:

     * `SA_NAME` with the service account name.
     * `PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  2. Create an Airflow user with the `Op` role for the service account:

###  Airflow UI 

     1. [Go to the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface).

     2. Go to **Admin** > **Users** and click **Create**. Your Airflow user must have the `Admin` role to open this page.

     3. Specify `accounts.google.com:NUMERIC_USER_ID` as the user name. Replace `NUMERIC_USER_ID` with the user ID obtained on the previous step.

     4. Specify a unique identifier as the email. You can use any unique string.

     5. Specify the role for the user. For example, `Op`.

     6. Make sure that **Is Active?** checkbox is selected.

     7. Specify the first and the last name for the user. You can use any string.

     8. Click **Save**.

###  gcloud 

**Note:** In Cloud Composer environments with Airflow 1, you cannot run Airflow CLI commands that create users through `gcloud`. You can use the Airflow UI.

In Airflow 2, run the following Airflow CLI command:
    
    gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        users create -- \
        -u accounts.google.com:NUMERIC_USER_ID \
        -e UNIQUE_ID  \
        -f UNIQUE_ID \
        -l - -r Op --use-random-password
    

Replace:

     * `ENVIRONMENT_NAME` with the name of the environment.
     * `LOCATION` with the region where the environment is located.
     * `NUMERIC_USER_ID` with the user ID obtained in the previous step.
     * `UNIQUE_ID` with the identifier for the Airflow user. You can use any unique string.

  3. After you create an Airflow user for a service account, a caller authenticated as the service account is recognized as a pre-registered user, and is logged into Airflow.




## Scaling the Airflow REST API component

Airflow REST API and Airflow UI endpoints are run within the Airflow web server. If you use REST API intensively, consider increasing the amount of CPU and memory available to the Airflow web server, based on the expected load.

## What's next

  * [Triggering DAGs with Cloud Run functions](https://docs.cloud.google.com/composer/docs/composer-1/triggering-with-gcf)
  * [Airflow command-line interface](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-14 UTC."],[],[]] 
