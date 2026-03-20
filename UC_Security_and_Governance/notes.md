### Notes - For Instructor Use Only

- The Managed Identity should be assigned a role of `Storage Blob Data Contributor` on the storage account to allow it to read and write data.

- When created the external ADLS connection, the URL path should be of the format: `abfss://<container>@<storage_account>.dfs.core.windows.net/<path>`