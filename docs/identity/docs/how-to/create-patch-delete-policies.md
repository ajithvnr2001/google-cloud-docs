---
url: https://docs.cloud.google.com/identity/docs/how-to/create-patch-delete-policies/
title: Creating, patching, and deleting policies \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:21.125551+00:00
---

# Creating, patching, and deleting policies  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-patch-delete-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating, patching, and deleting policies

This page provides code examples that show how to create, patch, and delete policies.

**Note:** Create, patch, and delete endpoints are only supported for rules and detectors settings for now.

## Before you begin

Make sure that you complete the [Setting up the Policy API](https://docs.cloud.google.com/identity/docs/how-to/setup-policies) procedure.

## Common utilities

The following snippets for imports, constants, and helper functions are reused in the create, patch and delete scripts on this page.
    
    
    from collections.abc import Mapping, Sequence
    import json
    import pprint
    from typing import Any, Optional
    import urllib.error
    import urllib.request
    from absl import app
    from absl import flags
    import google.auth
    from google.auth import iam
    from google.auth.transport import requests
    from google.oauth2 import service_account
    
    
    AUTH_SCOPES = ['https://www.googleapis.com/auth/iam']
    POLICY_SCOPES = ['https://www.googleapis.com/auth/cloud-identity.policies']
    BASE_URL = 'https://cloudidentity.googleapis.com/'
    VERSIONED_BASE_URL = f'{BASE_URL}v1/'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    
    
    _ADMIN_EMAIL = flags.DEFINE_string(
        name='admin_email',
        default=None,
        help='Administrator email to call as',
        required=True,
    )
    
    _POLICY_NAME = flags.DEFINE_string(
        name='policy_name',
        default=None,
        help='The resource name of the policy, e.g., policies/12345',
        required=True,
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
    
    
    def print_json_response(response: Mapping[str, Any]) -> None:
      pp = pprint.PrettyPrinter(indent=4)
      pp.pprint(response)
    
    
    def get_access_token(admin_email: str) -> str:
      """Creates delegated credentials and returns an access token.
    
      Args:
        admin_email: The administrator email to call as.
    
      Returns:
        The access token.
      """
      dc = create_delegated_credentials(admin_email)
      dc.refresh(requests.Request())
      if dc.token is None:
        raise ValueError(
            'Failed to refresh credentials and obtain an access token.'
        )
      return dc.token
    
    
    def execute_request(
        request: urllib.request.Request, message: str
    ) -> Optional[Mapping[str, Any]]:
      """Executes a request and prints the response.
    
      Args:
        request: The request to execute.
        message: The message to print before the response.
    
      Returns:
        Policy API response or None in case of exception.
      """
      try:
        with urllib.request.urlopen(request) as response:
          content = response.read()
          op = json.loads(content)
          print(message)
          print_json_response(op)
          return op
    
      except urllib.error.HTTPError as e:
        print(f'HTTPError: {e.code} {e.reason}')
        print(e.read().decode('utf-8'))

## Create a policy

The following example shows you how to create a policy in your organization using Python. This example specifically shows how to create a Data Protection rule and Data Protection detector.
    
    
    """Script to interact with the Cloud Identity Policies API.
    
    This script lets you create delegated credentials, build, and
    send requests to the Create Policy API. It includes a sample for creating a Data
    Protection rule and detector.
    """
    
    
    def build_create_policy_request(
        access_token: str, policy_payload: Mapping[str, Any]
    ) -> urllib.request.Request:
      """Builds the request for the Create Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_payload: The dictionary representing the policy to create.
    
      Returns:
        The request for the Create Policy API.
      """
      create_url = f'{VERSIONED_BASE_URL}policies'
      data = json.dumps(policy_payload).encode('utf-8')
      request = urllib.request.Request(create_url, data=data, method='POST')
      request.add_header('Authorization', 'Bearer ' + access_token)
      request.add_header('Content-Type', 'application/json')
      return request
    
    
    def call_create_policy_endpoint(
        access_token: str, policy_payload: Mapping[str, Any]
    ) -> Optional[Mapping[str, Any]]:
      """Calls the Create Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_payload: The policy payload to create.
    
      Returns:
        The response from the Create Policy API, or None if the request failed.
      """
      request = build_create_policy_request(access_token, policy_payload)
      execute_request(request, 'Create Policy operation started:')
    
    
    def main(argv: Sequence[str]):
      if len(argv) > 1:
        raise app.UsageError('Too many command-line arguments.')
    
      access_token = get_access_token(_ADMIN_EMAIL.value)
    
      # Holistic sample for creating drive_action rule.
      dlp_rule_payload = {
          'customer': 'customers/<customer_id>',
          'policyQuery': {
              'orgUnit': 'orgUnits/<org_unit_id>',
          },
          'setting': {
              'type': 'settings/rule.dlp',
              'value': {
                  'displayName': 'sample rule creation',
                  'state': 'ACTIVE',
                  'triggers': ['google.workspace.drive.file.v1.share'],
                  'condition': {
                      'contentCondition': (
                          "all_content.matches_dlp_detector('US_SOCIAL_SECURITY_NUMBER',"
                          ' google.privacy.dlp.v2.Likelihood.LIKELY,'
                          ' {minimum_match_count: 1,'
                          ' minimum_unique_match_count: 1})'
                      )
                  },
                  'action': {
                      'driveAction': {
                          'warnUser': {},
                      },
                  },
              },
          },
      }
    
      # Holistic sample for creating wordList detector
      dlp_detector_payload = {
          'customer': 'customers/<customer_id>',
          'policyQuery': {
              'orgUnit': 'orgUnits/<org_unit_id>',
          },
          'setting': {
              'type': 'settings/detector.word_list',
              'value': {
                  'displayName': 'Project Sensitive Terms',
                  'description': (
                      'Detector for project-specific confidential keywords.'
                  ),
                  'wordList': {
                      'words': [
                          'confidential',
                          'internal-only',
                          'top-secret',
                          'project-x',
                      ]
                  },
              },
          },
      }
    
      rule_response = call_create_policy_endpoint(access_token, dlp_rule_payload)
      detector_response = call_create_policy_endpoint(
          access_token, dlp_detector_payload
      )
    
    
    if __name__ == '__main__':
      app.run(main)

## Patch a policy

The following example shows you how to patch a policy in your organization using Python. This example specifically shows how to update a Data Protection rule to add word list detector as a condition.
    
    
    """Script to interact with the Cloud Identity Policies API.
    
    This script provides functionality to patch a policy, build, and
    send requests to the Patch Policy API. It includes a sample for updating a Data
    Protection rule.
    """
    
    
    def build_patch_policy_request(
        access_token: str, policy_name: str, policy_payload: Mapping[str, Any]
    ) -> urllib.request.Request:
      """Builds the request for the Patch Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_name: The resource name of the policy to patch.
        policy_payload: The dictionary representing the policy fields to patch.
    
      Returns:
        The request for the Patch Policy API.
      """
      patch_url = f'{VERSIONED_BASE_URL}{policy_name}'
      data = json.dumps(policy_payload).encode('utf-8')
      request = urllib.request.Request(patch_url, data=data, method='PATCH')
      request.add_header('Authorization', 'Bearer ' + access_token)
      request.add_header('Content-Type', 'application/json')
      return request
    
    
    def call_patch_policy_endpoint(
        access_token: str, policy_name: str, policy_payload: Mapping[str, Any]
    ) -> None:
      """Calls the Patch Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_name: The policy name to patch.
        policy_payload: The policy payload for patch.
      """
      request = build_patch_policy_request(
          access_token, policy_name, policy_payload
      )
      execute_request(request, 'Patch Policy operation started:')
    
    
    def main(argv: Sequence[str]):
      if len(argv) > 2:
        raise app.UsageError('Too many command-line arguments.')
    
      access_token = get_access_token(_ADMIN_EMAIL.value)
    
      # Sample for patching a rule policy to add a condition for a word list
      # detector. Replace <detector_response.name> with the name of a detector
      # policy created in the previous script.
      patch_policy_payload = {
          'policyQuery': {'orgUnit': 'orgUnits/<org_unit_id>'},
          'setting': {
              'type': 'settings/rule.dlp',
              'value': {
                  'displayName': 'Warn users for sharing of custom sensitive data',
                  'description': 'Rule triggered by custom word list detector',
                  'triggers': ['google.workspace.drive.file.v1.share'],
                  'condition': {
                      'contentCondition': (
                          "all_content.matches_word_list('<detector_response.name>')"
                      )
                  },
                  'action': {'driveAction': {'warnUser': {}}},
                  'state': 'ACTIVE',
              },
          },
      }
    
      call_patch_policy_endpoint(
          access_token, _POLICY_NAME.value, patch_policy_payload
      )
    
    
    if __name__ == '__main__':
      app.run(main)

## Delete a policy

The following example shows you how to delete a policy in your organization by using Python.
    
    
    """Script to interact with the Cloud Identity Policies API.
    
    This script lets you delete a policy, build, and
    send requests to the Delete Policy API.
    """
    
    
    def build_delete_policy_request(
        access_token: str, policy_name: str
    ) -> urllib.request.Request:
      """Builds the request for the Delete Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_name: The resource name of the policy to delete.
    
      Returns:
        The request for the Delete Policy API.
      """
      delete_url = f'{VERSIONED_BASE_URL}{policy_name}'
      request = urllib.request.Request(delete_url, method='DELETE')
      request.add_header('Authorization', 'Bearer ' + access_token)
      return request
    
    
    def call_delete_policy_api(access_token: str, policy_name: str) -> None:
      """Calls the Delete Policy API.
    
      Args:
        access_token: The access token for the API.
        policy_name: The policy name to delete.
      """
      request = build_delete_policy_request(access_token, policy_name)
      execute_request(request, 'Delete Policy operation started:')
    
    
    def main(argv: Sequence[str]):
      if len(argv) > 2:
        raise app.UsageError('Too many command-line arguments.')
    
      access_token = get_access_token(_ADMIN_EMAIL.value)
    
      call_delete_policy_api(access_token, _POLICY_NAME.value)
    
    
    if __name__ == '__main__':
      app.run(main)

## Quota

For each Google Cloud project, Cloud Identity Policy API supports one query per second (QPS). For each customer, Cloud Identity Policy API supports one QPS in total, even if the customer creates multiple Google Cloud projects.

A quota increase is not supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
