import os


def get_storage_options(storage: str) -> dict:
    if storage == "azure":
        return get_azure_options()
    elif storage == "aws":
        return get_aws_options()
    elif storage == "gcp":
        return get_gcp_options()
    else:
        return {}


def get_azure_options():
    azure_keys = {
        "azure_storage_account_name": os.getenv("AZURE_STORAGE_ACCOUNT_NAME"),
        "azure_storage_sas_key": os.getenv("AZURE_STORAGE_SAS_KEY"),
        "azure_storage_account_key": os.getenv("AZURE_STORAGE_ACCOUNT_KEY"),
        "azure_storage_client_id": os.getenv("AZURE_STORAGE_CLIENT_ID"),
        "azure_storage_client_secret": os.getenv("AZURE_STORAGE_CLIENT_SECRET"),
        "azure_storage_tenant_id": os.getenv("AZURE_STORAGE_TENANT_ID"),
    }

    keys_to_del = []
    for k, v in azure_keys.items():
        if not v:
            keys_to_del.append(k)

    for key in keys_to_del:
        del azure_keys[key]

    return azure_keys


def get_aws_options():
    aws_keys = {
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_secret_access_key": os.getenv("AWS_SECRET_ACCESS_KEY"),
        "aws_region": os.getenv("AWS_REGION"),
        "aws_default_region": os.getenv("AWS_DEFAULT_REGION"),
    }

    keys_to_del = []
    for k, v in aws_keys.items():
        if not v:
            keys_to_del.append(k)

    for key in keys_to_del:
        del aws_keys[key]

    return aws_keys


def get_gcp_options():
    gcp_keys = {
        "google_service_account": os.getenv("GOOGLE_SERVICE_ACCOUNT"),
        "google_service_account_key": os.getenv("GOOGLE_SERVICE_ACCOUNT_KEY"),
    }

    keys_to_del = []
    for k, v in gcp_keys.items():
        if not v:
            keys_to_del.append(k)

    for key in keys_to_del:
        del gcp_keys[key]

    return gcp_keys
