import React from 'react'
import './../assets/InfoBox.css'
import {Card,CardContent,Typography} from "@material-ui/core"

function InfoBox({title,isDate,total,isRed,active,...props}) {
    let totalCard, formatter;
    if (isDate) {
      formatter = <h4 className={`infoBox_cases ${!isRed && "infoBox__cases--green"}`}>
                      {new Date(total).toDateString("MMM DD, YYYY")}
                  </h4>;
    } else {
      formatter = <h2 className={`infoBox_cases ${!isRed && "infoBox__cases--green"}`}>
                      {total}
                  </h2>;
    }

    return (
        <Card
        onClick={props.onClick}
        className={`infoBox ${active &&'infoBox--selected'} ${isRed && 'infoBox--red'}`}>
            <CardContent>
                <Typography className='infoBox_title' color='textSecondary'>
                    {title}
                </Typography>
                {formatter}
            </CardContent>

        </Card>
    )
}

export default InfoBox
