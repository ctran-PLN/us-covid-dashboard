import {Circle,Popup } from 'react-leaflet';
import React from 'react';
import numeral from 'numeral';
const casesTypeColors={
    cases:{
        hex: "#CC1034",
        // rgb:"rgb(204,16,52)",
        // half_op:"rgba(204,16,52,0.5)",
        multiplier:800
    },
    recovered:{
        hex:'#7dd71d',
        // rgb:'rgb(125,215,29,0.5)',
        // half_op:'rgba(125,215,29,0.5)',
        multiplier:1200
    },
    deaths:{
        hex:'#fb4443',
        // rgb:'rgb(251,68,67)',
        // half_op:'rgba(251,68,67,0.5)',
        multiplier:2000
    }
}
export const sortData=(data, caseType)=>{
    const sortedData=[...data];
    sortedData.sort((a,b)=>{
        if(a[caseType]>b[caseType]){
            return -1;
        }else{
            return 1;
        }
    })
    return sortedData

}
export const showDataOnMap=(data,casesType='cases')=>(
    data.map(state=>{
        if (typeof state !== 'undefined'){
          return (
            <Circle center={[state.lat,state.long]}
                fillOpacity={0.4}
                color={casesTypeColors[casesType].hex}
                fillColor={casesTypeColors[casesType].hex}
                radius={
                    Math.sqrt(state[casesType]) * (casesTypeColors[casesType].multiplier / 2)
                }
                >
            </Circle>
          );
        }
    })
);
export const prettyPrintStat=(stat)=>
    stat ? `${numeral(stat).format("0.0a")}`:"+0";
