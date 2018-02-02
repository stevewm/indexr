# Indexr

Automated homepage creation using Docker labels. Currently POC.

## Use

Label your containers with the following:

- `indexr.enable` Must be set to `true` for Indexr to include it on the page
- `indexr.name` Name of the link 
- `indexr.url` URL the link goes to
- `indexr.icon` Icon of the service (put in `static/icons` directory)

