---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/
title: Dataform API: Nodejs Client \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:40.470552+00:00
---

# Dataform API: Nodejs Client  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Dataform API: Nodejs Client Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

This library is considered to be in **preview**. This means it is still a work-in-progress and under active development. Any release is subject to backwards-incompatible changes at any time.

[![npm version](https://img.shields.io/npm/v/@google-cloud/dataform.svg)](https://www.npmjs.org/package/@google-cloud/dataform)

Dataform API client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/CHANGELOG.md).

  * [Dataform API Nodejs Client API Reference](https://cloud.google.com/nodejs/docs/reference/dataform/latest)
  * [Dataform API Documentation](https://cloud.google.com/dataform/docs/overview)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart

    * Before you begin
    * Installing the client library
  * Versioning

  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Dataform API API](https://console.cloud.google.com/flows/enableapi?apiid=dataform.googleapis.com).
  4. [Set up authentication](https://cloud.google.com/docs/authentication/external/set-up-adc-local) so you can access the API from your local workstation. ### Installing the client library


    
    
    npm install @google-cloud/dataform
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code  
---|---  
cancel workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.cancel_workflow_invocation.js)  
commit repository changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.commit_repository_changes.js)  
commit workspace changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.commit_workspace_changes.js)  
compute repository access token status | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.compute_repository_access_token_status.js)  
create compilation result | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_compilation_result.js)  
create folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_folder.js)  
create release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_release_config.js)  
create repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_repository.js)  
create team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_team_folder.js)  
create workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_workflow_config.js)  
create workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_workflow_invocation.js)  
create workspace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.create_workspace.js)  
delete folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_folder.js)  
delete folder tree | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_folder_tree.js)  
delete release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_release_config.js)  
delete repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_repository.js)  
delete team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_team_folder.js)  
delete team folder tree | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_team_folder_tree.js)  
delete workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_workflow_config.js)  
delete workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_workflow_invocation.js)  
delete workspace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.delete_workspace.js)  
fetch file diff | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.fetch_file_diff.js)  
fetch file git statuses | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.fetch_file_git_statuses.js)  
fetch git ahead behind | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.fetch_git_ahead_behind.js)  
fetch remote branches | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.fetch_remote_branches.js)  
fetch repository history | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.fetch_repository_history.js)  
get compilation result | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_compilation_result.js)  
get config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_config.js)  
get folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_folder.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_iam_policy.js)  
get release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_release_config.js)  
get repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_repository.js)  
get team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_team_folder.js)  
get workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_workflow_config.js)  
get workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_workflow_invocation.js)  
get workspace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.get_workspace.js)  
install npm packages | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.install_npm_packages.js)  
list compilation results | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.list_compilation_results.js)  
list release configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.list_release_configs.js)  
list repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.list_repositories.js)  
list workflow configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.list_workflow_configs.js)  
list workflow invocations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.list_workflow_invocations.js)  
list workspaces | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.list_workspaces.js)  
make directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.make_directory.js)  
move directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.move_directory.js)  
move file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.move_file.js)  
move folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.move_folder.js)  
move repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.move_repository.js)  
pull git commits | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.pull_git_commits.js)  
push git commits | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.push_git_commits.js)  
query compilation result actions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_compilation_result_actions.js)  
query directory contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_directory_contents.js)  
query folder contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_folder_contents.js)  
query repository directory contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_repository_directory_contents.js)  
query team folder contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_team_folder_contents.js)  
query user root contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_user_root_contents.js)  
query workflow invocation actions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.query_workflow_invocation_actions.js)  
read file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.read_file.js)  
read repository file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.read_repository_file.js)  
remove directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.remove_directory.js)  
remove file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.remove_file.js)  
reset workspace changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.reset_workspace_changes.js)  
search files | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.search_files.js)  
search team folders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.search_team_folders.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.test_iam_permissions.js)  
update config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.update_config.js)  
update folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.update_folder.js)  
update release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.update_release_config.js)  
update repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.update_repository.js)  
update team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.update_team_folder.js)  
update workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.update_workflow_config.js)  
write file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1/dataform.write_file.js)  
cancel workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.cancel_workflow_invocation.js)  
commit repository changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.commit_repository_changes.js)  
commit workspace changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.commit_workspace_changes.js)  
compute repository access token status | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.compute_repository_access_token_status.js)  
create compilation result | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_compilation_result.js)  
create folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_folder.js)  
create release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_release_config.js)  
create repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_repository.js)  
create team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_team_folder.js)  
create workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_workflow_config.js)  
create workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_workflow_invocation.js)  
create workspace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.create_workspace.js)  
delete folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_folder.js)  
delete release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_release_config.js)  
delete repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_repository.js)  
delete team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_team_folder.js)  
delete workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_workflow_config.js)  
delete workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_workflow_invocation.js)  
delete workspace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.delete_workspace.js)  
fetch file diff | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.fetch_file_diff.js)  
fetch file git statuses | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.fetch_file_git_statuses.js)  
fetch git ahead behind | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.fetch_git_ahead_behind.js)  
fetch remote branches | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.fetch_remote_branches.js)  
fetch repository history | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.fetch_repository_history.js)  
get compilation result | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_compilation_result.js)  
get config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_config.js)  
get folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_folder.js)  
get iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_iam_policy.js)  
get release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_release_config.js)  
get repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_repository.js)  
get team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_team_folder.js)  
get workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_workflow_config.js)  
get workflow invocation | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_workflow_invocation.js)  
get workspace | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.get_workspace.js)  
install npm packages | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.install_npm_packages.js)  
list compilation results | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.list_compilation_results.js)  
list release configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.list_release_configs.js)  
list repositories | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.list_repositories.js)  
list workflow configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.list_workflow_configs.js)  
list workflow invocations | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.list_workflow_invocations.js)  
list workspaces | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.list_workspaces.js)  
make directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.make_directory.js)  
move directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.move_directory.js)  
move file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.move_file.js)  
move folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.move_folder.js)  
move repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.move_repository.js)  
pull git commits | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.pull_git_commits.js)  
push git commits | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.push_git_commits.js)  
query compilation result actions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_compilation_result_actions.js)  
query directory contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_directory_contents.js)  
query folder contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_folder_contents.js)  
query repository directory contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_repository_directory_contents.js)  
query team folder contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_team_folder_contents.js)  
query user root contents | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_user_root_contents.js)  
query workflow invocation actions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.query_workflow_invocation_actions.js)  
read file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.read_file.js)  
read repository file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.read_repository_file.js)  
remove directory | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.remove_directory.js)  
remove file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.remove_file.js)  
reset workspace changes | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.reset_workspace_changes.js)  
search files | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.search_files.js)  
search team folders | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.search_team_folders.js)  
set iam policy | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.set_iam_policy.js)  
test iam permissions | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.test_iam_permissions.js)  
update config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.update_config.js)  
update folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.update_folder.js)  
update release config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.update_release_config.js)  
update repository | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.update_repository.js)  
update team folder | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.update_team_folder.js)  
update workflow config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.update_workflow_config.js)  
write file | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-dataform/samples/generated/v1beta1/dataform.write_file.js)  
  
## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://github.com/nodejs/release#release-schedule). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/dataform@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md` and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template.

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
