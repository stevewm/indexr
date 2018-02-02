# Project TODO

Stuff I'd like to work on. Not ordered in any particular way.

## Core Work

- Better app structure
  ~* Docker stuff abstracted out of the main app py~
  ~* Follow best practices (eg /app, /app/routes.py etc)~
- Stats page
  * Info on indexr entries, eg url -> container name, icon, etc
- Admin interface to allow:
  * Theme changes (with list of installed themes)
  * Change settings
- Support for ordering (probably introduce indexr.order label)
- Dockerfile to build a small image
- Logging support
  * For each container found
  * When a label is missing
- Better error handling
  * If one of the labels is missing, this breaks everything presently
- Improve 'basic' theme
  ~* Load services in iframe~
  ~* Persistent icons on top~
  * Hovertext for icons
  * More icons
  * Remove scrollbar from main page, scroll inside iframe

## Nice-to-have

- Sonarr/Radarr Calendar
- SABnzbd/NZBGet download stats
- More themes
