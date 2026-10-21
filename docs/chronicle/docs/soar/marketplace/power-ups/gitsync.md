---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync/
title: GitSync \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:54.266101+00:00
---

# GitSync  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GitSync

**Mandatory platform requirement:** Starting with GitSync version 53.0, this integration communicates with Google Security Operations exclusively through **Chronicle REST APIs** using automated IAM authentication. Support for legacy Google SecOps platform API endpoints (`*.siemplify-soar.com/api/`) has been removed, and all GitSync actions and jobs fail on unmigrated instances. 

You must complete your platform migration before upgrading or configuring GitSync. For migration instructions, see Chronicle API-enabled environment migration.

GitSync is an integration built for Google SecOps that synchronizes security automation assets and components with an external Git repository (such as GitHub, GitLab, or Bitbucket). It facilitates bidirectional synchronization of content, providing automated version control, configuration backup, and cross-environment promotion across your security operations lifecycle. Notice that GitSync is designed to backup and migrate assets between related environments (such as development, staging, and production), rather than to distribute assets across unrelated systems where internal database identifiers may cause conflict.

## Use cases

The **GitSync** integration supports the following primary use cases:

  * **Version control and auditability (Security as Code)** : Track modifications, review diffs, and maintain a complete version history of changes across playbooks, connectors, integrations, and system settings.

  * **Multi-environment promotion (CI/CD pipeline)** : Promote playbooks, ontology mappings, and integration settings systematically from development and staging environments to production through pull requests and branch merges.

  * **Backup and disaster recovery** : Restore accidentally deleted, corrupted, or misconfigured playbooks and platform configurations directly from your Git repository.

  * **Cross-environment standardization** : Distribute standardized playbooks, custom visual families, and connector definitions across related Google SecOps environments from a centralized repository.

  * **Branching and staging isolation** : Test experimental playbooks and feature branches in dedicated environments without affecting production workflows or schedules.

  * **Offline review and collaboration** : Export platform definitions as JSON and Markdown to enable peer review, automated validation, and inspection in standard developer tools.

  * **Reusable workflow blocks** : Synchronize modular workflow blocks alongside or separately from full playbooks so teams can share common automation steps.




## Implementation workflows by goal

To go directly to the guidance matching your current objective, select your workflow:

  * **New GitSync deployment or new branch** : If you're configuring the GitSync integration for the first time or creating a new repository branch on a Chronicle API-enabled environment, follow this end-to-end setup sequence:

    1. Complete the prerequisites and credentials setup.
    2. Configure the shared integration instance.
    3. Test network connectivity and authentication with the Ping action.
    4. Run an initial Push Content job to populate the branch before running any pull jobs.
    5. Configure and schedule automated synchronization jobs.
  * **Migrate to Chronicle API (mandatory for existing deployments)** : To migrate an existing GitSync integration and repository branch after moving to a Chronicle API-enabled environment, see Chronicle API-enabled environment migration.

  * **Job and repository reference** :

    * To view configuration parameters and run standalone push or pull jobs for specific assets (playbooks, connectors, integrations, etc.), see Jobs.
    * To view the standard repository layout, see Repository directory structure.
  * **Troubleshoot synchronization issues** : If an action or job fails with an error, see Troubleshooting.




## Before you begin

Before configuring and executing GitSync operations, verify your environment, obtain repository access, and complete the following setup tasks:

  * **Verify your Chronicle API-enabled environment (required for GitSync v53.0 and later)** : Check your browser's web console URL to confirm your instance is hosted on `secops.google.com` or `*.chronicle.security.google.com` (or verify that `Google.com` appears after the system version number in **Settings > SOAR Settings > License Management**). If your instance is still hosted on `*.siemplify-soar.com`, complete the Chronicle API-enabled environment migration first.

  * **Use a private Git repository with write access** : Make sure you have write permissions to a **private** remote Git repository hosted on a supported Git provider (such as GitHub, GitLab, or Bitbucket). While `Password`-type parameters are excluded by default unless `Commit Passwords` is enabled, all other parameters (such as Application IDs, Client IDs, usernames, and endpoints) are exported in plaintext. Never use a public repository with GitSync.

  * **Initialize the remote repository** : Confirm that the remote repository has at least one initial commit (such as a `README.md` or `.gitignore` file). GitSync cannot synchronize to an empty repository.

  * **Prepare Git authentication credentials** : Generate an authentication credential with repository write permissions. GitSync supports base64-encoded SSH private keys (recommended), Personal Access Tokens (PATs), and basic username and password credentials.

To generate and encode an SSH key, see Generate SSH keys for GitSync.

  * **Verify network connectivity and VPC Service Controls** : Verify that your Google SecOps instance or remote runner has outbound firewall access on TCP port 443 (for HTTPS) or TCP port 22 (for SSH) to your Git provider.

If your Google Cloud environment uses a [VPC Service Controls service perimeter](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops), work with your Google Cloud administrator to configure [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) so that response integrations can communicate with required Google Cloud APIs and external endpoints.

  * **Obtain your Git host fingerprint (recommended)** : To protect against person-in-the-middle (PITM) attacks, retrieve your Git server's public key fingerprint for host fingerprint pinning.

For configuration steps, see Enable host fingerprint pinning.

  * **Grant playbook edit permissions** : If you intend to synchronize playbooks with restricted default access (such as default permissions set to **Can View**), grant the `Administrator` SOC role **Can Edit** permissions on the source system before running synchronization jobs.

For step-by-step instructions, see Configure playbook permissions.




### Generate SSH keys for GitSync

To configure secure, passwordless authentication using SSH keys:

  1. Generate an RSA or Ed25519 key pair in your terminal. When prompted for a passphrase, press **Enter** to leave it empty:
         
         ssh-keygen -b 2048 -t rsa -f ./id_rsa
         

This command creates two files: `id_rsa` (private key) and `id_rsa.pub` (public key).

  2. Add the public key (`id_rsa.pub`) to your remote Git hosting service as a Deploy Key or Access Key with write permissions.

  3. Convert the private key into a single-line base64-encoded string:

     * **Linux / macOS** :
           
           base64 -w 0 ./id_rsa
           

     * **Windows (PowerShell)** :
           
           [Convert]::ToBase64String([System.IO.File]::ReadAllBytes(".\id_rsa"))
           

  4. Copy the resulting base64 string and paste it into the **Git Password/Token/SSH Key** parameter when configuring the GitSync integration instance.




### Enable host fingerprint pinning

Host fingerprint pinning verifies your Git server's identity upon connection to protect against person-in-the-middle (PITM) attacks. While the **Git Server Fingerprint** parameter is optional, configuring it ensures GitSync connects exclusively to your verified Git host.

To configure host fingerprint pinning:

  1. **Retrieve your host fingerprint** : Run `ssh-keyscan` in your terminal against your Git server hostname:
         
         ssh-keyscan -t rsa <hostname>
         

For example, for GitHub, run `ssh-keyscan -t rsa github.com`. The command outputs a public host key line similar to the following:
         
         github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC...
         

  2. **Save the fingerprint for configuration** : Copy the public host key line. Enter this value into the **Git Server Fingerprint** parameter when configuring the GitSync integration instance (to apply it to all jobs) or on individual synchronization jobs (to override the setting for specific hosts).




### Configure playbook permissions

When synchronizing playbooks with restricted permissions (for example, default permissions set to **Can View**), assign **Can Edit** permissions to the `Administrator` SOC role:

  1. In Google SecOps, go to **Playbooks** and select the target playbook.
  2. Open the playbook permissions settings.
  3. Add the **`Administrator` SOC role** to the list of entities and set its permission to **Can Edit**.



## Chronicle API-enabled environment migration

This section provides procedures for migrating an existing GitSync deployment and repository branch to a Chronicle API-enabled environment (supported starting in GitSync version 53.0).

For guidance on migrating your overall Google SecOps platform, identity groups, IAM permissions, and API endpoints to Google Cloud, see the [Google SecOps migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

### Updates in Chronicle API-enabled environments

Starting with version 53.0, GitSync includes the following updates for Chronicle API-enabled environments:

  * **Automated IAM authentication** : GitSync connects to Google SecOps through Chronicle REST APIs and authenticates automatically at runtime using Google Cloud IAM.

  * **Updated configuration schema** : Exported JSON configuration files use Chronicle API resource identifiers and field formats, making them incompatible with pre-migration repository branches.

  * **Dedicated block synchronization options** : Playbook synchronization jobs include an **Include Playbook Blocks** option to export or import reusable workflow blocks alongside playbooks, and support importing blocks from either `/Playbooks` or `/Blocks`.

  * **Direct archive transfers for custom integrations** : Custom integration packages are uploaded and downloaded directly as `.zip` archives, reducing transfer times for large integrations.

  * **Source-scoped ontology mappings** : Mapping rules are organized by integration source under `/Ontology/Mappings/<Source_Name>/` to prevent conflicts between mapping rules from different sources.

  * **Automatic filtering of built-in system defaults** : GitSync automatically excludes built-in, read-only system items (such as default system tags and built-in system instances) during synchronization to prevent permission errors.




### Migrate your repository branch

Chronicle API-enabled environments and legacy environments use different JSON configuration formats and cannot synchronize against the same branch simultaneously. Choose either a dedicated branch (recommended) or reuse your existing branch:

#### Option 1: Recommended dedicated branch workflow

Creating a new branch isolates your updated Chronicle API configurations and preserves an untouched archive of your pre-migration configurations without modifying branch history:

  1. **Baseline legacy push** : Before your instance is migrated, execute a full **Push Content** job from your existing environment to commit a clean backup to your legacy branch (for example, `main`).

  2. **Create new Git branch** : Create a new, dedicated branch in your Git repository (for example, `git checkout -b gitsync-chronicle-api && git push origin gitsync-chronicle-api`).

  3. **Upgrade and reconfigure the integration instance** : In your Chronicle API-enabled environment, make sure GitSync is updated to version 53.0 or later in the Content Hub. Then go to **Settings > Integrations > GitSync**, update the **Branch** parameter to `gitsync-chronicle-api`, and verify connectivity using the **Ping** action.

  4. **Initial API-enabled push baseline** : Execute a full **Push Content** job from the Chronicle API-enabled instance to populate the new branch with the updated configuration files.

  5. **Verify and enable pull sync** : Inspect the repository to verify file structures, then enable scheduled **Pull Content** jobs as required.




#### Option 2: Existing branch reuse procedure

If automated CI/CD pipelines or branch policies require retaining an existing branch name, execute the following cutover procedure:

**Branch protection rules:** GitSync pushes commits directly to the remote repository and doesn't create pull requests. If your existing branch (such as `main`) enforces branch protection rules that require pull requests or review approvals, direct push operations from GitSync fail. 

Before executing this procedure, make sure your repository administrator configures an exception allowing the GitSync deploy key or account to push directly to the branch, or use Option 1 with a dedicated branch and merge changes into `main` through your standard pull request workflow.

  1. **Create a legacy backup tag** : Create a Git release tag of your legacy configurations as a historical archive.
         
         git tag backup-legacy-pre-migration
         git push origin backup-legacy-pre-migration
         

  2. **Pause sync jobs** : Disable active GitSync scheduled jobs (**Push Content** and **Pull Content**) to prevent concurrent writes during cutover.

  3. **Remove legacy branch content** : Remove the legacy directories from the branch.
         
         git rm -rf Playbooks/ Connectors/ Integrations/ Jobs/ Ontology/ SimulatedCases/ Settings/
         git commit -m "CHORE: Clear legacy files for Chronicle API baseline"
         git push origin main
         

  4. **Upgrade GitSync and push API-enabled baseline** : In your Chronicle API-enabled instance, make sure GitSync is updated to version 53.0 or later in the Content Hub. Once verified, execute a full **Push Content** job to populate the clean branch with updated configuration files.

  5. **Resume scheduled sync** : Verify the exported files in your repository and re-enable scheduled GitSync jobs on the Chronicle API-enabled instance.


**Remediating synchronization issues during migration:** Platform migration to a Chronicle API-enabled environment is a one-way infrastructure transition and cannot be reverted to legacy endpoints. If you encounter authentication, permission, or synchronization errors during migration, consult the Troubleshooting section. 

## Configure the integration

Configure the GitSync integration as a **Shared Instance** in Google SecOps so that all platform components and scheduled jobs can access repository configurations.

**Notes for existing deployments and authentication:**

  * **Updating an existing instance:** You don't need to delete or recreate your shared instance after migrating to a Chronicle API-enabled environment. Verify that the GitSync package is updated to version 53.0 or later in Content Hub, update the **Branch** parameter if you're using a new branch, and test connectivity using the **Ping** action.
  * **Repository-only credentials:** Because platform API authentication is handled automatically using Google Cloud IAM, you only need to configure credentials for your remote Git repository.



### GitSync integration parameters

Parameter | Description  
---|---  
`Repo URL` | Required. The remote Git repository URL. When using HTTPS authentication, the URL must start with `https://` (for example, `https://github.com/organization/secops-platform.git`). When using SSH authentication, the URL must start with `git@` or `ssh://` (for example, `git@github.com:organization/secops-platform.git`).  
`Branch` | Required. The Git repository branch to synchronize with (such as `main` or `gitsync-chronicle-api`).  
`Git Password/Token/SSH Key` | Required. The authentication credential for the remote Git repository. This parameter accepts a Git account password, Personal Access Token (PAT), or base64-encoded SSH private key (RSA 2048-bit or Ed25519).  
`Git Username` | Optional. The Git account username. Required when using username and password authentication over HTTPS.  
`Git Server Fingerprint` | Optional. The SSH public host key of your remote Git server (for example, `github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC...`). Configuring this parameter enables host fingerprint pinning, making sure GitSync connects exclusively to your verified Git host and mitigating person-in-the-middle (PITM) risks. To retrieve this value, see Enable host fingerprint pinning.  
`Commit Author` | Optional. The author identity attached to outbound Git commits generated by GitSync. The format must follow standard Git authorship: `Name &lt;email@domain.com&gt;` (defaults to `GitSync &lt;gitsync@siemplify.co&gt;`).  
`Siemplify Verify SSL` | Required. If selected, the integration validates the SSL certificate of the Google SecOps API endpoint. Enabled by default.  
`Git Verify SSL` | Required. If selected, the integration validates the SSL certificate of the remote Git provider server. Enabled by default.  
  
## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test network connectivity and verify authentication credentials against the configured Git repository and branch.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed action "Ping".` | The action succeeded and repository connectivity was verified.  
`Error executing action "Ping". Reason: ERROR_REASON` | The action failed. Verify repository URL, branch name, credentials, or network routes.  
  
##### Script result

The following table lists the script result value when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Jobs

GitSync provides 16 synchronization job configurations (2 full instance jobs and 7 standalone job pairs) to manage platform assets. These jobs support the full instance-level and targeted standalone synchronization scopes.

### Synchronization scope and supported assets

The integration organizes synchronization jobs into two distinct operational scopes to meet different administrative and automation needs:

  * **Full instance synchronization (`Push Content` and `Pull Content`)**: Synchronizes your complete Google SecOps platform in a single bulk operation.

This encompasses 21 platform asset categories across three functional areas:

    * **System and environment configurations** : Environments, Domains, Dynamic Parameters, Custom Lists, Networks, Blacklists (Denylists), Case Title Settings, Email Templates, and Logo.

    * **Alert and case management** : Case Tags, Case Stages, Case Close Reasons, SLA Records, and Simulated Cases.

    * **Security automation and integrations** : Playbooks (including reusable workflow Blocks), Integrations, Integration Instances, Connectors, Scheduled Jobs, Ontology Mappings, and Visual Families.

  * **Granular asset synchronization (standalone push and pull jobs)** :

Provides dedicated push and pull job pairs for seven specific assets. Use standalone jobs when developing, updating, or testing individual components without synchronizing or overwriting the rest of your environment:

    * **Playbooks and workflow blocks** : `Push Playbook` and `Pull Playbook`

    * **Connectors** : `Push Connectors` and `Pull Connector`

    * **Integrations** : `Push Integration` and `Pull Integration`

    * **Scheduled jobs** : `Push Job` and `Pull Jobs`

    * **Ontology mappings** : `Push Mappings` and `Pull Mappings`

    * **Custom visual families** : `Push Custom Family` and `Pull Custom Family`

    * **Simulated test cases** : `Push Simulated Cases` and `Pull Simulated Cases`




### Repository directory structure

Running an initial **Push Content** job (required before running any pull jobs on a new or migrated branch) creates the following predefined directory structure, JSON configuration files, root `GitSync.json` metadata file, and generated `README.md` documentation in your remote Git repository.

**Don't modify the repository structure manually:** GitSync relies on this predefined directory layout and the root `GitSync.json` metadata file to track and resolve platform assets. Manually renaming files, moving directories, or restructuring the repository through custom commits can cause synchronization jobs to fail. 
    
    
    ├── Connectors/
    │   └── <Integration_Name>/
    │       └── <Connector_Name>/
    │           ├── <Connector_Name>.json
    │           └── README.md
    ├── Integrations/
    │   └── <Integration_Identifier>/
    │       ├── Actions/
    │       ├── Connectors/
    │       ├── Dependencies/
    │       ├── Jobs/
    │       ├── Managers/
    │       ├── Resources/
    │       ├── Integration-<Integration_Identifier>.def
    │       └── README.md
    ├── Jobs/
    │   ├── <Job_Name>.json
    │   └── README.md
    ├── Ontology/
    │   ├── Mappings/
    │   │   └── <Source_Name>/
    │   │       ├── <Source_Name>_Records.json
    │   │       ├── <Source_Name>_Rules.json
    │   │       └── README.md
    │   └── VisualFamilies/
    │       └── <Family_Name>/
    │           ├── <Family_Name>.json
    │           ├── <Family_Name>.png
    │           └── README.md
    ├── Playbooks/
    │   ├── README.md
    │   └── <Folder_Name>/
    │       └── <Playbook_Or_Block_Name>/
    │           ├── <Playbook_Or_Block_Name>.json
    │           └── README.md
    ├── Settings/
    │   ├── blacklists.json
    │   ├── caseCloseCauses.json
    │   ├── caseTitles.json
    │   ├── customLists.json
    │   ├── domains.json
    │   ├── dynamicParameters.json
    │   ├── emailTemplates.json
    │   ├── environments.json
    │   ├── integrationInstances.json
    │   ├── logo.json
    │   ├── networks.json
    │   ├── slaDefinitions.json
    │   ├── stages.json
    │   └── tags.json
    ├── SimulatedCases/
    │   └── <Case_Name>.case
    ├── GitSync.json
    └── README.md
    

### Instance-level synchronization jobs

Instance-level jobs synchronize selected asset categories across an entire Google SecOps instance.

#### Push Content

Use the **Push Content** job to export selected asset categories from your Google SecOps instance and commit them to the configured Git repository branch. Always run **Push Content** first when initializing a new branch or migrating to a Chronicle API-enabled environment.

##### Job inputs

To configure the **Push Content** job, use the following parameters:

Parameter | Description  
---|---  
`Commit` | Required. The Git commit message describing the exported content changes.  
`Commit Passwords` | Optional. If selected, the job exports plaintext `Password`-type parameters for configured integration instances, connectors, and jobs. **Caution:** Never enable this option on public or shared repositories, as it exposes plaintext credentials. Note that even when `Commit Passwords` is disabled, parameters that aren't of type `Password` (such as Application IDs, Client IDs, usernames, and URLs) are always exported in plaintext.   
**Asset selection parameters** :  
`Integrations`, `Playbooks`, `Jobs`, `Connectors`, `Simulated Cases`, `Integration Instances`, `Visual Families`, `Mappings`, `Environments`, `Dynamic Parameters`, `Logo`, `Case Tags`, `Case Stages`, `Case Title Settings`, `Case Close Reasons`, `Networks`, `Domains`, `Custom Lists`, `Email Templates`, `Blacklists`, `SLA Records` | Optional (Boolean toggles). Select each asset category you want to include in the export.  
`Repo URL` | Optional. Overrides the repository URL configured in the integration instance.  
`Branch` | Optional. Overrides the repository branch configured in the integration instance.  
`Commit Author` | Optional. Overrides the commit author configured in the integration instance. Must use the format `Name &lt;email@domain.com&gt;`.  
`Git Server Fingerprint` | Optional. Overrides the SSH host fingerprint configured in the integration instance.  
  
##### Job outputs

The job writes JSON configuration files and `README.md` summaries to the target Git branch under the standard directory hierarchy (`/Playbooks`, `/Connectors`, `/Integrations`, `/Jobs`, `/Ontology/Mappings`, `/Ontology/VisualFamilies`, `/SimulatedCases`, and `/Settings`) and outputs execution logs to the job runner console. Custom integrations are exported as complete packages, while commercial integrations export only custom scripts or modifications added to the integration.

#### Pull Content

Use the **Pull Content** job to retrieve selected configuration categories from the configured Git repository branch and apply them to the Google SecOps platform.

**Commercial integrations and job timeouts:** When importing integrations, GitSync imports custom integrations directly from the repository, but installs the latest version of commercial integrations from the Content Hub before applying any custom scripts. Installing multiple commercial integrations at once can exceed the 5-minute job execution timeout. To avoid timeouts, install required commercial integrations from Content Hub before running **Pull Content** , or re-run the **Pull Content** job if a timeout occurs. 

##### Job inputs

To configure the **Pull Content** job, use the following parameters:

Parameter | Description  
---|---  
**Asset selection parameters** :  
`Integrations`, `Playbooks`, `Jobs`, `Connectors`, `Simulated Cases`, `Integration Instances`, `Visual Families`, `Mappings`, `Environments`, `Dynamic Parameters`, `Logo`, `Case Tags`, `Case Stages`, `Case Title Settings`, `Case Close Reasons`, `Networks`, `Domains`, `Custom Lists`, `Email Templates`, `Blacklists`, `SLA Records` | Optional (Boolean toggles). Select each asset category you want to import from the repository into your environment.  
`Repo URL` | Optional. Overrides the repository URL configured in the integration instance.  
`Branch` | Optional. Overrides the repository branch configured in the integration instance.  
`Git Server Fingerprint` | Optional. Overrides the SSH host fingerprint configured in the integration instance.  
  
##### Job outputs

The job imports the selected repository definitions into the platform, creates or updates integration instances, playbooks, connectors, jobs, ontology mappings, and settings, and outputs execution logs to the job runner console.

### Standalone synchronization jobs

Standalone jobs allow granular synchronization of specific assets without requiring a full repository sync.

#### Push Playbook

Use the **Push Playbook** job to export individual playbooks or reusable workflow blocks to Git.

##### Job inputs

To configure the **Push Playbook** job, use the following parameters:

Parameter | Description  
---|---  
`Commit` | Required. The Git commit message describing the playbook changes.  
`Playbook Whitelist` | Optional. A comma-separated list of exact, case-sensitive playbook or block names to export. Provide either `Playbook Whitelist` or `Folders Whitelist`.  
`Folders Whitelist` | Optional. A comma-separated list of playbook folder (category) names. All playbooks and blocks residing within these folders are exported.  
`Include Playbook Blocks` | Optional. If selected, exports reusable workflow blocks alongside the selected playbooks, including any blocks referenced as steps within those playbooks.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
`Readme Addon` | Optional.Custom content appended to the generated `README.md` for all playbooks pushed in this run and saved in the root `GitSync.json` metadata file. Supports both Markdown syntax and Jinja templates.  
  
##### Job outputs

Exports selected playbooks and included workflow blocks to `/Playbooks/<Folder_Name>/<Playbook_Name>/` and updates `/Playbooks/README.md`.

#### Pull Playbook

Use the **Pull Playbook** job to import specific playbooks or blocks from Git.

##### Job inputs

To configure the **Pull Playbook** job, use the following parameters:

Parameter | Description  
---|---  
`Playbook Whitelist` | Required. A comma-separated list of exact playbook or block names to import from the repository.  
`Include Playbook Blocks` | Optional. If selected, automatically imports any reusable workflow blocks referenced by the selected playbooks.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Imports the specified playbooks and blocks from `/Playbooks` (or `/Blocks`) into the platform, installing referenced blocks first before installing the parent playbooks.

#### Push Connectors

Use the **Push Connectors** job to export connector configurations to Git.

##### Job inputs

To configure the **Push Connectors** job, use the following parameters:

Parameter | Description  
---|---  
`Connectors` | Required. A comma-separated list of connector display names to export.  
`Commit` | Required.The Git commit message.  
`Include Mappings` | Optional. If selected, exports the ontology mapping records and rules associated with the connector's integration to `/Ontology/Mappings`.  
`Include Visual Families` | Optional. If selected, exports the custom visual families associated with the connector's ontology records to `/Ontology/VisualFamilies`.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
`Readme Addon` | Optional.Custom content appended to the generated `README.md` for all connectors pushed in this run and saved in `GitSync.json`. Supports both Markdown syntax and Jinja templates.  
  
##### Job outputs

Exports connector settings and schedules to `/Connectors/<Integration_Name>/<Connector_Name>/` (along with associated ontology mappings and visual families, if selected).

#### Pull Connector

Use the **Pull Connector** job to import a connector configuration from Git. Before running this job, make sure the connector's underlying integration is already installed on the target environment.

##### Job inputs

To configure the **Pull Connector** job, use the following parameters:

Parameter | Description  
---|---  
`Connector Name` | Required. The display name of the connector to import from the repository.  
`Include Mappings` | Optional. If selected, imports the ontology mappings associated with the connector's integration.  
`Include Visual Families` | Optional. If selected, imports the custom visual families associated with the connector's integration.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Installs or updates the connector on the target environment (along with associated mappings or visual families, if selected).

#### Push Integration

Use the **Push Integration** job to export custom integrations or custom scripts added to commercial integrations to Git. Custom integrations are exported as full integration packages, whereas commercial integrations export only custom scripts or modifications added to the integration.

##### Job inputs

To configure the **Push Integration** job, use the following parameters:

Parameter | Description  
---|---  
`Push Whitelist` | Required. A comma-separated list of integration identifiers to export.  
`Commit` | Required.The Git commit message.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
`Readme Addon` | Optional.Custom content appended to the generated `README.md` for all integrations pushed in this run and saved in `GitSync.json`. Supports both Markdown syntax and Jinja templates.  
  
##### Job outputs

Exports integration definitions, custom scripts (`Actions/`, `Connectors/`, `Jobs/`, `Managers/`), dependencies, and `README.md` documentation to `/Integrations/<Integration_Identifier>/`.

#### Pull Integration

Use the **Pull Integration** job to import custom integrations or custom scripts for commercial integrations from Git. For commercial integrations, GitSync installs the latest version of the integration from Content Hub and saves the custom scripts into it.

##### Job inputs

To configure the **Pull Integration** job, use the following parameters:

Parameter | Description  
---|---  
`Install Whitelist` | Required. A comma-separated list of integration identifiers to import from the repository.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Installs custom integration packages or installs commercial integrations from Content Hub and updates their custom scripts on the target environment.

#### Push Job

Use the **Push Job** job to export scheduled platform job configurations to Git.

##### Job inputs

To configure the **Push Job** job, use the following parameters:

Parameter | Description  
---|---  
`Job Whitelist` | Required. A comma-separated list of scheduled job names to export.  
`Commit` | Required.The Git commit message.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
`Readme Addon` | Optional.Custom content appended to the generated `README.md` for all jobs pushed in this run and saved in `GitSync.json`. Supports both Markdown syntax and Jinja templates.  
  
##### Job outputs

Exports job parameters and schedule intervals to `/Jobs/<Job_Name>.json` and updates `/Jobs/README.md`.

#### Pull Jobs

Use the **Pull Jobs** job to import scheduled platform jobs from Git.

##### Job inputs

To configure the **Pull Jobs** job, use the following parameters:

Parameter | Description  
---|---  
`Job Whitelist` | Required. A comma-separated list of scheduled job names to import from the repository.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Configures and registers the specified scheduled jobs in the platform job scheduler.

#### Push Mappings

Use the **Push Mappings** job to export ontology event mapping records and rules for a specific source to Git.

##### Job inputs

To configure the **Push Mappings** job, use the following parameters:

Parameter | Description  
---|---  
`Source` | Required. The ontology source (integration name) whose mapping records and rules you want to export.  
`Commit` | Required.The Git commit message.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
`Readme Addon` | Optional.Custom content appended to the generated `README.md` for all mappings pushed in this run and saved in `GitSync.json`. Supports both Markdown syntax and Jinja templates.  
  
##### Job outputs

Writes ontology records (`<Source>_Records.json`), mapping rules (`<Source>_Rules.json`), and `README.md` to `/Ontology/Mappings/<Source>/`.

#### Pull Mappings

Use the **Pull Mappings** job to import ontology mapping records and rules for a specific source from Git.

##### Job inputs

To configure the **Pull Mappings** job, use the following parameters:

Parameter | Description  
---|---  
`Source` | Required. The ontology source (integration name) whose mapping records and rules you want to import.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Registers ontology mapping rules and visual family assignments in the platform ontology settings. Mappings appear in the Ontology Status table after corresponding events are ingested.

#### Push Custom Family

Use the **Push Custom Family** job to export custom visual family definitions and icons to Git.

##### Job inputs

To configure the **Push Custom Family** job, use the following parameters:

Parameter | Description  
---|---  
`Family Name` | Required. A comma-separated list of custom visual family names to export.  
`Commit` | Required.The Git commit message.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
`Readme Addon` | Optional.Custom content appended to the generated `README.md` for all custom visual families pushed in this run and saved in `GitSync.json`. Supports both Markdown syntax and Jinja templates.  
  
##### Job outputs

Exports visual family definitions (`<Family_Name>.json`), icon image files (`<Family_Name>.png`), and `README.md` to `/Ontology/VisualFamilies/<Family_Name>/`.

#### Pull Custom Family

Use the **Pull Custom Family** job to import a custom visual family definition and icon from Git.

##### Job inputs

To configure the **Pull Custom Family** job, use the following parameters:

Parameter | Description  
---|---  
`Family Name` | Required. The exact name of the custom visual family to import.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Imports the custom visual family definition and icon into the platform ontology settings.

#### Push Simulated Cases

Use the **Push Simulated Cases** job to export simulated test cases to Git.

##### Job inputs

To configure the **Push Simulated Cases** job, use the following parameters:

Parameter | Description  
---|---  
`Simulated Cases` | Required. A comma-separated list of simulated case names to export.  
`Commit` | Required.The Git commit message.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Commit Author` | Optional.Overrides the default commit author.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Exports simulated cases as `.case` files to `/SimulatedCases/<Case_Name>.case`.

#### Pull Simulated Cases

Use the **Pull Simulated Cases** job to import simulated test cases from Git.

##### Job inputs

To configure the **Pull Simulated Cases** job, use the following parameters:

Parameter | Description  
---|---  
`Simulated Cases` | Required. A comma-separated list of simulated case names to import from the repository.  
`Repo URL` | Optional.Overrides the default repository URL.  
`Branch` | Optional.Overrides the default branch.  
`Git Server Fingerprint` | Optional.Overrides the default SSH host fingerprint.  
  
##### Job outputs

Imports the specified simulated cases into the platform's simulated cases catalog.

## Troubleshooting

The following table provides remediation steps for common synchronization errors:

Observed error message | Operational cause | Remediation procedure  
---|---|---  
`Authentication failed`, `401 Unauthorized`, or `Connection refused` during action or job execution | Running this integration on an unmigrated legacy instance (`*.siemplify-soar.com`). GitSync communicates with Google SecOps exclusively through Chronicle REST APIs using Google Cloud IAM authentication and no longer supports legacy platform API endpoints (`*.siemplify-soar.com/api/`). | Migrate your Google SecOps platform instance to a Chronicle API-enabled environment (accessible using `secops.google.com` or `*.chronicle.security.google.com`). For migration instructions, see Chronicle API-enabled environment migration.  
`Permission denied (publickey)` or `Host key verification failed` (or `Authentication failed for 'https://...'`) | Git authentication failure caused by an invalid credential format, missing deploy key write permissions, or mismatched host fingerprint. | 

  * **SSH authentication** : Verify that your private SSH key is converted to a single-line base64 string without trailing newlines or whitespace. Confirm that the corresponding public key is registered in your Git repository with write access.
  * **Host fingerprint** : If host fingerprint pinning is enabled, verify the fingerprint string using `ssh-keyscan -t rsa <hostname>` and update the **Git Server Fingerprint** parameter.
  * **HTTPS authentication** : Verify that your Personal Access Token (PAT) hasn't expired and possesses repository write scope.

  
`403 Forbidden: Insufficient permissions to modify playbook` (or `Failed to push playbook: Access denied`) | The target playbook has restricted default access permissions (such as **Can View**), and the `Administrator` SOC role hasn't been granted **Can Edit** permissions on the source system. | In Google SecOps, go to **Playbooks** , select the affected playbook, open its permissions settings, and add the **`Administrator` SOC role** with **Can Edit** permissions. For detailed steps, see Configure playbook permissions.  
**Pull Content** or **Pull Integration** job times out after 5 minutes | Installing multiple commercial integrations from Content Hub during a single pull operation exceeded the 5-minute job execution timeout. | Install the required commercial integrations manually from Content Hub before running **Pull Content** , or re-run the **Pull Content** job to continue importing the remaining assets.  
`General error performing Job Pull Content` (or `400 Bad Request` / `404 Not Found` when pulling from an existing legacy branch) | Attempting to pull a repository branch containing pre-migration legacy configuration files into a Chronicle API-enabled environment. | 

  * Execute a full **Push Content** job from your Chronicle API-enabled environment first to populate the branch with updated configuration files before running any pull jobs.
  * Verify that the integration instance is configured with the correct Chronicle API-enabled branch (see Chronicle API-enabled environment migration).

  
`Playbook '<Playbook_Name>' is assigned to environment(s) that don't exist` | A playbook or block being imported is assigned to an environment or environment group that hasn't been created on the destination instance. | Run **Pull Content** with the **Environments** option selected first, or manually create the missing environment in **Settings > Environments** on the destination instance before pulling playbooks.  
`Commit Author parameter must be in the following format: Name <example@gmail.com>` | The **Commit Author** parameter in the integration instance or job configuration is missing an email address in angle brackets. | Update the **Commit Author** parameter to match the required format: `Name <email@domain.com>` (for example, `GitSync <gitsync@example.com>`).  
`400 Bad Request` or `409 Conflict` when importing ontology mappings | Event mapping rules in the repository conflict with existing platform ontology rules, or were exported using an older GitSync version. | Execute a fresh **Push Mappings** job from your Chronicle API-enabled environment to re-export mapping definitions, or resolve duplicate event mapping rules in **Settings > Ontology > Mapping Rules** before re-running the job.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
