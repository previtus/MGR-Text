createdb gisdb
psql -d gisdb -c 'CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;'
osm2pgsql --create --database gisdb example_data.osm.pbf -U example_user