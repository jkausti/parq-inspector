ParqInspector
================

ParqInspector is a Parquet viewer for your terminal, built with [Textual](https://github.com/Textualize/textual).

ParqInspector can open local or remote Parquet files and lets you view their contents in a table format.
ParqInspector can since version 2.0 also open Delta tables.


https://github.com/jkausti/parq-inspector/assets/19781820/7ef7657a-0598-4d3e-bab8-3faa8032ff70



👉 Installation
------------

ParqInspector can be installed with pip (or pipx).
```bash
$ pip install parq-inspector
```

👉 Usage
------------

You start ParqInspector simply by running `inspector` from your terminal.

#### Local Files

You can also instantly open a *local file* by using the options `--filepath`
and `--row_limit`, or their short versions `-f` and `-rl`.

```bash
$ inspector --filepath ./data/my_data.parquet --row_limit 500
```

If row limit is not provided, it will get the default value of 200. Be careful, setting the
row limit to a very high value might make the app take a long time to start,
or it may not start at all depending on the size of your data.

#### Remote files

Currently, ParqInspector supports reading remote files from Azure Data Lake
Storage Gen2, Amazon S3 and Google Cloud Storage. In case your storage service
does not support anonymous access, you will need to set environment variables
in order to make ParqInspector able to authenticate to the service. Currently,
ParqInspector supports the following environment variables:

Azure:<br>
`AZURE_STORAGE_ACCOUNT_NAME`<br>
`AZURE_STORAGE_SAS_KEY`<br>
`AZURE_STORAGE_ACCOUNT_KEY`<br>
`AZURE_STORAGE_CLIENT_ID`<br>
`AZURE_STORAGE_CLIENT_SECRET`<br>
`AZURE_STORAGE_TENANT_ID`<br>

AWS:<br>
`AWS_ACCESS_KEY_ID`<br>
`AWS_SECRET_ACCESS_KEY`<br>
`AWS_REGION`<br>
`AWS_DEFAULT_REGION`<br>

GCP:<br>
`GOOGLE_SERVICE_ACCOUNT`<br>
`GOOGLE_SERVICE_ACCOUNT_KEY`<br>

Depending on your method of authentication, not all of the environment variables
need to be set.

Remote files can only be opened through the Settings-pane in the UI.
Pick the correct cloud provider and in the Path-field, you simply put the URL to your file instead of a local path.
ParqInspector uses [polars](https://github.com/pola-rs/polars) under the hood 
to read Parquet files from remote storage, and the supported protocols and
url-variants are determined by what polars supports. See more [here](https://pola-rs.github.io/polars/py-polars/html/reference/api/polars.scan_parquet.html).

👉 Roadmap
------------

[✓] - reading local single Parquet files<br>
[✓] - reading remote single Parquet files<br>
[] - Reading Parquet datasets<br>
[✓] - Reading Delta tables<br>

---

If you encounter any issues, bugs or feel there is a feature missing that would 
be valuable, please create an issue in this repo!
