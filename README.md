# Data explorer

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

## Quickstart

Run Data explorer with a test dataset:

* `ln -s test config`
* `docker-compose up --build`
* Navigate to `localhost:4400`

To use a different dataset:

* Index your data into an Elasticsearch started by
  `docker run -p 9200:9200 docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.2`. You can use one of the indexers at
  https://github.com/DataBiosphere/data-explorer-indexers, or any other indexer.
* Create a directory named `config` and copy over config files from above step.
  See [example](https://github.com/DataBiosphere/data-explorer-indexers/blob/master/bigquery/config/platinum_genomes)
  here. Specifically:
  * There must be a file named `dataset.json` that has a `name` field. This
    determines the name of the Elasticsearch index.
  * There must be a file named `facet_fields.csv` with the `readable_field_name`
    column filled out.
* `docker-compose up --build`
* Navigate to `localhost:4400`

## Architecture overview

For local development, an nginx reverse proxy is used to get around CORS.

![Architecture overview](https://i.imgur.com/ilh7RF1.png)

## Development

### Updating the API using swagger-codegen

We use [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to
automatically implement the API, as defined in `api/api.yaml`, for the API
server and the UI. Whenever the API is updated, follow these steps to
update the server implementations:

* Clear out existing generated models:
  ```
  rm ui/src/api/src/model/*
  rm api/data_explorer/models/*
  ```
* Regenerate Javascript and Python definitions.
  ```
  java -jar ~/swagger-codegen-cli.jar generate -i api/api.yaml -l python-flask -o api -DsupportPython2=true,packageName=data_explorer
  java -jar ~/swagger-codegen-cli.jar generate -i api/api.yaml -l javascript -o ui/src/api -DuseES6=true
  ```
* Update the server implementations to resolve any broken dependencies on old API definitions or implement additional functionality to match the new specs.

### One-time setup

* Install `swagger-codegen-cli.jar`.

```
# Linux
wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O ~/swagger-codegen-cli.jar
# macOS
brew install swagger-codegen
```

* In `ui/` run `npm install`. This will install tools used during git precommit,
  such as formatting tools.
* [Set up git secrets.](https://github.com/DataBiosphere/data-explorer/tree/master/hooks)

### Formatting

`ui/` is formatted via [Prettier](https://prettier.io/). husky is used to automatically format files upon commit.
