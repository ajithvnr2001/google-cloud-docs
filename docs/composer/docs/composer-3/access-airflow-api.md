---
url: https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api/
title: Access the Airflow REST API \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:45.160314+00:00
---

# Access the Airflow REST API  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Access the Airflow REST API Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-api "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api "View this page for Managed Airflow \(Legacy Gen 1\)")

Apache Airflow has a REST API interface that you can use to perform tasks such as getting information about DAG runs and tasks, updating DAGs, getting Airflow configuration, adding and deleting connections, and listing users.

For an example of using Airflow REST API with Cloud Run functions, see [Triggering DAGs with Cloud Run functions](https://docs.cloud.google.com/composer/docs/composer-3/triggering-with-gcf).

## Airflow REST API versions

  * Airflow 3 uses the [Airflow REST API v2](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html).
  * Airflow 2 uses the [Airflow REST API v1](https://airflow.apache.org/docs/apache-airflow/2.10.5/stable-rest-api-ref.html).



## Configure the Airflow REST API

###  Airflow 3 

Airflow 3 uses the Airflow REST API v2.

Managed Airflow uses its own [API authentication backend](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html#roll-your-own-api-authentication). 

Authorization works in the standard way provided by Airflow 3. When a new user authorizes through the API, the user's account gets the `Op` role by default.

The Airflow REST API in Airflow 3 is always enabled and it's not possible to disable it. You can change the default user role by [overriding](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration option:

Section | Key | Value | Notes  
---|---|---|---  
`api` |  `composer_auth_user_registration_role` |  `Op` |  You can specify [any other role](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/auth-manager/access-control.html#default-roles).  
  
###  Airflow 2 

The Airflow REST API v1 is enabled by default in Airflow 2.

Managed Airflow uses its own [API authentication backend](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html#roll-your-own-api-authentication). 

Authorization works in the standard way provided by Airflow. When a new user authorizes through the API, the user's account gets the `Op` role by default.

You can enable or disable the Airflow REST API, or change the default user role by [overriding](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value | Notes  
---|---|---|---  
`api` |  `auth_backends` |  `airflow.composer.api.backend.composer_auth` |  To disable the Airflow REST API, change to `airflow.api.auth.backend.deny_all`  
`api` |  `composer_auth_user_registration_role` |  `Op` |  You can specify [any other role](https://airflow.apache.org/docs/apache-airflow-providers-fab/stable/auth-manager/access-control.html#default-roles).  
  
## Allow API calls to Airflow REST API using web server access control

Depending on the method used to call Airflow REST API, the caller method can use either **IPv4 or IPv6 address**. Remember to unblock the IP traffic to Airflow REST API using [web server access control](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#network-access-controls).

Use the default configuration option which is `All IP addresses have access (default)` if you are not sure from which IP addresses your calls to Airflow REST API will be sent.

## Make calls to Airflow REST API

This section provides an example Python script which you can use to trigger DAGs with the Airflow REST API.

In the script, set the following variables:

  * `dag_id`: name of a DAG, as defined in the DAG source file.
  * `dag_config`: configuration for the DAG run.
  * `web_server_url`: Your Airflow web server URL. The format is `https://<web-server-id>.composer.googleusercontent.com`.

**Important:** Don't put the **backwards slash** at the end of the web server URL.
  * _(Airflow 3)_ `logical_date`: The [logical date](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html) for the DAG run.




###  Airflow 3 
    
    
    """
    Trigger a DAG in Cloud Composer 3 environment with Airflow 3 using the Airflow REST API v2.
    """
    
    from __future__ import annotations
    
    from typing import Any
    
    import google.auth
    from google.auth.transport.requests import AuthorizedSession
    import requests
    
    # Following best practices, these credentials should be
    # constructed at start-up time and used throughout
    # https://cloud.google.com/apis/docs/client-libraries-best-practices
    AUTH_SCOPE = "https://www.googleapis.com/auth/cloud-platform"
    CREDENTIALS, _ = google.auth.default(scopes=[AUTH_SCOPE])
    
    def make_composer3_web_server_request(
        url: str, method: str = "GET", **kwargs: Any
    ) -> google.auth.transport.Response:
        """
        Make a request to Cloud Composer 3 environment's web server with Airflow 3.
        Args:
          url: The URL to fetch.
          method: The request method to use ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT',
            'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                      If no timeout is provided, it is set to 90 by default.
        """
    
        authed_session = AuthorizedSession(CREDENTIALS)
    
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        return authed_session.request(method, url, **kwargs)
    
    def trigger_dag(web_server_url: str, dag_id: str, data: dict, logical_date: str) -> str:
        """
        Make a request to trigger a DAG using the Airflow REST API v2.
        https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
    
        Args:
          web_server_url: The URL of the Airflow 3 web server.
          dag_id: The DAG ID.
          data: Additional configuration parameters for the DAG run (json).
        """
    
        endpoint = f"api/v2/dags/{dag_id}/dagRuns"
        request_url = f"{web_server_url}/{endpoint}"
        json_data = {"conf": data, "logical_date": logical_date}
    
        response = make_composer3_web_server_request(
            request_url, method="POST", json=json_data
        )
    
        if response.status_code == 403:
            raise requests.HTTPError(
                "You do not have a permission to perform this operation. "
                "Check Airflow RBAC roles for your account."
                f"{response.headers} / {response.text}"
            )
        elif response.status_code != 200:
            response.raise_for_status()
        else:
            return response.text
    
    if __name__ == "__main__":
        # TODO(developer): replace with your values
        dag_id = "airflow_monitoring"  # Replace with the ID of the DAG that you want to run.
        dag_config = {
            "your-key": "your-value"
        }  # Replace with configuration parameters for the DAG run.
        # Replace web_server_url with the Airflow web server address. To obtain this
        # URL, run the following command for your environment:
        # gcloud composer environments describe example-environment \
        #  --location=your-composer-region \
        #  --format="value(config.airflowUri)"
        logical_date = "2025-01-01T14:00:00Z" # Replace with the data interval for which to run the DAG
        web_server_url = (
            "https://example-airflow-ui-url-dot-us-central1.composer-staging.googleusercontent.com"
        )
    
        response_text = trigger_dag(
            web_server_url=web_server_url, dag_id=dag_id, data=dag_config, logical_date=logical_date
        )
    
        print(response_text)
    

###  Airflow 2 
    
    
    from __future__ import annotations
    
    from typing import Any
    
    import google.auth
    from google.auth.transport.requests import AuthorizedSession
    import requests
    
    
    # Following GCP best practices, these credentials should be
    # constructed at start-up time and used throughout
    # https://cloud.google.com/apis/docs/client-libraries-best-practices
    AUTH_SCOPE = "https://www.googleapis.com/auth/cloud-platform"
    CREDENTIALS, _ = google.auth.default(scopes=[AUTH_SCOPE])
    
    
    def make_composer2_web_server_request(
        url: str, method: str = "GET", **kwargs: Any
    ) -> google.auth.transport.Response:
        """
        Make a request to Cloud Composer 2 environment's web server.
        Args:
          url: The URL to fetch.
          method: The request method to use ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT',
            'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                      If no timeout is provided, it is set to 90 by default.
        """
    
        authed_session = AuthorizedSession(CREDENTIALS)
    
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        return authed_session.request(method, url, **kwargs)
    
    
    def trigger_dag(web_server_url: str, dag_id: str, data: dict) -> str:
        """
        Make a request to trigger a dag using the stable Airflow 2 REST API.
        https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
    
        Args:
          web_server_url: The URL of the Airflow 2 web server.
          dag_id: The DAG ID.
          data: Additional configuration parameters for the DAG run (json).
        """
    
        endpoint = f"api/v1/dags/{dag_id}/dagRuns"
        request_url = f"{web_server_url}/{endpoint}"
        json_data = {"conf": data}
    
        response = make_composer2_web_server_request(
            request_url, method="POST", json=json_data
        )
    
        if response.status_code == 403:
            raise requests.HTTPError(
                "You do not have a permission to perform this operation. "
                "Check Airflow RBAC roles for your account."
                f"{response.headers} / {response.text}"
            )
        elif response.status_code != 200:
            response.raise_for_status()
        else:
            return response.text
    
    
    
    
    if __name__ == "__main__":
        # TODO(developer): replace with your values
        dag_id = "your-dag-id"  # Replace with the ID of the DAG that you want to run.
        dag_config = {
            "your-key": "your-value"
        }  # Replace with configuration parameters for the DAG run.
        # Replace web_server_url with the Airflow web server address. To obtain this
        # URL, run the following command for your environment:
        # gcloud composer environments describe example-environment \
        #  --location=your-composer-region \
        #  --format="value(config.airflowUri)"
        web_server_url = (
            "https://example-airflow-ui-url-dot-us-central1.composer.googleusercontent.com"
        )
    
        response_text = trigger_dag(
            web_server_url=web_server_url, dag_id=dag_id, data=dag_config
        )
    
        print(response_text)
    

## Access Airflow REST API using a service account

The Airflow database in Airflow versions before 2.3.0 limits the length of the email field to 64 characters. Service accounts sometimes have email addresses that are longer than 64 characters. It is not possible to create Airflow users for such service accounts in the usual way. If there is no Airflow user for such a service account, then accessing the Airflow REST API results in HTTP errors 401 and 403.

**Note:** Errors 401 (Unauthorized) and 403 (Forbidden) are generic HTTP errors. If you still get these errors after using the described workaround, then check for other possible causes. For example, IAM roles might be missing on the service account. To allow a service account to access the Airflow REST API, grant an IAM role that [allows accessing the web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-control#role-view-environments).

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

     1. [Go to the Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).

     2. Go to **Security** > **List Users** and click **Add a new record**. Your Airflow user must have the `Admin` role to open this page.

     3. Specify `accounts.google.com:NUMERIC_USER_ID` as the user name. Replace `NUMERIC_USER_ID` with the user ID obtained on the previous step.

     4. Specify a unique identifier as the email. You can use any unique string.

     5. Specify the role for the user. For example, `Op`.

     6. Make sure that **Is Active?** checkbox is selected.

     7. Specify the first and the last name for the user. You can use any string.

     8. Click **Save**.

###  gcloud 

Run the following Airflow CLI command:
    
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

  * [Triggering DAGs with Cloud Run functions](https://docs.cloud.google.com/composer/docs/composer-3/triggering-with-gcf)
  * [Airflow command-line interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
