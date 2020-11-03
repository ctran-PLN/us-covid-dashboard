import React from "react";
import './../assets/Map.css'
import { Map as LeafletMap, TileLayer } from "react-leaflet";
import {showDataOnMap} from './util';

function Map({USstates,casesType,center,zoom}) {
  return (
    <div className="map">
      <LeafletMap center={center} zoom={zoom}>
      <TileLayer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      attribution='$copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      />
      {showDataOnMap(USstates,casesType)}

      </LeafletMap>
    </div>
  );
}

export default Map;
