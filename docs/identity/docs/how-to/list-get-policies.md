---
url: https://docs.cloud.google.com/identity/docs/how-to/list-get-policies/
title: Listing and getting policies \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:12.979682+00:00
---

# Listing and getting policies  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/list-get-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Listing and getting policies

This page provides code examples that demonstrate how to list and get policies.

## Before you begin

Complete the [Setting up the Policy API](https://docs.cloud.google.com/identity/docs/how-to/setup-policies).

## List policies

The following example shows how to list organization policies using Python.

> **Important:** The OAuth scopes specified in your application code used to create delegated credentials must be present in the authorized scopes list for domain-wide delegation in the Google Admin Console. A broader or more permissive scope won't work. If a scope requested by the application to create delegated credentials is not authorized in domain-wide delegation, the application receives an `unauthorized_client` error.
    
    
    """Sample script to demonstrate the use of the List method in the Policy API."""
    
    from collections.abc import Mapping, Sequence
    import json
    import pprint
    import time
    from typing import Any
    import urllib.request
    from absl import app
    from absl import flags
    import google.auth
    from google.auth import iam
    from google.auth.transport import requests
    from google.oauth2 import service_account
    
    AUTH_SCOPES = ['https://www.googleapis.com/auth/iam']
    # The read-only scope of the API. Note that you must authorize the
    # exact same scope for domain-wide delegation in the Google Admin Console.
    POLICY_SCOPES = [
        'https://www.googleapis.com/auth/cloud-identity.policies.readonly'
    ]
    BASE_URL = 'https://cloudidentity.googleapis.com/'
    VERSIONED_BASE_URL = f'{BASE_URL}v1/'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    
    _ADMIN_EMAIL = flags.DEFINE_string(
        name='admin_email',
        default=None,
        help='Administrator email to call as',
        required=True,
    )
    
    _PAGE_SIZE = flags.DEFINE_integer(
        name='page_size',
        default=50,
        help='Page size for the List API request',
        required=False,
    )
    
    # To list all policies, set FILTER to '';
    # To list policies for a specific customer, set FILTER to
    # 'customer == "customers/{obfuscated_target_customer_id}"';
    # To list policies for a specific Application, such as Gmail, set FILTER to
    # 'setting.type.matches("gmail.*")';
    # To list policies for a specific Setting, such as service_status, set FILTER to
    # 'setting.type.matches(".*service_status")'.
    _LIST_FILTER = flags.DEFINE_string(
        name='list_filter',
        default='',
        help='Filter for the List API request',
        required=False,
    )
    
    
    def create_delegated_credentials(
        admin_email: str,
    ) -> google.auth.credentials.Credentials:
      """Creates delegated credentials for the user.
    
      Args:
        admin_email: The administrator email to call as.
    
      Returns:
        The delegated credentials for the user.
      """
      # Fetch application default credentials (ADC)
      credentials, _ = google.auth.default(scopes=AUTH_SCOPES)
    
      # Populate account information
      request = requests.Request()
      credentials.refresh(request)
    
      # Create an IAM signer
      signer = iam.Signer(request, credentials, credentials.service_account_email)
    
      # Create domain-wide delegated (DWD) credentials
      delegated_credentials = service_account.Credentials(
          signer=signer,
          service_account_email=credentials.service_account_email,
          token_uri=TOKEN_URI,
          scopes=POLICY_SCOPES,
          subject=admin_email,
      )
      return delegated_credentials
    
    
    def build_list_policies_request(
        page_size: int, list_filter: str, page_token: str, access_token: str
    ) -> urllib.request.Request:
      """Builds the request for the List Policies API.
    
      Args:
        page_size: The page size for the request.
        list_filter: The filter for the request.
        page_token: The page token for the request.
        access_token: The access token for the API.
    
      Returns:
        The request for the List Policies API.
      """
      list_url = (
          f'{VERSIONED_BASE_URL}policies?page_size={page_size}'
          f'&filter={list_filter}&page_token={page_token}'
      )
      request = urllib.request.Request(list_url)
      request.add_header('Authorization', 'Bearer ' + access_token)
      return request
    
    
    def call_list_policies_api(
        request: urllib.request.Request,
    ) -> Mapping[str, Any]:
      """Calls the List Policies API.
    
      Args:
        request: The request for the List Policies API.
    
      Returns:
        The response for the List Policies API.
      """
      content = urllib.request.urlopen(request).read()
      return json.loads(content)
    
    
    def call_list_policies_api_till_last_page(
        access_token: str, page_size: int, list_filter: str
    ) -> None:
      """Calls the List Policies API until the last page.
    
      Args:
        access_token: The access token for the API.
        page_size: The page size for the request.
        list_filter: The filter for the request.
      """
      page_token = ''
      # Paginate until the last page.
      while True:
        list_policies_request = build_list_policies_request(
            page_size, list_filter, page_token, access_token
        )
        list_policies_response = call_list_policies_api(list_policies_request)
        print_list_policies_response(list_policies_response)
        if (
            'nextPageToken' not in list_policies_response
            or not list_policies_response['nextPageToken']
        ):
          print('This is the last page.')
          break
        page_token = list_policies_response['nextPageToken']
        time.sleep(1)
    
    
    def print_list_policies_response(response: Mapping[str, Any]) -> None:
      pp = pprint.PrettyPrinter(indent=4)
    
      if 'policies' in response:
        for policy in response['policies']:
          pp.pprint(policy)
      if 'nextPageToken' in response:
        print('Next page token: ' + response['nextPageToken'])
    
    
    def main(argv: Sequence[str]):
      if len(argv) > 3:
        raise app.UsageError('Too many command-line arguments.')
    
      dc = create_delegated_credentials(_ADMIN_EMAIL.value)
      dc.refresh(requests.Request())
      if dc.token is None:
        raise ValueError('Failed to obtain access token.')
      call_list_policies_api_till_last_page(
          dc.token,
          _PAGE_SIZE.value,
          _LIST_FILTER.value,
      )
    
    
    if __name__ == '__main__':
      app.run(main)

## Get policy

The following example shows how to retrieve a specific policy using Python.
    
    
    """Sample script to demonstrate the use of the get method in the Policy API."""
    
    
    def build_get_policy_request(
        policy_name: str, access_token: str
    ) -> urllib.request.Request:
      """Builds the request for the Get Policy API.
    
      Args:
        policy_name: The policy name to get.
        access_token: The access token for the API.
    
      Returns:
        The request for the Get Policy API.
      """
      list_url = f'{VERSIONED_BASE_URL}{policy_name}'
      request = urllib.request.Request(list_url)
      request.add_header('Authorization', 'Bearer ' + access_token)
      return request
    
    
    def call_get_policy_api(access_token: str, policy_name: str) -> None:
      """Calls the Get Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_name: The policy name to get.
      """
      request = build_get_policy_request(policy_name, access_token)
      content = urllib.request.urlopen(request).read()
      response = json.loads(content)
      print_get_policy_response(response)
    
    
    def print_get_policy_response(response: str) -> None:
      pp = pprint.PrettyPrinter(indent=4)
      pp.pprint(response)

## Quota

For each Google Cloud project, Cloud Identity Policy API supports one query per second (QPS). For each customer, Cloud Identity Policy API supports one QPS in total, even if the customer creates multiple Google Cloud projects.

Quota increase is not supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
