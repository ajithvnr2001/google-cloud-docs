---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/integrations/use-backupdr-mcp/
title: Use the Backup and DR local MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:30:59.805839+00:00
---

# Use the Backup and DR local MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/integrations/use-backupdr-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Use the Backup and DR local MCP server Stay organized with collections  Save and categorize content based on your preferences. 

The Backup and DR Local Model Context Protocol (MCP) server enables AI assistants and LLM-powered applications to interact securely with your backup environment. By running the server locally, you can use generative AI to manage Backup and DR tasks—such as creating backup vaults and backup plans, or enabling alert notifications—using natural language prompts while maintaining control over your local environment. [Learn more how you can use MCP servers to interact across Google Cloud services](https://docs.cloud.google.com/mcp/overview).

The Backup and DR local MCP server acts as a bridge between an MCP-compatible host (such as Gemini CLI, ChatGPT, or Claude Code) and the Google Cloud Backup and DR API.

Because the server runs on your workstation, the AI can use your local credentials and network path to communicate directly with Google Cloud.

The Backup and DR local MCP server provides the following benefits:

  * **AI-driven management** : Use natural language prompts to automate and simplify complex Backup and DR tasks.
  * **Security** : Your data stays within your defined perimeters. The local server uses your existing [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) authentication.
  * **Simplified troubleshooting** : Identify and alert users for backup and restore job failures, and get remediation steps to fix errors.
  * **Centralized discovery** : Interact across multiple Google Cloud services, such as Cloud Monitoring, Cloud Storage, and BigQuery, using the same MCP environment.



## Before you begin

Before setting up the local MCP server for Backup and DR, ensure you have the following:

  * A **Google Cloud project** with the Backup and DR, Compute Engine, and Cloud SQL APIs enabled.
  * An **MCP host** , such as the Gemini CLI.
  * A **local environment** with the following: 
    * Node.js (v20+)
    * The Google Cloud SDK ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)) initialized and authenticated.



### Required permissions

Users need relevant Identity and Access Management (IAM) roles and permissions to perform the corresponding tasks using local MCP server. For example:

  * `roles/backupdr.viewer` (to query metadata information and status)
  * `roles/backupdr.restoreUser` (to trigger restores)



## Set up the local MCP server

To install the Gemini CLI and set up the Backup and DR local MCP server, follow these steps:

  1. Install the Gemini CLI

To integrate the Backup and DR local MCP server with the Gemini CLI or Gemini Code Assist, run this setup command. This will install the MCP server as a Gemini CLI extension for the current user, making it available for all your projects.
         
         npm install -g @google/gemini-cli
         

For more information, see <https://geminicli.com/docs/get-started/installation>.

  2. Set up the Backup and DR local MCP server

To install the Backup and DR MCP server run this command. By default it installs the server in `READ_ONLY` access level.
         
         npx @google-cloud/backupdr-mcp init --agent=gemini-cli
         

After the installation process, you can verify that the Backup and DR MCP server is configured correctly by running the following command:
         
         gemini mcp list
         

The output should show a status similar to the following:
         
         > ✓ backupdr (from @google-cloud/backupdr-mcp): npx -y backupdr-mcp --access-level READ_ONLY (stdio) - Connected
         

  3. Configure the local MCP server

You can customize the MCP server behavior using the following flags.

     1. Configure the access level.

The access level controls which tools are available to the AI agent.

        * **Flag** : `--access-level`
        * **Values** : `READ_ONLY` (default), `UPSERT`, `ALL`

        * **READ_ONLY** : Provides read-only tools for discovery and inspection.
              
              npx @google-cloud/backupdr-mcp init --agent=gemini-cli --access-level=READ_ONLY
              

        * **UPSERT** : Provides discovery, inspection, creation, and update tools (including restores).
              
              npx @google-cloud/backupdr-mcp init --agent=gemini-cli --access-level=UPSERT
              

        * **ALL** : Provides all tools, including destructive operations like deletion.
              
              npx @google-cloud/backupdr-mcp init --agent=gemini-cli --access-level=ALL
              

     2. Configure the context file

Context files are a powerful feature for providing instructional context to the Gemini model. The Backup and DR MCP server comes with some context information on how to use tools and common workflows.

     * **Flag** : `--overwrite-context-file`
     * **Values** : `true`, `false` (default)
     * **Location** : `~/.gemini/backupdr-mcp/GEMINI.md`

By default, the context file is only created if it doesn't already exist. To install the MCP server by overwriting the context file, run the following command:
    
    npx @google-cloud/backupdr-mcp init --agent=gemini-cli --overwrite-context-file=true
    

When `--overwrite-context-file` is set to false, on extension installation the context will be created only if it doesn't already exist in the directory.

To install the local MCP server without overwriting the context file, run the following command:
    
    npx @google-cloud/backupdr-mcp init --agent=gemini-cli --overwrite-context-file=false
    

For more details, see [Provide context with GEMINI.md files](https://geminicli.com/docs/cli/gemini-md/).

  4. Configure user authentication and authorization

The MCP server uses Application Default Credentials (ADC) to perform operations. IAM checks applicable to Backup and DR are performed on the ADC. For more information about application default credentials see [Set up Application Default Credentials](https://docs.cloud.google.com/sdk/docs/authorizing#adc).

     1. To configure your credentials run the following command:
            
            gcloud auth application-default login
            

     2. To use service account credentials instead of your own, impersonate a service account using Application Default Credentials (ADC). Run the following command to impersonate a service account:
            
            gcloud auth application-default login --impersonate-service-account [SERVICE_ACCOUNT_EMAIL]
            

**Note:** To use the service account, you need to have the Service Account Token Creator Role (`roles/iam.serviceAccountTokenCreator`) on the service account. IAM roles needed for the actions that you want to perform using the MCP server should be assigned to the service account.



## Available tools

The Backup and DR local MCP server includes the following tools.

### Read-only tools

These tools allow for discovery and inspection of Backup and DR resources without allowing any edits.

Tool | Description  
---|---  
`list_backup_vaults` | Lists all backup vaults in a project and location.  
`get_backup_vault` | Gets details of a specific backup vault.  
`list_backup_plans` | Lists all backup plans in a project and location.  
`get_backup_plan` | Gets details of a specific backup plan.  
`list_backup_plan_associations` | Lists all associations between backup plans and resources.  
`get_backup_plan_association` | Gets details of a specific backup plan association.  
`list_datasources` | Lists all data sources within a backup vault.  
`get_datasource` | Gets details of a specific data source.  
`list_backups` | Lists all backups for a given data source.  
`get_backup` | Gets details of a specific backup.  
`find_protectable_resources` | Discovers resources (VMs, Disks, SQL) that can be protected.  
`get_backupdr_operation` | Retrieves the status of a long-running Backup and DR operation.  
`get_csql_operation` | Retrieves the status of a long-running Cloud SQL operation.  
  
### Upsert tools

These tools allow creating and updating resources, including restore operations.

Tool | Description  
---|---  
`create_backup_vault` | Creates a new backup vault in a specified location.  
`create_backup_plan` | Creates a new backup plan with rules and retention.  
`update_backup_plan` | Modifies an existing backup plan.  
`create_backup_plan_association` | Associates a resource with a backup plan.  
`restore_backup` | Restores a backup to a target Compute Engine instance or disk.  
`csql_restore` | Restores a Cloud SQL backup to a target instance.  
  
### Delete tools

These tools include the ability to delete resources. Enable them only when necessary by setting the access level to `ALL`.

Tool | Description  
---|---  
`delete_backup_vault` | Deletes a backup vault.  
`delete_backup_plan` | Deletes a backup plan.  
`delete_backup_plan_association` | Removes protection from a resource.  
`delete_backup` | Deletes a specific backup from a vault.  
  
## Example prompts

Once the server is connected, you can use natural language prompts in your AI client to manage your backup environment.

  * **Assess backup health across a project**

"Show the list of unprotected resources in project PROJECT_ID for region LOCATION."

Replace the following:

    * `PROJECT_ID`: The project ID where you want to check backup health.
    * `LOCATION`: The region where your resources are located.
  * **Create a backup vault and backup plan**

"Create a backup vault named VAULT_NAME in LOCATION to protect resource RESOURCE_NAME using backup plan PLAN_NAME."

Replace the following:

    * `VAULT_NAME`: The name of the new backup vault.
    * `LOCATION`: The region where you want to create the vault.
    * `RESOURCE_NAME`: The name of the resource to protect.
    * `PLAN_NAME`: The name of the backup plan to apply.
  * **Audit backups for compliance**

"Audit all backups in the project PROJECT_ID in the region LOCATION. Once the audit is complete, compare the findings against my corporate backup policy to identify any compliance gaps."

Replace the following:

    * `PROJECT_ID`: The project ID to audit.
    * `LOCATION`: The region to audit.
  * **Root cause analysis for failures**

This prompt requires the `observability` tool. To install this MCP tool, see [Available MCP Tools](https://github.com/googleapis/gcloud-mcp?tab=readme-ov-file#-set-up-your-mcp-server) on GitHub.

"Identify and investigate the root cause of the resource RESOURCE_NAME backup failure in the last DURATION days in project PROJECT_ID."

Replace the following:

    * `RESOURCE_NAME`: The name of the resource with backup failures.
    * `DURATION`: The time window for the investigation (for example, `7`).
    * `PROJECT_ID`: The project ID where the failure occurred.
  * **Restore a backup**

"Restore the last successful backup for resource RESOURCE_NAME from project PROJECT_ID. Name the restored instance NEW_INSTANCE_NAME."

Replace the following:

    * `RESOURCE_NAME`: The name of the resource to restore.
    * `PROJECT_ID`: The project ID containing the backup.
    * `NEW_INSTANCE_NAME`: A name for the restored instance.
  * **Create an alert policy**

You can enable alerts for any combination of logs and added filters.

This prompt requires the `gcloud` tool. To install this MCP tool, see [Available MCP Tools](https://github.com/googleapis/gcloud-mcp?tab=readme-ov-file#-set-up-your-mcp-server) on GitHub.

"Create a log-based alert policy named ALERT_NAME to trigger on any log entry from `backupdr.googleapis.com` with severity `ERROR`. Send notification of the alerts immediately to EMAIL_ADDRESS."

Replace the following:

    * `ALERT_NAME`: A name for the new alert policy.
    * `EMAIL_ADDRESS`: The email to receive notifications.



## Access the server using other AI clients

You can use the Backup and DR MCP server with other clients.

  * To do this, add the following snippet to their respective JSON configuration files:
        
        "backupdr": {
          "command": "npx",
          "args": ["-y", "@google-cloud/backupdr-mcp"]
        }
        




Instructions for popular tools:

  * **Claude Desktop** : Open Claude > Settings > Developer > Edit Config and edit `claude_desktop_config.json`.
  * **Cline** : Click the MCP Servers icon, then Configure MCP Servers to edit `cline_mcp_settings.json`.
  * **Cursor** : Edit `.cursor/mcp.json` for a single project or `~/.cursor/mcp.json` for all projects.
  * **Gemini CLI (Manual Setup)** : If not using extensions, edit `.gemini/settings.json` for a single project or `~/.gemini/settings.json` for all projects.

  * For Visual Studio Code, edit the `.vscode/mcp.json` file in your workspace for a single project or your global user settings file for all projects:
        
        "servers": {
          "backupdr": {
            "command": "npx",
            "args": ["-y", "@google-cloud/backupdr-mcp"]
          }
        }
        




## Disclaimer

AI-assisted operations are still evolving; while we prioritize accuracy, remain mindful that model-driven outputs can include inaccuracies and should always be reviewed for correctness.

## What's next

  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).
  * Refer to the [Gemini CLI documentation](https://geminicli.com/docs/get-started/installation).
  * Learn more about [Application Default Credentials](https://docs.cloud.google.com/sdk/docs/authorizing#adc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
