import React,{useState,useEffect} from 'react';
import {
  MenuItem,
  FormControl,
  Select,
  Card,
  CardContent
} from '@material-ui/core';
import "leaflet/dist/leaflet.css";

import './assets/App.css';
import Map from './components/Map';
import Table from './components/Table';
import InfoBox from './components/InfoBox';
import LineGraph from './components/LineGraph'
import {statesCoords} from './components/statesCoords';

import {sortData,prettyPrintStat} from './components/util';
function App() {
  const APIurl = 'http://localhost:8000/rad/'
  const [USstates,setUSstates]=useState([]);
  const [USAInfo,setUSAInfo]=useState({});
  const [tableData,setTableData]=useState([]);
  const [mapCenter,setMapCenter]=useState({lat:35,lng:-90});
  const [mapZoom,setMapZoom]=useState(4.4);
  const [mapStates,setMapStates]=useState([]);
  const [casesType,setCasesType]=useState('cases');

  const capitalize = (s) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
  }
  const switchTableData = (data,caseType) => {
    const sortedData=sortData(data,caseType);
    setTableData(sortedData);
  }
  const addStatesCoords = (data) => {
    return data.map((st)=>{
              if (st.state in statesCoords){
                return {
                    "state" : st.state,
                    "cases" : st.cases,
                    "deaths" : st.deaths,
                    "lat" : statesCoords[st.state]['lat'],
                    "long" : statesCoords[st.state]['long']
                }
              }
            });
  }
  //fetch daily usa data onload
  useEffect(()=>{
    fetch(APIurl+'get_usa/?today=1')
    .then(response => response.json())
    .then(data => {
        setUSAInfo(data[0]);
    })
  },[]);
  //fetch daily states data onload
  useEffect(
    () => {
      const getStatesData=async()=>{
        await fetch(APIurl+'get_states/?today=1')
        .then((response)=>response.json())
        .then((data)=>{
            //data.forEach(function (e) {console.log(e.state)});
            const us_states=data.map((st)=>(
              {
                name:st.state,
                value:st.cases
              }
            ));
            switchTableData(data, casesType);
            const st_coords = addStatesCoords(data);
            setMapStates(st_coords);
            setUSstates(us_states);
        })
      }
      getStatesData()
      },[]);

  return (
    <div className="app">
     <div className='app_left'>
     <div className="app_header">
     <h1>RAD COVID-19 USA</h1>
     </div>
     <div className="app_stats">
        <InfoBox isRed={false} isDate={true} active={casesType==='Date'}
            title='Date'
            total={USAInfo.date}/>
        <InfoBox isRed={true} active={casesType==='cases'}
            onClick={e=>{setCasesType('cases');
                          switchTableData(tableData, 'cases')}}
            title='Total Cases'
            total={prettyPrintStat(USAInfo.cases)}/>
        <InfoBox isRed={true} active={casesType==='deaths'}
            onClick={e=>{setCasesType('deaths');
                          switchTableData(tableData, 'deaths')}}
            title='Total Deaths'
            total={prettyPrintStat(USAInfo.deaths)}/>
     </div>

      <Map casesType={casesType} USstates={mapStates} center={mapCenter} zoom={mapZoom}/>
      </div>
      <Card className='app_right'>
        <CardContent>
            <h3>{capitalize(casesType)} by States</h3>
            <Table states={tableData} caseType={casesType} />
            <h3 className='app_graphTitle'>USA {casesType} past 120 days</h3>
            <LineGraph className='app_graph' casesType={casesType}/>
        </CardContent>
      </Card>

    </div>
  );
}

export default App;
