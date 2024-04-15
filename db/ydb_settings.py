import ydb


def get_ydb_pool(ydb_endpoint, ydb_database, timeout=30):
    ydb_driver_config = ydb.DriverConfig(
        ydb_endpoint,
        ydb_database,
        credentials=ydb.credentials_from_env_variables(),
        root_certificates=ydb.load_ydb_root_certificate(),
    )

    ydb_driver = ydb.Driver(ydb_driver_config)
    print(ydb_driver_config)
    with ydb.Driver(ydb_driver_config) as driver:
        try:
            ydb_driver.wait(fail_fast=True, timeout=timeout)
        except TimeoutError:
            print("Connect failed to YDB")
            print("Last reported errors by discovery:")
            print(driver.discovery_debug_details())

    return ydb.SessionPool(ydb_driver)
