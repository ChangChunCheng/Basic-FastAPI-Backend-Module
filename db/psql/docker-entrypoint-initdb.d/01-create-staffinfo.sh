#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE EXTENSION "pgcrypto";
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    DROP TABLE IF EXISTS Users;
    CREATE TABLE Users (
        Id  UUID NOT NULL,
        Account VARCHAR(50) PRIMARY KEY,
        Password VARCHAR(256) NOT NULL,
        Name VARCHAR(10) NOT NULL,
        Disable BOOLEAN NOT NULL,
        CreateAt    TIMESTAMP NOT NULL,
        UpdateAt    TIMESTAMP NOT NULL
    );
EOSQL