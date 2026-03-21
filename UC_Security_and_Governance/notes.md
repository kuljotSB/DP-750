## Notes - For Instructor Use Only

### Creating External ADLS Connection for new UC Setup

- The Managed Identity should be assigned a role of `Storage Blob Data Contributor` and `Storage Account Contributor` on the storage account to allow it to read and write data.

- When created the external ADLS connection, the URL path should be of the format: `abfss://<container>@<storage_account>.dfs.core.windows.net/<path>`

- Disable All Blob Soft Deletes on the underlying Storage Account

- When Creating Schema and the Volumes make sure Appropriate Permissions are set for the user accounts using the Volume

### Creating Azure Key Vault Secret Scope

- Set Permission model to `Vault access policy` while creating the key vault in the `Access Permissions Tab`

- In Firewalls and virtual networks set `Allow public access`

- Go to `https://<databricks-instance>#secrets/createScope`
