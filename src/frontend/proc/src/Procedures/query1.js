import React, {useEffect, useState} from "react";
import {Box, CircularProgress, Container, FormControl, InputLabel, MenuItem, Select} from "@mui/material";


function query1() {

    const [selectedFlight, setSelectedFlight] = useState("");

    const [procData, setProcData] = useState(null);


    useEffect(() => {
        fetch('http://localhost:20001/api/query1')
        .then ((response)=>response.json())
        .then((procData)=>setProcData(procData));
     
    }, [selectedFlight])

    return (
        <>
            <h1>Voos Mumbai</h1>

            <Container maxWidth="100%"
                       sx={{backgroundColor: 'background.default', padding: "2rem", borderRadius: "1rem"}}>
                <Box>
                    <h2 style={{color: "white"}}>Options</h2>
                    <FormControl fullWidth>
                        <InputLabel id="Flight-select-label">Flight</InputLabel>
                        <Select
                            labelId="Flight-select-label"
                            id="demo-simple-select"
                            value={selectedFlight}
                            label="Flight"
                            onChange={(e, v) => {
                                setSelectedFlight(e.target.value)
                            }}
                        >
                            <MenuItem value={""}><em>None</em></MenuItem>
                            {
                                FLIGHTS.map(c => <MenuItem key={c} value={c}>{c}</MenuItem>)
                            }
                        </Select>
                    </FormControl>
                </Box>
            </Container>

            <Container maxWidth="100%" sx={{
                backgroundColor: 'info.dark',
                padding: "2rem",
                marginTop: "2rem",
                borderRadius: "1rem",
                color: "white"
            }}>
                <h2>Results <small>(PROC)</small></h2>
                {
                    procData ?
                        <ul>
                            {
                                procData.map(data => <li>{data.price}</li>)
                            }
                        </ul> :
                        selectedFlight? <CircularProgress/> : "--"
                }
                
            </Container>
        </>
    );
}

export default query1;
