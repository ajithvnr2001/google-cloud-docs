---
url: https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview/
title: Webhooks overview \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:17.286997+00:00
---

# Webhooks overview  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/webhooks-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Webhooks overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes Secure Source Manager webhooks. To set up a webhook, follow the instructions in [Set up webhooks](https://docs.cloud.google.com/secure-source-manager/docs/set-up-webhooks).

Webhooks are HTTP requests triggered by an event in a Secure Source Manager repository, and then sent to a user-specified URL.

## Webhook settings

Webhooks can only be configured in the Secure Source Manager web interface. The following fields are configurable:

Hook ID
    Human-readable name for the webhook. Hook IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lower case letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the webhook.
Target URL
    Webhook target URL. A webhook target is an open and public URL.
Sensitive query string
    

Sensitive query strings are attached to the end of the target URL as follows: `TARGET_URL?SENSITIVE_QUERY_STRING`.

Most services provide a token or a secret to ensure that the incoming requests are from an authorized service. To verify the request, you can store the required token or secret in the sensitive query string.

Sensitive query strings are static, long-lived, and must be created, rotated, and validated manually. Use sensitive query strings to target tools that expect a shared secret, API key, or token in the URL query parameters. You can also use sensitive query strings in cases where the webhook target doesn't support `auth` header-based token authentication.

Enable service account authentication
    

Select this option to authenticate the webhook using a service account. When service account authorization is enabled, Secure Source Manager creates a Google-signed OpenID Connect (OIDC) ID token for the repository's service account and send it as a bearer token in the webhook request.

Service account authorization is short-lived and doesn't require manual management of tokens. We recommend using service account authorization when your webhooks target services or endpoints that validate Google OIDC ID tokens using IAM instead of using shared secrets. Examples of such services include private Cloud Run services or Cloud Run functions functions.

Trigger on
    

Event to trigger the webhook request. Options are **Push** (triggers on a push to the repository), **Pull request state changed** (triggers when a pull request is opened, closed, reopened, or edited), and **Pull request comment** (triggers when a comment is added, edited, or deleted on a pull request).

Git refs filter for push events
    

A filter to specify which branches to report on for push events specified as a glob pattern. See the [glob](https://pkg.go.dev/github.com/gobwas/glob) documentation for syntax.

Active
    

The webhook sends requests on trigger events when selected. If unselected, no requests are sent.

## Test webhooks

After you configure your webhook, you can test the webhook by using the **Test Delivery** button in the webhooks tab.

## Event information examples

The following examples show the event information sent by Secure Source Manager to the target URL for different webhook events.

### Push event payload

The content of a push event payload is similar to the following:

#### Header
    
    
          Request URL: https://example.com?{sensitive_query_string_placeholder}
          Request method: POST
          Content-Type: application/json
          X-SecureSourceManager-Delivery: 6546af81-25c6-46d9-aa41-70c00dc67752
          X-SecureSourceManager-Event: push
          X-SecureSourceManager-Signature:
        

#### Body
    
    
        {
          "secret": "",
          "ref": "refs/heads/main",
          "before": "f22fe95d6097bc18ba2ace7c5808ef53c0211a2e",
          "after": "85c7e78e6dfb63bcad4a0bb0953c0b3554ed0e93",
          "compare_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/compare/f22fe95d6097bc18ba2ace7c5808ef53c0211a2e...85c7e78e6dfb63bcad4a0bb0953c0b3554ed0e93",
          "commits": [
            {
              "id": "85c7e78e6dfb63bcad4a0bb0953c0b3554ed0e93",
              "message": "Push Event'\n",
              "url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/commit/85c7e78e6dfb63bcad4a0bb0953c0b3554ed0e93",
              "author": {
                "name": "user",
                "email": "user@example.com",
                "username": "user@example.com"
              },
              "committer": {
                "name": "user",
                "email": "user@example.com",
                "username": "user@example.com"
              },
              "verification": null,
              "timestamp": "2024-07-03T18:27:38Z",
              "added": [],
              "removed": [],
              "modified": [
                "README.md"
              ]
            }
          ],
          "head_commit": null,
          "repository": {
            "id": 4,
            "owner": {"id":2,"login":"my-project","full_name":"","email":"email-address@example.com","avatar_url":"b2653dbf52c7e078e04b8b20020eaadeafe0337787cc0e19b976efc8d594aefb","language":"","is_admin":false,"last_login":"1970-01-01T00:00:00Z","created":"2023-06-02T14:18:40Z","restricted":false,"username":"my-project"},
            "name": "my-repo",
            "full_name": "my-project/my-repo",
            "description": "",
            "empty": false,
            "private": false,
            "fork": false,
            "template": false,
            "parent": null,
            "mirror": false,
            "size": 4,
            "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
            "ssh_url": "git@my-instance-123456789-ssh.us-central1.sourcemanager.dev:my-project/my-repo.git",
            "clone_url": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
            "original_url": "",
            "website": "",
            "stars_count": 0,
            "forks_count": 0,
            "watchers_count": 1,
            "open_issues_count": 0,
            "open_pr_counter": 1,
            "release_counter": 1,
            "default_branch": "main",
            "archived": false,
            "created_at": "2023-06-06T20:34:36Z",
            "updated_at": "2024-04-04T18:19:14Z",
            "permissions": {
              "admin": true,
              "push": true,
              "pull": true
            },
            "has_issues": true,
            "internal_tracker": {
              "enable_time_tracker": false,
              "allow_only_contributors_to_track_time": true,
              "enable_issue_dependencies": true
            },
            "has_wiki": true,
            "has_pull_requests": true,
            "has_projects": true,
            "ignore_whitespace_conflicts": false,
            "allow_merge_commits": true,
            "allow_rebase": true,
            "allow_rebase_explicit": true,
            "allow_squash_merge": true,
            "avatar_url": "",
            "internal": false,
            "mirror_interval": "",
            "uris": {
              "api": "https://my-instance-123456789-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
              "html": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
              "git_https": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git"
            }
          },
          "pusher": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://this-is-avatar.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"},
          "sender": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://this-is-avatar.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"}
        }
       

### Pull event payload

The content of a pull event payload is similar to the following.

#### Header
    
    
          Request URL: https://example.com?{sensitive_query_string_placeholder}
          Request method: POST
          Content-Type: application/json
          X-SecureSourceManager-Delivery: d7bb9273-17cf-431d-835c-b334c9702eee
          X-SecureSourceManager-Event: pull_request
          X-SecureSourceManager-Signature:
        

#### Body
    
    
          {
          "secret": "",
          "action": "opened",
          "number": 4,
          "pull_request": {
            "id": 18,
            "url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/pulls/4",
            "number": 4,
            "user": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://page-address.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"},
            "title": "Open a Pull Request'",
            "body": "",
            "labels": [],
            "milestone": null,
            "assignee": null,
            "assignees": null,
            "state": "open",
            "is_locked": false,
            "comments": 0,
            "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/cloud-git-test-pso-instance/test2/pulls/4",
            "diff_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/pulls/4.diff",
            "patch_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/pulls/4.patch",
            "mergeable": false,
            "merged": false,
            "merged_at": null,
            "merge_commit_sha": null,
            "merged_by": null,
            "base": {
              "label": "main",
              "ref": "main",
              "sha": "85c7e78e6dfb63bcad4a0bb0953c0b3554ed0e93",
              "repo_id": 4,
              "repo": {
                "id": 4,
                "owner": {"id":2,"login":"my-project","full_name":"","email":"email-address@example.com","avatar_url":"b2653dbf52c7e078e04b8b20020eaadeafe0337787cc0e19b976efc8d594aefb","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T14:18:40Z","restricted":false,"username":"my-project"},
                "name": "my-repo",
                "full_name": "my-project/my-repo",
                "description": "",
                "empty": false,
                "private": false,
                "fork": false,
                "template": false,
                "parent": null,
                "mirror": false,
                "size": 4,
                "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
                "ssh_url": "git@my-instance-123456789-ssh.us-central1.sourcemanager.dev:my-project/my-repo.git",
                "clone_url": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
                "original_url": "",
                "website": "",
                "stars_count": 0,
                "forks_count": 0,
                "watchers_count": 1,
                "open_issues_count": 0,
                "open_pr_counter": 0,
                "release_counter": 1,
                "default_branch": "main",
                "archived": false,
                "created_at": "2023-06-06T20:34:36Z",
                "updated_at": "2024-07-03T18:27:42Z",
                "permissions": {
                  "admin": false,
                  "push": false,
                  "pull": false
                },
                "has_issues": true,
                "internal_tracker": {
                  "enable_time_tracker": false,
                  "allow_only_contributors_to_track_time": true,
                  "enable_issue_dependencies": true
                },
                "has_wiki": true,
                "has_pull_requests": true,
                "has_projects": true,
                "ignore_whitespace_conflicts": false,
                "allow_merge_commits": true,
                "allow_rebase": true,
                "allow_rebase_explicit": true,
                "allow_squash_merge": true,
                "avatar_url": "",
                "internal": false,
                "mirror_interval": "",
                "uris": {
                  "api": "https://my-instance-123456789-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
                  "html": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
                  "git_https": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git"
                }
              }
            },
            "head": {
              "label": "dev",
              "ref": "dev",
              "sha": "06aa2c971d8e06e5271ce04248ef1920341ce208",
              "repo_id": 4,
              "repo": {
                "id": 4,
                "owner": {"id":2,"login":"my-project","full_name":"","email":"email-address@example.com","avatar_url":"b2653dbf52c7e078e04b8b20020eaadeafe0337787cc0e19b976efc8d594aefb","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T14:18:40Z","restricted":false,"username":"my-project"},
                "name": "my-repo",
                "full_name": "my-project/my-repo",
                "description": "",
                "empty": false,
                "private": false,
                "fork": false,
                "template": false,
                "parent": null,
                "mirror": false,
                "size": 4,
                "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
                "ssh_url": "git@my-instance-123456789-ssh.us-central1.sourcemanager.dev:my-project/my-repo.git",
                "clone_url": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
                "original_url": "",
                "website": "",
                "stars_count": 0,
                "forks_count": 0,
                "watchers_count": 1,
                "open_issues_count": 0,
                "open_pr_counter": 0,
                "release_counter": 1,
                "default_branch": "main",
                "archived": false,
                "created_at": "2023-06-06T20:34:36Z",
                "updated_at": "2024-07-03T18:27:42Z",
                "permissions": {
                  "admin": false,
                  "push": false,
                  "pull": false
                },
                "has_issues": true,
                "internal_tracker": {
                  "enable_time_tracker": false,
                  "allow_only_contributors_to_track_time": true,
                  "enable_issue_dependencies": true
                },
                "has_wiki": true,
                "has_pull_requests": true,
                "has_projects": true,
                "ignore_whitespace_conflicts": false,
                "allow_merge_commits": true,
                "allow_rebase": true,
                "allow_rebase_explicit": true,
                "allow_squash_merge": true,
                "avatar_url": "",
                "internal": false,
                "mirror_interval": "",
                "uris": {
                  "api": "https://my-instance-123456789-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
                  "html": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
                  "git_https": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git"
                }
              }
            },
            "merge_base": "af065efa8d3d7549154c560da5cb3ec236ad3002",
            "due_date": null,
            "created_at": "2024-07-03T18:40:21Z",
            "updated_at": "2024-07-03T18:40:21Z",
            "closed_at": null
          },
          "repository": {
            "id": 4,
            "owner": {"id":2,"login":"my-project","full_name":"","email":"email-address@example.com","avatar_url":"b2653dbf52c7e078e04b8b20020eaadeafe0337787cc0e19b976efc8d594aefb","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T14:18:40Z","restricted":false,"username":"my-project"},
            "name": "my-repo",
            "full_name": "my-project/my-repo",
            "description": "",
            "empty": false,
            "private": false,
            "fork": false,
            "template": false,
            "parent": null,
            "mirror": false,
            "size": 4,
            "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
            "ssh_url": "git@my-instance-123456789-ssh.us-central1.sourcemanager.dev:my-project/my-repo.git",
            "clone_url": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
            "original_url": "",
            "website": "",
            "stars_count": 0,
            "forks_count": 0,
            "watchers_count": 1,
            "open_issues_count": 0,
            "open_pr_counter": 1,
            "release_counter": 1,
            "default_branch": "main",
            "archived": false,
            "created_at": "2023-06-06T20:34:36Z",
            "updated_at": "2024-07-03T18:27:42Z",
            "permissions": {
              "admin": false,
              "push": false,
              "pull": true
            },
            "has_issues": true,
            "internal_tracker": {
              "enable_time_tracker": false,
              "allow_only_contributors_to_track_time": true,
              "enable_issue_dependencies": true
            },
            "has_wiki": true,
            "has_pull_requests": true,
            "has_projects": true,
            "ignore_whitespace_conflicts": false,
            "allow_merge_commits": true,
            "allow_rebase": true,
            "allow_rebase_explicit": true,
            "allow_squash_merge": true,
            "avatar_url": "",
            "internal": false,
            "mirror_interval": "",
            "uris": {
              "api": "https://my-instance-123456789-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
              "html": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
              "git_https": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git"
            }
          },
          "sender": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://this-is-avatar.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"},
          "review": null
        }
        

### Pull request comment event payload

The content of a pull request comment event payload is similar to the following:

#### Header
    
    
          Request URL: https://example.com?{sensitive_query_string_placeholder}
          Request method: POST
          Content-Type: application/json
          X-SecureSourceManager-Delivery: d7bb9273-17cf-431d-835c-b334c9702eee
          X-SecureSourceManager-Event: pull_request_comment
          X-SecureSourceManager-Signature:
        

#### Body
    
    
        {
          "secret": "",
          "action": "created",
          "issue": {
            "id": 18,
            "url": "https://my-instance-123456789-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo/issues/4",
            "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/pulls/4",
            "number": 4,
            "user": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://page-address.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"},
            "original_author": "",
            "original_author_id": 0,
            "title": "Open a Pull Request'",
            "body": "This is the description of the pull request.",
            "ref": "",
            "labels": [],
            "milestone": null,
            "assignee": null,
            "assignees": null,
            "state": "open",
            "is_locked": false,
            "comments": 1,
            "created_at": "2024-07-03T18:40:21Z",
            "updated_at": "2024-07-03T18:40:21Z",
            "closed_at": null,
            "due_date": null,
            "pull_request": {
              "merged": false,
              "merged_at": null
            },
            "repository": {
              "id": 4,
              "name": "my-repo",
              "owner": "my-project",
              "full_name": "my-project/my-repo"
            },
            "etag": "PSIsycnIx2xBaS1CtNRhB0qY-NCtxuHIeYlo8H12E1Q"
          },
          "comment": {
            "id": 1,
            "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/pulls/4#issuecomment-1",
            "pull_request_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo/pulls/4",
            "issue_url": "",
            "user": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://page-address.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"},
            "original_author": "",
            "original_author_id": 0,
            "body": "this is a comment",
            "created_at": "2024-07-03T18:40:21Z",
            "updated_at": "2024-07-03T18:40:21Z"
          },
          "repository": {
            "id": 4,
            "owner": {"id":2,"login":"my-project","full_name":"","email":"email-address@example.com","avatar_url":"b2653dbf52c7e078e04b8b20020eaadeafe0337787cc0e19b976efc8d594aefb","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T14:18:40Z","restricted":false,"username":"my-project"},
            "name": "my-repo",
            "full_name": "my-project/my-repo",
            "description": "",
            "empty": false,
            "private": false,
            "fork": false,
            "template": false,
            "parent": null,
            "mirror": false,
            "size": 4,
            "html_url": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
            "ssh_url": "git@my-instance-123456789-ssh.us-central1.sourcemanager.dev:my-project/my-repo.git",
            "clone_url": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
            "original_url": "",
            "website": "",
            "stars_count": 0,
            "forks_count": 0,
            "watchers_count": 1,
            "open_issues_count": 0,
            "open_pr_counter": 1,
            "release_counter": 1,
            "default_branch": "main",
            "archived": false,
            "created_at": "2023-06-06T20:34:36Z",
            "updated_at": "2024-07-03T18:27:42Z",
            "permissions": {
              "admin": false,
              "push": false,
              "pull": true
            },
            "has_issues": true,
            "internal_tracker": {
              "enable_time_tracker": false,
              "allow_only_contributors_to_track_time": true,
              "enable_issue_dependencies": true
            },
            "has_wiki": true,
            "has_pull_requests": true,
            "has_projects": true,
            "ignore_whitespace_conflicts": false,
            "allow_merge_commits": true,
            "allow_rebase": true,
            "allow_rebase_explicit": true,
            "allow_squash_merge": true,
            "avatar_url": "",
            "internal": false,
            "mirror_interval": "",
            "uris": {
              "api": "https://my-instance-123456789-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
              "html": "https://my-instance-123456789.us-central1.sourcemanager.dev/my-project/my-repo",
              "git_https": "https://my-instance-123456789-git.us-central1.sourcemanager.dev/my-project/my-repo.git"
            }
          },
          "sender": {"id":4,"login":"user@example.com","full_name":"user","email":"user@example.com","avatar_url":"https://this-is-avatar.com","language":"","is_admin":false,"last_login":"0001-01-01T00:00:00Z","created":"2023-06-02T20:53:58Z","restricted":false,"username":"user@example.com"},
          "is_pull": true
        }
        

## What's next

  * Use webhooks to [connect to Jenkins](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins).
  * [Set up webhooks](https://docs.cloud.google.com/secure-source-manager/docs/set-up-webhooks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
